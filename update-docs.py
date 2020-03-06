#!/usr/bin/python
# coding=utf-8
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse, glob, json, os, re

DEST_DIR = os.path.dirname(__file__)
OVERLAY_DIR = os.path.join(DEST_DIR, "overlay")

current_namespace_name = None
unique_id = 1


def merge_objects(a, b):
    if isinstance(a, list):
        for c in a:
            merged = False
            name = c.get("namespace", c.get("name", c.get("id", c.get("$extend"))))
            if name is not None:
                for d in b:
                    if d.get("namespace", d.get("name", d.get("id", d.get("$extend")))) == name:
                        merge_objects(c, d)
                        merged = True
            if not merged:
                b.append(c)
                continue
    elif isinstance(a, dict):
        for [e, f] in a.iteritems():
            if e not in b:
                b[e] = f
                continue
            if e not in ["namespace", "name", "id", "$extend"]:
                merge_objects(f, b[e])
    else:
        print "Unexpected item:", a


def replace_code(string):
    replacements = {
        "<em>": "*",
        "</em>": "*",
        "<b>": "**",
        "</b>": "**",
        "<code>": "``",
        "</code>": "``",
        "<var>": "``",
        "</var>": "``",
        "&mdash;": u"—",
        "\n": "\n\n",
    }
    for [s, r] in replacements.items():
        string = string.replace(s, r)

    return string


def get_type(obj, name):
    if "type" in obj:
        if obj.get("enum") is not None:
            return "`%s <enum_%s_%d_>`_" % (obj["type"], name, unique_id)
        elif obj["type"] == "array":
            if "items" in obj:
                return "array of %s" % get_type(obj["items"], name)
            else:
                return "array"
        elif "isInstanceOf" in obj:
            return "`%s <https://developer.mozilla.org/en-US/docs/Web/API/%s>`_" % \
                (obj["isInstanceOf"], obj["isInstanceOf"])
        else:
            return obj["type"]

    elif "$ref" in obj:
        return link_ref(obj["$ref"])


def link_ref(ref):
    if ref == "extensionTypes.Date":
        return "`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`_"
    for moz_namespace in ["extension.", "extensionTypes."]:
        if ref.startswith(moz_namespace):
            name = ref[len(moz_namespace):]
            url = "https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/%s/%s"
            url = url % (moz_namespace[:-1], name)
            return "`%s <%s>`_" % (name, url)
    if "." in ref or current_namespace_name is None:
        return ":ref:`%s`" % ref
    else:
        return ":ref:`%s.%s`" % (current_namespace_name, ref)


def format_addition(obj):
    if "backported" in obj:
        return "*Added in Thunderbird %s, backported to %s*" % (obj["added"], obj["backported"])
    return "*Added in Thunderbird %s*" % obj["added"]


def format_member(name, value):
    parts = []

    if name:
        type_string = "(%s)"
        if value.get("optional", False):
            parts.append("[``%s``]" % name)
        else:
            parts.append("``%s``" % name)
    else:
        type_string = "%s"

    if value.get("deprecated"):
        type_string += " **Deprecated.**"

    if "type" in value or "$ref" in value:
        parts.append(type_string % get_type(value, name))

    elif "choices" in value:
        choices = []
        for choice in value["choices"]:
            choices.append(get_type(choice, name))
        parts.append(type_string % " or ".join(choices))

    if "description" in value:
        parts.append(replace_code(value["description"]))

    if "added" in value:
        parts.append(format_addition(value))
    
    return " ".join(parts)


def format_enum(name, value):
    if value.get("enum") is None:
        if value.get("items") is not None:
            return format_enum(name, value["items"])
        return []

    enum_lines = reference("enum_%s_%d" % (name, unique_id)) + [
        "Values for %s:" % name,
        "",
    ]
    for enum_value in value.get("enum"):
        enum_lines.append("- ``%s``" % enum_value)
    enum_lines.append("")
    return enum_lines


