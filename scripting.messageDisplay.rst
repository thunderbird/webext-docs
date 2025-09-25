.. container:: sticky-sidebar

  ≡ scripting.messageDisplay API

  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

============================
scripting.messageDisplay API
============================

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`messagesRead`

   Read your email messages

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messagesRead` is required to use ``messenger.scripting.messageDisplay.*``.

.. rst-class:: api-main-section

Functions
=========

.. _scripting.messageDisplay.getRegisteredScripts:

getRegisteredScripts([filter])
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Returns all registered message display scripts for this extension that match the given filter.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`scripting.messageDisplay.MessageDisplayScriptFilter`, optional)

      An object to filter the extension's registered message display scripts.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`scripting.messageDisplay.MessageDisplayScriptDetails`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _scripting.messageDisplay.registerScripts:

registerScripts(scripts)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Registers one or more message display scripts for this extension, which should be injected into displayed messages.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``scripts``
      :type: (array of :ref:`scripting.messageDisplay.MessageDisplayScriptDetails`)

      Contains a list of message display scripts to be registered. If there are errors during script parsing/file validation, or if the IDs specified already exist, then no scripts are registered.

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _scripting.messageDisplay.unregisterScripts:

unregisterScripts([filter])
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Unregisters one or more message display scripts for this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`scripting.messageDisplay.MessageDisplayScriptFilter`, optional)

      If specified, only unregisters message display scripts which match the filter. Otherwise, all of the extension's message display scripts are unregistered.

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. rst-class:: api-main-section

Types
=====

.. _scripting.messageDisplay.RunAt:

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

.. _scripting.messageDisplay.ExtensionURL:

ExtensionURL
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string

.. _scripting.messageDisplay.MessageDisplayScriptDetails:

MessageDisplayScriptDetails
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

.. api-header::
   :label: object

   .. api-member::
      :name: ``id``
      :type: (string)

      The id of the message display script, specified in the API call.

   .. api-member::
      :name: [``css``]
      :type: (array of :ref:`scripting.messageDisplay.ExtensionURL`, optional)

      The list of CSS files to be injected. These are injected in the order they appear in this array.

   .. api-member::
      :name: [``js``]
      :type: (array of :ref:`scripting.messageDisplay.ExtensionURL`, optional)

      The list of JavaScript files to be injected. These are injected in the order they appear in this array.

   .. api-member::
      :name: [``runAt``]
      :type: (:ref:`scripting.messageDisplay.RunAt`, optional)

      Specifies when JavaScript files are injected. The preferred and default value is :code:`document_idle`.

.. _scripting.messageDisplay.MessageDisplayScriptFilter:

MessageDisplayScriptFilter
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

.. api-header::
   :label: object

   .. api-member::
      :name: [``ids``]
      :type: (array of string, optional)

      The IDs of specific message display scripts to retrieve with :code:`getRegisteredScripts()` or to unregister with :code:`unregisterScripts()`.
