========
contacts
========

The address books API, also including the :doc:`addressBooks` and :doc:`mailingLists` namespaces, first appeared in Thunderbird 64.
The quickSearch function was added in Thunderbird 68.

The `Address Books`__ sample extension uses this API.

__ https://github.com/thundernest/sample-extensions/tree/master/addressBooks

.. role:: permission

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`addressBooks`

   Read and modify your address books and contacts

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``contacts``.

.. rst-class:: api-main-section

Functions
=========

.. _contacts.list:

list(parentId)
--------------

.. api-section-annotation-hack:: 

Gets all the contacts in the address book with the id ``parentId``.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``parentId``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`contacts.ContactNode`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.quickSearch:

quickSearch([parentId], searchString)
-------------------------------------

.. api-section-annotation-hack:: 

Gets all contacts matching ``searchString`` in the address book with the id ``parentId``.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``parentId``]
      :type: (string)
      
      The ID of the address book to search. If not specified, all address books are searched.
   
   
   .. api-member::
      :name: ``searchString``
      :type: (string)
      
      One or more space-separated terms to search for.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`contacts.ContactNode`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.get:

get(id)
-------

.. api-section-annotation-hack:: 

Gets a single contact.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`contacts.ContactNode`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.create:

create(parentId, [id], properties)
----------------------------------

.. api-section-annotation-hack:: 

Adds a new contact to the address book with the id ``parentId``.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``parentId``
      :type: (string)
   
   
   .. api-member::
      :name: [``id``]
      :type: (string)
      
      Assigns the contact an id. If an existing contact has this id, an exception is thrown.
   
   
   .. api-member::
      :name: ``properties``
      :type: (:ref:`contacts.ContactProperties`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
      
      The ID of the new contact.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.update:

update(id, properties)
----------------------

.. api-section-annotation-hack:: 

Edits the properties of a contact. To remove a property, specify it as ``null``.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
   
   
   .. api-member::
      :name: ``properties``
      :type: (:ref:`contacts.ContactProperties`)
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.delete:

delete(id)
----------

.. api-section-annotation-hack:: 

Removes a contact from the address book. The contact is also removed from any mailing lists it is a member of.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Events
======

.. _contacts.onCreated:

onCreated(node, id)
-------------------

.. api-section-annotation-hack:: 

Fired when a contact is created.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``node``
      :type: (:ref:`contacts.ContactNode`)
   
   
   .. api-member::
      :name: ``id``
      :type: (string)
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.onUpdated:

onUpdated(node)
---------------

.. api-section-annotation-hack:: 

Fired when a contact is changed.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``node``
      :type: (:ref:`contacts.ContactNode`)
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.onDeleted:

onDeleted(parentId, id)
-----------------------

.. api-section-annotation-hack:: 

Fired when a contact is removed from an address book.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``parentId``
      :type: (string)
   
   
   .. api-member::
      :name: ``id``
      :type: (string)
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Types
=====

.. _contacts.ContactNode:

ContactNode
-----------

.. api-section-annotation-hack:: 

A node representing a contact in an address book.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``id``
      :type: (string)
      
      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.
   
   
   .. api-member::
      :name: ``properties``
      :type: (:ref:`contacts.ContactProperties`)
   
   
   .. api-member::
      :name: ``type``
      :type: (:ref:`addressBooks.NodeType`)
      
      Always set to ``contact``.
   
   
   .. api-member::
      :name: [``parentId``]
      :type: (string)
      
      The ``id`` of the parent object.
   
   
   .. api-member::
      :name: [``readOnly``]
      :type: (boolean)
      
      Indicates if the object is read-only. Currently this returns false in all cases, as read-only address books are ignored by the API.
   

.. _contacts.ContactProperties:

ContactProperties
-----------------

.. api-section-annotation-hack:: 

A set of properties for a particular contact. For a complete list of properties that Thunderbird uses, see https://hg.mozilla.org/comm-central/file/tip/mailnews/addrbook/public/nsIAbCard.idl

It is also possible to store custom properties. The custom property name however may only use a to z, A to Z, 1 to 9 and underscores.

.. api-header::
   :label: object
