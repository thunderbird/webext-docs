============
mailingLists
============
The permission ``addressBooks`` is required to use ``mailingLists``.

Types
=====

MailingListNode
---------------
A node representing a mailing list.

- ``description`` (string)
- ``id`` (string) The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.
- ``name`` (string)
- ``nickName`` (string)
- ``type`` `NodeType`_ Always set to ``mailingList``.
- [``contacts``] (array) A list of contacts held by this node's address book or mailing list.
- [``parentId``] (string) The ``id`` of the parent object.
- [``readOnly``] (boolean) Indicates if the object is read-only. Currently this returns false in all cases, as read-only address books are ignored by the API.


Functions
=========

list(parentId)
--------------
Gets all the mailing lists in the address book with id ``parentId``.

- ``parentId`` (string)


get(id)
-------
Gets a single mailing list.

- ``id`` (string)


create(parentId, properties)
----------------------------
Creates a new mailing list in the address book with id ``parentId``.

- ``parentId`` (string)
- ``properties`` (object)

  - ``name`` (string)
  - [``description``] (string)
  - [``nickName``] (string)



update(id, properties)
----------------------
Edits the properties of a mailing list.

- ``id`` (string)
- ``properties`` (object)

  - ``name`` (string)
  - [``description``] (string)
  - [``nickName``] (string)



delete(id)
----------
Removes the mailing list.

- ``id`` (string)


addMember(id, contactId)
------------------------
Adds a contact to the mailing list with id ``id``. If the contact and mailing list are in different address books, the contact will also be copied to the list's address book.

- ``id`` (string)
- ``contactId`` (string)


listMembers(id)
---------------
Gets all contacts that are members of the mailing list with id ``id``.

- ``id`` (string)


removeMember(id, contactId)
---------------------------
Removes a contact from the mailing list with id ``id``. This does not delete the contact from the address book.

- ``id`` (string)
- ``contactId`` (string)

