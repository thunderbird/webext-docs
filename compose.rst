.. container:: sticky-sidebar

  ≡ compose API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

===========
compose API
===========

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _compose.permission.accounts^read:

.. api-member::
   :name: :permission:`accountsRead`
   :refid: compose-permission-accounts-read

   See your mail accounts, their identities and their folders.

.. _compose.permission.compose:

.. api-member::
   :name: :permission:`compose`
   :refid: compose-permission-compose

   Read and modify your email messages as you compose and send them.

.. _compose.permission.compose.save:

.. api-member::
   :name: :permission:`compose.save`
   :refid: compose-permission-compose-save

   Save composed email messages as drafts or templates.

.. _compose.permission.compose.send:

.. api-member::
   :name: :permission:`compose.send`
   :refid: compose-permission-compose-send

   Send composed email messages on your behalf.

.. rst-class:: api-main-section

Functions
=========

.. _compose.add^attachment:

addAttachment(tabId, attachment)
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Adds an attachment to the message being composed in the specified tab.

.. api-header::
   :label: Parameters

   .. _compose.add^attachment.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-add-attachment-tab-id
      :type: (integer)

   .. _compose.add^attachment.attachment:

   .. api-member::
      :name: ``attachment``
      :refid: compose-add-attachment-attachment
      :type: (:ref:`compose.^file^attachment` or :ref:`compose.^compose^attachment`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.add^attachment.returns:

   .. api-member::
      :refid: compose-add-attachment-returns
      :type: :ref:`compose.^compose^attachment`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.begin^forward:

beginForward(messageId, [forwardType], [details])
-------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 67]

Open a new message compose window forwarding a given message.

.. note::

   The compose format can be set by :value:`details.isPlainText` or by specifying only one of :value:`details.body` or :value:`details.plainTextBody`. Otherwise the default compose format of the selected identity is used. If no identity is specified, this function is using the default identity and not the identity of the referenced message.

.. api-header::
   :label: Parameters

   .. _compose.begin^forward.message^id:

   .. api-member::
      :name: ``messageId``
      :refid: compose-begin-forward-message-id
      :type: (:ref:`messages.^message^id`)

      The message to forward, as retrieved using other APIs.

   .. _compose.begin^forward.forward^type:

   .. api-member::
      :name: [``forwardType``]
      :refid: compose-begin-forward-forward-type
      :type: (`string`, optional)

      Supported values:

      .. _compose.begin^forward.forward^type.forward^as^attachment:

      .. api-member::
         :name: :value:`forwardAsAttachment`
         :refid: compose-begin-forward-forward-type-forward-as-attachment

      .. _compose.begin^forward.forward^type.forward^inline:

      .. api-member::
         :name: :value:`forwardInline`
         :refid: compose-begin-forward-forward-type-forward-inline

   .. _compose.begin^forward.details:

   .. api-member::
      :name: [``details``]
      :refid: compose-begin-forward-details
      :type: (:ref:`compose.^compose^details`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.begin^forward.returns:

   .. api-member::
      :refid: compose-begin-forward-returns
      :type: :ref:`tabs.^tab`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.begin^new:

beginNew([messageId], [details])
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 67]

Open a new message compose window.

.. note::

   The compose format can be set by :value:`details.isPlainText` or by specifying only one of :value:`details.body` or :value:`details.plainTextBody`. Otherwise the default compose format of the selected identity is used. If no identity is specified, this function is using the default identity and not the identity of the referenced message.

.. api-header::
   :label: Parameters

   .. _compose.begin^new.message^id:

   .. api-member::
      :name: [``messageId``]
      :refid: compose-begin-new-message-id
      :type: (:ref:`messages.^message^id`, optional)

      If specified, the message or template to edit as a new message.

   .. _compose.begin^new.details:

   .. api-member::
      :name: [``details``]
      :refid: compose-begin-new-details
      :type: (:ref:`compose.^compose^details`, optional)
      :annotation: -- [Added in TB 84]

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.begin^new.returns:

   .. api-member::
      :refid: compose-begin-new-returns
      :type: :ref:`tabs.^tab`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.begin^reply:

beginReply(messageId, [replyType], [details])
---------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 67]

Open a new message compose window replying to a given message.

.. note::

   The compose format can be set by :value:`details.isPlainText` or by specifying only one of :value:`details.body` or :value:`details.plainTextBody`. Otherwise the default compose format of the selected identity is used. If no identity is specified, this function is using the default identity and not the identity of the referenced message.

.. api-header::
   :label: Parameters

   .. _compose.begin^reply.message^id:

   .. api-member::
      :name: ``messageId``
      :refid: compose-begin-reply-message-id
      :type: (:ref:`messages.^message^id`)

      The message to reply to, as retrieved using other APIs.

   .. _compose.begin^reply.reply^type:

   .. api-member::
      :name: [``replyType``]
      :refid: compose-begin-reply-reply-type
      :type: (`string`, optional)

      Supported values:

      .. _compose.begin^reply.reply^type.reply^to^all:

      .. api-member::
         :name: :value:`replyToAll`
         :refid: compose-begin-reply-reply-type-reply-to-all

      .. _compose.begin^reply.reply^type.reply^to^list:

      .. api-member::
         :name: :value:`replyToList`
         :refid: compose-begin-reply-reply-type-reply-to-list

      .. _compose.begin^reply.reply^type.reply^to^sender:

      .. api-member::
         :name: :value:`replyToSender`
         :refid: compose-begin-reply-reply-type-reply-to-sender

   .. _compose.begin^reply.details:

   .. api-member::
      :name: [``details``]
      :refid: compose-begin-reply-details
      :type: (:ref:`compose.^compose^details`, optional)
      :annotation: -- [Added in TB 76]

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.begin^reply.returns:

   .. api-member::
      :refid: compose-begin-reply-returns
      :type: :ref:`tabs.^tab`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.get^active^dictionaries:

getActiveDictionaries(tabId)
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Returns a :ref:`compose.^compose^dictionaries` object, listing all installed dictionaries, including the information whether they are currently enabled or not.

.. api-header::
   :label: Parameters

   .. _compose.get^active^dictionaries.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-get-active-dictionaries-tab-id
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.get^active^dictionaries.returns:

   .. api-member::
      :refid: compose-get-active-dictionaries-returns
      :type: :ref:`compose.^compose^dictionaries`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.get^attachment^file:

getAttachmentFile(id)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 98]

Gets the content of a :ref:`compose.^compose^attachment` as a `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__ object.

.. api-header::
   :label: Parameters

   .. _compose.get^attachment^file.id:

   .. api-member::
      :name: ``id``
      :refid: compose-get-attachment-file-id
      :type: (integer)

      The unique identifier for the attachment.

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.get^attachment^file.returns:

   .. api-member::
      :refid: compose-get-attachment-file-returns
      :type: `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.get^compose^details:

getComposeDetails(tabId)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 74]

Fetches the current state of a compose window. Currently only a limited amount of information is available, more will be added in later versions.

.. api-header::
   :label: Parameters

   .. _compose.get^compose^details.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-get-compose-details-tab-id
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.get^compose^details.returns:

   .. api-member::
      :refid: compose-get-compose-details-returns
      :type: :ref:`compose.^compose^details`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.get^compose^state:

getComposeState(tabId)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 90]

Returns information about the current state of the message composer.

.. api-header::
   :label: Parameters

   .. _compose.get^compose^state.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-get-compose-state-tab-id
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.get^compose^state.returns:

   .. api-member::
      :refid: compose-get-compose-state-returns
      :type: :ref:`compose.^compose^state`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.list^attachments:

listAttachments(tabId)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Lists all of the attachments of the message being composed in the specified tab.

.. api-header::
   :label: Parameters

   .. _compose.list^attachments.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-list-attachments-tab-id
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.list^attachments.returns:

   .. api-member::
      :refid: compose-list-attachments-returns
      :type: array of :ref:`compose.^compose^attachment`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.remove^attachment:

removeAttachment(tabId, attachmentId)
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Removes an attachment from the message being composed in the specified tab.

.. api-header::
   :label: Parameters

   .. _compose.remove^attachment.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-remove-attachment-tab-id
      :type: (integer)

   .. _compose.remove^attachment.attachment^id:

   .. api-member::
      :name: ``attachmentId``
      :refid: compose-remove-attachment-attachment-id
      :type: (integer)

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.save^message:

saveMessage(tabId, [options])
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Saves the message currently being composed as a draft or as a template. If the save mode is not specified, the message will be saved as a draft. The returned Promise fulfills once the message has been successfully saved.

