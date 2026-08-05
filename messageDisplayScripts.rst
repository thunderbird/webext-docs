.. container:: sticky-sidebar

  ≡ messageDisplayScripts API

  * `Manifest file properties`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=========================
messageDisplayScripts API
=========================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. rst-class:: api-main-section

Manifest file properties
========================

.. _message^display^scripts.compose_scripts:

.. api-member::
   :name: [``compose_scripts``]
   :refid: message-display-scripts-compose-scripts
   :refname: compose_scripts
   :type: (array of :ref:`compose^scripts.^compose^script`, optional)
   :annotation: -- [Added in TB 153.0]

   Scripts and CSS to inject into compose windows.

.. _message^display^scripts.message_display_scripts:

.. api-member::
   :name: [``message_display_scripts``]
   :refid: message-display-scripts-message-display-scripts
   :refname: message_display_scripts
   :type: (array of :ref:`compose^scripts.^message^display^script`, optional)
   :annotation: -- [Added in TB 153.0]

   Scripts and CSS to inject into message display pages.

.. rst-class:: api-main-section

Types
=====

.. _message^display^scripts.^compose^script:

ComposeScript
-------------

.. api-section-annotation-hack:: -- [Added in TB 153.0]

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

.. api-section-annotation-hack:: -- [Added in TB 153.0]

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
