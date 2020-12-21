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

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`accountsFolders` is required to use ``folders``.

.. rst-class:: api-main-section

Functions
=========

.. _folders.create:

create(parentFolder, childName)
-------------------------------

.. api-section-annotation-hack:: 

Creates a new subfolder of ``parentFolder``.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``parentFolder``
      :type: (:ref:`folders.MailFolder`)
   
   
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

.. rst-class:: api-main-section

Types
=====

.. _folders.MailFolder:

MailFolder
----------

.. api-section-annotation-hack:: 

A folder object, as returned by the ``list`` and ``get`` methods. Use the accountId and path properties to refer to a folder.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
      
      The account this folder belongs to.
   
   
   .. api-member::
      :name: ``path``
      :type: (string)
      
      Path to this folder in the account. Although paths look predictable, never guess a folder's path, as there are a number of reasons why it may not be what you think it is.
   
   
   .. api-member::
      :name: [``name``]
      :type: (string)
      
      The human-friendly name of this folder.
   
   
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
   
