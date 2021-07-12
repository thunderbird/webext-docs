.. _folders_api:

=======
folders
=======

The folders API first appeared in Thunderbird 68 (see `bug 1531591`__) as a part of the
:doc:`accounts` API. They were later moved here.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1531591

.. role:: permission

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`accountsFolders`

   Create, rename, or delete your mail account folders

.. rst-class:: api-main-section

Functions
=========

.. _folders.create:

create(parentFolderOrAccount, childName)
----------------------------------------

.. api-section-annotation-hack:: 

Creates a new subfolder in the specified folder or at the root of the specified account.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``parentFolderOrAccount``
      :type: (:ref:`folders.MailFolder` or :ref:`accounts.MailAccount`)
   
   
   .. api-member::
      :name: ``childName``
      :type: (string)
   

.. api-header::
   :label: Required permissions

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
   :label: Required permissions

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

   - :permission:`accountsFolders`

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
      
      Specifies whether the returned :ref:`folders.MailFolder` object for each parent folder should include its nested subfolders . Defaults to ``false``.
   

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
      
      Specifies whether the returned :ref:`folders.MailFolder` object for each direct subfolder should also include all its nested subfolders . Defaults to ``true``.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

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
      
      Subfolders are only included if requested.
   
   
   .. api-member::
      :name: [``type``]
      :type: (`string`)
      
      The type of folder, for several common types.
      
      Supported values:
      
      .. api-member::
         :name: ``inbox``
      
      .. api-member::
         :name: ``drafts``
      
      .. api-member::
         :name: ``sent``
      
      .. api-member::
         :name: ``trash``
      
      .. api-member::
         :name: ``templates``
      
      .. api-member::
         :name: ``archives``
      
      .. api-member::
         :name: ``junk``
      
      .. api-member::
         :name: ``outbox``
   
