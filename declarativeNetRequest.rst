.. container:: sticky-sidebar

  ≡ declarativeNetRequest API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Types`_
  * `Properties`_

  .. include:: /includes/developer-resources.rst

=========================
declarativeNetRequest API
=========================

.. role:: permission

.. role:: value

.. role:: code

Use the declarativeNetRequest API to block or modify network requests by specifying declarative rules.

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``declarative_net_request``]
   :type: (object, optional)
   :annotation: -- [Added in TB true]

   .. api-member::
      :name: ``rule_resources``
      :type: (array of object)

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`declarativeNetRequest`

   Block content on any page

.. api-member::
   :name: :permission:`declarativeNetRequestWithHostAccess`

.. api-member::
   :name: :permission:`declarativeNetRequestFeedback`

   Read your browsing history

.. rst-class:: api-permission-info

.. note::

   One of the permissions :permission:`declarativeNetRequest` or :permission:`declarativeNetRequestWithHostAccess` is required to use ``messenger.declarativeNetRequest.*``.

.. rst-class:: api-main-section

Functions
=========

.. _declarativeNetRequest.getAvailableStaticRuleCount:

getAvailableStaticRuleCount()
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Returns the remaining number of static rules an extension can enable

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: integer

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarativeNetRequest.getDisabledRuleIds:

getDisabledRuleIds(options)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Returns the list of individual disabled static rules from a given static ruleset id.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (object)

      .. api-member::
         :name: ``rulesetId``
         :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of integer

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarativeNetRequest.getDynamicRules:

getDynamicRules([filter])
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Returns the current set of dynamic rules for the extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`declarativeNetRequest.GetRulesFilter`, optional)
      :annotation: -- [Added in TB 127]

      An object to filter the set of dynamic rules for the extension.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`declarativeNetRequest.Rule`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarativeNetRequest.getEnabledRulesets:

getEnabledRulesets()
--------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Returns the ids for the current set of enabled static rulesets.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarativeNetRequest.getSessionRules:

getSessionRules([filter])
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Returns the current set of session scoped rules for the extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`declarativeNetRequest.GetRulesFilter`, optional)
      :annotation: -- [Added in TB 127]

      An object to filter the set of session scoped rules for the extension.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`declarativeNetRequest.Rule`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarativeNetRequest.isRegexSupported:

isRegexSupported(regexOptions)
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Checks if the given regular expression will be supported as a 'regexFilter' rule condition.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``regexOptions``
      :type: (object)

      .. api-member::
         :name: ``regex``
         :type: (string)

         The regular expresson to check.

      .. api-member::
         :name: [``isCaseSensitive``]
         :type: (boolean, optional)

         Whether the 'regex' specified is case sensitive.

      .. api-member::
         :name: [``requireCapturing``]
         :type: (boolean, optional)

         Whether the 'regex' specified requires capturing. Capturing is only required for redirect rules which specify a 'regexSubstition' action.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: object

      .. api-member::
         :name: ``isSupported``
         :type: (boolean)

         Whether the given regex is supported

      .. api-member::
         :name: [``reason``]
         :type: (:ref:`declarativeNetRequest.UnsupportedRegexReason`, optional)

         Specifies the reason why the regular expression is not supported. Only provided if 'isSupported' is false.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarativeNetRequest.testMatchOutcome:

testMatchOutcome(request, [options])
------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Checks if any of the extension's declarativeNetRequest rules would match a hypothetical request.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``request``
      :type: (object)

      The details of the request to test.

      .. api-member::
         :name: ``type``
         :type: (:ref:`declarativeNetRequest.ResourceType`)

         The resource type of the hypothetical request.

      .. api-member::
         :name: ``url``
         :type: (string)

         The URL of the hypothetical request.

      .. api-member::
         :name: [``initiator``]
         :type: (string, optional)

         The initiator URL (if any) for the hypothetical request.

      .. api-member::
         :name: [``method``]
         :type: (string, optional)

         Standard HTTP method of the hypothetical request.

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)

         The ID of the tab in which the hypothetical request takes place. Does not need to correspond to a real tab ID. Default is -1, meaning that the request isn't related to a tab.

   .. api-member::
      :name: [``options``]
      :type: (object, optional)

      .. api-member::
         :name: [``includeOtherExtensions``]
         :type: (boolean, optional)

         Whether to account for rules from other installed extensions during rule evaluation.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: object

      .. api-member::
         :name: ``matchedRules``
         :type: (array of :ref:`declarativeNetRequest.MatchedRule`)

         The rules (if any) that match the hypothetical request.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestFeedback`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarativeNetRequest.updateDynamicRules:

