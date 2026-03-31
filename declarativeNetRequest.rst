.. container:: sticky-sidebar

  ≡ declarativeNetRequest API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

=========================
declarativeNetRequest API
=========================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The declarativeNetRequest API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/declarativeNetRequest>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the declarativeNetRequest API to block or modify network requests by specifying declarative rules.

.. rst-class:: api-main-section

Manifest file properties
========================

.. _declarative^net^request.declarative_net_request:

.. api-member::
   :name: [``declarative_net_request``]
   :refid: declarative-net-request-declarative-net-request
   :refname: declarative_net_request
   :type: (object, optional)

   .. _declarative^net^request.declarative_net_request.rule_resources:

   .. api-member::
      :name: ``rule_resources``
      :refid: declarative-net-request-declarative-net-request-rule-resources
      :refname: rule_resources
      :type: (array of object)

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _declarative^net^request.permission.declarative^net^request:

.. api-member::
   :name: :permission:`declarativeNetRequest`
   :refid: declarative-net-request-permission-declarative-net-request
   :refname: declarativeNetRequest

   Block content on any page.

.. _declarative^net^request.permission.declarative^net^request^feedback:

.. api-member::
   :name: :permission:`declarativeNetRequestFeedback`
   :refid: declarative-net-request-permission-declarative-net-request-feedback
   :refname: declarativeNetRequestFeedback

   Read your browsing history.

.. _declarative^net^request.permission.declarative^net^request^with^host^access:

.. api-member::
   :name: :permission:`declarativeNetRequestWithHostAccess`
   :refid: declarative-net-request-permission-declarative-net-request-with-host-access
   :refname: declarativeNetRequestWithHostAccess

   Allows blocking or upgrading requests to hosts for which host permissions have already been granted.

.. rst-class:: api-permission-info

.. note::

   One of the permissions :permission:`declarativeNetRequest` or :permission:`declarativeNetRequestWithHostAccess` is required to use ``messenger.declarativeNetRequest.*``.

.. rst-class:: api-main-section

Functions
=========

.. _declarative^net^request.get^available^static^rule^count:

getAvailableStaticRuleCount()
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Returns the remaining number of static rules an extension can enable

.. api-header::
   :label: Return type (`Promise`_)

   .. _declarative^net^request.get^available^static^rule^count.returns:

   .. api-member::
      :refid: declarative-net-request-get-available-static-rule-count-returns
      :refname: _returns
      :type: integer

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarative^net^request.get^disabled^rule^ids:

getDisabledRuleIds(options)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Returns the list of individual disabled static rules from a given static ruleset id.

.. api-header::
   :label: Parameters

   .. _declarative^net^request.get^disabled^rule^ids.options:

   .. api-member::
      :name: ``options``
      :refid: declarative-net-request-get-disabled-rule-ids-options
      :refname: options
      :type: (object)

      .. _declarative^net^request.get^disabled^rule^ids.options.ruleset^id:

      .. api-member::
         :name: ``rulesetId``
         :refid: declarative-net-request-get-disabled-rule-ids-options-ruleset-id
         :refname: rulesetId
         :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _declarative^net^request.get^disabled^rule^ids.returns:

   .. api-member::
      :refid: declarative-net-request-get-disabled-rule-ids-returns
      :refname: _returns
      :type: array of integer

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarative^net^request.get^dynamic^rules:

getDynamicRules([filter])
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Returns the current set of dynamic rules for the extension.

.. api-header::
   :label: Parameters

   .. _declarative^net^request.get^dynamic^rules.filter:

   .. api-member::
      :name: [``filter``]
      :refid: declarative-net-request-get-dynamic-rules-filter
      :refname: filter
      :type: (:ref:`declarative^net^request.^get^rules^filter`, optional)
      :annotation: -- [Added in TB 127]

      An object to filter the set of dynamic rules for the extension.

.. api-header::
   :label: Return type (`Promise`_)

   .. _declarative^net^request.get^dynamic^rules.returns:

   .. api-member::
      :refid: declarative-net-request-get-dynamic-rules-returns
      :refname: _returns
      :type: array of :ref:`declarative^net^request.^rule`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarative^net^request.get^enabled^rulesets:

getEnabledRulesets()
--------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Returns the ids for the current set of enabled static rulesets.

.. api-header::
   :label: Return type (`Promise`_)

   .. _declarative^net^request.get^enabled^rulesets.returns:

   .. api-member::
      :refid: declarative-net-request-get-enabled-rulesets-returns
      :refname: _returns
      :type: array of string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarative^net^request.get^session^rules:

getSessionRules([filter])
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Returns the current set of session scoped rules for the extension.

.. api-header::
   :label: Parameters

   .. _declarative^net^request.get^session^rules.filter:

   .. api-member::
      :name: [``filter``]
      :refid: declarative-net-request-get-session-rules-filter
      :refname: filter
      :type: (:ref:`declarative^net^request.^get^rules^filter`, optional)
      :annotation: -- [Added in TB 127]

      An object to filter the set of session scoped rules for the extension.

