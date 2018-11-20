========
messages
========

This is preliminary documentation for the messages API being developed in `bug 1488176`__.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1488176

.. note::

  The permission ``messagesRead`` is required to use ``messages``.

Functions
=========

.. _messages.list:

list(folder)
------------

Lists all messages in the specified folder. WARNING: this could return a very large number of messages, which would negatively affect performance.

- ``folder`` (:ref:`accounts.MailFolder`)

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
