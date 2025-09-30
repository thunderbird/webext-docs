.. container:: sticky-sidebar

  ≡ folders API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

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

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`accountsFolders`

   Create, rename, or delete your mail account folders.

.. api-member::
   :name: :permission:`accountsRead`

   See your mail accounts, their identities and their folders.

.. api-member::
   :name: :permission:`messagesDelete`

   Permanently delete your email messages.

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
      :type: (:ref:`folders.^mail^folder^id`)

   .. api-member::
      :name: ``destinationFolderId``
      :type: (:ref:`folders.^mail^folder^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`folders.^mail^folder`

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
      :type: (:ref:`folders.^mail^folder^id`)

   .. api-member::
      :name: ``childName``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`folders.^mail^folder`
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
      :type: (:ref:`folders.^mail^folder^id`)

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
      :type: (:ref:`folders.^mail^folder^id`)

   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)

      Specifies whether the returned :ref:`folders.^mail^folder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^folder^capabilities:

getFolderCapabilities(folderId)
-------------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Get capability information about a folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`folders.^mail^folder^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`folders.^mail^folder^capabilities`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^folder^info:

getFolderInfo(folderId)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Get additional information about a folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`folders.^mail^folder^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`folders.^mail^folder^info`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^parent^folders:

getParentFolders(folderId, [includeSubFolders])
-----------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Get all parent folders as a flat ordered array. The first array entry is the direct parent.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`folders.^mail^folder^id`)

   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)

      Specifies whether each returned parent :ref:`folders.^mail^folder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^sub^folders:

getSubFolders(folderId, [includeSubFolders])
--------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Get the subfolders of the specified folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`folders.^mail^folder^id`)

   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)

      Specifies whether each returned direct child :ref:`folders.^mail^folder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^tag^folder:

getTagFolder(key)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Get one of the special virtual tag folders, which are virtual search folders and group messages from all mail accounts based on their tags. Throws if the requested folder does not exist.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``key``
      :type: (string)

      The tag key of the requested folder. See :ref:`messages.tags.list` for the available tags. Throws when specifying an invalid tag key.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^unified^folder:

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
         :name: :value:`archives`

      .. api-member::
         :name: :value:`drafts`

      .. api-member::
         :name: :value:`inbox`

      .. api-member::
         :name: :value:`junk`

      .. api-member::
         :name: :value:`sent`

      .. api-member::
         :name: :value:`templates`

      .. api-member::
         :name: :value:`trash`

   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)

      Specifies whether the returned :ref:`folders.^mail^folder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.mark^as^read:

markAsRead(folderId)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Marks all messages in a folder as read.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`folders.^mail^folder^id`)

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
      :type: (:ref:`folders.^mail^folder^id`)

   .. api-member::
      :name: ``destinationFolderId``
      :type: (:ref:`folders.^mail^folder^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`folders.^mail^folder`

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
         :type: (:ref:`accounts.^mail^account^id`, optional)

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
         :type: (:ref:`folders.^mail^folder^id`, optional)

         Limits the search to the folder with the specified id.

      .. api-member::
         :name: [``hasMessages``]
         :type: (boolean or :ref:`folders.^query^range`, optional)

         Whether the folder (excluding subfolders) contains messages, or not. Supports to specify a :ref:`folders.^query^range` (min/max) instead of a simple boolean value (none/some).

      .. api-member::
         :name: [``hasNewMessages``]
         :type: (boolean or :ref:`folders.^query^range`, optional)

         Whether the folder (excluding subfolders) contains new messages, or not. Supports to specify a :ref:`folders.^query^range` (min/max) instead of a simple boolean value (none/some).

      .. api-member::
         :name: [``hasSubFolders``]
         :type: (boolean or :ref:`folders.^query^range`, optional)

         Whether the folder has subfolders, or not. Supports to specify a :ref:`folders.^query^range` (min/max) instead of a simple boolean value (none/some).

      .. api-member::
         :name: [``hasUnreadMessages``]
         :type: (boolean or :ref:`folders.^query^range`, optional)

         Whether the folder (excluding subfolders) contains unread messages, or not. Supports to specify a :ref:`folders.^query^range` (min/max) instead of a simple boolean value (none/some).

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
         :type: (:ref:`folders.^query^date^range`, optional)
         :annotation: -- [Added in TB 137]

         Date the folder was last used (folder was accessed, user moved or copied messages into the folder or folder received new messages).

      .. api-member::
         :name: [``lastUsedAsDestination``]
         :type: (:ref:`folders.^query^date^range`, optional)
         :annotation: -- [Added in TB 137]

         Date the folder was last used as a destination (user moved or copied messages into the folder).

      .. api-member::
         :name: [``limit``]
         :type: (integer, optional)
         :annotation: -- [Added in TB 122]

         Limits the number of returned folders. If used together with :value:`recent`, supports being set to :ref:`folders.^d^e^f^a^u^l^t_^m^o^s^t_^r^e^c^e^n^t_^l^i^m^i^t`

      .. api-member::
         :name: [``name``]
         :type: (:ref:`folders.^regular^expression` or string, optional)

         Return only folders whose name is matched by the provided string or regular expression.

      .. api-member::
         :name: [``path``]
         :type: (:ref:`folders.^regular^expression` or string, optional)

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
         :type: (array of :ref:`folders.^mail^folder^special^use`, optional)

         Match only folders with the specified special use (folders have to match all specified uses).

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`folders.^mail^folder`

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
      :type: (:ref:`folders.^mail^folder^id`)

   .. api-member::
      :name: ``newName``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`folders.^mail^folder`
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
      :type: (:ref:`folders.^mail^folder^id`)

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

