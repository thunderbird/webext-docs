========
accounts
========

This is preliminary documentation for the accounts API being developed in `bug 1488176`__.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1488176

Permissions
===========

- accountsRead

.. note::

  The permission ``accountsRead`` is required to use ``accounts``.

Functions
=========

.. _accounts.list:

list()
------

Returns all mail accounts.

.. _accounts.get:

get(accountId)
--------------

Returns details of the requested account, or null if it doesn't exist.

- ``accountId`` (string)

Types
=====

.. _accounts.MailFolder:

MailFolder
----------

A folder object, as returned by the ``list`` and ``get`` methods.

- ``accountId`` (string)
- ``path`` (string)
- [``name``] (string)
