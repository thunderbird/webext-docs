.. _compose_api:

=======
compose
=======

This message composition window API first appeared in Thunderbird 67 (see `bug 1503423`__).

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1503423

.. role:: permission

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

Open a new message compose window. If the provided ComposeDetails object does not provide ``body``, ``plainTextBody`` or ``isPlainText``, the default compose format of the used/default identity is used. The :ref:`accounts_api` API can be used to get the used/default identity and its default compose format.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``messageId``]
      :type: (integer)
      :annotation: -- [Added in TB 84, backported to TB 78.7.0]
      
      If specified, the message or template to edit as a new message.
   
   
   .. api-member::
      :name: [``details``]
      :type: (:ref:`compose.ComposeDetails`)
   

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

Open a new message compose window replying to a given message. If the provided ComposeDetails object does not provide ``body``, ``plainTextBody`` or ``isPlainText``, the default compose format of the used/default identity is used. The :ref:`accounts_api` API can be used to get the used/default identity and its default compose format.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
      
      The message to reply to, as retrieved using other APIs.
   
   
   .. api-member::
      :name: [``replyType``]
      :type: (`string`)
      
      Supported values:
      
      .. api-member::
         :name: ``replyToSender``
      
      .. api-member::
         :name: ``replyToList``
      
      .. api-member::
         :name: ``replyToAll``
   
   
   .. api-member::
      :name: [``details``]
      :type: (:ref:`compose.ComposeDetails`)
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

Open a new message compose window forwarding a given message. If the provided ComposeDetails object does not provide ``body``, ``plainTextBody`` or ``isPlainText``, the default compose format of the used/default identity is used. The :ref:`accounts_api` API can be used to get the used/default identity and its default compose format.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
      
      The message to forward, as retrieved using other APIs.
   
   
   .. api-member::
      :name: [``forwardType``]
      :type: (`string`)
      
      Supported values:
      
      .. api-member::
         :name: ``forwardInline``
      
      .. api-member::
         :name: ``forwardAsAttachment``
   
   
   .. api-member::
      :name: [``details``]
      :type: (:ref:`compose.ComposeDetails`)
   

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
         :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`_)
      
      
      .. api-member::
         :name: [``name``]
         :type: (string)
         
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
         :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`_)
      
      
      .. api-member::
         :name: [``name``]
         :type: (string)
         
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
      :type: (object)
      
      .. api-member::
         :name: ``mode``
         :type: (`string`)
         
         Supported values:
         
         .. api-member::
            :name: ``default``
         
         .. api-member::
            :name: ``sendNow``
         
         .. api-member::
            :name: ``sendLater``
      
   

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

onBeforeSend(tab, details)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 74]

Fired when a message is about to be sent from the compose window. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Added in TB 74.0b2]
   
   
   .. api-member::
      :name: ``details``
      :type: (:ref:`compose.ComposeDetails`)
      
      The current state of the compose window. This is functionally the same as the :ref:`compose.getComposeDetails` function.
   

.. api-header::
   :label: Expected return value of event listeners

   
   .. api-member::
      :type: object
      
      .. api-member::
         :name: [``cancel``]
         :type: (boolean)
         
         Cancels the send.
      
      
      .. api-member::
         :name: [``details``]
         :type: (:ref:`compose.ComposeDetails`)
         
         Updates the compose window. See the :ref:`compose.setComposeDetails` function for more information.
      
   

.. api-header::
   :label: Required permissions

   - :permission:`compose`

.. _compose.onAttachmentAdded:

onAttachmentAdded(tab, attachment)
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Fired when an attachment is added to a message being composed.

.. api-header::
   :label: Parameters for event listeners

   
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

onAttachmentRemoved(tab, attachmentId)
--------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 78]

Fired when an attachment is removed from a message being composed.

.. api-header::
   :label: Parameters for event listeners

   
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

onIdentityChanged(tab, identityId)
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 78.0b2]

Fired when the user changes the identity that will be used to send a message being composed.

.. api-header::
   :label: Parameters for event listeners

   
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

