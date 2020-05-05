=======
folders
=======

The folders API first appeared in Thunderbird 68 (see `bug 1531591`__) as a part of the
:doc:`accounts` API. They were later moved here.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1531591

Permissions
===========

- accountsFolders "Create, rename, or delete your mail account folders"

.. note::

  The permission ``accountsFolders`` is required to use ``folders``.

Functions
=========

.. _folders.create:

create(parentFolder, childName)
-------------------------------

Creates a new subfolder of ``parentFolder``.

- ``parentFolder`` (:ref:`folders.MailFolder`)
- ``childName`` (string)

.. _folders.rename:

rename(folder, newName)
-----------------------

Renames a folder.

- ``folder`` (:ref:`folders.MailFolder`)
- ``newName`` (string)

.. _folders.delete:

delete(folder)
--------------

Deletes a folder.

- ``folder`` (:ref:`folders.MailFolder`)

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Types
=====

.. _folders.MailFolder:

MailFolder
----------

A folder object, as returned by the ``list`` and ``get`` methods. Use the accountId and path properties to refer to a folder.

object:

- ``accountId`` (string) The account this folder belongs to.
- ``path`` (string) Path to this folder in the account. Although paths look predictable, never guess a folder's path, as there are a number of reasons why it may not be what you think it is.
- [``name``] (string) The human-friendly name of this folder.
- [``subFolders``] (array of :ref:`folders.MailFolder`) *Added in Thunderbird 74*
- [``type``] (`string <enum_type_10_>`_) The type of folder, for several common types.

.. _enum_type_10:

Values for type:

- ``inbox``
- ``drafts``
- ``sent``
- ``trash``
- ``templates``
- ``archives``
- ``junk``
- ``outbox``
