.. container:: sticky-sidebar

  ≡ contacts API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

============
contacts API
============

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

The contacts API allows to access and manage the user's contacts.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _contacts.permission.address^books:

.. api-member::
   :name: :permission:`addressBooks`
   :refid: contacts-permission-address-books
   :refname: addressBooks

   Read and modify your address books and contacts.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``messenger.contacts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _contacts.create:

create(parentId, [id], properties)
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Adds a new contact to the address book with the id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. _contacts.create.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: contacts-create-parent-id
      :refname: parentId
      :type: (string)

   .. _contacts.create.id:

   .. api-member::
      :name: [``id``]
      :refid: contacts-create-id
      :refname: id
      :type: (string, optional) **Deprecated.**

      Assigns the contact an id. If an existing contact has this id, an exception is thrown.

   .. _contacts.create.properties:

   .. api-member::
      :name: ``properties``
      :refid: contacts-create-properties
      :refname: properties
      :type: (:ref:`contacts.^contact^properties`)
      :annotation: -- [Added in TB 68.0a1]

      The properties object for the new contact. If it includes a :value:`vCard` member, all specified `legacy properties <https://searchfox.org/comm-central/rev/8a1ae67088acf237dab2fd704db18589e7bf119e/mailnews/addrbook/modules/VCardUtils.jsm#295-334>`__ are ignored and the new contact will be based on the provided vCard string. If a UID is specified in the vCard string, which is already used by another contact, an exception is thrown.

      .. note::

         Using individual properties is deprecated, use the :value:`vCard` member instead.

.. api-header::
   :label: Return type (`Promise`_)

   .. _contacts.create.returns:

   .. api-member::
      :refid: contacts-create-returns
      :refname: _returns
      :type: string
      :annotation: -- [Added in TB 96.0a1]

      The ID of the new contact.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.delete:

delete(id)
----------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Removes a contact from the address book. The contact is also removed from any mailing lists it is a member of.

.. api-header::
   :label: Parameters

   .. _contacts.delete.id:

   .. api-member::
      :name: ``id``
      :refid: contacts-delete-id
      :refname: id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.get:

get(id)
-------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Gets a single contact.

.. api-header::
   :label: Parameters

   .. _contacts.get.id:

   .. api-member::
      :name: ``id``
      :refid: contacts-get-id
      :refname: id
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _contacts.get.returns:

   .. api-member::
      :refid: contacts-get-returns
      :refname: _returns
      :type: :ref:`contacts.^contact^node`
      :annotation: -- [Added in TB 96.0a1]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.get^photo:

getPhoto(id)
------------

.. api-section-annotation-hack:: -- [Added in TB 106.0a1]

Gets the photo associated with this contact. Returns :value:`null`, if no photo is available.

.. api-header::
   :label: Parameters

   .. _contacts.get^photo.id:

   .. api-member::
      :name: ``id``
      :refid: contacts-get-photo-id
      :refname: id
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _contacts.get^photo.returns:

   .. api-member::
      :refid: contacts-get-photo-returns
      :refname: _returns
      :type: `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__ or null

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.list:

list(parentId)
--------------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Gets all the contacts in the address book with the id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. _contacts.list.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: contacts-list-parent-id
      :refname: parentId
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _contacts.list.returns:

   .. api-member::
      :refid: contacts-list-returns
      :refname: _returns
      :type: array of :ref:`contacts.^contact^node`
      :annotation: -- [Added in TB 96.0a1]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.quick^search:

quickSearch([parentId], queryInfo)
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0a1]

Gets all contacts matching :value:`queryInfo` in the address book with the id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. _contacts.quick^search.parent^id:

   .. api-member::
      :name: [``parentId``]
      :refid: contacts-quick-search-parent-id
      :refname: parentId
      :type: (string, optional)

      The id of the address book to search. If not specified, all address books are searched.

   .. _contacts.quick^search.query^info:

   .. api-member::
      :name: ``queryInfo``
      :refid: contacts-quick-search-query-info
      :refname: queryInfo
      :type: (string or :ref:`contacts.^query^info`)

      Either a *string* with one or more space-separated terms to search for, or a complex :ref:`contacts.^query^info` search query.

.. api-header::
   :label: Return type (`Promise`_)

   .. _contacts.quick^search.returns:

   .. api-member::
      :refid: contacts-quick-search-returns
      :refname: _returns
      :type: array of :ref:`contacts.^contact^node`
      :annotation: -- [Added in TB 96.0a1]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.set^photo:

setPhoto(id, file)
------------------

.. api-section-annotation-hack:: -- [Added in TB 107.0a1]

Sets the photo associated with this contact.

.. api-header::
   :label: Parameters

   .. _contacts.set^photo.id:

   .. api-member::
      :name: ``id``
      :refid: contacts-set-photo-id
      :refname: id
      :type: (string)

   .. _contacts.set^photo.file:

   .. api-member::
      :name: ``file``
      :refid: contacts-set-photo-file
      :refname: file
      :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.update:

update(id, properties)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Updates a contact.

.. api-header::
   :label: Parameters

   .. _contacts.update.id:

   .. api-member::
      :name: ``id``
      :refid: contacts-update-id
      :refname: id
      :type: (string)

   .. _contacts.update.properties:

   .. api-member::
      :name: ``properties``
      :refid: contacts-update-properties
      :refname: properties
      :type: (:ref:`contacts.^contact^properties`)

      An object with properties to update the specified contact. Individual properties are removed, if they are set to :value:`null`. If the provided object includes a :value:`vCard` member, all specified `legacy properties <https://searchfox.org/comm-central/rev/8a1ae67088acf237dab2fd704db18589e7bf119e/mailnews/addrbook/modules/VCardUtils.jsm#295-334>`__ are ignored and the details of the contact will be replaced by the provided vCard. Changes to the UID will be ignored.

      .. note::

         Using individual properties is deprecated, use the :value:`vCard` member instead.

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Events
======

