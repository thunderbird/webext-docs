.. _addressBooks.provider_api:

=====================
addressBooks.provider
=====================

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

onSearchRequest(node, [searchString], [query])
----------------------------------------------

.. api-section-annotation-hack:: 

Use this API when you want to allow the user to search a third-party address book, but you do not want to cache the entire address book locally.

Adding a `SearchRequest` listener creates a read-only address book that fires this event when the user searches for a contact, and your code can determine the contacts that should be shown as a result of that search.

When the user types a name in the mail composer's "To:" field, or similar fields like the calendar meeting attendees, this event will fire and allow you to make a query on a server, or third-party local datasource, and return the matching contacts in that third-party source. These contacts will then be displayed as autocomplete result in the dropdown of the email field.

This API will also create a type of address book in the address book window, similar to LDAP address books. When selecting this address book, the user will first see no contacts, but he can search for them, which will fire this same event, and the results that you return here will be displayed as contact cards in the address book.

When you register this event, the address book will be created internally. The name that you pass in `extraParameters` is what the user will see as name of the address book. You can register several listeners, to create multiple address books.

Sample implementation:
```
messenger.addressBooks.onSearchRequest.addListener(async (ab, searchString) => {
  let response = await fetch("https://people.example.com/?query=" + searchString);
  // return [ { DisplayName: "Koyote", PrimaryEmail: "koyote@example.com" }, ... ];
  return response.json.map(contact => { DisplayName: contact.name, PrimaryEmail: contact.email });
}, {
 dirName: "ACME employees",
 isSecure: true,
});
```

Note: This event may change in future releases of Thunderbird.

TODO: Move this
Parameters of `addListener()`:
`extraParameters` contains an object with:
* `addressBookName`: The name of the address book that the end user will see.
* `isSecure`: True, if you use encrypted protocols like HTTPS, or no server. False, if you use HTTP or other unencrypted protocols.
* `id`: (Optional) The UID of the address book. If you add several listeners, that allows you to identify which address book the search event came from. If not passed, an UID will be generated for you.

.. api-header::
   :label: Parameters for event listeners

   
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
