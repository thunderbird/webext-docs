========
messages
========

This is preliminary documentation for the messages API being developed in `bug 1488176`__.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1488176

Permissions
===========

- messagesRead

.. note::

  The permission ``messagesRead`` is required to use ``messages``.

Functions
=========

.. _messages.list:

list(folder)
------------

Gets all messages in a folder.

- ``folder`` (:ref:`accounts.MailFolder`)

Returns:

- :ref:`messages.MessageList`

.. _messages.continueList:

continueList(messageListId)
---------------------------

Returns the next chunk of messages in a list. See :doc:`how-to/messageLists` for more information.

- ``messageListId`` (string)

Returns:

- :ref:`messages.MessageList`

.. _messages.get:

get(messageId)
--------------

Returns a specified message.

- ``messageId`` (integer)

Returns:

- :ref:`messages.MessageHeader`

.. _messages.getFull:

getFull(messageId)
------------------

Returns a specified message.

- ``messageId`` (integer)

.. _messages.update:

update(messageId, newProperties)
--------------------------------

Marks or unmarks a message as read, starred, or tagged.

- ``messageId`` (integer)
- ``newProperties`` (object)

  - [``flagged``] (boolean) Marks the message as starred or unstarred.
  - [``read``] (boolean) Marks the message as read or unread.
  - [``tags``] (array of string) Sets the tags on the message. For a list of available tags, call the listTags method.

.. _messages.listTags:

listTags()
----------

Returns a list of tags that can be set on messages, and their human-friendly name, colour, and sort order.

Returns:

- array of :ref:`messages.MessageTag`

Types
=====

.. _messages.MessageHeader:

MessageHeader
-------------

- ``author`` (string)
- ``bccList`` (string)
- ``ccList`` (string)
- ``date`` (date)
- ``flagged`` (boolean)
- ``folder`` (:ref:`accounts.MailFolder`)
- ``messageId`` (integer)
- ``read`` (boolean)
- ``recipients`` (string)
- ``subject`` (string)
- ``tags`` (array of string)

.. _messages.MessageList:

MessageList
-----------

See :doc:`how-to/messageLists` for more information.

- ``id`` (string)
- ``messages`` (array of :ref:`messages.MessageHeader`)

.. _messages.MessageTag:

MessageTag
----------

- ``color`` (string)
- ``key`` (string)
- ``ordinal`` (string)
- ``tag`` (string)
