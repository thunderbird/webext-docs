========
contacts
========
The permission ``addressBooks`` is required to use ``contacts``.

Types
=====

ContactNode
-----------
A node representing a contact in an address book.

- ``id`` (string) The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.
- ``properties`` `ContactProperties`_
- ``type`` `NodeType`_ Always set to ``contact``.
- [``parentId``] (string) The ``id`` of the parent object.
- [``readOnly``] (boolean) Indicates if the object is read-only. Currently this returns false in all cases, as read-only address books are ignored by the API.

ContactProperties
-----------------
A set of properties for a particular contact. For a complete list of properties that Thunderbird uses, see https://hg.mozilla.org/comm-central/file/tip/mailnews/addrbook/public/nsIAbCard.idl

Functions
=========

list(parentId)
--------------
Gets all the contacts in the address book with the id ``parentId``.

- ``parentId`` (string)

get(id)
-------
Gets a single contact.

- ``id`` (string)

create(parentId, properties)
----------------------------
Adds a new contact to the address book with the id ``parentId``.

- ``parentId`` (string)
- ``properties`` `ContactProperties`_

update(id, properties)
----------------------
Edits the properties of a contact. To remove a property, specify it as ``null``.

- ``id`` (string)
- ``properties`` `ContactProperties`_

delete(id)
----------
Removes a contact from the address book. The contact is also removed from any mailing lists it is a member of.

- ``id`` (string)

