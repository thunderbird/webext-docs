.. container:: sticky-sidebar

  ≡ folders API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /overlay/developer-resources.rst

  ≡ Related information
  
  * :doc:`/how-to/eventListeners`

===========
folders API
===========

The folders API first appeared in Thunderbird 68 as a part of the
:doc:`accounts`. It was later moved here.

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`accountsFolders`

   Create, rename, or delete your mail account folders

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`accountsRead` is required to use ``messenger.folders.*``.

.. rst-class:: api-main-section

Functions
=========

.. _folders.copy:

copy(source, destination)
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Copies the given source folder into the given destination folder. Throws if the destination already contains a folder with the name of the source folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``source``
      :type: (:ref:`folders.MailFolderId`)
   
   
   .. api-member::
      :name: ``destination``
      :type: (:ref:`folders.MailFolderId`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`accountsFolders`

.. _folders.create:

create(destination, childName)
------------------------------

.. api-section-annotation-hack:: 

Creates a new subfolder in the specified folder or at the root of the specified account.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``destination``
      :type: (:ref:`folders.MailFolderId`)
   
   
   .. api-member::
      :name: ``childName``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`accountsFolders`

.. _folders.delete:

delete(folder)
--------------

.. api-section-annotation-hack:: 

Deletes a folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolderId`)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`accountsFolders`
   - :permission:`messagesDelete`

.. _folders.get:

get(folder, [includeSubFolders])
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Returns the specified folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolderId`)
   
   
   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)
      
      Specifies whether the returned :ref:`folders.MailFolder` object should include all its nested subfolders . Defaults to :value:`true`.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.getFolderCapabilities:

getFolderCapabilities(folder)
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Get capability information about a folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolderId`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`folders.MailFolderCapabilities`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.getFolderInfo:

getFolderInfo(folder)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Get additional information about a folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolderId`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`folders.MailFolderInfo`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.getParentFolders:

getParentFolders(folder, [includeSubFolders])
---------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Get all parent folders as a flat ordered array. The first array entry is the direct parent.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolderId`)
   
   
   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)
      
      Specifies whether the returned :ref:`folders.MailFolder` object for each parent folder should include its nested subfolders . Defaults to :value:`false`.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.getSubFolders:

getSubFolders(folder, [includeSubFolders])
------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Get the subfolders of the specified folder or account.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolderId`)
   
   
   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)
      
      Specifies whether the returned :ref:`folders.MailFolder` object for each direct subfolder should also include all its nested subfolders . Defaults to :value:`true`.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.markAsRead:

