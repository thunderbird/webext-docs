.. container:: sticky-sidebar

  ≡ addressBooks API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

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

.. api-member::
   :name: :permission:`addressBooks`

   Read and modify your address books and contacts

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``messenger.addressBooks.*``.

.. rst-class:: api-main-section

Functions
=========

.. _addressBooks.closeUI:

closeUI()
---------

.. api-section-annotation-hack:: -- [Added in TB 64]

Closes the address book user interface.

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.create:

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

.. _addressBooks.delete:

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

.. _addressBooks.get:

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
      :type: :ref:`addressBooks.AddressBookNode`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.list:

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
      :type: array of :ref:`addressBooks.AddressBookNode`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.openUI:

openUI()
--------

.. api-section-annotation-hack:: -- [Added in TB 64]

Opens the address book user interface.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`tabs.Tab`
      :annotation: -- [Added in TB 114]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.update:

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

.. _addressBooks.onCreated:

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
      :type: (:ref:`addressBooks.AddressBookNode`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _addressBooks.onDeleted:

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

.. _addressBooks.onUpdated:

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
      :type: (:ref:`addressBooks.AddressBookNode`)

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Types
=====

.. _addressBooks.AddressBookNode:

AddressBookNode
---------------

.. api-section-annotation-hack:: -- [Added in TB 64]

A node representing an address book.

.. api-header::
   :label: object

   .. api-member::
      :name: ``id``
      :type: (string)

      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.

   .. api-member::
      :name: ``name``
      :type: (string)

   .. api-member::
      :name: ``type``
      :type: (:ref:`addressBooks.NodeType`)

      Always set to :value:`addressBook`.

   .. api-member::
      :name: [``contacts``]
      :type: (array of :ref:`contacts.ContactNode`, optional)

      A list of contacts held by this node's address book or mailing list.

   .. api-member::
      :name: [``mailingLists``]
      :type: (array of :ref:`mailingLists.MailingListNode`, optional)

      A list of mailingLists in this node's address book.

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
      :annotation: -- [Added in TB 91]

      Indicates if the address book is accessed via remote look-up.

.. _addressBooks.NodeType:

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
