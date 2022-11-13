.. _contacts_api:

========
contacts
========

The :doc:`addressBooks` API, also including the :doc:`contacts` and :doc:`mailingLists` namespaces, first appeared in Thunderbird 64.

The `Address Books`__ sample extension uses this API.

__ https://github.com/thundernest/sample-extensions/tree/master/addressBooks

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`addressBooks`

   Read and modify your address books and contacts

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``messenger.contacts.*``.

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

quickSearch([parentId], queryInfo)
----------------------------------

.. api-section-annotation-hack:: 

Gets all contacts matching ``queryInfo`` in the address book with the id ``parentId``.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``parentId``]
      :type: (string)
      
      The id of the address book to search. If not specified, all address books are searched.
   
   
   .. api-member::
      :name: ``queryInfo``
      :type: (string or :ref:`contacts.QueryInfo`)
      
      Either a *string* with one or more space-separated terms to search for, or a complex :ref:`contacts.QueryInfo` search query.
   

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

Edits the properties of a contact. To remove a property, specify it as :value:`null`.

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

onCreated
---------

.. api-section-annotation-hack:: 

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
      :type: (:ref:`contacts.ContactNode`)
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: 

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
      :type: (:ref:`contacts.ContactNode`)
   
   
   .. api-member::
      :name: ``changedProperties``
      :type: (:ref:`contacts.PropertyChange`)
      :annotation: -- [Added in TB 83]
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _contacts.onDeleted:

onDeleted
---------

.. api-section-annotation-hack:: 

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
      
      Always set to :value:`contact`.
   
   
   .. api-member::
      :name: [``parentId``]
      :type: (string)
      
      The ``id`` of the parent object.
   
   
   .. api-member::
      :name: [``readOnly``]
      :type: (boolean)
      
      Indicates if the object is read-only.
   
   
   .. api-member::
      :name: [``remote``]
      :type: (boolean)
      
      Indicates if the object came from a remote address book.
   

.. _contacts.ContactProperties:

ContactProperties
-----------------

.. api-section-annotation-hack:: 

A set of properties for a particular contact. For a complete list of properties that Thunderbird uses, see https://hg.mozilla.org/comm-central/file/tip/mailnews/addrbook/public/nsIAbCard.idl

It is also possible to store custom properties. The custom property name however may only use :value:`a-z`, :value:`A-Z`, :value:`1-9` and underscores.

.. api-header::
   :label: object

.. _contacts.PropertyChange:

PropertyChange
--------------

.. api-section-annotation-hack:: -- [Added in TB 83]

A dictionary of changed properties. Keys are the property name that changed, values are an object containing ``oldValue`` and ``newValue``. Values can be either a string or :value:`null`.

.. api-header::
   :label: object

.. _contacts.QueryInfo:

QueryInfo
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

Object defining a query for :ref:`contacts.quickSearch`.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``includeLocal``]
      :type: (boolean)
      
      Whether to include results from local address books. Defaults to true.
   
   
   .. api-member::
      :name: [``includeReadOnly``]
      :type: (boolean)
      
      Whether to include results from read-only address books. Defaults to true.
   
   
   .. api-member::
      :name: [``includeReadWrite``]
      :type: (boolean)
      
      Whether to include results from read-write address books. Defaults to true.
   
   
   .. api-member::
      :name: [``includeRemote``]
      :type: (boolean)
      
      Whether to include results from remote address books. Defaults to true.
   
   
   .. api-member::
      :name: [``searchString``]
      :type: (string)
      
      One or more space-separated terms to search for.
   
