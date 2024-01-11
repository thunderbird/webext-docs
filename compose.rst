.. _compose_api:

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
   :name: :permission:`compose.send`

   Send composed email messages on your behalf

.. rst-class:: api-main-section

Functions
=========

.. _compose.beginNew:

beginNew([messageId], [details])
--------------------------------

.. api-section-annotation-hack:: 

Open a new message compose window. If the provided ComposeDetails object does not provide ``body``, ``plainTextBody`` or ``isPlainText``, the default compose format of the used/default identity is used. The :ref:`accounts_api` can be used to get the used/default identity and its default compose format.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``messageId``]
      :type: (integer, optional)
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

Open a new message compose window replying to a given message. If the provided ComposeDetails object does not provide ``body``, ``plainTextBody`` or ``isPlainText``, the default compose format of the used/default identity is used. The :ref:`accounts_api` can be used to get the used/default identity and its default compose format.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
      
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

.. _compose.beginForward:

beginForward(messageId, [forwardType], [details])
-------------------------------------------------

.. api-section-annotation-hack:: 

Open a new message compose window forwarding a given message. If the provided ComposeDetails object does not provide ``body``, ``plainTextBody`` or ``isPlainText``, the default compose format of the used/default identity is used. The :ref:`accounts_api` can be used to get the used/default identity and its default compose format.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
      
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

.. _compose.setComposeDetails:

setComposeDetails(tabId, details)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 74]

Updates the compose window. Specify only fields that you want to change. Currently only the to/cc/bcc/replyTo/followupTo/newsgroups fields and the subject are implemented. It is not possible to change the compose format.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``details``
      :type: (:ref:`compose.ComposeDetails`)
      
      The compose format of an already opened compose window cannot be changed. Setting ``details.body``, ``details.plainTextBody`` or ``details.isPlaintext`` will fail if the compose format of the compose window does not match. Use :ref:`compose.getComposeDetails` to get the current compose format.
   

.. api-header::
   :label: Required permissions

   - :permission:`compose`

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

.. _compose.addAttachment:

addAttachment(tabId, data)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Adds an attachment to the message being composed in the specified tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``data``
      :type: (object)
      
      .. api-member::
         :name: ``file``
         :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__)
      
      
      .. api-member::
         :name: [``name``]
         :type: (string, optional)
         
         The name, as displayed to the user, of this attachment. If not specified, the name of the ``file`` object is used.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`compose.ComposeAttachment`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.updateAttachment:

updateAttachment(tabId, attachmentId, data)
-------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Renames and/or replaces the contents of an attachment to the message being composed in the specified tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``attachmentId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``data``
      :type: (object)
      
      .. api-member::
         :name: [``file``]
         :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__, optional)
      
      
      .. api-member::
         :name: [``name``]
         :type: (string, optional)
         
         The name, as displayed to the user, of this attachment. If not specified, the name of the ``file`` object is used.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`compose.ComposeAttachment`
   
   
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

.. _compose.sendMessage:

sendMessage(tabId, [options])
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 90]

Sends the message currently being composed.

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
      :type: boolean
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`compose.send`

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

.. rst-class:: api-main-section

Events
======

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
   
   - ``getFile()`` Retrieves the contents of the attachment as a `File <https://developer.mozilla.org/docs/Web/API/File>`__ object.

.. _compose.ComposeDetails:

ComposeDetails
--------------

.. api-section-annotation-hack:: 

Used by various functions to represent the state of a message being composed. Note that functions using this type may have a partial implementation.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``attachments``]
      :type: (array of object, optional)
      :annotation: -- [Added in TB 82, backported to TB 78.4.0]
      
      Attachments to add to the message. Only used in the begin* functions.
   
   
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
   
   
   .. api-member::
      :name: [``plainTextBody``]
      :type: (string, optional)
      :annotation: -- [Added in TB 75]
      
      The plain text content of the message.
   
   
   .. api-member::
      :name: [``relatedMessageId``]
      :type: (integer, optional)
      :annotation: -- [Added in TB 95, backported to TB 91.3.1]
      
      The id of the original message (in case of draft, template, forward or reply). Read-only. Is :value:`null` in all other cases or if the original message was opened from file.
   
   
   .. api-member::
      :name: [``replyTo``]
      :type: (:ref:`compose.ComposeRecipientList`, optional)
   
   
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
   
