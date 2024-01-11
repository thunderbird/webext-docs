.. container:: sticky-sidebar

  ≡ compose API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /overlay/developer-resources.rst

  ≡ Related information
  
  * :doc:`/examples/eventListeners`

  ≡ Related examples on Github

  * `"Compose Body" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v2/composeBody>`__

===========
compose API
===========

The compose API first appeared in Thunderbird 67. It allows to interact with the message composition window.

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`compose`

   Read and modify your email messages as you compose and send them

.. api-member::
   :name: :permission:`compose.save`

   Save composed email messages as drafts or templates

.. api-member::
   :name: :permission:`compose.send`

   Send composed email messages on your behalf

.. rst-class:: api-main-section

Functions
=========

.. _compose.addAttachment:

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
      :type: (:ref:`compose.FileAttachment` or :ref:`compose.ComposeAttachment`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`compose.ComposeAttachment`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.beginForward:

beginForward(messageId, [forwardType], [details])
-------------------------------------------------

.. api-section-annotation-hack:: 

Open a new message compose window forwarding a given message.

**Note:** The compose format can be set by ``details.isPlainText`` or by specifying only one of ``details.body`` or ``details.plainTextBody``. Otherwise the default compose format of the selected identity is used.

**Note:** Specifying ``details.body`` and ``details.plainTextBody`` without also specifying ``details.isPlainText`` threw an exception in Thunderbird up to version 97. Since Thunderbird 98, this combination creates a compose window with the compose format of the selected identity, using the matching ``details.body`` or ``details.plainTextBody`` value.

**Note:** If no identity is specified, this function is using the default identity and not the identity of the referenced message.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (:ref:`messages.MessageId`)
      
      The message to forward, as retrieved using other APIs.
   
   
   .. api-member::
      :name: [``forwardType``]
      :type: (`string`, optional)
      
      Supported values:
      
      .. api-member::
         :name: :value:`forwardInline`
      
      .. api-member::
         :name: :value:`forwardAsAttachment`
   
   
   .. api-member::
      :name: [``details``]
      :type: (:ref:`compose.ComposeDetails`, optional)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`tabs.Tab`
      :annotation: -- [Added in TB 77]
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.beginNew:

beginNew([messageId], [details])
--------------------------------

.. api-section-annotation-hack:: 

Open a new message compose window.

**Note:** The compose format can be set by ``details.isPlainText`` or by specifying only one of ``details.body`` or ``details.plainTextBody``. Otherwise the default compose format of the selected identity is used.

**Note:** Specifying ``details.body`` and ``details.plainTextBody`` without also specifying ``details.isPlainText`` threw an exception in Thunderbird up to version 97. Since Thunderbird 98, this combination creates a compose window with the compose format of the selected identity, using the matching ``details.body`` or ``details.plainTextBody`` value.

**Note:** If no identity is specified, this function is using the default identity and not the identity of the referenced message.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``messageId``]
      :type: (:ref:`messages.MessageId`, optional)
      :annotation: -- [Added in TB 84, backported to TB 78.7.0]
      
      If specified, the message or template to edit as a new message.
   
   
   .. api-member::
      :name: [``details``]
      :type: (:ref:`compose.ComposeDetails`, optional)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`tabs.Tab`
      :annotation: -- [Added in TB 77]
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.beginReply:

beginReply(messageId, [replyType], [details])
---------------------------------------------

.. api-section-annotation-hack:: 

Open a new message compose window replying to a given message.

**Note:** The compose format can be set by ``details.isPlainText`` or by specifying only one of ``details.body`` or ``details.plainTextBody``. Otherwise the default compose format of the selected identity is used.

**Note:** Specifying ``details.body`` and ``details.plainTextBody`` without also specifying ``details.isPlainText`` threw an exception in Thunderbird up to version 97. Since Thunderbird 98, this combination creates a compose window with the compose format of the selected identity, using the matching ``details.body`` or ``details.plainTextBody`` value.

