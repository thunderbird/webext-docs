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

Manifest file properties
========================

- [``cloud_file``] (object)

  - ``management_url`` (string) A page for configuring accounts, to be displayed in the preferences UI. **Note:** Within this UI only a limited subset of the WebExtension APIs is available: cloudFile, extension, i18n, runtime, storage, test.
  - ``name`` (string) Name of the cloud file service.
  - [``data_format``] (`string <enum_data_format_3_>`_) Determines the format of the ``data`` argument in ``onFileUpload``. *Added in Thunderbird 71, backported to 68.2.1*
  - [``new_account_url``] (string) **Deprecated.** This property was never used.
  - [``service_url``] (string) URL to the web page of the cloud file service.

.. _enum_data_format_3:

Values for data_format:

- ``ArrayBuffer``
- ``File``

.. note::

  A manifest entry named ``cloud_file`` is required to use ``cloudFile``.

Functions
=========

.. _cloudFile.getAccount:

getAccount(accountId)
---------------------

Retrieve information about a single cloud file account

- ``accountId`` (string) Unique identifier of the account

Returns a `Promise`_ fulfilled with:

- :ref:`cloudFile.CloudFileAccount`

.. _cloudFile.getAllAccounts:

getAllAccounts()
----------------

Retrieve all cloud file accounts for the current add-on

Returns a `Promise`_ fulfilled with:

- array of :ref:`cloudFile.CloudFileAccount`

.. _cloudFile.updateAccount:

updateAccount(accountId, updateProperties)
------------------------------------------

Update a cloud file account

- ``accountId`` (string) Unique identifier of the account
- ``updateProperties`` (object)

  - [``configured``] (boolean) If true, the account is configured and ready to use. This property is currently ignored and all accounts are assumed to be configured.
  - [``managementUrl``] (string) A page for configuring accounts, to be displayed in the preferences UI.
  - [``spaceRemaining``] (integer) The amount of remaining space on the cloud provider, in bytes. Set to -1 if unsupported.
  - [``spaceUsed``] (integer) The amount of space already used on the cloud provider, in bytes. Set to -1 if unsupported.
  - [``uploadSizeLimit``] (integer) The maximum size in bytes for a single file to upload. Set to -1 if unlimited.

Returns a `Promise`_ fulfilled with:

- :ref:`cloudFile.CloudFileAccount`

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Events
======

.. _cloudFile.onFileUpload:

onFileUpload(account, fileInfo)
-------------------------------

Fired when a file should be uploaded to the cloud file provider

- ``account`` (:ref:`cloudFile.CloudFileAccount`) The created account
- ``fileInfo`` (:ref:`cloudFile.CloudFile`) The file to upload

Event listeners should return:

- object

  - [``aborted``] (boolean) Set this to true if the file upload was aborted
  - [``url``] (string) The URL where the uploaded file can be accessed

.. _cloudFile.onFileUploadAbort:

onFileUploadAbort(account, fileId)
----------------------------------

- ``account`` (:ref:`cloudFile.CloudFileAccount`) The created account
- ``fileId`` (integer) An identifier for this file

.. _cloudFile.onFileDeleted:

onFileDeleted(account, fileId)
------------------------------

Fired when a file previously uploaded should be deleted

- ``account`` (:ref:`cloudFile.CloudFileAccount`) The created account
- ``fileId`` (integer) An identifier for this file

.. _cloudFile.onAccountAdded:

onAccountAdded(account)
-----------------------

Fired when a cloud file account of this add-on was created

- ``account`` (:ref:`cloudFile.CloudFileAccount`) The created account

.. _cloudFile.onAccountDeleted:

onAccountDeleted(accountId)
---------------------------

Fired when a cloud file account of this add-on was deleted

- ``accountId`` (string) The id of the removed account

Types
=====

.. _cloudFile.CloudFile:

CloudFile
---------

Information about a cloud file

object

- ``data`` (`ArrayBuffer <https://developer.mozilla.org/en-US/docs/Web/API/ArrayBuffer>`_ or `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`_)
- ``id`` (integer) An identifier for this file
- ``name`` (string) Filename of the file to be transferred

.. _cloudFile.CloudFileAccount:

CloudFileAccount
----------------

Information about a cloud file account

object

- ``configured`` (boolean) If true, the account is configured and ready to use. This property is currently ignored and all accounts are assumed to be configured.
- ``id`` (string) Unique identifier of the account
- ``managementUrl`` (string) A page for configuring accounts, to be displayed in the preferences UI.
- ``name`` (string) A user-friendly name for this account.
- [``spaceRemaining``] (integer) The amount of remaining space on the cloud provider, in bytes. Set to -1 if unsupported.
- [``spaceUsed``] (integer) The amount of space already used on the cloud provider, in bytes. Set to -1 if unsupported.
- [``uploadSizeLimit``] (integer) The maximum size in bytes for a single file to upload. Set to -1 if unlimited.
