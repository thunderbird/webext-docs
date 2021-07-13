.. _addressBooks.provider_api:

=====================
addressBooks.provider
=====================

<AB.PROVIDER.TEXT>

.. role:: permission

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`addressBooks`

   Read and modify your address books and contacts

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`addressBooks` is required to use ``addressBooks.provider``.

.. rst-class:: api-main-section

Events
======

.. _addressBooks.provider.onSearchRequest:

onSearchRequest(node, [searchString], [query])
----------------------------------------------

.. api-section-annotation-hack:: 

Creates a read-only addressbook that fires this event when searching for a contact. Note: This event may change in future releases of Thunderbird.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``node``
      :type: (:ref:`addressBooks.AddressBookNode`)
   
   
   .. api-member::
      :name: [``searchString``]
      :type: (string)
      
      The search text that the user entered. Not available when invoked from the advanced address book search dialog.
   
   
   .. api-member::
      :name: [``query``]
      :type: (string)
      
      The boolean query expression corresponding to the search. Note: This parameter may change in future releases of Thunderbird.
   

.. api-header::
   :label: Required permissions

   - :permission:`addressBooks`
