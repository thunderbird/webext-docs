.. container:: sticky-sidebar

  ≡ cloudFile API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=============
cloudFile API
=============

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

The cloudFile (a.k.a. fileLink) API allows to create a provider to store large attachments in the cloud instead of attaching them directly to the message.

.. rst-class:: api-main-section

Manifest file properties
========================

.. _cloud^file.cloud_file:

.. api-member::
   :name: [``cloud_file``]
   :refid: cloud-file-cloud-file
   :refname: cloud_file
   :type: (object, optional)
   :annotation: -- [Added in TB 64]

   Defines a cloud file provider for uploading large attachments to a remote server.

   .. _cloud^file.cloud_file.management_url:

   .. api-member::
      :name: ``management_url``
      :refid: cloud-file-cloud-file-management-url
      :refname: management_url
      :type: (string)
      :annotation: -- [Added in TB 64]

      A page for configuring accounts, to be displayed in the preferences UI.

      .. note::

         Within this UI only a limited subset of the WebExtension APIs is available: :value:`cloudFile`, :value:`extension`, :value:`i18n`, :value:`runtime`, :value:`storage`. The id of the to be configured cloud file account can be retrieved via :code:`new URL(location.href).searchParams.get('accountId');`.

   .. _cloud^file.cloud_file.name:

   .. api-member::
      :name: ``name``
      :refid: cloud-file-cloud-file-name
      :refname: name
      :type: (string)
      :annotation: -- [Added in TB 64]

      Name of the cloud file service.

   .. _cloud^file.cloud_file.browser_style:

   .. api-member::
      :name: [``browser_style``]
      :refid: cloud-file-cloud-file-browser-style
      :refname: browser_style
      :type: (boolean, optional)
      :annotation: -- [Added in TB 90]

      Enable browser styles in the :value:`management_url` page. See the `MDN documentation on browser styles <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information.

   .. _cloud^file.cloud_file.data_format:

   .. api-member::
      :name: [``data_format``]
      :refid: cloud-file-cloud-file-data-format
      :refname: data_format
      :type: (string, optional) **Deprecated.**
      :annotation: -- [Added in TB 71]

      This property is no longer used. The only supported data format for the :value:`data` argument in :ref:`cloud^file.on^file^upload` is `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__.

   .. _cloud^file.cloud_file.new_account_url:

   .. api-member::
      :name: [``new_account_url``]
      :refid: cloud-file-cloud-file-new-account-url
      :refname: new_account_url
      :type: (string, optional) **Deprecated.**
      :annotation: -- [Added in TB 64]

      This property was never used.

   .. _cloud^file.cloud_file.reuse_uploads:

   .. api-member::
      :name: [``reuse_uploads``]
      :refid: cloud-file-cloud-file-reuse-uploads
      :refname: reuse_uploads
      :type: (boolean, optional)
      :annotation: -- [Added in TB 98]

      If a previously uploaded cloud file attachment is reused at a later time in a different message, Thunderbird may use the already known :value:`url` and :value:`templateInfo` values without triggering the registered :ref:`cloud^file.on^file^upload` listener again. Setting this option to :value:`false` will always trigger the registered listener, providing the already known values through the :value:`relatedFileInfo` parameter of the :ref:`cloud^file.on^file^upload` event, to let the provider decide how to handle these cases.

   .. _cloud^file.cloud_file.service_url:

   .. api-member::
      :name: [``service_url``]
      :refid: cloud-file-cloud-file-service-url
      :refname: service_url
      :type: (string, optional) **Deprecated.**
      :annotation: -- [Added in TB 64]

      This property is no longer used. The :value:`service_url` property of the :ref:`cloud^file.^cloud^file^template^info` object returned by the :ref:`cloud^file.on^file^upload` event can be used to add a *Learn more about* link to the footer of the cloud file attachment element.

.. rst-class:: api-main-section

Permissions
===========

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`cloud_file` is required to use ``messenger.cloudFile.*``.

.. rst-class:: api-main-section

Functions
=========

.. _cloud^file.get^account:

getAccount(accountId)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Retrieve information about a single cloud file account. Returns :value:`undefined`, if the requested account does not exist.

