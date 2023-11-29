.. _cloudFile_api:

=============
cloudFile API
=============

The cloudFile (a.k.a. fileLink) API first appeared in Thunderbird 60. It allows to create a provider to store large attachments in the cloud instead of attaching them directly to the message.

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
      :type: (string, optional) **Deprecated.**
      
      This property is no longer used. The only supported data format for the ``data`` argument in :ref:`cloudFile.onFileUpload` is `File <https://developer.mozilla.org/docs/Web/API/File>`__.
   
   
   .. api-member::
      :name: [``new_account_url``]
      :type: (string, optional) **Deprecated.**
      
      This property was never used.
   
   
   .. api-member::
      :name: [``reuse_uploads``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 98]
      
      If a previously uploaded cloud file attachment is reused at a later time in a different message, Thunderbird may use the already known ``url`` and ``templateInfo`` values without triggering the registered :ref:`cloudFile.onFileUpload` listener again. Setting this option to :value:`false` will always trigger the registered listener, providing the already known values through the ``relatedFileInfo`` parameter of the :ref:`cloudFile.onFileUpload` event, to let the provider decide how to handle these cases.
   
   
   .. api-member::
      :name: [``service_url``]
      :type: (string, optional) **Deprecated.**
      
      This property is no longer used. The ``service_url`` property of the :ref:`cloudFile.CloudFileTemplateInfo` object returned by the :ref:`cloudFile.onFileUpload` event can be used to add a *Learn more about* link to the footer of the cloud file attachment element.
   

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
   

.. _cloudFile.onFileRename:

onFileRename
------------

.. api-section-annotation-hack:: -- [Added in TB 96, backported to TB 91.4.1]

Fired when a previously uploaded file should be renamed.

.. api-header::
   :label: Parameters for onFileRename.addListener(listener)

   
   .. api-member::
      :name: ``listener(account, fileId, newName, tab)``
      
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
      
      An identifier for the file which should be renamed.
   
   
   .. api-member::
      :name: ``newName``
      :type: (string)
      
      The new name of the file.
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      
      The tab where the rename was initiated. Currently only available for the message composer.
   

.. api-header::
   :label: Expected return value of the listener function

   
   .. api-member::
      :type: object
      
      .. api-member::
         :name: [``error``]
         :type: (boolean or string, optional)
         
         Report an error to the user. Set this to :value:`true` for showing a generic error message, or set a specific error message.
      
      
      .. api-member::
         :name: [``url``]
         :type: (string, optional)
         
         The URL where the renamed file can be accessed.
      
   

.. _cloudFile.onFileUpload:

onFileUpload
------------

.. api-section-annotation-hack:: 

Fired when a file should be uploaded to the cloud file provider.

.. api-header::
   :label: Parameters for onFileUpload.addListener(listener)

   
   .. api-member::
      :name: ``listener(account, fileInfo, tab, relatedFileInfo)``
      
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
   
   
   .. api-member::
      :name: [``relatedFileInfo``]
      :type: (:ref:`cloudFile.RelatedCloudFile`, optional)
      :annotation: -- [Added in TB 98]
      
      Information about an already uploaded file, which is related to this upload.
   

.. api-header::
   :label: Expected return value of the listener function

   
   .. api-member::
      :type: object
      
      .. api-member::
         :name: [``aborted``]
         :type: (boolean, optional)
         
         Set this to :value:`true` if the file upload was aborted by the user and an :ref:`cloudFile.onFileUploadAbort` event has been received. No error message will be shown to the user.
      
      
      .. api-member::
         :name: [``error``]
         :type: (boolean or string, optional)
         :annotation: -- [Added in TB 96]
         
         Report an error to the user. Set this to :value:`true` for showing a generic error message, or set a specific error message.
      
      
      .. api-member::
         :name: [``templateInfo``]
         :type: (:ref:`cloudFile.CloudFileTemplateInfo`, optional)
         :annotation: -- [Added in TB 96, backported to TB 91.4.1]
         
         Additional file information used in the cloud file entry added to the message.
      
      
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
      :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__)
      
      Contents of the file to be transferred.
   
   
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

.. api-section-annotation-hack:: -- [Added in TB 97]

Defines information to be used in the cloud file entry added to the message.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``download_expiry_date``]
      :type: (object, optional)
      :annotation: -- [Added in TB 98]
      
      If set, the cloud file entry for this upload will include a hint, that the link will only be available for a limited time.
      
      .. api-member::
         :name: ``timestamp``
         :type: (integer)
         
         The expiry date of the link as the number of milliseconds since the UNIX epoch.
      
      
      .. api-member::
         :name: [``format``]
         :type: (object, optional)
         
         A format options object as used by `Intl.DateTimeFormat <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat>`__. Defaults to: 
         
         .. literalinclude:: includes/cloudFile/defaultDateFormat.js
           :language: JavaScript
         
         
      
   
   
   .. api-member::
      :name: [``download_limit``]
      :type: (integer, optional)
      :annotation: -- [Added in TB 98]
      
      If set, the cloud file entry for this upload will include a hint, that the file has a download limit.
   
   
   .. api-member::
      :name: [``download_password_protected``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 98]
      
      If set to true, the cloud file entry for this upload will include a hint, that the download link is password protected.
   
   
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
      
      A URL pointing to a web page of the used cloud file service. Will be used in a *Learn more about* link in the footer of the cloud file attachment element.
   

.. _cloudFile.RelatedCloudFile:

RelatedCloudFile
----------------

.. api-section-annotation-hack:: 

Information about an already uploaded cloud file, which is related to a new upload. For example if the content of a cloud attachment is updated, if a repeatedly used cloud attachment is renamed (and therefore should be re-uploaded to not invalidate existing links) or if the provider has its manifest property ``reuse_uploads`` set to :value:`false`.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``dataChanged``
      :type: (boolean)
      
      The content of the new upload differs from the related file.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      Filename of the related file.
   
   
   .. api-member::
      :name: [``id``]
      :type: (integer, optional)
      
      The identifier for the related file. In some circumstances, the id is unavailable.
   
   
   .. api-member::
      :name: [``templateInfo``]
      :type: (:ref:`cloudFile.CloudFileTemplateInfo`, optional)
      
      Additional information of the related file, used in the cloud file entry added to the message.
   
   
   .. api-member::
      :name: [``url``]
      :type: (string, optional)
      
      The URL where the upload of the related file can be accessed.
   
