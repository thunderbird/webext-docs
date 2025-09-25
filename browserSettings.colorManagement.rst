.. container:: sticky-sidebar

  ≡ browserSettings.colorManagement API

  * `Permissions`_
  * `Properties`_

  .. include:: /includes/developer-resources.rst

===================================
browserSettings.colorManagement API
===================================

.. role:: permission

.. role:: value

.. role:: code

Use the <code>browserSettings.colorManagement</code> API to query and set items related to color management.

.. rst-class:: api-main-section

Permissions
===========

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`browserSettings` is required to use ``messenger.browserSettings.colorManagement.*``.

.. rst-class:: api-main-section

Properties
==========

.. _browserSettings.colorManagement.mode:

mode
----

.. api-section-annotation-hack:: 

This setting controls the mode used for color management and must be a string from :ref:`browserSettings.ColorManagementMode`

.. _browserSettings.colorManagement.useNativeSRGB:

useNativeSRGB
-------------

.. api-section-annotation-hack:: 

This boolean setting controls whether or not native sRGB color management is used.

.. _browserSettings.colorManagement.useWebRenderCompositor:

useWebRenderCompositor
----------------------

.. api-section-annotation-hack:: 

This boolean setting controls whether or not the WebRender compositor is used.
