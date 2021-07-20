=========================
Changes in Thunderbird 91
=========================

accounts API
============

* :ref:`accounts.list`, :ref:`accounts.get` and :ref:`accounts.getDefault` now have an optional parameter ``includeFolders`` to specify if the returned :ref:`accounts.MailAccount` objects should populate the ``folders`` property. Defaults to ``true``.


addressbooks API
================

* added ``remote`` property to :ref:`addressbooks.AddressBookNode`


cloudFile API
=============

* added the ``tab`` parameter to :ref:`cloudFile.onFileDeleted`
* added the ``tab`` parameter to :ref:`cloudFile.onFileUpload`
* added the ``tab`` parameter to :ref:`cloudFile.onFileUploadAbort`


compose API
===========

* all attachment related functions and events now also require the :permission:`compose` permission.


contacts API
============

* added ``remote`` property to :ref:`contacts.ContactNode`
* second parameter to :ref:`contacts.quickSearch` can now be a qeuryInfo object instead of just a string, to define mored detailes query parameters


folders API
===========

* added new function :ref:`folders.getParentFolders` to get information about the current hierarchy level and parent folders
* added new function :ref:`folders.getSubFolders` to get information about subfolders
* the :ref:`folders.create` function can now create folders in the root of an account, by specifying an account instead of a folder as first parameter


identities API
==============

* added :ref:`identities_api` API (including create/delete/update functions and onCreated/onDeleted/onUpdated events)
* added ``signature`` and ``signatureIsPlainText`` to :ref:`identities.MailIdentity`


mailingLists API
================

* added ``remote`` property to :ref:`mailingLists.MailingListNode`


mailTabs
========

* the :ref:`mailTabs.MailTab` object now includes a ``viewType`` property, supporting the values ``ungrouped``, ``groupedByThread`` and ``groupedBySortType``
* the :ref:`mailTabs.update` function allows to set the new ``viewType`` property


messages
========

* :ref:`messages.query` now searches all messages and not only the indexed ones 
* added support for negative tag search to :ref:`messages.query`
* added ``includeSubFolders`` to search folders recursivly with :ref:`messages.query`
* added :ref:`messages.onUpdated`
* added :ref:`messages.onMoved`
* added :ref:`messages.onCopied`
* added :ref:`messages.onDeleted`
* added the :permission:`messagesDelete` permission to guard :ref:`messages.delete`
