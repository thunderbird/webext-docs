========
messages
========
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
