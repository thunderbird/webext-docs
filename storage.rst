.. container:: sticky-sidebar

  ≡ storage API

  * `Permissions`_
  * `Events`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

===========
storage API
===========

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The storage API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/storage>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.storage` API to store, retrieve, and track changes to user data.

.. note::

   The storage API is supported in content scripts from version 48.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _storage.permission.storage:

.. api-member::
   :name: :permission:`storage`
   :refid: storage-permission-storage
   :refname: storage

   Grant access to some or all methods of the storage API.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`storage` is required to use ``messenger.storage.*``.

.. rst-class:: api-main-section

Events
======

.. _storage.on^changed:

onChanged
---------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when one or more items change.

.. api-header::
   :label: Parameters for onChanged.addListener(listener)

   .. _storage.on^changed.listener(changes, area^name):

   .. api-member::
      :name: ``listener(changes, areaName)``
      :refid: storage-on-changed-listener-changes-area-name
      :refname: listener(changes, areaName)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _storage.on^changed.changes:

   .. api-member::
      :name: ``changes``
      :refid: storage-on-changed-changes
      :refname: changes
      :type: (object)

      Object mapping each key that changed to its corresponding :ref:`storage.^storage^change` for that item.

   .. _storage.on^changed.area^name:

   .. api-member::
      :name: ``areaName``
      :refid: storage-on-changed-area-name
      :refname: areaName
      :type: (string)

      The name of the storage area (:code:`"sync"`, :code:`"local"` or :code:`"managed"`) the changes are for.

.. api-header::
   :label: Required permissions

   - :permission:`storage`

.. rst-class:: api-main-section

Types
=====

.. _storage.^storage^area:

StorageArea
-----------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

.. api-header::
   :label: object

.. _storage.^storage^area^with^usage:

StorageAreaWithUsage
--------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

.. _storage.^storage^change:

StorageChange
-------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

.. api-header::
   :label: object

   .. _storage.^storage^change.new^value:

   .. api-member::
      :name: [``newValue``]
      :refid: storage-storage-change-new-value
      :refname: newValue
      :type: (any, optional)

      The new value of the item, if there is a new value.

   .. _storage.^storage^change.old^value:

   .. api-member::
      :name: [``oldValue``]
      :refid: storage-storage-change-old-value
      :refname: oldValue
      :type: (any, optional)

      The old value of the item, if there was an old value.

.. rst-class:: api-main-section

Properties
==========

.. _storage.local:

local
-----

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Items in the :code:`local` storage area are local to each machine.

.. note::

   The storage API is supported in content scripts from version 48.

.. _storage.managed:

managed
-------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Items in the :code:`managed` storage area are set by administrators or native applications, and are read-only for the extension; trying to modify this namespace results in an error.

.. note::

   Platform-specific storage backends, such as Windows registry keys, are not supported.

.. note::

   Enforcement of extension-provided storage schemas is not supported.

.. note::

   The :code:`onChanged` event is not supported.

.. _storage.session:

session
-------

.. api-section-annotation-hack:: -- [Added in TB 115.0]

Items in the :code:`session` storage area are kept in memory, and only until the either browser or extension is closed or reloaded.

.. _storage.sync:

sync
----

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Items in the :code:`sync` storage area are synced by the browser.

.. note::

   Before version 79, storage quota limits are not enforced.
