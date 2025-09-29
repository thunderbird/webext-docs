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

.. hint::

   The storage API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/storage>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.storage` API to store, retrieve, and track changes to user data.

.. note::

   The storage API is supported in content scripts from version 48.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`storage`

   Grant access to some or all methods of the storage API.

Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`storage` is required to use ``messenger.storage.*``.

.. rst-class:: api-main-section

Events
======

.. _storage.onChanged:

onChanged
---------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when one or more items change.

.. api-header::
   :label: Parameters for onChanged.addListener(listener)

   .. api-member::
      :name: ``listener(changes, areaName)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``changes``
      :type: (object)

      Object mapping each key that changed to its corresponding :ref:`storage.StorageChange` for that item.

   .. api-member::
      :name: ``areaName``
      :type: (string)

      The name of the storage area (:code:`"sync"`, :code:`"local"` or :code:`"managed"`) the changes are for.

.. api-header::
   :label: Required permissions

   - :permission:`storage`

.. rst-class:: api-main-section

Types
=====

.. _storage.StorageArea:

StorageArea
-----------

.. api-section-annotation-hack:: -- [Added in TB 45]

.. api-header::
   :label: object

.. _storage.StorageChange:

StorageChange
-------------

.. api-section-annotation-hack:: -- [Added in TB 45]

.. api-header::
   :label: object

   .. _storage.StorageChange.newValue:

   .. api-member::
      :name: [``newValue``]
      :type: (any, optional)

      The new value of the item, if there is a new value.

   .. _storage.StorageChange.oldValue:

   .. api-member::
      :name: [``oldValue``]
      :type: (any, optional)

      The old value of the item, if there was an old value.

.. rst-class:: api-main-section

Properties
==========

.. _storage.local:

local
-----

.. api-section-annotation-hack:: 

Items in the :code:`local` storage area are local to each machine.

.. note::

   The storage API is supported in content scripts from version 48.

.. _storage.managed:

managed
-------

.. api-section-annotation-hack:: 

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

.. api-section-annotation-hack:: 

Items in the :code:`session` storage area are kept in memory, and only until the either browser or extension is closed or reloaded.

.. _storage.sync:

sync
----

.. api-section-annotation-hack:: 

Items in the :code:`sync` storage area are synced by the browser.

.. note::

   Before version 79, storage quota limits are not enforced.