updateDynamicRules(options)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Modifies the current set of dynamic rules for the extension. The rules with IDs listed in options.removeRuleIds are first removed, and then the rules given in options.addRules are added. These rules are persisted across browser sessions and extension updates.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (object)

      .. api-member::
         :name: [``addRules``]
         :type: (array of :ref:`declarativeNetRequest.Rule`, optional)

         Rules to add.

      .. api-member::
         :name: [``removeRuleIds``]
         :type: (array of integer, optional)

         IDs of the rules to remove. Any invalid IDs will be ignored.

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarativeNetRequest.updateEnabledRulesets:

updateEnabledRulesets(updateRulesetOptions)
-------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Modifies the static rulesets enabled/disabled state.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``updateRulesetOptions``
      :type: (object)

      .. api-member::
         :name: [``disableRulesetIds``]
         :type: (array of string, optional)

      .. api-member::
         :name: [``enableRulesetIds``]
         :type: (array of string, optional)

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarativeNetRequest.updateSessionRules:

updateSessionRules(options)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Modifies the current set of session scoped rules for the extension. The rules with IDs listed in options.removeRuleIds are first removed, and then the rules given in options.addRules are added. These rules are not persisted across sessions and are backed in memory.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (object)

      .. api-member::
         :name: [``addRules``]
         :type: (array of :ref:`declarativeNetRequest.Rule`, optional)

         Rules to add.

      .. api-member::
         :name: [``removeRuleIds``]
         :type: (array of integer, optional)

         IDs of the rules to remove. Any invalid IDs will be ignored.

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. _declarativeNetRequest.updateStaticRules:

updateStaticRules(options)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Modified individual static rules enabled/disabled state. Changes to rules belonging to a disabled ruleset will take effect when the ruleset becomes enabled.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (object)

      .. api-member::
         :name: ``rulesetId``
         :type: (string)

      .. api-member::
         :name: [``disableRuleIds``]
         :type: (array of integer, optional)

      .. api-member::
         :name: [``enableRuleIds``]
         :type: (array of integer, optional)

.. api-header::
   :label: Required permissions

   - :permission:`declarativeNetRequest`
   - :permission:`declarativeNetRequestWithHostAccess`

.. rst-class:: api-main-section

Types
=====

.. _declarativeNetRequest.GetRulesFilter:

GetRulesFilter
--------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. api-member::
      :name: [``ruleIds``]
      :type: (array of integer, optional)

      If specified, only rules with matching IDs are included.

.. _declarativeNetRequest.MatchedRule:

MatchedRule
-----------

.. api-section-annotation-hack:: -- [Added in TB 113]

.. api-header::
   :label: object

   .. api-member::
      :name: ``ruleId``
      :type: (integer)

      A matching rule's ID.

   .. api-member::
      :name: ``rulesetId``
      :type: (string)

      ID of the Ruleset this rule belongs to.

   .. api-member::
      :name: [``extensionId``]
      :type: (string, optional)

      ID of the extension, if this rule belongs to a different extension.

.. _declarativeNetRequest.ResourceType:

ResourceType
------------

.. api-section-annotation-hack:: -- [Added in TB 113]

