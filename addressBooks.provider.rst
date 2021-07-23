.. _addressBooks.provider_api:

=====================
addressBooks.provider
=====================

You want to add an address book to Thunderbird. Before you start to code, please consider which API you need, because there are two completely different approaches to do add address books to Thunderbird. They each come from opposite directions.

If your add-on wants to add and syncronize an address book with a server, and you want the contacts to be cached locally, so that the address book behaves like a built-in address book, you should not use `addressBooks.provider`, but you can simply use the `addressBooks` and `contacts` APIs:
```
let myAddressBook = messenger.addressBooks.create({ name: 'Kontacts' });
let newContact = messenger.contacts.create(myAddressBook, null, { displayName: 'Bugs Bunny' });
```
and listen to modifications with `messenger.contacts.onUpdated()` etc.. This will create a local address book, just like the built-in address books of Thunderbird, let you push and updates the contacts, and notify you of changes that the user made, so that you can write them back to the server. In this case, you do not need `addressBooks.provider`.

However, in some exceptional cases, you do *not* want the contacts to be cached locally, or you want to re-implement the storage. This API exists for these cases. So far, only the API for search-only address books is implemented.

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

Creates a read-only addressbook that fires this event when searching for a contact, and your code can determine the contacts that should be shown as a result of that search.

When the user types a name or address in the mail composer's "To:" field, or similar fields like the calendar meeting attendees, this event will fire and allow you to make a query on a server or third party local datasource, and return the matching contacts in that third party source. These contacts will then be displayed as autocomplete result in the dropdown of the email field.

This API will also create a type of address book similar to LDAP address books, which appears in the address book window. When selecting this address book, the user will first see no contacts, but he can search for them, which will fire this same event, and the results that you return here will be displayed as contact cards in the address book.

When you register this event, the address book will be created internally. The name that you pass here in `extraParameters` is what the user will see as name of the address book. If need be, you can register several times, to create multiple address books.

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
