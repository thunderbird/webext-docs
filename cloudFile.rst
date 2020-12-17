=========
cloudFile
=========

The cloudFile (a.k.a. fileLink) API first appeared in Thunderbird 64, and was uplifted to
Thunderbird 60.4 ESR.

From Thunderbird 68.2.1 (Thunderbird 71 beta), an extension can choose to receive data for upload
as a ``File`` object rather than as an ``ArrayBuffer``. You **should** specify which you want as
the default may change in a future version.

The `DropBox Uploader`__ sample extension uses this API.

__ https://github.com/thundernest/sample-extensions/tree/master/dropbox

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``cloud_file``]
   :type: (object)
   :annotation: 

   
   .. api-member::
      :name: ``management_url``
      :type: (string)
      :annotation: 
   
      A page for configuring accounts, to be displayed in the preferences UI. **Note:** Within this UI only a limited subset of the WebExtension APIs is available: cloudFile, extension, i18n, runtime, storage, test.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      :annotation: 
   
      Name of the cloud file service.
   
   
   .. api-member::
      :name: [``data_format``]
      :type: (`string`)
      :annotation: -- [Added in TB 71, backported to TB 68.2.1]
   
      Determines the format of the ``data`` argument in ``onFileUpload``.
      
      Allowed values:
      
      .. api-member::
         :name: ``ArrayBuffer``
      
      .. api-member::
         :name: ``File``
      
   
   
   .. api-member::
      :name: [``new_account_url``]
      :type: (string) **Deprecated.**
      :annotation: 
   
      This property was never used.
   
   
   .. api-member::
      :name: [``service_url``]
      :type: (string)
      :annotation: 
   
      URL to the web page of the cloud file service.
   

.. rst-class:: api-permission-info

.. note::

  A manifest entry named ``cloud_file`` is required to use ``cloudFile``.

.. rst-class:: api-main-section

Functions
=========

.. _cloudFile.getAccount:

getAccount(accountId)
---------------------

.. api-section-annotation-hack:: 

Retrieve information about a single cloud file account

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
      :annotation: 
   
      Unique identifier of the account
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`cloudFile.CloudFileAccount`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _cloudFile.getAllAccounts:

getAllAccounts()
----------------

.. api-section-annotation-hack:: 

Retrieve all cloud file accounts for the current add-on

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: array of :ref:`cloudFile.CloudFileAccount`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _cloudFile.updateAccount:

updateAccount(accountId, updateProperties)
------------------------------------------

.. api-section-annotation-hack:: 

Update a cloud file account

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
      :annotation: 
   
      Unique identifier of the account
   
   
   .. api-member::
      :name: ``updateProperties``
      :type: (object)
      :annotation: 
   
      
      .. api-member::
         :name: [``configured``]
         :type: (boolean)
         :annotation: 
      
         If true, the account is configured and ready to use. This property is currently ignored and all accounts are assumed to be configured.
      
      
      .. api-member::
         :name: [``managementUrl``]
         :type: (string)
         :annotation: 
      
         A page for configuring accounts, to be displayed in the preferences UI.
      
      
      .. api-member::
         :name: [``spaceRemaining``]
         :type: (integer)
         :annotation: 
      
         The amount of remaining space on the cloud provider, in bytes. Set to -1 if unsupported.
      
      
      .. api-member::
         :name: [``spaceUsed``]
         :type: (integer)
         :annotation: 
      
         The amount of space already used on the cloud provider, in bytes. Set to -1 if unsupported.
      
      
      .. api-member::
         :name: [``uploadSizeLimit``]
         :type: (integer)
         :annotation: 
      
         The maximum size in bytes for a single file to upload. Set to -1 if unlimited.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`cloudFile.CloudFileAccount`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _cloudFile.onFileUpload:

onFileUpload(account, fileInfo)
-------------------------------

.. api-section-annotation-hack:: 

