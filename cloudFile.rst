=========
cloudFile
=========

The cloudFile (a.k.a. fileLink) API first appeared in Thunderbird 64, however it is incomplete.
We also intend to uplift some or all of this API to Thunderbird 60 ESR.

Currently extensions using this API can have one account per provider (thus one per extension)
but it is designed for a future upgrade where multiple accounts per provider are possible.

Manifest file properties
========================

- [``cloud_file``] (object)

  - ``management_url`` (string)
  - ``name`` (string)
  - ``settings_url`` (string)
  - [``new_account_url``] (string)
  - [``service_url``] (string)

Functions
=========

.. _cloudFile.getAccount:

getAccount(accountId)
---------------------

Retrieve information about a single cloud file account

- ``accountId`` (string)

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

- ``accountId`` (string)
- ``updateProperties`` (object)

  - [``configured``] (boolean) If true, the account is configured and ready to use. This property is currently ignored and all accounts are assumed to be configured.
  - [``managementUrl``] (string)
  - [``settingsUrl``] (string)
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
- ``fileId`` (integer)

.. _cloudFile.onFileDeleted:

onFileDeleted(account, fileId)
------------------------------

Fired when a file previously uploaded should be deleted

- ``account`` (:ref:`cloudFile.CloudFileAccount`) The created account
- ``fileId`` (integer) An identifier for this file, TODO might go away

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

- ``data`` (object)
- ``id`` (integer)
- ``name`` (string)

.. _cloudFile.CloudFileAccount:

CloudFileAccount
----------------

Information about a cloud file account

- ``configured`` (boolean) If true, the account is configured and ready to use. This property is currently ignored and all accounts are assumed to be configured.
- ``id`` (string)
- ``managementUrl`` (string)
- ``name`` (string) A user-friendly name for this account.
- ``settingsUrl`` (string)
- [``spaceRemaining``] (integer) The amount of remaining space on the cloud provider, in bytes. Set to -1 if unsupported.
- [``spaceUsed``] (integer) The amount of space already used on the cloud provider, in bytes. Set to -1 if unsupported.
- [``uploadSizeLimit``] (integer) The maximum size in bytes for a single file to upload. Set to -1 if unlimited.
