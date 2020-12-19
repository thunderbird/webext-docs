============
mailingLists
============

The address books API, also including the :doc:`addressBooks` and :doc:`contacts` namespaces, first appeared in Thunderbird 64.

The `Address Books`__ sample extension uses this API.

__ https://github.com/thundernest/sample-extensions/tree/master/addressBooks

Permissions
===========

- addressBooks "Read and modify your address books and contacts"

.. note::

  The permission ``addressBooks`` is required to use ``mailingLists``.

Functions
=========

.. _mailingLists.list:

list(parentId)
--------------

Gets all the mailing lists in the address book with id ``parentId``.

- ``parentId`` (string)

Returns a `Promise`_ fulfilled with:

- array of :ref:`mailingLists.MailingListNode`

.. _mailingLists.get:

get(id)
-------

Gets a single mailing list.

- ``id`` (string)

Returns a `Promise`_ fulfilled with:

- :ref:`mailingLists.MailingListNode`

.. _mailingLists.create:

create(parentId, properties)
----------------------------

Creates a new mailing list in the address book with id ``parentId``.

- ``parentId`` (string)
- ``properties`` (object)

  - ``name`` (string)
  - [``description``] (string)
  - [``nickName``] (string)

Returns a `Promise`_ fulfilled with:

- string The ID of the new mailing list.

.. _mailingLists.update:

update(id, properties)
----------------------

Edits the properties of a mailing list.

- ``id`` (string)
- ``properties`` (object)

  - ``name`` (string)
  - [``description``] (string)
  - [``nickName``] (string)

.. _mailingLists.delete:

delete(id)
----------

Removes the mailing list.

- ``id`` (string)

.. _mailingLists.addMember:

addMember(id, contactId)
------------------------

Adds a contact to the mailing list with id ``id``. If the contact and mailing list are in different address books, the contact will also be copied to the list's address book.

- ``id`` (string)
- ``contactId`` (string)

.. _mailingLists.listMembers:

listMembers(id)
---------------

Gets all contacts that are members of the mailing list with id ``id``.

- ``id`` (string)

Returns a `Promise`_ fulfilled with:

- array of :ref:`contacts.ContactNode`

.. _mailingLists.removeMember:

removeMember(id, contactId)
---------------------------

Removes a contact from the mailing list with id ``id``. This does not delete the contact from the address book.

- ``id`` (string)
- ``contactId`` (string)

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Events
======

.. _mailingLists.onCreated:

onCreated(node)
---------------

Fired when a mailing list is created.

- ``node`` (:ref:`mailingLists.MailingListNode`)

.. _mailingLists.onUpdated:

onUpdated(node)
---------------

Fired when a mailing list is changed.

- ``node`` (:ref:`mailingLists.MailingListNode`)

.. _mailingLists.onDeleted:

onDeleted(parentId, id)
-----------------------

Fired when a mailing list is deleted.

- ``parentId`` (string)
- ``id`` (string)

.. _mailingLists.onMemberAdded:

onMemberAdded(node)
-------------------

Fired when a contact is added to the mailing list.

- ``node`` (:ref:`contacts.ContactNode`)

.. _mailingLists.onMemberRemoved:

onMemberRemoved(parentId, id)
-----------------------------

Fired when a contact is removed from the mailing list.

- ``parentId`` (string)
- ``id`` (string)

Types
=====

.. _mailingLists.MailingListNode:

MailingListNode
---------------

A node representing a mailing list.

object

- ``description`` (string)
- ``id`` (string) The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.
- ``name`` (string)
- ``nickName`` (string)
- ``type`` (:ref:`addressBooks.NodeType`) Always set to ``mailingList``.
- [``contacts``] (array of :ref:`contacts.ContactNode`) A list of contacts held by this node's address book or mailing list.
- [``parentId``] (string) The ``id`` of the parent object.
- [``readOnly``] (boolean) Indicates if the object is read-only. Currently this returns false in all cases, as read-only address books are ignored by the API.