.. api-header::
   :label: Return type (`Promise`_)

   .. _declarative^net^request.get^session^rules.returns:

   .. api-member::
      :refid: declarative-net-request-get-session-rules-returns
      :refname: _returns
      :type: array of :ref:`declarative^net^request.^rule`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarative^net^request.is^regex^supported:

isRegexSupported(regexOptions)
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Checks if the given regular expression will be supported as a 'regexFilter' rule condition.

.. api-header::
   :label: Parameters

   .. _declarative^net^request.is^regex^supported.regex^options:

   .. api-member::
      :name: ``regexOptions``
      :refid: declarative-net-request-is-regex-supported-regex-options
      :refname: regexOptions
      :type: (object)

      .. _declarative^net^request.is^regex^supported.regex^options.regex:

      .. api-member::
         :name: ``regex``
         :refid: declarative-net-request-is-regex-supported-regex-options-regex
         :refname: regex
         :type: (string)

         The regular expresson to check.

      .. _declarative^net^request.is^regex^supported.regex^options.is^case^sensitive:

      .. api-member::
         :name: [``isCaseSensitive``]
         :refid: declarative-net-request-is-regex-supported-regex-options-is-case-sensitive
         :refname: isCaseSensitive
         :type: (boolean, optional)

         Whether the 'regex' specified is case sensitive.

      .. _declarative^net^request.is^regex^supported.regex^options.require^capturing:

      .. api-member::
         :name: [``requireCapturing``]
         :refid: declarative-net-request-is-regex-supported-regex-options-require-capturing
         :refname: requireCapturing
         :type: (boolean, optional)

         Whether the 'regex' specified requires capturing. Capturing is only required for redirect rules which specify a 'regexSubstition' action.

.. api-header::
   :label: Return type (`Promise`_)

   .. _declarative^net^request.is^regex^supported.returns:

   .. api-member::
      :refid: declarative-net-request-is-regex-supported-returns
      :refname: _returns
      :type: object

      .. _declarative^net^request.is^regex^supported.returns.is^supported:

      .. api-member::
         :name: ``isSupported``
         :refid: declarative-net-request-is-regex-supported-returns-is-supported
         :refname: isSupported
         :type: (boolean)

         Whether the given regex is supported

      .. _declarative^net^request.is^regex^supported.returns.reason:

      .. api-member::
         :name: [``reason``]
         :refid: declarative-net-request-is-regex-supported-returns-reason
         :refname: reason
         :type: (:ref:`declarative^net^request.^unsupported^regex^reason`, optional)

         Specifies the reason why the regular expression is not supported. Only provided if 'isSupported' is false.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarative^net^request.test^match^outcome:

testMatchOutcome(request, [options])
------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Checks if any of the extension's declarativeNetRequest rules would match a hypothetical request.

.. api-header::
   :label: Parameters

   .. _declarative^net^request.test^match^outcome.request:

   .. api-member::
      :name: ``request``
      :refid: declarative-net-request-test-match-outcome-request
      :refname: request
      :type: (object)

      The details of the request to test.

      .. _declarative^net^request.test^match^outcome.request.type:

      .. api-member::
         :name: ``type``
         :refid: declarative-net-request-test-match-outcome-request-type
         :refname: type
         :type: (:ref:`declarative^net^request.^resource^type`)

         The resource type of the hypothetical request.

      .. _declarative^net^request.test^match^outcome.request.url:

      .. api-member::
         :name: ``url``
         :refid: declarative-net-request-test-match-outcome-request-url
         :refname: url
         :type: (string)

         The URL of the hypothetical request.

      .. _declarative^net^request.test^match^outcome.request.initiator:

      .. api-member::
         :name: [``initiator``]
         :refid: declarative-net-request-test-match-outcome-request-initiator
         :refname: initiator
         :type: (string, optional)

         The initiator URL (if any) for the hypothetical request.

      .. _declarative^net^request.test^match^outcome.request.method:

      .. api-member::
         :name: [``method``]
         :refid: declarative-net-request-test-match-outcome-request-method
         :refname: method
         :type: (string, optional)

         Standard HTTP method of the hypothetical request.

      .. _declarative^net^request.test^match^outcome.request.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: declarative-net-request-test-match-outcome-request-tab-id
         :refname: tabId
         :type: (integer, optional)

         The ID of the tab in which the hypothetical request takes place. Does not need to correspond to a real tab ID. Default is -1, meaning that the request isn't related to a tab.

   .. _declarative^net^request.test^match^outcome.options:

   .. api-member::
      :name: [``options``]
      :refid: declarative-net-request-test-match-outcome-options
      :refname: options
      :type: (object, optional)

      .. _declarative^net^request.test^match^outcome.options.include^other^extensions:

      .. api-member::
         :name: [``includeOtherExtensions``]
         :refid: declarative-net-request-test-match-outcome-options-include-other-extensions
         :refname: includeOtherExtensions
         :type: (boolean, optional)

         Whether to account for rules from other installed extensions during rule evaluation.

