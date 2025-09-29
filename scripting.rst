.. container:: sticky-sidebar

  ≡ scripting API

  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=============
scripting API
=============

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The scripting API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/scripting>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the scripting API to execute script in different contexts.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`scripting`

   Grant access to some or all methods of the scripting API.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`scripting` is required to use ``messenger.scripting.*``.

.. rst-class:: api-main-section

Functions
=========

.. _scripting.executeScript:

executeScript(injection)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Injects a script into a target context. The script will be run at :code:`document_idle`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``injection``
      :type: (:ref:`scripting.ScriptInjection`)

      The details of the script which to inject.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`scripting.InjectionResult`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.getRegisteredContentScripts:

getRegisteredContentScripts([filter])
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Returns all dynamically registered content scripts for this extension that match the given filter.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`scripting.ContentScriptFilter`, optional)

      An object to filter the extension's dynamically registered scripts.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`scripting.RegisteredContentScript`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.insertCSS:

insertCSS(injection)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Inserts a CSS stylesheet into a target context. If multiple frames are specified, unsuccessful injections are ignored.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``injection``
      :type: (:ref:`scripting.CSSInjection`)

      The details of the styles to insert.

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.registerContentScripts:

registerContentScripts(scripts)
-------------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Registers one or more content scripts for this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``scripts``
      :type: (array of :ref:`scripting.RegisteredContentScript`)

      Contains a list of scripts to be registered. If there are errors during script parsing/file validation, or if the IDs specified already exist, then no scripts are registered.

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.removeCSS:

removeCSS(injection)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Removes a CSS stylesheet that was previously inserted by this extension from a target context.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``injection``
      :type: (:ref:`scripting.CSSInjection`)

      The details of the styles to remove. Note that the :code:`css`, :code:`files`, and :code:`origin` properties must exactly match the stylesheet inserted through :code:`insertCSS`. Attempting to remove a non-existent stylesheet is a no-op.

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.unregisterContentScripts:

unregisterContentScripts([filter])
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Unregisters one or more content scripts for this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`scripting.ContentScriptFilter`, optional)

      If specified, only unregisters dynamic content scripts which match the filter. Otherwise, all of the extension's dynamic content scripts are unregistered.

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.updateContentScripts:

updateContentScripts(scripts)
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Updates one or more content scripts for this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``scripts``
      :type: (array of object)

      Contains a list of scripts to be updated. If there are errors during script parsing/file validation, or if the IDs specified do not already exist, then no scripts are updated.

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. rst-class:: api-main-section

Types
=====

.. _scripting.ContentScriptFilter:

ContentScriptFilter
-------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _scripting.ContentScriptFilter.ids:

   .. api-member::
      :name: [``ids``]
      :type: (array of string, optional)

      The IDs of specific scripts to retrieve with :code:`getRegisteredContentScripts()` or to unregister with :code:`unregisterContentScripts()`.

.. _scripting.CSSInjection:

CSSInjection
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _scripting.CSSInjection.target:

   .. api-member::
      :name: ``target``
      :type: (:ref:`scripting.InjectionTarget`)

      Details specifying the target into which to inject the CSS.

   .. _scripting.CSSInjection.css:

   .. api-member::
      :name: [``css``]
      :type: (string, optional)

      A string containing the CSS to inject. Exactly one of :code:`files` and :code:`css` must be specified.

   .. _scripting.CSSInjection.files:

   .. api-member::
      :name: [``files``]
      :type: (array of string, optional)

      The path of the CSS files to inject, relative to the extension's root directory. Exactly one of :code:`files` and :code:`css` must be specified.

   .. _scripting.CSSInjection.origin:

   .. api-member::
      :name: [``origin``]
      :type: (`string`, optional)

      The style origin for the injection. Defaults to :code:`'AUTHOR'`.

      Supported values:

      .. api-member::
         :name: :value:`USER`

      .. api-member::
         :name: :value:`AUTHOR`

.. _scripting.ExecutionWorld:

ExecutionWorld
--------------

.. api-section-annotation-hack:: -- [Added in TB 102]

The JavaScript world for a script to execute within. :code:`ISOLATED` is the default execution environment of content scripts, :code:`MAIN` is the web page's execution environment.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`ISOLATED`

         .. api-member::
            :name: :value:`MAIN`
            :annotation: -- [Added in TB 128]

.. _scripting.CSSOrigin:

CSSOrigin
---------

.. api-section-annotation-hack:: -- [Added in TB 53]

The origin of the CSS to inject, this affects the cascading order (priority) of the stylesheet.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`user`

         .. api-member::
            :name: :value:`author`

.. _scripting.RunAt:

RunAt
-----

.. api-section-annotation-hack:: -- [Added in TB 45]

The soonest that the JavaScript or CSS will be injected into the tab.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`document_start`

         .. api-member::
            :name: :value:`document_end`

         .. api-member::
            :name: :value:`document_idle`

.. _scripting.ExtensionURL:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _scripting.InjectionResult:

InjectionResult
---------------

.. api-section-annotation-hack:: 

Result of a script injection.

.. api-header::
   :label: object

   .. _scripting.InjectionResult.frameId:

   .. api-member::
      :name: ``frameId``
      :type: (integer)

      The frame ID associated with the injection.

   .. _scripting.InjectionResult.error:

   .. api-member::
      :name: [``error``]
      :type: (any, optional)

      The error property is set when the script execution failed. The value is typically an (Error) object with a message property, but could be any value (including primitives and undefined) if the script threw or rejected with such a value.

   .. _scripting.InjectionResult.result:

   .. api-member::
      :name: [``result``]
      :type: (any, optional)

      The result of the script execution.