def format_object(name, obj):
    global unique_id

    if name is None:
        lines = []
    else:
        lines = ["- %s" % format_member(name, obj)]
    enum_lines = []

    if obj.get("type") == "object" and "properties" in obj:
        lines.append("")
        items = sorted(obj["properties"].items())
        for [key, value] in items:
            if not value.get("optional", False):
                lines.append("  - %s" % format_member(key, value))
                enum_lines.extend(format_enum(key, value))
                unique_id += 1

        for [key, value] in items:
            if value.get("optional", False):
                lines.append("  - %s" % format_member(key, value))
                enum_lines.extend(format_enum(key, value))
                unique_id += 1

        lines.append("")

    lines.extend(enum_lines)
    return lines


def format_params(function, callback=None):
    params = []
    for param in function.get("parameters", []):
        if param["name"] == callback:
            continue
        if param.get("optional", False):
            params.append("[%s]" % param["name"])
        else:
            params.append(param["name"])
    return ", ".join(params)


def format_permissions(obj):
    if "permissions" not in obj:
        return []

    lines = []
    name = obj.get("namespace", obj.get("name"))
    for permission in obj["permissions"]:
        if permission.startswith("manifest:"):
            permission = permission[9:]
            text = "  A manifest entry named ``%s`` is required to use ``%s``."
        else:
            text = "  The permission ``%s`` is required to use ``%s``."
        lines.extend([
            "",
            ".. note::",
            "",
            text % (permission, name),
            "",
        ])
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


def header_3(string, label=None):
    return reference(label) + [
        string,
        "-" * len(string),
        "",
    ]


def reference(label):
    if label is None:
        return []

    return [
        ".. _%s:" % label,
        "",
    ]