markAsRead(folder)
------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Marks all messages in a folder as read.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolderId`)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`accountsFolders`

.. _folders.move:

move(source, destination)
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Moves the given source folder into the given destination folder. Throws if the destination already contains a folder with the name of the source folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``source``
      :type: (:ref:`folders.MailFolderId`)
   
   
   .. api-member::
      :name: ``destination``
      :type: (:ref:`folders.MailFolderId`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`accountsFolders`

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
         :type: (:ref:`folders.MailFolderId`, optional)
         
         Limits the search to the folder with the specified id.
      
      
      .. api-member::
         :name: [``hasMessages``]
         :type: (boolean or :ref:`folders.QueryRange`, optional)
         
         Whether the folder (excluding subfolders) contains messages, or not. Supports to specify a :ref:`folders.QueryRange` (min/max) instead of a simple boolean value (none/some).
      
      
      .. api-member::
         :name: [``hasNewMessages``]
         :type: (boolean or :ref:`folders.QueryRange`, optional)
         
         Whether the folder (excluding subfolders) contains new messages, or not. Supports to specify a :ref:`folders.QueryRange` (min/max) instead of a simple boolean value (none/some).
      
      
      .. api-member::
         :name: [``hasSubFolders``]
         :type: (boolean or :ref:`folders.QueryRange`, optional)
         
         Whether the folder has subfolders, or not. Supports to specify a :ref:`folders.QueryRange` (min/max) instead of a simple boolean value (none/some).
      
      
      .. api-member::
         :name: [``hasUnreadMessages``]
         :type: (boolean or :ref:`folders.QueryRange`, optional)
         
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
         :name: [``isVirtual``]
         :type: (boolean, optional)
         
         Whether this folder is a virtual search folder, or not.
      
      
      .. api-member::
         :name: [``mostRecent``]
         :type: (boolean, optional)
         
         Whether the folder (excluding subfolders) has been used within the last month. The returned folders will be sorted by their recentness and limited to the most recent ones, which is controlled by the :value:`mail.folder_widget.max_recent` preference. A value of :value:`false` is ignored.
      
      
      .. api-member::
         :name: [``name``]
         :type: (:ref:`folders.RegularExpression` or string, optional)
         
         Return only folders whose name is matched by the provided string or regular expression.
      
      
      .. api-member::
         :name: [``path``]
         :type: (:ref:`folders.RegularExpression` or string, optional)
         
         Return only folders whose path is matched by the provided string or regular expression.
      
      
      .. api-member::
         :name: [``recent``]
         :type: (boolean, optional)
         
         Whether the folder (excluding subfolders) has been used within the last month, or not. The returned folders will be sorted by their recentness. Ignored if :value:`mostRecent` is specified.
      
      
      .. api-member::
         :name: [``specialUse``]
         :type: (array of :ref:`folders.MailFolderSpecialUse`, optional)
         
         Match only folders with the specified special use (folders have to match all specified uses).
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.rename:

rename(folder, newName)
-----------------------

.. api-section-annotation-hack:: 

Renames a folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolderId`)
   
   
   .. api-member::
      :name: ``newName``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`accountsFolders`

.. _folders.update:

