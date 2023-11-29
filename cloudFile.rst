.. _cloudFile_api:

=============
cloudFile API
=============

The cloudFile (a.k.a. fileLink) API first appeared in Thunderbird 60. It allows to create a provider to store large attachments in the cloud instead of attaching them directly to the message.

From Thunderbird 68.2.1 (Thunderbird 71 beta), an extension can choose to receive data for upload
as a `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__ object rather than as an `ArrayBuffer <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer>`__. You **should** specify which you want as
the default may change in a future version.

The `DropBox Uploader`__ sample extension uses this API.

__ https://github.com/thunderbird/sample-extensions/tree/master/dropbox

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``cloud_file``]
   :type: (object, optional)
   
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
      :type: (boolean, optional)
      :annotation: -- [Added in TB 90]
      
      Enable browser styles in the ``management_url`` page. See the `MDN documentation on browser styles <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information.
   
   
   .. api-member::
      :name: [``data_format``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 71, backported to TB 68.2.1]
      
      Determines the format of the ``data`` argument in :ref:`cloudFile.onFileUpload`. Support for :value:`ArrayBuffer` will be removed in Thunderbird 102.
      
      Supported values:
      
      .. api-member::
         :name: :value:`ArrayBuffer`
      
      .. api-member::
         :name: :value:`File`
   
   
   .. api-member::
      :name: [``new_account_url``]
      :type: (string, optional) **Deprecated.**
      
      This property was never used.
   
   
   .. api-member::
      :name: [``service_url``]
      :type: (string, optional)
      
      URL to the web page of the cloud file service.
   

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`cloud_file` is required to use ``messenger.cloudFile.*``.

.. rst-class:: api-main-section

Functions
=========

.. _cloudFile.getAccount:

getAccount(accountId)
---------------------

.. api-section-annotation-hack:: 

Retrieve information about a single cloud file account.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
      
      Unique identifier of the account.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`cloudFile.CloudFileAccount`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _cloudFile.getAllAccounts:

getAllAccounts()
----------------

.. api-section-annotation-hack:: 

Retrieve all cloud file accounts for the current add-on.

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`cloudFile.CloudFileAccount`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _cloudFile.updateAccount:

updateAccount(accountId, updateProperties)
------------------------------------------

.. api-section-annotation-hack:: 

Update a cloud file account.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
      
      Unique identifier of the account.
   
   
   .. api-member::
      :name: ``updateProperties``
      :type: (object)
      
      .. api-member::
         :name: [``configured``]
         :type: (boolean, optional)
         
         If true, the account is configured and ready to use. Only configured accounts are offered to the user.
      
      
      .. api-member::
         :name: [``managementUrl``]
         :type: (string, optional)
         
         A page for configuring accounts, to be displayed in the preferences UI.
      
      
      .. api-member::
         :name: [``spaceRemaining``]
         :type: (integer, optional)
         
         The amount of remaining space on the cloud provider, in bytes. Set to :value:`-1` if unsupported.
      
      
      .. api-member::
         :name: [``spaceUsed``]
         :type: (integer, optional)
         
         The amount of space already used on the cloud provider, in bytes. Set to :value:`-1` if unsupported.
      
      
      .. api-member::
         :name: [``uploadSizeLimit``]
         :type: (integer, optional)
         
         The maximum size in bytes for a single file to upload. Set to :value:`-1` if unlimited.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`cloudFile.CloudFileAccount`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _cloudFile.onFileUpload:

onFileUpload
------------

.. api-section-annotation-hack:: 

Fired when a file should be uploaded to the cloud file provider.

.. api-header::
   :label: Parameters for onFileUpload.addListener(listener)

   
   .. api-member::
      :name: ``listener(account, fileInfo, tab)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``account``
      :type: (:ref:`cloudFile.CloudFileAccount`)
      
      The account used for the file upload.
   
   
   .. api-member::
      :name: ``fileInfo``
      :type: (:ref:`cloudFile.CloudFile`)
      
      The file to upload.
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Added in TB 91]
      
      The tab where the upload was initiated. Currently only available for the message composer.
   

.. api-header::
   :label: Expected return value of the listener function

   
   .. api-member::
      :type: object
      
      .. api-member::
         :name: [``aborted``]
         :type: (boolean, optional)
         
         Set this to :value:`true` if the file upload was aborted by the user and an :ref:`cloudFile.onFileUploadAbort` event has been received. No error message will be shown to the user.
      
      
      .. api-member::
         :name: [``templateInfo``]
         :type: (:ref:`cloudFile.CloudFileTemplateInfo`, optional)
         :annotation: -- [Added in TB 96, backported to TB 91.4.1]
         
         Information to override the default values used in the cloud file message template.
      
      
      .. api-member::
         :name: [``url``]
         :type: (string, optional)
         
         The URL where the uploaded file can be accessed.
      
   

