========
accounts
========
This is preliminary documentation for the accounts API being developed in `bug 1488176`__.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1488176

The permission ``accountsRead`` is required to use ``accounts``.

Types
=====

.. _MailFolder:

MailFolder
----------
A folder object, as returned by the ``list`` and ``get`` methods.

- ``accountId`` (string)
- ``path`` (string)
- [``name``] (string)

Functions
=========

list()
------
Returns all mail accounts.

get(accountId)
--------------
Returns details of the requested account, or null if it doesn't exist.

- ``accountId`` (string)

