#!/usr/bin/python
# coding=utf-8
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse, glob, json, os, re

DEST_DIR = os.path.dirname(__file__)
OVERLAY_DIR = os.path.join(DEST_DIR, "overlay")
MV = 3

current_namespace = None

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
            # choices will be replaced completely as specified
            if e in ["choices"]:
                b[e] = f;
                continue

            # merge existing dicts and lists (former restrictions are a subset)
            if e in b and (isinstance(f, list) or isinstance(f, dict)): # and e not in ["namespace", "name", "id", "$extend"]
                merge_objects(f, b[e])
                continue

            # allow new entries or overrides of descriptions and types
            if e not in b or e in ["description", "$ref", "type"]:
                if (e in b and e in ["description"]):
                    print("Replacing Description")
                    print("  comm-central: " + b[e])
                    print("  overlay file: " + f)
                    print("")
                
                # allow to replace a $ref by a type
                if e == "type" and "$ref" in b:
                    del b["$ref"]

                # allow to replace a type by a ref
                if e == "$ref" and "type" in b:
                    del b["type"]
                
                b[e] = f
                continue
                
    else:
        print "Unexpected item:", a


def replace_code(string):
    replacements = {
        "<em>": "*",
        "</em>": "*",
        "<b>": "**",
        "</b>": "**",
        "<code>":":code:`",
        "</code>":"`",
        "<codeblock>": "\n\n::\n\n  ",
        "</codeblock>": "\n\n",
        "<literalinclude>": "\n\n.. literalinclude:: ",
        "</literalinclude>": "\n\n",
        "<lang>": "\n  :language: ",
        "</lang>": "",
        "<var>": "``",
        "</var>": "``",
        "<permission>":":permission:`",
        "</permission>":"`",
        "<value>":":value:`",
        "</value>":"`",
        "&mdash;": u"—",
        "\n": "\n\n",
        "<li>": "\n\n* ",

        "|link-input-encoding|": "https://developer.mozilla.org/en-US/docs/Web/API/Encoding_API/Encodings",
        "|link-ui-elements|": "https://developer.thunderbird.net/add-ons/mailextensions/supported-ui-elements#menu-items",
        "|link-mdn-icon-size|": "https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action#choosing_icon_sizes",
        "|link-css-color-string|": "https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#color_keywords",
        "|link-mdn-browser-styles|": "https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles",
        "|link-legacy-properties|":"https://searchfox.org/comm-central/rev/8a1ae67088acf237dab2fd704db18589e7bf119e/mailnews/addrbook/modules/VCardUtils.jsm#295-334",
        "|link-user-input-restrictions|": "https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions",
        "|link-content-type|": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type",
        "|link-contextmenu-event|": "https://developer.mozilla.org/en-US/docs/Web/API/Element/contextmenu_event",
        "|link-binary-string|": "https://developer.mozilla.org/en-US/docs/Web/API/DOMString/Binary",
        "|link-content-scripts|": "https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts",
        "|link-commands-shortcuts|": "https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/commands#shortcut_values",
        "|link-runtime-last-error|": "https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError",
        "|link-runtime-on-connect|": "https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect",
        "|link-runtime-on-message|": "https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage",
        "|link-match-patterns|": "https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns",

        "|DateTimeFormat|": "`Intl.DateTimeFormat <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat>`__",
        "|File|": "`File <https://developer.mozilla.org/docs/Web/API/File>`__",
        "|Canvas|": "`canvas <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas>`__",
        "|ImageData|": "`ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__",
    }
    for [s, r] in replacements.items():
        string = string.replace(s, r)

    return string


def get_type(obj, name):
    if "type" in obj:
        if obj.get("enum") is not None:
            # enums have been moved inline and are no longer referenced
            #return "`%s <enum_%s_%d_>`__" % (obj["type"], name, unique_id)
            return "`%s`" % (obj["type"])
        elif obj["type"] == "array":
            if "items" in obj:
                if "choices" in obj["items"]:
                    choices = []
                    for choice in obj["items"]["choices"]:
                        choices.append(get_type(choice, name))
                    return "array of %s" % " or ".join(choices)
                else:
                    return "array of %s" % get_type(obj["items"], name)
            else:
                return "array"
        elif "isInstanceOf" in obj:
            return "`%s <https://developer.mozilla.org/en-US/docs/Web/API/%s>`__" % \
                (obj["isInstanceOf"], obj["isInstanceOf"])
        else:
            return obj["type"]

    elif "$ref" in obj:
        return link_ref(obj["$ref"])


