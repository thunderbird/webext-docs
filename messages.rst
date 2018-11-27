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

Gets all messages in a folder. See :doc:`messageLists` for more information.

- ``folder`` (:ref:`accounts.MailFolder`)

.. _messages.continueList:

continueList(messageListId)
---------------------------

Returns the next chunk of messages in a list. See :doc:`messageLists` for more information.

- ``messageListId`` (string)

.. _messages.get:

get(messageId)
--------------

Returns a specified message.

- ``messageId`` (integer)

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
  - [``tags``] (array) Sets the tags on the message. For a list of available tags, call the listTags method.

.. _messages.listTags:

listTags()
----------

Returns a list of tags that can be set on messages, and their human-friendly name, colour, and sort order.
