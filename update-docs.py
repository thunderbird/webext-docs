#!/usr/bin/python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse, glob, json, os, re

DEST_DIR = os.path.dirname(__file__)
PREAMBLE_DIR = os.path.join(DEST_DIR, "preamble")
SRC_DIR = "/home/geoff/mozilla/mozilla-central/comm/mail/components/extensions/schemas"

current_namespace_name = None


def replace_code(string):
    string = string.replace("<em>", "*").replace("</em>", "*")
    string = string.replace("<b>", "**").replace("</b>", "**")
    string = string.replace("<code>", "``").replace("</code>", "``")
    string = string.replace("<var>", "``").replace("</var>", "``")
    return string


def format_member(key, value):
    parts = []

    if value.get("optional", False):
        parts.append("[``%s``]" % key)
    else:
        parts.append("``%s``" % key)

    if "type" in value:
        if value.get("enum") is None:
            parts.append("(%s)" % value["type"])
        else:
            parts.append("(`%s <enum_%s_>`_)" % (value["type"], key))
    elif "$ref" in value:
        if "." in value["$ref"]:
            parts.append("(:ref:`%s`)" % value["$ref"])
        else:
            parts.append("(:ref:`%s.%s`)" % (current_namespace_name, value["$ref"]))

    if "description" in value:
        parts.append(replace_code(value["description"]))
    
    return " ".join(parts)


def format_enum(key, value):
    if value.get("enum") is None:
        return []

    enum_lines = [
        ".. _enum_%s:" % key,
        "",
        "Values for %s:" % key,
        "",
    ]
    for enum_value in value.get("enum"):
        enum_lines.append("- ``%s``" % enum_value)
    enum_lines.append("")
    return enum_lines


def format_object(name, prop):
    lines = ["- %s" % format_member(name, prop)]
    enum_lines = []

    if prop.get("type", None) == "object" and "properties" in prop:
        lines.append("")
        items = sorted(prop["properties"].items())
        for [key, value] in items:
            if not value.get("optional", False):
                lines.append("  - %s" % format_member(key, value))
                enum_lines.extend(format_enum(key, value))

        for [key, value] in items:
            if value.get("optional", False):
                lines.append("  - %s" % format_member(key, value))
                enum_lines.extend(format_enum(key, value))

        lines.append("")

    lines.extend(enum_lines)
    return lines


def header_1(string):
    return [
        "=" * len(string),
        string,
        "=" * len(string),
        "",
    ]


def header_2(string):
    return [
        string,
        "=" * len(string),
        "",
    ]


def header_3(string):
    return [
        string,
        "-" * len(string),
        "",
    ]


def format_namespace(namespace):
    global current_namespace_name
    current_namespace_name = namespace["namespace"]
    preamble = os.path.join(PREAMBLE_DIR, current_namespace_name + ".rst")
    if os.path.exists(preamble):
        with open(preamble) as fp_preamble:
            lines = map(lambda l: l.rstrip("\n"), fp_preamble.readlines())
            lines.append("")
    else:
        lines = header_1(current_namespace_name)

    if "description" in namespace:
        lines.append(replace_code(namespace["description"]))

    if "permissions" in namespace:
        for permission in namespace["permissions"]:
            lines.extend([
                ".. note::",
                "",
                "  The permission ``%s`` is required to use ``%s``." % (permission, current_namespace_name),
                "",
            ])

    if "types" in namespace:
        lines.append("")
        lines.extend(header_2("Types"))

        for type_ in namespace["types"]:
            lines.extend([
                "",
                ".. _%s.%s:" % (current_namespace_name, type_["id"]),
                "",
            ])
            lines.extend(header_3(type_["id"]))

            if "description" in type_:
                lines.append(replace_code(type_["description"]))

            if "properties" in type_:
                lines.append("")
                items = sorted(type_["properties"].items())
                for [key, value] in items:
                    if not value.get("optional", False):
                        lines.extend(format_object(key, value))

                for [key, value] in items:
                    if value.get("optional", False):
                        lines.extend(format_object(key, value))
                lines.append("")

    if "functions" in namespace:
        lines.append("")
        lines.extend(header_2("Functions"))
        for function in namespace["functions"]:
            params = []
            for param in function["parameters"]:
                if param.get("optional", False):
                    params.append("[%s]" % param["name"])
                else:
                    params.append(param["name"])
            lines.append("")
            lines.extend(header_3("%s(%s)" % (function["name"], ", ".join(params))))

            if "description" in function:
                lines.append(replace_code(function["description"]) + "")

            if len(params):
                lines.append("")
                for param in function["parameters"]:
                    lines.extend(format_object(param["name"], param))
                lines.append("")

    if "events" in namespace:
        lines.append("")
        lines.extend(header_2("Events"))
        for event in namespace["events"]:
            lines.append("")
            lines.extend(header_3(event["name"]))

            if "description" in event:
                lines.append(replace_code(event["description"]) + "")

            if len(event["parameters"]):
                lines.append("")
                for param in event["parameters"]:
                    lines.extend(format_object(param["name"], param))
                lines.append("")

    index = 0
    previous = ""
    while index < len(lines):
        if lines[index] == "" and previous == "":
            del lines[index]
        else:
            previous = lines[index]
            index += 1

    if lines[-1] != "":
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create WebExtensions documentation from schema files"
    )
    parser.add_argument("-a", "--all", dest="all", action="store_true",
                        help="Recreate all documentation")
    parser.add_argument("file", nargs="*",
                        help="""The name of an API to document, which corresponds
                        to a .json file in the schemas directory""")
    args = parser.parse_args()

    if (not args.file and not args.all) or (args.file and args.all):
        print "You must specify either -a or a file"
        exit(1)

    files = []
    if args.all:
        for filename in glob.glob(os.path.join(SRC_DIR, "*.json")):
            files.append(os.path.basename(filename)[:-5])
    else:
        for filename in args.file:
            if os.path.exists(os.path.join(SRC_DIR, filename + ".json")):
                files.append(filename)

    if len(files) == 0:
        print "No files found"

    for filename in sorted(files):
        with open(os.path.join(SRC_DIR, filename + ".json")) as fp_input:
            content = fp_input.read()
            content = re.sub(r"(^|\n)//.*", "", content)
            document = json.loads(content)

        for namespace in document:
            if namespace["namespace"] == "manifest":
                continue

            with open(os.path.join(DEST_DIR, namespace["namespace"] + ".rst"), "w") as fp_output:
                fp_output.write(format_namespace(namespace))
