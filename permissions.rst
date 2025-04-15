.. container:: sticky-sidebar

  ≡ permissions API

  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /overlay/developer-resources.rst

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

.. api-section-annotation-hack:: 

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

.. api-section-annotation-hack:: 

Get a list of all the extension's permissions.

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`permissions.AnyPermissions`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _permissions.remove:

remove(permissions)
-------------------

.. api-section-annotation-hack:: 

Relinquish the given permissions.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``permissions``
      :type: (:ref:`permissions.Permissions`)
   

.. _permissions.request:

request(permissions)
--------------------

.. api-section-annotation-hack:: 

Request the given permissions.

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

.. api-section-annotation-hack:: 

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

.. api-section-annotation-hack:: 

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

.. _permissions.AnyPermissions:

AnyPermissions
--------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``origins``]
      :type: (array of :ref:`permissions.MatchPattern`, optional)
   
   
   .. api-member::
      :name: [``permissions``]
      :type: (array of :ref:`permissions.Permission` or :ref:`permissions.OptionalOnlyPermission`, optional)
   

.. _permissions.Permissions:

Permissions
-----------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``origins``]
      :type: (array of :ref:`permissions.MatchPattern`, optional)
   
   
   .. api-member::
      :name: [``permissions``]
      :type: (array of :ref:`permissions.OptionalPermission` or :ref:`permissions.OptionalOnlyPermission`, optional)
   
