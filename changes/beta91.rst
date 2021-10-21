=========================
Changes in Thunderbird 91
=========================

accounts API
============

* :ref:`accounts.list`, :ref:`accounts.get` and :ref:`accounts.getDefault` now have an optional parameter ``includeFolders`` to specify if the returned :ref:`accounts.MailAccount` objects should populate the ``folders`` property. Defaults to ``true``


addressbooks API
================

* added ``remote`` property to :ref:`addressbooks.AddressBookNode`


browserAction API
=================

* added support for the ``tabstoolbar`` location, usable in the ``default_area`` manifest key


cloudFile API
=============

* added the ``tab`` parameter to :ref:`cloudFile.onFileDeleted`
* added the ``tab`` parameter to :ref:`cloudFile.onFileUpload`
* added the ``tab`` parameter to :ref:`cloudFile.onFileUploadAbort`


compose API
===========

* all attachment related functions and events now also require the :permission:`compose` permission


contacts API
============

* added ``remote`` property to :ref:`contacts.ContactNode`
* second parameter to :ref:`contacts.quickSearch` can now be a qeuryInfo object instead of just a string, to define mored detailes query parameters


folders API
===========

* :ref:`folders.delete` now requires the :permission:`messagesDelete` permission
* added new function :ref:`folders.getParentFolders` to get information about the current hierarchy level and parent folders
* added new function :ref:`folders.getSubFolders` to get information about subfolders
* the :ref:`folders.create` function can now create folders in the root of an account, by specifying an account instead of a folder as first parameter
* added :ref:`folders.move` function
* added :ref:`folders.copy` function
* added :ref:`folders.getFolderInfo` function and :ref:`folders.MailFolderInfo` type to obtain additional folder information like ``totalMessageCounts`` or ``unreadMessageCounts``
* added :ref:`folders.onCreated` event
* added :ref:`folders.onRenamed` event
* added :ref:`folders.onMoved` event
* added :ref:`folders.onCopied` event
* added :ref:`folders.onDeleted` event
* added :ref:`folders.onFolderInfoChanged` event

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

tabs API
========

* added ``type`` property to :ref:`tabs.Tab`, supporting ``addressBook``, ``calendar``, ``calendarEvent``, ``calendarTask``, ``chat``, ``content``, ``mail``, ``messageCompose``, ``messageDisplay``, ``special`` and ``tasks``
* added ``type`` as supported property of the ``queryInfo`` parameter of :ref:`tabs.query`
