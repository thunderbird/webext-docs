.. container:: sticky-sidebar

  ≡ folders API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_
  * `Properties`_

  .. include:: /includes/developer-resources.rst

===========
folders API
===========

.. role:: permission

.. role:: value

.. role:: code

The folders API allows to access and manage the user's message folders.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`accountsFolders`

   Create, rename, or delete your mail account folders

.. api-member::
   :name: :permission:`accountsRead`

   See your mail accounts, their identities and their folders

.. api-member::
   :name: :permission:`messagesDelete`

   Permanently delete your email messages

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`accountsRead` is required to use ``messenger.folders.*``.

.. rst-class:: api-main-section

Functions
=========

.. _folders.copy:

copy(sourceFolderId, destinationFolderId)
-----------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Copies the given source folder into the given destination folder. Throws if the destination already contains a folder with the name of the source folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``sourceFolderId``
      :type: (:ref:`MailFolderId`)

   .. api-member::
      :name: ``destinationFolderId``
      :type: (:ref:`MailFolderId`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`MailFolder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`

.. _folders.create:

create(folderId, childName)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 68]

Creates a new subfolder in the specified folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`MailFolderId`)

   .. api-member::
      :name: ``childName``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`MailFolder`
      :annotation: -- [Added in TB 91]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`

.. _folders.delete:

delete(folderId)
----------------

.. api-section-annotation-hack:: -- [Added in TB 68]

Deletes a folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`MailFolderId`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`
   - :permission:`messagesDelete`

.. _folders.get:

get(folderId, [includeSubFolders])
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Returns the specified folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`MailFolderId`)

   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)

      Specifies whether the returned :ref:`folders.MailFolder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`MailFolder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.getFolderCapabilities:

getFolderCapabilities(folderId)
-------------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Get capability information about a folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`MailFolderId`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`MailFolderCapabilities`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.getFolderInfo:

getFolderInfo(folderId)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Get additional information about a folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`MailFolderId`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`MailFolderInfo`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.getParentFolders:

getParentFolders(folderId, [includeSubFolders])
-----------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Get all parent folders as a flat ordered array. The first array entry is the direct parent.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`MailFolderId`)

   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)

      Specifies whether each returned parent :ref:`folders.MailFolder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`MailFolder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.getSubFolders:

getSubFolders(folderId, [includeSubFolders])
--------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Get the subfolders of the specified folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`MailFolderId`)

   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)

      Specifies whether each returned direct child :ref:`folders.MailFolder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`MailFolder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.getTagFolder:

getTagFolder(key)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Get one of the special virtual tag folders, which are virtual search folders and group messages from all mail accounts based on their tags. Throws if the requested folder does not exist.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``key``
      :type: (string)

      The tag key of the requested folder. See :ref:`messages.tags.list(`) for the available tags. Throws when specifying an invalid tag key.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`MailFolder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.getUnifiedFolder:

getUnifiedFolder(type, [includeSubFolders])
-------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Get one of the special unified mailbox folders, which are virtual search folders and return the content from all mail accounts. Throws if the requested folder does not exist.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``type``
      :type: (`string`)

      The requested unified mailbox folder type.

      Supported values:

      .. api-member::
         :name: :value:`inbox`

      .. api-member::
         :name: :value:`drafts`

      .. api-member::
         :name: :value:`sent`

      .. api-member::
         :name: :value:`trash`

      .. api-member::
         :name: :value:`templates`

      .. api-member::
         :name: :value:`archives`

      .. api-member::
         :name: :value:`junk`

   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)

      Specifies whether the returned :ref:`folders.MailFolder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`MailFolder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.markAsRead:

markAsRead(folderId)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Marks all messages in a folder as read.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`MailFolderId`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`

.. _folders.move:

