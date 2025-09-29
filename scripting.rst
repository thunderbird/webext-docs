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

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

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

.. _scripting.execute^script:

executeScript(injection)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Injects a script into a target context. The script will be run at :code:`document_idle`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``injection``
      :type: (:ref:`scripting.^script^injection`)

      The details of the script which to inject.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`scripting.^injection^result`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.get^registered^content^scripts:

getRegisteredContentScripts([filter])
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Returns all dynamically registered content scripts for this extension that match the given filter.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`scripting.^content^script^filter`, optional)

      An object to filter the extension's dynamically registered scripts.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`scripting.^registered^content^script`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.insert^c^s^s:

insertCSS(injection)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Inserts a CSS stylesheet into a target context. If multiple frames are specified, unsuccessful injections are ignored.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``injection``
      :type: (:ref:`scripting.^c^s^s^injection`)

      The details of the styles to insert.

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.register^content^scripts:

registerContentScripts(scripts)
-------------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Registers one or more content scripts for this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``scripts``
      :type: (array of :ref:`scripting.^registered^content^script`)

      Contains a list of scripts to be registered. If there are errors during script parsing/file validation, or if the IDs specified already exist, then no scripts are registered.

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.remove^c^s^s:

removeCSS(injection)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Removes a CSS stylesheet that was previously inserted by this extension from a target context.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``injection``
      :type: (:ref:`scripting.^c^s^s^injection`)

      The details of the styles to remove. Note that the :code:`css`, :code:`files`, and :code:`origin` properties must exactly match the stylesheet inserted through :code:`insertCSS`. Attempting to remove a non-existent stylesheet is a no-op.

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.unregister^content^scripts:

unregisterContentScripts([filter])
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Unregisters one or more content scripts for this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`scripting.^content^script^filter`, optional)

      If specified, only unregisters dynamic content scripts which match the filter. Otherwise, all of the extension's dynamic content scripts are unregistered.

.. api-header::
   :label: Required permissions

   - :permission:`scripting`

.. _scripting.update^content^scripts:

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

.. _scripting.^content^script^filter:

ContentScriptFilter
-------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _scripting.^content^script^filter.ids:

   .. api-member::
      :name: [``ids``]
      :type: (array of string, optional)

      The IDs of specific scripts to retrieve with :code:`getRegisteredContentScripts()` or to unregister with :code:`unregisterContentScripts()`.

.. _scripting.^c^s^s^injection:

CSSInjection
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _scripting.^c^s^s^injection.target:

   .. api-member::
      :name: ``target``
      :type: (:ref:`scripting.^injection^target`)

      Details specifying the target into which to inject the CSS.

   .. _scripting.^c^s^s^injection.css:

   .. api-member::
      :name: [``css``]
      :type: (string, optional)

      A string containing the CSS to inject. Exactly one of :code:`files` and :code:`css` must be specified.

   .. _scripting.^c^s^s^injection.files:

   .. api-member::
      :name: [``files``]
      :type: (array of string, optional)

      The path of the CSS files to inject, relative to the extension's root directory. Exactly one of :code:`files` and :code:`css` must be specified.

   .. _scripting.^c^s^s^injection.origin:

   .. api-member::
      :name: [``origin``]
      :type: (`string`, optional)

      The style origin for the injection. Defaults to :code:`'AUTHOR'`.

      Supported values:

      .. api-member::
         :name: :value:`USER`

      .. api-member::
         :name: :value:`AUTHOR`

.. _scripting.^c^s^s^origin:

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

.. _scripting.^execution^world:

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

.. _scripting.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _scripting.^injection^result:

InjectionResult
---------------

.. api-section-annotation-hack:: 

Result of a script injection.

.. api-header::
   :label: object

   .. _scripting.^injection^result.frame^id:

   .. api-member::
      :name: ``frameId``
      :type: (integer)

      The frame ID associated with the injection.

   .. _scripting.^injection^result.error:

   .. api-member::
      :name: [``error``]
      :type: (any, optional)

      The error property is set when the script execution failed. The value is typically an (Error) object with a message property, but could be any value (including primitives and undefined) if the script threw or rejected with such a value.

   .. _scripting.^injection^result.result:

   .. api-member::
      :name: [``result``]
      :type: (any, optional)

      The result of the script execution.

.. _scripting.^injection^target:

InjectionTarget
---------------

.. api-section-annotation-hack:: -- [Added in TB 102]

.. api-header::
   :label: object

   .. _scripting.^injection^target.tab^id:

   .. api-member::
      :name: ``tabId``
      :type: (number)

      The ID of the tab into which to inject.

   .. _scripting.^injection^target.all^frames:

   .. api-member::
      :name: [``allFrames``]
      :type: (boolean, optional)

      Whether the script should inject into all frames within the tab. Defaults to false. This must not be true if :code:`frameIds` is specified.

   .. _scripting.^injection^target.frame^ids:

   .. api-member::
      :name: [``frameIds``]
      :type: (array of number, optional)

      The IDs of specific frames to inject into.

