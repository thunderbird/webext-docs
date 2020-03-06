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

- [``details``] (:ref:`compose.ComposeDetails`)

.. _compose.beginReply:

beginReply(messageId, [replyType])
----------------------------------

- ``messageId`` (integer) The message to reply to, as retrieved using other APIs.
- [``replyType``] (`string <enum_replyType_3_>`_)

.. _enum_replyType_3:

Values for replyType:

- ``replyToSender``
- ``replyToList``
- ``replyToAll``

.. _compose.beginForward:

beginForward(messageId, [forwardType], [details])
-------------------------------------------------

- ``messageId`` (integer) The message to forward, as retrieved using other APIs.
- [``forwardType``] (`string <enum_forwardType_5_>`_)
- [``details``] (:ref:`compose.ComposeDetails`)

.. _enum_forwardType_5:

Values for forwardType:

- ``forwardInline``
- ``forwardAsAttachment``

.. _compose.getComposeDetails:

getComposeDetails(tabId)
------------------------

Fetches the current state of a compose window. Currently only a limited amount of information is available, more will be added in later versions.

- ``tabId`` (integer)

.. note::

  The permission ``compose`` is required to use ``getComposeDetails``.

.. _compose.setComposeDetails:

setComposeDetails(tabId, details)
---------------------------------

Updates the compose window. Specify only fields that you want to change. Currently only the to/cc/bcc/replyTo/followupTo/newsgroups fields and the subject are implemented.

- ``tabId`` (integer)
- ``details`` (:ref:`compose.ComposeDetails`)

.. note::

  The permission ``compose`` is required to use ``setComposeDetails``.

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Events
======

.. _compose.onBeforeSend:

onBeforeSend(tab, details)
--------------------------

Fired when a message is about to be sent from the compose window.

- ``tab`` (:ref:`tabs.Tab`) *Added in Thunderbird 74.0b2*
- ``details`` (:ref:`compose.ComposeDetails`) The current state of the compose window. This is functionally the same as the :ref:`compose.getComposeDetails` function.

Event listeners should return:

- object

  - [``cancel``] (boolean) Cancels the send.
  - [``details``] (:ref:`compose.ComposeDetails`) Updates the compose window. See the :ref:`compose.setComposeDetails` function for more information.

.. note::

  The permission ``compose`` is required to use ``onBeforeSend``.

Types
=====

.. _compose.ComposeDetails:

ComposeDetails
--------------

Used by various functions to represent the state of a message being composed. Note that functions using this type may have a partial implementation.

object

- [``bcc``] (:ref:`compose.ComposeRecipientList`)
- [``body``] (string)
- [``cc``] (:ref:`compose.ComposeRecipientList`)
- [``followupTo``] (:ref:`compose.ComposeRecipientList`)
- [``newsgroups``] (string or array of string)
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
  - ``type`` (`string <enum_type_21_>`_) Which sort of object this ID is for.

.. _enum_type_21:

Values for type:

- ``contact``
- ``mailingList``

.. _compose.ComposeRecipientList:

ComposeRecipientList
--------------------

string: A name and email address in the format "Name <email@example.com>", or just an email address.

OR

array of :ref:`compose.ComposeRecipient`: 
