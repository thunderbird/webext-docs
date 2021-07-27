.. _addressBooks.provider_api:

=====================
addressBooks.provider
=====================

<AB.PROVIDER.TEXT>

.. role:: permission

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`addressBooks`

   Read and modify your address books and contacts

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``addressBooks.provider``.

.. rst-class:: api-main-section

Events
======

.. _addressBooks.provider.onSearchRequest:

onSearchRequest
---------------

.. api-section-annotation-hack:: 

Creates a read-only addressbook that fires this event when searching for a contact. Note: This event may change in future releases of Thunderbird.

.. api-header::
   :label: Parameters for onSearchRequest.addListener(listener, parameters)

   
   .. api-member::
      :name: ``listener(node, searchString, query)``
      
      A function that will be called when this event occurs.
   
   
   .. api-member::
      :name: ``parameters``
      :type: (object)
      
      .. api-member::
         :name: [``addressBookName``]
         :type: (string)
         
         The initial name of the address book.
      
      
      .. api-member::
         :name: [``id``]
         :type: (string)
         
         The id of the address book.
      
      
      .. api-member::
         :name: [``isSecure``]
         :type: (boolean)
         
         Whether the address book is searched securely.
      
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``node``
      :type: (:ref:`addressBooks.AddressBookNode`)
   
   
   .. api-member::
      :name: [``searchString``]
      :type: (string)
      
      The search text that the user entered. Not available when invoked from the advanced address book search dialog.
   
   
   .. api-member::
      :name: [``query``]
      :type: (string)
      
      The boolean query expression corresponding to the search. Note: This parameter may change in future releases of Thunderbird.
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`