.. api-header::
   :label: Parameters

   .. _cloud^file.get^account.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: cloud-file-get-account-account-id
      :refname: accountId
      :type: (string)

      Unique identifier of the account.

.. api-header::
   :label: Return type (`Promise`_)

   .. _cloud^file.get^account.returns:

   .. api-member::
      :refid: cloud-file-get-account-returns
      :refname: _returns
      :type: :ref:`cloud^file.^cloud^file^account`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _cloud^file.get^all^accounts:

getAllAccounts()
----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Retrieve all cloud file accounts for the current add-on.

.. api-header::
   :label: Return type (`Promise`_)

   .. _cloud^file.get^all^accounts.returns:

   .. api-member::
      :refid: cloud-file-get-all-accounts-returns
      :refname: _returns
      :type: array of :ref:`cloud^file.^cloud^file^account`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _cloud^file.update^account:

updateAccount(accountId, updateProperties)
------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Update a cloud file account. Returns :value:`undefined`, if the requested account does not exist.

.. api-header::
   :label: Parameters

   .. _cloud^file.update^account.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: cloud-file-update-account-account-id
      :refname: accountId
      :type: (string)

      Unique identifier of the account.

   .. _cloud^file.update^account.update^properties:

   .. api-member::
      :name: ``updateProperties``
      :refid: cloud-file-update-account-update-properties
      :refname: updateProperties
      :type: (object)

      .. _cloud^file.update^account.update^properties.configured:

      .. api-member::
         :name: [``configured``]
         :refid: cloud-file-update-account-update-properties-configured
         :refname: configured
         :type: (boolean, optional)

         If true, the account is configured and ready to use. Only configured accounts are offered to the user.

      .. _cloud^file.update^account.update^properties.management^url:

      .. api-member::
         :name: [``managementUrl``]
         :refid: cloud-file-update-account-update-properties-management-url
         :refname: managementUrl
         :type: (string, optional)

         A page for configuring accounts, to be displayed in the preferences UI.

      .. _cloud^file.update^account.update^properties.space^remaining:

      .. api-member::
         :name: [``spaceRemaining``]
         :refid: cloud-file-update-account-update-properties-space-remaining
         :refname: spaceRemaining
         :type: (integer, optional)

         The amount of remaining space on the cloud provider, in bytes. Set to :value:`-1` if unsupported.

      .. _cloud^file.update^account.update^properties.space^used:

      .. api-member::
         :name: [``spaceUsed``]
         :refid: cloud-file-update-account-update-properties-space-used
         :refname: spaceUsed
         :type: (integer, optional)

         The amount of space already used on the cloud provider, in bytes. Set to :value:`-1` if unsupported.

      .. _cloud^file.update^account.update^properties.upload^size^limit:

      .. api-member::
         :name: [``uploadSizeLimit``]
         :refid: cloud-file-update-account-update-properties-upload-size-limit
         :refname: uploadSizeLimit
         :type: (integer, optional)

         The maximum size in bytes for a single file to upload. Set to :value:`-1` if unlimited.

.. api-header::
   :label: Return type (`Promise`_)

   .. _cloud^file.update^account.returns:

   .. api-member::
      :refid: cloud-file-update-account-returns
      :refname: _returns
      :type: :ref:`cloud^file.^cloud^file^account`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _cloud^file.on^account^added:

onAccountAdded
--------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Fired when a cloud file account of this add-on was created.

.. api-header::
   :label: Parameters for onAccountAdded.addListener(listener)

   .. _cloud^file.on^account^added.listener(account):

   .. api-member::
      :name: ``listener(account)``
      :refid: cloud-file-on-account-added-listener-account
      :refname: listener(account)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _cloud^file.on^account^added.account:

   .. api-member::
      :name: ``account``
      :refid: cloud-file-on-account-added-account
      :refname: account
      :type: (:ref:`cloud^file.^cloud^file^account`)

      The created account.

.. _cloud^file.on^account^deleted:

onAccountDeleted
----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Fired when a cloud file account of this add-on was deleted.

