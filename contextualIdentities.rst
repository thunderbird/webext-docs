.. container:: sticky-sidebar

  ≡ contextualIdentities API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

========================
contextualIdentities API
========================

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The contextualIdentities API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.contextualIdentities` API to query and modify contextual identity, also called as containers.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`contextualIdentities`

   Grant access to some or all methods of the contextualIdentities API.

Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`contextualIdentities` is required to use ``messenger.contextualIdentities.*``.

.. rst-class:: api-main-section

Functions
=========

.. _contextualIdentities.create:

create(details)
---------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Creates a contextual identity with the given data.

.. note::

   Before version 57, this method resolves its promise with :code:`false` if the contextual identities feature is disabled.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      Details about the contextual identity being created.

      .. api-member::
         :name: ``color``
         :type: (string)

         The color of the contextual identity.

      .. api-member::
         :name: ``icon``
         :type: (string)

         The icon of the contextual identity.

      .. api-member::
         :name: ``name``
         :type: (string)

         The name of the contextual identity.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextualIdentities.get:

get(cookieStoreId)
------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Retrieves information about a single contextual identity.

.. note::

   Before version 57, this method resolves its promise with :code:`false` if the contextual identities feature is disabled.

.. note::

   Before version 57, this method resolves its promise with :code:`null` if the given identity is not found.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``cookieStoreId``
      :type: (string)

      The ID of the contextual identity cookie store.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextualIdentities.move:

move(cookieStoreIds, position)
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 123]

Reorder one or more contextual identities by their cookieStoreIDs to a given position.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``cookieStoreIds``
      :type: (string or array of string)

      The ID or list of IDs of the contextual identity cookie stores.

   .. api-member::
      :name: ``position``
      :type: (integer)

      The position the contextual identity should move to.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextualIdentities.query:

query(details)
--------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Retrieves all contextual identities

.. note::

   Before version 57, this method resolves its promise with :code:`false` if the contextual identities feature is disabled.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      Information to filter the contextual identities being retrieved.

      .. api-member::
         :name: [``name``]
         :type: (string, optional)

         Filters the contextual identity by name.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextualIdentities.remove:

remove(cookieStoreId)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Deletes a contextual identity by its cookie Store ID.

.. note::

   Before version 57, this method resolves its promise with :code:`false` if the contextual identities feature is disabled.

.. note::

   Before version 57, this method resolves its promise with :code:`null` if the given identity is not found.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``cookieStoreId``
      :type: (string)

      The ID of the contextual identity cookie store.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextualIdentities.update:

update(cookieStoreId, details)
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Updates a contextual identity with the given data.

.. note::

   Before version 57, this method resolves its promise with :code:`false` if the contextual identities feature is disabled.

.. note::

   Before version 57, this method resolves its promise with :code:`null` if the given identity is not found.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``cookieStoreId``
      :type: (string)

      The ID of the contextual identity cookie store.

   .. api-member::
      :name: ``details``
      :type: (object)

      Details about the contextual identity being created.

      .. api-member::
         :name: [``color``]
         :type: (string, optional)

         The color of the contextual identity.

      .. api-member::
         :name: [``icon``]
         :type: (string, optional)

         The icon of the contextual identity.

      .. api-member::
         :name: [``name``]
         :type: (string, optional)

         The name of the contextual identity.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. rst-class:: api-main-section

Events
======

.. _contextualIdentities.onCreated:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 57]

Fired when a new container is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. api-member::
      :name: ``listener(changeInfo)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``changeInfo``
      :type: (object)

      .. api-member::
         :name: ``contextualIdentity``
         :type: (:ref:`contextualIdentities.ContextualIdentity`)

         Contextual identity that has been created

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextualIdentities.onRemoved:

onRemoved
---------

.. api-section-annotation-hack:: -- [Added in TB 57]

Fired when a container is removed.

.. api-header::
   :label: Parameters for onRemoved.addListener(listener)

   .. api-member::
      :name: ``listener(changeInfo)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``changeInfo``
      :type: (object)

      .. api-member::
         :name: ``contextualIdentity``
         :type: (:ref:`contextualIdentities.ContextualIdentity`)

         Contextual identity that has been removed

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextualIdentities.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 57]

Fired when a container is updated.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. api-member::
      :name: ``listener(changeInfo)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``changeInfo``
      :type: (object)

      .. api-member::
         :name: ``contextualIdentity``
         :type: (:ref:`contextualIdentities.ContextualIdentity`)

         Contextual identity that has been updated

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. rst-class:: api-main-section

Types
=====

.. _contextualIdentities.ContextualIdentity:

ContextualIdentity
------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Represents information about a contextual identity.

.. api-header::
   :label: object

   .. _contextualIdentities.ContextualIdentity.color:

   .. api-member::
      :name: ``color``
      :type: (string)

      The color name of the contextual identity.

   .. _contextualIdentities.ContextualIdentity.colorCode:

   .. api-member::
      :name: ``colorCode``
      :type: (string)
      :annotation: -- [Added in TB 57]

      The color hash of the contextual identity.

   .. _contextualIdentities.ContextualIdentity.cookieStoreId:

   .. api-member::
      :name: ``cookieStoreId``
      :type: (string)

      The cookie store ID of the contextual identity.

   .. _contextualIdentities.ContextualIdentity.icon:

   .. api-member::
      :name: ``icon``
      :type: (string)

      The icon name of the contextual identity.

   .. _contextualIdentities.ContextualIdentity.iconUrl:

   .. api-member::
      :name: ``iconUrl``
      :type: (string)
      :annotation: -- [Added in TB 57]

      The icon url of the contextual identity.

   .. _contextualIdentities.ContextualIdentity.name:

   .. api-member::
      :name: ``name``
      :type: (string)

      The name of the contextual identity.
