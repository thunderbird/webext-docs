.. container:: sticky-sidebar

  ≡ privacy API

  * `Permissions`_

  .. include:: /_includes/developer-resources.rst

===========
privacy API
===========

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The privacy API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/privacy>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _privacy.permission.privacy:

.. api-member::
   :name: :permission:`privacy`
   :refid: privacy-permission-privacy
   :refname: privacy

   Read and modify privacy settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.*``.