.. api-header::
   :label: Parameters

   .. _compose.save^message.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-save-message-tab-id
      :type: (integer)

   .. _compose.save^message.options:

   .. api-member::
      :name: [``options``]
      :refid: compose-save-message-options
      :type: (object, optional)

      .. _compose.save^message.options.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-save-message-options-mode
         :type: (`string`)

         Supported values:

         .. _compose.save^message.options.mode.draft:

         .. api-member::
            :name: :value:`draft`
            :refid: compose-save-message-options-mode-draft

         .. _compose.save^message.options.mode.template:

         .. api-member::
            :name: :value:`template`
            :refid: compose-save-message-options-mode-template

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.save^message.returns:

   .. api-member::
      :refid: compose-save-message-returns
      :type: object

      .. _compose.save^message.returns.messages:

      .. api-member::
         :name: ``messages``
         :refid: compose-save-message-returns-messages
         :type: (array of :ref:`messages.^message^header`)

         An array with exactly one element, the saved message.

         .. note::

            Starting with Thunderbird version 142, the File Carbon Copy (FCC) configuration is no longer respected during save operations. Regardless of any FCC settings, only one message is saved, and it is stored in the default folder for the given save mode.

      .. _compose.save^message.returns.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-save-message-returns-mode
         :type: (`string`)

         The used save mode.

         Supported values:

         .. _compose.save^message.returns.mode.draft:

         .. api-member::
            :name: :value:`draft`
            :refid: compose-save-message-returns-mode-draft

         .. _compose.save^message.returns.mode.template:

         .. api-member::
            :name: :value:`template`
            :refid: compose-save-message-returns-mode-template

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose.save`

.. _compose.send^message:

sendMessage(tabId, [options])
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 90]

Sends the message currently being composed. If the send mode is not specified or set to :value:`default`, the message will be send directly if the user is online and placed in the users outbox otherwise. The returned Promise fulfills once the message has been successfully sent or placed in the user's outbox. Throws when the send process has been aborted by the user, by an :ref:`compose.on^before^send` event or if there has been an error while sending the message to the outgoing mail server.

.. api-header::
   :label: Parameters

   .. _compose.send^message.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-send-message-tab-id
      :type: (integer)

   .. _compose.send^message.options:

   .. api-member::
      :name: [``options``]
      :refid: compose-send-message-options
      :type: (object, optional)

      .. _compose.send^message.options.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-send-message-options-mode
         :type: (`string`)

         Supported values:

         .. _compose.send^message.options.mode.default:

         .. api-member::
            :name: :value:`default`
            :refid: compose-send-message-options-mode-default

         .. _compose.send^message.options.mode.send^later:

         .. api-member::
            :name: :value:`sendLater`
            :refid: compose-send-message-options-mode-send-later

         .. _compose.send^message.options.mode.send^now:

         .. api-member::
            :name: :value:`sendNow`
            :refid: compose-send-message-options-mode-send-now

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.send^message.returns:

   .. api-member::
      :refid: compose-send-message-returns
      :type: object

      .. _compose.send^message.returns.messages:

      .. api-member::
         :name: ``messages``
         :refid: compose-send-message-returns-messages
         :type: (array of :ref:`messages.^message^header`)
         :annotation: -- [Added in TB 102]

         Copies of the sent message. The number of created copies depends on the applied file carbon copy configuration (fcc).

      .. _compose.send^message.returns.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-send-message-returns-mode
         :type: (`string`)
         :annotation: -- [Added in TB 102]

         The used send mode.

         Supported values:

         .. _compose.send^message.returns.mode.send^later:

         .. api-member::
            :name: :value:`sendLater`
            :refid: compose-send-message-returns-mode-send-later

         .. _compose.send^message.returns.mode.send^now:

         .. api-member::
            :name: :value:`sendNow`
            :refid: compose-send-message-returns-mode-send-now

      .. _compose.send^message.returns.header^message^id:

      .. api-member::
         :name: [``headerMessageId``]
         :refid: compose-send-message-returns-header-message-id
         :type: (string, optional)
         :annotation: -- [Added in TB 102]

         The header messageId of the outgoing message. Only included for actually sent messages.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose.send`

.. _compose.set^active^dictionaries:

setActiveDictionaries(tabId, activeDictionaries)
------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Updates the active dictionaries. Throws if the :value:`activeDictionaries` array contains unknown or invalid language identifiers.

.. api-header::
   :label: Parameters

   .. _compose.set^active^dictionaries.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-set-active-dictionaries-tab-id
      :type: (integer)

   .. _compose.set^active^dictionaries.active^dictionaries:

   .. api-member::
      :name: ``activeDictionaries``
      :refid: compose-set-active-dictionaries-active-dictionaries
      :type: (array of string)

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.set^compose^details:

setComposeDetails(tabId, details)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 74]

Updates the compose window. The properties of the given :ref:`compose.^compose^details` object will be used to overwrite the current values of the specified compose window, so only properties that are to be changed should be included. Modified settings will be treated as user initiated, and turn off further automatic changes on these settings.

.. hint::

   When updating any of the array properties (:value:`customHeaders` and most address fields), make sure to first get the current values to not accidentally remove all existing entries when setting the new value.

.. note::

   The compose format of an existing compose window cannot be changed.

.. api-header::
   :label: Parameters

   .. _compose.set^compose^details.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-set-compose-details-tab-id
      :type: (integer)

   .. _compose.set^compose^details.details:

   .. api-member::
      :name: ``details``
      :refid: compose-set-compose-details-details
      :type: (:ref:`compose.^compose^details`)

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.update^attachment:

updateAttachment(tabId, attachmentId, attachment)
-------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Updates the name and/or the content of an attachment in the message being composed in the specified tab. If the specified attachment is a cloud file attachment and the associated provider failed to update the attachment, the function will throw an *ExtensionError*.

