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

.. role:: small

The compose API allows to interact with the message composition window.

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
   :refname: accountsRead

   See your mail accounts, their identities and their folders.

.. _compose.permission.compose:

.. api-member::
   :name: :permission:`compose`
   :refid: compose-permission-compose
   :refname: compose

   Read and modify your email messages as you compose and send them.

.. _compose.permission.compose.save:

.. api-member::
   :name: :permission:`compose.save`
   :refid: compose-permission-compose-save
   :refname: compose.save

   Save composed email messages as drafts or templates.

.. _compose.permission.compose.send:

.. api-member::
   :name: :permission:`compose.send`
   :refid: compose-permission-compose-send
   :refname: compose.send

   Send composed email messages on your behalf.

.. _compose.permission.messages^read:

.. api-member::
   :name: :permission:`messagesRead`
   :refid: compose-permission-messages-read
   :refname: messagesRead

   Read your email messages.

.. rst-class:: api-main-section

Functions
=========

.. _compose.add^attachment:

addAttachment(tabId, attachment)
--------------------------------

.. api-section-annotation-hack:: 

Adds an attachment to the message being composed in the specified tab.

.. api-header::
   :label: Parameters

   .. _compose.add^attachment.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-add-attachment-tab-id
      :refname: tabId
      :type: (integer)

   .. _compose.add^attachment.attachment:

   .. api-member::
      :name: ``attachment``
      :refid: compose-add-attachment-attachment
      :refname: attachment
      :type: (:ref:`compose.^file^attachment` or :ref:`compose.^compose^attachment`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.add^attachment.returns:

   .. api-member::
      :refid: compose-add-attachment-returns
      :refname: _returns
      :type: :ref:`compose.^compose^attachment`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.begin^forward:

beginForward(messageId, [forwardType], [details])
-------------------------------------------------

.. api-section-annotation-hack:: 

Open a new message compose window forwarding a given message.

.. note::

   The compose format can be set by :value:`details.isPlainText` or by specifying only one of :value:`details.body` or :value:`details.plainTextBody`. Otherwise the default compose format of the selected identity is used. If no identity is specified, this function is using the default identity and not the identity of the referenced message.

.. api-header::
   :label: Parameters

   .. _compose.begin^forward.message^id:

   .. api-member::
      :name: ``messageId``
      :refid: compose-begin-forward-message-id
      :refname: messageId
      :type: (:ref:`messages.^message^id`)

      The message to forward, as retrieved using other APIs.

   .. _compose.begin^forward.forward^type:

   .. api-member::
      :name: [``forwardType``]
      :refid: compose-begin-forward-forward-type
      :refname: forwardType
      :type: (`string`, optional)

      Supported values:

      .. _compose.begin^forward.forward^type.forward^as^attachment:

      .. api-member::
         :name: :value:`forwardAsAttachment`
         :refid: compose-begin-forward-forward-type-forward-as-attachment
         :refname: forwardAsAttachment

      .. _compose.begin^forward.forward^type.forward^inline:

      .. api-member::
         :name: :value:`forwardInline`
         :refid: compose-begin-forward-forward-type-forward-inline
         :refname: forwardInline

   .. _compose.begin^forward.details:

   .. api-member::
      :name: [``details``]
      :refid: compose-begin-forward-details
      :refname: details
      :type: (:ref:`compose.^compose^details`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.begin^forward.returns:

   .. api-member::
      :refid: compose-begin-forward-returns
      :refname: _returns
      :type: :ref:`tabs.^tab`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.begin^new:

beginNew([messageId], [details])
--------------------------------

.. api-section-annotation-hack:: 

Open a new message compose window.

.. note::

   The compose format can be set by :value:`details.isPlainText` or by specifying only one of :value:`details.body` or :value:`details.plainTextBody`. Otherwise the default compose format of the selected identity is used. If no identity is specified, this function is using the default identity and not the identity of the referenced message.

.. api-header::
   :label: Parameters

   .. _compose.begin^new.message^id:

   .. api-member::
      :name: [``messageId``]
      :refid: compose-begin-new-message-id
      :refname: messageId
      :type: (:ref:`messages.^message^id`, optional)

      If specified, the message or template to edit as a new message.

   .. _compose.begin^new.details:

   .. api-member::
      :name: [``details``]
      :refid: compose-begin-new-details
      :refname: details
      :type: (:ref:`compose.^compose^details`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.begin^new.returns:

   .. api-member::
      :refid: compose-begin-new-returns
      :refname: _returns
      :type: :ref:`tabs.^tab`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.begin^reply:

beginReply(messageId, [replyType], [details])
---------------------------------------------

.. api-section-annotation-hack:: 

Open a new message compose window replying to a given message.

.. note::

   The compose format can be set by :value:`details.isPlainText` or by specifying only one of :value:`details.body` or :value:`details.plainTextBody`. Otherwise the default compose format of the selected identity is used. If no identity is specified, this function is using the default identity and not the identity of the referenced message.

.. api-header::
   :label: Parameters

   .. _compose.begin^reply.message^id:

   .. api-member::
      :name: ``messageId``
      :refid: compose-begin-reply-message-id
      :refname: messageId
      :type: (:ref:`messages.^message^id`)

      The message to reply to, as retrieved using other APIs.

   .. _compose.begin^reply.reply^type:

   .. api-member::
      :name: [``replyType``]
      :refid: compose-begin-reply-reply-type
      :refname: replyType
      :type: (`string`, optional)

      Supported values:

      .. _compose.begin^reply.reply^type.reply^to^all:

      .. api-member::
         :name: :value:`replyToAll`
         :refid: compose-begin-reply-reply-type-reply-to-all
         :refname: replyToAll

      .. _compose.begin^reply.reply^type.reply^to^list:

      .. api-member::
         :name: :value:`replyToList`
         :refid: compose-begin-reply-reply-type-reply-to-list
         :refname: replyToList

      .. _compose.begin^reply.reply^type.reply^to^sender:

      .. api-member::
         :name: :value:`replyToSender`
         :refid: compose-begin-reply-reply-type-reply-to-sender
         :refname: replyToSender

   .. _compose.begin^reply.details:

   .. api-member::
      :name: [``details``]
      :refid: compose-begin-reply-details
      :refname: details
      :type: (:ref:`compose.^compose^details`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.begin^reply.returns:

   .. api-member::
      :refid: compose-begin-reply-returns
      :refname: _returns
      :type: :ref:`tabs.^tab`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.get^active^dictionaries:

getActiveDictionaries(tabId)
----------------------------

.. api-section-annotation-hack:: 

Returns a :ref:`compose.^compose^dictionaries` object, listing all installed dictionaries, including the information whether they are currently enabled or not.

.. api-header::
   :label: Parameters

   .. _compose.get^active^dictionaries.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-get-active-dictionaries-tab-id
      :refname: tabId
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.get^active^dictionaries.returns:

   .. api-member::
      :refid: compose-get-active-dictionaries-returns
      :refname: _returns
      :type: :ref:`compose.^compose^dictionaries`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.get^attachment^file:

getAttachmentFile(id)
---------------------

.. api-section-annotation-hack:: 

Gets the content of a :ref:`compose.^compose^attachment` as a `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__ object.

.. api-header::
   :label: Parameters

   .. _compose.get^attachment^file.id:

   .. api-member::
      :name: ``id``
      :refid: compose-get-attachment-file-id
      :refname: id
      :type: (integer)

      The unique identifier for the attachment.

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.get^attachment^file.returns:

   .. api-member::
      :refid: compose-get-attachment-file-returns
      :refname: _returns
      :type: `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.get^compose^details:

getComposeDetails(tabId)
------------------------

.. api-section-annotation-hack:: 

Fetches the current state of a compose window. Currently only a limited amount of information is available, more will be added in later versions.

.. api-header::
   :label: Parameters

   .. _compose.get^compose^details.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-get-compose-details-tab-id
      :refname: tabId
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.get^compose^details.returns:

   .. api-member::
      :refid: compose-get-compose-details-returns
      :refname: _returns
      :type: :ref:`compose.^compose^details`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.get^compose^state:

getComposeState(tabId)
----------------------

.. api-section-annotation-hack:: 

Returns information about the current state of the message composer.

.. api-header::
   :label: Parameters

   .. _compose.get^compose^state.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-get-compose-state-tab-id
      :refname: tabId
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.get^compose^state.returns:

   .. api-member::
      :refid: compose-get-compose-state-returns
      :refname: _returns
      :type: :ref:`compose.^compose^state`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.list^attachments:

listAttachments(tabId)
----------------------

.. api-section-annotation-hack:: 

Lists all of the attachments of the message being composed in the specified tab.

.. api-header::
   :label: Parameters

   .. _compose.list^attachments.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-list-attachments-tab-id
      :refname: tabId
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.list^attachments.returns:

   .. api-member::
      :refid: compose-list-attachments-returns
      :refname: _returns
      :type: array of :ref:`compose.^compose^attachment`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.remove^attachment:

removeAttachment(tabId, attachmentId)
-------------------------------------

.. api-section-annotation-hack:: 

Removes an attachment from the message being composed in the specified tab.

.. api-header::
   :label: Parameters

   .. _compose.remove^attachment.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-remove-attachment-tab-id
      :refname: tabId
      :type: (integer)

   .. _compose.remove^attachment.attachment^id:

   .. api-member::
      :name: ``attachmentId``
      :refid: compose-remove-attachment-attachment-id
      :refname: attachmentId
      :type: (integer)

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.save^message:

saveMessage(tabId, [options])
-----------------------------

.. api-section-annotation-hack:: 

Saves the message currently being composed as a draft or as a template. If the save mode is not specified, the message will be saved as a draft. The returned Promise fulfills once the message has been successfully saved.

.. api-header::
   :label: Parameters

   .. _compose.save^message.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-save-message-tab-id
      :refname: tabId
      :type: (integer)

   .. _compose.save^message.options:

   .. api-member::
      :name: [``options``]
      :refid: compose-save-message-options
      :refname: options
      :type: (object, optional)

      .. _compose.save^message.options.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-save-message-options-mode
         :refname: mode
         :type: (`string`)

         Supported values:

         .. _compose.save^message.options.mode.draft:

         .. api-member::
            :name: :value:`draft`
            :refid: compose-save-message-options-mode-draft
            :refname: draft

         .. _compose.save^message.options.mode.template:

         .. api-member::
            :name: :value:`template`
            :refid: compose-save-message-options-mode-template
            :refname: template

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.save^message.returns:

   .. api-member::
      :refid: compose-save-message-returns
      :refname: _returns
      :type: object

      .. _compose.save^message.returns.messages:

      .. api-member::
         :name: ``messages``
         :refid: compose-save-message-returns-messages
         :refname: messages
         :type: (array of :ref:`messages.^message^header`)

         An array with exactly one element, the saved message.

         .. note::

            Starting with Thunderbird version 142, the File Carbon Copy (FCC) configuration is no longer respected during save operations. Regardless of any FCC settings, only one message is saved, and it is stored in the default folder for the given save mode.

      .. _compose.save^message.returns.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-save-message-returns-mode
         :refname: mode
         :type: (`string`)

         The used save mode.

         Supported values:

         .. _compose.save^message.returns.mode.draft:

         .. api-member::
            :name: :value:`draft`
            :refid: compose-save-message-returns-mode-draft
            :refname: draft

         .. _compose.save^message.returns.mode.template:

         .. api-member::
            :name: :value:`template`
            :refid: compose-save-message-returns-mode-template
            :refname: template

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose.save`

.. _compose.send^message:

sendMessage(tabId, [options])
-----------------------------

.. api-section-annotation-hack:: 

Sends the message currently being composed. If the send mode is not specified or set to :value:`default`, the message will be send directly if the user is online and placed in the users outbox otherwise. The returned Promise fulfills once the message has been successfully sent or placed in the user's outbox. Throws when the send process has been aborted by the user, by an :ref:`compose.on^before^send` event or if there has been an error while sending the message to the outgoing mail server.

.. api-header::
   :label: Parameters

   .. _compose.send^message.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-send-message-tab-id
      :refname: tabId
      :type: (integer)

   .. _compose.send^message.options:

   .. api-member::
      :name: [``options``]
      :refid: compose-send-message-options
      :refname: options
      :type: (object, optional)

      .. _compose.send^message.options.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-send-message-options-mode
         :refname: mode
         :type: (`string`)

         Supported values:

         .. _compose.send^message.options.mode.default:

         .. api-member::
            :name: :value:`default`
            :refid: compose-send-message-options-mode-default
            :refname: default

         .. _compose.send^message.options.mode.send^later:

         .. api-member::
            :name: :value:`sendLater`
            :refid: compose-send-message-options-mode-send-later
            :refname: sendLater

         .. _compose.send^message.options.mode.send^now:

         .. api-member::
            :name: :value:`sendNow`
            :refid: compose-send-message-options-mode-send-now
            :refname: sendNow

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.send^message.returns:

   .. api-member::
      :refid: compose-send-message-returns
      :refname: _returns
      :type: object

      .. _compose.send^message.returns.messages:

      .. api-member::
         :name: ``messages``
         :refid: compose-send-message-returns-messages
         :refname: messages
         :type: (array of :ref:`messages.^message^header`)

         Copies of the sent message. The number of created copies depends on the applied file carbon copy configuration (fcc).

      .. _compose.send^message.returns.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-send-message-returns-mode
         :refname: mode
         :type: (`string`)

         The used send mode.

         Supported values:

         .. _compose.send^message.returns.mode.send^later:

         .. api-member::
            :name: :value:`sendLater`
            :refid: compose-send-message-returns-mode-send-later
            :refname: sendLater

         .. _compose.send^message.returns.mode.send^now:

         .. api-member::
            :name: :value:`sendNow`
            :refid: compose-send-message-returns-mode-send-now
            :refname: sendNow

      .. _compose.send^message.returns.header^message^id:

      .. api-member::
         :name: [``headerMessageId``]
         :refid: compose-send-message-returns-header-message-id
         :refname: headerMessageId
         :type: (string, optional)

         The header messageId of the outgoing message. Only included for actually sent messages.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose.send`

.. _compose.set^active^dictionaries:

setActiveDictionaries(tabId, activeDictionaries)
------------------------------------------------

.. api-section-annotation-hack:: 

Updates the active dictionaries. Throws if the :value:`activeDictionaries` array contains unknown or invalid language identifiers.

.. api-header::
   :label: Parameters

   .. _compose.set^active^dictionaries.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-set-active-dictionaries-tab-id
      :refname: tabId
      :type: (integer)

   .. _compose.set^active^dictionaries.active^dictionaries:

   .. api-member::
      :name: ``activeDictionaries``
      :refid: compose-set-active-dictionaries-active-dictionaries
      :refname: activeDictionaries
      :type: (array of string)

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.set^compose^details:

setComposeDetails(tabId, details)
---------------------------------

.. api-section-annotation-hack:: 

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
      :refname: tabId
      :type: (integer)

   .. _compose.set^compose^details.details:

   .. api-member::
      :name: ``details``
      :refid: compose-set-compose-details-details
      :refname: details
      :type: (:ref:`compose.^compose^details`)

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.update^attachment:

updateAttachment(tabId, attachmentId, attachment)
-------------------------------------------------

.. api-section-annotation-hack:: 

Updates the name and/or the content of an attachment in the message being composed in the specified tab. If the specified attachment is a cloud file attachment and the associated provider failed to update the attachment, the function will throw an *ExtensionError*.

.. api-header::
   :label: Parameters

   .. _compose.update^attachment.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: compose-update-attachment-tab-id
      :refname: tabId
      :type: (integer)

   .. _compose.update^attachment.attachment^id:

   .. api-member::
      :name: ``attachmentId``
      :refid: compose-update-attachment-attachment-id
      :refname: attachmentId
      :type: (integer)

   .. _compose.update^attachment.attachment:

   .. api-member::
      :name: ``attachment``
      :refid: compose-update-attachment-attachment
      :refname: attachment
      :type: (:ref:`compose.^file^attachment`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _compose.update^attachment.returns:

   .. api-member::
      :refid: compose-update-attachment-returns
      :refname: _returns
      :type: :ref:`compose.^compose^attachment`

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

.. api-section-annotation-hack:: 

Fired when one or more dictionaries have been activated or deactivated.

.. api-header::
   :label: Parameters for onActiveDictionariesChanged.addListener(listener)

   .. _compose.on^active^dictionaries^changed.listener(tab, dictionaries):

   .. api-member::
      :name: ``listener(tab, dictionaries)``
      :refid: compose-on-active-dictionaries-changed-listener-tab-dictionaries
      :refname: listener(tab, dictionaries)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^active^dictionaries^changed.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-active-dictionaries-changed-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^active^dictionaries^changed.dictionaries:

   .. api-member::
      :name: ``dictionaries``
      :refid: compose-on-active-dictionaries-changed-dictionaries
      :refname: dictionaries
      :type: (:ref:`compose.^compose^dictionaries`)

.. _compose.on^after^save:

onAfterSave
-----------

.. api-section-annotation-hack:: 

Fired when saving a message as draft or template succeeded or failed.

.. api-header::
   :label: Parameters for onAfterSave.addListener(listener)

   .. _compose.on^after^save.listener(tab, save^info):

   .. api-member::
      :name: ``listener(tab, saveInfo)``
      :refid: compose-on-after-save-listener-tab-save-info
      :refname: listener(tab, saveInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^after^save.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-after-save-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^after^save.save^info:

   .. api-member::
      :name: ``saveInfo``
      :refid: compose-on-after-save-save-info
      :refname: saveInfo
      :type: (object)

      .. _compose.on^after^save.save^info.details:

      .. api-member::
         :name: ``details``
         :refid: compose-on-after-save-save-info-details
         :refname: details
         :type: (:ref:`compose.^compose^details`)

         The :ref:`compose.^compose^details` of the saved message.

      .. _compose.on^after^save.save^info.messages:

      .. api-member::
         :name: ``messages``
         :refid: compose-on-after-save-save-info-messages
         :refname: messages
         :type: (array of :ref:`messages.^message^header`)

         An array with exactly one element, the saved message. The :permission:`messagesRead` permission is required for this property to be included.

         .. note::

            Starting with Thunderbird version 142, the File Carbon Copy (FCC) configuration is no longer respected during save operations. Regardless of any FCC settings, only one message is saved, and it is stored in the default folder for the given save mode.

      .. _compose.on^after^save.save^info.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-on-after-save-save-info-mode
         :refname: mode
         :type: (`string`)

         The used save mode.

         Supported values:

         .. _compose.on^after^save.save^info.mode.auto^save:

         .. api-member::
            :name: :value:`autoSave`
            :refid: compose-on-after-save-save-info-mode-auto-save
            :refname: autoSave

         .. _compose.on^after^save.save^info.mode.draft:

         .. api-member::
            :name: :value:`draft`
            :refid: compose-on-after-save-save-info-mode-draft
            :refname: draft

         .. _compose.on^after^save.save^info.mode.template:

         .. api-member::
            :name: :value:`template`
            :refid: compose-on-after-save-save-info-mode-template
            :refname: template

      .. _compose.on^after^save.save^info.error:

      .. api-member::
         :name: [``error``]
         :refid: compose-on-after-save-save-info-error
         :refname: error
         :type: (string, optional)

         An error description, if saving the message failed.

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.on^after^send:

onAfterSend
-----------

.. api-section-annotation-hack:: 

Fired when sending a message succeeded or failed.

.. api-header::
   :label: Parameters for onAfterSend.addListener(listener)

   .. _compose.on^after^send.listener(tab, send^info):

   .. api-member::
      :name: ``listener(tab, sendInfo)``
      :refid: compose-on-after-send-listener-tab-send-info
      :refname: listener(tab, sendInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^after^send.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-after-send-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

      The tab of the associated compose window. By the time the event listener is called, this window may have already been destroyed.

   .. _compose.on^after^send.send^info:

   .. api-member::
      :name: ``sendInfo``
      :refid: compose-on-after-send-send-info
      :refname: sendInfo
      :type: (object)

      .. _compose.on^after^send.send^info.details:

      .. api-member::
         :name: ``details``
         :refid: compose-on-after-send-send-info-details
         :refname: details
         :type: (:ref:`compose.^compose^details`)

         The :ref:`compose.^compose^details` of the send message.

      .. _compose.on^after^send.send^info.messages:

      .. api-member::
         :name: ``messages``
         :refid: compose-on-after-send-send-info-messages
         :refname: messages
         :type: (array of :ref:`messages.^message^header`)

         Copies of the sent message. The number of created copies depends on the applied file carbon copy configuration (fcc). The :permission:`messagesRead` permission is required for this property to be included.

      .. _compose.on^after^send.send^info.mode:

      .. api-member::
         :name: ``mode``
         :refid: compose-on-after-send-send-info-mode
         :refname: mode
         :type: (`string`)

         The used send mode.

         Supported values:

         .. _compose.on^after^send.send^info.mode.send^later:

         .. api-member::
            :name: :value:`sendLater`
            :refid: compose-on-after-send-send-info-mode-send-later
            :refname: sendLater

         .. _compose.on^after^send.send^info.mode.send^now:

         .. api-member::
            :name: :value:`sendNow`
            :refid: compose-on-after-send-send-info-mode-send-now
            :refname: sendNow

      .. _compose.on^after^send.send^info.error:

      .. api-member::
         :name: [``error``]
         :refid: compose-on-after-send-send-info-error
         :refname: error
         :type: (string, optional)

         An error description, if sending the message failed.

      .. _compose.on^after^send.send^info.header^message^id:

      .. api-member::
         :name: [``headerMessageId``]
         :refid: compose-on-after-send-send-info-header-message-id
         :refname: headerMessageId
         :type: (string, optional)

         The header messageId of the outgoing message. Only included for actually sent messages.

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.on^attachment^added:

onAttachmentAdded
-----------------

.. api-section-annotation-hack:: 

Fired when an attachment is added to a message being composed.

.. api-header::
   :label: Parameters for onAttachmentAdded.addListener(listener)

   .. _compose.on^attachment^added.listener(tab, attachment):

   .. api-member::
      :name: ``listener(tab, attachment)``
      :refid: compose-on-attachment-added-listener-tab-attachment
      :refname: listener(tab, attachment)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^attachment^added.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-attachment-added-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^attachment^added.attachment:

   .. api-member::
      :name: ``attachment``
      :refid: compose-on-attachment-added-attachment
      :refname: attachment
      :type: (:ref:`compose.^compose^attachment`)

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.on^attachment^removed:

onAttachmentRemoved
-------------------

.. api-section-annotation-hack:: 

Fired when an attachment is removed from a message being composed.

.. api-header::
   :label: Parameters for onAttachmentRemoved.addListener(listener)

   .. _compose.on^attachment^removed.listener(tab, attachment^id):

   .. api-member::
      :name: ``listener(tab, attachmentId)``
      :refid: compose-on-attachment-removed-listener-tab-attachment-id
      :refname: listener(tab, attachmentId)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^attachment^removed.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-attachment-removed-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^attachment^removed.attachment^id:

   .. api-member::
      :name: ``attachmentId``
      :refid: compose-on-attachment-removed-attachment-id
      :refname: attachmentId
      :type: (integer)

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.on^before^send:

onBeforeSend
------------

.. api-section-annotation-hack:: 

Fired when a message is about to be sent from the compose window. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for onBeforeSend.addListener(listener)

   .. _compose.on^before^send.listener(tab, details):

   .. api-member::
      :name: ``listener(tab, details)``
      :refid: compose-on-before-send-listener-tab-details
      :refname: listener(tab, details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^before^send.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-before-send-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^before^send.details:

   .. api-member::
      :name: ``details``
      :refid: compose-on-before-send-details
      :refname: details
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
         :refname: cancel
         :type: (boolean, optional)

         Cancels the send.

      .. _compose.on^before^send.returns.details:

      .. api-member::
         :name: [``details``]
         :refid: compose-on-before-send-returns-details
         :refname: details
         :type: (:ref:`compose.^compose^details`, optional)

         Updates the compose window. This is functionally the same as calling the :ref:`compose.set^compose^details` function.

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.on^compose^state^changed:

onComposeStateChanged
---------------------

.. api-section-annotation-hack:: 

Fired when the state of the message composer changed.

.. api-header::
   :label: Parameters for onComposeStateChanged.addListener(listener)

   .. _compose.on^compose^state^changed.listener(tab, state):

   .. api-member::
      :name: ``listener(tab, state)``
      :refid: compose-on-compose-state-changed-listener-tab-state
      :refname: listener(tab, state)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^compose^state^changed.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-compose-state-changed-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^compose^state^changed.state:

   .. api-member::
      :name: ``state``
      :refid: compose-on-compose-state-changed-state
      :refname: state
      :type: (:ref:`compose.^compose^state`)

.. _compose.on^identity^changed:

onIdentityChanged
-----------------

.. api-section-annotation-hack:: 

Fired when the user changes the identity that will be used to send a message being composed.

.. api-header::
   :label: Parameters for onIdentityChanged.addListener(listener)

   .. _compose.on^identity^changed.listener(tab, identity^id):

   .. api-member::
      :name: ``listener(tab, identityId)``
      :refid: compose-on-identity-changed-listener-tab-identity-id
      :refname: listener(tab, identityId)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _compose.on^identity^changed.tab:

   .. api-member::
      :name: ``tab``
      :refid: compose-on-identity-changed-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

   .. _compose.on^identity^changed.identity^id:

   .. api-member::
      :name: ``identityId``
      :refid: compose-on-identity-changed-identity-id
      :refname: identityId
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

.. api-section-annotation-hack:: 

Represents an attachment in a message being composed.

.. api-header::
   :label: object

   .. _compose.^compose^attachment.id:

   .. api-member::
      :name: ``id``
      :refid: compose-compose-attachment-id
      :refname: id
      :type: (integer)

      A unique identifier for this attachment.

   .. _compose.^compose^attachment.name:

   .. api-member::
      :name: [``name``]
      :refid: compose-compose-attachment-name
      :refname: name
      :type: (string, optional)

      The name of this attachment, as displayed to the user.

   .. _compose.^compose^attachment.size:

   .. api-member::
      :name: [``size``]
      :refid: compose-compose-attachment-size
      :refname: size
      :type: (integer, optional)

      The size in bytes of this attachment. Read-only.

.. _compose.^compose^details:

ComposeDetails
--------------

.. api-section-annotation-hack:: 

Used by various functions to represent the state of a message being composed. Note that functions using this type may have a partial implementation.

.. api-header::
   :label: object

   .. _compose.^compose^details.additional^fcc^folder^id:

   .. api-member::
      :name: [``additionalFccFolderId``]
      :refid: compose-compose-details-additional-fcc-folder-id
      :refname: additionalFccFolderId
      :type: (:ref:`folders.^mail^folder^id`, optional)

      An additional fcc folder which can be selected while composing the message. Cleared when set to :value:`null`. The permission :permission:`accountsRead` is required to use this property.

   .. _compose.^compose^details.attachments:

   .. api-member::
      :name: [``attachments``]
      :refid: compose-compose-details-attachments
      :refname: attachments
      :type: (array of :ref:`compose.^file^attachment` or :ref:`compose.^compose^attachment`, optional)

      Only used in the begin* functions. Attachments to add to the message.

   .. _compose.^compose^details.attach^public^p^g^p^key:

   .. api-member::
      :name: [``attachPublicPGPKey``]
      :refid: compose-compose-details-attach-public-p-g-p-key
      :refname: attachPublicPGPKey
      :type: (boolean, optional)

      Whether the public OpenPGP key of the sending identity should be attached to the message.

   .. _compose.^compose^details.attach^v^card:

   .. api-member::
      :name: [``attachVCard``]
      :refid: compose-compose-details-attach-v-card
      :refname: attachVCard
      :type: (boolean, optional)

      Whether or not the vCard of the used identity will be attached to the message during send.

      .. note::

         If the value has not been modified, selecting a different identity will load the default value of the new identity.

   .. _compose.^compose^details.bcc:

   .. api-member::
      :name: [``bcc``]
      :refid: compose-compose-details-bcc
      :refname: bcc
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.body:

   .. api-member::
      :name: [``body``]
      :refid: compose-compose-details-body
      :refname: body
      :type: (string, optional)

      The HTML content of the message.

   .. _compose.^compose^details.cc:

   .. api-member::
      :name: [``cc``]
      :refid: compose-compose-details-cc
      :refname: cc
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.custom^headers:

   .. api-member::
      :name: [``customHeaders``]
      :refid: compose-compose-details-custom-headers
      :refname: customHeaders
      :type: (array of :ref:`compose.^custom^header`, optional)

      Array of custom headers. Headers will be returned in *Http-Header-Case* (a.k.a. *Train-Case*). Set an empty array to clear all custom headers.

   .. _compose.^compose^details.delivery^format:

   .. api-member::
      :name: [``deliveryFormat``]
      :refid: compose-compose-details-delivery-format
      :refname: deliveryFormat
      :type: (`string`, optional)

      Defines the MIME format of the sent message (ignored on plain text messages). Defaults to :value:`auto`, which will send html messages as plain text, if they do not include any formatting, and as :value:`both` otherwise (a multipart/mixed message).

      Supported values:

      .. _compose.^compose^details.delivery^format.auto:

      .. api-member::
         :name: :value:`auto`
         :refid: compose-compose-details-delivery-format-auto
         :refname: auto

      .. _compose.^compose^details.delivery^format.both:

      .. api-member::
         :name: :value:`both`
         :refid: compose-compose-details-delivery-format-both
         :refname: both

      .. _compose.^compose^details.delivery^format.html:

      .. api-member::
         :name: :value:`html`
         :refid: compose-compose-details-delivery-format-html
         :refname: html

      .. _compose.^compose^details.delivery^format.plaintext:

      .. api-member::
         :name: :value:`plaintext`
         :refid: compose-compose-details-delivery-format-plaintext
         :refname: plaintext

   .. _compose.^compose^details.delivery^status^notification:

   .. api-member::
      :name: [``deliveryStatusNotification``]
      :refid: compose-compose-details-delivery-status-notification
      :refname: deliveryStatusNotification
      :type: (boolean, optional)

      Let the sender know when the recipient's server received the message. Not supported by all servers.

   .. _compose.^compose^details.followup^to:

   .. api-member::
      :name: [``followupTo``]
      :refid: compose-compose-details-followup-to
      :refname: followupTo
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.from:

   .. api-member::
      :name: [``from``]
      :refid: compose-compose-details-from
      :refname: from
      :type: (:ref:`compose.^compose^recipient`, optional)

      *Caution*: Setting a value for :value:`from` does not change the used identity, it overrides the *From* header. Many email servers do not accept emails where the *From* header does not match the sender identity. Must be set to exactly one valid email address.

   .. _compose.^compose^details.identity^id:

   .. api-member::
      :name: [``identityId``]
      :refid: compose-compose-details-identity-id
      :refname: identityId
      :type: (string, optional)

      The ID of an identity from the :doc:`accounts`. The settings from the identity will be used in the composed message. If :value:`replyTo` is also specified, the :value:`replyTo` property of the identity is overridden. The permission :permission:`accountsRead` is required to include the :value:`identityId`.

   .. _compose.^compose^details.is^modified:

   .. api-member::
      :name: [``isModified``]
      :refid: compose-compose-details-is-modified
      :refname: isModified
      :type: (boolean, optional)

      Whether the composer is considered modified by the user. A modified composer asks for confirmation, when it is closed.

   .. _compose.^compose^details.is^plain^text:

   .. api-member::
      :name: [``isPlainText``]
      :refid: compose-compose-details-is-plain-text
      :refname: isPlainText
      :type: (boolean, optional)

      Whether the message is an HTML message or a plain text message.

   .. _compose.^compose^details.newsgroups:

   .. api-member::
      :name: [``newsgroups``]
      :refid: compose-compose-details-newsgroups
      :refname: newsgroups
      :type: (string or array of string, optional)

      A single newsgroup name or an array of newsgroup names.

   .. _compose.^compose^details.override^default^fcc^folder^id:

   .. api-member::
      :name: [``overrideDefaultFccFolderId``]
      :refid: compose-compose-details-override-default-fcc-folder-id
      :refname: overrideDefaultFccFolderId
      :type: (:ref:`folders.^mail^folder^id`, optional)

      This value overrides the default fcc setting (defined by the used identity) for this message only. Either a :ref:`folders.^mail^folder^id` specifying the folder for the copy of the sent message, or an empty string to not save a copy at all. Reset when set to :value:`null`. The permission :permission:`accountsRead` is required to use this property.

   .. _compose.^compose^details.plain^text^body:

   .. api-member::
      :name: [``plainTextBody``]
      :refid: compose-compose-details-plain-text-body
      :refname: plainTextBody
      :type: (string, optional)

      The plain text content of the message.

   .. _compose.^compose^details.priority:

   .. api-member::
      :name: [``priority``]
      :refid: compose-compose-details-priority
      :refname: priority
      :type: (`string`, optional)

      The priority of the message.

      Supported values:

      .. _compose.^compose^details.priority.high:

      .. api-member::
         :name: :value:`high`
         :refid: compose-compose-details-priority-high
         :refname: high

      .. _compose.^compose^details.priority.highest:

      .. api-member::
         :name: :value:`highest`
         :refid: compose-compose-details-priority-highest
         :refname: highest

      .. _compose.^compose^details.priority.low:

      .. api-member::
         :name: :value:`low`
         :refid: compose-compose-details-priority-low
         :refname: low

      .. _compose.^compose^details.priority.lowest:

      .. api-member::
         :name: :value:`lowest`
         :refid: compose-compose-details-priority-lowest
         :refname: lowest

      .. _compose.^compose^details.priority.normal:

      .. api-member::
         :name: :value:`normal`
         :refid: compose-compose-details-priority-normal
         :refname: normal

   .. _compose.^compose^details.related^message^id:

   .. api-member::
      :name: [``relatedMessageId``]
      :refid: compose-compose-details-related-message-id
      :refname: relatedMessageId
      :type: (:ref:`messages.^message^id`, optional)

      The id of the original message (in case of draft, template, forward or reply). Read-only. Is :value:`undefined` in all other cases or if the original message was opened from file. The :permission:`messagesRead` permission is required to use this property.

   .. _compose.^compose^details.reply^to:

   .. api-member::
      :name: [``replyTo``]
      :refid: compose-compose-details-reply-to
      :refname: replyTo
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.return^receipt:

   .. api-member::
      :name: [``returnReceipt``]
      :refid: compose-compose-details-return-receipt
      :refname: returnReceipt
      :type: (boolean, optional)

      Add the *Disposition-Notification-To* header to the message to requests the recipients email client to send a reply once the message has been received. Recipient server may strip the header and the recipient might ignore the request.

   .. _compose.^compose^details.selected^encryption^technology:

   .. api-member::
      :name: [``selectedEncryptionTechnology``]
      :refid: compose-compose-details-selected-encryption-technology
      :refname: selectedEncryptionTechnology
      :type: (:ref:`compose.^encryption^properties^s^m^i^m^e` or :ref:`compose.^encryption^properties^open^p^g^p`, optional)

      The selected encryption technology (:value:`OpenPGP` or :value:`S/MIME`) which is to be used to sign and/or encrypt the message. If the sending identity does not support encryption at all, this will be :value:`undefined`.

   .. _compose.^compose^details.subject:

   .. api-member::
      :name: [``subject``]
      :refid: compose-compose-details-subject
      :refname: subject
      :type: (string, optional)

   .. _compose.^compose^details.to:

   .. api-member::
      :name: [``to``]
      :refid: compose-compose-details-to
      :refname: to
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.type:

   .. api-member::
      :name: [``type``]
      :refid: compose-compose-details-type
      :refname: type
      :type: (`string`, optional)

      Read-only. The type of the message being composed, depending on how the compose window was opened by the user.

      Supported values:

      .. _compose.^compose^details.type.draft:

      .. api-member::
         :name: :value:`draft`
         :refid: compose-compose-details-type-draft
         :refname: draft

      .. _compose.^compose^details.type.forward:

      .. api-member::
         :name: :value:`forward`
         :refid: compose-compose-details-type-forward
         :refname: forward

      .. _compose.^compose^details.type.new:

      .. api-member::
         :name: :value:`new`
         :refid: compose-compose-details-type-new
         :refname: new

      .. _compose.^compose^details.type.redirect:

      .. api-member::
         :name: :value:`redirect`
         :refid: compose-compose-details-type-redirect
         :refname: redirect

      .. _compose.^compose^details.type.reply:

      .. api-member::
         :name: :value:`reply`
         :refid: compose-compose-details-type-reply
         :refname: reply

.. _compose.^compose^dictionaries:

ComposeDictionaries
-------------------

.. api-section-annotation-hack:: 

A *dictionary object* with entries for all installed dictionaries, having a language identifier as *key* (for example :value:`en-US`) and a boolean expression as *value*, indicating whether that dictionary is enabled for spellchecking or not.

.. api-header::
   :label: object

.. _compose.^compose^recipient:

ComposeRecipient
----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string

   .. container:: api-member-node

      .. container:: api-member-description-only

         A name and email address in mailbox format (:value:`Name <email@example.com>`), or just an email address. Mailing lists are specified as :value:`ListName <ListName>`. Use :ref:`messenger^utilities.parse^mailbox^string` to extract the name and/or the email from the mailbox string, or to expand mailing list entries.

*or*

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _compose.^compose^recipient.node^id:

         .. api-member::
            :name: ``nodeId``
            :refid: compose-compose-recipient-node-id
            :refname: nodeId
            :type: (string)

            The ID of a contact or mailing list node from the :doc:`addressBooks.contacts` or :doc:`addressBooks.mailingLists`.

         .. _compose.^compose^recipient.type:

         .. api-member::
            :name: ``type``
            :refid: compose-compose-recipient-type
            :refname: type
            :type: (`string`)

            Which sort of object this ID is for.

            Supported values:

            .. _compose.^compose^recipient.type.contact:

            .. api-member::
               :name: :value:`contact`
               :refid: compose-compose-recipient-type-contact
               :refname: contact

            .. _compose.^compose^recipient.type.mailing^list:

            .. api-member::
               :name: :value:`mailingList`
               :refid: compose-compose-recipient-type-mailing-list
               :refname: mailingList

.. _compose.^compose^recipient^list:

ComposeRecipientList
--------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: :ref:`compose.^compose^recipient`

*or*

.. api-header::
   :label: array of :ref:`compose.^compose^recipient`

.. _compose.^compose^state:

ComposeState
------------

.. api-section-annotation-hack:: 

Represent the state of the message composer.

.. api-header::
   :label: object

   .. _compose.^compose^state.can^send^later:

   .. api-member::
      :name: ``canSendLater``
      :refid: compose-compose-state-can-send-later
      :refname: canSendLater
      :type: (boolean)

      The message can be send later.

   .. _compose.^compose^state.can^send^now:

   .. api-member::
      :name: ``canSendNow``
      :refid: compose-compose-state-can-send-now
      :refname: canSendNow
      :type: (boolean)

      The message can be send now.

.. _compose.^custom^header:

CustomHeader
------------

.. api-section-annotation-hack:: 

A custom header definition.

.. api-header::
   :label: object

   .. _compose.^custom^header.name:

   .. api-member::
      :name: ``name``
      :refid: compose-custom-header-name
      :refname: name
      :type: (string)

      Name of a custom header, must be prefixed by :value:`X-` (but not by :value:`X-Mozilla-`) or be one of the explicitly allowed headers (:value:`MSIP_Labels`)

   .. _compose.^custom^header.value:

   .. api-member::
      :name: ``value``
      :refid: compose-custom-header-value
      :refname: value
      :type: (string)

.. _compose.^encryption^properties^open^p^g^p:

EncryptionPropertiesOpenPGP
---------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _compose.^encryption^properties^open^p^g^p.encrypt^body:

   .. api-member::
      :name: ``encryptBody``
      :refid: compose-encryption-properties-open-p-g-p-encrypt-body
      :refname: encryptBody
      :type: (boolean)

      Whether encryption of the message body using the OpenPGP technology is enabled.

      .. note::

         If encryption is enabled, but the `preconditions <https://support.mozilla.org/en-US/kb/thunderbird-help-cannot-encrypt>`__ for sending an encrypted message are not met, the message cannot be sent.

   .. _compose.^encryption^properties^open^p^g^p.encrypt^subject:

   .. api-member::
      :name: ``encryptSubject``
      :refid: compose-encryption-properties-open-p-g-p-encrypt-subject
      :refname: encryptSubject
      :type: (boolean)

      Whether encryption of the message subject using the OpenPGP technology is enabled (only supported if encryption of the body is enabled a well).

   .. _compose.^encryption^properties^open^p^g^p.name:

   .. api-member::
      :name: ``name``
      :refid: compose-encryption-properties-open-p-g-p-name
      :refname: name
      :type: (string)

   .. _compose.^encryption^properties^open^p^g^p.sign^message:

   .. api-member::
      :name: ``signMessage``
      :refid: compose-encryption-properties-open-p-g-p-sign-message
      :refname: signMessage
      :type: (boolean)

      Whether the message will be signed using the OpenPGP technology.

.. _compose.^encryption^properties^s^m^i^m^e:

EncryptionPropertiesSMIME
-------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _compose.^encryption^properties^s^m^i^m^e.encrypt^body:

   .. api-member::
      :name: ``encryptBody``
      :refid: compose-encryption-properties-s-m-i-m-e-encrypt-body
      :refname: encryptBody
      :type: (boolean)

      Whether encryption of the message body using the S/MIME technology is enabled.

      .. note::

         If encryption is enabled, but the `preconditions <https://support.mozilla.org/en-US/kb/thunderbird-help-cannot-encrypt>`__ for sending an encrypted message are not met, the message cannot be sent.

   .. _compose.^encryption^properties^s^m^i^m^e.name:

   .. api-member::
      :name: ``name``
      :refid: compose-encryption-properties-s-m-i-m-e-name
      :refname: name
      :type: (string)

   .. _compose.^encryption^properties^s^m^i^m^e.sign^message:

   .. api-member::
      :name: ``signMessage``
      :refid: compose-encryption-properties-s-m-i-m-e-sign-message
      :refname: signMessage
      :type: (boolean)

      Whether the message will be signed using the S/MIME technology

.. _compose.^file^attachment:

FileAttachment
--------------

.. api-section-annotation-hack:: 

Object used to add, update or rename an attachment in a message being composed.

.. api-header::
   :label: object

   .. _compose.^file^attachment.file:

   .. api-member::
      :name: [``file``]
      :refid: compose-file-attachment-file
      :refname: file
      :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__, optional)

      The new content for the attachment.

   .. _compose.^file^attachment.name:

   .. api-member::
      :name: [``name``]
      :refid: compose-file-attachment-name
      :refname: name
      :type: (string, optional)

      The new name for the attachment, as displayed to the user. If not specified, the name of the provided :value:`file` object is used.
