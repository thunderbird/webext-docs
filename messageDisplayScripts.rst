.. container:: sticky-sidebar

  ≡ messageDisplayScripts API

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

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`messagesModify`

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

   .. api-member::
      :name: ``messageDisplayScriptOptions``
      :type: (:ref:`message^display^scripts.^registered^message^display^script^options`)

.. api-header::
   :label: Required permissions

   - :permission:`messagesModify`

.. rst-class:: api-main-section

Types
=====

.. _message^display^scripts.^extension^file^or^code:

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
            :type: (:ref:`message^display^scripts.^extension^u^r^l`)

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

.. _message^display^scripts.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

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
      :type: (array of :ref:`message^display^scripts.^extension^file^or^code`, optional)

      The list of CSS files to inject

   .. _message^display^scripts.^registered^message^display^script^options.js:

   .. api-member::
      :name: [``js``]
      :type: (array of :ref:`message^display^scripts.^extension^file^or^code`, optional)

      The list of JavaScript files to inject

   .. _message^display^scripts.^registered^message^display^script^options.run^at:

   .. api-member::
      :name: [``runAt``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 126]

      Determines when the files specified in css and js are injected. The states directly correspond to :code:`Document.readyState`: :value:`loading`, :value:`interactive` and :value:`complete`

      Supported values:

      .. api-member::
         :name: :value:`document_end`

      .. api-member::
         :name: :value:`document_idle`

      .. api-member::
         :name: :value:`document_start`
