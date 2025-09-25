.. container:: sticky-sidebar

  ≡ addressBooks.provider API

  * `Permissions`_
  * `Events`_

  .. include:: /includes/developer-resources.rst

=========================
addressBooks.provider API
=========================

.. role:: permission

.. role:: value

.. role:: code

The address book provider API allows to add address books, which are not stored or cached by Thunderbird itself, but are handled completely by the extension. Address books created by the this API will forward all access requests to the WebExtension.

Possible use cases include:

So far, only the API for search-only address books has been implemented.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`addressBooks`

   Read and modify your address books and contacts

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``messenger.addressBooks.provider.*``.

.. rst-class:: api-main-section

Events
======

.. _addressBooks.provider.onSearchRequest:

onSearchRequest
---------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Registering this listener will create a read-only address book, similar to an LDAP address book. When selecting this address book, users will first see no contacts, but they can search for contacts, which will fire this event. Contacts returned by the listener callback will be displayed as contact cards in the address book. Several listeners can be registered, to create multiple address books.

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
      :type: (:ref:`addressBooks.provider.AddressBookNode`)

   .. api-member::
      :name: [``searchString``]
      :type: (string, optional)

      The search text that the user entered. Not available when invoked from the advanced address book search dialog.

   .. api-member::
      :name: [``query``]
      :type: (string, optional)

      The boolean query expression corresponding to the search.

.. api-header::
   :label: Expected return value of the listener function

   .. api-member::
      :type: object

      .. api-member::
         :name: ``isCompleteResult``
         :type: (boolean)
         :annotation: -- [Added in TB 142]

      .. api-member::
         :name: ``results``
         :type: (array of :ref:`addressBooks.provider.ContactProperties`)
         :annotation: -- [Added in TB 142]

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`
