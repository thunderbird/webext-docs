.. container:: sticky-sidebar

  ≡ composeScripts API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

==================
composeScripts API
==================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

The composeScripts API allows to register and unregister scripts for the message compose window.

.. rst-class:: api-main-section

Manifest file properties
========================

.. _compose^scripts.compose_scripts:

.. api-member::
   :name: [``compose_scripts``]
   :refid: compose-scripts-compose-scripts
   :refname: compose_scripts
   :type: (array of :ref:`compose^scripts.^compose^script`, optional)
   :annotation: -- [Added in TB 151]

   Scripts and CSS to inject into compose windows.

.. _compose^scripts.message_display_scripts:

.. api-member::
   :name: [``message_display_scripts``]
   :refid: compose-scripts-message-display-scripts
   :refname: message_display_scripts
   :type: (array of :ref:`compose^scripts.^message^display^script`, optional)
   :annotation: -- [Added in TB 151]

   Scripts and CSS to inject into message display pages.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _compose^scripts.permission.compose:

.. api-member::
   :name: :permission:`compose`
   :refid: compose-scripts-permission-compose
   :refname: compose

   Read and modify your email messages as you compose and send them.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`compose` is required to use ``messenger.composeScripts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _compose^scripts.register:

register(composeScriptOptions)
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 82]

Register a compose script programmatically.

.. note::

   Registered scripts will only be applied to newly opened message composer tabs. To apply the script to already open message composer tab, manually inject your script by calling :ref:`tabs.execute^script` for each of the open :value:`messageCompose` tabs.

.. api-header::
   :label: Parameters

   .. _compose^scripts.register.compose^script^options:

   .. api-member::
      :name: ``composeScriptOptions``
      :refid: compose-scripts-register-compose-script-options
      :refname: composeScriptOptions
      :type: (:ref:`compose^scripts.^registered^compose^script^options`)

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. rst-class:: api-main-section

Types
=====

.. _compose^scripts.^compose^script:

ComposeScript
-------------

.. api-section-annotation-hack:: -- [Added in TB 151]

A script and/or CSS to inject into compose windows via the manifest.

.. note::

   The :value:`run_at` option is not supported for compose scripts, because the compose editor does not load content in the same way as a regular web page.

.. api-header::
   :label: object

   .. _compose^scripts.^compose^script.css:

   .. api-member::
      :name: [``css``]
      :refid: compose-scripts-compose-script-css
      :refname: css
      :type: (array of :ref:`compose^scripts.^extension^u^r^l`, optional)

      The list of CSS files to inject.

   .. _compose^scripts.^compose^script.js:

   .. api-member::
      :name: [``js``]
      :refid: compose-scripts-compose-script-js
      :refname: js
      :type: (array of :ref:`compose^scripts.^extension^u^r^l`, optional)

      The list of JavaScript files to inject.

.. _compose^scripts.^extension^file^or^code:

ExtensionFileOrCode
-------------------

.. api-section-annotation-hack:: 

Specify code, either by pointing to a file or by providing the code directly. Only one of the two is allowed.

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _compose^scripts.^extension^file^or^code.file:

         .. api-member::
            :name: ``file``
            :refid: compose-scripts-extension-file-or-code-file
            :refname: file
            :type: (:ref:`compose^scripts.^extension^u^r^l`)

            A URL relative to the extension's :value:`manifest.json` file, and pointing to a JavaScript file to register.

*or*

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _compose^scripts.^extension^file^or^code.code:

         .. api-member::
            :name: ``code``
            :refid: compose-scripts-extension-file-or-code-code
            :refname: code
            :type: (string)

            A string of JavaScript code to register.

.. _compose^scripts.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _compose^scripts.^message^display^script:

MessageDisplayScript
--------------------

.. api-section-annotation-hack:: -- [Added in TB 151]

A script and/or CSS to inject into message display pages via the manifest.

.. api-header::
   :label: object

   .. _compose^scripts.^message^display^script.css:

   .. api-member::
      :name: [``css``]
      :refid: compose-scripts-message-display-script-css
      :refname: css
      :type: (array of :ref:`compose^scripts.^extension^u^r^l`, optional)

      The list of CSS files to inject.

   .. _compose^scripts.^message^display^script.js:

   .. api-member::
      :name: [``js``]
      :refid: compose-scripts-message-display-script-js
      :refname: js
      :type: (array of :ref:`compose^scripts.^extension^u^r^l`, optional)

      The list of JavaScript files to inject.

   .. _compose^scripts.^message^display^script.run_at:

   .. api-member::
      :name: [``run_at``]
      :refid: compose-scripts-message-display-script-run-at
      :refname: run_at
      :type: (`string`, optional)

      Determines when the files specified in css and js are injected. The states directly correspond to :code:`Document.readyState`: :value:`loading`, :value:`interactive` and :value:`complete`.

      Supported values:

      .. _compose^scripts.^message^display^script.run_at.document_end:

      .. api-member::
         :name: :value:`document_end`
         :refid: compose-scripts-message-display-script-run-at-document-end
         :refname: document_end

      .. _compose^scripts.^message^display^script.run_at.document_idle:

      .. api-member::
         :name: :value:`document_idle`
         :refid: compose-scripts-message-display-script-run-at-document-idle
         :refname: document_idle

      .. _compose^scripts.^message^display^script.run_at.document_start:

      .. api-member::
         :name: :value:`document_start`
         :refid: compose-scripts-message-display-script-run-at-document-start
         :refname: document_start

.. _compose^scripts.^registered^compose^script:

RegisteredComposeScript
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 82]

An object that represents a compose script registered programmatically.

.. api-header::
   :label: object

.. _compose^scripts.^registered^compose^script^options:

RegisteredComposeScriptOptions
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 82]

Details of a compose script registered programmatically.

.. api-header::
   :label: object

   .. _compose^scripts.^registered^compose^script^options.css:

   .. api-member::
      :name: [``css``]
      :refid: compose-scripts-registered-compose-script-options-css
      :refname: css
      :type: (array of :ref:`compose^scripts.^extension^file^or^code`, optional)

      The list of CSS files to inject.

   .. _compose^scripts.^registered^compose^script^options.js:

   .. api-member::
      :name: [``js``]
      :refid: compose-scripts-registered-compose-script-options-js
      :refname: js
      :type: (array of :ref:`compose^scripts.^extension^file^or^code`, optional)

      The list of JavaScript files to inject.
