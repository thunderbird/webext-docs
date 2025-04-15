.. container:: sticky-sidebar

  ≡ storage API

  * `Events`_
  * `Types`_
  * `Properties`_

  .. include:: /overlay/developer-resources.rst

===========
storage API
===========

.. role:: permission

.. role:: value

.. role:: code

Use the :code:`browser.storage` API to store, retrieve, and track changes to user data.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`storage` is required to use ``messenger.storage.*``.

.. rst-class:: api-main-section

Events
======

.. _storage.onChanged:

onChanged
---------

.. api-section-annotation-hack:: 

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

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   - ``clear([callback])`` Removes all items from storage.
   - ``get([keys], callback)`` Gets one or more items from storage.
   - ``getBytesInUse([keys], callback)`` Gets the amount of space (in bytes) being used by one or more items.
   - ``remove(keys, [callback])`` Removes one or more items from storage.
   - ``set(items, [callback])`` Sets multiple items.

.. _storage.StorageAreaWithUsage:

StorageAreaWithUsage
--------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   - ``clear([callback])`` Removes all items from storage.
   - ``get([keys], callback)`` Gets one or more items from storage.
   - ``getBytesInUse([keys], callback)`` Gets the amount of space (in bytes) being used by one or more items.
   - ``remove(keys, [callback])`` Removes one or more items from storage.
   - ``set(items, [callback])`` Sets multiple items.

.. _storage.StorageChange:

StorageChange
-------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``newValue``]
      :type: (any, optional)
      
      The new value of the item, if there is a new value.
   
   
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

.. _storage.managed:

managed
-------

.. api-section-annotation-hack:: 

Items in the :code:`managed` storage area are set by administrators or native applications, and are read-only for the extension; trying to modify this namespace results in an error.

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
