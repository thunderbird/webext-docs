#!/usr/bin/python
# coding=utf-8
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse, glob, json, os, re

DEST_DIR = os.path.dirname(__file__)
OVERLAY_DIR = os.path.join(DEST_DIR, "overlay")

current_namespace_name = None

# enums have been moved inline and are no longer referenced
# unique_id is no longer needed
unique_id = 1
additional_type_defs = {}
additional_type_used = []

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
        "<permission>":":permission:`",
        "</permission>":"`",        
        "&mdash;": u"—",
        "\n": "\n\n",
    }
    for [s, r] in replacements.items():
        string = string.replace(s, r)

    return string


def get_type(obj, name):
    if "type" in obj:
        if obj.get("enum") is not None:
            # enums have been moved inline and are no longer referenced
            #return "`%s <enum_%s_%d_>`_" % (obj["type"], name, unique_id)
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
    global additional_type_used
    if ref == "extensionTypes.Date":
        return "`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`_"
    if ref == "runtime.Port":
        return "`Port <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port>`_"
    if ref == "IconPath":
        return "string"

    for additional_type in additional_type_defs:
        if additional_type['id'] == ref:
            if not ref in additional_type_used:
                additional_type_used.append(ref)
            return ":ref:`%s.%s`" % (current_namespace_name, ref)
    
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
        return "-- [Added in TB %s, backported to TB %s]" % (obj["added"], obj["backported"])
    if "added" in obj:
        return "-- [Added in TB %s]" % obj["added"]
    return ""

def format_changes(obj, inline = False):
    lines = []
    if "changed" in obj:
        for k, v in obj['changed'].items():
            if inline:
                lines.extend([
                    ".. container:: api-member-inline-changes",
                    "",
                    "   :Changes in TB " + k + ": " + replace_code(v),
                    ""])
            else:
                lines.extend(api_header("Changes in Thunderbird " + k, api_member(name=replace_code(v))))
    return lines

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
        parts['description'].append("")
        parts['description'].append(replace_code(value["description"]))
    
    if "changed" in value:
        parts['description'].append("")
        parts['description'].extend(format_changes(value, inline=True))
    
    parts['enum'].extend(format_enum(name, value))
    
    if "added" in value or "changed" in value:
        parts['annotation'] = format_addition(value)
    return parts


def format_enum(name, value):
    if value.get("enum") is None:
        if value.get("items") is not None:
            return format_enum(name, value["items"])
        return []
    
    enum_lines = [""]
    # enums have been moved inline and are no longer referenced
    #enum_lines.extend(["Values for ``%s``:" % name, ""])
    #enum_lines.extend(reference("enum_%s_%d" % (name, unique_id)))
    enum_lines.append("Supported values:")

    for enum_value in value.get("enum"):       
        enum_annotation = None
        if "enumChanges" in value:
            changes = value.get("enumChanges")
            if enum_value in changes:
                enum_annotation = format_addition(changes.get(enum_value))
        enum_lines.extend(api_member(name="``" + enum_value + "``", annotation=enum_annotation))

    return enum_lines
    
def format_object(name, obj, print_description_only = False, print_enum_only = False):
    global unique_id
    # enums have been moved inline and are no longer referenced
    #enum_lines = []
    parts =  get_api_member_parts(name, obj)
  
    #enum_only:        fake header + enum
    #description_only: fake header + description + enum + nested
    #default:          standard header + description enum + nested

    fakeHeader = []
    content = []
    lines = []

    if print_enum_only or print_description_only:
        # fake api-member div structure, so style sheets continue to work
        indent = "      "
        fakeHeader.extend([
            "",
            ".. container:: api-member-node",
            "",
            "   .. container:: api-member-description-only",
        ])
    else:
        indent = "   "
        content.extend(api_member(name=parts['name'], type=parts['type'], annotation=parts['annotation']))

    nested_content = []
    if obj.get("type") == "object" and "properties" in obj:
        items = sorted(obj["properties"].items())
        for [key, value] in items:
            if not value.get("optional", False):
                nested_content.extend(format_object(key, value))
                #nested_content.append("  - %s" % get_api_member_parts(key, value))
                #enum_lines.extend(format_enum(key, value))
                #unique_id += 1

        for [key, value] in items:
            if value.get("optional", False):
                nested_content.extend(format_object(key, value))
                #nested_content.append("  - %s" % get_api_member_parts(key, value))
                #enum_lines.extend(format_enum(key, value))
                #unique_id += 1

    if print_enum_only:
        content.extend([indent + sub for sub in parts['enum']])       
    else:
        content.extend([indent + sub for sub in parts['description']])
        content.extend([indent + sub for sub in parts['enum']])
        content.extend([indent + sub for sub in nested_content])

    if len(content) > 0:
        lines.extend(fakeHeader)
        lines.extend(content)
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