How the requested resource will be used. Comparable to the webRequest.ResourceType type. object_subrequest is unsupported.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`main_frame`

         .. api-member::
            :name: :value:`sub_frame`

         .. api-member::
            :name: :value:`stylesheet`

         .. api-member::
            :name: :value:`script`

         .. api-member::
            :name: :value:`image`

         .. api-member::
            :name: :value:`object`

         .. api-member::
            :name: :value:`object_subrequest`

         .. api-member::
            :name: :value:`xmlhttprequest`

         .. api-member::
            :name: :value:`xslt`

         .. api-member::
            :name: :value:`ping`

         .. api-member::
            :name: :value:`beacon`

         .. api-member::
            :name: :value:`xml_dtd`

         .. api-member::
            :name: :value:`font`

         .. api-member::
            :name: :value:`media`

         .. api-member::
            :name: :value:`websocket`

         .. api-member::
            :name: :value:`csp_report`

         .. api-member::
            :name: :value:`imageset`

         .. api-member::
            :name: :value:`web_manifest`

         .. api-member::
            :name: :value:`speculative`

         .. api-member::
            :name: :value:`json`
            :annotation: -- [Added in TB 138]

            .. note::

               The "json" property is supported from Thunderbird 135, but requests of this type are only available from Thunderbird 138.

         .. api-member::
            :name: :value:`other`

.. _declarativeNetRequest.Rule:

Rule
----

.. api-section-annotation-hack:: -- [Added in TB 113]

.. api-header::
   :label: object

   .. api-member::
      :name: ``action``
      :type: (object)

      The action to take if this rule is matched.

      .. api-member::
         :name: ``type``
         :type: (`string`)

         Supported values:

         .. api-member::
            :name: :value:`block`

         .. api-member::
            :name: :value:`redirect`

         .. api-member::
            :name: :value:`allow`

         .. api-member::
            :name: :value:`upgradeScheme`

         .. api-member::
            :name: :value:`modifyHeaders`

         .. api-member::
            :name: :value:`allowAllRequests`

      .. api-member::
         :name: [``redirect``]
         :type: (object, optional)

         Describes how the redirect should be performed. Only valid when type is 'redirect'.

         .. api-member::
            :name: [``extensionPath``]
            :type: (string, optional)

            Path relative to the extension directory. Should start with '/'.

         .. api-member::
            :name: [``regexSubstitution``]
            :type: (string, optional)

            Substitution pattern for rules which specify a 'regexFilter'. The first match of regexFilter within the url will be replaced with this pattern. Within regexSubstitution, backslash-escaped digits (\\1 to \\9) can be used to insert the corresponding capture groups. \\0 refers to the entire matching text.

         .. api-member::
            :name: [``transform``]
            :type: (:ref:`declarativeNetRequest.URLTransform`, optional)

            Url transformations to perform.

         .. api-member::
            :name: [``url``]
            :type: (string, optional)

            The redirect url. Redirects to JavaScript urls are not allowed.

      .. api-member::
         :name: [``requestHeaders``]
         :type: (array of object, optional)

         The request headers to modify for the request. Only valid when type is 'modifyHeaders'.

      .. api-member::
         :name: [``responseHeaders``]
         :type: (array of object, optional)

         The response headers to modify for the request. Only valid when type is 'modifyHeaders'.

   .. api-member::
      :name: ``condition``
      :type: (object)

      The condition under which this rule is triggered.

      .. api-member::
         :name: [``domainType``]
         :type: (`string`, optional)

         Specifies whether the network request is first-party or third-party to the domain from which it originated. If omitted, all requests are matched.

         Supported values:

         .. api-member::
            :name: :value:`firstParty`

         .. api-member::
            :name: :value:`thirdParty`

      .. api-member::
         :name: [``excludedInitiatorDomains``]
         :type: (array of string, optional)

         The rule will not match network requests originating from the list of 'initiatorDomains'. If the list is empty or omitted, no domains are excluded. This takes precedence over 'initiatorDomains'.

      .. api-member::
         :name: [``excludedRequestDomains``]
         :type: (array of string, optional)

         The rule will not match network requests when the domains matches one from the list of 'excludedRequestDomains'. If the list is empty or omitted, no domains are excluded. This takes precedence over 'requestDomains'.

      .. api-member::
         :name: [``excludedRequestMethods``]
         :type: (array of string, optional)

         List of request methods which the rule won't match. Cannot be specified if 'requestMethods' is specified. If neither of them is specified, all request methods are matched.

      .. api-member::
         :name: [``excludedResourceTypes``]
         :type: (array of :ref:`declarativeNetRequest.ResourceType`, optional)

         List of resource types which the rule won't match. Cannot be specified if 'resourceTypes' is specified. If neither of them is specified, all resource types except 'main_frame' are matched.

      .. api-member::
         :name: [``excludedTabIds``]
         :type: (array of integer, optional)

         List of tabIds which the rule should not match. An ID of -1 excludes requests which don't originate from a tab. Only supported for session-scoped rules.

      .. api-member::
         :name: [``initiatorDomains``]
         :type: (array of string, optional)

         The rule will only match network requests originating from the list of 'initiatorDomains'. If the list is omitted, the rule is applied to requests from all domains.

      .. api-member::
         :name: [``isUrlFilterCaseSensitive``]
         :type: (boolean, optional)

         Whether 'urlFilter' or 'regexFilter' is case-sensitive.

      .. api-member::
         :name: [``regexFilter``]
         :type: (string, optional)

         Regular expression to match against the network request url. Only one of 'urlFilter' or 'regexFilter' can be specified.

      .. api-member::
         :name: [``requestDomains``]
         :type: (array of string, optional)

         The rule will only match network requests when the domain matches one from the list of 'requestDomains'. If the list is omitted, the rule is applied to requests from all domains.

      .. api-member::
         :name: [``requestMethods``]
         :type: (array of string, optional)

         List of HTTP request methods which the rule can match. Should be a lower-case method such as 'connect', 'delete', 'get', 'head', 'options', 'patch', 'post', 'put'.'

      .. api-member::
         :name: [``resourceTypes``]
         :type: (array of :ref:`declarativeNetRequest.ResourceType`, optional)

         List of resource types which the rule can match. When the rule action is 'allowAllRequests', this must be specified and may only contain 'main_frame' or 'sub_frame'. Cannot be specified if 'excludedResourceTypes' is specified. If neither of them is specified, all resource types except 'main_frame' are matched.

      .. api-member::
         :name: [``tabIds``]
         :type: (array of integer, optional)

         List of tabIds which the rule should match. An ID of -1 matches requests which don't originate from a tab. Only supported for session-scoped rules.

      .. api-member::
         :name: [``urlFilter``]
         :type: (string, optional)

         TODO: link to doc explaining supported pattern. The pattern which is matched against the network request url. Only one of 'urlFilter' or 'regexFilter' can be specified.

   .. api-member::
      :name: ``id``
      :type: (integer)

      An id which uniquely identifies a rule. Mandatory and should be >= 1.

   .. api-member::
      :name: [``priority``]
      :type: (integer, optional)

      Rule priority. Defaults to 1. When specified, should be >= 1

