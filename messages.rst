========
messages
========

The messages API first appeared in Thunderbird 66 (see `bug 1488176`__).

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1488176

Permissions
===========

- messagesMove "Move, copy, or delete your email messages"
- messagesRead "Read your email messages and mark or tag them"

.. note::

  The permission ``messagesRead`` is required to use ``messages``.

Functions
=========

.. _messages.list:

list(folder)
------------

Gets all messages in a folder.

- ``folder`` (:ref:`accounts.MailFolder`)

Returns a `Promise`_ fulfilled with:

- :ref:`messages.MessageList`

.. _messages.continueList:

continueList(messageListId)
---------------------------

Returns the next chunk of messages in a list. See :doc:`how-to/messageLists` for more information.

- ``messageListId`` (string)

Returns a `Promise`_ fulfilled with:

- :ref:`messages.MessageList`

.. _messages.get:

get(messageId)
--------------

Returns a specified message.

- ``messageId`` (integer)

Returns a `Promise`_ fulfilled with:

- :ref:`messages.MessageHeader`

.. _messages.getFull:

getFull(messageId)
------------------

Returns a specified message, including all headers and MIME parts.

- ``messageId`` (integer)

Returns a `Promise`_ fulfilled with:

- :ref:`messages.MessagePart`

.. _messages.update:

update(messageId, newProperties)
--------------------------------

Marks or unmarks a message as read, starred, or tagged.

- ``messageId`` (integer)
- ``newProperties`` (object)

  - [``flagged``] (boolean) Marks the message as starred or unstarred.
  - [``read``] (boolean) Marks the message as read or unread.
  - [``tags``] (array of string) Sets the tags on the message. For a list of available tags, call the listTags method.

.. _messages.move:

move(messageIds, destination)
-----------------------------

Moves messages to a specified folder.

- ``messageIds`` (array of integer) The IDs of the messages to move.
- ``destination`` (:ref:`accounts.MailFolder`) The folder to move the messages to.

.. note::

  The permission ``messagesMove`` is required to use ``move``.

.. _messages.copy:

copy(messageIds, destination)
-----------------------------

Copies messages to a specified folder.

- ``messageIds`` (array of integer) The IDs of the messages to copy.
- ``destination`` (:ref:`accounts.MailFolder`) The folder to copy the messages to.

.. note::

  The permission ``messagesMove`` is required to use ``copy``.

.. _messages.delete:

delete(messageIds, [skipTrash])
-------------------------------

Deletes messages, or moves them to the trash folder.

- ``messageIds`` (array of integer) The IDs of the messages to delete.
- [``skipTrash``] (boolean) If true, the message will be permanently deleted without warning the user. If false or not specified, it will be moved to the trash folder.

.. note::

  The permission ``messagesMove`` is required to use ``delete``.

.. _messages.listTags:

listTags()
----------

Returns a list of tags that can be set on messages, and their human-friendly name, colour, and sort order.

Returns a `Promise`_ fulfilled with:

- array of :ref:`messages.MessageTag`

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Types
=====

.. _messages.MessageHeader:

MessageHeader
-------------

object

- ``author`` (string)
- ``bccList`` (array of string)
- ``ccList`` (array of string)
- ``date`` (date)
- ``flagged`` (boolean)
- ``folder`` (:ref:`accounts.MailFolder`)
- ``id`` (integer)
- ``read`` (boolean)
- ``recipients`` (array of string)
- ``subject`` (string)
- ``tags`` (array of string)

.. _messages.MessageList:

MessageList
-----------

See :doc:`how-to/messageLists` for more information.

object

- ``id`` (string)
- ``messages`` (array of :ref:`messages.MessageHeader`)

.. _messages.MessagePart:

MessagePart
-----------

Represents an email message "part", which could be the whole message

object

- [``body``] (string) The content of the part
- [``contentType``] (string)
- [``headers``] (object) An object of part headers, with the header name as key, and an array of header values as value
- [``name``] (string) Name of the part, if it is a file
- [``partName``] (string)
- [``parts``] (array of :ref:`messages.MessagePart`) Any sub-parts of this part
- [``size``] (integer)

.. _messages.MessageTag:

MessageTag
----------

object

- ``color`` (string) Tag color
- ``key`` (string) Distinct tag identifier – use this string when referring to a tag
- ``ordinal`` (string) Custom sort string (usually empty)
- ``tag`` (string) Human-readable tag name