def link_ref(ref):
    global additional_type_used
    if ref == "extensionTypes.File":
        return "`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__"
    if ref == "extensionTypes.Date":
        return "`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__"
    if ref == "runtime.Port":
        return "`Port <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port>`__"
    if ref.startswith("manifest."):
        ref = ref[9:]
    if ref == "IconPath" or ref.endswith(".IconPath"):
        ref = "IconPath"

    for additional_type in additional_type_defs:
        if additional_type['id'] == ref:
            if not ref in additional_type_used:
                additional_type_used.append(ref)
            return ":ref:`%s.%s`" % (current_namespace["namespace"], ref)
    
    for moz_namespace in ["extension.", "extensionTypes."]:
        if ref.startswith(moz_namespace):
            name = ref[len(moz_namespace):]
            url = "https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/%s/%s"
            url = url % (moz_namespace[:-1], name)
            return "`%s <%s>`__" % (name, url)
    if "manifest." in ref:
        # manifest types are not global and need to be prepended by the current namespace
        return ":ref:`%s.%s`" % (current_namespace["namespace"], ref.replace("manifest.",""))
    elif "." in ref or current_namespace["namespace"] is None:
        return ":ref:`%s`" % ref
    else:
        return ":ref:`%s.%s`" % (current_namespace["namespace"], ref)


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

def format_hints(obj):
    lines = []
    if "hints" in obj:
        lines.extend(replace_code(obj['hints']).split("\n"))
    return lines

def get_api_member_parts(name, value):
    parts = {
        "name" : "",
        "type" : "",
        "annotation" : "",
        "description" : [],
        "enum" : [],
    }

    # The return element is using a fake "_returns" name to get here.
    type_string = "%s"
    if name == "_returns":
        if value.get("optional", False):
            # type_string = "[%s]" activate not yet
            type_string = "%s"
    elif name:
        type_string = "(%s)"
        if value.get("optional", False):
            parts['name'] = "[``%s``]" % name
            type_string = "(%s, optional)"
        else:
            parts['name'] = "``%s``" % name

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
        parts['description'].extend(replace_code(value["description"]).split("\n"))
    
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

    enum_changes = value.get("enumChanges", None)
    for enum_value in value.get("enum"):       
        enum_annotation = None
        enum_description = []
        if enum_changes and enum_value in enum_changes:
            enum_change = enum_changes.get(enum_value)
            enum_annotation = format_addition(enum_change)
            if "description" in enum_change:
                enum_description.extend(replace_code(enum_change.get("description")).split("\n"))
        enum_lines.extend(api_member(name=":value:`" + enum_value + "`", annotation=enum_annotation, description=enum_description))

    return enum_lines
    