.. _declarativeNetRequest.UnsupportedRegexReason:

UnsupportedRegexReason
----------------------

.. api-section-annotation-hack:: 

Describes the reason why a given regular expression isn't supported.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`syntaxError`

         .. api-member::
            :name: :value:`memoryLimitExceeded`

.. _declarativeNetRequest.URLTransform:

URLTransform
------------

.. api-section-annotation-hack:: -- [Added in TB 113]

Describes the type of the Rule.action.redirect.transform property.

.. api-header::
   :label: object

   .. api-member::
      :name: [``fragment``]
      :type: (string, optional)

      The new fragment for the request. Should be either empty, in which case the existing fragment is cleared; or should begin with '#'.

   .. api-member::
      :name: [``host``]
      :type: (string, optional)

      The new host name for the request.

   .. api-member::
      :name: [``password``]
      :type: (string, optional)

      The new password for the request.

   .. api-member::
      :name: [``path``]
      :type: (string, optional)

      The new path for the request. If empty, the existing path is cleared.

   .. api-member::
      :name: [``port``]
      :type: (string, optional)

      The new port for the request. If empty, the existing port is cleared.

   .. api-member::
      :name: [``query``]
      :type: (string, optional)

      The new query for the request. Should be either empty, in which case the existing query is cleared; or should begin with '?'. Cannot be specified if 'queryTransform' is specified.

   .. api-member::
      :name: [``queryTransform``]
      :type: (object, optional)

      Add, remove or replace query key-value pairs. Cannot be specified if 'query' is specified.

      .. api-member::
         :name: [``addOrReplaceParams``]
         :type: (array of object, optional)

         The list of query key-value pairs to be added or replaced.

      .. api-member::
         :name: [``removeParams``]
         :type: (array of string, optional)

         The list of query keys to be removed.

   .. api-member::
      :name: [``scheme``]
      :type: (`string`, optional)

      The new scheme for the request.

      Supported values:

      .. api-member::
         :name: :value:`http`

      .. api-member::
         :name: :value:`https`

      .. api-member::
         :name: :value:`moz-extension`

   .. api-member::
      :name: [``username``]
      :type: (string, optional)

      The new username for the request.