**Note:** If no identity is specified, this function is using the default identity and not the identity of the referenced message.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (:ref:`messages.MessageId`)
      
      The message to reply to, as retrieved using other APIs.
   
   
   .. api-member::
      :name: [``replyType``]
      :type: (`string`, optional)
      
      Supported values:
      
      .. api-member::
         :name: :value:`replyToSender`
      
      .. api-member::
         :name: :value:`replyToList`
      
      .. api-member::
         :name: :value:`replyToAll`
   
   
   .. api-member::
      :name: [``details``]
      :type: (:ref:`compose.ComposeDetails`, optional)
      :annotation: -- [Added in TB 76]
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`tabs.Tab`
      :annotation: -- [Added in TB 77]
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.getActiveDictionaries:

getActiveDictionaries(tabId)
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Returns a :ref:`compose.ComposeDictionaries` object, listing all installed dictionaries, including the information whether they are currently enabled or not.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`compose.ComposeDictionaries`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.getAttachmentFile:

getAttachmentFile(id)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 98]

Gets the content of a :ref:`compose.ComposeAttachment` as a `File <https://developer.mozilla.org/docs/Web/API/File>`__ object.

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

.. _compose.getComposeDetails:

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
      :type: :ref:`compose.ComposeDetails`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.getComposeState:

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
      :type: :ref:`compose.ComposeState`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose.listAttachments:

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
      :type: array of :ref:`compose.ComposeAttachment`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.removeAttachment:

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

.. _compose.saveMessage:

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
         :type: (array of :ref:`messages.MessageHeader`)
         
         The saved message(s). The number of saved messages depends on the applied file carbon copy configuration (fcc).
      
      
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

.. _compose.sendMessage:

sendMessage(tabId, [options])
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 90]

