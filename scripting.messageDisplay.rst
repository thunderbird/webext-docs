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

.. role:: small

The scripting.messageDisplay API allows to register and unregister scripts for the message display window.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _scripting.message^display.permission.messages^read:

.. api-member::
   :name: :permission:`messagesRead`
   :refid: scripting-message-display-permission-messages-read
   :refname: messagesRead

   Read your email messages.

.. _scripting.message^display.permission.scripting:

.. api-member::
   :name: :permission:`scripting`
   :refid: scripting-message-display-permission-scripting
   :refname: scripting

   Grant access to some or all methods of the scripting API.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`scripting` is required to use ``messenger.scripting.messageDisplay.*``.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messagesRead` is required to use ``messenger.scripting.messageDisplay.*``.

.. rst-class:: api-main-section

Functions
=========

.. _scripting.message^display.get^registered^scripts:

getRegisteredScripts([filter])
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Returns all registered message display scripts for this extension that match the given filter.

.. api-header::
   :label: Parameters

   .. _scripting.message^display.get^registered^scripts.filter:

   .. api-member::
      :name: [``filter``]
      :refid: scripting-message-display-get-registered-scripts-filter
      :refname: filter
      :type: (:ref:`scripting.message^display.^message^display^script^filter`, optional)

      An object to filter the extension's registered message display scripts.

.. api-header::
   :label: Return type (`Promise`_)

   .. _scripting.message^display.get^registered^scripts.returns:

   .. api-member::
      :refid: scripting-message-display-get-registered-scripts-returns
      :refname: _returns
      :type: array of :ref:`scripting.message^display.^message^display^script^details`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`scripting`

.. _scripting.message^display.register^scripts:

registerScripts(scripts)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Registers one or more message display scripts for this extension, which should be injected into displayed messages.

.. note::

   Registered scripts will only be applied to newly opened messages. To apply the script to already open messages, manually inject your script by calling :ref:`scripting.execute^script` for each of the open :value:`messageDisplay` tabs.

.. hint::

   There is a known issue in the logging mechanism of message display scripts: All entries logged to the console appear twice.

.. api-header::
   :label: Parameters

   .. _scripting.message^display.register^scripts.scripts:

   .. api-member::
      :name: ``scripts``
      :refid: scripting-message-display-register-scripts-scripts
      :refname: scripts
      :type: (array of :ref:`scripting.message^display.^message^display^script^details`)

      Contains a list of message display scripts to be registered. If there are errors during script parsing/file validation, or if the IDs specified already exist, then no scripts are registered.

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`scripting`

.. _scripting.message^display.unregister^scripts:

unregisterScripts([filter])
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Unregisters one or more message display scripts for this extension.

.. api-header::
   :label: Parameters

   .. _scripting.message^display.unregister^scripts.filter:

   .. api-member::
      :name: [``filter``]
      :refid: scripting-message-display-unregister-scripts-filter
      :refname: filter
      :type: (:ref:`scripting.message^display.^message^display^script^filter`, optional)

      If specified, only unregisters message display scripts which match the filter. Otherwise, all of the extension's message display scripts are unregistered.

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`scripting`

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

.. api-section-annotation-hack:: -- [Added in TB 128.0]

.. api-header::
   :label: object

   .. _scripting.message^display.^message^display^script^details.id:

   .. api-member::
      :name: ``id``
      :refid: scripting-message-display-message-display-script-details-id
      :refname: id
      :type: (string)

      The id of the message display script, specified in the API call.

   .. _scripting.message^display.^message^display^script^details.css:

   .. api-member::
      :name: [``css``]
      :refid: scripting-message-display-message-display-script-details-css
      :refname: css
      :type: (array of :ref:`scripting.message^display.^extension^u^r^l`, optional)

      The list of CSS files to be injected. These are injected in the order they appear in this array.

   .. _scripting.message^display.^message^display^script^details.js:

   .. api-member::
      :name: [``js``]
      :refid: scripting-message-display-message-display-script-details-js
      :refname: js
      :type: (array of :ref:`scripting.message^display.^extension^u^r^l`, optional)

      The list of JavaScript files to be injected. These are injected in the order they appear in this array.

   .. _scripting.message^display.^message^display^script^details.run^at:

   .. api-member::
      :name: [``runAt``]
      :refid: scripting-message-display-message-display-script-details-run-at
      :refname: runAt
      :type: (:ref:`scripting.message^display.^run^at`, optional)

      Specifies when JavaScript files are injected. The preferred and default value is :code:`document_idle`.

.. _scripting.message^display.^message^display^script^filter:

MessageDisplayScriptFilter
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

.. api-header::
   :label: object

   .. _scripting.message^display.^message^display^script^filter.ids:

   .. api-member::
      :name: [``ids``]
      :refid: scripting-message-display-message-display-script-filter-ids
      :refname: ids
      :type: (array of string, optional)

      The IDs of specific message display scripts to retrieve with :code:`getRegisteredScripts()` or to unregister with :code:`unregisterScripts()`.

.. _scripting.message^display.^run^at:

RunAt
-----

.. api-section-annotation-hack:: -- [Added in TB 60.0]

The soonest that the JavaScript or CSS will be injected into the tab.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _scripting.message^display.^run^at.document_end:

         .. api-member::
            :name: :value:`document_end`
            :refid: scripting-message-display-run-at-document-end
            :refname: document_end

         .. _scripting.message^display.^run^at.document_idle:

         .. api-member::
            :name: :value:`document_idle`
            :refid: scripting-message-display-run-at-document-idle
            :refname: document_idle

         .. _scripting.message^display.^run^at.document_start:

         .. api-member::
            :name: :value:`document_start`
            :refid: scripting-message-display-run-at-document-start
            :refname: document_start
