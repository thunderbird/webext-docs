.. container:: sticky-sidebar

  ≡ addressBooks API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

================
addressBooks API
================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

The addressBooks API allows to access and manage the user's address books.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _address^books.permission.address^books:

.. api-member::
   :name: :permission:`addressBooks`
   :refid: address-books-permission-address-books
   :refname: addressBooks

   Read and modify your address books and contacts.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``messenger.addressBooks.*``.

.. rst-class:: api-main-section

Functions
=========

.. _address^books.close^u^i:

closeUI()
---------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Closes the address book user interface.

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.create:

create(properties)
------------------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Creates a new, empty address book.

.. api-header::
   :label: Parameters

   .. _address^books.create.properties:

   .. api-member::
      :name: ``properties``
      :refid: address-books-create-properties
      :refname: properties
      :type: (object)

      .. _address^books.create.properties.name:

      .. api-member::
         :name: ``name``
         :refid: address-books-create-properties-name
         :refname: name
         :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.create.returns:

   .. api-member::
      :refid: address-books-create-returns
      :refname: _returns
      :type: string
      :annotation: -- [Added in TB 89.0a1]

      The id of the new address book.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.delete:

delete(id)
----------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Removes an address book, and all associated contacts and mailing lists.

.. api-header::
   :label: Parameters

   .. _address^books.delete.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-delete-id
      :refname: id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.get:

get(id, [complete])
-------------------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Gets a single address book, optionally including all contacts and mailing lists.

.. api-header::
   :label: Parameters

   .. _address^books.get.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-get-id
      :refname: id
      :type: (string)

   .. _address^books.get.complete:

   .. api-member::
      :name: [``complete``]
      :refid: address-books-get-complete
      :refname: complete
      :type: (boolean, optional)

      If set to true, results will include contacts and mailing lists for this address book.

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.get.returns:

   .. api-member::
      :refid: address-books-get-returns
      :refname: _returns
      :type: :ref:`address^books.^address^book^node`
      :annotation: -- [Added in TB 89.0a1]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.list:

list([complete])
----------------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Gets a list of the user's address books, optionally including all contacts and mailing lists.

.. api-header::
   :label: Parameters

   .. _address^books.list.complete:

   .. api-member::
      :name: [``complete``]
      :refid: address-books-list-complete
      :refname: complete
      :type: (boolean, optional)

      If set to true, results will include contacts and mailing lists for each address book.

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.list.returns:

   .. api-member::
      :refid: address-books-list-returns
      :refname: _returns
      :type: array of :ref:`address^books.^address^book^node`
      :annotation: -- [Added in TB 89.0a1]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.open^u^i:

openUI()
--------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Opens the address book user interface.

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.open^u^i.returns:

   .. api-member::
      :refid: address-books-open-u-i-returns
      :refname: _returns
      :type: :ref:`tabs.^tab`
      :annotation: -- [Added in TB 114.0a1]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.update:

update(id, properties)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Renames an address book.

.. api-header::
   :label: Parameters

   .. _address^books.update.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-update-id
      :refname: id
      :type: (string)

   .. _address^books.update.properties:

   .. api-member::
      :name: ``properties``
      :refid: address-books-update-properties
      :refname: properties
      :type: (object)

      .. _address^books.update.properties.name:

      .. api-member::
         :name: ``name``
         :refid: address-books-update-properties-name
         :refname: name
         :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Events
======

.. _address^books.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Fired when an address book is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _address^books.on^created.listener(node):

   .. api-member::
      :name: ``listener(node)``
      :refid: address-books-on-created-listener-node
      :refname: listener(node)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _address^books.on^created.node:

   .. api-member::
      :name: ``node``
      :refid: address-books-on-created-node
      :refname: node
      :type: (:ref:`address^books.^address^book^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Fired when an addressBook is deleted.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. _address^books.on^deleted.listener(id):

   .. api-member::
      :name: ``listener(id)``
      :refid: address-books-on-deleted-listener-id
      :refname: listener(id)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _address^books.on^deleted.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-on-deleted-id
      :refname: id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Fired when an address book is renamed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. _address^books.on^updated.listener(node):

   .. api-member::
      :name: ``listener(node)``
      :refid: address-books-on-updated-listener-node
      :refname: listener(node)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _address^books.on^updated.node:

   .. api-member::
      :name: ``node``
      :refid: address-books-on-updated-node
      :refname: node
      :type: (:ref:`address^books.^address^book^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Types
=====

.. _address^books.^address^book^node:

AddressBookNode
---------------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

A node representing an address book.

.. api-header::
   :label: object

   .. _address^books.^address^book^node.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-address-book-node-id
      :refname: id
      :type: (string)

      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.

   .. _address^books.^address^book^node.name:

   .. api-member::
      :name: ``name``
      :refid: address-books-address-book-node-name
      :refname: name
      :type: (string)

   .. _address^books.^address^book^node.type:

   .. api-member::
      :name: ``type``
      :refid: address-books-address-book-node-type
      :refname: type
      :type: (:ref:`address^books.^node^type`)

      Always set to :value:`addressBook`.

   .. _address^books.^address^book^node.contacts:

   .. api-member::
      :name: [``contacts``]
      :refid: address-books-address-book-node-contacts
      :refname: contacts
      :type: (array of :ref:`contacts.^contact^node`, optional)

      A list of contacts held by this node's address book or mailing list.

   .. _address^books.^address^book^node.mailing^lists:

   .. api-member::
      :name: [``mailingLists``]
      :refid: address-books-address-book-node-mailing-lists
      :refname: mailingLists
      :type: (array of :ref:`mailing^lists.^mailing^list^node`, optional)

      A list of mailingLists in this node's address book.

   .. _address^books.^address^book^node.parent^id:

   .. api-member::
      :name: [``parentId``]
      :refid: address-books-address-book-node-parent-id
      :refname: parentId
      :type: (string, optional)

      The :value:`id` of the parent object.

   .. _address^books.^address^book^node.read^only:

   .. api-member::
      :name: [``readOnly``]
      :refid: address-books-address-book-node-read-only
      :refname: readOnly
      :type: (boolean, optional)

      Indicates if the object is read-only.

   .. _address^books.^address^book^node.remote:

   .. api-member::
      :name: [``remote``]
      :refid: address-books-address-book-node-remote
      :refname: remote
      :type: (boolean, optional)
      :annotation: -- [Added in TB 91.0b2]

      Indicates if the address book is accessed via remote look-up.

.. _address^books.^node^type:

NodeType
--------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Indicates the type of a Node.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _address^books.^node^type.address^book:

         .. api-member::
            :name: :value:`addressBook`
            :refid: address-books-node-type-address-book
            :refname: addressBook

         .. _address^books.^node^type.contact:

         .. api-member::
            :name: :value:`contact`
            :refid: address-books-node-type-contact
            :refname: contact

         .. _address^books.^node^type.mailing^list:

         .. api-member::
            :name: :value:`mailingList`
            :refid: address-books-node-type-mailing-list
            :refname: mailingList
