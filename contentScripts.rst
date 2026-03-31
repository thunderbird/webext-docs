.. container:: sticky-sidebar

  ≡ contentScripts API

  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

==================
contentScripts API
==================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The contentScripts API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

.. rst-class:: api-main-section

Functions
=========

.. _content^scripts.register:

register(contentScriptOptions)
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 59]

Register a content script programmatically

.. api-header::
   :label: Parameters

   .. _content^scripts.register.content^script^options:

   .. api-member::
      :name: ``contentScriptOptions``
      :refid: content-scripts-register-content-script-options
      :refname: contentScriptOptions
      :type: (:ref:`content^scripts.^registered^content^script^options`)

.. rst-class:: api-main-section

Types
=====

.. _content^scripts.^c^s^s^origin:

CSSOrigin
---------

.. api-section-annotation-hack:: -- [Added in TB 53]

The origin of the CSS to inject, this affects the cascading order (priority) of the stylesheet.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _content^scripts.^c^s^s^origin.author:

         .. api-member::
            :name: :value:`author`
            :refid: content-scripts-c-s-s-origin-author
            :refname: author

         .. _content^scripts.^c^s^s^origin.user:

         .. api-member::
            :name: :value:`user`
            :refid: content-scripts-c-s-s-origin-user
            :refname: user

.. _content^scripts.^execution^world:

ExecutionWorld
--------------

.. api-section-annotation-hack:: 

The JavaScript world for a script to execute within. :code:`ISOLATED` is the default execution environment of content scripts, :code:`MAIN` is the web page's execution environment.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _content^scripts.^execution^world.^i^s^o^l^a^t^e^d:

         .. api-member::
            :name: :value:`ISOLATED`
            :refid: content-scripts-execution-world-i-s-o-l-a-t-e-d
            :refname: ISOLATED

         .. _content^scripts.^execution^world.^m^a^i^n:

         .. api-member::
            :name: :value:`MAIN`
            :refid: content-scripts-execution-world-m-a-i-n
            :refname: MAIN

.. _content^scripts.^extension^file^or^code:

ExtensionFileOrCode
-------------------

.. api-section-annotation-hack:: 

Specify code, either by pointing to a file or by providing the code directly. Only one of the two is allowed.

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _content^scripts.^extension^file^or^code.file:

         .. api-member::
            :name: ``file``
            :refid: content-scripts-extension-file-or-code-file
            :refname: file
            :type: (:ref:`content^scripts.^extension^u^r^l`)

            A URL relative to the extension's :value:`manifest.json` file, and pointing to a JavaScript file to register.

*or*

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _content^scripts.^extension^file^or^code.code:

         .. api-member::
            :name: ``code``
            :refid: content-scripts-extension-file-or-code-code
            :refname: code
            :type: (string)

            A string of JavaScript code to register.

.. _content^scripts.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _content^scripts.^match^pattern:

MatchPattern
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _content^scripts.^match^pattern.<all_urls>:

         .. api-member::
            :name: :value:`<all_urls>`
            :refid: content-scripts-match-pattern-all-urls
            :refname: <all_urls>

*or*

.. api-header::
   :label: :ref:`content^scripts.^match^pattern^restricted`

*or*

.. api-header::
   :label: :ref:`content^scripts.^match^pattern^unestricted`

.. _content^scripts.^match^pattern^restricted:

MatchPatternRestricted
----------------------

.. api-section-annotation-hack:: 

Same as MatchPattern above, but excludes <all_urls>

.. api-header::
   :label: string

*or*

.. api-header::
   :label: string

.. _content^scripts.^match^pattern^unestricted:

MatchPatternUnestricted
-----------------------

.. api-section-annotation-hack:: 

Mostly unrestricted match patterns for privileged add-ons. This should technically be rejected for unprivileged add-ons, but, reasons. The MatchPattern class will still refuse privileged schemes for those extensions.

.. api-header::
   :label: string

.. _content^scripts.^registered^content^script:

RegisteredContentScript
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 59]

An object that represents a content script registered programmatically

.. api-header::
   :label: object

.. _content^scripts.^registered^content^script^options:

RegisteredContentScriptOptions
------------------------------

.. api-section-annotation-hack:: 

Details of a content script registered programmatically

