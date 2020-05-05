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

.. _accounts.setDefaultIdentity:

setDefaultIdentity(accountId, identityId)
-----------------------------------------

*Added in Thunderbird 76*

Sets the default identity for an account.

- ``accountId`` (string)
- ``identityId`` (string)

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Types
=====

.. _accounts.MailAccount:

MailAccount
-----------

object:

- ``folders`` (array of :ref:`folders.MailFolder`) The folders for this account.
- ``id`` (string) A unique identifier for this account.
- ``identities`` (array of :ref:`accounts.MailIdentity`) The identities associated with this account. The default identity is listed first, others in no particular order. *Added in Thunderbird 76*
- ``name`` (string) The human-friendly name of this account.
- ``type`` (string) What sort of account this is, e.g. ``imap``, ``nntp``, or ``pop3``.

.. _accounts.MailIdentity:

MailIdentity
------------

*Added in Thunderbird 76*

object:

- ``accountId`` (string) The id of the :ref:`accounts.MailAccount` this identity belongs to.
- ``email`` (string) The user's email address as used when messages are sent from this identity.
- ``id`` (string) A unique identifier for this identity.
- ``label`` (string) A user-defined label for this identity.
- ``name`` (string) The user's name as used when messages are sent from this identity.
- ``organization`` (string) The organization associated with this identity.
- ``replyTo`` (string) The reply-to email address associated with this identity.
