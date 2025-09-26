.. container:: sticky-sidebar

  ≡ dns API

  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=======
dns API
=======

.. role:: permission

.. role:: value

.. role:: code

Asynchronous DNS API

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`dns`

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`dns` is required to use ``messenger.dns.*``.

.. rst-class:: api-main-section

Functions
=========

.. _dns.resolve:

resolve(hostname, [flags])
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 60]

Resolves a hostname to a DNS record.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``hostname``
      :type: (string)

   .. api-member::
      :name: [``flags``]
      :type: (:ref:`dns.ResolveFlags`, optional)

.. api-header::
   :label: Required permissions

   - :permission:`dns`

.. rst-class:: api-main-section

Types
=====

.. _dns.ResolveFlags:

ResolveFlags
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: array of `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`allow_name_collisions`

         .. api-member::
            :name: :value:`bypass_cache`

         .. api-member::
            :name: :value:`canonical_name`

         .. api-member::
            :name: :value:`disable_ipv4`

         .. api-member::
            :name: :value:`disable_ipv6`

         .. api-member::
            :name: :value:`disable_trr`

         .. api-member::
            :name: :value:`offline`

         .. api-member::
            :name: :value:`priority_low`

         .. api-member::
            :name: :value:`priority_medium`

         .. api-member::
            :name: :value:`speculate`