Sends the message currently being composed. If the send mode is not specified or set to :value:`default`, the message will be send directly if the user is online and placed in the users outbox otherwise. The returned Promise fulfills once the message has been successfully sent or placed in the user's outbox. Throws when the send process has been aborted by the user, by an :ref:`compose.onBeforeSend` event or if there has been an error while sending the message to the outgoing mail server.

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
            :name: :value:`sendNow`
         
         .. api-member::
            :name: :value:`sendLater`
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: object
      :annotation: -- [Added in TB 102]
      
      .. api-member::
         :name: ``messages``
         :type: (array of :ref:`messages.MessageHeader`)
         
         Copies of the sent message. The number of created copies depends on the applied file carbon copy configuration (fcc).
      
      
      .. api-member::
         :name: ``mode``
         :type: (`string`)
         
         The used send mode.
         
         Supported values:
         
         .. api-member::
            :name: :value:`sendNow`
         
         .. api-member::
            :name: :value:`sendLater`
      
      
      .. api-member::
         :name: [``headerMessageId``]
         :type: (string, optional)
         
         The header messageId of the outgoing message. Only included for actually sent messages.
      
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose.send`

.. _compose.setActiveDictionaries:

setActiveDictionaries(tabId, activeDictionaries)
------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Updates the active dictionaries. Throws if the ``activeDictionaries`` array contains unknown or invalid language identifiers.

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

.. _compose.setComposeDetails:

setComposeDetails(tabId, details)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 74]

Updates the compose window. The properties of the given :ref:`compose.ComposeDetails` object will be used to overwrite the current values of the specified compose window, so only properties that are to be changed should be included.

When updating any of the array properties (``customHeaders`` and most address fields), make sure to first get the current values to not accidentally remove all existing entries when setting the new value.

**Note:** The compose format of an existing compose window cannot be changed. Since Thunderbird 98, setting conflicting values for ``details.body``, ``details.plainTextBody`` or ``details.isPlaintext`` no longer throws an exception, instead the compose window chooses the matching ``details.body`` or ``details.plainTextBody`` value and ignores the other.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``details``
      :type: (:ref:`compose.ComposeDetails`)
   

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.updateAttachment:

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
      :type: (:ref:`compose.FileAttachment`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`compose.ComposeAttachment`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. rst-class:: api-main-section

Events
======

.. _compose.onActiveDictionariesChanged:

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
      :type: (:ref:`tabs.Tab`)
   
   
   .. api-member::
      :name: ``dictionaries``
      :type: (:ref:`compose.ComposeDictionaries`)
   

.. _compose.onAfterSave:

onAfterSave
-----------

.. api-section-annotation-hack:: -- [Added in TB 106, backported to TB 102.3.0]

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
      :type: (:ref:`tabs.Tab`)
   
   
   .. api-member::
      :name: ``saveInfo``
      :type: (object)
      
      .. api-member::
         :name: ``messages``
         :type: (array of :ref:`messages.MessageHeader`)
         
         The saved message(s). The number of saved messages depends on the applied file carbon copy configuration (fcc).
      
      
      .. api-member::
         :name: ``mode``
         :type: (`string`)
         
         The used save mode.
         
         Supported values:
         
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

.. _compose.onAfterSend:

onAfterSend
-----------

.. api-section-annotation-hack:: -- [Added in TB 106, backported to TB 102.3.0]

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
      :type: (:ref:`tabs.Tab`)
   
   
   .. api-member::
      :name: ``sendInfo``
      :type: (object)
      
      .. api-member::
         :name: ``messages``
         :type: (array of :ref:`messages.MessageHeader`)
         
         Copies of the sent message. The number of created copies depends on the applied file carbon copy configuration (fcc).
      
      
      .. api-member::
         :name: ``mode``
         :type: (`string`)
         
         The used send mode.
         
         Supported values:
         
         .. api-member::
            :name: :value:`sendNow`
         
         .. api-member::
            :name: :value:`sendLater`
      
      
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

.. _compose.onAttachmentAdded:

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
      :type: (:ref:`tabs.Tab`)
   
   
   .. api-member::
      :name: ``attachment``
      :type: (:ref:`compose.ComposeAttachment`)
   

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.onAttachmentRemoved:

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
      :type: (:ref:`tabs.Tab`)
   
   
   .. api-member::
      :name: ``attachmentId``
      :type: (integer)
   

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.onBeforeSend:

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
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Added in TB 74.0b2]
   
   
   .. api-member::
      :name: ``details``
      :type: (:ref:`compose.ComposeDetails`)
      
      The current state of the compose window. This is functionally the same as calling the :ref:`compose.getComposeDetails` function.
   

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
         :type: (:ref:`compose.ComposeDetails`, optional)
         
         Updates the compose window. This is functionally the same as calling the :ref:`compose.setComposeDetails` function.
      
   

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.onComposeStateChanged:

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
      :type: (:ref:`tabs.Tab`)
   
   
   .. api-member::
      :name: ``state``
      :type: (:ref:`compose.ComposeState`)
   

.. _compose.onIdentityChanged:

onIdentityChanged
-----------------

.. api-section-annotation-hack:: -- [Added in TB 78.0b2]

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
      :type: (:ref:`tabs.Tab`)
   
   
   .. api-member::
      :name: ``identityId``
      :type: (string)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Types
=====

.. _compose.ComposeAttachment:

ComposeAttachment
-----------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Represents an attachment in a message being composed.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``getFile()``
      :type: (function) **Deprecated.**
      
      Use :ref:`compose.getAttachmentFile` instead, for example in a backward-compatible drop-in wrapper function: 
      
      .. literalinclude:: includes/compose/getFile.js
        :language: JavaScript
      
      
   
   
   .. api-member::
      :name: ``id``
      :type: (integer)
      
      A unique identifier for this attachment.
   
   
   .. api-member::
      :name: [``name``]
      :type: (string, optional)
      
      The name of this attachment, as displayed to the user.
   
   
   .. api-member::
      :name: [``size``]
      :type: (integer, optional)
      :annotation: -- [Added in TB 83, backported to TB 78.5.0]
      
      The size in bytes of this attachment. Read-only.
   

.. _compose.ComposeDetails:

ComposeDetails
--------------

.. api-section-annotation-hack:: 

Used by various functions to represent the state of a message being composed. Note that functions using this type may have a partial implementation.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``additionalFccFolder``]
      :type: (:ref:`folders.MailFolder` or `string`, optional)
      :annotation: -- [Added in TB 102]
      
      An additional fcc folder which can be selected while composing the message, an empty string if not used.
   
   
   .. api-member::
      :name: [``attachVCard``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 102]
      
      Whether or not the vCard of the used identity will be attached to the message during send. Note: If the value has not been modified, selecting a different identity will load the default value of the new identity.
   
   
   .. api-member::
      :name: [``attachments``]
      :type: (array of :ref:`compose.FileAttachment` or :ref:`compose.ComposeAttachment`, optional)
      :annotation: -- [Added in TB 82, backported to TB 78.4.0]
      
      Only used in the begin* functions. Attachments to add to the message.
   
   
   .. api-member::
      :name: [``bcc``]
      :type: (:ref:`compose.ComposeRecipientList`, optional)
   
   
   .. api-member::
      :name: [``body``]
      :type: (string, optional)
      
      The HTML content of the message.
   
   
   .. api-member::
      :name: [``cc``]
      :type: (:ref:`compose.ComposeRecipientList`, optional)
   
   
   .. api-member::
      :name: [``customHeaders``]
      :type: (array of :ref:`compose.CustomHeader`, optional)
      :annotation: -- [Added in TB 100]
      
      Array of custom headers. Headers will be returned in *Http-Header-Case* (a.k.a. *Train-Case*). Set an empty array to clear all custom headers.
   
   
   .. api-member::
      :name: [``deliveryFormat``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 102]
      
      Defines the mime format of the sent message (ignored on plain text messages). Defaults to :value:`auto`, which will send html messages as plain text, if they do not include any formatting, and as :value:`both` otherwise (a multipart/mixed message).
      
      Supported values:
      
      .. api-member::
         :name: :value:`auto`
      
      .. api-member::
         :name: :value:`plaintext`
      
      .. api-member::
         :name: :value:`html`
      
      .. api-member::
         :name: :value:`both`
   
   
   .. api-member::
      :name: [``deliveryStatusNotification``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 102]
      
      Let the sender know when the recipient's server received the message. Not supported by all servers.
   
   
   .. api-member::
      :name: [``followupTo``]
      :type: (:ref:`compose.ComposeRecipientList`, optional)
      :annotation: -- [Added in TB 74]
   
   
   .. api-member::
      :name: [``from``]
      :type: (:ref:`compose.ComposeRecipient`, optional)
      :annotation: -- [Added in TB 88]
      
      *Caution*: Setting a value for ``from`` does not change the used identity, it overrides the FROM header. Many email servers do not accept emails where the FROM header does not match the sender identity. Must be set to exactly one valid email address.
   
   
   .. api-member::
      :name: [``identityId``]
      :type: (string, optional)
      :annotation: -- [Added in TB 76]
      
      The ID of an identity from the :doc:`accounts`. The settings from the identity will be used in the composed message. If ``replyTo`` is also specified, the ``replyTo`` property of the identity is overridden. The permission :permission:`accountsRead` is required to include the ``identityId``.
   
   
   .. api-member::
      :name: [``isPlainText``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 75]
      
      Whether the message is an HTML message or a plain text message.
   
   
   .. api-member::
      :name: [``newsgroups``]
      :type: (string or array of string, optional)
      :annotation: -- [Added in TB 74]
      
      A single newsgroup name or an array of newsgroup names.
   
   
   .. api-member::
      :name: [``overrideDefaultFcc``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 102]
      
      Indicates whether the default fcc setting (defined by the used identity) is being overridden for this message. Setting :value:`false` will clear the override. Setting :value:`true` will throw an *ExtensionError*, if ``overrideDefaultFccFolder`` is not set as well.
   
   
   .. api-member::
      :name: [``overrideDefaultFccFolder``]
      :type: (:ref:`folders.MailFolder` or `string`, optional)
      :annotation: -- [Added in TB 102]
      
       This value overrides the default fcc setting (defined by the used identity) for this message only. Either a :ref:`folders.MailFolder` specifying the folder for the copy of the sent message, or an empty string to not save a copy at all.
   
   
   .. api-member::
      :name: [``plainTextBody``]
      :type: (string, optional)
      :annotation: -- [Added in TB 75]
      
      The plain text content of the message.
   
   
   .. api-member::
      :name: [``priority``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 102]
      
      The priority of the message.
      
      Supported values:
      
      .. api-member::
         :name: :value:`lowest`
      
      .. api-member::
         :name: :value:`low`
      
      .. api-member::
         :name: :value:`normal`
      
      .. api-member::
         :name: :value:`high`
      
      .. api-member::
         :name: :value:`highest`
   
   
   .. api-member::
      :name: [``relatedMessageId``]
      :type: (:ref:`messages.MessageId`, optional)
      :annotation: -- [Added in TB 95]
      
      The id of the original message (in case of draft, template, forward or reply). Read-only. Is :value:`null` in all other cases or if the original message was opened from file.
   
   
   .. api-member::
      :name: [``replyTo``]
      :type: (:ref:`compose.ComposeRecipientList`, optional)
   
   
   .. api-member::
      :name: [``returnReceipt``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 102]
      
      Add the *Disposition-Notification-To* header to the message to requests the recipients email client to send a reply once the message has been received. Recipient server may strip the header and the recipient might ignore the request.
   
   
   .. api-member::
      :name: [``subject``]
      :type: (string, optional)
   
   
   .. api-member::
      :name: [``to``]
      :type: (:ref:`compose.ComposeRecipientList`, optional)
   
   
   .. api-member::
      :name: [``type``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 88]
      
      Read-only. The type of the message being composed, depending on how the compose window was opened by the user.
      
      Supported values:
      
      .. api-member::
         :name: :value:`draft`
      
      .. api-member::
         :name: :value:`new`
      
      .. api-member::
         :name: :value:`redirect`
         :annotation: -- [Added in TB 90]
      
      .. api-member::
         :name: :value:`reply`
      
      .. api-member::
         :name: :value:`forward`
   

.. _compose.ComposeDictionaries:

ComposeDictionaries
-------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

A *dictionary object* with entries for all installed dictionaries, having a language identifier as *key* (for example :value:`en-US`) and a boolean expression as *value*, indicating whether that dictionary is enabled for spellchecking or not.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``<language identifier>``
      :type: (boolean)
   

.. _compose.ComposeRecipient:

ComposeRecipient
----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         A name and email address in the format :value:`Name <email@example.com>`, or just an email address.
   

OR

.. api-header::
   :label: object

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         .. api-member::
            :name: ``id``
            :type: (string)
            
            The ID of a contact or mailing list from the :doc:`contacts` and :doc:`mailingLists`.
         
         
         .. api-member::
            :name: ``type``
            :type: (`string`)
            
            Which sort of object this ID is for.
            
            Supported values:
            
            .. api-member::
               :name: :value:`contact`
            
            .. api-member::
               :name: :value:`mailingList`
         
   

.. _compose.ComposeRecipientList:

ComposeRecipientList
--------------------

.. api-section-annotation-hack:: -- [Added in TB 74]

.. api-header::
   :label: :ref:`compose.ComposeRecipient`

OR

.. api-header::
   :label: array of :ref:`compose.ComposeRecipient`

.. _compose.ComposeState:

ComposeState
------------

.. api-section-annotation-hack:: -- [Added in TB 90]

Represent the state of the message composer.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``canSendLater``
      :type: (boolean)
      
      The message can be send later.
   
   
   .. api-member::
      :name: ``canSendNow``
      :type: (boolean)
      
      The message can be send now.
   

.. _compose.CustomHeader:

CustomHeader
------------

.. api-section-annotation-hack:: 

A custom header definition.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      Name of a custom header, must have a :value:`X-` prefix.
   
   
   .. api-member::
      :name: ``value``
      :type: (string)
   

.. _compose.FileAttachment:

FileAttachment
--------------

.. api-section-annotation-hack:: 

Object used to add, update or rename an attachment in a message being composed.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``file``]
      :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__, optional)
      
      The new content for the attachment.
   
   
   .. api-member::
      :name: [``name``]
      :type: (string, optional)
      
      The new name for the attachment, as displayed to the user. If not specified, the name of the provided ``file`` object is used.
   
