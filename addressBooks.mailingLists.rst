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

.. api-member::
   :name: :permission:`addressBooks`

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

   .. api-member::
      :name: ``id``
      :type: (string)

   .. api-member::
      :name: ``contactId``
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

.. _address^books.mailing^lists.delete:

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

.. _address^books.mailing^lists.get:

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

   .. api-member::
      :name: ``parentId``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
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

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
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

   .. api-member::
      :name: ``id``
      :type: (string)

   .. api-member::
      :name: ``contactId``
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

.. _address^books.mailing^lists.on^created:

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

.. _address^books.mailing^lists.on^member^added:

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

.. _address^books.mailing^lists.on^updated:

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
      :type: (string)

   .. _address^books.mailing^lists.^mailing^list^node.id:

   .. api-member::
      :name: ``id``
      :type: (string)

      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.

   .. _address^books.mailing^lists.^mailing^list^node.name:

   .. api-member::
      :name: ``name``
      :type: (string)

   .. _address^books.mailing^lists.^mailing^list^node.nick^name:

   .. api-member::
      :name: ``nickName``
      :type: (string)

   .. _address^books.mailing^lists.^mailing^list^node.type:

   .. api-member::
      :name: ``type``
      :type: (:ref:`address^books.^node^type`)

      Always set to :value:`mailingList`.

   .. _address^books.mailing^lists.^mailing^list^node.contacts:

   .. api-member::
      :name: [``contacts``]
      :type: (array of :ref:`address^books.contacts.^contact^node`, optional)

      A list of contacts held by this node's address book or mailing list.

   .. _address^books.mailing^lists.^mailing^list^node.parent^id:

   .. api-member::
      :name: [``parentId``]
      :type: (string, optional)

      The :value:`id` of the parent object.

   .. _address^books.mailing^lists.^mailing^list^node.read^only:

   .. api-member::
      :name: [``readOnly``]
      :type: (boolean, optional)

      Indicates if the object is read-only.

   .. _address^books.mailing^lists.^mailing^list^node.remote:

   .. api-member::
      :name: [``remote``]
      :type: (boolean, optional)

      Indicates if the object came from a remote address book.