.. _contacts.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Fired when a contact is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _contacts.on^created.listener(node):

   .. api-member::
      :name: ``listener(node)``
      :refid: contacts-on-created-listener-node
      :refname: listener(node)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _contacts.on^created.node:

   .. api-member::
      :name: ``node``
      :refid: contacts-on-created-node
      :refname: node
      :type: (:ref:`contacts.^contact^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Fired when a contact is removed from an address book.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. _contacts.on^deleted.listener(parent^id, id):

   .. api-member::
      :name: ``listener(parentId, id)``
      :refid: contacts-on-deleted-listener-parent-id-id
      :refname: listener(parentId, id)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _contacts.on^deleted.parent^id:

   .. api-member::
      :name: ``parentId``
      :refid: contacts-on-deleted-parent-id
      :refname: parentId
      :type: (string)

   .. _contacts.on^deleted.id:

   .. api-member::
      :name: ``id``
      :refid: contacts-on-deleted-id
      :refname: id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

Fired when a contact is changed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. _contacts.on^updated.listener(node, changed^properties):

   .. api-member::
      :name: ``listener(node, changedProperties)``
      :refid: contacts-on-updated-listener-node-changed-properties
      :refname: listener(node, changedProperties)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _contacts.on^updated.node:

   .. api-member::
      :name: ``node``
      :refid: contacts-on-updated-node
      :refname: node
      :type: (:ref:`contacts.^contact^node`)

   .. _contacts.on^updated.changed^properties:

   .. api-member::
      :name: ``changedProperties``
      :refid: contacts-on-updated-changed-properties
      :refname: changedProperties
      :type: (:ref:`contacts.^property^change`)
      :annotation: -- [Added in TB 83.0a1]

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Types
=====

.. _contacts.^contact^node:

ContactNode
-----------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

A node representing a contact in an address book.

.. api-header::
   :label: object

   .. _contacts.^contact^node.id:

   .. api-member::
      :name: ``id``
      :refid: contacts-contact-node-id
      :refname: id
      :type: (string)

      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.

   .. _contacts.^contact^node.properties:

   .. api-member::
      :name: ``properties``
      :refid: contacts-contact-node-properties
      :refname: properties
      :type: (:ref:`contacts.^contact^properties`)

   .. _contacts.^contact^node.type:

   .. api-member::
      :name: ``type``
      :refid: contacts-contact-node-type
      :refname: type
      :type: (:ref:`address^books.^node^type`)

      Always set to :value:`contact`.

   .. _contacts.^contact^node.parent^id:

   .. api-member::
      :name: [``parentId``]
      :refid: contacts-contact-node-parent-id
      :refname: parentId
      :type: (string, optional)

      The :value:`id` of the parent object.

   .. _contacts.^contact^node.read^only:

   .. api-member::
      :name: [``readOnly``]
      :refid: contacts-contact-node-read-only
      :refname: readOnly
      :type: (boolean, optional)

      Indicates if the object is read-only.

   .. _contacts.^contact^node.remote:

   .. api-member::
      :name: [``remote``]
      :refid: contacts-contact-node-remote
      :refname: remote
      :type: (boolean, optional)
      :annotation: -- [Added in TB 91.0b2]

      Indicates if the object came from a remote address book.

.. _contacts.^contact^properties:

ContactProperties
-----------------

.. api-section-annotation-hack:: -- [Added in TB 64.0a1]

A set of individual properties for a particular contact, and its vCard string. Further information can be found in :doc:`guides/vcard`.

.. api-header::
   :label: object

.. _contacts.^property^change:

PropertyChange
--------------

.. api-section-annotation-hack:: -- [Added in TB 83.0a1]

A dictionary of changed properties. Keys are the property name that changed, values are an object containing :value:`oldValue` and :value:`newValue`. Values can be either a string or :value:`null`.

.. api-header::
   :label: object

.. _contacts.^query^info:

QueryInfo
---------

.. api-section-annotation-hack:: -- [Added in TB 108.0a1]

Object defining a query for :ref:`contacts.quick^search`.

.. api-header::
   :label: object

   .. _contacts.^query^info.include^local:

   .. api-member::
      :name: [``includeLocal``]
      :refid: contacts-query-info-include-local
      :refname: includeLocal
      :type: (boolean, optional)

      Whether to include results from local address books. Defaults to :value:`true`.

   .. _contacts.^query^info.include^read^only:

   .. api-member::
      :name: [``includeReadOnly``]
      :refid: contacts-query-info-include-read-only
      :refname: includeReadOnly
      :type: (boolean, optional)

      Whether to include results from read-only address books. Defaults to :value:`true`.

   .. _contacts.^query^info.include^read^write:

   .. api-member::
      :name: [``includeReadWrite``]
      :refid: contacts-query-info-include-read-write
      :refname: includeReadWrite
      :type: (boolean, optional)

      Whether to include results from read-write address books. Defaults to :value:`true`.

   .. _contacts.^query^info.include^remote:

   .. api-member::
      :name: [``includeRemote``]
      :refid: contacts-query-info-include-remote
      :refname: includeRemote
      :type: (boolean, optional)

      Whether to include results from remote address books. Defaults to :value:`true`.

   .. _contacts.^query^info.search^string:

   .. api-member::
      :name: [``searchString``]
      :refid: contacts-query-info-search-string
      :refname: searchString
      :type: (string, optional)

      One or more space-separated terms to search for in predefined contact fields (defined by the preference :value:`mail.addr_book.quicksearchquery.format`).