.. api-header::
   :label: Parameters for onAccountDeleted.addListener(listener)

   .. _cloud^file.on^account^deleted.listener(account^id):

   .. api-member::
      :name: ``listener(accountId)``
      :refid: cloud-file-on-account-deleted-listener-account-id
      :refname: listener(accountId)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _cloud^file.on^account^deleted.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: cloud-file-on-account-deleted-account-id
      :refname: accountId
      :type: (string)

      The id of the removed account.

.. _cloud^file.on^file^deleted:

onFileDeleted
-------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Fired when a previously uploaded file should be deleted.

.. api-header::
   :label: Parameters for onFileDeleted.addListener(listener)

   .. _cloud^file.on^file^deleted.listener(account, file^id, tab):

   .. api-member::
      :name: ``listener(account, fileId, tab)``
      :refid: cloud-file-on-file-deleted-listener-account-file-id-tab
      :refname: listener(account, fileId, tab)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _cloud^file.on^file^deleted.account:

   .. api-member::
      :name: ``account``
      :refid: cloud-file-on-file-deleted-account
      :refname: account
      :type: (:ref:`cloud^file.^cloud^file^account`)

      The account used for the file upload.

   .. _cloud^file.on^file^deleted.file^id:

   .. api-member::
      :name: ``fileId``
      :refid: cloud-file-on-file-deleted-file-id
      :refname: fileId
      :type: (integer)

      An identifier for this file.

   .. _cloud^file.on^file^deleted.tab:

   .. api-member::
      :name: ``tab``
      :refid: cloud-file-on-file-deleted-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)
      :annotation: -- [Added in TB 91]

      The tab where the upload was initiated. Currently only available for the message composer.

.. _cloud^file.on^file^rename:

onFileRename
------------

.. api-section-annotation-hack:: -- [Added in TB 97]

Fired when a previously uploaded file should be renamed.

.. api-header::
   :label: Parameters for onFileRename.addListener(listener)

   .. _cloud^file.on^file^rename.listener(account, file^id, new^name, tab):

   .. api-member::
      :name: ``listener(account, fileId, newName, tab)``
      :refid: cloud-file-on-file-rename-listener-account-file-id-new-name-tab
      :refname: listener(account, fileId, newName, tab)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _cloud^file.on^file^rename.account:

   .. api-member::
      :name: ``account``
      :refid: cloud-file-on-file-rename-account
      :refname: account
      :type: (:ref:`cloud^file.^cloud^file^account`)

      The account used for the file upload.

   .. _cloud^file.on^file^rename.file^id:

   .. api-member::
      :name: ``fileId``
      :refid: cloud-file-on-file-rename-file-id
      :refname: fileId
      :type: (integer)

      An identifier for the file which should be renamed.

   .. _cloud^file.on^file^rename.new^name:

   .. api-member::
      :name: ``newName``
      :refid: cloud-file-on-file-rename-new-name
      :refname: newName
      :type: (string)

      The new name of the file.

   .. _cloud^file.on^file^rename.tab:

   .. api-member::
      :name: ``tab``
      :refid: cloud-file-on-file-rename-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

      The tab where the rename was initiated. Currently only available for the message composer.

.. api-header::
   :label: Expected return value of the listener function

   .. _cloud^file.on^file^rename.returns:

   .. api-member::
      :refid: cloud-file-on-file-rename-returns
      :type: object

      .. _cloud^file.on^file^rename.returns.error:

      .. api-member::
         :name: [``error``]
         :refid: cloud-file-on-file-rename-returns-error
         :refname: error
         :type: (boolean or string, optional)

         Report an error to the user. Set this to :value:`true` for showing a generic error message, or set a specific error message.

      .. _cloud^file.on^file^rename.returns.url:

      .. api-member::
         :name: [``url``]
         :refid: cloud-file-on-file-rename-returns-url
         :refname: url
         :type: (string, optional)

         The URL where the renamed file can be accessed.

.. _cloud^file.on^file^upload:

onFileUpload
------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Fired when a file should be uploaded to the cloud file provider.