def format_object(name, obj, print_description_only = False, print_enum_only = False):
    global unique_id
    # enums have been moved inline and are no longer referenced
    #enum_lines = []
    
    # Cater for MV2/3 differences, pick the correct one and proceed as normal. We
    # do not support individual descriptions of the allowed types.
    if "choices" in obj:
        for choice in obj["choices"]:
            if "min_manifest_version" in choice and choice["min_manifest_version"] > MV:
                continue
            if "max_manifest_version" in choice and choice["max_manifest_version"] < MV:
                continue
            if "type" in choice and "description" in choice:
                for key in choice:
                    obj[key] = choice[key]

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
            if value.get("ignore", False):
                continue
            if not value.get("optional", False):
                nested_content.extend(format_object(key, value))
                #nested_content.append("  - %s" % get_api_member_parts(key, value))
                #enum_lines.extend(format_enum(key, value))
                #unique_id += 1

        for [key, value] in items:
            if value.get("ignore", False):
                continue
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
            "single" : "A manifest entry named %s is required to use ``messenger.%s.*``.",
            "multiple" : "One of the manifest entries %s or %s is required to use ``messenger.%s.*``.",
            "entries" : [],
            },
        "permissions" : {
            "single" : "The permission %s is required to use ``messenger.%s.*``.",
            "multiple" : "One of the permissions %s or %s is required to use ``messenger.%s.*``.",
            "entries" : []
            },
    }
    
    # read the global permissions first (if provided)
    if namespace_obj and "permissions" in namespace_obj:
        permissions = list(dict.fromkeys(namespace_obj["permissions"]))
        permissions.sort()
        for i in range(0, len(permissions)):
            permission = permissions[i]
            if permission.startswith("manifest:"):
                continue
            else:
                entries['permissions']['entries'].append(":permission:`%s`" % permission)

    if obj and "permissions" in obj:
        permissions = list(dict.fromkeys(obj["permissions"]))
        permissions.sort()
        for i in range(0, len(permissions)):
            permission = permissions[i]
            if permission.startswith("manifest:"):
                entries['manifest']['entries'].append(":value:`%s`" % permission[9:])
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


def format_namespace(manifest, namespace):
    global unique_id, additional_type_used

    lines = []
    lines.extend([
        "",
        ".. _%s_api:" % namespace["namespace"],
        ""]);

    #unique_id = 1
    preamble = os.path.join(OVERLAY_DIR, namespace["namespace"] + ".rst")
    if os.path.exists(preamble):
        with open(preamble) as fp_preamble:
            lines.extend(map(lambda l: l.rstrip("\n").decode("utf-8"), fp_preamble.readlines()))
            lines.append("")
    else:
        lines.extend(header_1(namespace["namespace"]))

    lines.extend([
        "",
        ".. role:: permission",
        ""]);

    lines.extend([
        "",
        ".. role:: value",
        ""]);

    lines.extend([
        "",
        ".. role:: code",
        ""]);

    if "description" in namespace:
        lines.extend(replace_code(namespace["description"]).split("\n"))
        lines.append("")

    if manifest is not None:
        lines.extend(format_manifest_namespace(manifest, namespace))

    lines.extend(format_permissions(namespace))

    if "functions" in namespace:
        lines.append("")
        lines.extend(header_2("Functions", "api-main-section"))
        for function in namespace["functions"]:
            async = function.get("async")
            lines.extend(header_3(
                "%s(%s)" % (function["name"], format_params(function, callback=async)),
                label="%s.%s" % (namespace["namespace"], function["name"]),
                info=format_addition(function)
            ))
            # enums have been moved inline and are no longer referenced
            #enum_lines = []

            if "description" in function:
                lines.extend(replace_code(function["description"]).split("\n"))
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
                content.extend(format_object("_returns", function["returns"]))
                content.append("")
                content.append(".. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise")
                lines.extend(api_header("Return type (`Promise`_)", content))

            lines.extend(format_permissions(function, namespace))
            #lines.extend(enum_lines)
            
            if "hints" in function:
                lines.extend(format_hints(function))


            

    if "events" in namespace:
        lines.append("")
        lines.extend(header_2("Events", "api-main-section"))
        for event in namespace["events"]:
            lines.extend(header_3(
                "%s" % (event["name"]), # , (%s)format_params(event)
                label="%s.%s" % (namespace["namespace"], event["name"]),
                info=format_addition(event)
            ))

            if "description" in event:
                lines.extend(replace_code(event["description"]).split("\n"))
                lines.append("")

            if "changed" in event:
                lines.extend(api_header("API changes", format_changes(event)))


            listener = {
                "name": "listener(%s)" % ", ".join(list(map(lambda x : x['name'], event.get("parameters", [])))),
                "description": "A function that will be called when this event occurs."
            }
            content = []
            for param in ([listener] + event.get("extraParameters", [])):
                content.extend(format_object(param["name"], param))
            extraParams = list(map(lambda x : x['name'], event.get("extraParameters", [])))
            lines.extend(api_header(
                "Parameters for %s.addListener(%s)" % (event["name"], ", ".join(["listener"] + extraParams)),
                content
            ))

            if len(event.get("parameters", [])):
                content = []
                for param in event["parameters"]:
                    content.extend(format_object(param["name"], param))
                lines.extend(api_header("Parameters passed to the listener function", content))


            
            if "returns" in event:
                lines.extend(api_header("Expected return value of the listener function", format_object("", event["returns"])))

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
                label="%s.%s" % (namespace["namespace"], type_["id"]),
                info=format_addition(type_)
            ))

            if "description" in type_:
                type_lines.extend(replace_code(type_["description"]).split("\n"))
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
                                content[-1] += " %s" % replace_code(description)

                    type_lines.extend(api_header("object", content))
                else:
                    type_lines.extend(api_header(get_type(type_, type_["id"]), format_object(None, type_, print_enum_only=True)))
                    
                type_lines.append("")
                #enum_lines.extend(format_enum(type_["id"], type_))

            elif "choices" in type_:
                first = True
                for choice in type_["choices"]:
                    if "min_manifest_version" in choice and choice["min_manifest_version"] > MV:
                        continue
                    if "max_manifest_version" in choice and choice["max_manifest_version"] < MV:
                        continue
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
            lines.extend(header_3(key, label="%s.%s" % (namespace["namespace"], key)))
            lines.extend(replace_code(namespace["properties"][key].get("description")).split("\n"))
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

