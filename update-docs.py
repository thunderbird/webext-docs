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
            if isinstance(c, dict):
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
            if e not in b or e in ["description"]:
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
        "<codeblock>": " ::\n\n",
        "</codeblock>": "\n\n",
        "<var>": "``",
        "</var>": "``",
        "&mdash;": u"—",
        "\n": "\n\n",
    }
    for [s, r] in replacements.items():
        string = string.replace(s, r)

    return string


def get_type(obj, name, use_enum_ref = False):
    if "type" in obj:
        if obj.get("enum") is not None:
            if use_enum_ref:
                return "`%s <enum_%s_%d_>`_" % (obj["type"], name, unique_id)
            else:
                return "`%s`" % (obj["type"])
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
    if "changed" in obj:
        return "-- [Changed in TB %s]" % obj["changed"]
    if "backported" in obj:
        return "-- [Added in TB %s, backported to TB %s]" % (obj["added"], obj["backported"])
    if "added" in obj:
        return "-- [Added in TB %s]" % obj["added"]
    return ""

def get_api_member_parts(name, value):
    parts = {
        "name" : "",
        "type" : "",
        "annotation" : "",
        "description" : [],
        "enum" : [],
    }

    if name:
        type_string = "(%s)"
        if value.get("optional", False):
            parts['name'] = "[``%s``]" % name
        else:
            parts['name'] = "``%s``" % name
    else:
        type_string = "%s"

    if "unsupported" in value:
        type_string += " **Unsupported.**"
    elif "deprecated" in value:
        type_string += " **Deprecated.**"

    if "type" in value or "$ref" in value:
        parts['type'] = type_string % get_type(value, name)
    elif "choices" in value:
        choices = []
        for choice in value["choices"]:
            choices.append(get_type(choice, name))
        parts['type'] = type_string % " or ".join(choices)

    if "description" in value:
        parts['description'] = [replace_code(value["description"])]
    
    parts['enum'].extend(format_enum(name, value))
    if len(parts['enum']) > 0:
        if len(parts['description']) > 0:
            parts['description'].append("")
        parts['description'].extend(parts['enum'])

    if "added" in value or "changed" in value:
        parts['annotation'] = format_addition(value)
    return parts


def format_enum(name, value, use_enum_ref = False):
    if value.get("enum") is None:
        if value.get("items") is not None:
            return format_enum(name, value["items"])
        return []
    
    enum_lines = []
    if use_enum_ref:
        enum_lines.extend(["Values for ``%s``:" % name, ""])
        enum_lines.extend(reference("enum_%s_%d" % (name, unique_id)))
    else:
        enum_lines.extend(["Allowed values:", ""])

    for enum_value in value.get("enum"):
        enum_lines.append(".. api-member::")
        enum_lines.append("   :name: ``" + enum_value + "``");
        if "enumChanges" in value:
            changes = value.get("enumChanges")
            if enum_value in changes:
                enum_lines.append("   :annotation: " + format_addition(changes.get(enum_value)))
        enum_lines.append("")

    return enum_lines


def format_object(name, obj, print_description_only = False, print_enum_only = False):
    global unique_id
    # enums have been moved inline and are no longer referenced
    #enum_lines = []
    lines = []
    parts =  get_api_member_parts(name, obj)

    if print_enum_only or print_description_only:
        part = 'description' if print_description_only else 'enum'
        if not len(parts[part]) > 0:
            return []
            
        # fake api-member structure, so style sheets continue to work
        lines.extend([
            "",
            ".. container:: api-member-node",
            "",
            "   .. container:: api-member-description",
            "",
        ])
        for line in parts[part]:
            lines.append("      " + line)
        return lines

    lines.extend([
        "",
        ".. api-member::",
        "   :name: " + parts['name'],
        "   :type: " + parts['type'],
        "   :annotation: " + parts['annotation'],
    ])    
    if len(parts['description']):
        lines.append(""),
        for line in parts['description']:
            lines.append("   " + line)
        
    if obj.get("type") == "object" and "properties" in obj:
        lines.append("")
        items = sorted(obj["properties"].items())
        for [key, value] in items:
            if not value.get("optional", False):
                lines.extend(["   " + sub for sub in format_object(key, value)] )
                #lines.append("  - %s" % get_api_member_parts(key, value))
                #enum_lines.extend(format_enum(key, value))
                #unique_id += 1

        for [key, value] in items:
            if value.get("optional", False):
                lines.extend(["   " + sub for sub in format_object(key, value)] )
                #lines.append("  - %s" % get_api_member_parts(key, value))
                #enum_lines.extend(format_enum(key, value))
                #unique_id += 1


    lines.append("")
    #lines.extend(enum_lines)
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


