.. container:: sticky-sidebar

  ≡ addressBooks.contacts API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=========================
addressBooks.contacts API
=========================

.. role:: permission

.. role:: value

.. role:: code

The contacts API allows to access and manage the user's contacts.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _address^books.contacts.permission.address^books:

.. api-member::
   :name: :permission:`addressBooks`
   :refid: address-books-contacts-permission-address-books

   Read and modify your address books and contacts.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``messenger.addressBooks.contacts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _address^books.contacts.create:

create(parentId, vCard)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Adds a new contact to the address book with the id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. _address^books.contacts.create.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: address-books-contacts-create-parent-id
      :type: (string)

   .. _address^books.contacts.create.v^card:

   .. api-member::
      :name: ``vCard``
      :refid: address-books-contacts-create-v-card
      :type: (string)

      The vCard for the new contact. If it includes an (optional) id and an existing contact has this id already, an exception is thrown.

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.contacts.create.returns:

   .. api-member::
      :refid: address-books-contacts-create-returns
      :type: string
      :annotation: -- [Added in TB 128]

      The ID of the new contact.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.contacts.delete:

delete(id)
----------

.. api-section-annotation-hack:: -- [Added in TB 127]

Removes a contact from the address book. The contact is also removed from any mailing lists it is a member of.

.. api-header::
   :label: Parameters

   .. _address^books.contacts.delete.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-contacts-delete-id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.contacts.get:

get(id)
-------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets a single contact.

.. api-header::
   :label: Parameters

   .. _address^books.contacts.get.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-contacts-get-id
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.contacts.get.returns:

   .. api-member::
      :refid: address-books-contacts-get-returns
      :type: :ref:`address^books.contacts.^contact^node`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.contacts.get^photo:

getPhoto(id)
------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets the photo associated with this contact. Returns :value:`null`, if no photo is available.

.. api-header::
   :label: Parameters

   .. _address^books.contacts.get^photo.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-contacts-get-photo-id
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.contacts.get^photo.returns:

   .. api-member::
      :refid: address-books-contacts-get-photo-returns
      :type: `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__ or null

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.contacts.list:

list(parentId)
--------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets all the contacts in the address book with the id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. _address^books.contacts.list.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: address-books-contacts-list-parent-id
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.contacts.list.returns:

   .. api-member::
      :refid: address-books-contacts-list-returns
      :type: array of :ref:`address^books.contacts.^contact^node`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.contacts.query:

query(queryInfo)
----------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets all contacts matching :value:`queryInfo`.

.. api-header::
   :label: Parameters

   .. _address^books.contacts.query.query^info:

   .. api-member::
      :name: ``queryInfo``
      :refid: address-books-contacts-query-query-info
      :type: (:ref:`address^books.contacts.^query^info`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _address^books.contacts.query.returns:

   .. api-member::
      :refid: address-books-contacts-query-returns
      :type: array of :ref:`address^books.contacts.^contact^node`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.contacts.set^photo:

setPhoto(id, file)
------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Sets the photo associated with this contact.

.. api-header::
   :label: Parameters

   .. _address^books.contacts.set^photo.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-contacts-set-photo-id
      :type: (string)

   .. _address^books.contacts.set^photo.file:

   .. api-member::
      :name: ``file``
      :refid: address-books-contacts-set-photo-file
      :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.contacts.update:

update(id, vCard)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Updates a contact.

.. api-header::
   :label: Parameters

   .. _address^books.contacts.update.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-contacts-update-id
      :type: (string)

   .. _address^books.contacts.update.v^card:

   .. api-member::
      :name: ``vCard``
      :refid: address-books-contacts-update-v-card
      :type: (string)

      The updated vCard for the contact.

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Events
======

.. _address^books.contacts.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a contact is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _address^books.contacts.on^created.listener(node):

   .. api-member::
      :name: ``listener(node)``
      :refid: address-books-contacts-on-created-listener-node

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _address^books.contacts.on^created.node:

   .. api-member::
      :name: ``node``
      :refid: address-books-contacts-on-created-node
      :type: (:ref:`address^books.contacts.^contact^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.contacts.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a contact is removed from an address book.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. _address^books.contacts.on^deleted.listener(parent^id, id):

   .. api-member::
      :name: ``listener(parentId, id)``
      :refid: address-books-contacts-on-deleted-listener-parent-id-id

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _address^books.contacts.on^deleted.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: address-books-contacts-on-deleted-parent-id
      :type: (string)

   .. _address^books.contacts.on^deleted.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-contacts-on-deleted-id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.contacts.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a contact is changed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. _address^books.contacts.on^updated.listener(node, old^v^card):

   .. api-member::
      :name: ``listener(node, oldVCard)``
      :refid: address-books-contacts-on-updated-listener-node-old-v-card

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _address^books.contacts.on^updated.node:

   .. api-member::
      :name: ``node``
      :refid: address-books-contacts-on-updated-node
      :type: (:ref:`address^books.contacts.^contact^node`)

   .. _address^books.contacts.on^updated.old^v^card:

   .. api-member::
      :name: ``oldVCard``
      :refid: address-books-contacts-on-updated-old-v-card
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Types
=====

