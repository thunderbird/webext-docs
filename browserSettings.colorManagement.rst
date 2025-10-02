.. container:: sticky-sidebar

  ≡ browserSettings.colorManagement API

  * `Permissions`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

===================================
browserSettings.colorManagement API
===================================

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The browserSettings.colorManagement API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/browserSettings/colorManagement>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browserSettings.colorManagement` API to query and set items related to color management.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _browser^settings.color^management.permission.browser^settings:

.. api-member::
   :name: :permission:`browserSettings`
   :refid: browser-settings-color-management-permission-browser-settings

   Read and modify browser settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`browserSettings` is required to use ``messenger.browserSettings.colorManagement.*``.

.. rst-class:: api-main-section

Properties
==========

.. _browser^settings.color^management.mode:

mode
----

.. api-section-annotation-hack:: 

This setting controls the mode used for color management and must be a string from :ref:`browser^settings.^color^management^mode`

.. _browser^settings.color^management.use^native^s^r^g^b:

useNativeSRGB
-------------

.. api-section-annotation-hack:: 

This boolean setting controls whether or not native sRGB color management is used.

.. _browser^settings.color^management.use^web^render^compositor:

useWebRenderCompositor
----------------------

.. api-section-annotation-hack:: 

This boolean setting controls whether or not the WebRender compositor is used.
