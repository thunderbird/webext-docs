=========
cloudfile
=========

This is preliminary documentation for the cloudFile (a.k.a. fileLink) API being developed in `bug 1481052`__.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1481052

Types
=====

.. _cloudfile.CloudFileAccount:

CloudFileAccount
----------------

Information about a cloud file account

- ``configured`` (boolean)
- ``id`` (string)
- ``managementUrl`` (string)
- ``name`` (string)
- ``settingsUrl`` (string)
- [``spaceRemaining``] (integer) The amount of remaining space on the cloud provider, in bytes. Set to -1 if unsupported.
- [``spaceUsed``] (integer) The amount of space already used on the cloud provider, in bytes. Set to -1 if unsupported.
- [``uploadSizeLimit``] (integer) The maximum size in bytes for a single file to upload. Set to -1 if unlimited.

.. _cloudfile.CloudFile:

CloudFile
---------

Information about a cloud file

- ``data`` (object)
- ``id`` (integer)
- ``name`` (string)

Functions
=========

.. _cloudfile.getAccount:

getAccount(accountId)
---------------------

Retrieve information about a single cloud file account

- ``accountId`` (string)

.. _cloudfile.getAllAccounts:

getAllAccounts()
----------------

Retrieve all cloud file accounts for the current add-on

.. _cloudfile.updateAccount:

updateAccount(accountId, updateProperties)
------------------------------------------

Update a cloud file account

- ``accountId`` (string)
- ``updateProperties`` (object)

  - [``configured``] (boolean) If true, the account is configured and ready to use.
  - [``managementUrl``] (string)
  - [``settingsUrl``] (string)
  - [``spaceRemaining``] (integer) The amount of remaining space on the cloud provider, in bytes. Set to -1 if unsupported.
  - [``spaceUsed``] (integer) The amount of space already used on the cloud provider, in bytes. Set to -1 if unsupported.
  - [``uploadSizeLimit``] (integer) The maximum size in bytes for a single file to upload. Set to -1 if unlimited.

Events
======

.. _cloudfile.onFileUpload:

onFileUpload(account, fileInfo)
-------------------------------

Fired when a file should be uploaded to the cloud file provider

- ``account`` (:ref:`cloudfile.CloudFileAccount`) The created account
- ``fileInfo`` (:ref:`cloudfile.CloudFile`) The file to upload

Event listeners should return:

- (object)

  - [``aborted``] (boolean) Set this to true if the file upload was aborted
  - [``url``] (string) The URL where the uploaded file can be accessed

.. _cloudfile.onFileUploadAbort:

onFileUploadAbort(account, fileId)
----------------------------------

- ``account`` (:ref:`cloudfile.CloudFileAccount`) The created account
- ``fileId`` (integer)

.. _cloudfile.onFileDeleted:

onFileDeleted(account, fileId)
------------------------------

Fired when a file previously uploaded should be deleted

- ``account`` (:ref:`cloudfile.CloudFileAccount`) The created account
- ``fileId`` (integer) An identifier for this file, TODO might go away

.. _cloudfile.onAccountAdded:

onAccountAdded(account)
-----------------------

Fired when a cloud file account of this add-on was created

- ``account`` (:ref:`cloudfile.CloudFileAccount`) The created account

.. _cloudfile.onAccountDeleted:

onAccountDeleted(accountId)
---------------------------

Fired when a cloud file account of this add-on was deleted

- ``accountId`` (string) The id of the removed account
