=======
compose
=======

This is preliminary documentation for the message composition window API being developed in `bug 1503423`__.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1503423

Functions
=========

.. _compose.beginNew:

beginNew([details])
-------------------

- [``details``] (:ref:`compose.ComposeParams`)

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
- [``details``] (:ref:`compose.ComposeParams`)

.. _enum_forwardType_5:

Values for forwardType:

- ``forwardInline``
- ``forwardAsAttachment``

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Types
=====

.. _compose.ComposeParams:

ComposeParams
-------------

object

- [``bcc``] (array of :ref:`compose.ComposeRecipient`)
- [``body``] (string)
- [``cc``] (array of :ref:`compose.ComposeRecipient`)
- [``replyTo``] (string)
- [``subject``] (string)
- [``to``] (array of :ref:`compose.ComposeRecipient`)

.. _compose.ComposeRecipient:

ComposeRecipient
----------------

string: A name and email address in the format "Name <email@example.com>", or just an email address.

OR

object: 

  - ``id`` (string) The ID of a contact or mailing list from the :doc:`contacts` and :doc:`mailingLists` APIs.
  - ``type`` (`string <enum_type_14_>`_) Which sort of object this ID is for.

.. _enum_type_14:

Values for type:

- ``contact``
- ``mailingList``
