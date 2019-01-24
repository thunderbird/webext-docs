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

- ``folders`` (array of :ref:`accounts.MailFolder`) The folders for this account.
- ``id`` (string) A unique identifier for this account.
- ``name`` (string) The human-friendly name of this account.
- ``type`` (string) What sort of account this is, e.g. ``imap``, ``nntp``, or ``pop3``.

.. _accounts.MailFolder:

MailFolder
----------

A folder object, as returned by the ``list`` and ``get`` methods. Use the accountId and path properties to refer to a folder.

object

- ``accountId`` (string) The account this folder belongs to.
- ``path`` (string) Path to this folder in the account. Although paths look predictable, never guess a folder's path, as there are a number of reasons why it may not be what you think it is.
- [``name``] (string) The human-friendly name of this folder.
- [``type``] (`string <enum_type_9_>`_) The type of folder, for several common types.

.. _enum_type_9:

Values for type:

- ``inbox``
- ``drafts``
- ``sent``
- ``trash``
- ``templates``
- ``archives``
- ``junk``
- ``outbox``
