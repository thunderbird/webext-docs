========
contacts
========

The address books API, also including the :doc:`addressBooks` and :doc:`mailingLists` namespaces, first appeared in Thunderbird 64.
The quickSearch function was added in Thunderbird 68.

The `Address Books`__ sample extension uses this API.

__ https://github.com/thundernest/sample-extensions/tree/master/addressBooks

Permissions
===========

- addressBooks "Read and modify your address books and contacts"

.. note::

  The permission ``addressBooks`` is required to use ``contacts``.

Functions
=========

.. _contacts.list:

list(parentId)
--------------

Gets all the contacts in the address book with the id ``parentId``.

- ``parentId`` (string)

Returns a `Promise`_ fulfilled with:

- array of :ref:`contacts.ContactNode`

.. _contacts.quickSearch:

quickSearch([parentId], searchString)
-------------------------------------

Gets all contacts matching ``searchString`` in the address book with the id ``parentId``.

- [``parentId``] (string) The ID of the address book to search. If not specified, all address books are searched.
- ``searchString`` (string) One or more space-separated terms to search for.

Returns a `Promise`_ fulfilled with:

- array of :ref:`contacts.ContactNode`

.. _contacts.get:

get(id)
-------

Gets a single contact.

- ``id`` (string)

Returns a `Promise`_ fulfilled with:

- :ref:`contacts.ContactNode`

.. _contacts.create:

create(parentId, [id], properties)
----------------------------------

Adds a new contact to the address book with the id ``parentId``.

- ``parentId`` (string)
- [``id``] (string) Assigns the contact an id. If an existing contact has this id, an exception is thrown.
- ``properties`` (:ref:`contacts.ContactProperties`)

Returns a `Promise`_ fulfilled with:

- string The ID of the new contact.

.. _contacts.update:

update(id, properties)
----------------------

Edits the properties of a contact. To remove a property, specify it as ``null``.

- ``id`` (string)
- ``properties`` (:ref:`contacts.ContactProperties`)

.. _contacts.delete:

delete(id)
----------

Removes a contact from the address book. The contact is also removed from any mailing lists it is a member of.

- ``id`` (string)

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Events
======

.. _contacts.onCreated:

onCreated(node, id)
-------------------

Fired when a contact is created.

- ``node`` (:ref:`contacts.ContactNode`)
- ``id`` (string)

.. _contacts.onUpdated:

onUpdated(node)
---------------

Fired when a contact is changed.

- ``node`` (:ref:`contacts.ContactNode`)

.. _contacts.onDeleted:

onDeleted(parentId, id)
-----------------------

Fired when a contact is removed from an address book.

- ``parentId`` (string)
- ``id`` (string)

Types
=====

.. _contacts.ContactNode:

ContactNode
-----------

A node representing a contact in an address book.

object:

- ``id`` (string) The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.
- ``properties`` (:ref:`contacts.ContactProperties`)
- ``type`` (:ref:`addressBooks.NodeType`) Always set to ``contact``.
- [``parentId``] (string) The ``id`` of the parent object.
- [``readOnly``] (boolean) Indicates if the object is read-only. Currently this returns false in all cases, as read-only address books are ignored by the API.

.. _contacts.ContactProperties:

ContactProperties
-----------------

A set of properties for a particular contact. For a complete list of properties that Thunderbird uses, see https://hg.mozilla.org/comm-central/file/tip/mailnews/addrbook/public/nsIAbCard.idl

It is also possible to store custom properties. The custom property name however may only use a to z, A to Z, 1 to 9 and underscores.

object
