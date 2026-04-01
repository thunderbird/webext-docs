.. container:: sticky-sidebar

  ≡ mailingLists API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

================
mailingLists API
================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

The mailingLists API allows to access and manage the user's mailing lists.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _mailing^lists.permission.address^books:

.. api-member::
   :name: :permission:`addressBooks`
   :refid: mailing-lists-permission-address-books
   :refname: addressBooks

   Read and modify your address books and contacts.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``messenger.mailingLists.*``.

.. rst-class:: api-main-section

Functions
=========

.. _mailing^lists.add^member:

addMember(id, contactId)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Adds a contact to the mailing list with id :value:`id`. If the contact and mailing list are in different address books, the contact will also be copied to the list's address book.

.. api-header::
   :label: Parameters

   .. _mailing^lists.add^member.id:

   .. api-member::
      :name: ``id``
      :refid: mailing-lists-add-member-id
      :refname: id
      :type: (string)

   .. _mailing^lists.add^member.contact^id:

   .. api-member::
      :name: ``contactId``
      :refid: mailing-lists-add-member-contact-id
      :refname: contactId
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailing^lists.create:

create(parentId, properties)
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Creates a new mailing list in the address book with id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. _mailing^lists.create.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: mailing-lists-create-parent-id
      :refname: parentId
      :type: (string)

   .. _mailing^lists.create.properties:

   .. api-member::
      :name: ``properties``
      :refid: mailing-lists-create-properties
      :refname: properties
      :type: (object)

      .. _mailing^lists.create.properties.name:

      .. api-member::
         :name: ``name``
         :refid: mailing-lists-create-properties-name
         :refname: name
         :type: (string)

      .. _mailing^lists.create.properties.description:

      .. api-member::
         :name: [``description``]
         :refid: mailing-lists-create-properties-description
         :refname: description
         :type: (string, optional)

      .. _mailing^lists.create.properties.nick^name:

      .. api-member::
         :name: [``nickName``]
         :refid: mailing-lists-create-properties-nick-name
         :refname: nickName
         :type: (string, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _mailing^lists.create.returns:

   .. api-member::
      :refid: mailing-lists-create-returns
      :refname: _returns
      :type: string
      :annotation: -- [Added in TB 102.0]

      The ID of the new mailing list.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailing^lists.delete:

delete(id)
----------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Removes the mailing list.

.. api-header::
   :label: Parameters

   .. _mailing^lists.delete.id:

   .. api-member::
      :name: ``id``
      :refid: mailing-lists-delete-id
      :refname: id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailing^lists.get:

get(id)
-------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Gets a single mailing list.

.. api-header::
   :label: Parameters

   .. _mailing^lists.get.id:

   .. api-member::
      :name: ``id``
      :refid: mailing-lists-get-id
      :refname: id
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _mailing^lists.get.returns:

   .. api-member::
      :refid: mailing-lists-get-returns
      :refname: _returns
      :type: :ref:`mailing^lists.^mailing^list^node`
      :annotation: -- [Added in TB 102.0]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailing^lists.list:

list(parentId)
--------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Gets all the mailing lists in the address book with id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. _mailing^lists.list.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: mailing-lists-list-parent-id
      :refname: parentId
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _mailing^lists.list.returns:

   .. api-member::
      :refid: mailing-lists-list-returns
      :refname: _returns
      :type: array of :ref:`mailing^lists.^mailing^list^node`
      :annotation: -- [Added in TB 102.0]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailing^lists.list^members:

listMembers(id)
---------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Gets all contacts that are members of the mailing list with id :value:`id`.

.. api-header::
   :label: Parameters

   .. _mailing^lists.list^members.id:

   .. api-member::
      :name: ``id``
      :refid: mailing-lists-list-members-id
      :refname: id
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _mailing^lists.list^members.returns:

   .. api-member::
      :refid: mailing-lists-list-members-returns
      :refname: _returns
      :type: array of :ref:`contacts.^contact^node`
      :annotation: -- [Added in TB 102.0]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailing^lists.remove^member:

removeMember(id, contactId)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Removes a contact from the mailing list with id :value:`id`. This does not delete the contact from the address book.

.. api-header::
   :label: Parameters

   .. _mailing^lists.remove^member.id:

   .. api-member::
      :name: ``id``
      :refid: mailing-lists-remove-member-id
      :refname: id
      :type: (string)

   .. _mailing^lists.remove^member.contact^id:

   .. api-member::
      :name: ``contactId``
      :refid: mailing-lists-remove-member-contact-id
      :refname: contactId
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailing^lists.update:

update(id, properties)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Edits the properties of a mailing list.

.. api-header::
   :label: Parameters

   .. _mailing^lists.update.id:

   .. api-member::
      :name: ``id``
      :refid: mailing-lists-update-id
      :refname: id
      :type: (string)

   .. _mailing^lists.update.properties:

   .. api-member::
      :name: ``properties``
      :refid: mailing-lists-update-properties
      :refname: properties
      :type: (object)

      .. _mailing^lists.update.properties.name:

      .. api-member::
         :name: ``name``
         :refid: mailing-lists-update-properties-name
         :refname: name
         :type: (string)

      .. _mailing^lists.update.properties.description:

      .. api-member::
         :name: [``description``]
         :refid: mailing-lists-update-properties-description
         :refname: description
         :type: (string, optional)

      .. _mailing^lists.update.properties.nick^name:

      .. api-member::
         :name: [``nickName``]
         :refid: mailing-lists-update-properties-nick-name
         :refname: nickName
         :type: (string, optional)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Events
======

.. _mailing^lists.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Fired when a mailing list is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _mailing^lists.on^created.listener(node):

   .. api-member::
      :name: ``listener(node)``
      :refid: mailing-lists-on-created-listener-node
      :refname: listener(node)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _mailing^lists.on^created.node:

   .. api-member::
      :name: ``node``
      :refid: mailing-lists-on-created-node
      :refname: node
      :type: (:ref:`mailing^lists.^mailing^list^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailing^lists.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Fired when a mailing list is deleted.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. _mailing^lists.on^deleted.listener(parent^id, id):

   .. api-member::
      :name: ``listener(parentId, id)``
      :refid: mailing-lists-on-deleted-listener-parent-id-id
      :refname: listener(parentId, id)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _mailing^lists.on^deleted.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: mailing-lists-on-deleted-parent-id
      :refname: parentId
      :type: (string)

   .. _mailing^lists.on^deleted.id:

   .. api-member::
      :name: ``id``
      :refid: mailing-lists-on-deleted-id
      :refname: id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailing^lists.on^member^added:

onMemberAdded
-------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Fired when a contact is added to the mailing list.

.. api-header::
   :label: Parameters for onMemberAdded.addListener(listener)

   .. _mailing^lists.on^member^added.listener(node):

   .. api-member::
      :name: ``listener(node)``
      :refid: mailing-lists-on-member-added-listener-node
      :refname: listener(node)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _mailing^lists.on^member^added.node:

   .. api-member::
      :name: ``node``
      :refid: mailing-lists-on-member-added-node
      :refname: node
      :type: (:ref:`contacts.^contact^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailing^lists.on^member^removed:

onMemberRemoved
---------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Fired when a contact is removed from the mailing list.

.. api-header::
   :label: Parameters for onMemberRemoved.addListener(listener)

   .. _mailing^lists.on^member^removed.listener(parent^id, id):

   .. api-member::
      :name: ``listener(parentId, id)``
      :refid: mailing-lists-on-member-removed-listener-parent-id-id
      :refname: listener(parentId, id)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _mailing^lists.on^member^removed.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: mailing-lists-on-member-removed-parent-id
      :refname: parentId
      :type: (string)

   .. _mailing^lists.on^member^removed.id:

   .. api-member::
      :name: ``id``
      :refid: mailing-lists-on-member-removed-id
      :refname: id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailing^lists.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Fired when a mailing list is changed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. _mailing^lists.on^updated.listener(node):

   .. api-member::
      :name: ``listener(node)``
      :refid: mailing-lists-on-updated-listener-node
      :refname: listener(node)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _mailing^lists.on^updated.node:

   .. api-member::
      :name: ``node``
      :refid: mailing-lists-on-updated-node
      :refname: node
      :type: (:ref:`mailing^lists.^mailing^list^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Types
=====

.. _mailing^lists.^mailing^list^node:

MailingListNode
---------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

A node representing a mailing list.

.. api-header::
   :label: object

   .. _mailing^lists.^mailing^list^node.description:

   .. api-member::
      :name: ``description``
      :refid: mailing-lists-mailing-list-node-description
      :refname: description
      :type: (string)

   .. _mailing^lists.^mailing^list^node.id:

   .. api-member::
      :name: ``id``
      :refid: mailing-lists-mailing-list-node-id
      :refname: id
      :type: (string)

      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.

   .. _mailing^lists.^mailing^list^node.name:

   .. api-member::
      :name: ``name``
      :refid: mailing-lists-mailing-list-node-name
      :refname: name
      :type: (string)

   .. _mailing^lists.^mailing^list^node.nick^name:

   .. api-member::
      :name: ``nickName``
      :refid: mailing-lists-mailing-list-node-nick-name
      :refname: nickName
      :type: (string)

   .. _mailing^lists.^mailing^list^node.type:

   .. api-member::
      :name: ``type``
      :refid: mailing-lists-mailing-list-node-type
      :refname: type
      :type: (:ref:`address^books.^node^type`)

      Always set to :value:`mailingList`.

   .. _mailing^lists.^mailing^list^node.contacts:

   .. api-member::
      :name: [``contacts``]
      :refid: mailing-lists-mailing-list-node-contacts
      :refname: contacts
      :type: (array of :ref:`contacts.^contact^node`, optional)

      A list of contacts held by this node's address book or mailing list.

   .. _mailing^lists.^mailing^list^node.parent^id:

   .. api-member::
      :name: [``parentId``]
      :refid: mailing-lists-mailing-list-node-parent-id
      :refname: parentId
      :type: (string, optional)

      The :value:`id` of the parent object.

   .. _mailing^lists.^mailing^list^node.read^only:

   .. api-member::
      :name: [``readOnly``]
      :refid: mailing-lists-mailing-list-node-read-only
      :refname: readOnly
      :type: (boolean, optional)

      Indicates if the object is read-only.

   .. _mailing^lists.^mailing^list^node.remote:

   .. api-member::
      :name: [``remote``]
      :refid: mailing-lists-mailing-list-node-remote
      :refname: remote
      :type: (boolean, optional)
      :annotation: -- [Added in TB 91.0]

      Indicates if the object came from a remote address book.