def format_permissions(obj, use_info_box=True):
    if "permissions" not in obj:
        return []

    lines = []
    manifest_entries = []
    permission_entries = []
    text = ""
    
    name = obj.get("namespace", obj.get("name"))
    if len(obj["permissions"]) == 1:
        permission = obj["permissions"][0]
        if permission.startswith("manifest:"):
            permission = permission[9:]
            text = "  A manifest entry named ``%s`` is required to use ``%s``." % (permission, name)
            manifest_entries.append(permission)
        else:
            text = "  The permission ``%s`` is required to use ``%s``." % (permission, name)
            permission_entries.append(permission)
    else:
        permissions = ""
        for i in range(0, len(obj["permissions"])):
            permission = obj["permissions"][i]
            permission_entries.append(permission)           
            if i > 0:
                if i + 1 == len(obj["permissions"]):
                    permissions += " and "
                else:
                    permissions += ", "
            permissions += "``%s``" % permission
        text = "  The permissions %s are required to use ``%s``." % (permissions, name)

    if use_info_box:
        lines.extend([
            "",
            ".. rst-class:: api-permission-info",
            "",
            ".. note::",
            "",
            text,
            "",
        ])        
    else:
        content = []
        for i in range(0, len(permission_entries)):
            content.append("- ``%s``" % permission_entries[i])
        lines.extend(api_entry("Required permissions", content))

    return lines


def header_1(string):
    return [
        "=" * len(string),
        string,
        "=" * len(string),
        "",
    ]

def header_2(string, classnames=""):
    return [
        ".. rst-class:: " + classnames,
        "",
        string,
        "=" * len(string),
        "",
    ]

def header_3(string, label=None, info=""):
    # The api-section-annotation-hack directive attaches the anotation to the preeding section
    # header, closes standard section div and opens api-section-body div
    return reference(label) + [
        string,
        "-" * len(string),
        "",
        ".. api-section-annotation-hack:: " + info,
        "",
    ]

