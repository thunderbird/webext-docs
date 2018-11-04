========
messages
========
This is preliminary documentation for the messages API being developed in `bug 1488176`__.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1488176

The permission ``messagesRead`` is required to use ``messages``.

Functions
=========

list(folder)
------------

- ``folder`` (object)

  - ``accountId`` (string)
  - ``path`` (string)
  - [``name``] (string)

get(messageId)
--------------

- ``messageId`` (integer)

update(messageId, newProperties)
--------------------------------

- ``messageId`` (integer)
- ``newProperties`` (object)

  - [``flagged``] (boolean)
  - [``read``] (boolean)
  - [``tags``] (array)

listTags()
----------
