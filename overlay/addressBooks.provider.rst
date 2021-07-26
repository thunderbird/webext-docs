=====================
addressBooks.provider
=====================

The :ref:`addressBooks.provider_api` API first appeared in Thunderbird 90. It allows to add address books, which should not be stored or cached locally by Thunderbird itself, but be handled completely by the extension. Such address books are fundamentally different to standard address books added by the :ref:`addressBooks_api` API.

Consider an extension that synchronizes an address book with a server, which should store its contacts locally and behave like a built-in address book. Such an extension should use the :ref:`addressBooks_api` and the :ref:`contacts_api` APIs as follows:

.. code-block:: javascript

  let myAddressBook = messenger.addressBooks.create({ name: 'RemoteContacts' });
  let newContact = messenger.contacts.create(myAddressBook, null, { displayName: 'Bugs Bunny' });

The extension can listen to modifications with :ref:`contacts.onUpdated` etc. to keep the local copy of the address book in sync with the server.

However, in some exceptional cases, Thunderbird itself should *not* store or cache address book and its contacts locally. This API exists for these cases and it will redirect access requests to such address books and their contacts to the extension. Possible use cases:
* implement a custom storage
* implement search-only address books querying a remote server

So far, only the API for search-only address books is implemented.