def api_entry(label, content = [], annotation=None):
    lines = [
        "",
        ".. api-header::",
        "   :label: " + label,
    ]
    if annotation:
        lines.append("   :annotation: " + annotation)
    
    lines.append("")
    if len(content):
        for line in content:
            lines.append("   " + line)
        lines.append("")

    return lines
    
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
        lines.append("")
        lines.extend(header_2("Functions", "api-main-section"))
        for function in namespace["functions"]:
            async = function.get("async")
            lines.extend(header_3(
                "%s(%s)" % (function["name"], format_params(function, callback=async)),
                label="%s.%s" % (current_namespace_name, function["name"]),
                info=format_addition(function)
            ))
            # enums have been moved inline and are no longer referenced
            #enum_lines = []

            if "description" in function:
                lines.append(replace_code(function["description"]))
                lines.append("")

            if len(function.get("parameters", [])) > 0:
                content = []
                for param in function["parameters"]:
                    if async == param["name"]:
                        # used for callback type
                        if len(param["parameters"]) > 0:
                            function["returns"] = param["parameters"][0]
                    else:
                        content.extend(format_object(param["name"], param))
                        #enum_lines.extend(format_enum(param["name"], param))
                        unique_id += 1
                
                if len(content) > 0:
                    lines.extend(api_entry("Parameters", content))

            if "returns" in function:
                content = []
                content.extend(format_object("", function["returns"]))
                content.append("")
                content.append(".. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise")
                lines.extend(api_entry("Return type (`Promise`_)", content))

            lines.extend(format_permissions(function, use_info_box=False))
            #lines.extend(enum_lines)
            

    if "events" in namespace:
        lines.append("")
        lines.extend(header_2("Events", "api-main-section"))
        for event in namespace["events"]:
            lines.extend(header_3(
                "%s(%s)" % (event["name"], format_params(event)),
                label="%s.%s" % (current_namespace_name, event["name"]),
                info=format_addition(event)
            ))

            if "description" in event:
                lines.append(replace_code(event["description"]))
                lines.append("")

            if len(event.get("parameters", [])):
                content = []
                for param in event["parameters"]:
                    content.extend(format_object(param["name"], param))
                lines.extend(api_entry("Parameters for event listeners", content))

            if "returns" in event:
                lines.extend(api_entry("Expected return value of event listeners", format_object("", event["returns"])))

            lines.extend(format_permissions(event, use_info_box=False))

    if "types" in namespace:
        lines.append("")
        lines.extend(header_2("Types", "api-main-section"))

        for type_ in sorted(namespace["types"], key=lambda t: t["id"]):
            # enums have been moved inline and are no longer referenced
            #enum_lines = []
            lines.extend(header_3(
                type_["id"],
                label="%s.%s" % (current_namespace_name, type_["id"]),
                info=format_addition(type_)
            ))

            if "description" in type_:
                lines.append(replace_code(type_["description"]))
                lines.append("")

            if "type" in type_:
                if (type_["type"] == "object" and
                        "isInstanceOf" not in type_ and
                        ("properties" in type_ or "functions" in type_)):
                    content = [];
                    if "properties" in type_:
                        items = sorted(type_["properties"].items())
                        for [key, value] in items:
                            if not value.get("optional", False):
                                content.extend(format_object(key, value))
                                #enum_lines.extend(format_enum(key, value))
                                unique_id += 1

                        for [key, value] in items:
                            if value.get("optional", False):
                                content.extend(format_object(key, value))
                                #enum_lines.extend(format_enum(key, value))
                                unique_id += 1

                    if "functions" in type_:
                        for function in sorted(type_["functions"], key=lambda f: f["name"]):
                            content.append("- ``%s(%s)``" % (function["name"], format_params(function)))
                            description = function.get("description", "")
                            if description:
                                content[-1] += " %s" % description

                    lines.extend(api_entry("object", content))
                else:
                    lines.extend(api_entry(get_type(type_, type_["id"]), format_object(None, type_, print_enum_only=True)))
                    
                lines.append("")
                #enum_lines.extend(format_enum(type_["id"], type_))

            elif "choices" in type_:
                first = True
                for choice in type_["choices"]:
                    if first:
                        first = False
                    else:
                        lines.extend(["", "OR", ""])
                    lines.extend(api_entry(get_type(choice, type_["id"]), format_object(None, choice, print_description_only=True)))
                    #enum_lines.extend(format_enum(type_["id"], choice))

            lines.append("")
            #lines.extend(enum_lines)

    if "properties" in namespace:
        lines.append("")
        lines.extend(header_2("Properties", "api-main-section"))

        for key in sorted(namespace["properties"].iterkeys()):
            lines.extend(header_3(key, label="%s.%s" % (current_namespace_name, key)))
            lines.extend([
                namespace["properties"][key].get("description"),
                "",
            ])


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
        if type_.get("$extend", None) in [
            "OptionalPermission",
            "OptionalPermissionNoPrompt",
            "Permission",
            "PermissionNoPrompt"
        ]:
            for choice in type_["choices"]:
                for value in choice["enum"]:
                    permission_lines.append(".. api-member::")
                    permission_lines.append("   :name: ``" + value + "``");
                    if value in permission_strings:
                        permission_lines.append("");
                        permission_lines.append("   " + permission_strings[value])               

    if len(permission_lines) > 0:
        permission_lines.append("")

    if len(property_lines) > 0:
        lines = header_2("Manifest file properties", "api-main-section") + property_lines

    if len(permission_lines) > 0:
        lines.extend(header_2("Permissions", "api-main-section"))
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

        for namespace in document:
            if namespace["namespace"] == "manifest":
                continue

            with open(os.path.join(DEST_DIR, namespace["namespace"] + ".rst"), "w") as fp_output:
                fp_output.write(format_namespace(namespace, manifest_namespace=manifest_namespace))
