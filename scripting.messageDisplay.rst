.. container:: sticky-sidebar

  ≡ scripting.messageDisplay API

  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

============================
scripting.messageDisplay API
============================

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
   :name: :permission:`messagesRead`

   Read your email messages.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messagesRead` is required to use ``messenger.scripting.messageDisplay.*``.

.. rst-class:: api-main-section

Functions
=========

.. _scripting.message^display.get^registered^scripts:

getRegisteredScripts([filter])
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Returns all registered message display scripts for this extension that match the given filter.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`scripting.message^display.^message^display^script^filter`, optional)

      An object to filter the extension's registered message display scripts.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`scripting.message^display.^message^display^script^details`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _scripting.message^display.register^scripts:

registerScripts(scripts)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Registers one or more message display scripts for this extension, which should be injected into displayed messages.

.. note::

   Registered scripts will only be applied to newly opened messages. To apply the script to already open messages, manually inject your script by calling :ref:`scripting.execute^script` for each of the open :value:`messageDisplay` tabs.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``scripts``
      :type: (array of :ref:`scripting.message^display.^message^display^script^details`)

      Contains a list of message display scripts to be registered. If there are errors during script parsing/file validation, or if the IDs specified already exist, then no scripts are registered.

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _scripting.message^display.unregister^scripts:

unregisterScripts([filter])
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Unregisters one or more message display scripts for this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`scripting.message^display.^message^display^script^filter`, optional)

      If specified, only unregisters message display scripts which match the filter. Otherwise, all of the extension's message display scripts are unregistered.

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. rst-class:: api-main-section

Types
=====

.. _scripting.message^display.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _scripting.message^display.^message^display^script^details:

MessageDisplayScriptDetails
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

.. api-header::
   :label: object

   .. _scripting.message^display.^message^display^script^details.id:

   .. api-member::
      :name: ``id``
      :type: (string)

      The id of the message display script, specified in the API call.

   .. _scripting.message^display.^message^display^script^details.css:

   .. api-member::
      :name: [``css``]
      :type: (array of :ref:`scripting.message^display.^extension^u^r^l`, optional)

      The list of CSS files to be injected. These are injected in the order they appear in this array.

   .. _scripting.message^display.^message^display^script^details.js:

   .. api-member::
      :name: [``js``]
      :type: (array of :ref:`scripting.message^display.^extension^u^r^l`, optional)

      The list of JavaScript files to be injected. These are injected in the order they appear in this array.

   .. _scripting.message^display.^message^display^script^details.run^at:

   .. api-member::
      :name: [``runAt``]
      :type: (:ref:`scripting.message^display.^run^at`, optional)

      Specifies when JavaScript files are injected. The preferred and default value is :code:`document_idle`.

.. _scripting.message^display.^message^display^script^filter:

MessageDisplayScriptFilter
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

.. api-header::
   :label: object

   .. _scripting.message^display.^message^display^script^filter.ids:

   .. api-member::
      :name: [``ids``]
      :type: (array of string, optional)

      The IDs of specific message display scripts to retrieve with :code:`getRegisteredScripts()` or to unregister with :code:`unregisterScripts()`.

.. _scripting.message^display.^run^at:

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
