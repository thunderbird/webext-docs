#!/usr/bin/python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse, glob, json, os, re

DEST_DIR = os.path.dirname(__file__)
PREAMBLE_DIR = os.path.join(DEST_DIR, "preamble")

current_namespace_name = None


def replace_code(string):
    string = string.replace("<em>", "*").replace("</em>", "*")
    string = string.replace("<b>", "**").replace("</b>", "**")
    string = string.replace("<code>", "``").replace("</code>", "``")
    string = string.replace("<var>", "``").replace("</var>", "``")
    return string


def format_member(name, value):
    parts = []

    if (name):
        if value.get("optional", False):
            parts.append("[``%s``]" % name)
        else:
            parts.append("``%s``" % name)

    if "type" in value:
        if value.get("enum") is None:
            parts.append("(%s)" % value["type"])
        else:
            parts.append("(`%s <enum_%s_>`_)" % (value["type"], name))
    elif "$ref" in value:
        if "." in value["$ref"] or current_namespace_name is None:
            parts.append("(:ref:`%s`)" % value["$ref"])
        else:
            parts.append("(:ref:`%s.%s`)" % (current_namespace_name, value["$ref"]))
    elif "choices" in value:
        choices = []
        for choice in value["choices"]:
            if "type" in choice:
                choices.append(choice["type"])
            elif "$ref" in choice:
                choices.append(":ref:`%s.%s`" % (current_namespace_name, choice["$ref"]))
        parts.append("(%s)" % " or ".join(choices))

    if "description" in value:
        parts.append(replace_code(value["description"]))
    
    return " ".join(parts)


def format_enum(name, value):
    if value.get("enum") is None:
        return []

    enum_lines = [
        ".. _enum_%s:" % name,
        "",
        "Values for %s:" % name,
        "",
    ]
    for enum_value in value.get("enum"):
        enum_lines.append("- ``%s``" % enum_value)
    enum_lines.append("")
    return enum_lines


def format_object(name, obj):
    lines = ["- %s" % format_member(name, obj)]
    enum_lines = []

    if obj.get("type", None) == "object" and "properties" in obj:
        lines.append("")
        items = sorted(obj["properties"].items())
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


def format_params(function):
    params = []
    for param in function["parameters"]:
        if param.get("optional", False):
            params.append("[%s]" % param["name"])
        else:
            params.append(param["name"])
    return ", ".join(params)


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


def format_namespace(namespace, manifest_namespace=None):
    global current_namespace_name
    current_namespace_name = namespace["namespace"]
    preamble = os.path.join(PREAMBLE_DIR, current_namespace_name + ".rst")
    if os.path.exists(preamble):
        with open(preamble) as fp_preamble:
            lines = map(lambda l: l.rstrip("\n").decode("utf-8"), fp_preamble.readlines())
            lines.append("")
    else:
        lines = header_1(current_namespace_name)

    if manifest_namespace is not None:
        lines.extend(manifest_namespace)

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
        enum_lines = []

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
                        enum_lines.extend(format_enum(key, value))

                for [key, value] in items:
                    if value.get("optional", False):
                        lines.extend(format_object(key, value))
                        enum_lines.extend(format_enum(key, value))
                lines.append("")

        lines.extend(enum_lines)

    if "functions" in namespace:
        lines.append("")
        lines.extend(header_2("Functions"))
        for function in namespace["functions"]:
            lines.extend([
                "",
                ".. _%s.%s:" % (current_namespace_name, function["name"]),
                "",
            ])
            lines.extend(header_3("%s(%s)" % (function["name"], format_params(function))))

            if "description" in function:
                lines.append(replace_code(function["description"]) + "")

            if len(function["parameters"]):
                lines.append("")
                for param in function["parameters"]:
                    lines.extend(format_object(param["name"], param))
                lines.append("")

    if "events" in namespace:
        lines.append("")
        lines.extend(header_2("Events"))
        for event in namespace["events"]:
            lines.extend([
                "",
                ".. _%s.%s:" % (current_namespace_name, event["name"]),
                "",
            ])
            lines.extend(header_3("%s(%s)" % (event["name"], format_params(event))))

            if "description" in event:
                lines.append(replace_code(event["description"]) + "")

            if len(event["parameters"]):
                lines.append("")
                for param in event["parameters"]:
                    lines.extend(format_object(param["name"], param))
                lines.append("")

            if "returns" in event:
                lines.extend([
                    "",
                    "Event listeners should return:",
                    "",
                ])
                lines.extend(format_object("", event["returns"]))
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

    return "\n".join(lines).encode("utf-8")


def format_manifest_namespace(manifest):
    global current_namespace_name
    current_namespace_name = None

    if "types" not in manifest:
        return

    lines = []
    property_lines = []
    permission_lines = []
    for type_ in manifest["types"]:
        if type_.get("$extend", None) == "WebExtensionManifest":
            for [name, value] in type_["properties"].items():
                property_lines.extend(format_object(name, value))
        if type_.get("$extend", None) == "OptionalPermission":
            for choice in type_["choices"]:
                for value in choice["enum"]:
                    permission_lines.append("- %s" % value)

    if len(property_lines) > 0:
        lines = header_2("Manifest file properties") + property_lines

    if len(permission_lines) > 0:
        lines.extend(header_2("Permissions"))
        lines.extend(permission_lines)
        lines.append("")

    return lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create WebExtensions documentation from schema files"
    )
    parser.add_argument("path", help="""Path to comm-central""")
    parser.add_argument("file", nargs="*",
                        help="""The name of an API to document, which corresponds
                        to a .json file in the schemas directory""")
    args = parser.parse_args()

    src_dir = os.path.join(args.path, "mail/components/extensions/schemas")

    files = []
    if len(args.file) == 0:
        # Do all files.
        for filename in glob.glob(os.path.join(src_dir, "*.json")):
            files.append(os.path.basename(filename)[:-5])
    else:
        for filename in args.file:
            if os.path.exists(os.path.join(src_dir, filename + ".json")):
                files.append(filename)

    if len(files) == 0:
        print "No files found"

    for filename in sorted(files):
        with open(os.path.join(src_dir, filename + ".json")) as fp_input:
            content = fp_input.read()
            content = re.sub(r"(^|\n)//.*", "", content)
            document = json.loads(content)

        manifest_namespace = None
        for namespace in document:
            if namespace["namespace"] == "manifest":
                manifest_namespace = format_manifest_namespace(namespace)
                continue

            with open(os.path.join(DEST_DIR, namespace["namespace"] + ".rst"), "w") as fp_output:
                fp_output.write(format_namespace(namespace, manifest_namespace=manifest_namespace))
                manifest_namespace = None

        if manifest_namespace is not None:
            namespace = {
                "namespace": filename
            }
            with open(os.path.join(DEST_DIR, namespace["namespace"] + ".rst"), "w") as fp_output:
                fp_output.write(format_namespace(namespace, manifest_namespace=manifest_namespace))