.. api-header::
   :label: object

   .. _content^scripts.^registered^content^script^options.matches:

   .. api-member::
      :name: ``matches``
      :refid: content-scripts-registered-content-script-options-matches
      :refname: matches
      :type: (array of :ref:`content^scripts.^match^pattern`)

   .. _content^scripts.^registered^content^script^options.all^frames:

   .. api-member::
      :name: [``allFrames``]
      :refid: content-scripts-registered-content-script-options-all-frames
      :refname: allFrames
      :type: (boolean, optional)

      If allFrames is :code:`true`, implies that the JavaScript or CSS should be injected into all frames of current page. By default, it's :code:`false` and is only injected into the top frame.

   .. _content^scripts.^registered^content^script^options.cookie^store^id:

   .. api-member::
      :name: [``cookieStoreId``]
      :refid: content-scripts-registered-content-script-options-cookie-store-id
      :refname: cookieStoreId
      :type: (array of string or string, optional)

      limit the set of matched tabs to those that belong to the given cookie store id

   .. _content^scripts.^registered^content^script^options.css:

   .. api-member::
      :name: [``css``]
      :refid: content-scripts-registered-content-script-options-css
      :refname: css
      :type: (array of :ref:`content^scripts.^extension^file^or^code`, optional)

      The list of CSS files to inject

   .. _content^scripts.^registered^content^script^options.css^origin:

   .. api-member::
      :name: [``cssOrigin``]
      :refid: content-scripts-registered-content-script-options-css-origin
      :refname: cssOrigin
      :type: (:ref:`content^scripts.^c^s^s^origin`, optional)

      The css origin of the stylesheet to inject. Defaults to "author".

   .. _content^scripts.^registered^content^script^options.exclude^globs:

   .. api-member::
      :name: [``excludeGlobs``]
      :refid: content-scripts-registered-content-script-options-exclude-globs
      :refname: excludeGlobs
      :type: (array of string, optional)

   .. _content^scripts.^registered^content^script^options.exclude^matches:

   .. api-member::
      :name: [``excludeMatches``]
      :refid: content-scripts-registered-content-script-options-exclude-matches
      :refname: excludeMatches
      :type: (array of :ref:`content^scripts.^match^pattern`, optional)

   .. _content^scripts.^registered^content^script^options.include^globs:

   .. api-member::
      :name: [``includeGlobs``]
      :refid: content-scripts-registered-content-script-options-include-globs
      :refname: includeGlobs
      :type: (array of string, optional)

   .. _content^scripts.^registered^content^script^options.js:

   .. api-member::
      :name: [``js``]
      :refid: content-scripts-registered-content-script-options-js
      :refname: js
      :type: (array of :ref:`content^scripts.^extension^file^or^code`, optional)

      The list of JS files to inject

   .. _content^scripts.^registered^content^script^options.match^about^blank:

   .. api-member::
      :name: [``matchAboutBlank``]
      :refid: content-scripts-registered-content-script-options-match-about-blank
      :refname: matchAboutBlank
      :type: (boolean, optional)

      If matchAboutBlank is true, then the code is also injected in about:blank and about:srcdoc frames if your extension has access to its parent document. Ignored if matchOriginAsFallback is specified. By default it is :code:`false`.

   .. _content^scripts.^registered^content^script^options.match^origin^as^fallback:

   .. api-member::
      :name: [``matchOriginAsFallback``]
      :refid: content-scripts-registered-content-script-options-match-origin-as-fallback
      :refname: matchOriginAsFallback
      :type: (boolean, optional)

      If matchOriginAsFallback is true, then the code is also injected in about:, data:, blob: when their origin matches the pattern in 'matches', even if the actual document origin is opaque (due to the use of CSP sandbox or iframe sandbox). Match patterns in 'matches' must specify a wildcard path glob. By default it is :code:`false`.

   .. _content^scripts.^registered^content^script^options.run^at:

   .. api-member::
      :name: [``runAt``]
      :refid: content-scripts-registered-content-script-options-run-at
      :refname: runAt
      :type: (:ref:`content^scripts.^run^at`, optional)

      The soonest that the JavaScript or CSS will be injected into the tab. Defaults to "document_idle".

   .. _content^scripts.^registered^content^script^options.world:

   .. api-member::
      :name: [``world``]
      :refid: content-scripts-registered-content-script-options-world
      :refname: world
      :type: (:ref:`content^scripts.^execution^world`, optional)

      The JavaScript world for a script to execute within. Defaults to "ISOLATED".

.. _content^scripts.^run^at:

RunAt
-----

.. api-section-annotation-hack:: -- [Added in TB 45]

The soonest that the JavaScript or CSS will be injected into the tab.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _content^scripts.^run^at.document_end:

         .. api-member::
            :name: :value:`document_end`
            :refid: content-scripts-run-at-document-end
            :refname: document_end

         .. _content^scripts.^run^at.document_idle:

         .. api-member::
            :name: :value:`document_idle`
            :refid: content-scripts-run-at-document-idle
            :refname: document_idle

         .. _content^scripts.^run^at.document_start:

         .. api-member::
            :name: :value:`document_start`
            :refid: content-scripts-run-at-document-start
            :refname: document_start
