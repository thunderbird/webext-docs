========
accounts
========

The accounts API first appeared in Thunderbird 66 (see `bug 1488176`__).

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1488176

Permissions
===========

- accountsRead "See your mail accounts and their folders"

.. note::

  The permission ``accountsRead`` is required to use ``accounts``.

Functions
=========

.. _accounts.list:

list()
------

Returns all mail accounts.

Returns a `Promise`_ fulfilled with:

- array of :ref:`accounts.MailAccount`

.. _accounts.get:

get(accountId)
--------------

Returns details of the requested account, or null if it doesn't exist.

- ``accountId`` (string)

Returns a `Promise`_ fulfilled with:

- :ref:`accounts.MailAccount`

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Types
=====

.. _accounts.MailAccount:

MailAccount
-----------

object

- ``folders`` (array of :ref:`folders.MailFolder`) The folders for this account.
- ``id`` (string) A unique identifier for this account.
- ``name`` (string) The human-friendly name of this account.
- ``type`` (string) What sort of account this is, e.g. ``imap``, ``nntp``, or ``pop3``.
