.. container:: sticky-sidebar

  ≡ privacy.services API

  * `Permissions`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

====================
privacy.services API
====================

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The privacy.services API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/privacy/services>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.privacy` API to control usage of the features in the browser that can affect a user's privacy.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`privacy`

   Read and modify privacy settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.services.*``.

.. rst-class:: api-main-section

Properties
==========

.. _privacy.services.passwordSavingEnabled:

passwordSavingEnabled
---------------------

.. api-section-annotation-hack:: 

If enabled, the password manager will ask if you want to save passwords. This preference's value is a boolean, defaulting to :code:`true`.