.. rst-class:: api-main-section

Properties
==========

.. _declarativeNetRequest.DYNAMIC_RULESET_ID:

DYNAMIC_RULESET_ID
------------------

.. api-section-annotation-hack:: 

Ruleset ID for the dynamic rules added by the extension.

.. _declarativeNetRequest.GUARANTEED_MINIMUM_STATIC_RULES:

GUARANTEED_MINIMUM_STATIC_RULES
-------------------------------

.. api-section-annotation-hack:: 

The minimum number of static rules guaranteed to an extension across its enabled static rulesets. Any rules above this limit will count towards the global static rule limit.

.. _declarativeNetRequest.MAX_NUMBER_OF_DISABLED_STATIC_RULES:

MAX_NUMBER_OF_DISABLED_STATIC_RULES
-----------------------------------

.. api-section-annotation-hack:: 

The maximum number of static rules that can be disabled on each static ruleset.

.. _declarativeNetRequest.MAX_NUMBER_OF_DYNAMIC_AND_SESSION_RULES:

MAX_NUMBER_OF_DYNAMIC_AND_SESSION_RULES
---------------------------------------

.. api-section-annotation-hack:: 

Deprecated property returning the maximum number of dynamic and session rules an extension can add, replaced by MAX_NUMBER_OF_DYNAMIC_RULES/MAX_NUMBER_OF_SESSION_RULES.

.. note::

   Deprecated in Thunderbird 128. Use :code:`MAX_NUMBER_OF_DYNAMIC_RULES` and :code:`MAX_NUMBER_OF_SESSION_RULES` instead.

.. _declarativeNetRequest.MAX_NUMBER_OF_DYNAMIC_RULES:

MAX_NUMBER_OF_DYNAMIC_RULES
---------------------------

.. api-section-annotation-hack:: 

The maximum number of dynamic session rules an extension can add.

.. _declarativeNetRequest.MAX_NUMBER_OF_ENABLED_STATIC_RULESETS:

MAX_NUMBER_OF_ENABLED_STATIC_RULESETS
-------------------------------------

.. api-section-annotation-hack:: 

The maximum number of static Rulesets an extension can enable at any one time.

.. _declarativeNetRequest.MAX_NUMBER_OF_REGEX_RULES:

MAX_NUMBER_OF_REGEX_RULES
-------------------------

.. api-section-annotation-hack:: 

The maximum number of regular expression rules that an extension can add. This limit is evaluated separately for the set of session rules, dynamic rules and those specified in the rule_resources file.

.. _declarativeNetRequest.MAX_NUMBER_OF_SESSION_RULES:

MAX_NUMBER_OF_SESSION_RULES
---------------------------

.. api-section-annotation-hack:: 

The maximum number of dynamic session rules an extension can add.

.. _declarativeNetRequest.MAX_NUMBER_OF_STATIC_RULESETS:

MAX_NUMBER_OF_STATIC_RULESETS
-----------------------------

.. api-section-annotation-hack:: 

The maximum number of static Rulesets an extension can specify as part of the rule_resources manifest key.

.. _declarativeNetRequest.SESSION_RULESET_ID:

SESSION_RULESET_ID
------------------

.. api-section-annotation-hack:: 

Ruleset ID for the session-scoped rules added by the extension.
