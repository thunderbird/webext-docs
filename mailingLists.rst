============
mailingLists
============

The address books API, also including the :doc:`addressBooks` and :doc:`contacts` namespaces, first appeared in Thunderbird 64.

.. note::

  The permission ``addressBooks`` is required to use ``mailingLists``.

Types
=====

.. _mailingLists.MailingListNode:

MailingListNode
---------------

A node representing a mailing list.

- ``description`` (string)
- ``id`` (string) The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.
- ``name`` (string)
- ``nickName`` (string)
- ``type`` (:ref:`addressBooks.NodeType`) Always set to ``mailingList``.
- [``contacts``] (array) A list of contacts held by this node's address book or mailing list.
- [``parentId``] (string) The ``id`` of the parent object.
- [``readOnly``] (boolean) Indicates if the object is read-only. Currently this returns false in all cases, as read-only address books are ignored by the API.

Functions
=========

.. _mailingLists.list:

list(parentId)
--------------

Gets all the mailing lists in the address book with id ``parentId``.

- ``parentId`` (string)

.. _mailingLists.get:

get(id)
-------

Gets a single mailing list.

- ``id`` (string)

.. _mailingLists.create:

create(parentId, properties)
----------------------------

Creates a new mailing list in the address book with id ``parentId``.

- ``parentId`` (string)
- ``properties`` (object)

  - ``name`` (string)
  - [``description``] (string)
  - [``nickName``] (string)

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

.. _mailingLists.removeMember:

removeMember(id, contactId)
---------------------------

Removes a contact from the mailing list with id ``id``. This does not delete the contact from the address book.

- ``id`` (string)
- ``contactId`` (string)

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