def map_permission_to_key(permission):
    mapping = {
        "accountsRead": "accountsRead",
        "messagesMove": "messagesMove",
    }
    if permission in mapping:
        return mapping[permission]
    return permission

def format_manifest_namespace(manifest, namespace):
    global unique_id
    #unique_id = 1

    if "types" not in manifest:
        return

    lines = []
    property_lines = []
    permission_lines = []

    permission_strings = {}
    for permissions_file in permissions_files:
        with open(permissions_file) as pf:
            for line in pf:
                if line.startswith("webext-perms-description"):
                    parts = line.split("=", 2)
                    permission_strings[parts[0][25:].replace("-", "." ).strip()] = parts[1].strip()

    for type_ in manifest["types"]:
        if type_.get("$extend", None) == "WebExtensionManifest":
            for [name, value] in sorted(type_["properties"].items(), key=lambda t: t[0] if "sort" not in t[1] else t[1]["sort"]):
                property_lines.extend(format_object(name, value))
        if type_.get("$extend", None) in [
            "OptionalPermission",
            "OptionalPermissionNoPrompt",
            "Permission",
            "PermissionNoPrompt"
        ]:
            for choice in type_["choices"]:
                for value in choice["enum"]:
                    if "ignore_permissions" not in namespace or value not in namespace["ignore_permissions"]:
                        description = None
                        if "permissions" in manifest and value in manifest["permissions"] and "description" in manifest["permissions"][value]:
                            description = [manifest["permissions"][value]["description"]]
                        elif map_permission_to_key(value) in permission_strings:
                            description = [permission_strings[map_permission_to_key(value)]]
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
    global src_dir, permissions_files

    parser = argparse.ArgumentParser(
        description="Create WebExtensions documentation from schema files"
    )
    parser.add_argument("path", help="""Path to comm-central""")
    parser.add_argument("file", nargs="*",
                        help="""The name of an API to document, which corresponds
                        to a .json file in the schemas directory""")
    args = parser.parse_args()

    src_dir = os.path.join(args.path, "mail/components/extensions/schemas")
    permissions_files = [
        os.path.join(args.path, "../toolkit/locales/en-US/toolkit/global/extensionPermissions.ftl"),
        os.path.join(args.path, "mail/locales/en-US/messenger/extensionPermissions.ftl")
    ]

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
            if not filename.endswith("_child"):
                files.append(filename)
    else:
        for filename in args.file:
            if os.path.exists(os.path.join(src_dir, filename + ".json")):
                files.append(filename)

    if len(files) == 0:
        print "No files found"

    for filename in sorted(files):
        # Is there a child implementation?
        child = None
        if os.path.exists(os.path.join(src_dir, filename + "_child.json")):
            with open(os.path.join(src_dir, filename + "_child.json")) as fp_child:
                print("Reading file: " + filename + "_child.json")
                childString = fp_child.read()
                childString = re.sub(r"(^|\n)//.*", "", childString)
                child = json.loads(childString)

        with open(os.path.join(src_dir, filename + ".json")) as fp_parent:
            print("Reading file: " + filename + ".json")
            parentString = fp_parent.read()
            parentString = re.sub(r"(^|\n)//.*", "", parentString)
            parent = json.loads(parentString)
            if child is not None:
                document = child
                merge_objects(parent, document)
            else:
                document = parent

        overlays = {}
        if os.path.exists(os.path.join(OVERLAY_DIR, filename + ".json")):
            with open(os.path.join(OVERLAY_DIR, filename + ".json")) as fp_overlay:
                overlay = json.load(fp_overlay)
                for namespace in overlay:
                    overlays[namespace["namespace"]] = namespace 

        # get all namespaces defined in the current file
        namespaces = {}
        for namespace in document:
            namespaces[namespace["namespace"]] = namespace 

        # Loop thru all namespaces/pages and evaluate the manifest for EACH namespace
        # in case we need to put global types (without external doc) used in the
        # manifest local in this page 
        for namespace in document:
            if namespace["namespace"] == "manifest":
                # overlay manifest
                if "manifest" in overlays:
                    merge_objects(overlays["manifest"], namespace)
                
                types = namespace.get("types", list())
                for type in types:
                    # limit to requested manifests version
                    if "$extend" in type and "properties" in type and type["$extend"] == "WebExtensionManifest":
                        properties = type["properties"]
                        for property in properties:
                            if "min_manifest_version" in properties[property] and properties[property]["min_manifest_version"] > MV:
                                types.remove(type)
                            if "max_manifest_version" in properties[property] and properties[property]["max_manifest_version"] < MV:
                                types.remove(type)
                
                continue

            additional_type_used = []
            current_namespace = namespace.copy()
            manifest = namespaces.get("manifest", None)

            # import other namespaces
            if "$import" in namespace:
                current_namespace = namespaces[namespace["$import"]].copy()
                # m-c imports the entire action namespace into the browser_action
                # namespace, which includes its min_manifest_version = 3, which is
                # of course wrong
                for key in ["min_manifest_version", "max_manifest_version"]:
                    if key in current_namespace:
                        del current_namespace[key]
                current_namespace.update(namespace)

            # overlay namespace
            if current_namespace["namespace"] in overlays:
                for entry in overlays[current_namespace["namespace"]]:
                    if entry in ["types", "events", "functions"]:
                        merge_objects(overlays[current_namespace["namespace"]][entry], current_namespace[entry])
                    elif entry in ["permissions", "ignore_permissions"]:
                        current_namespace[entry] = list(overlays[current_namespace["namespace"]][entry])

            # Import selected manifest types into the namespace (used in theme)
            # Decided to select which types should be imported, as sometimes
            # importing all types is not desired.
            if manifest:
                manifestTypes = manifest.get("types", None);
                namespaceTypes = current_namespace.get("types", None)
                if manifestTypes and namespaceTypes:
                    manifestTypeDict = {}
                    for manifestType in manifestTypes:
                            if "id" in manifestType:
                                manifestTypeDict[manifestType["id"]] = manifestType
                    
                    for index, item in enumerate(namespaceTypes):
                        if "$import_from_manifest" in item:
                            namespaceTypes[index] = manifestTypeDict[item["$import_from_manifest"]]

            # limit to requested manifests version
            if "min_manifest_version" in current_namespace and current_namespace["min_manifest_version"] > MV:
                continue
            if "max_manifest_version" in current_namespace and current_namespace["max_manifest_version"] < MV:
                continue

            with open(os.path.join(DEST_DIR, current_namespace["namespace"] + ".rst"), "w") as fp_output:
                fp_output.write(format_namespace(manifest, current_namespace))
