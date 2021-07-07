.. _cloudFile_api:

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

.. role:: permission

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``cloud_file``]
   :type: (object)
   
   .. api-member::
      :name: ``management_url``
      :type: (string)
      
      A page for configuring accounts, to be displayed in the preferences UI. **Note:** Within this UI only a limited subset of the WebExtension APIs is available: ``cloudFile``, ``extension``, ``i18n``, ``runtime``, ``storage``, ``test``.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      Name of the cloud file service.
   
   
   .. api-member::
      :name: [``browser_style``]
      :type: (boolean)
      :annotation: -- [Added in TB 90]
      
      Enable browser styles. See the `MDN documentation <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information.
   
   
   .. api-member::
      :name: [``data_format``]
      :type: (`string`)
      :annotation: -- [Added in TB 71, backported to TB 68.2.1]
      
      Determines the format of the ``data`` argument in ``onFileUpload``.
      
      Supported values:
      
      .. api-member::
         :name: ``ArrayBuffer``
      
      .. api-member::
         :name: ``File``
   
   
   .. api-member::
      :name: [``new_account_url``]
      :type: (string) **Deprecated.**
      
      This property was never used.
   
   
   .. api-member::
      :name: [``service_url``]
      :type: (string)
      
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
      
      Unique identifier of the account
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`cloudFile.CloudFileAccount`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _cloudFile.getAllAccounts:

getAllAccounts()
----------------

.. api-section-annotation-hack:: 

Retrieve all cloud file accounts for the current add-on

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`cloudFile.CloudFileAccount`
   
   
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
      
      Unique identifier of the account
   
   
   .. api-member::
      :name: ``updateProperties``
      :type: (object)
      
      .. api-member::
         :name: [``configured``]
         :type: (boolean)
         
         If true, the account is configured and ready to use. Only configured accounts are offered to the user.
      
      
      .. api-member::
         :name: [``managementUrl``]
         :type: (string)
         
         A page for configuring accounts, to be displayed in the preferences UI.
      
      
      .. api-member::
         :name: [``spaceRemaining``]
         :type: (integer)
         
         The amount of remaining space on the cloud provider, in bytes. Set to -1 if unsupported.
      
      
      .. api-member::
         :name: [``spaceUsed``]
         :type: (integer)
         
         The amount of space already used on the cloud provider, in bytes. Set to -1 if unsupported.
      
      
      .. api-member::
         :name: [``uploadSizeLimit``]
         :type: (integer)
         
         The maximum size in bytes for a single file to upload. Set to -1 if unlimited.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`cloudFile.CloudFileAccount`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _cloudFile.onFileUpload:

onFileUpload(account, fileInfo, tab)
------------------------------------

.. api-section-annotation-hack:: 

Fired when a file should be uploaded to the cloud file provider

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``account``
      :type: (:ref:`cloudFile.CloudFileAccount`)
      
      The created account
   
   
   .. api-member::
      :name: ``fileInfo``
      :type: (:ref:`cloudFile.CloudFile`)
      
      The file to upload
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Added in TB 91]
      
      The tab where the upload was initiated. Currently only available for the message composer.
   

.. api-header::
   :label: Expected return value of event listeners

   
   .. api-member::
      :type: object
      
      .. api-member::
         :name: [``aborted``]
         :type: (boolean)
         
         Set this to true if the file upload was aborted
      
      
      .. api-member::
         :name: [``url``]
         :type: (string)
         
         The URL where the uploaded file can be accessed
      
   

.. _cloudFile.onFileUploadAbort:

onFileUploadAbort(account, fileId, tab)
---------------------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``account``
      :type: (:ref:`cloudFile.CloudFileAccount`)
      
      The created account
   
   
   .. api-member::
      :name: ``fileId``
      :type: (integer)
      
      An identifier for this file
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Added in TB 91]
      
      The tab where the upload was initiated. Currently only available for the message composer.
   

.. _cloudFile.onFileDeleted:

onFileDeleted(account, fileId, tab)
-----------------------------------

.. api-section-annotation-hack:: 

Fired when a file previously uploaded should be deleted

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``account``
      :type: (:ref:`cloudFile.CloudFileAccount`)
      
      The created account
   
   
   .. api-member::
      :name: ``fileId``
      :type: (integer)
      
      An identifier for this file
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Added in TB 91]
      
      The tab where the upload was initiated. Currently only available for the message composer.
   

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
   
   
   .. api-member::
      :name: ``id``
      :type: (integer)
      
      An identifier for this file
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      
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
      
      If true, the account is configured and ready to use. Only configured accounts are offered to the user.
   
   
   .. api-member::
      :name: ``id``
      :type: (string)
      
      Unique identifier of the account
   
   
   .. api-member::
      :name: ``managementUrl``
      :type: (string)
      
      A page for configuring accounts, to be displayed in the preferences UI.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      A user-friendly name for this account.
   
   
   .. api-member::
      :name: [``spaceRemaining``]
      :type: (integer)
      
      The amount of remaining space on the cloud provider, in bytes. Set to -1 if unsupported.
   
   
   .. api-member::
      :name: [``spaceUsed``]
      :type: (integer)
      
      The amount of space already used on the cloud provider, in bytes. Set to -1 if unsupported.
   
   
   .. api-member::
      :name: [``uploadSizeLimit``]
      :type: (integer)
      
      The maximum size in bytes for a single file to upload. Set to -1 if unlimited.
   
