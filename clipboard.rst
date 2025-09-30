.. container:: sticky-sidebar

  ≡ clipboard API

  * `Permissions`_
  * `Functions`_

  .. include:: /_includes/developer-resources.rst

=============
clipboard API
=============

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The clipboard API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/clipboard>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Offers the ability to write to the clipboard. Reading is not supported because the clipboard can already be read through the standard web platform APIs.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`clipboardWrite`

   Input data to the clipboard.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`clipboardWrite` is required to use ``messenger.clipboard.*``.

.. rst-class:: api-main-section

Functions
=========

.. _clipboard.set^image^data:

setImageData(imageData, imageType)
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 57]

Copy an image to the clipboard. The image is re-encoded before it is written to the clipboard. If the image is invalid, the clipboard is not modified.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``imageData``
      :type: (`ArrayBuffer <https://developer.mozilla.org/en-US/docs/Web/API/ArrayBuffer>`__)

      The image data to be copied.

   .. api-member::
      :name: ``imageType``
      :type: (`string`)

      The type of imageData.

      Supported values:

      .. api-member::
         :name: :value:`jpeg`

      .. api-member::
         :name: :value:`png`

.. api-header::
   :label: Required permissions

   - :permission:`clipboardWrite`
