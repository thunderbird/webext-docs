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

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`privacy`

   Read and modify privacy settings

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.*``.