.. api-header::
   :label: Parameters

   .. _compose.update^attachment.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-update-attachment-tab-id
      :type: (integer)

   .. _compose.update^attachment.attachment^id:

   .. api-member::
      :name: ``attachmentId``
      :refid: compose-update-attachment-attachment-id
      :type: (integer)

   .. _compose.update^attachment.attachment:

   .. api-member::
      :name: ``attachment``
      :refid: compose-update-attachment-attachment
      :type: (:ref:`compose.^file^attachment`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.update^attachment.returns:

   .. api-member::
      :refid: compose-update-attachment-returns
      :type: :ref:`compose.^compose^attachment`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. rst-class:: api-main-section

Events
======

.. _compose.on^active^dictionaries^changed:

onActiveDictionariesChanged
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Fired when one or more dictionaries have been activated or deactivated.

.. api-header::
   :label: Parameters for onActiveDictionariesChanged.addListener(listener)

   .. _compose.on^active^dictionaries^changed.listener(tab, dictionaries):

   .. api-member::
      :name: ``listener(tab, dictionaries)``
      :refid: compose-on-active-dictionaries-changed-listener-tab-dictionaries

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^active^dictionaries^changed.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-active-dictionaries-changed-tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^active^dictionaries^changed.dictionaries:

   .. api-member::
      :name: ``dictionaries``
      :refid: compose-on-active-dictionaries-changed-dictionaries
      :type: (:ref:`compose.^compose^dictionaries`)

.. _compose.on^after^save:

onAfterSave
-----------

.. api-section-annotation-hack:: -- [Added in TB 105]

Fired when saving a message as draft or template succeeded or failed.

.. api-header::
   :label: Parameters for onAfterSave.addListener(listener)

   .. _compose.on^after^save.listener(tab, save^info):

   .. api-member::
      :name: ``listener(tab, saveInfo)``
      :refid: compose-on-after-save-listener-tab-save-info

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^after^save.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-after-save-tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^after^save.save^info:

   .. api-member::
      :name: ``saveInfo``
      :refid: compose-on-after-save-save-info
      :type: (object)

      .. _compose.on^after^save.save^info.messages:

      .. api-member::
         :name: ``messages``
         :refid: compose-on-after-save-save-info-messages
         :type: (array of :ref:`messages.^message^header`)

         An array with exactly one element, the saved message.

         .. note::

            Starting with Thunderbird version 142, the File Carbon Copy (FCC) configuration is no longer respected during save operations. Regardless of any FCC settings, only one message is saved, and it is stored in the default folder for the given save mode.

      .. _compose.on^after^save.save^info.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-on-after-save-save-info-mode
         :type: (`string`)

         The used save mode.

         Supported values:

         .. _compose.on^after^save.save^info.mode.auto^save:

         .. api-member::
            :name: :value:`autoSave`
            :refid: compose-on-after-save-save-info-mode-auto-save
            :annotation: -- [Added in TB 125]

         .. _compose.on^after^save.save^info.mode.draft:

         .. api-member::
            :name: :value:`draft`
            :refid: compose-on-after-save-save-info-mode-draft

         .. _compose.on^after^save.save^info.mode.template:

         .. api-member::
            :name: :value:`template`
            :refid: compose-on-after-save-save-info-mode-template

      .. _compose.on^after^save.save^info.error:

      .. api-member::
         :name: [``error``]
         :refid: compose-on-after-save-save-info-error
         :type: (string, optional)

         An error description, if saving the message failed.

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.on^after^send:

onAfterSend
-----------

.. api-section-annotation-hack:: -- [Added in TB 105]

Fired when sending a message succeeded or failed.

.. api-header::
   :label: Parameters for onAfterSend.addListener(listener)

   .. _compose.on^after^send.listener(tab, send^info):

   .. api-member::
      :name: ``listener(tab, sendInfo)``
      :refid: compose-on-after-send-listener-tab-send-info

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^after^send.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-after-send-tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^after^send.send^info:

   .. api-member::
      :name: ``sendInfo``
      :refid: compose-on-after-send-send-info
      :type: (object)

      .. _compose.on^after^send.send^info.messages:

      .. api-member::
         :name: ``messages``
         :refid: compose-on-after-send-send-info-messages
         :type: (array of :ref:`messages.^message^header`)

         Copies of the sent message. The number of created copies depends on the applied file carbon copy configuration (fcc).

      .. _compose.on^after^send.send^info.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-on-after-send-send-info-mode
         :type: (`string`)

         The used send mode.

         Supported values:

         .. _compose.on^after^send.send^info.mode.send^later:

         .. api-member::
            :name: :value:`sendLater`
            :refid: compose-on-after-send-send-info-mode-send-later

         .. _compose.on^after^send.send^info.mode.send^now:

         .. api-member::
            :name: :value:`sendNow`
            :refid: compose-on-after-send-send-info-mode-send-now

      .. _compose.on^after^send.send^info.error:

      .. api-member::
         :name: [``error``]
         :refid: compose-on-after-send-send-info-error
         :type: (string, optional)

         An error description, if sending the message failed.

      .. _compose.on^after^send.send^info.header^message^id:

      .. api-member::
         :name: [``headerMessageId``]
         :refid: compose-on-after-send-send-info-header-message-id
         :type: (string, optional)

         The header messageId of the outgoing message. Only included for actually sent messages.

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.on^attachment^added:

onAttachmentAdded
-----------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Fired when an attachment is added to a message being composed.

.. api-header::
   :label: Parameters for onAttachmentAdded.addListener(listener)

   .. _compose.on^attachment^added.listener(tab, attachment):

   .. api-member::
      :name: ``listener(tab, attachment)``
      :refid: compose-on-attachment-added-listener-tab-attachment

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^attachment^added.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-attachment-added-tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^attachment^added.attachment:

   .. api-member::
      :name: ``attachment``
      :refid: compose-on-attachment-added-attachment
      :type: (:ref:`compose.^compose^attachment`)

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.on^attachment^removed:

onAttachmentRemoved
-------------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Fired when an attachment is removed from a message being composed.

.. api-header::
   :label: Parameters for onAttachmentRemoved.addListener(listener)

   .. _compose.on^attachment^removed.listener(tab, attachment^id):

   .. api-member::
      :name: ``listener(tab, attachmentId)``
      :refid: compose-on-attachment-removed-listener-tab-attachment-id

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^attachment^removed.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-attachment-removed-tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^attachment^removed.attachment^id:

   .. api-member::
      :name: ``attachmentId``
      :refid: compose-on-attachment-removed-attachment-id
      :type: (integer)

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.on^before^send:

onBeforeSend
------------

.. api-section-annotation-hack:: -- [Added in TB 74]

Fired when a message is about to be sent from the compose window. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for onBeforeSend.addListener(listener)

   .. _compose.on^before^send.listener(tab, details):

   .. api-member::
      :name: ``listener(tab, details)``
      :refid: compose-on-before-send-listener-tab-details

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^before^send.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-before-send-tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^before^send.details:

   .. api-member::
      :name: ``details``
      :refid: compose-on-before-send-details
      :type: (:ref:`compose.^compose^details`)

      The current state of the compose window. This is functionally the same as calling the :ref:`compose.get^compose^details` function.

.. api-header::
   :label: Expected return value of the listener function

   .. _compose.on^before^send.returns:

   .. api-member::
      :refid: compose-on-before-send-returns
      :type: object

      .. _compose.on^before^send.returns.cancel:

      .. api-member::
         :name: [``cancel``]
         :refid: compose-on-before-send-returns-cancel
         :type: (boolean, optional)

         Cancels the send.

      .. _compose.on^before^send.returns.details:

      .. api-member::
         :name: [``details``]
         :refid: compose-on-before-send-returns-details
         :type: (:ref:`compose.^compose^details`, optional)

         Updates the compose window. This is functionally the same as calling the :ref:`compose.set^compose^details` function.

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.on^compose^state^changed:

onComposeStateChanged
---------------------

.. api-section-annotation-hack:: -- [Added in TB 90]

Fired when the state of the message composer changed.

.. api-header::
   :label: Parameters for onComposeStateChanged.addListener(listener)

   .. _compose.on^compose^state^changed.listener(tab, state):

   .. api-member::
      :name: ``listener(tab, state)``
      :refid: compose-on-compose-state-changed-listener-tab-state

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^compose^state^changed.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-compose-state-changed-tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^compose^state^changed.state:

   .. api-member::
      :name: ``state``
      :refid: compose-on-compose-state-changed-state
      :type: (:ref:`compose.^compose^state`)

.. _compose.on^identity^changed:

onIdentityChanged
-----------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Fired when the user changes the identity that will be used to send a message being composed.

.. api-header::
   :label: Parameters for onIdentityChanged.addListener(listener)

   .. _compose.on^identity^changed.listener(tab, identity^id):

   .. api-member::
      :name: ``listener(tab, identityId)``
      :refid: compose-on-identity-changed-listener-tab-identity-id

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^identity^changed.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-identity-changed-tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^identity^changed.identity^id:

   .. api-member::
      :name: ``identityId``
      :refid: compose-on-identity-changed-identity-id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Types
=====

.. _compose.^compose^attachment:

ComposeAttachment
-----------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Represents an attachment in a message being composed.

.. api-header::
   :label: object

   .. _compose.^compose^attachment.id:

   .. api-member::
      :name: ``id``
      :refid: compose-compose-attachment-id
      :type: (integer)

      A unique identifier for this attachment.

   .. _compose.^compose^attachment.name:

   .. api-member::
      :name: [``name``]
      :refid: compose-compose-attachment-name
      :type: (string, optional)

      The name of this attachment, as displayed to the user.

   .. _compose.^compose^attachment.size:

   .. api-member::
      :name: [``size``]
      :refid: compose-compose-attachment-size
      :type: (integer, optional)
      :annotation: -- [Added in TB 83]

      The size in bytes of this attachment. Read-only.

.. _compose.^compose^details:

ComposeDetails
--------------

.. api-section-annotation-hack:: -- [Added in TB 74]

Used by various functions to represent the state of a message being composed. Note that functions using this type may have a partial implementation.

.. api-header::
   :label: object

   .. _compose.^compose^details.additional^fcc^folder:

   .. api-member::
      :name: [``additionalFccFolder``]
      :refid: compose-compose-details-additional-fcc-folder
      :type: (:ref:`folders.^mail^folder` or `string` or :ref:`folders.^mail^folder^id`, optional)
      :annotation: -- [Added in TB 102]

      An additional fcc folder which can be selected while composing the message, an empty string if not used. The permission :permission:`accountsRead` is required to use this property.

   .. _compose.^compose^details.attachments:

   .. api-member::
      :name: [``attachments``]
      :refid: compose-compose-details-attachments
      :type: (array of :ref:`compose.^file^attachment` or :ref:`compose.^compose^attachment`, optional)
      :annotation: -- [Added in TB 82]

      Only used in the begin* functions. Attachments to add to the message.

   .. _compose.^compose^details.attach^public^p^g^p^key:

   .. api-member::
      :name: [``attachPublicPGPKey``]
      :refid: compose-compose-details-attach-public-p-g-p-key
      :type: (boolean, optional)
      :annotation: -- [Added in TB 128]

      Whether the public OpenPGP key of the sending identity should be attached to the message.

   .. _compose.^compose^details.attach^v^card:

   .. api-member::
      :name: [``attachVCard``]
      :refid: compose-compose-details-attach-v-card
      :type: (boolean, optional)
      :annotation: -- [Added in TB 102]

      Whether or not the vCard of the used identity will be attached to the message during send.

      .. note::

         If the value has not been modified, selecting a different identity will load the default value of the new identity.

   .. _compose.^compose^details.bcc:

   .. api-member::
      :name: [``bcc``]
      :refid: compose-compose-details-bcc
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.body:

   .. api-member::
      :name: [``body``]
      :refid: compose-compose-details-body
      :type: (string, optional)

      The HTML content of the message.

   .. _compose.^compose^details.cc:

   .. api-member::
      :name: [``cc``]
      :refid: compose-compose-details-cc
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.custom^headers:

   .. api-member::
      :name: [``customHeaders``]
      :refid: compose-compose-details-custom-headers
      :type: (array of :ref:`compose.^custom^header`, optional)
      :annotation: -- [Added in TB 100]

      Array of custom headers. Headers will be returned in *Http-Header-Case* (a.k.a. *Train-Case*). Set an empty array to clear all custom headers.

   .. _compose.^compose^details.delivery^format:

   .. api-member::
      :name: [``deliveryFormat``]
      :refid: compose-compose-details-delivery-format
      :type: (`string`, optional)
      :annotation: -- [Added in TB 102]

      Defines the MIME format of the sent message (ignored on plain text messages). Defaults to :value:`auto`, which will send html messages as plain text, if they do not include any formatting, and as :value:`both` otherwise (a multipart/mixed message).

      Supported values:

      .. _compose.^compose^details.delivery^format.auto:

      .. api-member::
         :name: :value:`auto`
         :refid: compose-compose-details-delivery-format-auto

      .. _compose.^compose^details.delivery^format.both:

      .. api-member::
         :name: :value:`both`
         :refid: compose-compose-details-delivery-format-both

      .. _compose.^compose^details.delivery^format.html:

      .. api-member::
         :name: :value:`html`
         :refid: compose-compose-details-delivery-format-html

      .. _compose.^compose^details.delivery^format.plaintext:

      .. api-member::
         :name: :value:`plaintext`
         :refid: compose-compose-details-delivery-format-plaintext

   .. _compose.^compose^details.delivery^status^notification:

   .. api-member::
      :name: [``deliveryStatusNotification``]
      :refid: compose-compose-details-delivery-status-notification
      :type: (boolean, optional)
      :annotation: -- [Added in TB 102]

      Let the sender know when the recipient's server received the message. Not supported by all servers.

   .. _compose.^compose^details.followup^to:

   .. api-member::
      :name: [``followupTo``]
      :refid: compose-compose-details-followup-to
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.from:

   .. api-member::
      :name: [``from``]
      :refid: compose-compose-details-from
      :type: (:ref:`compose.^compose^recipient`, optional)
      :annotation: -- [Added in TB 88]

      *Caution*: Setting a value for :value:`from` does not change the used identity, it overrides the *From* header. Many email servers do not accept emails where the *From* header does not match the sender identity. Must be set to exactly one valid email address.

   .. _compose.^compose^details.identity^id:

   .. api-member::
      :name: [``identityId``]
      :refid: compose-compose-details-identity-id
      :type: (string, optional)
      :annotation: -- [Added in TB 76]

      The ID of an identity from the :doc:`accounts`. The settings from the identity will be used in the composed message. If :value:`replyTo` is also specified, the :value:`replyTo` property of the identity is overridden. The permission :permission:`accountsRead` is required to include the :value:`identityId`.

   .. _compose.^compose^details.is^modified:

   .. api-member::
      :name: [``isModified``]
      :refid: compose-compose-details-is-modified
      :type: (boolean, optional)
      :annotation: -- [Added in TB 125]

      Whether the composer is considered modified by the user. A modified composer asks for confirmation, when it is closed.

   .. _compose.^compose^details.is^plain^text:

   .. api-member::
      :name: [``isPlainText``]
      :refid: compose-compose-details-is-plain-text
      :type: (boolean, optional)
      :annotation: -- [Added in TB 75]

      Whether the message is an HTML message or a plain text message.

   .. _compose.^compose^details.newsgroups:

   .. api-member::
      :name: [``newsgroups``]
      :refid: compose-compose-details-newsgroups
      :type: (string or array of string, optional)

      A single newsgroup name or an array of newsgroup names.

   .. _compose.^compose^details.override^default^fcc:

   .. api-member::
      :name: [``overrideDefaultFcc``]
      :refid: compose-compose-details-override-default-fcc
      :type: (boolean, optional)
      :annotation: -- [Added in TB 102]

      Indicates whether the default fcc setting (defined by the used identity) is being overridden for this message. Setting :value:`false` will clear the override. Setting :value:`true` will throw an *ExtensionError*, if :value:`overrideDefaultFccFolder` is not set as well. The permission :permission:`accountsRead` is required to use this property.

   .. _compose.^compose^details.override^default^fcc^folder:

   .. api-member::
      :name: [``overrideDefaultFccFolder``]
      :refid: compose-compose-details-override-default-fcc-folder
      :type: (:ref:`folders.^mail^folder` or `string` or :ref:`folders.^mail^folder^id`, optional)
      :annotation: -- [Added in TB 102]

      This value overrides the default fcc setting (defined by the used identity) for this message only. Either a :ref:`folders.^mail^folder` specifying the folder for the copy of the sent message, or an empty string to not save a copy at all. The permission :permission:`accountsRead` is required to use this property.

   .. _compose.^compose^details.plain^text^body:

   .. api-member::
      :name: [``plainTextBody``]
      :refid: compose-compose-details-plain-text-body
      :type: (string, optional)
      :annotation: -- [Added in TB 75]

      The plain text content of the message.

   .. _compose.^compose^details.priority:

   .. api-member::
      :name: [``priority``]
      :refid: compose-compose-details-priority
      :type: (`string`, optional)
      :annotation: -- [Added in TB 102]

      The priority of the message.

      Supported values:

      .. _compose.^compose^details.priority.high:

      .. api-member::
         :name: :value:`high`
         :refid: compose-compose-details-priority-high

      .. _compose.^compose^details.priority.highest:

      .. api-member::
         :name: :value:`highest`
         :refid: compose-compose-details-priority-highest

      .. _compose.^compose^details.priority.low:

      .. api-member::
         :name: :value:`low`
         :refid: compose-compose-details-priority-low

      .. _compose.^compose^details.priority.lowest:

      .. api-member::
         :name: :value:`lowest`
         :refid: compose-compose-details-priority-lowest

      .. _compose.^compose^details.priority.normal:

      .. api-member::
         :name: :value:`normal`
         :refid: compose-compose-details-priority-normal

   .. _compose.^compose^details.related^message^id:

   .. api-member::
      :name: [``relatedMessageId``]
      :refid: compose-compose-details-related-message-id
      :type: (:ref:`messages.^message^id`, optional)
      :annotation: -- [Added in TB 95]

      The id of the original message (in case of draft, template, forward or reply). Read-only. Is :value:`undefined` in all other cases or if the original message was opened from file.

   .. _compose.^compose^details.reply^to:

   .. api-member::
      :name: [``replyTo``]
      :refid: compose-compose-details-reply-to
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.return^receipt:

   .. api-member::
      :name: [``returnReceipt``]
      :refid: compose-compose-details-return-receipt
      :type: (boolean, optional)
      :annotation: -- [Added in TB 102]

      Add the *Disposition-Notification-To* header to the message to requests the recipients email client to send a reply once the message has been received. Recipient server may strip the header and the recipient might ignore the request.

   .. _compose.^compose^details.selected^encryption^technology:

   .. api-member::
      :name: [``selectedEncryptionTechnology``]
      :refid: compose-compose-details-selected-encryption-technology
      :type: (:ref:`compose.^encryption^properties^s^m^i^m^e` or :ref:`compose.^encryption^properties^open^p^g^p`, optional)
      :annotation: -- [Added in TB 128]

      The selected encryption technology (:value:`OpenPGP` or :value:`S/MIME`) which is to be used to sign and/or encrypt the message. If the sending identity does not support encryption at all, this will be :value:`undefined`.

   .. _compose.^compose^details.subject:

   .. api-member::
      :name: [``subject``]
      :refid: compose-compose-details-subject
      :type: (string, optional)

   .. _compose.^compose^details.to:

   .. api-member::
      :name: [``to``]
      :refid: compose-compose-details-to
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.type:

   .. api-member::
      :name: [``type``]
      :refid: compose-compose-details-type
      :type: (`string`, optional)
      :annotation: -- [Added in TB 88]

      Read-only. The type of the message being composed, depending on how the compose window was opened by the user.

      Supported values:

      .. _compose.^compose^details.type.draft:

      .. api-member::
         :name: :value:`draft`
         :refid: compose-compose-details-type-draft

      .. _compose.^compose^details.type.forward:

      .. api-member::
         :name: :value:`forward`
         :refid: compose-compose-details-type-forward

      .. _compose.^compose^details.type.new:

      .. api-member::
         :name: :value:`new`
         :refid: compose-compose-details-type-new

      .. _compose.^compose^details.type.redirect:

      .. api-member::
         :name: :value:`redirect`
         :refid: compose-compose-details-type-redirect
         :annotation: -- [Added in TB 90]

      .. _compose.^compose^details.type.reply:

      .. api-member::
         :name: :value:`reply`
         :refid: compose-compose-details-type-reply

.. _compose.^compose^dictionaries:

ComposeDictionaries
-------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

A *dictionary object* with entries for all installed dictionaries, having a language identifier as *key* (for example :value:`en-US`) and a boolean expression as *value*, indicating whether that dictionary is enabled for spellchecking or not.

.. api-header::
   :label: object

.. _compose.^compose^recipient:

ComposeRecipient
----------------

.. api-section-annotation-hack:: -- [Added in TB 67]

.. api-header::
   :label: string

   .. container:: api-member-node

      .. container:: api-member-description-only

         A name and email address in the format :value:`Name <email@example.com>`, or just an email address.

*or*

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _compose.^compose^recipient.id:

         .. api-member::
            :name: ``id``
            :refid: compose-compose-recipient-id
            :type: (string)

            The ID of a contact or mailing list from the :doc:`contacts` or :doc:`mailingLists`.

         .. _compose.^compose^recipient.type:

         .. api-member::
            :name: ``type``
            :refid: compose-compose-recipient-type
            :type: (`string`)

            Which sort of object this ID is for.

            Supported values:

            .. _compose.^compose^recipient.type.contact:

            .. api-member::
               :name: :value:`contact`
               :refid: compose-compose-recipient-type-contact

            .. _compose.^compose^recipient.type.mailing^list:

            .. api-member::
               :name: :value:`mailingList`
               :refid: compose-compose-recipient-type-mailing-list

.. _compose.^compose^recipient^list:

ComposeRecipientList
--------------------

.. api-section-annotation-hack:: -- [Added in TB 74]

.. api-header::
   :label: :ref:`compose.^compose^recipient`

*or*

.. api-header::
   :label: array of :ref:`compose.^compose^recipient`

.. _compose.^compose^state:

ComposeState
------------

.. api-section-annotation-hack:: -- [Added in TB 90]

Represent the state of the message composer.

.. api-header::
   :label: object

   .. _compose.^compose^state.can^send^later:

   .. api-member::
      :name: ``canSendLater``
      :refid: compose-compose-state-can-send-later
      :type: (boolean)

      The message can be send later.

   .. _compose.^compose^state.can^send^now:

   .. api-member::
      :name: ``canSendNow``
      :refid: compose-compose-state-can-send-now
      :type: (boolean)

      The message can be send now.

.. _compose.^custom^header:

CustomHeader
------------

.. api-section-annotation-hack:: -- [Added in TB 100]

A custom header definition.

.. api-header::
   :label: object

   .. _compose.^custom^header.name:

   .. api-member::
      :name: ``name``
      :refid: compose-custom-header-name
      :type: (string)

      Name of a custom header, must be prefixed by :value:`X-` (but not by :value:`X-Mozilla-`) or be one of the explicitly allowed headers (:value:`MSIP_Labels`)

   .. _compose.^custom^header.value:

   .. api-member::
      :name: ``value``
      :refid: compose-custom-header-value
      :type: (string)

.. _compose.^encryption^properties^open^p^g^p:

EncryptionPropertiesOpenPGP
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

.. api-header::
   :label: object

   .. _compose.^encryption^properties^open^p^g^p.encrypt^body:

   .. api-member::
      :name: ``encryptBody``
      :refid: compose-encryption-properties-open-p-g-p-encrypt-body
      :type: (boolean)

      Whether encryption of the message body using the OpenPGP technology is enabled.

      .. note::

         If encryption is enabled, but the `preconditions <https://support.mozilla.org/en-US/kb/thunderbird-help-cannot-encrypt>`__ for sending an encrypted message are not met, the message cannot be sent.

   .. _compose.^encryption^properties^open^p^g^p.encrypt^subject:

   .. api-member::
      :name: ``encryptSubject``
      :refid: compose-encryption-properties-open-p-g-p-encrypt-subject
      :type: (boolean)

      Whether encryption of the message subject using the OpenPGP technology is enabled (only supported if encryption of the body is enabled a well).

   .. _compose.^encryption^properties^open^p^g^p.name:

   .. api-member::
      :name: ``name``
      :refid: compose-encryption-properties-open-p-g-p-name
      :type: (string)

   .. _compose.^encryption^properties^open^p^g^p.sign^message:

   .. api-member::
      :name: ``signMessage``
      :refid: compose-encryption-properties-open-p-g-p-sign-message
      :type: (boolean)

      Whether the message will be signed using the OpenPGP technology.

.. _compose.^encryption^properties^s^m^i^m^e:

EncryptionPropertiesSMIME
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

.. api-header::
   :label: object

   .. _compose.^encryption^properties^s^m^i^m^e.encrypt^body:

   .. api-member::
      :name: ``encryptBody``
      :refid: compose-encryption-properties-s-m-i-m-e-encrypt-body
      :type: (boolean)

      Whether encryption of the message body using the S/MIME technology is enabled.

      .. note::

         If encryption is enabled, but the `preconditions <https://support.mozilla.org/en-US/kb/thunderbird-help-cannot-encrypt>`__ for sending an encrypted message are not met, the message cannot be sent.

   .. _compose.^encryption^properties^s^m^i^m^e.name:

   .. api-member::
      :name: ``name``
      :refid: compose-encryption-properties-s-m-i-m-e-name
      :type: (string)

   .. _compose.^encryption^properties^s^m^i^m^e.sign^message:

   .. api-member::
      :name: ``signMessage``
      :refid: compose-encryption-properties-s-m-i-m-e-sign-message
      :type: (boolean)

      Whether the message will be signed using the S/MIME technology

.. _compose.^file^attachment:

FileAttachment
--------------

.. api-section-annotation-hack:: -- [Added in TB 98]

Object used to add, update or rename an attachment in a message being composed.

.. api-header::
   :label: object

   .. _compose.^file^attachment.file:

   .. api-member::
      :name: [``file``]
      :refid: compose-file-attachment-file
      :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__, optional)

      The new content for the attachment.

   .. _compose.^file^attachment.name:

   .. api-member::
      :name: [``name``]
      :refid: compose-file-attachment-name
      :type: (string, optional)

      The new name for the attachment, as displayed to the user. If not specified, the name of the provided :value:`file` object is used.