.. _address^books.contacts.^contact^node:

ContactNode
-----------

.. api-section-annotation-hack:: -- [Added in TB 127]

A node representing a contact in an address book.

.. api-header::
   :label: object

   .. _address^books.contacts.^contact^node.id:

   .. api-member::
      :name: ``id``
      :refid: address-books-contacts-contact-node-id
      :type: (string)

      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.

   .. _address^books.contacts.^contact^node.type:

   .. api-member::
      :name: ``type``
      :refid: address-books-contacts-contact-node-type
      :type: (:ref:`address^books.^node^type`)

      Always set to :value:`contact`.

   .. _address^books.contacts.^contact^node.v^card:

   .. api-member::
      :name: ``vCard``
      :refid: address-books-contacts-contact-node-v-card
      :type: (string)
      :annotation: -- [Added in TB 128]

   .. _address^books.contacts.^contact^node.parent^id:

   .. api-member::
      :name: [``parentId``]
      :refid: address-books-contacts-contact-node-parent-id
      :type: (string, optional)

      The :value:`id` of the parent object.

   .. _address^books.contacts.^contact^node.read^only:

   .. api-member::
      :name: [``readOnly``]
      :refid: address-books-contacts-contact-node-read-only
      :type: (boolean, optional)

      Indicates if the object is read-only.

   .. _address^books.contacts.^contact^node.remote:

   .. api-member::
      :name: [``remote``]
      :refid: address-books-contacts-contact-node-remote
      :type: (boolean, optional)

      Indicates if the object came from a remote address book.

.. _address^books.contacts.^contact^properties:

ContactProperties
-----------------

.. api-section-annotation-hack:: -- [Added in TB 127]

A set of individual properties for a particular contact, and its vCard string. Further information can be found in :doc:`guides/vcard`.

.. api-header::
   :label: object

.. _address^books.contacts.^property^change:

PropertyChange
--------------

.. api-section-annotation-hack:: -- [Added in TB 127]

A dictionary of changed properties. Keys are the property name that changed, values are an object containing :value:`oldValue` and :value:`newValue`. Values can be either a string or :value:`null`.

.. api-header::
   :label: object

.. _address^books.contacts.^query^info:

QueryInfo
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Object defining a query for :ref:`address^books.contacts.quick^search`.

.. api-header::
   :label: object

   .. _address^books.contacts.^query^info.include^local:

   .. api-member::
      :name: [``includeLocal``]
      :refid: address-books-contacts-query-info-include-local
      :type: (boolean, optional)

      Whether to include results from local address books. Defaults to :value:`true`.

   .. _address^books.contacts.^query^info.include^read^only:

   .. api-member::
      :name: [``includeReadOnly``]
      :refid: address-books-contacts-query-info-include-read-only
      :type: (boolean, optional)

      Whether to include results from read-only address books. Defaults to :value:`true`.

   .. _address^books.contacts.^query^info.include^read^write:

   .. api-member::
      :name: [``includeReadWrite``]
      :refid: address-books-contacts-query-info-include-read-write
      :type: (boolean, optional)

      Whether to include results from read-write address books. Defaults to :value:`true`.

   .. _address^books.contacts.^query^info.include^remote:

   .. api-member::
      :name: [``includeRemote``]
      :refid: address-books-contacts-query-info-include-remote
      :type: (boolean, optional)

      Whether to include results from remote address books. Defaults to :value:`true`.

   .. _address^books.contacts.^query^info.parent^id:

   .. api-member::
      :name: [``parentId``]
      :refid: address-books-contacts-query-info-parent-id
      :type: (string, optional)

      The id of the address book to search. If not specified, all address books are searched.

   .. _address^books.contacts.^query^info.search^string:

   .. api-member::
      :name: [``searchString``]
      :refid: address-books-contacts-query-info-search-string
      :type: (string, optional)

      One or more space-separated terms to search for in predefined contact fields (defined by the preference :value:`mail.addr_book.quicksearchquery.format`).