update(folder, updateProperties)
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Updates properties of a folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolderId`)
   
   
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

   - :permission:`accountsRead`
   - :permission:`accountsFolders`

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
      :type: (:ref:`folders.MailFolder`)
   
   
   .. api-member::
      :name: ``copiedFolder``
      :type: (:ref:`folders.MailFolder`)
   

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
      :type: (:ref:`folders.MailFolder`)
   

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
      :type: (:ref:`folders.MailFolder`)
   

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
      :type: (:ref:`folders.MailFolder`)
   
   
   .. api-member::
      :name: ``folderInfo``
      :type: (:ref:`folders.MailFolderInfo`)
   

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
      :type: (:ref:`folders.MailFolder`)
   
   
   .. api-member::
      :name: ``movedFolder``
      :type: (:ref:`folders.MailFolder`)
   

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
      :type: (:ref:`folders.MailFolder`)
   
   
   .. api-member::
      :name: ``renamedFolder``
      :type: (:ref:`folders.MailFolder`)
   

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
      :type: (:ref:`folders.MailFolder`)
   
   
   .. api-member::
      :name: ``updatedFolder``
      :type: (:ref:`folders.MailFolder`)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Types
=====

.. _folders.MailFolder:

MailFolder
----------

.. api-section-annotation-hack:: 

An object describing a folder. The ``subFolders`` property is only included if requested.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``accountId``
      :type: (:ref:`accounts.MailAccountId`)
      
      The id of the account this folder belongs to.
   
   
   .. api-member::
      :name: ``path``
      :type: (string)
      
      Path to this folder in the account. Although paths look predictable, never guess a folder's path, as there are a number of reasons why it may not be what you think it is. Use :ref:`folders.getParentFolders` or :ref:`folders.getSubFolders` to obtain hierarchy information.
   
   
   .. api-member::
      :name: [``id``]
      :type: (:ref:`folders.MailFolderId`, optional)
      
      An identifier for the folder.
   
   
   .. api-member::
      :name: [``isFavorite``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 121]
      
      Whether this folder is a favorite folder.
   
   
   .. api-member::
      :name: [``isRoot``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 121]
      
      Whether this folder is a root folder.
   
   
   .. api-member::
      :name: [``isVirtual``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 121]
      
      Whether this folder is a virtual search folder.
   
   
   .. api-member::
      :name: [``name``]
      :type: (string, optional)
      
      The human-friendly name of this folder.
   
   
   .. api-member::
      :name: [``specialUse``]
      :type: (array of :ref:`folders.MailFolderSpecialUse`, optional)
      :annotation: -- [Added in TB 121]
      
      The special use of this folder. A folder can have multiple special uses.
   
   
   .. api-member::
      :name: [``subFolders``]
      :type: (array of :ref:`folders.MailFolder`, optional)
      :annotation: -- [Added in TB 74]
      
      Subfolders are only included if requested. They will be returned in the same order as used in Thunderbird's folder pane.
   

.. _folders.MailFolderCapabilities:

MailFolderCapabilities
----------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

An object containing capability information about a folder.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``canAddMessages``]
      :type: (boolean, optional)
      
      Whether this folder supports adding new messages.
   
   
   .. api-member::
      :name: [``canAddSubfolders``]
      :type: (boolean, optional)
      
      Whether this folder supports adding new subfolders.
   
   
   .. api-member::
      :name: [``canBeDeleted``]
      :type: (boolean, optional)
      
      Whether this folder can be deleted.
   
   
   .. api-member::
      :name: [``canBeRenamed``]
      :type: (boolean, optional)
      
      Whether this folder can be renamed.
   
   
   .. api-member::
      :name: [``canDeleteMessages``]
      :type: (boolean, optional)
      
      Whether this folder supports deleting messages.
   

.. _folders.MailFolderId:

MailFolderId
------------

.. api-section-annotation-hack:: 

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

   
   .. api-member::
      :name: [``lastUsed``]
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)
      :annotation: -- [Added in TB 121]
      
      Date the folder was last used (precision: seconds).
   
   
   .. api-member::
      :name: [``newMessageCount``]
      :type: (integer, optional)
      :annotation: -- [Added in TB 121]
      
      Number of new messages in this folder.
   
   
   .. api-member::
      :name: [``quota``]
      :type: (array of :ref:`folders.MailFolderQuota`, optional)
      :annotation: -- [Added in TB 121]
      
      Quota information, if available.
   
   
   .. api-member::
      :name: [``totalMessageCount``]
      :type: (integer, optional)
      
      Number of messages in this folder.
   
   
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

   
   .. api-member::
      :name: ``limit``
      :type: (integer)
      
      The maximum available quota.
   
   
   .. api-member::
      :name: ``type``
      :type: (`string`)
      
      The type of the quota as defined by RFC2087. A :value:`STORAGE` quota is constraining the available storage in bytes, a :value:`MESSAGE` quota is constraining the number of storable messages.
      
      Supported values:
      
      .. api-member::
         :name: :value:`STORAGE`
      
      .. api-member::
         :name: :value:`MESSAGE`
   
   
   .. api-member::
      :name: ``unused``
      :type: (integer)
      
      The currently unused quota.
   
   
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
   

.. _folders.QueryRange:

QueryRange
----------

.. api-section-annotation-hack:: 

An object defining a range.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``max``]
      :type: (integer, optional)
      
      The maximum value required to match the query.
   
   
   .. api-member::
      :name: [``min``]
      :type: (integer, optional)
      
      The minimum value required to match the query.
   

.. _folders.RegularExpression:

RegularExpression
-----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``regexp``
      :type: (string)
      
      A regular expression, for example :value:`^Projects \d{4}$`.
   
   
   .. api-member::
      :name: [``flags``]
      :type: (string, optional)
      
      Supported RegExp flags: :value:`i` = case insensitive, and/or one of :value:`u` = unicode support or :value:`v` = extended unicode support
   
