==================================
Changes up to Thunderbird 121 Beta
==================================

--------------------
Thunderbird 117 Beta
--------------------

messages API
============
* Added the optional ``data_format`` parameter to :ref:`messages.getRaw` to request the message as a DOM ``File`` object.

--------------------
Thunderbird 120 Beta
--------------------

messages API
============
* Added :ref:`messages.abortList` to  terminate any process currently still adding messages to the given list.
* Added the ``messagesPerPage`` property to the ``queryInfo`` parameter of :ref:`messages.query`, to allow queries to override the default size of message pages.  See :doc:`../how-to/messageLists` for more information.
* Added the ``autoPaginationTimeout`` property to the ``queryInfo`` parameter of :ref:`messages.query`, to allow queries to override the default pagination timeout of ``1000ms``. Long running queries will return pages even if they have not reached the nominal page size, to allow extensions to work with the already received results or terminate the list (and the associated query) using :ref:`messages.abortList`.
* Added the ``returnMessageListId`` property to the ``queryInfo`` parameter of :ref:`messages.query`, to force queries to immediately return the id of the list associated with the query, instead of waiting for at least one found message and returning the first page.

--------------------
Thunderbird 121 Beta
--------------------

accounts API
============

The deprecated functions ``accounts.getDefaultIdentity()`` and ``accounts.setDefaultIdentity()`` have been removed.

folders API
===========

The folders API has been changed to use a :ref:`folders.MailFolderId` instead of :ref:`folders.MailFolder`, to specify a folder. The nature of the id will change in a future release.

* Added :ref:`folders.get` to retrieve a folder identified by the given :ref:`folders.MailFolderId`.
* Added :ref:`folders.getFolderCapabilities` to retrieve capabilitiy information about a given folder.
* Added :ref:`folders.markAsRead` to mark all messages in a folder as read.
* Added :ref:`folders.query` to query for folders with specified properties.
* Added :ref:`folders.update` to update properties of the given folder.
* Added the :ref:`folders.onUpdated` event.
* Added ``isVirtual``, ``isRoot`` and ``isFavorite`` members to the :ref:`folders.MailFolder` type.
* Added ``lastUsed``, ``newMessageCount`` and ``quota`` members to the :ref:`folders.MailFolderInfo` type.
* The ``type`` member of the :ref:`folders.MailFolder` type has been deprecated. It was replaced by the array member ``specialUse``, allowing folders to have multiple special uses.
* The ``favorite`` member of the :ref:`folders.MailFolderInfo` type has been deprecated. It was replaced by the ``isFavorite`` property of the :ref:`folders.MailFolder` type.

mailTabs API
============
* Added :ref:`mailTabs.create`, to create a new mail tab with a specified folder.
* Added :ref:`mailTabs.getListedMessages`, to retrieve the messages currently being listed in the specified tab, honoring sort order and filters.
* The ``displayedFolder`` property of the :ref:`mailTabs.MailTabProperties` parameter used in various functions needs to use a :ref:`folders.MailFolderId` instead of :ref:`folders.MailFolder`, to specify a folder.


messages API
============
* Added the ``accountId``, ``folderId``, ``junk``, ``junkScore``, ``new`` and ``size`` properties to the ``queryInfo`` parameter of :ref:`messages.query`, to query for messages with the given properties.
* Support
* Added the ability to :ref:`messages.query` for a range instead of a fixed value for ``attachment``, ``junkScore`` and ``size``.
* Added the ``monitorAllFolders`` parameter to the :ref:`messages.onNewMailReceived` event, to allow extensions to listen for new messages in all folders, not just in inbox folders.
* The functions :ref:`messages.list`, :ref:`messages.move`, :ref:`messages.copy` and :ref:`messages.import` need to use a :ref:`folders.MailFolderId` instead of :ref:`folders.MailFolder`, to specify a folder.

messages.tags API
=================

All tag related functions have been moved into its own :ref:`messages.tags_api` namespace.

* Added :ref:`messages.tags.list` function, to list tags.
* Added :ref:`messages.tags.create` function, to create new tags.
* Added :ref:`messages.tags.update` function, to update tags.
* Added :ref:`messages.tags.delete` function, to delete tags.

The former functions ``messages.listTags()``, ``messages.createTag()``, ``messages.updateTag()`` and ``messages.deleteTag()`` have been removed.