.. _scripting.InjectionTarget:

InjectionTarget
---------------

.. api-section-annotation-hack:: -- [Added in TB 102]

.. api-header::
   :label: object

   .. _scripting.InjectionTarget.tabId:

   .. api-member::
      :name: ``tabId``
      :type: (number)

      The ID of the tab into which to inject.

   .. _scripting.InjectionTarget.allFrames:

   .. api-member::
      :name: [``allFrames``]
      :type: (boolean, optional)

      Whether the script should inject into all frames within the tab. Defaults to false. This must not be true if :code:`frameIds` is specified.

   .. _scripting.InjectionTarget.frameIds:

   .. api-member::
      :name: [``frameIds``]
      :type: (array of number, optional)

      The IDs of specific frames to inject into.

.. _scripting.RegisteredContentScript:

RegisteredContentScript
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

.. api-header::
   :label: object

   .. _scripting.RegisteredContentScript.id:

   .. api-member::
      :name: ``id``
      :type: (string)

      The id of the content script, specified in the API call.

   .. _scripting.RegisteredContentScript.allFrames:

   .. api-member::
      :name: [``allFrames``]
      :type: (boolean, optional)

      If specified true, it will inject into all frames, even if the frame is not the top-most frame in the tab. Each frame is checked independently for URL requirements; it will not inject into child frames if the URL requirements are not met. Defaults to false, meaning that only the top frame is matched.

   .. _scripting.RegisteredContentScript.css:

   .. api-member::
      :name: [``css``]
      :type: (array of :ref:`scripting.ExtensionURL`, optional)

      The list of CSS files to be injected into matching pages. These are injected in the order they appear in this array.

   .. _scripting.RegisteredContentScript.cssOrigin:

   .. api-member::
      :name: [``cssOrigin``]
      :type: (:ref:`scripting.CSSOrigin`, optional)

   .. _scripting.RegisteredContentScript.excludeMatches:

   .. api-member::
      :name: [``excludeMatches``]
      :type: (array of string, optional)

      Excludes pages that this content script would otherwise be injected into.

   .. _scripting.RegisteredContentScript.js:

   .. api-member::
      :name: [``js``]
      :type: (array of :ref:`scripting.ExtensionURL`, optional)

      The list of JavaScript files to be injected into matching pages. These are injected in the order they appear in this array.

   .. _scripting.RegisteredContentScript.matches:

   .. api-member::
      :name: [``matches``]
      :type: (array of string, optional)

      Specifies which pages this content script will be injected into. Must be specified for :code:`registerContentScripts()`.

   .. _scripting.RegisteredContentScript.matchOriginAsFallback:

   .. api-member::
      :name: [``matchOriginAsFallback``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 128]

      If matchOriginAsFallback is true, then the code is also injected in about:, data:, blob: when their origin matches the pattern in 'matches', even if the actual document origin is opaque (due to the use of CSP sandbox or iframe sandbox). Match patterns in 'matches' must specify a wildcard path glob. By default it is :code:`false`.

   .. _scripting.RegisteredContentScript.persistAcrossSessions:

   .. api-member::
      :name: [``persistAcrossSessions``]
      :type: (boolean, optional)

      Specifies if this content script will persist into future sessions. Defaults to true.

      .. note::

         Since Thunderbird 105, this option is optional and accepts any boolean value.

      .. note::

         Prior to Thunderbird 105, this option was required and only accepted the :code:`false` value.

   .. _scripting.RegisteredContentScript.runAt:

   .. api-member::
      :name: [``runAt``]
      :type: (:ref:`scripting.RunAt`, optional)

      Specifies when JavaScript files are injected into the web page. The preferred and default value is :code:`document_idle`.

   .. _scripting.RegisteredContentScript.world:

   .. api-member::
      :name: [``world``]
      :type: (:ref:`scripting.ExecutionWorld`, optional)
      :annotation: -- [Added in TB 128]

      The JavaScript world for a script to execute within. Defaults to "ISOLATED".

.. _scripting.ScriptInjection:

ScriptInjection
---------------

.. api-section-annotation-hack:: 

Details of a script injection

.. api-header::
   :label: object

   .. _scripting.ScriptInjection.target:

   .. api-member::
      :name: ``target``
      :type: (:ref:`scripting.InjectionTarget`)

      Details specifying the target into which to inject the script.

   .. _scripting.ScriptInjection.args:

   .. api-member::
      :name: [``args``]
      :type: (array of any, optional)

      The arguments to curry into a provided function. This is only valid if the :code:`func` parameter is specified. These arguments must be JSON-serializable.

   .. _scripting.ScriptInjection.files:

   .. api-member::
      :name: [``files``]
      :type: (array of string, optional)

      The path of the JS files to inject, relative to the extension's root directory. Exactly one of :code:`files` and :code:`func` must be specified.

   .. _scripting.ScriptInjection.func:

   .. api-member::
      :name: [``func``]
      :type: (function, optional)

      A JavaScript function to inject. This function will be serialized, and then deserialized for injection. This means that any bound parameters and execution context will be lost. Exactly one of :code:`files` and :code:`func` must be specified.

   .. _scripting.ScriptInjection.injectImmediately:

   .. api-member::
      :name: [``injectImmediately``]
      :type: (boolean, optional)

      Whether the injection should be triggered in the target as soon as possible (but not necessarily prior to page load).

   .. _scripting.ScriptInjection.world:

   .. api-member::
      :name: [``world``]
      :type: (:ref:`scripting.ExecutionWorld`, optional)