.. api-header::
   :label: Parameters for onFileUpload.addListener(listener)

   .. _cloud^file.on^file^upload.listener(account, file^info, tab, related^file^info):

   .. api-member::
      :name: ``listener(account, fileInfo, tab, relatedFileInfo)``
      :refid: cloud-file-on-file-upload-listener-account-file-info-tab-related-file-info
      :refname: listener(account, fileInfo, tab, relatedFileInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _cloud^file.on^file^upload.account:

   .. api-member::
      :name: ``account``
      :refid: cloud-file-on-file-upload-account
      :refname: account
      :type: (:ref:`cloud^file.^cloud^file^account`)

      The account used for the file upload.

   .. _cloud^file.on^file^upload.file^info:

   .. api-member::
      :name: ``fileInfo``
      :refid: cloud-file-on-file-upload-file-info
      :refname: fileInfo
      :type: (:ref:`cloud^file.^cloud^file`)

      The file to upload.

   .. _cloud^file.on^file^upload.tab:

   .. api-member::
      :name: ``tab``
      :refid: cloud-file-on-file-upload-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)
      :annotation: -- [Added in TB 91]

      The tab where the upload was initiated. Currently only available for the message composer.

   .. _cloud^file.on^file^upload.related^file^info:

   .. api-member::
      :name: [``relatedFileInfo``]
      :refid: cloud-file-on-file-upload-related-file-info
      :refname: relatedFileInfo
      :type: (:ref:`cloud^file.^related^cloud^file`, optional)
      :annotation: -- [Added in TB 98]

      Information about an already uploaded file, which is related to this upload.

.. api-header::
   :label: Expected return value of the listener function

   .. _cloud^file.on^file^upload.returns:

   .. api-member::
      :refid: cloud-file-on-file-upload-returns
      :type: object

      .. _cloud^file.on^file^upload.returns.aborted:

      .. api-member::
         :name: [``aborted``]
         :refid: cloud-file-on-file-upload-returns-aborted
         :refname: aborted
         :type: (boolean, optional)

         Set this to :value:`true` if the file upload was aborted by the user and an :ref:`cloud^file.on^file^upload^abort` event has been received. No error message will be shown to the user.

      .. _cloud^file.on^file^upload.returns.error:

      .. api-member::
         :name: [``error``]
         :refid: cloud-file-on-file-upload-returns-error
         :refname: error
         :type: (boolean or string, optional)
         :annotation: -- [Added in TB 97]

         Report an error to the user. Set this to :value:`true` for showing a generic error message, or set a specific error message.

      .. _cloud^file.on^file^upload.returns.template^info:

      .. api-member::
         :name: [``templateInfo``]
         :refid: cloud-file-on-file-upload-returns-template-info
         :refname: templateInfo
         :type: (:ref:`cloud^file.^cloud^file^template^info`, optional)
         :annotation: -- [Added in TB 96]

         Additional file information used in the cloud file entry added to the message.

      .. _cloud^file.on^file^upload.returns.url:

      .. api-member::
         :name: [``url``]
         :refid: cloud-file-on-file-upload-returns-url
         :refname: url
         :type: (string, optional)

         The URL where the uploaded file can be accessed.

.. _cloud^file.on^file^upload^abort:

onFileUploadAbort
-----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

.. api-header::
   :label: Parameters for onFileUploadAbort.addListener(listener)

   .. _cloud^file.on^file^upload^abort.listener(account, file^id, tab):

   .. api-member::
      :name: ``listener(account, fileId, tab)``
      :refid: cloud-file-on-file-upload-abort-listener-account-file-id-tab
      :refname: listener(account, fileId, tab)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _cloud^file.on^file^upload^abort.account:

   .. api-member::
      :name: ``account``
      :refid: cloud-file-on-file-upload-abort-account
      :refname: account
      :type: (:ref:`cloud^file.^cloud^file^account`)

      The account used for the file upload.

   .. _cloud^file.on^file^upload^abort.file^id:

   .. api-member::
      :name: ``fileId``
      :refid: cloud-file-on-file-upload-abort-file-id
      :refname: fileId
      :type: (integer)

      An identifier for this file.

   .. _cloud^file.on^file^upload^abort.tab:

   .. api-member::
      :name: ``tab``
      :refid: cloud-file-on-file-upload-abort-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)
      :annotation: -- [Added in TB 91]

      The tab where the upload was initiated. Currently only available for the message composer.

