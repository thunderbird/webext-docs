=======
compose
=======

This message composition window API first appeared in Thunderbird 67 (see `bug 1503423`__).

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1503423

Permissions
===========

- compose "Read and modify your email messages as you compose and send them"

Functions
=========

.. _compose.beginNew:

beginNew([details])
-------------------

*Changed in Thunderbird 77: return value added*

- [``details``] (:ref:`compose.ComposeDetails`)

Returns a `Promise`_ fulfilled with:

- :ref:`tabs.Tab`

.. _compose.beginReply:

beginReply(messageId, [replyType], [details])
---------------------------------------------

*Changed in Thunderbird 77: return value added*

- ``messageId`` (integer) The message to reply to, as retrieved using other APIs.
- [``replyType``] (`string <enum_replyType_3_>`_)
- [``details``] (:ref:`compose.ComposeDetails`) *Added in Thunderbird 76*

Returns a `Promise`_ fulfilled with:

- :ref:`tabs.Tab`

.. _enum_replyType_3:

Values for replyType:

- ``replyToSender``
- ``replyToList``
- ``replyToAll``

.. _compose.beginForward:

beginForward(messageId, [forwardType], [details])
-------------------------------------------------

*Changed in Thunderbird 77: return value added*

- ``messageId`` (integer) The message to forward, as retrieved using other APIs.
- [``forwardType``] (`string <enum_forwardType_6_>`_)
- [``details``] (:ref:`compose.ComposeDetails`)

Returns a `Promise`_ fulfilled with:

- :ref:`tabs.Tab`

.. _enum_forwardType_6:

Values for forwardType:

- ``forwardInline``
- ``forwardAsAttachment``

.. _compose.getComposeDetails:

getComposeDetails(tabId)
------------------------

*Added in Thunderbird 74*

Fetches the current state of a compose window. Currently only a limited amount of information is available, more will be added in later versions.

- ``tabId`` (integer)

Returns a `Promise`_ fulfilled with:

- :ref:`compose.ComposeDetails`

.. note::

  The permission ``compose`` is required to use ``getComposeDetails``.

.. _compose.setComposeDetails:

setComposeDetails(tabId, details)
---------------------------------

*Added in Thunderbird 74*

Updates the compose window. Specify only fields that you want to change. Currently only the to/cc/bcc/replyTo/followupTo/newsgroups fields and the subject are implemented.

- ``tabId`` (integer)
- ``details`` (:ref:`compose.ComposeDetails`)

.. note::

  The permission ``compose`` is required to use ``setComposeDetails``.

.. _compose.listAttachments:

listAttachments(tabId)
----------------------

*Added in Thunderbird 78*

Lists all of the attachments of the message being composed in the specified tab.

- ``tabId`` (integer)

.. _compose.addAttachment:

addAttachment(tabId, data)
--------------------------

*Added in Thunderbird 78*

Adds an attachment to the message being composed in the specified tab.

- ``tabId`` (integer)
- ``data`` (object)

  - ``file`` (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`_)
  - [``name``] (string) The name, as displayed to the user, of this attachment. If not specified, the name of the ``file`` object is used.

.. _compose.updateAttachment:

updateAttachment(tabId, attachmentId, data)
-------------------------------------------

*Added in Thunderbird 78*

Renames and/or replaces the contents of an attachment to the message being composed in the specified tab.

- ``tabId`` (integer)
- ``attachmentId`` (integer)
- ``data`` (object)

  - [``file``] (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`_)
  - [``name``] (string) The name, as displayed to the user, of this attachment. If not specified, the name of the ``file`` object is used.

.. _compose.removeAttachment:

removeAttachment(tabId, attachmentId)
-------------------------------------

*Added in Thunderbird 78*

Removes an attachment from the message being composed in the specified tab.

- ``tabId`` (integer)
- ``attachmentId`` (integer)

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Events
======

.. _compose.onBeforeSend:

onBeforeSend(tab, details)
--------------------------

*Added in Thunderbird 74*

Fired when a message is about to be sent from the compose window.

