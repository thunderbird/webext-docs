.. container:: sticky-sidebar

  ≡ composeScripts API

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
