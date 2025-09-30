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

The contacts API allows to access and manage the user's contacts.

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

   The permission :permission:`addressBooks` is required to use ``messenger.contacts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _contacts.create:

create(parentId, [id], properties)
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Adds a new contact to the address book with the id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``parentId``
      :type: (string)

   .. api-member::
      :name: [``id``]
      :type: (string, optional) **Deprecated.**

      Assigns the contact an id. If an existing contact has this id, an exception is thrown.

   .. api-member::
      :name: ``properties``
      :type: (:ref:`contacts.^contact^properties`)
      :annotation: -- [Added in TB 68]

      The properties object for the new contact. If it includes a :value:`vCard` member, all specified `legacy properties <https://searchfox.org/comm-central/rev/8a1ae67088acf237dab2fd704db18589e7bf119e/mailnews/addrbook/modules/VCardUtils.jsm#295-334>`__ are ignored and the new contact will be based on the provided vCard string. If a UID is specified in the vCard string, which is already used by another contact, an exception is thrown.

      .. note::

         Using individual properties is deprecated, use the :value:`vCard` member instead.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string
      :annotation: -- [Added in TB 96]

      The ID of the new contact.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.delete:

delete(id)
----------

.. api-section-annotation-hack:: -- [Added in TB 64]

Removes a contact from the address book. The contact is also removed from any mailing lists it is a member of.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.get:

get(id)
-------

.. api-section-annotation-hack:: -- [Added in TB 64]

Gets a single contact.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`contacts.^contact^node`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.get^photo:

getPhoto(id)
------------

.. api-section-annotation-hack:: -- [Added in TB 106]

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

.. _contacts.list:

list(parentId)
--------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Gets all the contacts in the address book with the id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``parentId``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`contacts.^contact^node`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.quick^search:

quickSearch([parentId], queryInfo)
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 68]

Gets all contacts matching :value:`queryInfo` in the address book with the id :value:`parentId`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``parentId``]
      :type: (string, optional)

      The id of the address book to search. If not specified, all address books are searched.

   .. api-member::
      :name: ``queryInfo``
      :type: (string or :ref:`contacts.^query^info`)

      Either a *string* with one or more space-separated terms to search for, or a complex :ref:`contacts.^query^info` search query.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`contacts.^contact^node`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.set^photo:

setPhoto(id, file)
------------------

.. api-section-annotation-hack:: -- [Added in TB 107]

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

.. _contacts.update:

update(id, properties)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Updates a contact.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

   .. api-member::
      :name: ``properties``
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

.. api-section-annotation-hack:: -- [Added in TB 64]

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
      :type: (:ref:`contacts.^contact^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 64]

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

.. _contacts.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 64]

Fired when a contact is changed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. api-member::
      :name: ``listener(node, changedProperties)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``node``
      :type: (:ref:`contacts.^contact^node`)

   .. api-member::
      :name: ``changedProperties``
      :type: (:ref:`contacts.^property^change`)
      :annotation: -- [Added in TB 83]

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Types
=====

.. _contacts.^contact^node:

ContactNode
-----------

.. api-section-annotation-hack:: -- [Added in TB 64]

A node representing a contact in an address book.

.. api-header::
   :label: object

   .. _contacts.^contact^node.id:

   .. api-member::
      :name: ``id``
      :type: (string)

      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.

   .. _contacts.^contact^node.properties:

   .. api-member::
      :name: ``properties``
      :type: (:ref:`contacts.^contact^properties`)

   .. _contacts.^contact^node.type:

   .. api-member::
      :name: ``type``
      :type: (:ref:`address^books.^node^type`)

      Always set to :value:`contact`.

   .. _contacts.^contact^node.parent^id:

   .. api-member::
      :name: [``parentId``]
      :type: (string, optional)

      The :value:`id` of the parent object.

   .. _contacts.^contact^node.read^only:

   .. api-member::
      :name: [``readOnly``]
      :type: (boolean, optional)

      Indicates if the object is read-only.

   .. _contacts.^contact^node.remote:

   .. api-member::
      :name: [``remote``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 91]

      Indicates if the object came from a remote address book.

.. _contacts.^contact^properties:

ContactProperties
-----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

A set of individual properties for a particular contact, and its vCard string. Further information can be found in :doc:`guides/vcard`.

.. api-header::
   :label: object

.. _contacts.^property^change:

PropertyChange
--------------

.. api-section-annotation-hack:: -- [Added in TB 83]

A dictionary of changed properties. Keys are the property name that changed, values are an object containing :value:`oldValue` and :value:`newValue`. Values can be either a string or :value:`null`.

.. api-header::
   :label: object

.. _contacts.^query^info:

QueryInfo
---------

.. api-section-annotation-hack:: -- [Added in TB 108]

Object defining a query for :ref:`contacts.quick^search`.

.. api-header::
   :label: object

   .. _contacts.^query^info.include^local:

   .. api-member::
      :name: [``includeLocal``]
      :type: (boolean, optional)

      Whether to include results from local address books. Defaults to :value:`true`.

   .. _contacts.^query^info.include^read^only:

   .. api-member::
      :name: [``includeReadOnly``]
      :type: (boolean, optional)

      Whether to include results from read-only address books. Defaults to :value:`true`.

   .. _contacts.^query^info.include^read^write:

   .. api-member::
      :name: [``includeReadWrite``]
      :type: (boolean, optional)

      Whether to include results from read-write address books. Defaults to :value:`true`.

   .. _contacts.^query^info.include^remote:

   .. api-member::
      :name: [``includeRemote``]
      :type: (boolean, optional)

      Whether to include results from remote address books. Defaults to :value:`true`.

   .. _contacts.^query^info.search^string:

   .. api-member::
      :name: [``searchString``]
      :type: (string, optional)

      One or more space-separated terms to search for in predefined contact fields (defined by the preference :value:`mail.addr_book.quicksearchquery.format`).
