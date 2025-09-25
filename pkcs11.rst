.. container:: sticky-sidebar

  ≡ pkcs11 API

  * `Permissions`_
  * `Functions`_

  .. include:: /includes/developer-resources.rst

==========
pkcs11 API
==========

.. role:: permission

.. role:: value

.. role:: code

PKCS#11 module management API

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`pkcs11`

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