.. _folders.on^copied:

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
      :type: (:ref:`folders.^mail^folder`)

   .. api-member::
      :name: ``copiedFolder``
      :type: (:ref:`folders.^mail^folder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^created:

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
      :type: (:ref:`folders.^mail^folder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^deleted:

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
      :type: (:ref:`folders.^mail^folder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^folder^info^changed:

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
      :type: (:ref:`folders.^mail^folder`)

   .. api-member::
      :name: ``folderInfo``
      :type: (:ref:`folders.^mail^folder^info`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^moved:

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
      :type: (:ref:`folders.^mail^folder`)

   .. api-member::
      :name: ``movedFolder``
      :type: (:ref:`folders.^mail^folder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^renamed:

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
      :type: (:ref:`folders.^mail^folder`)

   .. api-member::
      :name: ``renamedFolder``
      :type: (:ref:`folders.^mail^folder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^updated:

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
      :type: (:ref:`folders.^mail^folder`)

   .. api-member::
      :name: ``updatedFolder``
      :type: (:ref:`folders.^mail^folder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Types
=====

.. _folders.^mail^folder:

MailFolder
----------

.. api-section-annotation-hack:: -- [Added in TB 68]

An object describing a folder.

.. api-header::
   :label: object

   .. _folders.^mail^folder.id:

   .. api-member::
      :name: ``id``
      :type: (:ref:`folders.^mail^folder^id`)
      :annotation: -- [Added in TB 121]

      An identifier for the folder.

   .. _folders.^mail^folder.is^favorite:

   .. api-member::
      :name: ``isFavorite``
      :type: (boolean)
      :annotation: -- [Added in TB 121]

      Whether this folder is a favorite folder.

   .. _folders.^mail^folder.is^root:

   .. api-member::
      :name: ``isRoot``
      :type: (boolean)
      :annotation: -- [Added in TB 121]

      Whether this folder is a root folder.

   .. _folders.^mail^folder.is^tag:

   .. api-member::
      :name: ``isTag``
      :type: (boolean)
      :annotation: -- [Added in TB 127]

      Whether this folder is a virtual tag folder.

   .. _folders.^mail^folder.is^unified:

   .. api-member::
      :name: ``isUnified``
      :type: (boolean)
      :annotation: -- [Added in TB 127]

      Whether this folder is a unified mailbox folder.

   .. _folders.^mail^folder.is^virtual:

   .. api-member::
      :name: ``isVirtual``
      :type: (boolean)
      :annotation: -- [Added in TB 121]

      Whether this folder is a virtual search folder.

   .. _folders.^mail^folder.name:

   .. api-member::
      :name: ``name``
      :type: (string)

      The human-friendly name of this folder.

   .. _folders.^mail^folder.path:

   .. api-member::
      :name: ``path``
      :type: (string)

      Path to this folder in the account. Although paths look predictable, never guess a folder's path, as there are a number of reasons why it may not be what you think it is. Use :ref:`folders.get^parent^folders` or :ref:`folders.get^sub^folders` to obtain hierarchy information.

   .. _folders.^mail^folder.special^use:

   .. api-member::
      :name: ``specialUse``
      :type: (array of :ref:`folders.^mail^folder^special^use`)
      :annotation: -- [Added in TB 121]

      The special use of this folder. A folder can have multiple special uses.

   .. _folders.^mail^folder.account^id:

   .. api-member::
      :name: [``accountId``]
      :type: (:ref:`accounts.^mail^account^id`, optional)

      The id of the account this folder belongs to. This property is optional and not available for unified mailbox folders or virtual tag folders.

   .. _folders.^mail^folder.sub^folders:

   .. api-member::
      :name: [``subFolders``]
      :type: (array of :ref:`folders.^mail^folder`, optional)
      :annotation: -- [Added in TB 74]

      Subfolders of this folder. This property is optional and only present if the inclusion of subfolders had been requested. The folders will be returned in the same order as used in Thunderbird's folder pane.

.. _folders.^mail^folder^capabilities:

MailFolderCapabilities
----------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

An object containing capability information about a folder.

.. api-header::
   :label: object

   .. _folders.^mail^folder^capabilities.can^add^messages:

   .. api-member::
      :name: [``canAddMessages``]
      :type: (boolean, optional)

      Whether this folder supports adding new messages.

   .. _folders.^mail^folder^capabilities.can^add^subfolders:

   .. api-member::
      :name: [``canAddSubfolders``]
      :type: (boolean, optional)

      Whether this folder supports adding new subfolders.

   .. _folders.^mail^folder^capabilities.can^be^deleted:

   .. api-member::
      :name: [``canBeDeleted``]
      :type: (boolean, optional)

      Whether this folder can be deleted.

   .. _folders.^mail^folder^capabilities.can^be^renamed:

   .. api-member::
      :name: [``canBeRenamed``]
      :type: (boolean, optional)

      Whether this folder can be renamed.

   .. _folders.^mail^folder^capabilities.can^delete^messages:

   .. api-member::
      :name: [``canDeleteMessages``]
      :type: (boolean, optional)

      Whether this folder supports deleting messages.

.. _folders.^mail^folder^id:

MailFolderId
------------

.. api-section-annotation-hack:: -- [Added in TB 121]

A unique id representing a :ref:`folders.^mail^folder` throughout a session. Renaming or moving a folder will invalidate its id.

.. api-header::
   :label: string

.. _folders.^mail^folder^info:

MailFolderInfo
--------------

.. api-section-annotation-hack:: -- [Added in TB 91]

An object containing additional information about a folder.

.. api-header::
   :label: object

   .. _folders.^mail^folder^info.last^used:

   .. api-member::
      :name: [``lastUsed``]
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)
      :annotation: -- [Added in TB 121]

      Date the folder was last used. It is updated every time the folder was accessed, when the user moved or copied messages into the folder and when the folder received new messages. (precision: seconds).

   .. _folders.^mail^folder^info.last^used^as^destination:

   .. api-member::
      :name: [``lastUsedAsDestination``]
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)
      :annotation: -- [Added in TB 137]

      Date the folder was last used as a destination. It is updated every time the user moved or copied messages into the folder. (precision: seconds).

   .. _folders.^mail^folder^info.new^message^count:

   .. api-member::
      :name: [``newMessageCount``]
      :type: (integer, optional)
      :annotation: -- [Added in TB 121]

      Number of new messages in this folder.

   .. _folders.^mail^folder^info.quota:

   .. api-member::
      :name: [``quota``]
      :type: (array of :ref:`folders.^mail^folder^quota`, optional)
      :annotation: -- [Added in TB 121]

      Quota information, if available.

   .. _folders.^mail^folder^info.total^message^count:

   .. api-member::
      :name: [``totalMessageCount``]
      :type: (integer, optional)

      Number of messages in this folder.

   .. _folders.^mail^folder^info.unread^message^count:

   .. api-member::
      :name: [``unreadMessageCount``]
      :type: (integer, optional)

      Number of unread messages in this folder.

.. _folders.^mail^folder^quota:

MailFolderQuota
---------------

.. api-section-annotation-hack:: -- [Added in TB 121]

An object containing quota information.

.. api-header::
   :label: object

   .. _folders.^mail^folder^quota.limit:

   .. api-member::
      :name: ``limit``
      :type: (integer)

      The maximum available quota.

   .. _folders.^mail^folder^quota.type:

   .. api-member::
      :name: ``type``
      :type: (`string`)

      The type of the quota as defined by RFC 2087. A :value:`STORAGE` quota is constraining the available storage in bytes, a :value:`MESSAGE` quota is constraining the number of storable messages.

      Supported values:

      .. api-member::
         :name: :value:`MESSAGE`

      .. api-member::
         :name: :value:`STORAGE`

   .. _folders.^mail^folder^quota.unused:

   .. api-member::
      :name: ``unused``
      :type: (integer)

      The currently unused quota.

   .. _folders.^mail^folder^quota.used:

   .. api-member::
      :name: ``used``
      :type: (integer)

      The currently used quota.

.. _folders.^mail^folder^special^use:

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
            :name: :value:`archives`

         .. api-member::
            :name: :value:`drafts`

         .. api-member::
            :name: :value:`inbox`

         .. api-member::
            :name: :value:`junk`

         .. api-member::
            :name: :value:`outbox`

         .. api-member::
            :name: :value:`sent`

         .. api-member::
            :name: :value:`templates`

         .. api-member::
            :name: :value:`trash`

.. _folders.^query^date^range:

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

*or*

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

.. _folders.^query^range:

QueryRange
----------

.. api-section-annotation-hack:: -- [Added in TB 121]

An object defining a range for an integer value to be used in queries.

.. api-header::
   :label: object

   .. _folders.^query^range.max:

   .. api-member::
      :name: [``max``]
      :type: (integer, optional)

      The maximum value required to match the query.

   .. _folders.^query^range.min:

   .. api-member::
      :name: [``min``]
      :type: (integer, optional)

      The minimum value required to match the query.

.. _folders.^regular^expression:

RegularExpression
-----------------

.. api-section-annotation-hack:: -- [Added in TB 121]

.. api-header::
   :label: object

   .. _folders.^regular^expression.regexp:

   .. api-member::
      :name: ``regexp``
      :type: (string)

      A regular expression, for example :value:`^Projects \\d{4}$`.

   .. _folders.^regular^expression.flags:

   .. api-member::
      :name: [``flags``]
      :type: (string, optional)

      Supported RegExp flags: :value:`i` = case insensitive, and/or one of :value:`u` = unicode support or :value:`v` = extended unicode support

.. rst-class:: api-main-section

Properties
==========

.. _folders.^d^e^f^a^u^l^t_^m^o^s^t_^r^e^c^e^n^t_^l^i^m^i^t:

DEFAULT_MOST_RECENT_LIMIT
-------------------------

.. api-section-annotation-hack:: 

The number of most recent folders used in Thunderbird's UI. Controlled by the :value:`mail.folder_widget.max_recent` preference.