.. _scripting.^registered^content^script:

RegisteredContentScript
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

.. api-header::
   :label: object

   .. _scripting.^registered^content^script.id:

   .. api-member::
      :name: ``id``
      :type: (string)

      The id of the content script, specified in the API call.

   .. _scripting.^registered^content^script.all^frames:

   .. api-member::
      :name: [``allFrames``]
      :type: (boolean, optional)

      If specified true, it will inject into all frames, even if the frame is not the top-most frame in the tab. Each frame is checked independently for URL requirements; it will not inject into child frames if the URL requirements are not met. Defaults to false, meaning that only the top frame is matched.

   .. _scripting.^registered^content^script.css:

   .. api-member::
      :name: [``css``]
      :type: (array of :ref:`scripting.^extension^u^r^l`, optional)

      The list of CSS files to be injected into matching pages. These are injected in the order they appear in this array.

   .. _scripting.^registered^content^script.css^origin:

   .. api-member::
      :name: [``cssOrigin``]
      :type: (:ref:`scripting.^c^s^s^origin`, optional)

   .. _scripting.^registered^content^script.exclude^matches:

   .. api-member::
      :name: [``excludeMatches``]
      :type: (array of string, optional)

      Excludes pages that this content script would otherwise be injected into.

   .. _scripting.^registered^content^script.js:

   .. api-member::
      :name: [``js``]
      :type: (array of :ref:`scripting.^extension^u^r^l`, optional)

      The list of JavaScript files to be injected into matching pages. These are injected in the order they appear in this array.

   .. _scripting.^registered^content^script.matches:

   .. api-member::
      :name: [``matches``]
      :type: (array of string, optional)

      Specifies which pages this content script will be injected into. Must be specified for :code:`registerContentScripts()`.

   .. _scripting.^registered^content^script.match^origin^as^fallback:

   .. api-member::
      :name: [``matchOriginAsFallback``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 128]

      If matchOriginAsFallback is true, then the code is also injected in about:, data:, blob: when their origin matches the pattern in 'matches', even if the actual document origin is opaque (due to the use of CSP sandbox or iframe sandbox). Match patterns in 'matches' must specify a wildcard path glob. By default it is :code:`false`.

   .. _scripting.^registered^content^script.persist^across^sessions:

   .. api-member::
      :name: [``persistAcrossSessions``]
      :type: (boolean, optional)

      Specifies if this content script will persist into future sessions. Defaults to true.

      .. note::

         Since Thunderbird 105, this option is optional and accepts any boolean value.

      .. note::

         Prior to Thunderbird 105, this option was required and only accepted the :code:`false` value.

   .. _scripting.^registered^content^script.run^at:

   .. api-member::
      :name: [``runAt``]
      :type: (:ref:`scripting.^run^at`, optional)

      Specifies when JavaScript files are injected into the web page. The preferred and default value is :code:`document_idle`.

   .. _scripting.^registered^content^script.world:

   .. api-member::
      :name: [``world``]
      :type: (:ref:`scripting.^execution^world`, optional)
      :annotation: -- [Added in TB 128]

      The JavaScript world for a script to execute within. Defaults to "ISOLATED".

.. _scripting.^run^at:

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

.. _scripting.^script^injection:

ScriptInjection
---------------

.. api-section-annotation-hack:: 

Details of a script injection

.. api-header::
   :label: object

   .. _scripting.^script^injection.target:

   .. api-member::
      :name: ``target``
      :type: (:ref:`scripting.^injection^target`)

      Details specifying the target into which to inject the script.

   .. _scripting.^script^injection.args:

   .. api-member::
      :name: [``args``]
      :type: (array of any, optional)

      The arguments to curry into a provided function. This is only valid if the :code:`func` parameter is specified. These arguments must be JSON-serializable.

   .. _scripting.^script^injection.files:

   .. api-member::
      :name: [``files``]
      :type: (array of string, optional)

      The path of the JS files to inject, relative to the extension's root directory. Exactly one of :code:`files` and :code:`func` must be specified.

   .. _scripting.^script^injection.func:

   .. api-member::
      :name: [``func``]
      :type: (function, optional)

      A JavaScript function to inject. This function will be serialized, and then deserialized for injection. This means that any bound parameters and execution context will be lost. Exactly one of :code:`files` and :code:`func` must be specified.

   .. _scripting.^script^injection.inject^immediately:

   .. api-member::
      :name: [``injectImmediately``]
      :type: (boolean, optional)

      Whether the injection should be triggered in the target as soon as possible (but not necessarily prior to page load).

   .. _scripting.^script^injection.world:

   .. api-member::
      :name: [``world``]
      :type: (:ref:`scripting.^execution^world`, optional)
