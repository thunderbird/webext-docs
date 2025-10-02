.. container:: sticky-sidebar

  ≡ userScripts API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

===============
userScripts API
===============

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The userScripts API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/userScripts>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

.. note::

   Available for use with Manifest V3 only.

.. note::

   An incompatible version of this API is available for Manifest V2. See `userScripts (Legacy) <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/userScripts_legacy>`__.

.. rst-class:: api-main-section

Manifest file properties
========================

.. _user^scripts.user_scripts:

.. api-member::
   :name: [``user_scripts``]
   :refid: user-scripts-user-scripts
   :type: (object, optional)

   .. _user^scripts.user_scripts.api_script:

   .. api-member::
      :name: [``api_script``]
      :refid: user-scripts-user-scripts-api-script
      :type: (:ref:`user^scripts.^extension^u^r^l`, optional)

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _user^scripts.permission.user^scripts:

.. api-member::
   :name: :permission:`userScripts`
   :refid: user-scripts-permission-user-scripts

   Allow unverified third-party scripts to access your data.

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`user_scripts` is required to use ``messenger.userScripts.*``.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`userScripts` is required to use ``messenger.userScripts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _user^scripts.register:

register(userScriptOptions)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Register a user script programmatically given its :ref:`user^scripts.^user^script^options`, and resolves to an object with the unregister() function

.. note::

   An incompatible version of this function is available for Manifest V2. See `userScripts (Legacy) <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/userScripts_legacy/register>`__.