def format_permissions(obj, namespace_obj = None):
    name = obj.get("namespace", obj.get("name"))
    entries = {
        "manifest" : {
            "single" : "A manifest entry named %s is required to use ``%s``.",
            "multiple" : "The manifest entrys %s and %s are required to use ``%s``.",
            "entries" : [],
            },
        "permissions" : {
            "single" : "The permission %s is required to use ``%s``.",
            "multiple" : "The permissions %s and %s are required to use ``%s``.",
            "entries" : []
            },
    }
    
    # read the global permissions first (if provided)
    if namespace_obj and "permissions" in namespace_obj:
        for i in range(0, len(namespace_obj["permissions"])):
            permission = namespace_obj["permissions"][i]
            if permission.startswith("manifest:"):
                continue
            else:
                entries['permissions']['entries'].append(":permission:`%s`" % permission)

    if obj and "permissions" in obj:
        for i in range(0, len(obj["permissions"])):
            permission = obj["permissions"][i]
            if permission.startswith("manifest:"):
                entries['manifest']['entries'].append("``%s``" % permission[9:])
            else:
                entries['permissions']['entries'].append(":permission:`%s`" % permission)

    
    lines = []
    # if a namespace_obj is provided, we only print a list of required permissions
    # including the permission required by the namespace itself
    # manifest entries are ignored
    if namespace_obj:
        content = []
        for permission in entries['permissions']['entries']:
            content.append("- %s" % permission)
        if len(content)>0:
            lines.extend(api_header("Required permissions", content))
    else:
        for entrytype in ['manifest', 'permissions']:
            entry = entries[entrytype]
            text = ""
            if len(entry['entries']) == 0:
                continue
            elif len(entry['entries']) == 1:
                text = entry['single'] % (entry['entries'][0], name)
            else:
                last = entry['entries'].pop()
                text = entry['multiple'] % (", ".join(entry['entries']), last, name)
                
            lines.extend([
                "",
                ".. rst-class:: api-permission-info",
                "",
                ".. note::",
                "",
                "   " + text,
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

def api_member(name=None, type=None, annotation=None, description=[]):
    lines = [
        "",
        ".. api-member::",
    ]    
    if name:
        lines.append("   :name: " + name)
    if type:
        lines.append("   :type: " + type)
    if annotation:
        lines.append("   :annotation: " + annotation)
    if description and len(description)>0:
        lines.append("")
        for line in description:
            lines.append("   " + line)
    return lines

def api_header(label, content = [], annotation=None):
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
    global unique_id, additional_type_used

    lines = []
    lines.extend([
        "",
        ".. _%s_api:" % current_namespace_name,
        ""]);

    #unique_id = 1
    preamble = os.path.join(OVERLAY_DIR, current_namespace_name + ".rst")
    if os.path.exists(preamble):
        with open(preamble) as fp_preamble:
            lines.extend(map(lambda l: l.rstrip("\n").decode("utf-8"), fp_preamble.readlines()))
            lines.append("")
    else:
        lines.extend(header_1(current_namespace_name))

    lines.extend([
        "",
        ".. role:: permission",
        ""]);
    
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
                
            if "changed" in function:
                lines.extend(format_changes(function))

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
                        #unique_id += 1
                
                if len(content) > 0:
                    lines.extend(api_header("Parameters", content))

            if "returns" in function:
                content = []
                content.extend(format_object("", function["returns"]))
                content.append("")
                content.append(".. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise")
                lines.extend(api_header("Return type (`Promise`_)", content))

            lines.extend(format_permissions(function, namespace))
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

            if "changed" in event:
                lines.extend(api_header("API changes", format_changes(event)))

            if len(event.get("parameters", [])):
                content = []
                for param in event["parameters"]:
                    content.extend(format_object(param["name"], param))
                lines.extend(api_header("Parameters for event listeners", content))

            if "returns" in event:
                lines.extend(api_header("Expected return value of event listeners", format_object("", event["returns"])))

            lines.extend(format_permissions(event, namespace))

    # loop over own type defs and additional type defs   
    for run in range(2):
        type_lines = []
        type_header = []
        typegroup = None

        if run == 0:
            if "types" in namespace:
                typegroup = namespace['types']
                type_header.append("")
                type_header.extend(header_2("Types", "api-main-section"))
            else:
                continue
        
        if run == 1:
            typegroup = additional_type_defs
            type_header.append("")
            type_header.extend(header_2("External Types", "api-main-section"))
            type_header.append("The following types are not defined by this API, but by the underlying Mozilla WebExtension code base. They are included here, because there is no other public documentation available.")
            type_header.append("")
            

        for type_ in sorted(typegroup, key=lambda t: t["id"]):
            # skip this type if it is not used
            if run == 1 and not type_['id'] in additional_type_used:
                continue
            
            # enums have been moved inline and are no longer referenced
            #enum_lines = []
            type_lines.extend(header_3(
                type_["name"] if "name" in type_ else type_["id"],
                label="%s.%s" % (current_namespace_name, type_["id"]),
                info=format_addition(type_)
            ))

            if "description" in type_:
                type_lines.append(replace_code(type_["description"]))
                type_lines.append("")

            if "changed" in type_:
                lines.extend(api_header("API changes", format_changes(type_)))

            if "type" in type_:
                if (type_["type"] == "object" and
                        "isInstanceOf" not in type_ and
                        ("properties" in type_ or "functions" in type_)):
                    content = []
                    if "properties" in type_:
                        items = sorted(type_["properties"].items())
                        for [key, value] in items:
                            if not value.get("optional", False):
                                content.extend(format_object(key, value))
                                #enum_lines.extend(format_enum(key, value))
                                #unique_id += 1

                        for [key, value] in items:
                            if value.get("optional", False):
                                content.extend(format_object(key, value))
                                #enum_lines.extend(format_enum(key, value))
                                #unique_id += 1

                    if "functions" in type_:
                        for function in sorted(type_["functions"], key=lambda f: f["name"]):
                            content.append("- ``%s(%s)``" % (function["name"], format_params(function)))
                            description = function.get("description", "")
                            if description:
                                content[-1] += " %s" % description

                    type_lines.extend(api_header("object", content))
                else:
                    type_lines.extend(api_header(get_type(type_, type_["id"]), format_object(None, type_, print_enum_only=True)))
                    
                type_lines.append("")
                #enum_lines.extend(format_enum(type_["id"], type_))

            elif "choices" in type_:
                first = True
                for choice in type_["choices"]:
                    if first:
                        first = False
                    else:
                        type_lines.extend(["", "OR", ""])
                    type_lines.extend(api_header(get_type(choice, type_["id"]), format_object(None, choice, print_description_only=True)))
                    #enum_lines.extend(format_enum(type_["id"], choice))

            type_lines.append("")
            #type_lines.extend(enum_lines)
            
        if len(type_lines) > 0:
            lines.extend(type_header)
            lines.extend(type_lines)

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
    global unique_id
    #unique_id = 1

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
                    description = [permission_strings[value]] if value in permission_strings else None
                    permission_lines.extend(api_member(name=":permission:`" + value + "`", description=description))

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

    # read additional type defs
    additional_type_defs_file = os.path.join(OVERLAY_DIR, "additional_type_defs.json")
    with open(additional_type_defs_file) as fp_input:
        content = fp_input.read()
        content = re.sub(r"(^|\n)//.*", "", content)
        additional_type_defs = json.loads(content)

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
            print("Reading file: " + filename + ".json")
            content = fp_input.read()
            content = re.sub(r"(^|\n)//.*", "", content)
            document = json.loads(content)

        if os.path.exists(os.path.join(OVERLAY_DIR, filename + ".json")):
            with open(os.path.join(OVERLAY_DIR, filename + ".json")) as fp_overlay:
                overlay = json.load(fp_overlay)
                merge_objects(overlay, document)
                # print(json.dumps(document, indent=2))

        manifest_namespace = None
        # get all namespaces defined in the current file
        namespaces = {}
        for namespace in document:
            namespaces[namespace["namespace"]] = namespace 

        # Loop thru all namespaces/pages and evaluate the manifest for EACH namespace
        # in case we need to put global types (without external doc) used in the
        # manifest local in this page 
        for namespace in document:
            if namespace["namespace"] == "manifest":
                continue

            additional_type_used = []
            current_namespace_name = namespace["namespace"]

            if "manifest" in namespaces:
                manifest_namespace = format_manifest_namespace(namespaces["manifest"])
                
            with open(os.path.join(DEST_DIR, namespace["namespace"] + ".rst"), "w") as fp_output:
                fp_output.write(format_namespace(namespace, manifest_namespace=manifest_namespace))
