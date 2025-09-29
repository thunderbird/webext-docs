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

.. hint::

   The dns API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/dns>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Asynchronous DNS API

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`dns`

   Grant access to some or all methods of the dns API.

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

.. _dns.DNSRecord:

DNSRecord
---------

.. api-section-annotation-hack:: 

An object encapsulating a DNS Record.

.. api-header::
   :label: object

   .. _dns.DNSRecord.addresses:

   .. api-member::
      :name: ``addresses``
      :type: (array of string)

   .. _dns.DNSRecord.isTRR:

   .. api-member::
      :name: ``isTRR``
      :type: (string)

      Record retreived with TRR.

   .. _dns.DNSRecord.canonicalName:

   .. api-member::
      :name: [``canonicalName``]
      :type: (string, optional)

      The canonical hostname for this record.  this value is empty if the record was not fetched with the 'canonical_name' flag.

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
