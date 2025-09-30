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

.. api-member::
   :name: :permission:`accountsRead`

   See your mail accounts, their identities and their folders.

.. api-member::
   :name: :permission:`compose`

   Read and modify your email messages as you compose and send them.

.. api-member::
   :name: :permission:`compose.save`

   Save composed email messages as drafts or templates.

.. api-member::
   :name: :permission:`compose.send`

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

   .. api-member::
      :name: ``tabId``
      :type: (integer)

   .. api-member::
      :name: ``attachment``
      :type: (:ref:`compose.^file^attachment` or :ref:`compose.^compose^attachment`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
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

   .. api-member::
      :name: ``messageId``
      :type: (:ref:`messages.^message^id`)

      The message to forward, as retrieved using other APIs.

   .. api-member::
      :name: [``forwardType``]
      :type: (`string`, optional)

      Supported values:

      .. api-member::
         :name: :value:`forwardAsAttachment`

      .. api-member::
         :name: :value:`forwardInline`

   .. api-member::
      :name: [``details``]
      :type: (:ref:`compose.^compose^details`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
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

   .. api-member::
      :name: [``messageId``]
      :type: (:ref:`messages.^message^id`, optional)

      If specified, the message or template to edit as a new message.

   .. api-member::
      :name: [``details``]
      :type: (:ref:`compose.^compose^details`, optional)
      :annotation: -- [Added in TB 84]

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
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

   .. api-member::
      :name: ``messageId``
      :type: (:ref:`messages.^message^id`)

      The message to reply to, as retrieved using other APIs.

   .. api-member::
      :name: [``replyType``]
      :type: (`string`, optional)

      Supported values:

      .. api-member::
         :name: :value:`replyToAll`

      .. api-member::
         :name: :value:`replyToList`

      .. api-member::
         :name: :value:`replyToSender`

   .. api-member::
      :name: [``details``]
      :type: (:ref:`compose.^compose^details`, optional)
      :annotation: -- [Added in TB 76]

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
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

   .. api-member::
      :name: ``tabId``
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
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

   .. api-member::
      :name: ``id``
      :type: (integer)

      The unique identifier for the attachment.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.get^compose^details:

getComposeDetails(tabId)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 74]

Fetches the current state of a compose window. Currently only a limited amount of information is available, more will be added in later versions.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``tabId``
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
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

   .. api-member::
      :name: ``tabId``
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`compose.^compose^state`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.list^attachments:

listAttachments(tabId)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Lists all of the attachments of the message being composed in the specified tab.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``tabId``
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
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

   .. api-member::
      :name: ``tabId``
      :type: (integer)

   .. api-member::
      :name: ``attachmentId``
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

   .. api-member::
      :name: ``tabId``
      :type: (integer)

   .. api-member::
      :name: [``options``]
      :type: (object, optional)

      .. api-member::
         :name: ``mode``
         :type: (`string`)

         Supported values:

         .. api-member::
            :name: :value:`draft`

         .. api-member::
            :name: :value:`template`

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: object

      .. api-member::
         :name: ``messages``
         :type: (array of :ref:`messages.^message^header`)

         An array with exactly one element, the saved message.

         .. note::

            Starting with Thunderbird version 142, the File Carbon Copy (FCC) configuration is no longer respected during save operations. Regardless of any FCC settings, only one message is saved, and it is stored in the default folder for the given save mode.

      .. api-member::
         :name: ``mode``
         :type: (`string`)

         The used save mode.

         Supported values:

         .. api-member::
            :name: :value:`draft`

         .. api-member::
            :name: :value:`template`

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

   .. api-member::
      :name: ``tabId``
      :type: (integer)

   .. api-member::
      :name: [``options``]
      :type: (object, optional)

      .. api-member::
         :name: ``mode``
         :type: (`string`)

         Supported values:

         .. api-member::
            :name: :value:`default`

         .. api-member::
            :name: :value:`sendLater`

         .. api-member::
            :name: :value:`sendNow`

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: object

      .. api-member::
         :name: ``messages``
         :type: (array of :ref:`messages.^message^header`)
         :annotation: -- [Added in TB 102]

         Copies of the sent message. The number of created copies depends on the applied file carbon copy configuration (fcc).

      .. api-member::
         :name: ``mode``
         :type: (`string`)
         :annotation: -- [Added in TB 102]

         The used send mode.

         Supported values:

         .. api-member::
            :name: :value:`sendLater`

         .. api-member::
            :name: :value:`sendNow`

      .. api-member::
         :name: [``headerMessageId``]
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

   .. api-member::
      :name: ``tabId``
      :type: (integer)

   .. api-member::
      :name: ``activeDictionaries``
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

   .. api-member::
      :name: ``tabId``
      :type: (integer)

   .. api-member::
      :name: ``details``
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

   .. api-member::
      :name: ``tabId``
      :type: (integer)

   .. api-member::
      :name: ``attachmentId``
      :type: (integer)

   .. api-member::
      :name: ``attachment``
      :type: (:ref:`compose.^file^attachment`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
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

   .. api-member::
      :name: ``listener(tab, dictionaries)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.^tab`)

   .. api-member::
      :name: ``dictionaries``
      :type: (:ref:`compose.^compose^dictionaries`)

.. _compose.on^after^save:

onAfterSave
-----------

.. api-section-annotation-hack:: -- [Added in TB 105]

Fired when saving a message as draft or template succeeded or failed.

.. api-header::
   :label: Parameters for onAfterSave.addListener(listener)

   .. api-member::
      :name: ``listener(tab, saveInfo)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.^tab`)

   .. api-member::
      :name: ``saveInfo``
      :type: (object)

      .. api-member::
         :name: ``messages``
         :type: (array of :ref:`messages.^message^header`)

         An array with exactly one element, the saved message.

         .. note::

            Starting with Thunderbird version 142, the File Carbon Copy (FCC) configuration is no longer respected during save operations. Regardless of any FCC settings, only one message is saved, and it is stored in the default folder for the given save mode.

      .. api-member::
         :name: ``mode``
         :type: (`string`)

         The used save mode.

         Supported values:

         .. api-member::
            :name: :value:`autoSave`
            :annotation: -- [Added in TB 125]

         .. api-member::
            :name: :value:`draft`

         .. api-member::
            :name: :value:`template`

      .. api-member::
         :name: [``error``]
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

   .. api-member::
      :name: ``listener(tab, sendInfo)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.^tab`)

   .. api-member::
      :name: ``sendInfo``
      :type: (object)

      .. api-member::
         :name: ``messages``
         :type: (array of :ref:`messages.^message^header`)

         Copies of the sent message. The number of created copies depends on the applied file carbon copy configuration (fcc).

      .. api-member::
         :name: ``mode``
         :type: (`string`)

         The used send mode.

         Supported values:

         .. api-member::
            :name: :value:`sendLater`

         .. api-member::
            :name: :value:`sendNow`

      .. api-member::
         :name: [``error``]
         :type: (string, optional)

         An error description, if sending the message failed.

      .. api-member::
         :name: [``headerMessageId``]
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

   .. api-member::
      :name: ``listener(tab, attachment)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.^tab`)

   .. api-member::
      :name: ``attachment``
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

   .. api-member::
      :name: ``listener(tab, attachmentId)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.^tab`)

   .. api-member::
      :name: ``attachmentId``
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

   .. api-member::
      :name: ``listener(tab, details)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.^tab`)

   .. api-member::
      :name: ``details``
      :type: (:ref:`compose.^compose^details`)

      The current state of the compose window. This is functionally the same as calling the :ref:`compose.get^compose^details` function.

