.. container:: sticky-sidebar

  ≡ addressBooks.provider API

  * `Permissions`_
  * `Events`_

  .. include:: /_includes/developer-resources.rst

=========================
addressBooks.provider API
=========================

.. role:: permission

.. role:: value

.. role:: code

The address book provider API allows to add address books, which are not stored or cached by Thunderbird itself, but are handled completely by the extension. Address books created by the this API will forward all access requests to the WebExtension.

Possible use cases include:

 * Implementing a custom storage.
 * Implementing search-only address books that query a remote server.

So far, only the API for search-only address books has been implemented.

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

   The permission :permission:`addressBooks` is required to use ``messenger.addressBooks.provider.*``.

.. rst-class:: api-main-section

Events
======

.. _address^books.provider.on^search^request:

onSearchRequest
---------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Registering this listener will create a read-only address book, similar to an LDAP address book. When selecting this address book, users will first see no contacts, but they can search for contacts, which will fire this event. Contacts returned by the listener callback will be displayed as contact cards in the address book. Several listeners can be registered, to create multiple address books.

.. note::

   Ensure all listeners are registered at the top-level and use the synchronous pattern, otherwise the associated address books will be removed on background termination.

The event also fires for each registered listener (for each created read-only address book), when users type something into the mail composer's *To:* field, or into similar fields like the calendar meeting attendees field. Contacts returned by the listener callback will be added to the autocomplete results in the dropdown of that field.

Example:

.. code-block:: JavaScript

   messenger.addressBooks.provider.onSearchRequest.addListener(
     async (node, searchString, query) => {
       const response = await fetch(
         "https://people.acme.com/?query=" + searchString
       );
       const json = await response.json();
       return {
         isCompleteResult: true,
         // Return an array of ContactProperties as results.
         results: json.map(contact => ({
           DisplayName: contact.name,
           PrimaryEmail: contact.email,
         })),
       };
     },
     {
       addressBookName: "ACME employees",
       isSecure: true,
     }
   );

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
         :type: (string, optional)

         The name of the created address book. If not provided, the name of the extension is used.

      .. api-member::
         :name: [``id``]
         :type: (string, optional)

         The unique identifier of the created address book. If not provided, a unique identifier will be generated for you.

      .. api-member::
         :name: [``isSecure``]
         :type: (boolean, optional)

         Whether the address book search queries are using encrypted protocols like HTTPS.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``node``
      :type: (:ref:`address^books.^address^book^node`)

   .. api-member::
      :name: [``searchString``]
      :type: (string, optional)

      The search text that the user entered. Not available when invoked from the advanced address book search dialog.

   .. api-member::
      :name: [``query``]
      :type: (string, optional)

      The boolean query expression corresponding to the search.

      .. note::

         This parameter may change in future releases of Thunderbird.

.. api-header::
   :label: Expected return value of the listener function

   .. api-member::
      :type: object

      .. api-member::
         :name: ``isCompleteResult``
         :type: (boolean)
         :annotation: -- [Added in TB 140]

      .. api-member::
         :name: ``results``
         :type: (array of :ref:`address^books.contacts.^contact^properties`)
         :annotation: -- [Added in TB 140]

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`
