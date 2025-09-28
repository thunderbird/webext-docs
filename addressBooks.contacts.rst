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

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`addressBooks`

   Read and modify your address books and contacts

Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``messenger.addressBooks.contacts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _addressBooks.contacts.create:

create(parentId, vCard)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Adds a new contact to the address book with the id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``parentId``
      :type: (string)

   .. api-member::
      :name: ``vCard``
      :type: (string)

      The vCard for the new contact. If it includes an (optional) id and an existing contact has this id already, an exception is thrown.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string
      :annotation: -- [Added in TB 128]

      The ID of the new contact.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.contacts.delete:

delete(id)
----------

.. api-section-annotation-hack:: -- [Added in TB 127]

Removes a contact from the address book. The contact is also removed from any mailing lists it is a member of.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.contacts.get:

get(id)
-------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets a single contact.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`addressBooks.contacts.ContactNode`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.contacts.getPhoto:

getPhoto(id)
------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets the photo associated with this contact. Returns :value:`null`, if no photo is available.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__ or null

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.contacts.list:

list(parentId)
--------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets all the contacts in the address book with the id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``parentId``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`addressBooks.contacts.ContactNode`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.contacts.query:

query(queryInfo)
----------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Gets all contacts matching :value:`queryInfo`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``queryInfo``
      :type: (:ref:`addressBooks.contacts.QueryInfo`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`addressBooks.contacts.ContactNode`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.contacts.setPhoto:

setPhoto(id, file)
------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Sets the photo associated with this contact.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

   .. api-member::
      :name: ``file``
      :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.contacts.update:

update(id, vCard)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Updates a contact.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

   .. api-member::
      :name: ``vCard``
      :type: (string)

      The updated vCard for the contact.

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Events
======

.. _addressBooks.contacts.onCreated:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a contact is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. api-member::
      :name: ``listener(node)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``node``
      :type: (:ref:`addressBooks.contacts.ContactNode`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.contacts.onDeleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a contact is removed from an address book.

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

.. _addressBooks.contacts.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fired when a contact is changed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. api-member::
      :name: ``listener(node, oldVCard)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``node``
      :type: (:ref:`addressBooks.contacts.ContactNode`)

   .. api-member::
      :name: ``oldVCard``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Types
=====

.. _addressBooks.contacts.ContactNode:

ContactNode
-----------

.. api-section-annotation-hack:: -- [Added in TB 127]

A node representing a contact in an address book.

.. api-header::
   :label: object

   .. _addressBooks.contacts.ContactNode.id:

   .. api-member::
      :name: ``id``
      :type: (string)

      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.

   .. _addressBooks.contacts.ContactNode.type:

   .. api-member::
      :name: ``type``
      :type: (:ref:`addressBooks.NodeType`)

      Always set to :value:`contact`.

   .. _addressBooks.contacts.ContactNode.vCard:

   .. api-member::
      :name: ``vCard``
      :type: (string)
      :annotation: -- [Added in TB 128]

   .. _addressBooks.contacts.ContactNode.parentId:

   .. api-member::
      :name: [``parentId``]
      :type: (string, optional)

      The :value:`id` of the parent object.

   .. _addressBooks.contacts.ContactNode.readOnly:

   .. api-member::
      :name: [``readOnly``]
      :type: (boolean, optional)

      Indicates if the object is read-only.

   .. _addressBooks.contacts.ContactNode.remote:

   .. api-member::
      :name: [``remote``]
      :type: (boolean, optional)

      Indicates if the object came from a remote address book.

.. _addressBooks.contacts.QueryInfo:

QueryInfo
---------

.. api-section-annotation-hack:: -- [Added in TB 127]

Object defining a query for :ref:`contacts.quickSearch`.

.. api-header::
   :label: object

   .. _addressBooks.contacts.QueryInfo.includeLocal:

   .. api-member::
      :name: [``includeLocal``]
      :type: (boolean, optional)

      Whether to include results from local address books. Defaults to :value:`true`.

   .. _addressBooks.contacts.QueryInfo.includeReadOnly:

   .. api-member::
      :name: [``includeReadOnly``]
      :type: (boolean, optional)

      Whether to include results from read-only address books. Defaults to :value:`true`.

   .. _addressBooks.contacts.QueryInfo.includeReadWrite:

   .. api-member::
      :name: [``includeReadWrite``]
      :type: (boolean, optional)

      Whether to include results from read-write address books. Defaults to :value:`true`.

   .. _addressBooks.contacts.QueryInfo.includeRemote:

   .. api-member::
      :name: [``includeRemote``]
      :type: (boolean, optional)

      Whether to include results from remote address books. Defaults to :value:`true`.

   .. _addressBooks.contacts.QueryInfo.parentId:

   .. api-member::
      :name: [``parentId``]
      :type: (string, optional)

      The id of the address book to search. If not specified, all address books are searched.

   .. _addressBooks.contacts.QueryInfo.searchString:

   .. api-member::
      :name: [``searchString``]
      :type: (string, optional)

      One or more space-separated terms to search for in predefined contact fields (defined by the preference :value:`mail.addr_book.quicksearchquery.format`).