.. api-header::
   :label: Expected return value of the listener function

   .. api-member::
      :type: object

      .. api-member::
         :name: [``cancel``]
         :type: (boolean, optional)

         Cancels the send.

      .. api-member::
         :name: [``details``]
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

   .. api-member::
      :name: ``listener(tab, state)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.^tab`)

   .. api-member::
      :name: ``state``
      :type: (:ref:`compose.^compose^state`)

.. _compose.on^identity^changed:

onIdentityChanged
-----------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Fired when the user changes the identity that will be used to send a message being composed.

.. api-header::
   :label: Parameters for onIdentityChanged.addListener(listener)

   .. api-member::
      :name: ``listener(tab, identityId)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.^tab`)

   .. api-member::
      :name: ``identityId``
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
      :type: (integer)

      A unique identifier for this attachment.

   .. _compose.^compose^attachment.name:

   .. api-member::
      :name: [``name``]
      :type: (string, optional)

      The name of this attachment, as displayed to the user.

   .. _compose.^compose^attachment.size:

   .. api-member::
      :name: [``size``]
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

   .. _compose.^compose^details.additional^fcc^folder^id:

   .. api-member::
      :name: [``additionalFccFolderId``]
      :type: (:ref:`folders.^mail^folder^id`, optional)
      :annotation: -- [Added in TB 127]

      An additional fcc folder which can be selected while composing the message. Cleared when set to :value:`null`. The permission :permission:`accountsRead` is required to use this property.

   .. _compose.^compose^details.attachments:

   .. api-member::
      :name: [``attachments``]
      :type: (array of :ref:`compose.^file^attachment` or :ref:`compose.^compose^attachment`, optional)
      :annotation: -- [Added in TB 82]

      Only used in the begin* functions. Attachments to add to the message.

   .. _compose.^compose^details.attach^public^p^g^p^key:

   .. api-member::
      :name: [``attachPublicPGPKey``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 128]

      Whether the public OpenPGP key of the sending identity should be attached to the message.

   .. _compose.^compose^details.attach^v^card:

   .. api-member::
      :name: [``attachVCard``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 102]

      Whether or not the vCard of the used identity will be attached to the message during send.

      .. note::

         If the value has not been modified, selecting a different identity will load the default value of the new identity.

   .. _compose.^compose^details.bcc:

   .. api-member::
      :name: [``bcc``]
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.body:

   .. api-member::
      :name: [``body``]
      :type: (string, optional)

      The HTML content of the message.

   .. _compose.^compose^details.cc:

   .. api-member::
      :name: [``cc``]
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.custom^headers:

   .. api-member::
      :name: [``customHeaders``]
      :type: (array of :ref:`compose.^custom^header`, optional)
      :annotation: -- [Added in TB 100]

      Array of custom headers. Headers will be returned in *Http-Header-Case* (a.k.a. *Train-Case*). Set an empty array to clear all custom headers.

   .. _compose.^compose^details.delivery^format:

   .. api-member::
      :name: [``deliveryFormat``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 102]

      Defines the MIME format of the sent message (ignored on plain text messages). Defaults to :value:`auto`, which will send html messages as plain text, if they do not include any formatting, and as :value:`both` otherwise (a multipart/mixed message).

      Supported values:

      .. api-member::
         :name: :value:`auto`

      .. api-member::
         :name: :value:`both`

      .. api-member::
         :name: :value:`html`

      .. api-member::
         :name: :value:`plaintext`

   .. _compose.^compose^details.delivery^status^notification:

   .. api-member::
      :name: [``deliveryStatusNotification``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 102]

      Let the sender know when the recipient's server received the message. Not supported by all servers.

   .. _compose.^compose^details.followup^to:

   .. api-member::
      :name: [``followupTo``]
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.from:

   .. api-member::
      :name: [``from``]
      :type: (:ref:`compose.^compose^recipient`, optional)
      :annotation: -- [Added in TB 88]

      *Caution*: Setting a value for :value:`from` does not change the used identity, it overrides the *From* header. Many email servers do not accept emails where the *From* header does not match the sender identity. Must be set to exactly one valid email address.

   .. _compose.^compose^details.identity^id:

   .. api-member::
      :name: [``identityId``]
      :type: (string, optional)
      :annotation: -- [Added in TB 76]

      The ID of an identity from the :doc:`accounts`. The settings from the identity will be used in the composed message. If :value:`replyTo` is also specified, the :value:`replyTo` property of the identity is overridden. The permission :permission:`accountsRead` is required to include the :value:`identityId`.

   .. _compose.^compose^details.is^modified:

   .. api-member::
      :name: [``isModified``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 125]

      Whether the composer is considered modified by the user. A modified composer asks for confirmation, when it is closed.

   .. _compose.^compose^details.is^plain^text:

   .. api-member::
      :name: [``isPlainText``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 75]

      Whether the message is an HTML message or a plain text message.

   .. _compose.^compose^details.newsgroups:

   .. api-member::
      :name: [``newsgroups``]
      :type: (string or array of string, optional)

      A single newsgroup name or an array of newsgroup names.

   .. _compose.^compose^details.override^default^fcc^folder^id:

   .. api-member::
      :name: [``overrideDefaultFccFolderId``]
      :type: (:ref:`folders.^mail^folder^id`, optional)
      :annotation: -- [Added in TB 127]

      This value overrides the default fcc setting (defined by the used identity) for this message only. Either a :ref:`folders.^mail^folder^id` specifying the folder for the copy of the sent message, or an empty string to not save a copy at all. Reset when set to :value:`null`. The permission :permission:`accountsRead` is required to use this property.

   .. _compose.^compose^details.plain^text^body:

   .. api-member::
      :name: [``plainTextBody``]
      :type: (string, optional)
      :annotation: -- [Added in TB 75]

      The plain text content of the message.

   .. _compose.^compose^details.priority:

   .. api-member::
      :name: [``priority``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 102]

      The priority of the message.

      Supported values:

      .. api-member::
         :name: :value:`high`

      .. api-member::
         :name: :value:`highest`

      .. api-member::
         :name: :value:`low`

      .. api-member::
         :name: :value:`lowest`

      .. api-member::
         :name: :value:`normal`

   .. _compose.^compose^details.related^message^id:

   .. api-member::
      :name: [``relatedMessageId``]
      :type: (:ref:`messages.^message^id`, optional)
      :annotation: -- [Added in TB 95]

      The id of the original message (in case of draft, template, forward or reply). Read-only. Is :value:`undefined` in all other cases or if the original message was opened from file.

   .. _compose.^compose^details.reply^to:

   .. api-member::
      :name: [``replyTo``]
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.return^receipt:

   .. api-member::
      :name: [``returnReceipt``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 102]

      Add the *Disposition-Notification-To* header to the message to requests the recipients email client to send a reply once the message has been received. Recipient server may strip the header and the recipient might ignore the request.

   .. _compose.^compose^details.selected^encryption^technology:

   .. api-member::
      :name: [``selectedEncryptionTechnology``]
      :type: (:ref:`compose.^encryption^properties^s^m^i^m^e` or :ref:`compose.^encryption^properties^open^p^g^p`, optional)
      :annotation: -- [Added in TB 128]

      The selected encryption technology (:value:`OpenPGP` or :value:`S/MIME`) which is to be used to sign and/or encrypt the message. If the sending identity does not support encryption at all, this will be :value:`undefined`.

   .. _compose.^compose^details.subject:

   .. api-member::
      :name: [``subject``]
      :type: (string, optional)

   .. _compose.^compose^details.to:

   .. api-member::
      :name: [``to``]
      :type: (:ref:`compose.^compose^recipient^list`, optional)

   .. _compose.^compose^details.type:

   .. api-member::
      :name: [``type``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 88]

      Read-only. The type of the message being composed, depending on how the compose window was opened by the user.

      Supported values:

      .. api-member::
         :name: :value:`draft`

      .. api-member::
         :name: :value:`forward`

      .. api-member::
         :name: :value:`new`

      .. api-member::
         :name: :value:`redirect`
         :annotation: -- [Added in TB 90]

      .. api-member::
         :name: :value:`reply`

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

         .. api-member::
            :name: ``nodeId``
            :type: (string)
            :annotation: -- [Added in TB 128]

            The ID of a contact or mailing list node from the :doc:`addressBook.contacts` or :doc:`addressBook.mailingLists`.

         .. api-member::
            :name: ``type``
            :type: (`string`)

            Which sort of object this ID is for.

            Supported values:

            .. api-member::
               :name: :value:`contact`

            .. api-member::
               :name: :value:`mailingList`

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
      :type: (boolean)

      The message can be send later.

   .. _compose.^compose^state.can^send^now:

   .. api-member::
      :name: ``canSendNow``
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
      :type: (string)

      Name of a custom header, must be prefixed by :value:`X-` (but not by :value:`X-Mozilla-`) or be one of the explicitly allowed headers (:value:`MSIP_Labels`)

   .. _compose.^custom^header.value:

   .. api-member::
      :name: ``value``
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
      :type: (boolean)

      Whether encryption of the message body using the OpenPGP technology is enabled.

      .. note::

         If encryption is enabled, but the `preconditions <https://support.mozilla.org/en-US/kb/thunderbird-help-cannot-encrypt>`__ for sending an encrypted message are not met, the message cannot be sent.

   .. _compose.^encryption^properties^open^p^g^p.encrypt^subject:

   .. api-member::
      :name: ``encryptSubject``
      :type: (boolean)

      Whether encryption of the message subject using the OpenPGP technology is enabled (only supported if encryption of the body is enabled a well).

   .. _compose.^encryption^properties^open^p^g^p.name:

   .. api-member::
      :name: ``name``
      :type: (string)

   .. _compose.^encryption^properties^open^p^g^p.sign^message:

   .. api-member::
      :name: ``signMessage``
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
      :type: (boolean)

      Whether encryption of the message body using the S/MIME technology is enabled.

      .. note::

         If encryption is enabled, but the `preconditions <https://support.mozilla.org/en-US/kb/thunderbird-help-cannot-encrypt>`__ for sending an encrypted message are not met, the message cannot be sent.

   .. _compose.^encryption^properties^s^m^i^m^e.name:

   .. api-member::
      :name: ``name``
      :type: (string)

   .. _compose.^encryption^properties^s^m^i^m^e.sign^message:

   .. api-member::
      :name: ``signMessage``
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
      :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__, optional)

      The new content for the attachment.

   .. _compose.^file^attachment.name:

   .. api-member::
      :name: [``name``]
      :type: (string, optional)

      The new name for the attachment, as displayed to the user. If not specified, the name of the provided :value:`file` object is used.