onComposeStateChanged(tab, state)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 90]

Fired when the state of the message composer changed.

.. api-header::
   :label: Parameters for event listeners

   
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
      :name: ``name``
      :type: (string)
      
      The name, as displayed to the user, of this attachment. This is usually but not always the filename of the attached file.
   
   
   .. api-member::
      :name: ``size``
      :type: (integer)
      :annotation: -- [Added in TB 83, backported to TB 78.5.0]
      
      The size in bytes of this attachment.
   
   - ``getFile()`` Retrieves the contents of the attachment as a DOM ``File`` object.

.. _compose.ComposeDetails:

ComposeDetails
--------------

.. api-section-annotation-hack:: 

Used by various functions to represent the state of a message being composed. Note that functions using this type may have a partial implementation.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``attachments``]
      :type: (array of object)
      :annotation: -- [Added in TB 82, backported to TB 78.4.0]
      
      Attachments to add to the message. Only used in the begin* functions.
   
   
   .. api-member::
      :name: [``bcc``]
      :type: (:ref:`compose.ComposeRecipientList`)
   
   
   .. api-member::
      :name: [``body``]
      :type: (string)
   
   
   .. api-member::
      :name: [``cc``]
      :type: (:ref:`compose.ComposeRecipientList`)
   
   
   .. api-member::
      :name: [``followupTo``]
      :type: (:ref:`compose.ComposeRecipientList`)
      :annotation: -- [Added in TB 74]
   
   
   .. api-member::
      :name: [``from``]
      :type: (:ref:`compose.ComposeRecipient`)
      :annotation: -- [Added in TB 88]
      
      *Caution*: Setting a value for `from` does not change the used identity, it overrides the FROM header. Many email servers do not accept emails where the FROM header does not match the sender identity. Must be set to exactly one valid email address.
   
   
   .. api-member::
      :name: [``identityId``]
      :type: (string)
      :annotation: -- [Added in TB 76]
      
      The ID of an identity from the :doc:`accounts` API. The settings from the identity will be used in the composed message. If ``replyTo`` is also specified, the ``replyTo`` property of the identity is overridden. The permission :permission:`accountsRead` is required to include the ``identityId``.
   
   
   .. api-member::
      :name: [``isPlainText``]
      :type: (boolean)
      :annotation: -- [Added in TB 75]
   
   
   .. api-member::
      :name: [``newsgroups``]
      :type: (string or array of string)
      :annotation: -- [Added in TB 74]
   
   
   .. api-member::
      :name: [``plainTextBody``]
      :type: (string)
      :annotation: -- [Added in TB 75]
   
   
   .. api-member::
      :name: [``replyTo``]
      :type: (:ref:`compose.ComposeRecipientList`)
   
   
   .. api-member::
      :name: [``subject``]
      :type: (string)
   
   
   .. api-member::
      :name: [``to``]
      :type: (:ref:`compose.ComposeRecipientList`)
   
   
   .. api-member::
      :name: [``type``]
      :type: (`string`)
      :annotation: -- [Added in TB 88]
      
      Read-only. The type of the message being composed, depending on how the compose window was opened by the user.
      
      Supported values:
      
      .. api-member::
         :name: ``draft``
      
      .. api-member::
         :name: ``new``
      
      .. api-member::
         :name: ``redirect``
         :annotation: -- [Added in TB 90]
      
      .. api-member::
         :name: ``reply``
      
      .. api-member::
         :name: ``forward``
   

.. _compose.ComposeRecipient:

ComposeRecipient
----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         A name and email address in the format "Name <email@example.com>", or just an email address.
   

OR

.. api-header::
   :label: object

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         .. api-member::
            :name: ``id``
            :type: (string)
            
            The ID of a contact or mailing list from the :doc:`contacts` and :doc:`mailingLists` APIs.
         
         
         .. api-member::
            :name: ``type``
            :type: (`string`)
            
            Which sort of object this ID is for.
            
            Supported values:
            
            .. api-member::
               :name: ``contact``
            
            .. api-member::
               :name: ``mailingList``
         
   

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
   
