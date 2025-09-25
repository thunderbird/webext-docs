.. container:: sticky-sidebar

  ≡ permissions API

  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

===============
permissions API
===============

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Functions
=========

.. _permissions.contains:

contains(permissions)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 55]

Check if the extension has the given permissions.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``permissions``
      :type: (:ref:`permissions.AnyPermissions`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: boolean

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _permissions.getAll:

getAll()
--------

.. api-section-annotation-hack:: -- [Added in TB 55]

Get a list of all the extension's permissions.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`permissions.AnyPermissions`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _permissions.remove:

remove(permissions)
-------------------

.. api-section-annotation-hack:: -- [Added in TB 55]

Relinquish the given permissions.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``permissions``
      :type: (:ref:`permissions.Permissions`)

.. _permissions.request:

request(permissions)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 55]

Request the given permissions.

.. note::

   It's not possible to request permissions from within DevTools (`bug 1796933 <https://bugzil.la/1796933>`__).

.. note::

   Before version 101, permissions cannot be requested from a sidebar document (`bug 1493396 <https://bugzil.la/1493396>`__).

.. note::

   Before version 75, permissions cannot be requested from popup panels (see `bug 1432083 <https://bugzil.la/1432083>`__).

.. note::

   Before version 61, permissions cannot be requested from options pages embedded in :code:`about:addons` (see `bug 1382953 <https://bugzil.la/1382953>`__).

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``permissions``
      :type: (:ref:`permissions.Permissions`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: boolean

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _permissions.onAdded:

onAdded
-------

.. api-section-annotation-hack:: -- [Added in TB 77]

Fired when the extension acquires new permissions.

.. api-header::
   :label: Parameters for onAdded.addListener(listener)

   .. api-member::
      :name: ``listener(permissions)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``permissions``
      :type: (:ref:`permissions.Permissions`)

.. _permissions.onRemoved:

onRemoved
---------

.. api-section-annotation-hack:: -- [Added in TB 77]

Fired when permissions are removed from the extension.

.. api-header::
   :label: Parameters for onRemoved.addListener(listener)

   .. api-member::
      :name: ``listener(permissions)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``permissions``
      :type: (:ref:`permissions.Permissions`)

.. rst-class:: api-main-section

Types
=====

.. _permissions.MatchPattern:

MatchPattern
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`<all_urls>`

OR

.. api-header::
   :label: :ref:`permissions.MatchPatternRestricted`

OR

.. api-header::
   :label: :ref:`permissions.MatchPatternUnestricted`

.. _permissions.OptionalDataCollectionPermission:

OptionalDataCollectionPermission
--------------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: :ref:`permissions.CommonDataCollectionPermission`

OR

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`technicalAndInteraction`

.. _permissions.OptionalOnlyPermission:

OptionalOnlyPermission
----------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

.. _permissions.OptionalPermission:

OptionalPermission
------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: :ref:`permissions.OptionalPermissionNoPrompt`

OR

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`clipboardRead`

         .. api-member::
            :name: :value:`clipboardWrite`

         .. api-member::
            :name: :value:`geolocation`

         .. api-member::
            :name: :value:`notifications`

.. _permissions.Permission:

Permission
----------

.. api-section-annotation-hack:: 

.. api-header::
   :label: :ref:`permissions.PermissionNoPrompt`

OR

.. api-header::
   :label: :ref:`permissions.OptionalPermission`

.. _permissions.AnyPermissions:

AnyPermissions
--------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. api-member::
      :name: [``data_collection``]
      :type: (array of :ref:`permissions.OptionalDataCollectionPermission`, optional)

   .. api-member::
      :name: [``origins``]
      :type: (array of :ref:`permissions.MatchPattern`, optional)

   .. api-member::
      :name: [``permissions``]
      :type: (array of :ref:`permissions.Permission` or :ref:`permissions.OptionalOnlyPermission`, optional)

.. _permissions.Permissions:

Permissions
-----------

.. api-section-annotation-hack:: -- [Added in TB 55]

.. api-header::
   :label: object

   .. api-member::
      :name: [``data_collection``]
      :type: (array of :ref:`permissions.OptionalDataCollectionPermission`, optional)

   .. api-member::
      :name: [``origins``]
      :type: (array of :ref:`permissions.MatchPattern`, optional)

   .. api-member::
      :name: [``permissions``]
      :type: (array of :ref:`permissions.OptionalPermission` or :ref:`permissions.OptionalOnlyPermission`, optional)
