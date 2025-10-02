.. container:: sticky-sidebar

  ≡ addressBooks.mailingLists API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

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

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _address^books.mailing^lists.permission.address^books:

.. api-member::
   :name: :permission:`addressBooks`
   :refid: address-books-mailing-lists-permission-address-books

   Read and modify your address books and contacts.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``messenger.addressBooks.mailingLists.*``.

.. rst-class:: api-main-section

Functions
=========

.. _address^books.mailing^lists.add^member:

addMember(id, contactId)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Adds a contact to the mailing list with id :value:`id`. If the contact and mailing list are in different address books, the contact will also be copied to the list's address book.

.. api-header::
   :label: Parameters

   .. _address^books.mailing^lists.add^member.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-mailing-lists-add-member-id
      :type: (string)

   .. _address^books.mailing^lists.add^member.contact^id:

   .. api-member::
      :name: ``contactId``
      :refid: address-books-mailing-lists-add-member-contact-id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.mailing^lists.create:

create(parentId, properties)
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Creates a new mailing list in the address book with id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. _address^books.mailing^lists.create.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: address-books-mailing-lists-create-parent-id
      :type: (string)

   .. _address^books.mailing^lists.create.properties:

   .. api-member::
      :name: ``properties``
      :refid: address-books-mailing-lists-create-properties
      :type: (object)

      .. _address^books.mailing^lists.create.properties.name:

      .. api-member::
         :name: ``name``
         :refid: address-books-mailing-lists-create-properties-name
         :type: (string)

      .. _address^books.mailing^lists.create.properties.description:

      .. api-member::
         :name: [``description``]
         :refid: address-books-mailing-lists-create-properties-description
         :type: (string, optional)

      .. _address^books.mailing^lists.create.properties.nick^name:

      .. api-member::
         :name: [``nickName``]
         :refid: address-books-mailing-lists-create-properties-nick-name
         :type: (string, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.mailing^lists.create.returns:

   .. api-member::
      :refid: address-books-mailing-lists-create-returns
      :type: string

      The ID of the new mailing list.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.mailing^lists.delete:

delete(id)
----------

.. api-section-annotation-hack:: -- [Added in TB 127]

Removes the mailing list.

.. api-header::
   :label: Parameters

   .. _address^books.mailing^lists.delete.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-mailing-lists-delete-id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.mailing^lists.get:

get(id)
-------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets a single mailing list.

.. api-header::
   :label: Parameters

   .. _address^books.mailing^lists.get.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-mailing-lists-get-id
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.mailing^lists.get.returns:

   .. api-member::
      :refid: address-books-mailing-lists-get-returns
      :type: :ref:`address^books.mailing^lists.^mailing^list^node`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.mailing^lists.list:

list(parentId)
--------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets all the mailing lists in the address book with id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. _address^books.mailing^lists.list.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: address-books-mailing-lists-list-parent-id
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.mailing^lists.list.returns:

   .. api-member::
      :refid: address-books-mailing-lists-list-returns
      :type: array of :ref:`address^books.mailing^lists.^mailing^list^node`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.mailing^lists.list^members:

listMembers(id)
---------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets all contacts that are members of the mailing list with id :value:`id`.

.. api-header::
   :label: Parameters

   .. _address^books.mailing^lists.list^members.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-mailing-lists-list-members-id
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.mailing^lists.list^members.returns:

   .. api-member::
      :refid: address-books-mailing-lists-list-members-returns
      :type: array of :ref:`address^books.contacts.^contact^node`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.mailing^lists.remove^member:

removeMember(id, contactId)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Removes a contact from the mailing list with id :value:`id`. This does not delete the contact from the address book.

.. api-header::
   :label: Parameters

   .. _address^books.mailing^lists.remove^member.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-mailing-lists-remove-member-id
      :type: (string)

   .. _address^books.mailing^lists.remove^member.contact^id:

   .. api-member::
      :name: ``contactId``
      :refid: address-books-mailing-lists-remove-member-contact-id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.mailing^lists.update:

update(id, properties)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Edits the properties of a mailing list.

.. api-header::
   :label: Parameters

   .. _address^books.mailing^lists.update.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-mailing-lists-update-id
      :type: (string)

   .. _address^books.mailing^lists.update.properties:

   .. api-member::
      :name: ``properties``
      :refid: address-books-mailing-lists-update-properties
      :type: (object)

      .. _address^books.mailing^lists.update.properties.name:

      .. api-member::
         :name: ``name``
         :refid: address-books-mailing-lists-update-properties-name
         :type: (string)

      .. _address^books.mailing^lists.update.properties.description:

      .. api-member::
         :name: [``description``]
         :refid: address-books-mailing-lists-update-properties-description
         :type: (string, optional)

      .. _address^books.mailing^lists.update.properties.nick^name:

      .. api-member::
         :name: [``nickName``]
         :refid: address-books-mailing-lists-update-properties-nick-name
         :type: (string, optional)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Events
======

.. _address^books.mailing^lists.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a mailing list is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _address^books.mailing^lists.on^created.listener(node):

   .. api-member::
      :name: ``listener(node)``
      :refid: address-books-mailing-lists-on-created-listener-node

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _address^books.mailing^lists.on^created.node:

   .. api-member::
      :name: ``node``
      :refid: address-books-mailing-lists-on-created-node
      :type: (:ref:`address^books.mailing^lists.^mailing^list^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.mailing^lists.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a mailing list is deleted.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. _address^books.mailing^lists.on^deleted.listener(parent^id, id):

   .. api-member::
      :name: ``listener(parentId, id)``
      :refid: address-books-mailing-lists-on-deleted-listener-parent-id-id

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _address^books.mailing^lists.on^deleted.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: address-books-mailing-lists-on-deleted-parent-id
      :type: (string)

   .. _address^books.mailing^lists.on^deleted.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-mailing-lists-on-deleted-id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.mailing^lists.on^member^added:

onMemberAdded
-------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a contact is added to the mailing list.

.. api-header::
   :label: Parameters for onMemberAdded.addListener(listener)

   .. _address^books.mailing^lists.on^member^added.listener(node):

   .. api-member::
      :name: ``listener(node)``
      :refid: address-books-mailing-lists-on-member-added-listener-node

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _address^books.mailing^lists.on^member^added.node:

   .. api-member::
      :name: ``node``
      :refid: address-books-mailing-lists-on-member-added-node
      :type: (:ref:`address^books.contacts.^contact^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.mailing^lists.on^member^removed:

onMemberRemoved
---------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a contact is removed from the mailing list.

.. api-header::
   :label: Parameters for onMemberRemoved.addListener(listener)

   .. _address^books.mailing^lists.on^member^removed.listener(parent^id, id):

   .. api-member::
      :name: ``listener(parentId, id)``
      :refid: address-books-mailing-lists-on-member-removed-listener-parent-id-id

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _address^books.mailing^lists.on^member^removed.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: address-books-mailing-lists-on-member-removed-parent-id
      :type: (string)

   .. _address^books.mailing^lists.on^member^removed.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-mailing-lists-on-member-removed-id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.mailing^lists.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a mailing list is changed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. _address^books.mailing^lists.on^updated.listener(node):

   .. api-member::
      :name: ``listener(node)``
      :refid: address-books-mailing-lists-on-updated-listener-node

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _address^books.mailing^lists.on^updated.node:

   .. api-member::
      :name: ``node``
      :refid: address-books-mailing-lists-on-updated-node
      :type: (:ref:`address^books.mailing^lists.^mailing^list^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Types
=====

.. _address^books.mailing^lists.^mailing^list^node:

MailingListNode
---------------

.. api-section-annotation-hack:: -- [Added in TB 127]

A node representing a mailing list.

.. api-header::
   :label: object

   .. _address^books.mailing^lists.^mailing^list^node.description:

   .. api-member::
      :name: ``description``
      :refid: address-books-mailing-lists-mailing-list-node-description
      :type: (string)

   .. _address^books.mailing^lists.^mailing^list^node.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-mailing-lists-mailing-list-node-id
      :type: (string)

      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.

   .. _address^books.mailing^lists.^mailing^list^node.name:

   .. api-member::
      :name: ``name``
      :refid: address-books-mailing-lists-mailing-list-node-name
      :type: (string)

   .. _address^books.mailing^lists.^mailing^list^node.nick^name:

   .. api-member::
      :name: ``nickName``
      :refid: address-books-mailing-lists-mailing-list-node-nick-name
      :type: (string)

   .. _address^books.mailing^lists.^mailing^list^node.type:

   .. api-member::
      :name: ``type``
      :refid: address-books-mailing-lists-mailing-list-node-type
      :type: (:ref:`address^books.^node^type`)

      Always set to :value:`mailingList`.

   .. _address^books.mailing^lists.^mailing^list^node.contacts:

   .. api-member::
      :name: [``contacts``]
      :refid: address-books-mailing-lists-mailing-list-node-contacts
      :type: (array of :ref:`address^books.contacts.^contact^node`, optional)

      A list of contacts held by this node's address book or mailing list.

   .. _address^books.mailing^lists.^mailing^list^node.parent^id:

   .. api-member::
      :name: [``parentId``]
      :refid: address-books-mailing-lists-mailing-list-node-parent-id
      :type: (string, optional)

      The :value:`id` of the parent object.

   .. _address^books.mailing^lists.^mailing^list^node.read^only:

   .. api-member::
      :name: [``readOnly``]
      :refid: address-books-mailing-lists-mailing-list-node-read-only
      :type: (boolean, optional)

      Indicates if the object is read-only.

   .. _address^books.mailing^lists.^mailing^list^node.remote:

   .. api-member::
      :name: [``remote``]
      :refid: address-books-mailing-lists-mailing-list-node-remote
      :type: (boolean, optional)

      Indicates if the object came from a remote address book.