.. api-header::
   :label: Parameters

   .. _user^scripts.register.user^script^options:

   .. api-member::
      :name: ``userScriptOptions``
      :refid: user-scripts-register-user-script-options
      :type: (:ref:`user^scripts.^user^script^options`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _user^scripts.register.returns:

   .. api-member::
      :refid: user-scripts-register-returns
      :type: object

      An object that represents a user script registered programmatically

      .. _user^scripts.register.returns.unregister:

      .. api-member::
         :name: ``unregister``
         :refid: user-scripts-register-returns-unregister
         :type: (function)

         Unregister a user script registered programmatically

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. rst-class:: api-main-section

Events
======

.. _user^scripts.on^before^script:

onBeforeScript
--------------

.. api-section-annotation-hack:: 

Event called when a new userScript global has been created

.. api-header::
   :label: Parameters for onBeforeScript.addListener(listener)

   .. _user^scripts.on^before^script.listener(user^script):

   .. api-member::
      :name: ``listener(userScript)``
      :refid: user-scripts-on-before-script-listener-user-script

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _user^scripts.on^before^script.user^script:

   .. api-member::
      :name: ``userScript``
      :refid: user-scripts-on-before-script-user-script
      :type: (object)

      .. _user^scripts.on^before^script.user^script.define^globals:

      .. api-member::
         :name: ``defineGlobals``
         :refid: user-scripts-on-before-script-user-script-define-globals
         :type: (function)

         Exports all the properties of a given plain object as userScript globals

      .. _user^scripts.on^before^script.user^script.export:

      .. api-member::
         :name: ``export``
         :refid: user-scripts-on-before-script-user-script-export
         :type: (function)

         Convert a given value to make it accessible to the userScript code

      .. _user^scripts.on^before^script.user^script.global:

      .. api-member::
         :name: ``global``
         :refid: user-scripts-on-before-script-user-script-global
         :type: (any)

         The userScript global

      .. _user^scripts.on^before^script.user^script.metadata:

      .. api-member::
         :name: ``metadata``
         :refid: user-scripts-on-before-script-user-script-metadata
         :type: (any)

         The userScript metadata (as set in userScripts.register)

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. rst-class:: api-main-section

Types
=====

.. _user^scripts.^extension^file^or^code:

ExtensionFileOrCode
-------------------

.. api-section-annotation-hack:: 

Specify code, either by pointing to a file or by providing the code directly. Only one of the two is allowed.

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _user^scripts.^extension^file^or^code.file:

         .. api-member::
            :name: ``file``
            :refid: user-scripts-extension-file-or-code-file
            :type: (:ref:`user^scripts.^extension^u^r^l`)

            A URL relative to the extension's :value:`manifest.json` file, and pointing to a JavaScript file to register.

*or*

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _user^scripts.^extension^file^or^code.code:

         .. api-member::
            :name: ``code``
            :refid: user-scripts-extension-file-or-code-code
            :type: (string)

            A string of JavaScript code to register.

.. _user^scripts.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _user^scripts.^match^pattern:

MatchPattern
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _user^scripts.^match^pattern.<all_urls>:

         .. api-member::
            :name: :value:`<all_urls>`
            :refid: user-scripts-match-pattern-all-urls

*or*

.. api-header::
   :label: :ref:`user^scripts.^match^pattern^restricted`

*or*

.. api-header::
   :label: :ref:`user^scripts.^match^pattern^unestricted`

.. _user^scripts.^match^pattern^restricted:

MatchPatternRestricted
----------------------

.. api-section-annotation-hack:: 

Same as MatchPattern above, but excludes <all_urls>

.. api-header::
   :label: string

*or*

.. api-header::
   :label: string

.. _user^scripts.^match^pattern^unestricted:

MatchPatternUnestricted
-----------------------

.. api-section-annotation-hack:: 

Mostly unrestricted match patterns for privileged add-ons. This should technically be rejected for unprivileged add-ons, but, reasons. The MatchPattern class will still refuse privileged schemes for those extensions.

.. api-header::
   :label: string

.. _user^scripts.^plain^j^s^o^n^value:

PlainJSONValue
--------------

.. api-section-annotation-hack:: 

A plain JSON value

.. api-header::
   :label: null

*or*

.. api-header::
   :label: number

*or*

.. api-header::
   :label: string

*or*

.. api-header::
   :label: boolean

*or*

.. api-header::
   :label: array of :ref:`user^scripts.^plain^j^s^o^n^value`

*or*

.. api-header::
   :label: object

.. _user^scripts.^run^at:

RunAt
-----

.. api-section-annotation-hack:: -- [Added in TB 45]

The soonest that the JavaScript or CSS will be injected into the tab.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _user^scripts.^run^at.document_end:

         .. api-member::
            :name: :value:`document_end`
            :refid: user-scripts-run-at-document-end

         .. _user^scripts.^run^at.document_idle:

         .. api-member::
            :name: :value:`document_idle`
            :refid: user-scripts-run-at-document-idle

         .. _user^scripts.^run^at.document_start:

         .. api-member::
            :name: :value:`document_start`
            :refid: user-scripts-run-at-document-start

.. _user^scripts.^user^script^options:

UserScriptOptions
-----------------

.. api-section-annotation-hack:: 

Details of a user script

.. api-header::
   :label: object

   .. _user^scripts.^user^script^options.js:

   .. api-member::
      :name: ``js``
      :refid: user-scripts-user-script-options-js
      :type: (array of :ref:`user^scripts.^extension^file^or^code`)

      The list of JS files to inject

   .. _user^scripts.^user^script^options.matches:

   .. api-member::
      :name: ``matches``
      :refid: user-scripts-user-script-options-matches
      :type: (array of :ref:`user^scripts.^match^pattern`)

   .. _user^scripts.^user^script^options.all^frames:

   .. api-member::
      :name: [``allFrames``]
      :refid: user-scripts-user-script-options-all-frames
      :type: (boolean, optional)

      If allFrames is :code:`true`, implies that the JavaScript should be injected into all frames of current page. By default, it's :code:`false` and is only injected into the top frame.

   .. _user^scripts.^user^script^options.cookie^store^id:

   .. api-member::
      :name: [``cookieStoreId``]
      :refid: user-scripts-user-script-options-cookie-store-id
      :type: (array of string or string, optional)

      limit the set of matched tabs to those that belong to the given cookie store id

   .. _user^scripts.^user^script^options.exclude^globs:

   .. api-member::
      :name: [``excludeGlobs``]
      :refid: user-scripts-user-script-options-exclude-globs
      :type: (array of string, optional)

   .. _user^scripts.^user^script^options.exclude^matches:

   .. api-member::
      :name: [``excludeMatches``]
      :refid: user-scripts-user-script-options-exclude-matches
      :type: (array of :ref:`user^scripts.^match^pattern`, optional)

   .. _user^scripts.^user^script^options.include^globs:

   .. api-member::
      :name: [``includeGlobs``]
      :refid: user-scripts-user-script-options-include-globs
      :type: (array of string, optional)

   .. _user^scripts.^user^script^options.match^about^blank:

   .. api-member::
      :name: [``matchAboutBlank``]
      :refid: user-scripts-user-script-options-match-about-blank
      :type: (boolean, optional)

      If matchAboutBlank is true, then the code is also injected in about:blank and about:srcdoc frames if your extension has access to its parent document. Code cannot be inserted in top-level about:-frames. By default it is :code:`false`.

   .. _user^scripts.^user^script^options.run^at:

   .. api-member::
      :name: [``runAt``]
      :refid: user-scripts-user-script-options-run-at
      :type: (:ref:`user^scripts.^run^at`, optional)

      The soonest that the JavaScript will be injected into the tab. Defaults to "document_idle".

   .. _user^scripts.^user^script^options.script^metadata:

   .. api-member::
      :name: [``scriptMetadata``]
      :refid: user-scripts-user-script-options-script-metadata
      :type: (:ref:`user^scripts.^plain^j^s^o^n^value`, optional)

      An opaque user script metadata value
