.. _addressBooks.provider_api:

=====================
addressBooks.provider
=====================

The :ref:`addressBooks.provider_api` API first appeared in Thunderbird 90. It allows to add address books, which are not stored or cached by Thunderbird itself, but are handled completely by the extension. Address books created by the :ref:`addressBooks.provider_api` API will forward all access requests to the WebExtension. Possible use cases:

* implement a custom storage
* implement search-only address books querying a remote server

So far, only the API for search-only address books is implemented. 

.. warning::

  This API will change in future releases of Thunderbird.

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

Registering this listener will create and list a read-only address book in Thunderbird's address book window, similar to LDAP address books. When selecting this address book, the user will first see no contacts, but he can search for them, which will fire this event. Contacts returned by the listener callback will be displayed as contact cards in the address book. Several listeners can be registered, to create multiple address books.

The event also fires for each registered listener (for each created read-only address book), when the user types something into the mail composer's ``To:`` field, or into similar fields like the calendar meeting attendees field. Contacts returned by the listener callback will be added to the autocomplete results in the dropdown of that field.

Example: 

.. literalinclude:: includes/addressBooks/onSearchRequest.js
  :language: JavaScript

.. api-header::
   :label: Parameters for onSearchRequest.addListener(listener, parameters)

   
   .. api-member::
      :name: ``listener(node, searchString, query)``
      
      A function that will be called when this event occurs.
   
   
   .. api-member::
      :name: ``parameters``
      :type: (object)
      
      Descriptions for the address book created by registering this listener.
      
      .. api-member::
         :name: [``addressBookName``]
         :type: (string)
         
         The name of the created address book.
      
      
      .. api-member::
         :name: [``id``]
         :type: (string)
         
         The UID of the created address book. If several listeners have been added, the ``id`` allows to identify which address book initiated the search request. If not provided, a UID will be generated for you.
      
      
      .. api-member::
         :name: [``isSecure``]
         :type: (boolean)
         
         Whether the address book search queries are using encrypted protocols like HTTPS.
      
   

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
   :label: Expected return value of the listener function

   
   .. api-member::
      :type: array of :ref:`contacts.ContactProperties`
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`