Fired when a file should be uploaded to the cloud file provider

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``account``
      :type: (:ref:`cloudFile.CloudFileAccount`)
      :annotation: 
   
      The created account
   
   
   .. api-member::
      :name: ``fileInfo``
      :type: (:ref:`cloudFile.CloudFile`)
      :annotation: 
   
      The file to upload
   

.. api-header::
   :label: Expected return value of event listeners

   
   .. api-member::
      :name: 
      :type: object
      :annotation: 
   
      
      .. api-member::
         :name: [``aborted``]
         :type: (boolean)
         :annotation: 
      
         Set this to true if the file upload was aborted
      
      
      .. api-member::
         :name: [``url``]
         :type: (string)
         :annotation: 
      
         The URL where the uploaded file can be accessed
      
   

.. _cloudFile.onFileUploadAbort:

onFileUploadAbort(account, fileId)
----------------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``account``
      :type: (:ref:`cloudFile.CloudFileAccount`)
      :annotation: 
   
      The created account
   
   
   .. api-member::
      :name: ``fileId``
      :type: (integer)
      :annotation: 
   
      An identifier for this file
   

.. _cloudFile.onFileDeleted:

onFileDeleted(account, fileId)
------------------------------

.. api-section-annotation-hack:: 

Fired when a file previously uploaded should be deleted

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``account``
      :type: (:ref:`cloudFile.CloudFileAccount`)
      :annotation: 
   
      The created account
   
   
   .. api-member::
      :name: ``fileId``
      :type: (integer)
      :annotation: 
   
      An identifier for this file
   

.. _cloudFile.onAccountAdded:

onAccountAdded(account)
-----------------------

.. api-section-annotation-hack:: 

Fired when a cloud file account of this add-on was created

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``account``
      :type: (:ref:`cloudFile.CloudFileAccount`)
      :annotation: 
   
      The created account
   

.. _cloudFile.onAccountDeleted:

onAccountDeleted(accountId)
---------------------------

.. api-section-annotation-hack:: 

Fired when a cloud file account of this add-on was deleted

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
      :annotation: 
   
      The id of the removed account
   

.. rst-class:: api-main-section

Types
=====

.. _cloudFile.CloudFile:

CloudFile
---------

.. api-section-annotation-hack:: 

Information about a cloud file

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``data``
      :type: (`ArrayBuffer <https://developer.mozilla.org/en-US/docs/Web/API/ArrayBuffer>`_ or `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`_)
      :annotation: 
   
   
   .. api-member::
      :name: ``id``
      :type: (integer)
      :annotation: 
   
      An identifier for this file
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      :annotation: 
   
      Filename of the file to be transferred
   

.. _cloudFile.CloudFileAccount:

CloudFileAccount
----------------

.. api-section-annotation-hack:: 

Information about a cloud file account

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``configured``
      :type: (boolean)
      :annotation: 
   
      If true, the account is configured and ready to use. This property is currently ignored and all accounts are assumed to be configured.
   
   
   .. api-member::
      :name: ``id``
      :type: (string)
      :annotation: 
   
      Unique identifier of the account
   
   
   .. api-member::
      :name: ``managementUrl``
      :type: (string)
      :annotation: 
   
      A page for configuring accounts, to be displayed in the preferences UI.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      :annotation: 
   
      A user-friendly name for this account.
   
   
   .. api-member::
      :name: [``spaceRemaining``]
      :type: (integer)
      :annotation: 
   
      The amount of remaining space on the cloud provider, in bytes. Set to -1 if unsupported.
   
   
   .. api-member::
      :name: [``spaceUsed``]
      :type: (integer)
      :annotation: 
   
      The amount of space already used on the cloud provider, in bytes. Set to -1 if unsupported.
   
   
   .. api-member::
      :name: [``uploadSizeLimit``]
      :type: (integer)
      :annotation: 
   
      The maximum size in bytes for a single file to upload. Set to -1 if unlimited.
   