.. rst-class:: api-main-section

Types
=====

.. _cloud^file.^cloud^file:

CloudFile
---------

.. api-section-annotation-hack:: -- [Added in TB 64]

Information about a cloud file.

.. api-header::
   :label: object

   .. _cloud^file.^cloud^file.data:

   .. api-member::
      :name: ``data``
      :refid: cloud-file-cloud-file-data
      :refname: data
      :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__)

      Contents of the file to be transferred.

   .. _cloud^file.^cloud^file.id:

   .. api-member::
      :name: ``id``
      :refid: cloud-file-cloud-file-id
      :refname: id
      :type: (integer)

      An identifier for this file.

   .. _cloud^file.^cloud^file.name:

   .. api-member::
      :name: ``name``
      :refid: cloud-file-cloud-file-name
      :refname: name
      :type: (string)

      Filename of the file to be transferred.

.. _cloud^file.^cloud^file^account:

CloudFileAccount
----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Information about a cloud file account.

.. api-header::
   :label: object

   .. _cloud^file.^cloud^file^account.configured:

   .. api-member::
      :name: ``configured``
      :refid: cloud-file-cloud-file-account-configured
      :refname: configured
      :type: (boolean)

      If true, the account is configured and ready to use. Only configured accounts are offered to the user.

   .. _cloud^file.^cloud^file^account.id:

   .. api-member::
      :name: ``id``
      :refid: cloud-file-cloud-file-account-id
      :refname: id
      :type: (string)

      Unique identifier of the account.

   .. _cloud^file.^cloud^file^account.management^url:

   .. api-member::
      :name: ``managementUrl``
      :refid: cloud-file-cloud-file-account-management-url
      :refname: managementUrl
      :type: (string)

      A page for configuring accounts, to be displayed in the preferences UI.

   .. _cloud^file.^cloud^file^account.name:

   .. api-member::
      :name: ``name``
      :refid: cloud-file-cloud-file-account-name
      :refname: name
      :type: (string)

      A user-friendly name for this account.

   .. _cloud^file.^cloud^file^account.space^remaining:

   .. api-member::
      :name: [``spaceRemaining``]
      :refid: cloud-file-cloud-file-account-space-remaining
      :refname: spaceRemaining
      :type: (integer, optional)

      The amount of remaining space on the cloud provider, in bytes. Set to :value:`-1` if unsupported.

   .. _cloud^file.^cloud^file^account.space^used:

   .. api-member::
      :name: [``spaceUsed``]
      :refid: cloud-file-cloud-file-account-space-used
      :refname: spaceUsed
      :type: (integer, optional)

      The amount of space already used on the cloud provider, in bytes. Set to :value:`-1` if unsupported.

   .. _cloud^file.^cloud^file^account.upload^size^limit:

   .. api-member::
      :name: [``uploadSizeLimit``]
      :refid: cloud-file-cloud-file-account-upload-size-limit
      :refname: uploadSizeLimit
      :type: (integer, optional)

      The maximum size in bytes for a single file to upload. Set to :value:`-1` if unlimited.

.. _cloud^file.^cloud^file^template^info:

CloudFileTemplateInfo
---------------------

.. api-section-annotation-hack:: -- [Added in TB 96]

Defines information to be used in the cloud file entry added to the message.

