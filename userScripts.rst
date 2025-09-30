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

.. api-member::
   :name: [``user_scripts``]
   :type: (object, optional)

   .. api-member::
      :name: [``api_script``]
      :type: (:ref:`user^scripts.^extension^u^r^l`, optional)

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`userScripts`

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

   .. api-member::
      :name: ``userScriptOptions``
      :type: (:ref:`user^scripts.^user^script^options`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: object

      An object that represents a user script registered programmatically

      .. api-member::
         :name: ``unregister``
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

   .. api-member::
      :name: ``listener(userScript)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``userScript``
      :type: (object)

      .. api-member::
         :name: ``defineGlobals``
         :type: (function)

         Exports all the properties of a given plain object as userScript globals

      .. api-member::
         :name: ``export``
         :type: (function)

         Convert a given value to make it accessible to the userScript code

      .. api-member::
         :name: ``global``
         :type: (any)

         The userScript global

      .. api-member::
         :name: ``metadata``
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

         .. api-member::
            :name: ``file``
            :type: (:ref:`user^scripts.^extension^u^r^l`)

            A URL relative to the extension's :value:`manifest.json` file, and pointing to a JavaScript file to register.

*or*

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. api-member::
            :name: ``code``
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

         .. api-member::
            :name: :value:`<all_urls>`

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

         .. api-member::
            :name: :value:`document_end`

         .. api-member::
            :name: :value:`document_idle`

         .. api-member::
            :name: :value:`document_start`

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
      :type: (array of :ref:`user^scripts.^extension^file^or^code`)

      The list of JS files to inject

   .. _user^scripts.^user^script^options.matches:

   .. api-member::
      :name: ``matches``
      :type: (array of :ref:`user^scripts.^match^pattern`)

   .. _user^scripts.^user^script^options.all^frames:

   .. api-member::
      :name: [``allFrames``]
      :type: (boolean, optional)

      If allFrames is :code:`true`, implies that the JavaScript should be injected into all frames of current page. By default, it's :code:`false` and is only injected into the top frame.

   .. _user^scripts.^user^script^options.cookie^store^id:

   .. api-member::
      :name: [``cookieStoreId``]
      :type: (array of string or string, optional)

      limit the set of matched tabs to those that belong to the given cookie store id

   .. _user^scripts.^user^script^options.exclude^globs:

   .. api-member::
      :name: [``excludeGlobs``]
      :type: (array of string, optional)

   .. _user^scripts.^user^script^options.exclude^matches:

   .. api-member::
      :name: [``excludeMatches``]
      :type: (array of :ref:`user^scripts.^match^pattern`, optional)

   .. _user^scripts.^user^script^options.include^globs:

   .. api-member::
      :name: [``includeGlobs``]
      :type: (array of string, optional)

   .. _user^scripts.^user^script^options.match^about^blank:

   .. api-member::
      :name: [``matchAboutBlank``]
      :type: (boolean, optional)

      If matchAboutBlank is true, then the code is also injected in about:blank and about:srcdoc frames if your extension has access to its parent document. Code cannot be inserted in top-level about:-frames. By default it is :code:`false`.

   .. _user^scripts.^user^script^options.run^at:

   .. api-member::
      :name: [``runAt``]
      :type: (:ref:`user^scripts.^run^at`, optional)

      The soonest that the JavaScript will be injected into the tab. Defaults to "document_idle".

   .. _user^scripts.^user^script^options.script^metadata:

   .. api-member::
      :name: [``scriptMetadata``]
      :type: (:ref:`user^scripts.^plain^j^s^o^n^value`, optional)

      An opaque user script metadata value
