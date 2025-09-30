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

The addressBooks API allows to access and manage the user's address books.

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

   The permission :permission:`addressBooks` is required to use ``messenger.addressBooks.*``.

.. rst-class:: api-main-section

Functions
=========

.. _address^books.close^u^i:

closeUI()
---------

.. api-section-annotation-hack:: -- [Added in TB 64]

Closes the address book user interface.

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.create:

create(properties)
------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Creates a new, empty address book.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``properties``
      :type: (object)

      .. api-member::
         :name: ``name``
         :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string
      :annotation: -- [Added in TB 89]

      The id of the new address book.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.delete:

delete(id)
----------

.. api-section-annotation-hack:: -- [Added in TB 64]

Removes an address book, and all associated contacts and mailing lists.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.get:

get(id, [complete])
-------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Gets a single address book, optionally including all contacts and mailing lists.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

   .. api-member::
      :name: [``complete``]
      :type: (boolean, optional)

      If set to true, results will include contacts and mailing lists for this address book.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`address^books.^address^book^node`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.list:

list([complete])
----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Gets a list of the user's address books, optionally including all contacts and mailing lists.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``complete``]
      :type: (boolean, optional)

      If set to true, results will include contacts and mailing lists for each address book.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`address^books.^address^book^node`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.open^u^i:

openUI()
--------

.. api-section-annotation-hack:: -- [Added in TB 64]

Opens the address book user interface.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`tabs.^tab`
      :annotation: -- [Added in TB 114]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.update:

update(id, properties)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Renames an address book.

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

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Events
======

.. _address^books.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 64]

Fired when an address book is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. api-member::
      :name: ``listener(node)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``node``
      :type: (:ref:`address^books.^address^book^node`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 64]

Fired when an addressBook is deleted.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. api-member::
      :name: ``listener(id)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``id``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _address^books.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 64]

Fired when an address book is renamed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. api-member::
      :name: ``listener(node)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``node``
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

.. api-section-annotation-hack:: -- [Added in TB 64]

A node representing an address book.

.. api-header::
   :label: object

   .. _address^books.^address^book^node.id:

   .. api-member::
      :name: ``id``
      :type: (string)

      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.

   .. _address^books.^address^book^node.name:

   .. api-member::
      :name: ``name``
      :type: (string)

   .. _address^books.^address^book^node.type:

   .. api-member::
      :name: ``type``
      :type: (:ref:`address^books.^node^type`)

      Always set to :value:`addressBook`.

   .. _address^books.^address^book^node.contacts:

   .. api-member::
      :name: [``contacts``]
      :type: (array of :ref:`address^books.contacts.^contact^node`, optional)

      A list of contacts held by this node's address book or mailing list.

   .. _address^books.^address^book^node.mailing^lists:

   .. api-member::
      :name: [``mailingLists``]
      :type: (array of :ref:`address^books.mailing^lists.^mailing^list^node`, optional)

      A list of mailingLists in this node's address book.

   .. _address^books.^address^book^node.parent^id:

   .. api-member::
      :name: [``parentId``]
      :type: (string, optional)

      The :value:`id` of the parent object.

   .. _address^books.^address^book^node.read^only:

   .. api-member::
      :name: [``readOnly``]
      :type: (boolean, optional)

      Indicates if the object is read-only.

   .. _address^books.^address^book^node.remote:

   .. api-member::
      :name: [``remote``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 91]

      Indicates if the address book is accessed via remote look-up.

.. _address^books.^node^type:

NodeType
--------

.. api-section-annotation-hack:: -- [Added in TB 64]

Indicates the type of a Node.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`addressBook`

         .. api-member::
            :name: :value:`contact`

         .. api-member::
            :name: :value:`mailingList`
