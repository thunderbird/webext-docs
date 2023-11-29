.. _folders_api:

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

.. _folders.create:

create(parent, childName)
-------------------------

.. api-section-annotation-hack:: 

Creates a new subfolder in the specified folder or at the root of the specified account.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``parent``
      :type: (:ref:`folders.MailFolder` or :ref:`accounts.MailAccount`)
   
   
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

.. _folders.rename:

rename(folder, newName)
-----------------------

.. api-section-annotation-hack:: 

Renames a folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolder`)
   
   
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

.. _folders.move:

move(sourceFolder, destination)
-------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Moves the given ``sourceFolder`` into the given ``destination``. Throws if the destination already contains a folder with the name of the source folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``sourceFolder``
      :type: (:ref:`folders.MailFolder`)
   
   
   .. api-member::
      :name: ``destination``
      :type: (:ref:`folders.MailFolder` or :ref:`accounts.MailAccount`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`accountsFolders`

.. _folders.copy:

copy(sourceFolder, destination)
-------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Copies the given ``sourceFolder`` into the given ``destination``. Throws if the destination already contains a folder with the name of the source folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``sourceFolder``
      :type: (:ref:`folders.MailFolder`)
   
   
   .. api-member::
      :name: ``destination``
      :type: (:ref:`folders.MailFolder` or :ref:`accounts.MailAccount`)
   

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
      :type: (:ref:`folders.MailFolder`)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`accountsFolders`
   - :permission:`messagesDelete`

.. _folders.getFolderInfo:

getFolderInfo(folder)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Get additional information about a mail folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolder`)
   

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
      :type: (:ref:`folders.MailFolder`)
   
   
   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean)
      
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

getSubFolders(folderOrAccount, [includeSubFolders])
---------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Get the subfolders of the specified folder or account.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folderOrAccount``
      :type: (:ref:`folders.MailFolder` or :ref:`accounts.MailAccount`)
   
   
   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean)
      
      Specifies whether the returned :ref:`folders.MailFolder` object for each direct subfolder should also include all its nested subfolders . Defaults to :value:`true`.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Events
======

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

.. rst-class:: api-main-section

Types
=====

.. _folders.MailFolder:

MailFolder
----------

.. api-section-annotation-hack:: 

An object describing a mail folder, as returned for example by the :ref:`folders.getParentFolders` or :ref:`folders.getSubFolders` methods, or part of a :ref:`accounts.MailAccount` object, which is returned for example by the :ref:`accounts.list` and :ref:`accounts.get` methods. The ``subFolders`` property is only included if requested.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
      
      The account this folder belongs to.
   
   
   .. api-member::
      :name: ``path``
      :type: (string)
      
      Path to this folder in the account. Although paths look predictable, never guess a folder's path, as there are a number of reasons why it may not be what you think it is. Use :ref:`folders.getParentFolders` or :ref:`folders.getSubFolders` to obtain hierarchy information.
   
   
   .. api-member::
      :name: [``name``]
      :type: (string)
      
      The human-friendly name of this folder.
   
   
   .. api-member::
      :name: [``subFolders``]
      :type: (array of :ref:`folders.MailFolder`)
      :annotation: -- [Added in TB 74]
      
      Subfolders are only included if requested. They will be returned in the same order as used in Thunderbird's folder pane.
   
   
   .. api-member::
      :name: [``type``]
      :type: (`string`)
      
      The type of folder, for several common types.
      
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
   

.. _folders.MailFolderInfo:

MailFolderInfo
--------------

.. api-section-annotation-hack:: -- [Added in TB 91]

An object containing additional information about a mail folder.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``favorite``]
      :type: (boolean)
      
      Whether this folder is a favorite folder.
   
   
   .. api-member::
      :name: [``totalMessageCount``]
      :type: (integer)
      
      Number of messages in this folder.
   
   
   .. api-member::
      :name: [``unreadMessageCount``]
      :type: (integer)
      
      Number of unread messages in this folder.
   
