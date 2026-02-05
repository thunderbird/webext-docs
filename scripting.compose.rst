.. container:: sticky-sidebar

  ≡ scripting.compose API

  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=====================
scripting.compose API
=====================

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _scripting.compose.permission.compose:

.. api-member::
   :name: :permission:`compose`
   :refid: scripting-compose-permission-compose
   :refname: compose

   Read and modify your email messages as you compose and send them.

.. _scripting.compose.permission.scripting:

.. api-member::
   :name: :permission:`scripting`
   :refid: scripting-compose-permission-scripting
   :refname: scripting

   Grant access to some or all methods of the scripting API.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`scripting` is required to use ``messenger.scripting.compose.*``.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`compose` is required to use ``messenger.scripting.compose.*``.

.. rst-class:: api-main-section

Functions
=========

.. _scripting.compose.get^registered^scripts:

getRegisteredScripts([filter])
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Returns all registered compose scripts for this extension that match the given filter.

.. api-header::
   :label: Parameters

   .. _scripting.compose.get^registered^scripts.filter:

   .. api-member::
      :name: [``filter``]
      :refid: scripting-compose-get-registered-scripts-filter
      :refname: filter
      :type: (:ref:`scripting.compose.^compose^script^filter`, optional)

      An object to filter the extension's registered compose scripts.

.. api-header::
   :label: Return type (`Promise`_)

   .. _scripting.compose.get^registered^scripts.returns:

   .. api-member::
      :refid: scripting-compose-get-registered-scripts-returns
      :refname: _returns
      :type: array of :ref:`scripting.compose.^compose^script^details`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`
   - :permission:`scripting`

.. _scripting.compose.register^scripts:

registerScripts(scripts)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Registers one or more compose scripts for this extension, which should be injected into the message compose editor.

.. note::

   Registered scripts will only be applied to newly opened message compose tabs. To apply the script to already open message compose tabs, manually inject your script by calling :ref:`scripting.execute^script` for each of the open :value:`messageCompose` tabs.

.. api-header::
   :label: Parameters

   .. _scripting.compose.register^scripts.scripts:

   .. api-member::
      :name: ``scripts``
      :refid: scripting-compose-register-scripts-scripts
      :refname: scripts
      :type: (array of :ref:`scripting.compose.^compose^script^details`)

      Contains a list of compose scripts to be registered. If there are errors during script parsing/file validation, or if the IDs specified already exist, then no scripts are registered.

.. api-header::
   :label: Required permissions

   - :permission:`compose`
   - :permission:`scripting`

.. _scripting.compose.unregister^scripts:

unregisterScripts([filter])
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Unregisters one or more compose scripts for this extension.

.. api-header::
   :label: Parameters

   .. _scripting.compose.unregister^scripts.filter:

   .. api-member::
      :name: [``filter``]
      :refid: scripting-compose-unregister-scripts-filter
      :refname: filter
      :type: (:ref:`scripting.compose.^compose^script^filter`, optional)

      If specified, only unregisters compose scripts which match the filter. Otherwise, all of the extension's compose scripts are unregistered.

.. api-header::
   :label: Required permissions

   - :permission:`compose`
   - :permission:`scripting`

.. rst-class:: api-main-section

Types
=====

.. _scripting.compose.^compose^script^details:

ComposeScriptDetails
--------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

.. api-header::
   :label: object

   .. _scripting.compose.^compose^script^details.id:

   .. api-member::
      :name: ``id``
      :refid: scripting-compose-compose-script-details-id
      :refname: id
      :type: (string)

      The id of the compose script, specified in the API call.

   .. _scripting.compose.^compose^script^details.css:

   .. api-member::
      :name: [``css``]
      :refid: scripting-compose-compose-script-details-css
      :refname: css
      :type: (array of :ref:`scripting.compose.^extension^u^r^l`, optional)

      The list of CSS files to be injected. These are injected in the order they appear in this array.

   .. _scripting.compose.^compose^script^details.js:

   .. api-member::
      :name: [``js``]
      :refid: scripting-compose-compose-script-details-js
      :refname: js
      :type: (array of :ref:`scripting.compose.^extension^u^r^l`, optional)

      The list of JavaScript files to be injected. These are injected in the order they appear in this array.

   .. _scripting.compose.^compose^script^details.run^at:

   .. api-member::
      :name: [``runAt``]
      :refid: scripting-compose-compose-script-details-run-at
      :refname: runAt
      :type: (:ref:`scripting.compose.^run^at`, optional)

      Specifies when JavaScript files are injected. The preferred and default value is :code:`document_idle`.

.. _scripting.compose.^compose^script^filter:

ComposeScriptFilter
-------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

.. api-header::
   :label: object

   .. _scripting.compose.^compose^script^filter.ids:

   .. api-member::
      :name: [``ids``]
      :refid: scripting-compose-compose-script-filter-ids
      :refname: ids
      :type: (array of string, optional)

      The IDs of specific compose scripts to retrieve with :code:`getRegisteredScripts()` or to unregister with :code:`unregisterScripts()`.

.. _scripting.compose.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _scripting.compose.^run^at:

RunAt
-----

.. api-section-annotation-hack:: -- [Added in TB 45]

The soonest that the JavaScript or CSS will be injected into the tab.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _scripting.compose.^run^at.document_end:

         .. api-member::
            :name: :value:`document_end`
            :refid: scripting-compose-run-at-document-end
            :refname: document_end

         .. _scripting.compose.^run^at.document_idle:

         .. api-member::
            :name: :value:`document_idle`
            :refid: scripting-compose-run-at-document-idle
            :refname: document_idle

         .. _scripting.compose.^run^at.document_start:

         .. api-member::
            :name: :value:`document_start`
            :refid: scripting-compose-run-at-document-start
            :refname: document_start
