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

.. api-member::
   :name: :permission:`sensitiveDataUpload`

   Transfer sensitive user data (if access has been granted) to a remote server for further processing

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``messenger.contacts.*``.

.. rst-class:: api-main-section

Functions
=========

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
      :type: (string, optional)
      
      Assigns the contact an id. If an existing contact has this id, an exception is thrown. **Note:** Deprecated, the card's id should be specified in the vCard string instead.
   
   
   .. api-member::
      :name: ``properties``
      :type: (:ref:`contacts.ContactProperties`)
      
      The properties object for the new contact. If it includes a ``vCard`` member, all specified `legacy properties <https://searchfox.org/comm-central/rev/8a1ae67088acf237dab2fd704db18589e7bf119e/mailnews/addrbook/modules/VCardUtils.jsm#295-334>`__ are ignored and the new contact will be based on the provided vCard string. If a UID is specified in the vCard string, which is already used by another contact, an exception is thrown. **Note:** Using individual properties is deprecated, use the ``vCard`` member instead.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
      
      The ID of the new contact.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

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

.. _contacts.getPhoto:

getPhoto(id)
------------

.. api-section-annotation-hack:: -- [Added in TB 106]

Gets the photo associated with this contact, if any.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

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
      :type: (string, optional)
      
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

.. _contacts.setPhoto:

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

.. api-section-annotation-hack:: 

Updates a contact.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
   
   
   .. api-member::
      :name: ``properties``
      :type: (:ref:`contacts.ContactProperties`)
      
      An object with properties to update the specified contact. Individual properties are removed, if they are set to :value:`null`. If the provided object includes a ``vCard`` member, all specified `legacy properties <https://searchfox.org/comm-central/rev/8a1ae67088acf237dab2fd704db18589e7bf119e/mailnews/addrbook/modules/VCardUtils.jsm#295-334>`__ are ignored and the details of the contact will be replaced by the provided vCard. Changes to the UID will be ignored. **Note:** Using individual properties is deprecated, use the ``vCard`` member instead. 
   

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
      :type: (string, optional)
      
      The ``id`` of the parent object.
   
   
   .. api-member::
      :name: [``readOnly``]
      :type: (boolean, optional)
      
      Indicates if the object is read-only.
   
   
   .. api-member::
      :name: [``remote``]
      :type: (boolean, optional)
      
      Indicates if the object came from a remote address book.
   

.. _contacts.ContactProperties:

ContactProperties
-----------------

.. api-section-annotation-hack:: 

A set of individual properties for a particular contact, and its vCard string. Further information can be found in :ref:`howto_contacts`.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``<custom properties>``
      :type: (string)
      
      Custom properties are not saved in the users vCard. Therefore, they are not transferred to the users server, if the contact is stored on a remote CardDAV server. Names of custom properties may include :value:`a-z`, :value:`A-Z`, :value:`1-9` and :value:`_`.
   
   
   .. api-member::
      :name: ``<legacy properties>``
      :type: (string)
      
      `Legacy properties <https://searchfox.org/comm-central/rev/8a1ae67088acf237dab2fd704db18589e7bf119e/mailnews/addrbook/modules/VCardUtils.jsm#295-334>`__ point to certain fields in the contacts vCard string and provide direct read/write access.
   
   
   .. api-member::
      :name: ``vCard``
      :type: (string)
      :annotation: -- [Added in TB 102]
      
      The contacts vCard string.
   

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
      :type: (boolean, optional)
      
      Whether to include results from local address books. Defaults to true.
   
   
   .. api-member::
      :name: [``includeReadOnly``]
      :type: (boolean, optional)
      
      Whether to include results from read-only address books. Defaults to true.
   
   
   .. api-member::
      :name: [``includeReadWrite``]
      :type: (boolean, optional)
      
      Whether to include results from read-write address books. Defaults to true.
   
   
   .. api-member::
      :name: [``includeRemote``]
      :type: (boolean, optional)
      
      Whether to include results from remote address books. Defaults to true.
   
   
   .. api-member::
      :name: [``searchString``]
      :type: (string, optional)
      
      One or more space-separated terms to search for.
   