move(sourceFolderId, destinationFolderId)
-----------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Moves the given source folder into the given destination folder. Throws if the destination already contains a folder with the name of the source folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``sourceFolderId``
      :type: (:ref:`MailFolderId`)

   .. api-member::
      :name: ``destinationFolderId``
      :type: (:ref:`MailFolderId`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`MailFolder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`

.. _folders.query:

query([queryInfo])
------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Gets folders that match the specified properties, or all folders if no properties are specified.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``queryInfo``]
      :type: (object, optional)

      .. api-member::
         :name: [``accountId``]
         :type: (:ref:`accounts.MailAccountId`, optional)

         Limits the search to folders of the account with the specified id.

      .. api-member::
         :name: [``canAddMessages``]
         :type: (boolean, optional)

         Whether the folder supports adding new messages, or not.

      .. api-member::
         :name: [``canAddSubfolders``]
         :type: (boolean, optional)

         Whether the folder supports adding new subfolders, or not.

      .. api-member::
         :name: [``canBeDeleted``]
         :type: (boolean, optional)

         Whether the folder can be deleted, or not.

      .. api-member::
         :name: [``canBeRenamed``]
         :type: (boolean, optional)

         Whether the folder can be renamed, or not.

      .. api-member::
         :name: [``canDeleteMessages``]
         :type: (boolean, optional)

         Whether the folder supports deleting messages, or not.

      .. api-member::
         :name: [``folderId``]
         :type: (:ref:`MailFolderId`, optional)

         Limits the search to the folder with the specified id.

      .. api-member::
         :name: [``hasMessages``]
         :type: (boolean or :ref:`QueryRange`, optional)

         Whether the folder (excluding subfolders) contains messages, or not. Supports to specify a :ref:`folders.QueryRange` (min/max) instead of a simple boolean value (none/some).

      .. api-member::
         :name: [``hasNewMessages``]
         :type: (boolean or :ref:`QueryRange`, optional)

         Whether the folder (excluding subfolders) contains new messages, or not. Supports to specify a :ref:`folders.QueryRange` (min/max) instead of a simple boolean value (none/some).

      .. api-member::
         :name: [``hasSubFolders``]
         :type: (boolean or :ref:`QueryRange`, optional)

         Whether the folder has subfolders, or not. Supports to specify a :ref:`folders.QueryRange` (min/max) instead of a simple boolean value (none/some).

      .. api-member::
         :name: [``hasUnreadMessages``]
         :type: (boolean or :ref:`QueryRange`, optional)

         Whether the folder (excluding subfolders) contains unread messages, or not. Supports to specify a :ref:`folders.QueryRange` (min/max) instead of a simple boolean value (none/some).

      .. api-member::
         :name: [``isFavorite``]
         :type: (boolean, optional)

         Whether the folder is a favorite folder, or not.

      .. api-member::
         :name: [``isRoot``]
         :type: (boolean, optional)

         Whether the folder is a root folder, or not.

      .. api-member::
         :name: [``isTag``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 127]

         Whether the folder is a virtual tag folder, or not. Virtual tag folders are always skipped, unless this property is set to :value:`true`

      .. api-member::
         :name: [``isUnified``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 127]

         Whether the folder is a unified mailbox folder, or not. Unified mailbox folders are always skipped, unless this property is set to :value:`true`

      .. api-member::
         :name: [``isVirtual``]
         :type: (boolean, optional)

         Whether the folder is a virtual search folder, or not.

      .. api-member::
         :name: [``lastUsed``]
         :type: (:ref:`QueryDateRange`, optional)
         :annotation: -- [Added in TB 137]

         Date the folder was last used (folder was accessed, user moved or copied messages into the folder or folder received new messages).

      .. api-member::
         :name: [``lastUsedAsDestination``]
         :type: (:ref:`QueryDateRange`, optional)
         :annotation: -- [Added in TB 137]

         Date the folder was last used as a destination (user moved or copied messages into the folder).

      .. api-member::
         :name: [``limit``]
         :type: (integer, optional)
         :annotation: -- [Added in TB 122]

         Limits the number of returned folders. If used together with :value:`recent`, supports being set to :ref:`folders.DEFAULT_MOST_RECENT_LIMIT`

      .. api-member::
         :name: [``name``]
         :type: (:ref:`RegularExpression` or string, optional)

         Return only folders whose name is matched by the provided string or regular expression.

      .. api-member::
         :name: [``path``]
         :type: (:ref:`RegularExpression` or string, optional)

         Return only folders whose path is matched by the provided string or regular expression.

      .. api-member::
         :name: [``recent``]
         :type: (boolean, optional) **Deprecated.**

         Whether the folder (excluding subfolders) has been used within the last month, or not. The returned folders will be sorted by :value:`lastUsed`.

      .. api-member::
         :name: [``sort``]
         :type: (`string`, optional)
         :annotation: -- [Added in TB 137]

         The sort order of the returned folders. If not specified, folders will be sorted by :value:`path`. Sorting by :value:`name` is case-insensitive.

         Supported values:

         .. api-member::
            :name: :value:`lastUsed`

         .. api-member::
            :name: :value:`lastUsedAsDestination`

         .. api-member::
            :name: :value:`name`

         .. api-member::
            :name: :value:`path`

      .. api-member::
         :name: [``specialUse``]
         :type: (array of :ref:`MailFolderSpecialUse`, optional)

         Match only folders with the specified special use (folders have to match all specified uses).

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`MailFolder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.rename:

rename(folderId, newName)
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 68]

Renames a folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`MailFolderId`)

   .. api-member::
      :name: ``newName``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`MailFolder`
      :annotation: -- [Added in TB 91]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`

