.. container:: sticky-sidebar

  ≡ mailingLists API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /overlay/developer-resources.rst

  ≡ Related information
  
  * :doc:`/examples/vcard`
  * :doc:`/examples/eventListeners`

  ≡ Related examples on Github
  
  * `"Address Book" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v2/addressBooks>`__

================
mailingLists API
================

The :doc:`addressBooks`, also including the :doc:`contacts` and :doc:`mailingLists` namespaces, first appeared in Thunderbird 64.

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

   The permission :permission:`addressBooks` is required to use ``messenger.mailingLists.*``.

.. rst-class:: api-main-section

Functions
=========

.. _mailingLists.addMember:

addMember(id, contactId)
------------------------

.. api-section-annotation-hack:: 

Adds a contact to the mailing list with id ``id``. If the contact and mailing list are in different address books, the contact will also be copied to the list's address book.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
   
   
   .. api-member::
      :name: ``contactId``
      :type: (string)
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailingLists.create:

create(parentId, properties)
----------------------------

.. api-section-annotation-hack:: 

Creates a new mailing list in the address book with id ``parentId``.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``parentId``
      :type: (string)
   
   
   .. api-member::
      :name: ``properties``
      :type: (object)
      
      .. api-member::
         :name: ``name``
         :type: (string)
      
      
      .. api-member::
         :name: [``description``]
         :type: (string, optional)
      
      
      .. api-member::
         :name: [``nickName``]
         :type: (string, optional)
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
      
      The ID of the new mailing list.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailingLists.delete:

delete(id)
----------

.. api-section-annotation-hack:: 

Removes the mailing list.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailingLists.get:

get(id)
-------

.. api-section-annotation-hack:: 

Gets a single mailing list.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`mailingLists.MailingListNode`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailingLists.list:

list(parentId)
--------------

.. api-section-annotation-hack:: 

Gets all the mailing lists in the address book with id ``parentId``.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``parentId``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`mailingLists.MailingListNode`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailingLists.listMembers:

listMembers(id)
---------------

.. api-section-annotation-hack:: 

Gets all contacts that are members of the mailing list with id ``id``.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`contacts.ContactNode`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailingLists.removeMember:

removeMember(id, contactId)
---------------------------

.. api-section-annotation-hack:: 

Removes a contact from the mailing list with id ``id``. This does not delete the contact from the address book.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
   
   
   .. api-member::
      :name: ``contactId``
      :type: (string)
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailingLists.update:

update(id, properties)
----------------------

.. api-section-annotation-hack:: 

Edits the properties of a mailing list.

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
      
      
      .. api-member::
         :name: [``description``]
         :type: (string, optional)
      
      
      .. api-member::
         :name: [``nickName``]
         :type: (string, optional)
      
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Events
======

.. _mailingLists.onCreated:

onCreated
---------

.. api-section-annotation-hack:: 

Fired when a mailing list is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   
   .. api-member::
      :name: ``listener(node)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``node``
      :type: (:ref:`mailingLists.MailingListNode`)
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. _mailingLists.onDeleted:

onDeleted
---------

.. api-section-annotation-hack:: 

Fired when a mailing list is deleted.

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

.. _mailingLists.onMemberAdded:

onMemberAdded
-------------

.. api-section-annotation-hack:: 

Fired when a contact is added to the mailing list.

.. api-header::
   :label: Parameters for onMemberAdded.addListener(listener)

   
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

.. _mailingLists.onMemberRemoved:

onMemberRemoved
---------------

.. api-section-annotation-hack:: 

Fired when a contact is removed from the mailing list.

.. api-header::
   :label: Parameters for onMemberRemoved.addListener(listener)

   
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

.. _mailingLists.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: 

Fired when a mailing list is changed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   
   .. api-member::
      :name: ``listener(node)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``node``
      :type: (:ref:`mailingLists.MailingListNode`)
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`

.. rst-class:: api-main-section

Types
=====

.. _mailingLists.MailingListNode:

MailingListNode
---------------

.. api-section-annotation-hack:: 

A node representing a mailing list.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``description``
      :type: (string)
   
   
   .. api-member::
      :name: ``id``
      :type: (string)
      
      The unique identifier for the node. IDs are unique within the current profile, and they remain valid even after the program is restarted.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
   
   
   .. api-member::
      :name: ``nickName``
      :type: (string)
   
   
   .. api-member::
      :name: ``type``
      :type: (:ref:`addressBooks.NodeType`)
      
      Always set to :value:`mailingList`.
   
   
   .. api-member::
      :name: [``contacts``]
      :type: (array of :ref:`contacts.ContactNode`, optional)
      
      A list of contacts held by this node's address book or mailing list.
   
   
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
      :annotation: -- [Added in TB 91]
      
      Indicates if the object came from a remote address book.
   