- ``tab`` (:ref:`tabs.Tab`) *Added in Thunderbird 74.0b2*
- ``details`` (:ref:`compose.ComposeDetails`) The current state of the compose window. This is functionally the same as the :ref:`compose.getComposeDetails` function.

Event listeners should return:

- object

  - [``cancel``] (boolean) Cancels the send.
  - [``details``] (:ref:`compose.ComposeDetails`) Updates the compose window. See the :ref:`compose.setComposeDetails` function for more information.

.. note::

  The permission ``compose`` is required to use ``onBeforeSend``.

.. _compose.onAttachmentAdded:

onAttachmentAdded(tab, attachment)
----------------------------------

*Added in Thunderbird 78*

Fired when an attachment is added to a message being composed.

- ``tab`` (:ref:`tabs.Tab`)
- ``attachment`` (:ref:`compose.ComposeAttachment`)

.. _compose.onAttachmentRemoved:

onAttachmentRemoved(tab, attachmentId)
--------------------------------------

*Added in Thunderbird 78*

Fired when an attachment is removed from a message being composed.

- ``tab`` (:ref:`tabs.Tab`)
- ``attachmentId`` (integer)

.. _compose.onIdentityChanged:

onIdentityChanged(tab, identityId)
----------------------------------

*Added in Thunderbird 78.0b2*

Fired when the user changes the identity that will be used to send a message being composed.

- ``tab`` (:ref:`tabs.Tab`)
- ``identityId`` (string)

.. note::

  The permission ``accountsRead`` is required to use ``onIdentityChanged``.

Types
=====

.. _compose.ComposeAttachment:

ComposeAttachment
-----------------

*Added in Thunderbird 78*

Represents an attachment in a message being composed.

object:

- ``id`` (integer) A unique identifier for this attachment.
- ``name`` (string) The name, as displayed to the user, of this attachment. This is usually but not always the filename of the attached file.
- ``size`` (integer) The size in bytes of this attachment. *Added in Thunderbird 83, backported to 78.5.0*
- ``getFile()`` Retrieves the contents of the attachment as a DOM ``File`` object.

.. _compose.ComposeDetails:

ComposeDetails
--------------

Used by various functions to represent the state of a message being composed. Note that functions using this type may have a partial implementation.

object:

- [``attachments``] (array of object) Attachments to add to the message. Only used in the begin* functions. *Added in Thunderbird 82, backported to 78.4*
- [``bcc``] (:ref:`compose.ComposeRecipientList`)
- [``body``] (string)
- [``cc``] (:ref:`compose.ComposeRecipientList`)
- [``followupTo``] (:ref:`compose.ComposeRecipientList`) *Added in Thunderbird 74*
- [``identityId``] (string) The ID of an identity from the :doc:`accounts` API. The settings from the identity will be used in the composed message. If ``replyTo`` is also specified, the ``replyTo`` property of the identity is overridden. The permission ``accountsRead`` is required to include the ``identityId``. *Added in Thunderbird 76*
- [``isPlainText``] (boolean) *Added in Thunderbird 75*
- [``newsgroups``] (string or array of string) *Added in Thunderbird 74*
- [``plainTextBody``] (string) *Added in Thunderbird 75*
- [``replyTo``] (:ref:`compose.ComposeRecipientList`)
- [``subject``] (string)
- [``to``] (:ref:`compose.ComposeRecipientList`)

.. _compose.ComposeRecipient:

ComposeRecipient
----------------

string: A name and email address in the format "Name <email@example.com>", or just an email address.

OR

object: 

  - ``id`` (string) The ID of a contact or mailing list from the :doc:`contacts` and :doc:`mailingLists` APIs.
  - ``type`` (`string <enum_type_41_>`_) Which sort of object this ID is for.

.. _enum_type_41:

Values for type:

- ``contact``
- ``mailingList``

.. _compose.ComposeRecipientList:

ComposeRecipientList
--------------------

*Added in Thunderbird 74*

string: A name and email address in the format "Name <email@example.com>", or just an email address.

OR

array of :ref:`compose.ComposeRecipient`: 