.. _cloudFile.onFileUploadAbort:

onFileUploadAbort
-----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: Parameters for onFileUploadAbort.addListener(listener)

   
   .. api-member::
      :name: ``listener(account, fileId, tab)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``account``
      :type: (:ref:`cloudFile.CloudFileAccount`)
      
      The account used for the file upload.
   
   
   .. api-member::
      :name: ``fileId``
      :type: (integer)
      
      An identifier for this file.
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Added in TB 91]
      
      The tab where the upload was initiated. Currently only available for the message composer.
   

.. _cloudFile.onFileDeleted:

onFileDeleted
-------------

.. api-section-annotation-hack:: 

Fired when a previously uploaded file should be deleted.

.. api-header::
   :label: Parameters for onFileDeleted.addListener(listener)

   
   .. api-member::
      :name: ``listener(account, fileId, tab)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``account``
      :type: (:ref:`cloudFile.CloudFileAccount`)
      
      The account used for the file upload.
   
   
   .. api-member::
      :name: ``fileId``
      :type: (integer)
      
      An identifier for this file.
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Added in TB 91]
      
      The tab where the upload was initiated. Currently only available for the message composer.
   

.. _cloudFile.onAccountAdded:

onAccountAdded
--------------

.. api-section-annotation-hack:: 

Fired when a cloud file account of this add-on was created.

.. api-header::
   :label: Parameters for onAccountAdded.addListener(listener)

   
   .. api-member::
      :name: ``listener(account)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``account``
      :type: (:ref:`cloudFile.CloudFileAccount`)
      
      The created account.
   

.. _cloudFile.onAccountDeleted:

onAccountDeleted
----------------

.. api-section-annotation-hack:: 

Fired when a cloud file account of this add-on was deleted.

.. api-header::
   :label: Parameters for onAccountDeleted.addListener(listener)

   
   .. api-member::
      :name: ``listener(accountId)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
      
      The id of the removed account.
   

.. rst-class:: api-main-section

Types
=====

.. _cloudFile.CloudFile:

CloudFile
---------

.. api-section-annotation-hack:: 

Information about a cloud file.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``data``
      :type: (`ArrayBuffer <https://developer.mozilla.org/en-US/docs/Web/API/ArrayBuffer>`__ or `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__)
   
   
   .. api-member::
      :name: ``id``
      :type: (integer)
      
      An identifier for this file.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      Filename of the file to be transferred.
   

.. _cloudFile.CloudFileAccount:

CloudFileAccount
----------------

.. api-section-annotation-hack:: 

Information about a cloud file account.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``configured``
      :type: (boolean)
      
      If true, the account is configured and ready to use. Only configured accounts are offered to the user.
   
   
   .. api-member::
      :name: ``id``
      :type: (string)
      
      Unique identifier of the account.
   
   
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
      :type: (integer, optional)
      
      The amount of remaining space on the cloud provider, in bytes. Set to :value:`-1` if unsupported.
   
   
   .. api-member::
      :name: [``spaceUsed``]
      :type: (integer, optional)
      
      The amount of space already used on the cloud provider, in bytes. Set to :value:`-1` if unsupported.
   
   
   .. api-member::
      :name: [``uploadSizeLimit``]
      :type: (integer, optional)
      
      The maximum size in bytes for a single file to upload. Set to :value:`-1` if unlimited.
   

.. _cloudFile.CloudFileTemplateInfo:

CloudFileTemplateInfo
---------------------

.. api-section-annotation-hack:: 

Defines information to be used in the cloud file entry added to the message.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``service_icon``]
      :type: (string, optional)
      
      A URL pointing to an icon to represent the used cloud file service. Defaults to the icon of the provider add-on.
   
   
   .. api-member::
      :name: [``service_name``]
      :type: (string, optional)
      
      A name to represent the used cloud file service. Defaults to the associated cloud file account name.
   
   
   .. api-member::
      :name: [``service_url``]
      :type: (string, optional)
      
      An URL to the web page of the used cloud file service. Used to attach a link to the ``service_name``. Defaults to the ``service_url`` manifest entry. Set to an empty string in order to not create a link.
   