.. api-header::
   :label: object

   .. _cloud^file.^cloud^file^template^info.download_expiry_date:

   .. api-member::
      :name: [``download_expiry_date``]
      :refid: cloud-file-cloud-file-template-info-download-expiry-date
      :refname: download_expiry_date
      :type: (object, optional)
      :annotation: -- [Added in TB 97]

      If set, the cloud file entry for this upload will include a hint, that the link will only be available for a limited time.

      .. _cloud^file.^cloud^file^template^info.download_expiry_date.timestamp:

      .. api-member::
         :name: ``timestamp``
         :refid: cloud-file-cloud-file-template-info-download-expiry-date-timestamp
         :refname: timestamp
         :type: (integer)
         :annotation: -- [Added in TB 97]

         The expiry date of the link as the number of milliseconds since the UNIX epoch.

      .. _cloud^file.^cloud^file^template^info.download_expiry_date.format:

      .. api-member::
         :name: [``format``]
         :refid: cloud-file-cloud-file-template-info-download-expiry-date-format
         :refname: format
         :type: (object, optional)
         :annotation: -- [Added in TB 97]

         A format options object as used by `Intl.DateTimeFormat <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat>`__.

         Defaults to:

         .. code-block:: JSON

            {
              "day": "2-digit",
              "month": "2-digit",
              "year": "numeric",
              "hour": "2-digit",
              "minute": "2-digit",
              "timeZoneName": "short"
            }

   .. _cloud^file.^cloud^file^template^info.download_limit:

   .. api-member::
      :name: [``download_limit``]
      :refid: cloud-file-cloud-file-template-info-download-limit
      :refname: download_limit
      :type: (integer, optional)
      :annotation: -- [Added in TB 97]

      If set, the cloud file entry for this upload will include a hint, that the file has a download limit.

   .. _cloud^file.^cloud^file^template^info.download_password_protected:

   .. api-member::
      :name: [``download_password_protected``]
      :refid: cloud-file-cloud-file-template-info-download-password-protected
      :refname: download_password_protected
      :type: (boolean, optional)
      :annotation: -- [Added in TB 97]

      If set to true, the cloud file entry for this upload will include a hint, that the download link is password protected.

   .. _cloud^file.^cloud^file^template^info.service_icon:

   .. api-member::
      :name: [``service_icon``]
      :refid: cloud-file-cloud-file-template-info-service-icon
      :refname: service_icon
      :type: (string, optional)

      A URL pointing to an icon to represent the used cloud file service. Defaults to the icon of the provider add-on.

   .. _cloud^file.^cloud^file^template^info.service_name:

   .. api-member::
      :name: [``service_name``]
      :refid: cloud-file-cloud-file-template-info-service-name
      :refname: service_name
      :type: (string, optional)

      A name to represent the used cloud file service. Defaults to the associated cloud file account name.

   .. _cloud^file.^cloud^file^template^info.service_url:

   .. api-member::
      :name: [``service_url``]
      :refid: cloud-file-cloud-file-template-info-service-url
      :refname: service_url
      :type: (string, optional)

      A URL pointing to a web page of the used cloud file service. Will be used in a *Learn more about* link in the footer of the cloud file attachment element.

.. _cloud^file.^related^cloud^file:

RelatedCloudFile
----------------

.. api-section-annotation-hack:: -- [Added in TB 98]

Information about an already uploaded cloud file, which is related to a new upload. For example if the content of a cloud attachment is updated, if a repeatedly used cloud attachment is renamed (and therefore should be re-uploaded to not invalidate existing links) or if the provider has its manifest property :value:`reuse_uploads` set to :value:`false`.

.. api-header::
   :label: object

   .. _cloud^file.^related^cloud^file.data^changed:

   .. api-member::
      :name: ``dataChanged``
      :refid: cloud-file-related-cloud-file-data-changed
      :refname: dataChanged
      :type: (boolean)

      The content of the new upload differs from the related file.

   .. _cloud^file.^related^cloud^file.name:

   .. api-member::
      :name: ``name``
      :refid: cloud-file-related-cloud-file-name
      :refname: name
      :type: (string)

      Filename of the related file.

   .. _cloud^file.^related^cloud^file.id:

   .. api-member::
      :name: [``id``]
      :refid: cloud-file-related-cloud-file-id
      :refname: id
      :type: (integer, optional)

      The identifier for the related file. In some circumstances, the id is unavailable.

   .. _cloud^file.^related^cloud^file.template^info:

   .. api-member::
      :name: [``templateInfo``]
      :refid: cloud-file-related-cloud-file-template-info
      :refname: templateInfo
      :type: (:ref:`cloud^file.^cloud^file^template^info`, optional)

      Additional information of the related file, used in the cloud file entry added to the message.

   .. _cloud^file.^related^cloud^file.url:

   .. api-member::
      :name: [``url``]
      :refid: cloud-file-related-cloud-file-url
      :refname: url
      :type: (string, optional)

      The URL where the upload of the related file can be accessed.
