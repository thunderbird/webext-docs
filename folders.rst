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

.. role:: small

The folders API allows to access and manage the user's message folders.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _folders.permission.accounts^folders:

.. api-member::
   :name: :permission:`accountsFolders`
   :refid: folders-permission-accounts-folders
   :refname: accountsFolders

   Create, rename, or delete your mail account folders.

.. _folders.permission.accounts^read:

.. api-member::
   :name: :permission:`accountsRead`
   :refid: folders-permission-accounts-read
   :refname: accountsRead

   See your mail accounts, their identities and their folders.

.. _folders.permission.messages^delete:

.. api-member::
   :name: :permission:`messagesDelete`
   :refid: folders-permission-messages-delete
   :refname: messagesDelete

   Permanently delete your email messages.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`accountsRead` is required to use ``messenger.folders.*``.

.. rst-class:: api-main-section

Functions
=========

.. _folders.copy:

copy(source, destination)
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Copies the given source folder into the given destination folder. Throws if the destination already contains a folder with the name of the source folder.

.. api-header::
   :label: Parameters

   .. _folders.copy.source:

   .. api-member::
      :name: ``source``
      :refid: folders-copy-source
      :refname: source
      :type: (:ref:`folders.^mail^folder` or :ref:`folders.^mail^folder^id`)

   .. _folders.copy.destination:

   .. api-member::
      :name: ``destination``
      :refid: folders-copy-destination
      :refname: destination
      :type: (:ref:`folders.^mail^folder` or :ref:`accounts.^mail^account` or :ref:`folders.^mail^folder^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.copy.returns:

   .. api-member::
      :refid: folders-copy-returns
      :refname: _returns
      :type: :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`

.. _folders.create:

create(destination, childName)
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Creates a new subfolder in the specified folder, or at the root of the specified account.

.. api-header::
   :label: Parameters

   .. _folders.create.destination:

   .. api-member::
      :name: ``destination``
      :refid: folders-create-destination
      :refname: destination
      :type: (:ref:`folders.^mail^folder` or :ref:`accounts.^mail^account` or :ref:`folders.^mail^folder^id`)

   .. _folders.create.child^name:

   .. api-member::
      :name: ``childName``
      :refid: folders-create-child-name
      :refname: childName
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.create.returns:

   .. api-member::
      :refid: folders-create-returns
      :refname: _returns
      :type: :ref:`folders.^mail^folder`
      :annotation: -- [Added in TB 91.0]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`

.. _folders.delete:

delete(folder)
--------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Deletes a folder.

.. api-header::
   :label: Parameters

   .. _folders.delete.folder:

   .. api-member::
      :name: ``folder``
      :refid: folders-delete-folder
      :refname: folder
      :type: (:ref:`folders.^mail^folder` or :ref:`folders.^mail^folder^id`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`
   - :permission:`messagesDelete`

.. _folders.get:

get(folderId, [includeSubFolders])
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Returns the specified folder.

.. api-header::
   :label: Parameters

   .. _folders.get.folder^id:

   .. api-member::
      :name: ``folderId``
      :refid: folders-get-folder-id
      :refname: folderId
      :type: (:ref:`folders.^mail^folder^id`)

   .. _folders.get.include^sub^folders:

   .. api-member::
      :name: [``includeSubFolders``]
      :refid: folders-get-include-sub-folders
      :refname: includeSubFolders
      :type: (boolean, optional)

      Specifies whether the returned :ref:`folders.^mail^folder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`true`.

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.get.returns:

   .. api-member::
      :refid: folders-get-returns
      :refname: _returns
      :type: :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^folder^capabilities:

getFolderCapabilities(folder)
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Get capability information about a folder.

.. api-header::
   :label: Parameters

   .. _folders.get^folder^capabilities.folder:

   .. api-member::
      :name: ``folder``
      :refid: folders-get-folder-capabilities-folder
      :refname: folder
      :type: (:ref:`folders.^mail^folder` or :ref:`folders.^mail^folder^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.get^folder^capabilities.returns:

   .. api-member::
      :refid: folders-get-folder-capabilities-returns
      :refname: _returns
      :type: :ref:`folders.^mail^folder^capabilities`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^folder^info:

getFolderInfo(folder)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Get additional information about a folder.

.. api-header::
   :label: Parameters

   .. _folders.get^folder^info.folder:

   .. api-member::
      :name: ``folder``
      :refid: folders-get-folder-info-folder
      :refname: folder
      :type: (:ref:`folders.^mail^folder` or :ref:`folders.^mail^folder^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.get^folder^info.returns:

   .. api-member::
      :refid: folders-get-folder-info-returns
      :refname: _returns
      :type: :ref:`folders.^mail^folder^info`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^parent^folders:

getParentFolders(folder, [includeSubFolders])
---------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Get all parent folders as a flat ordered array. The first array entry is the direct parent.

.. api-header::
   :label: Parameters

   .. _folders.get^parent^folders.folder:

   .. api-member::
      :name: ``folder``
      :refid: folders-get-parent-folders-folder
      :refname: folder
      :type: (:ref:`folders.^mail^folder` or :ref:`folders.^mail^folder^id`)

   .. _folders.get^parent^folders.include^sub^folders:

   .. api-member::
      :name: [``includeSubFolders``]
      :refid: folders-get-parent-folders-include-sub-folders
      :refname: includeSubFolders
      :type: (boolean, optional)

      Specifies whether each returned parent :ref:`folders.^mail^folder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.get^parent^folders.returns:

   .. api-member::
      :refid: folders-get-parent-folders-returns
      :refname: _returns
      :type: array of :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^sub^folders:

getSubFolders(folder, [includeSubFolders])
------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Get the subfolders of the specified folder or account.

.. api-header::
   :label: Parameters

   .. _folders.get^sub^folders.folder:

   .. api-member::
      :name: ``folder``
      :refid: folders-get-sub-folders-folder
      :refname: folder
      :type: (:ref:`folders.^mail^folder` or :ref:`accounts.^mail^account` or :ref:`folders.^mail^folder^id`)

   .. _folders.get^sub^folders.include^sub^folders:

   .. api-member::
      :name: [``includeSubFolders``]
      :refid: folders-get-sub-folders-include-sub-folders
      :refname: includeSubFolders
      :type: (boolean, optional)

      Specifies whether each returned direct child :ref:`folders.^mail^folder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`true`.

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.get^sub^folders.returns:

   .. api-member::
      :refid: folders-get-sub-folders-returns
      :refname: _returns
      :type: array of :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^tag^folder:

getTagFolder(key)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Get one of the special virtual tag folders, which are virtual search folders and group messages from all mail accounts based on their tags. Throws if the requested folder does not exist.

.. api-header::
   :label: Parameters

   .. _folders.get^tag^folder.key:

   .. api-member::
      :name: ``key``
      :refid: folders-get-tag-folder-key
      :refname: key
      :type: (string)

      The tag key of the requested folder. See :ref:`messages.tags.list` for the available tags. Throws when specifying an invalid tag key.

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.get^tag^folder.returns:

   .. api-member::
      :refid: folders-get-tag-folder-returns
      :refname: _returns
      :type: :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.get^unified^folder:

getUnifiedFolder(type, [includeSubFolders])
-------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Get one of the special unified mailbox folders, which are virtual search folders and return the content from all mail accounts. Throws if the requested folder does not exist.

.. api-header::
   :label: Parameters

   .. _folders.get^unified^folder.type:

   .. api-member::
      :name: ``type``
      :refid: folders-get-unified-folder-type
      :refname: type
      :type: (`string`)

      The requested unified mailbox folder type.

      Supported values:

      .. _folders.get^unified^folder.type.archives:

      .. api-member::
         :name: :value:`archives`
         :refid: folders-get-unified-folder-type-archives
         :refname: archives

      .. _folders.get^unified^folder.type.drafts:

      .. api-member::
         :name: :value:`drafts`
         :refid: folders-get-unified-folder-type-drafts
         :refname: drafts

      .. _folders.get^unified^folder.type.inbox:

      .. api-member::
         :name: :value:`inbox`
         :refid: folders-get-unified-folder-type-inbox
         :refname: inbox

      .. _folders.get^unified^folder.type.junk:

      .. api-member::
         :name: :value:`junk`
         :refid: folders-get-unified-folder-type-junk
         :refname: junk

      .. _folders.get^unified^folder.type.sent:

      .. api-member::
         :name: :value:`sent`
         :refid: folders-get-unified-folder-type-sent
         :refname: sent

      .. _folders.get^unified^folder.type.templates:

      .. api-member::
         :name: :value:`templates`
         :refid: folders-get-unified-folder-type-templates
         :refname: templates

      .. _folders.get^unified^folder.type.trash:

      .. api-member::
         :name: :value:`trash`
         :refid: folders-get-unified-folder-type-trash
         :refname: trash

   .. _folders.get^unified^folder.include^sub^folders:

   .. api-member::
      :name: [``includeSubFolders``]
      :refid: folders-get-unified-folder-include-sub-folders
      :refname: includeSubFolders
      :type: (boolean, optional)

      Specifies whether the returned :ref:`folders.^mail^folder` should populate its :value:`subFolders` property and include all its (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.get^unified^folder.returns:

   .. api-member::
      :refid: folders-get-unified-folder-returns
      :refname: _returns
      :type: :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.mark^as^read:

markAsRead(folder)
------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Marks all messages in a folder as read.

.. api-header::
   :label: Parameters

   .. _folders.mark^as^read.folder:

   .. api-member::
      :name: ``folder``
      :refid: folders-mark-as-read-folder
      :refname: folder
      :type: (:ref:`folders.^mail^folder` or :ref:`folders.^mail^folder^id`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`

.. _folders.move:

move(source, destination)
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Moves the given source folder into the given destination folder. Throws if the destination already contains a folder with the name of the source folder.

.. api-header::
   :label: Parameters

   .. _folders.move.source:

   .. api-member::
      :name: ``source``
      :refid: folders-move-source
      :refname: source
      :type: (:ref:`folders.^mail^folder` or :ref:`folders.^mail^folder^id`)

   .. _folders.move.destination:

   .. api-member::
      :name: ``destination``
      :refid: folders-move-destination
      :refname: destination
      :type: (:ref:`folders.^mail^folder` or :ref:`accounts.^mail^account` or :ref:`folders.^mail^folder^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.move.returns:

   .. api-member::
      :refid: folders-move-returns
      :refname: _returns
      :type: :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`

.. _folders.query:

query([queryInfo])
------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Gets folders that match the specified properties, or all folders if no properties are specified.

.. api-header::
   :label: Parameters

   .. _folders.query.query^info:

   .. api-member::
      :name: [``queryInfo``]
      :refid: folders-query-query-info
      :refname: queryInfo
      :type: (object, optional)

      .. _folders.query.query^info.account^id:

      .. api-member::
         :name: [``accountId``]
         :refid: folders-query-query-info-account-id
         :refname: accountId
         :type: (:ref:`accounts.^mail^account^id`, optional)

         Limits the search to folders of the account with the specified id.

      .. _folders.query.query^info.can^add^messages:

      .. api-member::
         :name: [``canAddMessages``]
         :refid: folders-query-query-info-can-add-messages
         :refname: canAddMessages
         :type: (boolean, optional)

         Whether the folder supports adding new messages, or not.

      .. _folders.query.query^info.can^add^subfolders:

      .. api-member::
         :name: [``canAddSubfolders``]
         :refid: folders-query-query-info-can-add-subfolders
         :refname: canAddSubfolders
         :type: (boolean, optional)

         Whether the folder supports adding new subfolders, or not.

      .. _folders.query.query^info.can^be^deleted:

      .. api-member::
         :name: [``canBeDeleted``]
         :refid: folders-query-query-info-can-be-deleted
         :refname: canBeDeleted
         :type: (boolean, optional)

         Whether the folder can be deleted, or not.

      .. _folders.query.query^info.can^be^renamed:

      .. api-member::
         :name: [``canBeRenamed``]
         :refid: folders-query-query-info-can-be-renamed
         :refname: canBeRenamed
         :type: (boolean, optional)

         Whether the folder can be renamed, or not.

      .. _folders.query.query^info.can^delete^messages:

      .. api-member::
         :name: [``canDeleteMessages``]
         :refid: folders-query-query-info-can-delete-messages
         :refname: canDeleteMessages
         :type: (boolean, optional)

         Whether the folder supports deleting messages, or not.

      .. _folders.query.query^info.folder^id:

      .. api-member::
         :name: [``folderId``]
         :refid: folders-query-query-info-folder-id
         :refname: folderId
         :type: (:ref:`folders.^mail^folder^id`, optional)

         Limits the search to the folder with the specified id.

      .. _folders.query.query^info.has^messages:

      .. api-member::
         :name: [``hasMessages``]
         :refid: folders-query-query-info-has-messages
         :refname: hasMessages
         :type: (boolean or :ref:`folders.^query^range`, optional)

         Whether the folder (excluding subfolders) contains messages, or not. Supports to specify a :ref:`folders.^query^range` (min/max) instead of a simple boolean value (none/some).

      .. _folders.query.query^info.has^new^messages:

      .. api-member::
         :name: [``hasNewMessages``]
         :refid: folders-query-query-info-has-new-messages
         :refname: hasNewMessages
         :type: (boolean or :ref:`folders.^query^range`, optional)

         Whether the folder (excluding subfolders) contains new messages, or not. Supports to specify a :ref:`folders.^query^range` (min/max) instead of a simple boolean value (none/some).

      .. _folders.query.query^info.has^sub^folders:

      .. api-member::
         :name: [``hasSubFolders``]
         :refid: folders-query-query-info-has-sub-folders
         :refname: hasSubFolders
         :type: (boolean or :ref:`folders.^query^range`, optional)

         Whether the folder has subfolders, or not. Supports to specify a :ref:`folders.^query^range` (min/max) instead of a simple boolean value (none/some).

      .. _folders.query.query^info.has^unread^messages:

      .. api-member::
         :name: [``hasUnreadMessages``]
         :refid: folders-query-query-info-has-unread-messages
         :refname: hasUnreadMessages
         :type: (boolean or :ref:`folders.^query^range`, optional)

         Whether the folder (excluding subfolders) contains unread messages, or not. Supports to specify a :ref:`folders.^query^range` (min/max) instead of a simple boolean value (none/some).

      .. _folders.query.query^info.is^favorite:

      .. api-member::
         :name: [``isFavorite``]
         :refid: folders-query-query-info-is-favorite
         :refname: isFavorite
         :type: (boolean, optional)

         Whether the folder is a favorite folder, or not.

      .. _folders.query.query^info.is^root:

      .. api-member::
         :name: [``isRoot``]
         :refid: folders-query-query-info-is-root
         :refname: isRoot
         :type: (boolean, optional)

         Whether the folder is a root folder, or not.

      .. _folders.query.query^info.is^tag:

      .. api-member::
         :name: [``isTag``]
         :refid: folders-query-query-info-is-tag
         :refname: isTag
         :type: (boolean, optional)

         Whether the folder is a virtual tag folder, or not. Virtual tag folders are always skipped, unless this property is set to :value:`true`

      .. _folders.query.query^info.is^unified:

      .. api-member::
         :name: [``isUnified``]
         :refid: folders-query-query-info-is-unified
         :refname: isUnified
         :type: (boolean, optional)

         Whether the folder is a unified mailbox folder, or not. Unified mailbox folders are always skipped, unless this property is set to :value:`true`

      .. _folders.query.query^info.is^virtual:

      .. api-member::
         :name: [``isVirtual``]
         :refid: folders-query-query-info-is-virtual
         :refname: isVirtual
         :type: (boolean, optional)

         Whether the folder is a virtual search folder, or not.

      .. _folders.query.query^info.last^used:

      .. api-member::
         :name: [``lastUsed``]
         :refid: folders-query-query-info-last-used
         :refname: lastUsed
         :type: (:ref:`folders.^query^date^range`, optional)
         :annotation: -- [Added in TB 140.0]

         Date the folder was last used (folder was accessed, user moved or copied messages into the folder or folder received new messages).

      .. _folders.query.query^info.last^used^as^destination:

      .. api-member::
         :name: [``lastUsedAsDestination``]
         :refid: folders-query-query-info-last-used-as-destination
         :refname: lastUsedAsDestination
         :type: (:ref:`folders.^query^date^range`, optional)
         :annotation: -- [Added in TB 140.0]

         Date the folder was last used as a destination (user moved or copied messages into the folder).

      .. _folders.query.query^info.limit:

      .. api-member::
         :name: [``limit``]
         :refid: folders-query-query-info-limit
         :refname: limit
         :type: (integer, optional)

         Limits the number of returned folders. If used together with :value:`recent`, supports being set to :ref:`folders.^d^e^f^a^u^l^t_^m^o^s^t_^r^e^c^e^n^t_^l^i^m^i^t`

      .. _folders.query.query^info.name:

      .. api-member::
         :name: [``name``]
         :refid: folders-query-query-info-name
         :refname: name
         :type: (:ref:`folders.^regular^expression` or string, optional)

         Return only folders whose name is matched by the provided string or regular expression.

      .. _folders.query.query^info.path:

      .. api-member::
         :name: [``path``]
         :refid: folders-query-query-info-path
         :refname: path
         :type: (:ref:`folders.^regular^expression` or string, optional)

         Return only folders whose path is matched by the provided string or regular expression.

      .. _folders.query.query^info.recent:

      .. api-member::
         :name: [``recent``]
         :refid: folders-query-query-info-recent
         :refname: recent
         :type: (boolean, optional) **Deprecated.**

         Whether the folder (excluding subfolders) has been used within the last month, or not. The returned folders will be sorted by :value:`lastUsed`.

      .. _folders.query.query^info.sort:

      .. api-member::
         :name: [``sort``]
         :refid: folders-query-query-info-sort
         :refname: sort
         :type: (`string`, optional)
         :annotation: -- [Added in TB 140.0]

         The sort order of the returned folders. If not specified, folders will be sorted by :value:`path`. Sorting by :value:`name` is case-insensitive.

         Supported values:

         .. _folders.query.query^info.sort.last^used:

         .. api-member::
            :name: :value:`lastUsed`
            :refid: folders-query-query-info-sort-last-used
            :refname: lastUsed

         .. _folders.query.query^info.sort.last^used^as^destination:

         .. api-member::
            :name: :value:`lastUsedAsDestination`
            :refid: folders-query-query-info-sort-last-used-as-destination
            :refname: lastUsedAsDestination

         .. _folders.query.query^info.sort.name:

         .. api-member::
            :name: :value:`name`
            :refid: folders-query-query-info-sort-name
            :refname: name

         .. _folders.query.query^info.sort.path:

         .. api-member::
            :name: :value:`path`
            :refid: folders-query-query-info-sort-path
            :refname: path

      .. _folders.query.query^info.special^use:

      .. api-member::
         :name: [``specialUse``]
         :refid: folders-query-query-info-special-use
         :refname: specialUse
         :type: (array of :ref:`folders.^mail^folder^special^use`, optional)

         Match only folders with the specified special use (folders have to match all specified uses).

      .. _folders.query.query^info.type:

      .. api-member::
         :name: [``type``]
         :refid: folders-query-query-info-type
         :refname: type
         :type: (:ref:`folders.^mail^folder^special^use`, optional)

         Deprecated. Match only folders with the specified special use.

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.query.returns:

   .. api-member::
      :refid: folders-query-returns
      :refname: _returns
      :type: array of :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.rename:

rename(folder, newName)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Renames a folder.

.. api-header::
   :label: Parameters

   .. _folders.rename.folder:

   .. api-member::
      :name: ``folder``
      :refid: folders-rename-folder
      :refname: folder
      :type: (:ref:`folders.^mail^folder` or :ref:`folders.^mail^folder^id`)

   .. _folders.rename.new^name:

   .. api-member::
      :name: ``newName``
      :refid: folders-rename-new-name
      :refname: newName
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _folders.rename.returns:

   .. api-member::
      :refid: folders-rename-returns
      :refname: _returns
      :type: :ref:`folders.^mail^folder`
      :annotation: -- [Added in TB 91.0]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsFolders`
   - :permission:`accountsRead`

.. _folders.update:

update(folder, updateProperties)
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Updates properties of a folder.

.. api-header::
   :label: Parameters

   .. _folders.update.folder:

   .. api-member::
      :name: ``folder``
      :refid: folders-update-folder
      :refname: folder
      :type: (:ref:`folders.^mail^folder` or :ref:`folders.^mail^folder^id`)

   .. _folders.update.update^properties:

   .. api-member::
      :name: ``updateProperties``
      :refid: folders-update-update-properties
      :refname: updateProperties
      :type: (object)

      The properties to update.

      .. _folders.update.update^properties.is^favorite:

      .. api-member::
         :name: [``isFavorite``]
         :refid: folders-update-update-properties-is-favorite
         :refname: isFavorite
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

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Fired when a folder has been copied.

.. api-header::
   :label: Parameters for onCopied.addListener(listener)

   .. _folders.on^copied.listener(original^folder, copied^folder):

   .. api-member::
      :name: ``listener(originalFolder, copiedFolder)``
      :refid: folders-on-copied-listener-original-folder-copied-folder
      :refname: listener(originalFolder, copiedFolder)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _folders.on^copied.original^folder:

   .. api-member::
      :name: ``originalFolder``
      :refid: folders-on-copied-original-folder
      :refname: originalFolder
      :type: (:ref:`folders.^mail^folder`)

   .. _folders.on^copied.copied^folder:

   .. api-member::
      :name: ``copiedFolder``
      :refid: folders-on-copied-copied-folder
      :refname: copiedFolder
      :type: (:ref:`folders.^mail^folder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Fired when a folder has been created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _folders.on^created.listener(created^folder):

   .. api-member::
      :name: ``listener(createdFolder)``
      :refid: folders-on-created-listener-created-folder
      :refname: listener(createdFolder)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _folders.on^created.created^folder:

   .. api-member::
      :name: ``createdFolder``
      :refid: folders-on-created-created-folder
      :refname: createdFolder
      :type: (:ref:`folders.^mail^folder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Fired when a folder has been deleted.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. _folders.on^deleted.listener(deleted^folder):

   .. api-member::
      :name: ``listener(deletedFolder)``
      :refid: folders-on-deleted-listener-deleted-folder
      :refname: listener(deletedFolder)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _folders.on^deleted.deleted^folder:

   .. api-member::
      :name: ``deletedFolder``
      :refid: folders-on-deleted-deleted-folder
      :refname: deletedFolder
      :type: (:ref:`folders.^mail^folder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^folder^info^changed:

onFolderInfoChanged
-------------------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Fired when certain information of a folder have changed. Bursts of message count changes are collapsed to a single event.

.. api-header::
   :label: Parameters for onFolderInfoChanged.addListener(listener)

   .. _folders.on^folder^info^changed.listener(folder, folder^info):

   .. api-member::
      :name: ``listener(folder, folderInfo)``
      :refid: folders-on-folder-info-changed-listener-folder-folder-info
      :refname: listener(folder, folderInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _folders.on^folder^info^changed.folder:

   .. api-member::
      :name: ``folder``
      :refid: folders-on-folder-info-changed-folder
      :refname: folder
      :type: (:ref:`folders.^mail^folder`)

   .. _folders.on^folder^info^changed.folder^info:

   .. api-member::
      :name: ``folderInfo``
      :refid: folders-on-folder-info-changed-folder-info
      :refname: folderInfo
      :type: (:ref:`folders.^mail^folder^info`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^moved:

onMoved
-------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Fired when a folder has been moved.

.. api-header::
   :label: Parameters for onMoved.addListener(listener)

   .. _folders.on^moved.listener(original^folder, moved^folder):

   .. api-member::
      :name: ``listener(originalFolder, movedFolder)``
      :refid: folders-on-moved-listener-original-folder-moved-folder
      :refname: listener(originalFolder, movedFolder)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _folders.on^moved.original^folder:

   .. api-member::
      :name: ``originalFolder``
      :refid: folders-on-moved-original-folder
      :refname: originalFolder
      :type: (:ref:`folders.^mail^folder`)

   .. _folders.on^moved.moved^folder:

   .. api-member::
      :name: ``movedFolder``
      :refid: folders-on-moved-moved-folder
      :refname: movedFolder
      :type: (:ref:`folders.^mail^folder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^renamed:

onRenamed
---------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Fired when a folder has been renamed.

.. api-header::
   :label: Parameters for onRenamed.addListener(listener)

   .. _folders.on^renamed.listener(original^folder, renamed^folder):

   .. api-member::
      :name: ``listener(originalFolder, renamedFolder)``
      :refid: folders-on-renamed-listener-original-folder-renamed-folder
      :refname: listener(originalFolder, renamedFolder)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _folders.on^renamed.original^folder:

   .. api-member::
      :name: ``originalFolder``
      :refid: folders-on-renamed-original-folder
      :refname: originalFolder
      :type: (:ref:`folders.^mail^folder`)

   .. _folders.on^renamed.renamed^folder:

   .. api-member::
      :name: ``renamedFolder``
      :refid: folders-on-renamed-renamed-folder
      :refname: renamedFolder
      :type: (:ref:`folders.^mail^folder`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _folders.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Fired when properties of a folder have changed (:value:`specialUse` and :value:`isFavorite`).

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. _folders.on^updated.listener(original^folder, updated^folder):

   .. api-member::
      :name: ``listener(originalFolder, updatedFolder)``
      :refid: folders-on-updated-listener-original-folder-updated-folder
      :refname: listener(originalFolder, updatedFolder)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _folders.on^updated.original^folder:

   .. api-member::
      :name: ``originalFolder``
      :refid: folders-on-updated-original-folder
      :refname: originalFolder
      :type: (:ref:`folders.^mail^folder`)

   .. _folders.on^updated.updated^folder:

   .. api-member::
      :name: ``updatedFolder``
      :refid: folders-on-updated-updated-folder
      :refname: updatedFolder
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

.. api-section-annotation-hack:: -- [Added in TB 68.0]

An object describing a folder.

.. api-header::
   :label: object

   .. _folders.^mail^folder.path:

   .. api-member::
      :name: ``path``
      :refid: folders-mail-folder-path
      :refname: path
      :type: (string)

      Path to this folder in the account. Although paths look predictable, never guess a folder's path, as there are a number of reasons why it may not be what you think it is. Use :ref:`folders.get^parent^folders` or :ref:`folders.get^sub^folders` to obtain hierarchy information.

   .. _folders.^mail^folder.account^id:

   .. api-member::
      :name: [``accountId``]
      :refid: folders-mail-folder-account-id
      :refname: accountId
      :type: (:ref:`accounts.^mail^account^id`, optional)

      The id of the account this folder belongs to.

   .. _folders.^mail^folder.id:

   .. api-member::
      :name: [``id``]
      :refid: folders-mail-folder-id
      :refname: id
      :type: (:ref:`folders.^mail^folder^id`, optional)
      :annotation: -- [Added in TB 128.0]

      An identifier for the folder.

   .. _folders.^mail^folder.is^favorite:

   .. api-member::
      :name: [``isFavorite``]
      :refid: folders-mail-folder-is-favorite
      :refname: isFavorite
      :type: (boolean, optional)
      :annotation: -- [Added in TB 128.0]

      Whether this folder is a favorite folder.

   .. _folders.^mail^folder.is^root:

   .. api-member::
      :name: [``isRoot``]
      :refid: folders-mail-folder-is-root
      :refname: isRoot
      :type: (boolean, optional)
      :annotation: -- [Added in TB 128.0]

      Whether this folder is a root folder.

   .. _folders.^mail^folder.is^tag:

   .. api-member::
      :name: [``isTag``]
      :refid: folders-mail-folder-is-tag
      :refname: isTag
      :type: (boolean, optional)
      :annotation: -- [Added in TB 128.0]

      Whether this folder is a virtual tag folder.

   .. _folders.^mail^folder.is^unified:

   .. api-member::
      :name: [``isUnified``]
      :refid: folders-mail-folder-is-unified
      :refname: isUnified
      :type: (boolean, optional)
      :annotation: -- [Added in TB 128.0]

      Whether this folder is a unified mailbox folder.

   .. _folders.^mail^folder.is^virtual:

   .. api-member::
      :name: [``isVirtual``]
      :refid: folders-mail-folder-is-virtual
      :refname: isVirtual
      :type: (boolean, optional)
      :annotation: -- [Added in TB 128.0]

      Whether this folder is a virtual search folder.

   .. _folders.^mail^folder.name:

   .. api-member::
      :name: [``name``]
      :refid: folders-mail-folder-name
      :refname: name
      :type: (string, optional)

      The human-friendly name of this folder.

   .. _folders.^mail^folder.special^use:

   .. api-member::
      :name: [``specialUse``]
      :refid: folders-mail-folder-special-use
      :refname: specialUse
      :type: (array of :ref:`folders.^mail^folder^special^use`, optional)
      :annotation: -- [Added in TB 128.0]

      The special use of this folder. A folder can have multiple special uses.

   .. _folders.^mail^folder.sub^folders:

   .. api-member::
      :name: [``subFolders``]
      :refid: folders-mail-folder-sub-folders
      :refname: subFolders
      :type: (array of :ref:`folders.^mail^folder`, optional)
      :annotation: -- [Added in TB 78.0]

      Subfolders of this folder. This property is optional and only present if the inclusion of subfolders had been requested. The folders will be returned in the same order as used in Thunderbird's folder pane.

   .. _folders.^mail^folder.type:

   .. api-member::
      :name: [``type``]
      :refid: folders-mail-folder-type
      :refname: type
      :type: (:ref:`folders.^mail^folder^special^use`, optional)

      Deprecated. Was used to represent the type of this folder.

.. _folders.^mail^folder^capabilities:

MailFolderCapabilities
----------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

An object containing capability information about a folder.

.. api-header::
   :label: object

   .. _folders.^mail^folder^capabilities.can^add^messages:

   .. api-member::
      :name: [``canAddMessages``]
      :refid: folders-mail-folder-capabilities-can-add-messages
      :refname: canAddMessages
      :type: (boolean, optional)

      Whether this folder supports adding new messages.

   .. _folders.^mail^folder^capabilities.can^add^subfolders:

   .. api-member::
      :name: [``canAddSubfolders``]
      :refid: folders-mail-folder-capabilities-can-add-subfolders
      :refname: canAddSubfolders
      :type: (boolean, optional)

      Whether this folder supports adding new subfolders.

   .. _folders.^mail^folder^capabilities.can^be^deleted:

   .. api-member::
      :name: [``canBeDeleted``]
      :refid: folders-mail-folder-capabilities-can-be-deleted
      :refname: canBeDeleted
      :type: (boolean, optional)

      Whether this folder can be deleted.

   .. _folders.^mail^folder^capabilities.can^be^renamed:

   .. api-member::
      :name: [``canBeRenamed``]
      :refid: folders-mail-folder-capabilities-can-be-renamed
      :refname: canBeRenamed
      :type: (boolean, optional)

      Whether this folder can be renamed.

   .. _folders.^mail^folder^capabilities.can^delete^messages:

   .. api-member::
      :name: [``canDeleteMessages``]
      :refid: folders-mail-folder-capabilities-can-delete-messages
      :refname: canDeleteMessages
      :type: (boolean, optional)

      Whether this folder supports deleting messages.

.. _folders.^mail^folder^id:

MailFolderId
------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

A unique id representing a :ref:`folders.^mail^folder` throughout a session. Renaming or moving a folder will invalidate its id.

.. api-header::
   :label: string

.. _folders.^mail^folder^info:

MailFolderInfo
--------------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

An object containing additional information about a folder.

.. api-header::
   :label: object

   .. _folders.^mail^folder^info.favorite:

   .. api-member::
      :name: [``favorite``]
      :refid: folders-mail-folder-info-favorite
      :refname: favorite
      :type: (boolean, optional)

      Deprecated. This information is now available in :ref:`folders.^mail^folder`.

   .. _folders.^mail^folder^info.last^used:

   .. api-member::
      :name: [``lastUsed``]
      :refid: folders-mail-folder-info-last-used
      :refname: lastUsed
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)
      :annotation: -- [Added in TB 128.0]

      Date the folder was last used. It is updated every time the folder was accessed, when the user moved or copied messages into the folder and when the folder received new messages. (precision: seconds).

   .. _folders.^mail^folder^info.last^used^as^destination:

   .. api-member::
      :name: [``lastUsedAsDestination``]
      :refid: folders-mail-folder-info-last-used-as-destination
      :refname: lastUsedAsDestination
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)
      :annotation: -- [Added in TB 140.0]

      Date the folder was last used as a destination. It is updated every time the user moved or copied messages into the folder. (precision: seconds).

   .. _folders.^mail^folder^info.new^message^count:

   .. api-member::
      :name: [``newMessageCount``]
      :refid: folders-mail-folder-info-new-message-count
      :refname: newMessageCount
      :type: (integer, optional)
      :annotation: -- [Added in TB 128.0]

      Number of new messages in this folder.

   .. _folders.^mail^folder^info.quota:

   .. api-member::
      :name: [``quota``]
      :refid: folders-mail-folder-info-quota
      :refname: quota
      :type: (array of :ref:`folders.^mail^folder^quota`, optional)
      :annotation: -- [Added in TB 128.0]

      Quota information, if available.

   .. _folders.^mail^folder^info.total^message^count:

   .. api-member::
      :name: [``totalMessageCount``]
      :refid: folders-mail-folder-info-total-message-count
      :refname: totalMessageCount
      :type: (integer, optional)

      Number of messages in this folder.

   .. _folders.^mail^folder^info.unread^message^count:

   .. api-member::
      :name: [``unreadMessageCount``]
      :refid: folders-mail-folder-info-unread-message-count
      :refname: unreadMessageCount
      :type: (integer, optional)

      Number of unread messages in this folder.

.. _folders.^mail^folder^quota:

MailFolderQuota
---------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

An object containing quota information.

.. api-header::
   :label: object

   .. _folders.^mail^folder^quota.limit:

   .. api-member::
      :name: ``limit``
      :refid: folders-mail-folder-quota-limit
      :refname: limit
      :type: (integer)

      The maximum available quota.

   .. _folders.^mail^folder^quota.type:

   .. api-member::
      :name: ``type``
      :refid: folders-mail-folder-quota-type
      :refname: type
      :type: (`string`)

      The type of the quota as defined by RFC 2087. A :value:`STORAGE` quota is constraining the available storage in bytes, a :value:`MESSAGE` quota is constraining the number of storable messages.

      Supported values:

      .. _folders.^mail^folder^quota.type.^m^e^s^s^a^g^e:

      .. api-member::
         :name: :value:`MESSAGE`
         :refid: folders-mail-folder-quota-type-m-e-s-s-a-g-e
         :refname: MESSAGE

      .. _folders.^mail^folder^quota.type.^s^t^o^r^a^g^e:

      .. api-member::
         :name: :value:`STORAGE`
         :refid: folders-mail-folder-quota-type-s-t-o-r-a-g-e
         :refname: STORAGE

   .. _folders.^mail^folder^quota.unused:

   .. api-member::
      :name: ``unused``
      :refid: folders-mail-folder-quota-unused
      :refname: unused
      :type: (integer)

      The currently unused quota.

   .. _folders.^mail^folder^quota.used:

   .. api-member::
      :name: ``used``
      :refid: folders-mail-folder-quota-used
      :refname: used
      :type: (integer)

      The currently used quota.

.. _folders.^mail^folder^special^use:

MailFolderSpecialUse
--------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Supported values for the special use of a folder.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _folders.^mail^folder^special^use.archives:

         .. api-member::
            :name: :value:`archives`
            :refid: folders-mail-folder-special-use-archives
            :refname: archives

         .. _folders.^mail^folder^special^use.drafts:

         .. api-member::
            :name: :value:`drafts`
            :refid: folders-mail-folder-special-use-drafts
            :refname: drafts

         .. _folders.^mail^folder^special^use.inbox:

         .. api-member::
            :name: :value:`inbox`
            :refid: folders-mail-folder-special-use-inbox
            :refname: inbox

         .. _folders.^mail^folder^special^use.junk:

         .. api-member::
            :name: :value:`junk`
            :refid: folders-mail-folder-special-use-junk
            :refname: junk

         .. _folders.^mail^folder^special^use.outbox:

         .. api-member::
            :name: :value:`outbox`
            :refid: folders-mail-folder-special-use-outbox
            :refname: outbox

         .. _folders.^mail^folder^special^use.sent:

         .. api-member::
            :name: :value:`sent`
            :refid: folders-mail-folder-special-use-sent
            :refname: sent

         .. _folders.^mail^folder^special^use.templates:

         .. api-member::
            :name: :value:`templates`
            :refid: folders-mail-folder-special-use-templates
            :refname: templates

         .. _folders.^mail^folder^special^use.trash:

         .. api-member::
            :name: :value:`trash`
            :refid: folders-mail-folder-special-use-trash
            :refname: trash

.. _folders.^query^date^range:

QueryDateRange
--------------

.. api-section-annotation-hack:: -- [Added in TB 140.0]

An object defining a range for a date value to be used in queries.

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _folders.^query^date^range.recent:

         .. api-member::
            :name: ``recent``
            :refid: folders-query-date-range-recent
            :refname: recent
            :type: (boolean)

            Whether the date must be considered to be recent by Thunderbird (within the last month) or not, to match the query.

*or*

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _folders.^query^date^range.after:

         .. api-member::
            :name: [``after``]
            :refid: folders-query-date-range-after
            :refname: after
            :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)

            The minimum date required to match the query.

         .. _folders.^query^date^range.before:

         .. api-member::
            :name: [``before``]
            :refid: folders-query-date-range-before
            :refname: before
            :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)

            The maximum date required to match the query.

.. _folders.^query^range:

QueryRange
----------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

An object defining a range for an integer value to be used in queries.

.. api-header::
   :label: object

   .. _folders.^query^range.max:

   .. api-member::
      :name: [``max``]
      :refid: folders-query-range-max
      :refname: max
      :type: (integer, optional)

      The maximum value required to match the query.

   .. _folders.^query^range.min:

   .. api-member::
      :name: [``min``]
      :refid: folders-query-range-min
      :refname: min
      :type: (integer, optional)

      The minimum value required to match the query.

.. _folders.^regular^expression:

RegularExpression
-----------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

.. api-header::
   :label: object

   .. _folders.^regular^expression.regexp:

   .. api-member::
      :name: ``regexp``
      :refid: folders-regular-expression-regexp
      :refname: regexp
      :type: (string)

      A regular expression, for example :value:`^Projects \\d{4}$`.

   .. _folders.^regular^expression.flags:

   .. api-member::
      :name: [``flags``]
      :refid: folders-regular-expression-flags
      :refname: flags
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
