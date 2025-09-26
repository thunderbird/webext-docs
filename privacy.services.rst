.. container:: sticky-sidebar

  ≡ privacy.services API

  * `Permissions`_
  * `Properties`_

  .. include:: /includes/developer-resources.rst

====================
privacy.services API
====================

.. role:: permission

.. role:: value

.. role:: code

Use the :code:`browser.privacy` API to control usage of the features in the browser that can affect a user's privacy.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`privacy`

   Read and modify privacy settings

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
