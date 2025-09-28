.. container:: sticky-sidebar

  ≡ pkcs11 API

  * `Permissions`_
  * `Functions`_

  .. include:: /_includes/developer-resources.rst

==========
pkcs11 API
==========

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The pkcs11 API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/pkcs11>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

PKCS#11 module management API

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`pkcs11`

   Grant access to some or all methods of the pkcs11 API.

Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`pkcs11` is required to use ``messenger.pkcs11.*``.

.. rst-class:: api-main-section

Functions
=========

.. _pkcs11.getModuleSlots:

getModuleSlots(name)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 58]

Enumerate a module's slots, each with their name and whether a token is present

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``name``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`pkcs11`

.. _pkcs11.installModule:

installModule(name, [flags])
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 58]

Install a PKCS#11 module with a given name

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``name``
      :type: (string)

   .. api-member::
      :name: [``flags``]
      :type: (integer, optional)

.. api-header::
   :label: Required permissions

   - :permission:`pkcs11`

.. _pkcs11.isModuleInstalled:

isModuleInstalled(name)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 58]

checks whether a PKCS#11 module, given by name, is installed

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``name``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`pkcs11`

.. _pkcs11.uninstallModule:

uninstallModule(name)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 58]

Remove an installed PKCS#11 module from firefox

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``name``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`pkcs11`
