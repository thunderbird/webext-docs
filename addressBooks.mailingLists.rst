.. container:: sticky-sidebar

  ≡ addressBooks.mailingLists API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

=============================
addressBooks.mailingLists API
=============================

.. role:: permission

.. role:: value

.. role:: code

The mailingLists API allows to access and manage the user's mailing lists.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`addressBooks`

   Read and modify your address books and contacts

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``messenger.addressBooks.mailingLists.*``.

.. rst-class:: api-main-section

Functions
=========

.. _addressBooks.mailingLists.addMember:

addMember(id, contactId)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Adds a contact to the mailing list with id :value:`id`. If the contact and mailing list are in different address books, the contact will also be copied to the list's address book.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

   .. api-member::
      :name: ``contactId``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.mailingLists.create:

create(parentId, properties)
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Creates a new mailing list in the address book with id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``parentId``
      :type: (string)

   .. api-member::
      :name: ``properties``
      :type: (object)

      .. api-member::
         :name: ``name``
         :type: (string)

      .. api-member::
         :name: [``description``]
         :type: (string, optional)

      .. api-member::
         :name: [``nickName``]
         :type: (string, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string

      The ID of the new mailing list.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.mailingLists.delete:

delete(id)
----------

.. api-section-annotation-hack:: -- [Added in TB 127]

Removes the mailing list.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.mailingLists.get:

get(id)
-------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets a single mailing list.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`addressBooks.mailingLists.MailingListNode`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.mailingLists.list:

list(parentId)
--------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets all the mailing lists in the address book with id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``parentId``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`addressBooks.mailingLists.MailingListNode`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.mailingLists.listMembers:

listMembers(id)
---------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets all contacts that are members of the mailing list with id :value:`id`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`contacts.ContactNode`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.mailingLists.removeMember:

removeMember(id, contactId)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Removes a contact from the mailing list with id :value:`id`. This does not delete the contact from the address book.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

   .. api-member::
      :name: ``contactId``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.mailingLists.update:

update(id, properties)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Edits the properties of a mailing list.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

   .. api-member::
      :name: ``properties``
      :type: (object)

      .. api-member::
         :name: ``name``
         :type: (string)

      .. api-member::
         :name: [``description``]
         :type: (string, optional)

      .. api-member::
         :name: [``nickName``]
         :type: (string, optional)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Events
======

.. _addressBooks.mailingLists.onCreated:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a mailing list is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. api-member::
      :name: ``listener(node)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``node``
      :type: (:ref:`addressBooks.mailingLists.MailingListNode`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.mailingLists.onDeleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a mailing list is deleted.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. api-member::
      :name: ``listener(parentId, id)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``parentId``
      :type: (string)

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.mailingLists.onMemberAdded:

onMemberAdded
-------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a contact is added to the mailing list.

.. api-header::
   :label: Parameters for onMemberAdded.addListener(listener)

   .. api-member::
      :name: ``listener(node)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``node``
      :type: (:ref:`contacts.ContactNode`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.mailingLists.onMemberRemoved:

onMemberRemoved
---------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a contact is removed from the mailing list.

.. api-header::
   :label: Parameters for onMemberRemoved.addListener(listener)

   .. api-member::
      :name: ``listener(parentId, id)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``parentId``
      :type: (string)

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.mailingLists.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a mailing list is changed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. api-member::
      :name: ``listener(node)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``node``
      :type: (:ref:`addressBooks.mailingLists.MailingListNode`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Types
=====

.. _addressBooks.mailingLists.MailingListNode:

MailingListNode
---------------

.. api-section-annotation-hack:: -- [Added in TB 127]

A node representing a mailing list.

.. api-header::
   :label: object

   .. api-member::
      :name: ``description``
      :type: (string)

   .. api-member::
      :name: ``id``
      :type: (string)

      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.

   .. api-member::
      :name: ``name``
      :type: (string)

   .. api-member::
      :name: ``nickName``
      :type: (string)

   .. api-member::
      :name: ``type``
      :type: (:ref:`addressBooks.NodeType`)

      Always set to :value:`mailingList`.

   .. api-member::
      :name: [``contacts``]
      :type: (array of :ref:`contacts.ContactNode`, optional)

      A list of contacts held by this node's address book or mailing list.

   .. api-member::
      :name: [``parentId``]
      :type: (string, optional)

      The :value:`id` of the parent object.

   .. api-member::
      :name: [``readOnly``]
      :type: (boolean, optional)

      Indicates if the object is read-only.

   .. api-member::
      :name: [``remote``]
      :type: (boolean, optional)

      Indicates if the object came from a remote address book.