def format_namespace(namespace, manifest_namespace=None):
    global current_namespace_name, unique_id

    current_namespace_name = namespace["namespace"]
    unique_id = 1
    preamble = os.path.join(OVERLAY_DIR, current_namespace_name + ".rst")
    if os.path.exists(preamble):
        with open(preamble) as fp_preamble:
            lines = map(lambda l: l.rstrip("\n").decode("utf-8"), fp_preamble.readlines())
            lines.append("")
    else:
        lines = header_1(current_namespace_name)

    if "description" in namespace:
        lines.append(replace_code(namespace["description"]))
        lines.append("")

    if manifest_namespace is not None:
        lines.extend(manifest_namespace)

    lines.extend(format_permissions(namespace))

    if "functions" in namespace:
        lines.extend(header_2("Functions"))
        for function in namespace["functions"]:
            async = function.get("async")
            lines.extend(header_3(
                "%s(%s)" % (function["name"], format_params(function, callback=async)),
                label="%s.%s" % (current_namespace_name, function["name"]),
            ))
            enum_lines = []

            if "added" in function:
                lines.append(format_addition(function))
                lines.append("")

            if "description" in function:
                lines.append(replace_code(function["description"]))
                lines.append("")

            if len(function.get("parameters", [])):
                for param in function["parameters"]:
                    if async == param["name"]:
                        if len(param["parameters"]) > 0:
                            function["returns"] = param["parameters"][0]
                    else:
                        lines.extend(format_object(param["name"], param))
                        enum_lines.extend(format_enum(param["name"], param))
                        unique_id += 1

                lines.append("")

            if "returns" in function:
                lines.extend([
                    "Returns a `Promise`_ fulfilled with:",
                    "",
                ])
                lines.extend(format_object("", function["returns"]))
                lines.append("")

            lines.extend(format_permissions(function))
            lines.extend(enum_lines)

        lines.extend([
            ".. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise",
            "",
        ])

    if "events" in namespace:
        lines.append("")
        lines.extend(header_2("Events"))
        for event in namespace["events"]:
            lines.extend(header_3(
                "%s(%s)" % (event["name"], format_params(event)),
                label="%s.%s" % (current_namespace_name, event["name"]),
            ))

            if "added" in event:
                lines.append(format_addition(event))
                lines.append("")

            if "description" in event:
                lines.append(replace_code(event["description"]))
                lines.append("")

            if len(event.get("parameters", [])):
                for param in event["parameters"]:
                    lines.extend(format_object(param["name"], param))
                lines.append("")

            if "returns" in event:
                lines.extend([
                    "Event listeners should return:",
                    "",
                ])
                lines.extend(format_object("", event["returns"]))
                lines.append("")

            lines.extend(format_permissions(event))

    if "properties" in namespace:
        lines.extend(header_2("Properties"))

        for key in sorted(namespace["properties"].iterkeys()):
            lines.extend(header_3(key, label="%s.%s" % (current_namespace_name, key)))
            lines.extend([
                namespace["properties"][key].get("description"),
                "",
            ])

    if "types" in namespace:
        lines.extend(header_2("Types"))

        for type_ in sorted(namespace["types"], key=lambda t: t["id"]):
            enum_lines = []
            lines.extend(header_3(
                type_["id"],
                label="%s.%s" % (current_namespace_name, type_["id"])
            ))

            if "added" in type_:
                lines.append(format_addition(type_))
                lines.append("")

            if "description" in type_:
                lines.append(replace_code(type_["description"]))
                lines.append("")

            if "type" in type_:
                lines.append(get_type(type_, type_["id"]))
                lines.append("")
                enum_lines.extend(format_enum(type_["id"], type_))

            elif "choices" in type_:
                first = True
                for choice in type_["choices"]:
                    if first:
                        first = False
                    else:
                        lines.extend(["", "OR", ""])
                    lines.append("%s: %s" % (get_type(choice, type_["id"]), choice.get("description", "")))
                    if choice["type"] == "object":
                        lines.extend(format_object(None, choice))
                    enum_lines.extend(format_enum(type_["id"], choice))

            if "properties" in type_:
                items = sorted(type_["properties"].items())
                for [key, value] in items:
                    if not value.get("optional", False):
                        lines.extend(format_object(key, value))
                        enum_lines.extend(format_enum(key, value))
                        unique_id += 1

                for [key, value] in items:
                    if value.get("optional", False):
                        lines.extend(format_object(key, value))
                        enum_lines.extend(format_enum(key, value))
                        unique_id += 1
                lines.append("")

            lines.extend(enum_lines)

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
    global current_namespace_name, unique_id
    current_namespace_name = None
    unique_id = 1

    if "types" not in manifest:
        return

    lines = []
    property_lines = []
    permission_lines = []

    permission_strings = {}
    with open(permissions_file) as pf:
        for line in pf:
            if line.startswith("webextPerms.description"):
                parts = line.split("=", 2)
                permission_strings[parts[0][24:]] = parts[1].strip()

    for type_ in manifest["types"]:
        if type_.get("$extend", None) == "WebExtensionManifest":
            for [name, value] in type_["properties"].items():
                property_lines.extend(format_object(name, value))
        if type_.get("$extend", None) in ["OptionalPermission", "Permission"]:
            for choice in type_["choices"]:
                for value in choice["enum"]:
                    if value in permission_strings:
                        permission_lines.append("- %s \"%s\"" % (value, permission_strings[value]))
                    else:
                        permission_lines.append("- %s" % value)

    if len(permission_lines) > 0:
        permission_lines.append("")

    if len(property_lines) > 0:
        lines = header_2("Manifest file properties") + property_lines

    if len(permission_lines) > 0:
        lines.extend(header_2("Permissions"))
        lines.extend(permission_lines)

    return lines


if __name__ == "__main__":
    global src_dir, permissions_file

    parser = argparse.ArgumentParser(
        description="Create WebExtensions documentation from schema files"
    )
    parser.add_argument("path", help="""Path to comm-central""")
    parser.add_argument("file", nargs="*",
                        help="""The name of an API to document, which corresponds
                        to a .json file in the schemas directory""")
    args = parser.parse_args()

    src_dir = os.path.join(args.path, "mail/components/extensions/schemas")
    permissions_file = os.path.join(args.path, "mail/locales/en-US/chrome/messenger/addons.properties")

    files = []
    if len(args.file) == 0:
        # Do all files.
        for filename in glob.glob(os.path.join(src_dir, "*.json")):
            filename = os.path.basename(filename)[:-5]
            if filename not in ["menus_child"]:
                files.append(filename)
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

        if os.path.exists(os.path.join(OVERLAY_DIR, filename + ".json")):
            with open(os.path.join(OVERLAY_DIR, filename + ".json")) as fp_overlay:
                overlay = json.load(fp_overlay)
                merge_objects(overlay, document)
                # print(json.dumps(document, indent=2))

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
