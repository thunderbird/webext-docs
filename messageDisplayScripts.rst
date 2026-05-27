.. container:: sticky-sidebar

  ≡ messageDisplayScripts API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=========================
messageDisplayScripts API
=========================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

The messageDisplayScripts API allows to register and unregister scripts for the message display window.

.. rst-class:: api-main-section

Manifest file properties
========================

.. _message^display^scripts.compose_scripts:

.. api-member::
   :name: [``compose_scripts``]
   :refid: message-display-scripts-compose-scripts
   :refname: compose_scripts
   :type: (array of :ref:`compose^scripts.^compose^script`, optional)
   :annotation: -- [Added in TB 151]

   Scripts and CSS to inject into compose windows.

.. _message^display^scripts.message_display_scripts:

.. api-member::
   :name: [``message_display_scripts``]
   :refid: message-display-scripts-message-display-scripts
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

.. _message^display^scripts.permission.messages^modify:

.. api-member::
   :name: :permission:`messagesModify`
   :refid: message-display-scripts-permission-messages-modify
   :refname: messagesModify

   Read and modify your email messages as they are displayed to you.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messagesModify` is required to use ``messenger.messageDisplayScripts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _message^display^scripts.register:

register(messageDisplayScriptOptions)
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 82]

Register a message display script programmatically.

.. note::

   Registered scripts will only be applied to newly opened messages. To apply the script to already open messages, manually inject your script by calling :ref:`tabs.execute^script` for each of the open :value:`messageDisplay` tabs.

.. api-header::
   :label: Parameters

   .. _message^display^scripts.register.message^display^script^options:

   .. api-member::
      :name: ``messageDisplayScriptOptions``
      :refid: message-display-scripts-register-message-display-script-options
      :refname: messageDisplayScriptOptions
      :type: (:ref:`message^display^scripts.^registered^message^display^script^options`)

.. api-header::
   :label: Required permissions

   - :permission:`messagesModify`

.. rst-class:: api-main-section

Types
=====

.. _message^display^scripts.^compose^script:

ComposeScript
-------------

.. api-section-annotation-hack:: -- [Added in TB 151]

A script and/or CSS to inject into compose windows via the manifest.

.. note::

   The :value:`run_at` option is not supported for compose scripts, because the compose editor does not load content in the same way as a regular web page.

.. api-header::
   :label: object

   .. _message^display^scripts.^compose^script.css:

   .. api-member::
      :name: [``css``]
      :refid: message-display-scripts-compose-script-css
      :refname: css
      :type: (array of :ref:`message^display^scripts.^extension^u^r^l`, optional)

      The list of CSS files to inject.

   .. _message^display^scripts.^compose^script.js:

   .. api-member::
      :name: [``js``]
      :refid: message-display-scripts-compose-script-js
      :refname: js
      :type: (array of :ref:`message^display^scripts.^extension^u^r^l`, optional)

      The list of JavaScript files to inject.

.. _message^display^scripts.^extension^file^or^code:

ExtensionFileOrCode
-------------------

.. api-section-annotation-hack:: 

Specify code, either by pointing to a file or by providing the code directly. Only one of the two is allowed.

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _message^display^scripts.^extension^file^or^code.file:

         .. api-member::
            :name: ``file``
            :refid: message-display-scripts-extension-file-or-code-file
            :refname: file
            :type: (:ref:`message^display^scripts.^extension^u^r^l`)

            A URL relative to the extension's :value:`manifest.json` file, and pointing to a JavaScript file to register.

*or*

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _message^display^scripts.^extension^file^or^code.code:

         .. api-member::
            :name: ``code``
            :refid: message-display-scripts-extension-file-or-code-code
            :refname: code
            :type: (string)

            A string of JavaScript code to register.

.. _message^display^scripts.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _message^display^scripts.^message^display^script:

MessageDisplayScript
--------------------

.. api-section-annotation-hack:: -- [Added in TB 151]

A script and/or CSS to inject into message display pages via the manifest.

.. api-header::
   :label: object

   .. _message^display^scripts.^message^display^script.css:

   .. api-member::
      :name: [``css``]
      :refid: message-display-scripts-message-display-script-css
      :refname: css
      :type: (array of :ref:`message^display^scripts.^extension^u^r^l`, optional)

      The list of CSS files to inject.

   .. _message^display^scripts.^message^display^script.js:

   .. api-member::
      :name: [``js``]
      :refid: message-display-scripts-message-display-script-js
      :refname: js
      :type: (array of :ref:`message^display^scripts.^extension^u^r^l`, optional)

      The list of JavaScript files to inject.

   .. _message^display^scripts.^message^display^script.run_at:

   .. api-member::
      :name: [``run_at``]
      :refid: message-display-scripts-message-display-script-run-at
      :refname: run_at
      :type: (`string`, optional)

      Determines when the files specified in css and js are injected. The states directly correspond to :code:`Document.readyState`: :value:`loading`, :value:`interactive` and :value:`complete`.

      Supported values:

      .. _message^display^scripts.^message^display^script.run_at.document_end:

      .. api-member::
         :name: :value:`document_end`
         :refid: message-display-scripts-message-display-script-run-at-document-end
         :refname: document_end

      .. _message^display^scripts.^message^display^script.run_at.document_idle:

      .. api-member::
         :name: :value:`document_idle`
         :refid: message-display-scripts-message-display-script-run-at-document-idle
         :refname: document_idle

      .. _message^display^scripts.^message^display^script.run_at.document_start:

      .. api-member::
         :name: :value:`document_start`
         :refid: message-display-scripts-message-display-script-run-at-document-start
         :refname: document_start

.. _message^display^scripts.^registered^message^display^script:

RegisteredMessageDisplayScript
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 82]

An object that represents a message display script registered programmatically

.. api-header::
   :label: object

.. _message^display^scripts.^registered^message^display^script^options:

RegisteredMessageDisplayScriptOptions
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 82]

Details of a message display script registered programmatically

.. api-header::
   :label: object

   .. _message^display^scripts.^registered^message^display^script^options.css:

   .. api-member::
      :name: [``css``]
      :refid: message-display-scripts-registered-message-display-script-options-css
      :refname: css
      :type: (array of :ref:`message^display^scripts.^extension^file^or^code`, optional)

      The list of CSS files to inject

   .. _message^display^scripts.^registered^message^display^script^options.js:

   .. api-member::
      :name: [``js``]
      :refid: message-display-scripts-registered-message-display-script-options-js
      :refname: js
      :type: (array of :ref:`message^display^scripts.^extension^file^or^code`, optional)

      The list of JavaScript files to inject

   .. _message^display^scripts.^registered^message^display^script^options.run^at:

   .. api-member::
      :name: [``runAt``]
      :refid: message-display-scripts-registered-message-display-script-options-run-at
      :refname: runAt
      :type: (`string`, optional)
      :annotation: -- [Added in TB 126]

      Determines when the files specified in css and js are injected. The states directly correspond to :code:`Document.readyState`: :value:`loading`, :value:`interactive` and :value:`complete`

      Supported values:

      .. _message^display^scripts.^registered^message^display^script^options.run^at.document_end:

      .. api-member::
         :name: :value:`document_end`
         :refid: message-display-scripts-registered-message-display-script-options-run-at-document-end
         :refname: document_end

         Inject the script after the DOM is complete, but before subresources like images and frames have loaded.

      .. _message^display^scripts.^registered^message^display^script^options.run^at.document_idle:

      .. api-member::
         :name: :value:`document_idle`
         :refid: message-display-scripts-registered-message-display-script-options-run-at-document-idle
         :refname: document_idle

         Inject the script after the page is fully loaded. This is the default.

      .. _message^display^scripts.^registered^message^display^script^options.run^at.document_start:

      .. api-member::
         :name: :value:`document_start`
         :refid: message-display-scripts-registered-message-display-script-options-run-at-document-start
         :refname: document_start

         Inject the script after the document is created, but before any other content is loaded.