.. _folders.update:

update(folderId, updateProperties)
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Updates properties of a folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`MailFolderId`)

   .. api-member::
      :name: ``updateProperties``
      :type: (object)

      The properties to update.

      .. api-member::
         :name: [``isFavorite``]
         :type: (boolean, optional)

         Sets or clears the favorite status.

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`

.. rst-class:: api-main-section

Events
======

.. _folders.onCopied:

onCopied
--------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when a folder has been copied.

.. api-header::
   :label: Parameters for onCopied.addListener(listener)

   .. api-member::
      :name: ``listener(originalFolder, copiedFolder)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``originalFolder``
      :type: (:ref:`MailFolder`)

   .. api-member::
      :name: ``copiedFolder``
      :type: (:ref:`MailFolder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.onCreated:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when a folder has been created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. api-member::
      :name: ``listener(createdFolder)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``createdFolder``
      :type: (:ref:`MailFolder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.onDeleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when a folder has been deleted.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. api-member::
      :name: ``listener(deletedFolder)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``deletedFolder``
      :type: (:ref:`MailFolder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.onFolderInfoChanged:

onFolderInfoChanged
-------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when certain information of a folder have changed. Bursts of message count changes are collapsed to a single event.

.. api-header::
   :label: Parameters for onFolderInfoChanged.addListener(listener)

   .. api-member::
      :name: ``listener(folder, folderInfo)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``folder``
      :type: (:ref:`MailFolder`)

   .. api-member::
      :name: ``folderInfo``
      :type: (:ref:`MailFolderInfo`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.onMoved:

onMoved
-------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when a folder has been moved.

.. api-header::
   :label: Parameters for onMoved.addListener(listener)

   .. api-member::
      :name: ``listener(originalFolder, movedFolder)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``originalFolder``
      :type: (:ref:`MailFolder`)

   .. api-member::
      :name: ``movedFolder``
      :type: (:ref:`MailFolder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.onRenamed:

onRenamed
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when a folder has been renamed.

.. api-header::
   :label: Parameters for onRenamed.addListener(listener)

   .. api-member::
      :name: ``listener(originalFolder, renamedFolder)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``originalFolder``
      :type: (:ref:`MailFolder`)

   .. api-member::
      :name: ``renamedFolder``
      :type: (:ref:`MailFolder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 121]

Fired when properties of a folder have changed (:value:`specialUse` and :value:`isFavorite`).

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. api-member::
      :name: ``listener(originalFolder, updatedFolder)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``originalFolder``
      :type: (:ref:`MailFolder`)

   .. api-member::
      :name: ``updatedFolder``
      :type: (:ref:`MailFolder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Types
=====

.. _folders.MailFolder:

MailFolder
----------

.. api-section-annotation-hack:: -- [Added in TB 68]

An object describing a folder.

.. api-header::
   :label: object

   .. _folders.MailFolder.id:

   .. api-member::
      :name: ``id``
      :type: (:ref:`MailFolderId`)
      :annotation: -- [Added in TB 121]

      An identifier for the folder.

   .. _folders.MailFolder.isFavorite:

   .. api-member::
      :name: ``isFavorite``
      :type: (boolean)
      :annotation: -- [Added in TB 121]

      Whether this folder is a favorite folder.

   .. _folders.MailFolder.isRoot:

   .. api-member::
      :name: ``isRoot``
      :type: (boolean)
      :annotation: -- [Added in TB 121]

      Whether this folder is a root folder.

   .. _folders.MailFolder.isTag:

   .. api-member::
      :name: ``isTag``
      :type: (boolean)
      :annotation: -- [Added in TB 127]

      Whether this folder is a virtual tag folder.

   .. _folders.MailFolder.isUnified:

   .. api-member::
      :name: ``isUnified``
      :type: (boolean)
      :annotation: -- [Added in TB 127]

      Whether this folder is a unified mailbox folder.

   .. _folders.MailFolder.isVirtual:

   .. api-member::
      :name: ``isVirtual``
      :type: (boolean)
      :annotation: -- [Added in TB 121]

      Whether this folder is a virtual search folder.

   .. _folders.MailFolder.name:

   .. api-member::
      :name: ``name``
      :type: (string)

      The human-friendly name of this folder.

   .. _folders.MailFolder.path:

   .. api-member::
      :name: ``path``
      :type: (string)

      Path to this folder in the account. Although paths look predictable, never guess a folder's path, as there are a number of reasons why it may not be what you think it is. Use :ref:`folders.getParentFolders` or :ref:`folders.getSubFolders` to obtain hierarchy information.

   .. _folders.MailFolder.specialUse:

   .. api-member::
      :name: ``specialUse``
      :type: (array of :ref:`MailFolderSpecialUse`)
      :annotation: -- [Added in TB 121]

      The special use of this folder. A folder can have multiple special uses.

   .. _folders.MailFolder.accountId:

   .. api-member::
      :name: [``accountId``]
      :type: (:ref:`accounts.MailAccountId`, optional)

      The id of the account this folder belongs to. This property is optional and not available for unified mailbox folders or virtual tag folders.

   .. _folders.MailFolder.subFolders:

   .. api-member::
      :name: [``subFolders``]
      :type: (array of :ref:`MailFolder`, optional)
      :annotation: -- [Added in TB 74]

      Subfolders of this folder. This property is optional and only present if the inclusion of subfolders had been requested. The folders will be returned in the same order as used in Thunderbird's folder pane.

.. _folders.MailFolderCapabilities:

MailFolderCapabilities
----------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

An object containing capability information about a folder.

.. api-header::
   :label: object

   .. _folders.MailFolderCapabilities.canAddMessages:

   .. api-member::
      :name: [``canAddMessages``]
      :type: (boolean, optional)

      Whether this folder supports adding new messages.

   .. _folders.MailFolderCapabilities.canAddSubfolders:

   .. api-member::
      :name: [``canAddSubfolders``]
      :type: (boolean, optional)

      Whether this folder supports adding new subfolders.

   .. _folders.MailFolderCapabilities.canBeDeleted:

   .. api-member::
      :name: [``canBeDeleted``]
      :type: (boolean, optional)

      Whether this folder can be deleted.

   .. _folders.MailFolderCapabilities.canBeRenamed:

   .. api-member::
      :name: [``canBeRenamed``]
      :type: (boolean, optional)

      Whether this folder can be renamed.

   .. _folders.MailFolderCapabilities.canDeleteMessages:

   .. api-member::
      :name: [``canDeleteMessages``]
      :type: (boolean, optional)

      Whether this folder supports deleting messages.

.. _folders.MailFolderId:

MailFolderId
------------

.. api-section-annotation-hack:: -- [Added in TB 121]

A unique id representing a :ref:`folders.MailFolder` throughout a session. Renaming or moving a folder will invalidate its id.

.. api-header::
   :label: string

.. _folders.MailFolderInfo:

MailFolderInfo
--------------

.. api-section-annotation-hack:: -- [Added in TB 91]

An object containing additional information about a folder.

.. api-header::
   :label: object

   .. _folders.MailFolderInfo.lastUsed:

   .. api-member::
      :name: [``lastUsed``]
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)
      :annotation: -- [Added in TB 121]

      Date the folder was last used. It is updated every time the folder was accessed, when the user moved or copied messages into the folder and when the folder received new messages. (precision: seconds).

   .. _folders.MailFolderInfo.lastUsedAsDestination:

   .. api-member::
      :name: [``lastUsedAsDestination``]
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)
      :annotation: -- [Added in TB 137]

      Date the folder was last used as a destination. It is updated every time the user moved or copied messages into the folder. (precision: seconds).

   .. _folders.MailFolderInfo.newMessageCount:

   .. api-member::
      :name: [``newMessageCount``]
      :type: (integer, optional)
      :annotation: -- [Added in TB 121]

      Number of new messages in this folder.

   .. _folders.MailFolderInfo.quota:

   .. api-member::
      :name: [``quota``]
      :type: (array of :ref:`MailFolderQuota`, optional)
      :annotation: -- [Added in TB 121]

      Quota information, if available.

   .. _folders.MailFolderInfo.totalMessageCount:

   .. api-member::
      :name: [``totalMessageCount``]
      :type: (integer, optional)

      Number of messages in this folder.

   .. _folders.MailFolderInfo.unreadMessageCount:

   .. api-member::
      :name: [``unreadMessageCount``]
      :type: (integer, optional)

      Number of unread messages in this folder.

.. _folders.MailFolderQuota:

MailFolderQuota
---------------

.. api-section-annotation-hack:: -- [Added in TB 121]

An object containing quota information.

.. api-header::
   :label: object

   .. _folders.MailFolderQuota.limit:

   .. api-member::
      :name: ``limit``
      :type: (integer)

      The maximum available quota.

   .. _folders.MailFolderQuota.type:

   .. api-member::
      :name: ``type``
      :type: (`string`)

      The type of the quota as defined by RFC 2087. A :value:`STORAGE` quota is constraining the available storage in bytes, a :value:`MESSAGE` quota is constraining the number of storable messages.

      Supported values:

      .. api-member::
         :name: :value:`STORAGE`

      .. api-member::
         :name: :value:`MESSAGE`

   .. _folders.MailFolderQuota.unused:

   .. api-member::
      :name: ``unused``
      :type: (integer)

      The currently unused quota.

   .. _folders.MailFolderQuota.used:

   .. api-member::
      :name: ``used``
      :type: (integer)

      The currently used quota.

.. _folders.MailFolderSpecialUse:

MailFolderSpecialUse
--------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Supported values for the special use of a folder.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`inbox`

         .. api-member::
            :name: :value:`drafts`

         .. api-member::
            :name: :value:`sent`

         .. api-member::
            :name: :value:`trash`

         .. api-member::
            :name: :value:`templates`

         .. api-member::
            :name: :value:`archives`

         .. api-member::
            :name: :value:`junk`

         .. api-member::
            :name: :value:`outbox`

.. _folders.QueryDateRange:

QueryDateRange
--------------

.. api-section-annotation-hack:: -- [Added in TB 137]

An object defining a range for a date value to be used in queries.

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. api-member::
            :name: ``recent``
            :type: (boolean)

            Whether the date must be considered to be recent by Thunderbird (within the last month) or not, to match the query.

OR

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. api-member::
            :name: [``after``]
            :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)

            The minimum date required to match the query.

         .. api-member::
            :name: [``before``]
            :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)

            The maximum date required to match the query.

.. _folders.QueryRange:

QueryRange
----------

.. api-section-annotation-hack:: -- [Added in TB 121]

An object defining a range for an integer value to be used in queries.

.. api-header::
   :label: object

   .. _folders.QueryRange.max:

   .. api-member::
      :name: [``max``]
      :type: (integer, optional)

      The maximum value required to match the query.

   .. _folders.QueryRange.min:

   .. api-member::
      :name: [``min``]
      :type: (integer, optional)

      The minimum value required to match the query.

.. _folders.RegularExpression:

RegularExpression
-----------------

.. api-section-annotation-hack:: -- [Added in TB 121]

.. api-header::
   :label: object

   .. _folders.RegularExpression.regexp:

   .. api-member::
      :name: ``regexp``
      :type: (string)

      A regular expression, for example :value:`^Projects \\d{4}$`.

   .. _folders.RegularExpression.flags:

   .. api-member::
      :name: [``flags``]
      :type: (string, optional)

      Supported RegExp flags: :value:`i` = case insensitive, and/or one of :value:`u` = unicode support or :value:`v` = extended unicode support

.. rst-class:: api-main-section

Properties
==========

.. _folders.DEFAULT_MOST_RECENT_LIMIT:

DEFAULT_MOST_RECENT_LIMIT
-------------------------

.. api-section-annotation-hack:: 

The number of most recent folders used in Thunderbird's UI. Controlled by the :value:`mail.folder_widget.max_recent` preference.