.. api-header::
   :label: Return type (`Promise`_)

   .. _declarative^net^request.test^match^outcome.returns:

   .. api-member::
      :refid: declarative-net-request-test-match-outcome-returns
      :refname: _returns
      :type: object

      .. _declarative^net^request.test^match^outcome.returns.matched^rules:

      .. api-member::
         :name: ``matchedRules``
         :refid: declarative-net-request-test-match-outcome-returns-matched-rules
         :refname: matchedRules
         :type: (array of :ref:`declarative^net^request.^matched^rule`)

         The rules (if any) that match the hypothetical request.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestFeedback`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarative^net^request.update^dynamic^rules:

updateDynamicRules(options)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Modifies the current set of dynamic rules for the extension. The rules with IDs listed in options.removeRuleIds are first removed, and then the rules given in options.addRules are added. These rules are persisted across browser sessions and extension updates.

.. api-header::
   :label: Parameters

   .. _declarative^net^request.update^dynamic^rules.options:

   .. api-member::
      :name: ``options``
      :refid: declarative-net-request-update-dynamic-rules-options
      :refname: options
      :type: (object)

      .. _declarative^net^request.update^dynamic^rules.options.add^rules:

      .. api-member::
         :name: [``addRules``]
         :refid: declarative-net-request-update-dynamic-rules-options-add-rules
         :refname: addRules
         :type: (array of :ref:`declarative^net^request.^rule`, optional)

         Rules to add.

      .. _declarative^net^request.update^dynamic^rules.options.remove^rule^ids:

      .. api-member::
         :name: [``removeRuleIds``]
         :refid: declarative-net-request-update-dynamic-rules-options-remove-rule-ids
         :refname: removeRuleIds
         :type: (array of integer, optional)

         IDs of the rules to remove. Any invalid IDs will be ignored.

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarative^net^request.update^enabled^rulesets:

updateEnabledRulesets(updateRulesetOptions)
-------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Modifies the static rulesets enabled/disabled state.

.. api-header::
   :label: Parameters

   .. _declarative^net^request.update^enabled^rulesets.update^ruleset^options:

   .. api-member::
      :name: ``updateRulesetOptions``
      :refid: declarative-net-request-update-enabled-rulesets-update-ruleset-options
      :refname: updateRulesetOptions
      :type: (object)

      .. _declarative^net^request.update^enabled^rulesets.update^ruleset^options.disable^ruleset^ids:

      .. api-member::
         :name: [``disableRulesetIds``]
         :refid: declarative-net-request-update-enabled-rulesets-update-ruleset-options-disable-ruleset-ids
         :refname: disableRulesetIds
         :type: (array of string, optional)

      .. _declarative^net^request.update^enabled^rulesets.update^ruleset^options.enable^ruleset^ids:

      .. api-member::
         :name: [``enableRulesetIds``]
         :refid: declarative-net-request-update-enabled-rulesets-update-ruleset-options-enable-ruleset-ids
         :refname: enableRulesetIds
         :type: (array of string, optional)

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarative^net^request.update^session^rules:

updateSessionRules(options)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Modifies the current set of session scoped rules for the extension. The rules with IDs listed in options.removeRuleIds are first removed, and then the rules given in options.addRules are added. These rules are not persisted across sessions and are backed in memory.

.. api-header::
   :label: Parameters

   .. _declarative^net^request.update^session^rules.options:

   .. api-member::
      :name: ``options``
      :refid: declarative-net-request-update-session-rules-options
      :refname: options
      :type: (object)

      .. _declarative^net^request.update^session^rules.options.add^rules:

      .. api-member::
         :name: [``addRules``]
         :refid: declarative-net-request-update-session-rules-options-add-rules
         :refname: addRules
         :type: (array of :ref:`declarative^net^request.^rule`, optional)

         Rules to add.

      .. _declarative^net^request.update^session^rules.options.remove^rule^ids:

      .. api-member::
         :name: [``removeRuleIds``]
         :refid: declarative-net-request-update-session-rules-options-remove-rule-ids
         :refname: removeRuleIds
         :type: (array of integer, optional)

         IDs of the rules to remove. Any invalid IDs will be ignored.

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarative^net^request.update^static^rules:

updateStaticRules(options)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Modified individual static rules enabled/disabled state. Changes to rules belonging to a disabled ruleset will take effect when the ruleset becomes enabled.

.. api-header::
   :label: Parameters

   .. _declarative^net^request.update^static^rules.options:

   .. api-member::
      :name: ``options``
      :refid: declarative-net-request-update-static-rules-options
      :refname: options
      :type: (object)

      .. _declarative^net^request.update^static^rules.options.ruleset^id:

      .. api-member::
         :name: ``rulesetId``
         :refid: declarative-net-request-update-static-rules-options-ruleset-id
         :refname: rulesetId
         :type: (string)

      .. _declarative^net^request.update^static^rules.options.disable^rule^ids:

      .. api-member::
         :name: [``disableRuleIds``]
         :refid: declarative-net-request-update-static-rules-options-disable-rule-ids
         :refname: disableRuleIds
         :type: (array of integer, optional)

      .. _declarative^net^request.update^static^rules.options.enable^rule^ids:

      .. api-member::
         :name: [``enableRuleIds``]
         :refid: declarative-net-request-update-static-rules-options-enable-rule-ids
         :refname: enableRuleIds
         :type: (array of integer, optional)

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. rst-class:: api-main-section

Types
=====

.. _declarative^net^request.^get^rules^filter:

GetRulesFilter
--------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _declarative^net^request.^get^rules^filter.rule^ids:

   .. api-member::
      :name: [``ruleIds``]
      :refid: declarative-net-request-get-rules-filter-rule-ids
      :refname: ruleIds
      :type: (array of integer, optional)

      If specified, only rules with matching IDs are included.

.. _declarative^net^request.^matched^rule:

MatchedRule
-----------

.. api-section-annotation-hack:: -- [Added in TB 113]

.. api-header::
   :label: object

   .. _declarative^net^request.^matched^rule.rule^id:

   .. api-member::
      :name: ``ruleId``
      :refid: declarative-net-request-matched-rule-rule-id
      :refname: ruleId
      :type: (integer)

      A matching rule's ID.

   .. _declarative^net^request.^matched^rule.ruleset^id:

   .. api-member::
      :name: ``rulesetId``
      :refid: declarative-net-request-matched-rule-ruleset-id
      :refname: rulesetId
      :type: (string)

      ID of the Ruleset this rule belongs to.

   .. _declarative^net^request.^matched^rule.extension^id:

   .. api-member::
      :name: [``extensionId``]
      :refid: declarative-net-request-matched-rule-extension-id
      :refname: extensionId
      :type: (string, optional)

      ID of the extension, if this rule belongs to a different extension.

.. _declarative^net^request.^resource^type:

ResourceType
------------

.. api-section-annotation-hack:: -- [Added in TB 113]

How the requested resource will be used. Comparable to the webRequest.ResourceType type. object_subrequest is unsupported.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _declarative^net^request.^resource^type.beacon:

         .. api-member::
            :name: :value:`beacon`
            :refid: declarative-net-request-resource-type-beacon
            :refname: beacon

         .. _declarative^net^request.^resource^type.csp_report:

         .. api-member::
            :name: :value:`csp_report`
            :refid: declarative-net-request-resource-type-csp-report
            :refname: csp_report

         .. _declarative^net^request.^resource^type.font:

         .. api-member::
            :name: :value:`font`
            :refid: declarative-net-request-resource-type-font
            :refname: font

         .. _declarative^net^request.^resource^type.image:

         .. api-member::
            :name: :value:`image`
            :refid: declarative-net-request-resource-type-image
            :refname: image

         .. _declarative^net^request.^resource^type.imageset:

         .. api-member::
            :name: :value:`imageset`
            :refid: declarative-net-request-resource-type-imageset
            :refname: imageset

         .. _declarative^net^request.^resource^type.json:

         .. api-member::
            :name: :value:`json`
            :refid: declarative-net-request-resource-type-json
            :refname: json
            :annotation: -- [Added in TB 138]

            .. note::

               The "json" property is supported from Thunderbird 135, but requests of this type are only available from Thunderbird 138.

         .. _declarative^net^request.^resource^type.main_frame:

         .. api-member::
            :name: :value:`main_frame`
            :refid: declarative-net-request-resource-type-main-frame
            :refname: main_frame

         .. _declarative^net^request.^resource^type.media:

         .. api-member::
            :name: :value:`media`
            :refid: declarative-net-request-resource-type-media
            :refname: media

         .. _declarative^net^request.^resource^type.object:

         .. api-member::
            :name: :value:`object`
            :refid: declarative-net-request-resource-type-object
            :refname: object

         .. _declarative^net^request.^resource^type.object_subrequest:

         .. api-member::
            :name: :value:`object_subrequest`
            :refid: declarative-net-request-resource-type-object-subrequest
            :refname: object_subrequest

         .. _declarative^net^request.^resource^type.other:

         .. api-member::
            :name: :value:`other`
            :refid: declarative-net-request-resource-type-other
            :refname: other

         .. _declarative^net^request.^resource^type.ping:

         .. api-member::
            :name: :value:`ping`
            :refid: declarative-net-request-resource-type-ping
            :refname: ping

         .. _declarative^net^request.^resource^type.script:

         .. api-member::
            :name: :value:`script`
            :refid: declarative-net-request-resource-type-script
            :refname: script

         .. _declarative^net^request.^resource^type.speculative:

         .. api-member::
            :name: :value:`speculative`
            :refid: declarative-net-request-resource-type-speculative
            :refname: speculative

         .. _declarative^net^request.^resource^type.stylesheet:

         .. api-member::
            :name: :value:`stylesheet`
            :refid: declarative-net-request-resource-type-stylesheet
            :refname: stylesheet

         .. _declarative^net^request.^resource^type.sub_frame:

         .. api-member::
            :name: :value:`sub_frame`
            :refid: declarative-net-request-resource-type-sub-frame
            :refname: sub_frame

         .. _declarative^net^request.^resource^type.web_manifest:

         .. api-member::
            :name: :value:`web_manifest`
            :refid: declarative-net-request-resource-type-web-manifest
            :refname: web_manifest

         .. _declarative^net^request.^resource^type.websocket:

         .. api-member::
            :name: :value:`websocket`
            :refid: declarative-net-request-resource-type-websocket
            :refname: websocket

         .. _declarative^net^request.^resource^type.xml_dtd:

         .. api-member::
            :name: :value:`xml_dtd`
            :refid: declarative-net-request-resource-type-xml-dtd
            :refname: xml_dtd

         .. _declarative^net^request.^resource^type.xmlhttprequest:

         .. api-member::
            :name: :value:`xmlhttprequest`
            :refid: declarative-net-request-resource-type-xmlhttprequest
            :refname: xmlhttprequest

         .. _declarative^net^request.^resource^type.xslt:

         .. api-member::
            :name: :value:`xslt`
            :refid: declarative-net-request-resource-type-xslt
            :refname: xslt

.. _declarative^net^request.^rule:

Rule
----

.. api-section-annotation-hack:: -- [Added in TB 113]

.. api-header::
   :label: object

   .. _declarative^net^request.^rule.action:

   .. api-member::
      :name: ``action``
      :refid: declarative-net-request-rule-action
      :refname: action
      :type: (object)

      The action to take if this rule is matched.

      .. _declarative^net^request.^rule.action.type:

      .. api-member::
         :name: ``type``
         :refid: declarative-net-request-rule-action-type
         :refname: type
         :type: (`string`)

         Supported values:

         .. _declarative^net^request.^rule.action.type.allow:

         .. api-member::
            :name: :value:`allow`
            :refid: declarative-net-request-rule-action-type-allow
            :refname: allow

         .. _declarative^net^request.^rule.action.type.allow^all^requests:

         .. api-member::
            :name: :value:`allowAllRequests`
            :refid: declarative-net-request-rule-action-type-allow-all-requests
            :refname: allowAllRequests

         .. _declarative^net^request.^rule.action.type.block:

         .. api-member::
            :name: :value:`block`
            :refid: declarative-net-request-rule-action-type-block
            :refname: block

         .. _declarative^net^request.^rule.action.type.modify^headers:

         .. api-member::
            :name: :value:`modifyHeaders`
            :refid: declarative-net-request-rule-action-type-modify-headers
            :refname: modifyHeaders

         .. _declarative^net^request.^rule.action.type.redirect:

         .. api-member::
            :name: :value:`redirect`
            :refid: declarative-net-request-rule-action-type-redirect
            :refname: redirect

         .. _declarative^net^request.^rule.action.type.upgrade^scheme:

         .. api-member::
            :name: :value:`upgradeScheme`
            :refid: declarative-net-request-rule-action-type-upgrade-scheme
            :refname: upgradeScheme

      .. _declarative^net^request.^rule.action.redirect:

      .. api-member::
         :name: [``redirect``]
         :refid: declarative-net-request-rule-action-redirect
         :refname: redirect
         :type: (object, optional)

         Describes how the redirect should be performed. Only valid when type is 'redirect'.

         .. _declarative^net^request.^rule.action.redirect.extension^path:

         .. api-member::
            :name: [``extensionPath``]
            :refid: declarative-net-request-rule-action-redirect-extension-path
            :refname: extensionPath
            :type: (string, optional)

            Path relative to the extension directory. Should start with '/'.

         .. _declarative^net^request.^rule.action.redirect.regex^substitution:

         .. api-member::
            :name: [``regexSubstitution``]
            :refid: declarative-net-request-rule-action-redirect-regex-substitution
            :refname: regexSubstitution
            :type: (string, optional)

            Substitution pattern for rules which specify a 'regexFilter'. The first match of regexFilter within the url will be replaced with this pattern. Within regexSubstitution, backslash-escaped digits (\\1 to \\9) can be used to insert the corresponding capture groups. \\0 refers to the entire matching text.

         .. _declarative^net^request.^rule.action.redirect.transform:

         .. api-member::
            :name: [``transform``]
            :refid: declarative-net-request-rule-action-redirect-transform
            :refname: transform
            :type: (:ref:`declarative^net^request.^u^r^l^transform`, optional)

            Url transformations to perform.

         .. _declarative^net^request.^rule.action.redirect.url:

         .. api-member::
            :name: [``url``]
            :refid: declarative-net-request-rule-action-redirect-url
            :refname: url
            :type: (string, optional)

            The redirect url. Redirects to JavaScript urls are not allowed.

      .. _declarative^net^request.^rule.action.request^headers:

      .. api-member::
         :name: [``requestHeaders``]
         :refid: declarative-net-request-rule-action-request-headers
         :refname: requestHeaders
         :type: (array of object, optional)

         The request headers to modify for the request. Only valid when type is 'modifyHeaders'.

      .. _declarative^net^request.^rule.action.response^headers:

      .. api-member::
         :name: [``responseHeaders``]
         :refid: declarative-net-request-rule-action-response-headers
         :refname: responseHeaders
         :type: (array of object, optional)

         The response headers to modify for the request. Only valid when type is 'modifyHeaders'.

   .. _declarative^net^request.^rule.condition:

   .. api-member::
      :name: ``condition``
      :refid: declarative-net-request-rule-condition
      :refname: condition
      :type: (object)

      The condition under which this rule is triggered.

      .. _declarative^net^request.^rule.condition.domain^type:

      .. api-member::
         :name: [``domainType``]
         :refid: declarative-net-request-rule-condition-domain-type
         :refname: domainType
         :type: (`string`, optional)

         Specifies whether the network request is first-party or third-party to the domain from which it originated. If omitted, all requests are matched.

         Supported values:

         .. _declarative^net^request.^rule.condition.domain^type.first^party:

         .. api-member::
            :name: :value:`firstParty`
            :refid: declarative-net-request-rule-condition-domain-type-first-party
            :refname: firstParty

         .. _declarative^net^request.^rule.condition.domain^type.third^party:

         .. api-member::
            :name: :value:`thirdParty`
            :refid: declarative-net-request-rule-condition-domain-type-third-party
            :refname: thirdParty

      .. _declarative^net^request.^rule.condition.excluded^initiator^domains:

      .. api-member::
         :name: [``excludedInitiatorDomains``]
         :refid: declarative-net-request-rule-condition-excluded-initiator-domains
         :refname: excludedInitiatorDomains
         :type: (array of string, optional)

         The rule will not match network requests originating from the list of 'initiatorDomains'. If the list is empty or omitted, no domains are excluded. This takes precedence over 'initiatorDomains'.

      .. _declarative^net^request.^rule.condition.excluded^request^domains:

      .. api-member::
         :name: [``excludedRequestDomains``]
         :refid: declarative-net-request-rule-condition-excluded-request-domains
         :refname: excludedRequestDomains
         :type: (array of string, optional)

         The rule will not match network requests when the domains matches one from the list of 'excludedRequestDomains'. If the list is empty or omitted, no domains are excluded. This takes precedence over 'requestDomains'.

      .. _declarative^net^request.^rule.condition.excluded^request^methods:

      .. api-member::
         :name: [``excludedRequestMethods``]
         :refid: declarative-net-request-rule-condition-excluded-request-methods
         :refname: excludedRequestMethods
         :type: (array of string, optional)

         List of request methods which the rule won't match. Cannot be specified if 'requestMethods' is specified. If neither of them is specified, all request methods are matched.

      .. _declarative^net^request.^rule.condition.excluded^resource^types:

      .. api-member::
         :name: [``excludedResourceTypes``]
         :refid: declarative-net-request-rule-condition-excluded-resource-types
         :refname: excludedResourceTypes
         :type: (array of :ref:`declarative^net^request.^resource^type`, optional)

         List of resource types which the rule won't match. Cannot be specified if 'resourceTypes' is specified. If neither of them is specified, all resource types except 'main_frame' are matched.

      .. _declarative^net^request.^rule.condition.excluded^tab^ids:

      .. api-member::
         :name: [``excludedTabIds``]
         :refid: declarative-net-request-rule-condition-excluded-tab-ids
         :refname: excludedTabIds
         :type: (array of integer, optional)

         List of tabIds which the rule should not match. An ID of -1 excludes requests which don't originate from a tab. Only supported for session-scoped rules.

      .. _declarative^net^request.^rule.condition.initiator^domains:

      .. api-member::
         :name: [``initiatorDomains``]
         :refid: declarative-net-request-rule-condition-initiator-domains
         :refname: initiatorDomains
         :type: (array of string, optional)

         The rule will only match network requests originating from the list of 'initiatorDomains'. If the list is omitted, the rule is applied to requests from all domains.

      .. _declarative^net^request.^rule.condition.is^url^filter^case^sensitive:

      .. api-member::
         :name: [``isUrlFilterCaseSensitive``]
         :refid: declarative-net-request-rule-condition-is-url-filter-case-sensitive
         :refname: isUrlFilterCaseSensitive
         :type: (boolean, optional)

         Whether 'urlFilter' or 'regexFilter' is case-sensitive.

      .. _declarative^net^request.^rule.condition.regex^filter:

      .. api-member::
         :name: [``regexFilter``]
         :refid: declarative-net-request-rule-condition-regex-filter
         :refname: regexFilter
         :type: (string, optional)

         Regular expression to match against the network request url. Only one of 'urlFilter' or 'regexFilter' can be specified.

      .. _declarative^net^request.^rule.condition.request^domains:

      .. api-member::
         :name: [``requestDomains``]
         :refid: declarative-net-request-rule-condition-request-domains
         :refname: requestDomains
         :type: (array of string, optional)

         The rule will only match network requests when the domain matches one from the list of 'requestDomains'. If the list is omitted, the rule is applied to requests from all domains.

      .. _declarative^net^request.^rule.condition.request^methods:

      .. api-member::
         :name: [``requestMethods``]
         :refid: declarative-net-request-rule-condition-request-methods
         :refname: requestMethods
         :type: (array of string, optional)

         List of HTTP request methods which the rule can match. Should be a lower-case method such as 'connect', 'delete', 'get', 'head', 'options', 'patch', 'post', 'put'.'

      .. _declarative^net^request.^rule.condition.resource^types:

      .. api-member::
         :name: [``resourceTypes``]
         :refid: declarative-net-request-rule-condition-resource-types
         :refname: resourceTypes
         :type: (array of :ref:`declarative^net^request.^resource^type`, optional)

         List of resource types which the rule can match. When the rule action is 'allowAllRequests', this must be specified and may only contain 'main_frame' or 'sub_frame'. Cannot be specified if 'excludedResourceTypes' is specified. If neither of them is specified, all resource types except 'main_frame' are matched.

      .. _declarative^net^request.^rule.condition.tab^ids:

      .. api-member::
         :name: [``tabIds``]
         :refid: declarative-net-request-rule-condition-tab-ids
         :refname: tabIds
         :type: (array of integer, optional)

         List of tabIds which the rule should match. An ID of -1 matches requests which don't originate from a tab. Only supported for session-scoped rules.

      .. _declarative^net^request.^rule.condition.url^filter:

      .. api-member::
         :name: [``urlFilter``]
         :refid: declarative-net-request-rule-condition-url-filter
         :refname: urlFilter
         :type: (string, optional)

         TODO: link to doc explaining supported pattern. The pattern which is matched against the network request url. Only one of 'urlFilter' or 'regexFilter' can be specified.

   .. _declarative^net^request.^rule.id:

   .. api-member::
      :name: ``id``
      :refid: declarative-net-request-rule-id
      :refname: id
      :type: (integer)

      An id which uniquely identifies a rule. Mandatory and should be >= 1.

   .. _declarative^net^request.^rule.priority:

   .. api-member::
      :name: [``priority``]
      :refid: declarative-net-request-rule-priority
      :refname: priority
      :type: (integer, optional)

      Rule priority. Defaults to 1. When specified, should be >= 1

.. _declarative^net^request.^unsupported^regex^reason:

UnsupportedRegexReason
----------------------

.. api-section-annotation-hack:: 

Describes the reason why a given regular expression isn't supported.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _declarative^net^request.^unsupported^regex^reason.memory^limit^exceeded:

         .. api-member::
            :name: :value:`memoryLimitExceeded`
            :refid: declarative-net-request-unsupported-regex-reason-memory-limit-exceeded
            :refname: memoryLimitExceeded

         .. _declarative^net^request.^unsupported^regex^reason.syntax^error:

         .. api-member::
            :name: :value:`syntaxError`
            :refid: declarative-net-request-unsupported-regex-reason-syntax-error
            :refname: syntaxError

.. _declarative^net^request.^u^r^l^transform:

URLTransform
------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Describes the type of the Rule.action.redirect.transform property.

.. api-header::
   :label: object

   .. _declarative^net^request.^u^r^l^transform.fragment:

   .. api-member::
      :name: [``fragment``]
      :refid: declarative-net-request-u-r-l-transform-fragment
      :refname: fragment
      :type: (string, optional)

      The new fragment for the request. Should be either empty, in which case the existing fragment is cleared; or should begin with '#'.

   .. _declarative^net^request.^u^r^l^transform.host:

   .. api-member::
      :name: [``host``]
      :refid: declarative-net-request-u-r-l-transform-host
      :refname: host
      :type: (string, optional)

      The new host name for the request.

   .. _declarative^net^request.^u^r^l^transform.password:

   .. api-member::
      :name: [``password``]
      :refid: declarative-net-request-u-r-l-transform-password
      :refname: password
      :type: (string, optional)

      The new password for the request.

   .. _declarative^net^request.^u^r^l^transform.path:

   .. api-member::
      :name: [``path``]
      :refid: declarative-net-request-u-r-l-transform-path
      :refname: path
      :type: (string, optional)

      The new path for the request. If empty, the existing path is cleared.

   .. _declarative^net^request.^u^r^l^transform.port:

   .. api-member::
      :name: [``port``]
      :refid: declarative-net-request-u-r-l-transform-port
      :refname: port
      :type: (string, optional)

      The new port for the request. If empty, the existing port is cleared.

   .. _declarative^net^request.^u^r^l^transform.query:

   .. api-member::
      :name: [``query``]
      :refid: declarative-net-request-u-r-l-transform-query
      :refname: query
      :type: (string, optional)

      The new query for the request. Should be either empty, in which case the existing query is cleared; or should begin with '?'. Cannot be specified if 'queryTransform' is specified.

   .. _declarative^net^request.^u^r^l^transform.query^transform:

   .. api-member::
      :name: [``queryTransform``]
      :refid: declarative-net-request-u-r-l-transform-query-transform
      :refname: queryTransform
      :type: (object, optional)

      Add, remove or replace query key-value pairs. Cannot be specified if 'query' is specified.

      .. _declarative^net^request.^u^r^l^transform.query^transform.add^or^replace^params:

      .. api-member::
         :name: [``addOrReplaceParams``]
         :refid: declarative-net-request-u-r-l-transform-query-transform-add-or-replace-params
         :refname: addOrReplaceParams
         :type: (array of object, optional)

         The list of query key-value pairs to be added or replaced.

      .. _declarative^net^request.^u^r^l^transform.query^transform.remove^params:

      .. api-member::
         :name: [``removeParams``]
         :refid: declarative-net-request-u-r-l-transform-query-transform-remove-params
         :refname: removeParams
         :type: (array of string, optional)

         The list of query keys to be removed.

   .. _declarative^net^request.^u^r^l^transform.scheme:

   .. api-member::
      :name: [``scheme``]
      :refid: declarative-net-request-u-r-l-transform-scheme
      :refname: scheme
      :type: (`string`, optional)

      The new scheme for the request.

      Supported values:

      .. _declarative^net^request.^u^r^l^transform.scheme.http:

      .. api-member::
         :name: :value:`http`
         :refid: declarative-net-request-u-r-l-transform-scheme-http
         :refname: http

      .. _declarative^net^request.^u^r^l^transform.scheme.https:

      .. api-member::
         :name: :value:`https`
         :refid: declarative-net-request-u-r-l-transform-scheme-https
         :refname: https

      .. _declarative^net^request.^u^r^l^transform.scheme.moz-extension:

      .. api-member::
         :name: :value:`moz-extension`
         :refid: declarative-net-request-u-r-l-transform-scheme-moz-extension
         :refname: moz-extension

   .. _declarative^net^request.^u^r^l^transform.username:

   .. api-member::
      :name: [``username``]
      :refid: declarative-net-request-u-r-l-transform-username
      :refname: username
      :type: (string, optional)

      The new username for the request.

.. rst-class:: api-main-section

Properties
==========

.. _declarative^net^request.^d^y^n^a^m^i^c_^r^u^l^e^s^e^t_^i^d:

DYNAMIC_RULESET_ID
------------------

.. api-section-annotation-hack:: 

Ruleset ID for the dynamic rules added by the extension.

.. _declarative^net^request.^g^u^a^r^a^n^t^e^e^d_^m^i^n^i^m^u^m_^s^t^a^t^i^c_^r^u^l^e^s:

GUARANTEED_MINIMUM_STATIC_RULES
-------------------------------

.. api-section-annotation-hack:: 

The minimum number of static rules guaranteed to an extension across its enabled static rulesets. Any rules above this limit will count towards the global static rule limit.

.. _declarative^net^request.^m^a^x_^n^u^m^b^e^r_^o^f_^d^i^s^a^b^l^e^d_^s^t^a^t^i^c_^r^u^l^e^s:

MAX_NUMBER_OF_DISABLED_STATIC_RULES
-----------------------------------

.. api-section-annotation-hack:: 

The maximum number of static rules that can be disabled on each static ruleset.

.. _declarative^net^request.^m^a^x_^n^u^m^b^e^r_^o^f_^d^y^n^a^m^i^c_^a^n^d_^s^e^s^s^i^o^n_^r^u^l^e^s:

MAX_NUMBER_OF_DYNAMIC_AND_SESSION_RULES
---------------------------------------

.. api-section-annotation-hack:: 

Deprecated property returning the maximum number of dynamic and session rules an extension can add, replaced by MAX_NUMBER_OF_DYNAMIC_RULES/MAX_NUMBER_OF_SESSION_RULES.

.. note::

   Deprecated in Thunderbird 128. Use :code:`MAX_NUMBER_OF_DYNAMIC_RULES` and :code:`MAX_NUMBER_OF_SESSION_RULES` instead.

.. _declarative^net^request.^m^a^x_^n^u^m^b^e^r_^o^f_^d^y^n^a^m^i^c_^r^u^l^e^s:

MAX_NUMBER_OF_DYNAMIC_RULES
---------------------------

.. api-section-annotation-hack:: 

The maximum number of dynamic session rules an extension can add.

.. _declarative^net^request.^m^a^x_^n^u^m^b^e^r_^o^f_^e^n^a^b^l^e^d_^s^t^a^t^i^c_^r^u^l^e^s^e^t^s:

MAX_NUMBER_OF_ENABLED_STATIC_RULESETS
-------------------------------------

.. api-section-annotation-hack:: 

The maximum number of static Rulesets an extension can enable at any one time.

.. _declarative^net^request.^m^a^x_^n^u^m^b^e^r_^o^f_^r^e^g^e^x_^r^u^l^e^s:

MAX_NUMBER_OF_REGEX_RULES
-------------------------

.. api-section-annotation-hack:: 

The maximum number of regular expression rules that an extension can add. This limit is evaluated separately for the set of session rules, dynamic rules and those specified in the rule_resources file.

.. _declarative^net^request.^m^a^x_^n^u^m^b^e^r_^o^f_^s^e^s^s^i^o^n_^r^u^l^e^s:

MAX_NUMBER_OF_SESSION_RULES
---------------------------

.. api-section-annotation-hack:: 

The maximum number of dynamic session rules an extension can add.

.. _declarative^net^request.^m^a^x_^n^u^m^b^e^r_^o^f_^s^t^a^t^i^c_^r^u^l^e^s^e^t^s:

MAX_NUMBER_OF_STATIC_RULESETS
-----------------------------

.. api-section-annotation-hack:: 

The maximum number of static Rulesets an extension can specify as part of the rule_resources manifest key.

.. _declarative^net^request.^s^e^s^s^i^o^n_^r^u^l^e^s^e^t_^i^d:

SESSION_RULESET_ID
------------------

.. api-section-annotation-hack:: 

Ruleset ID for the session-scoped rules added by the extension.
