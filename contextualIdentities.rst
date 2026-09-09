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

.. role:: small

.. hint::

   The contextualIdentities API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.contextualIdentities` API to query and modify contextual identity, also called as containers.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _contextual^identities.permission.contextual^identities:

.. api-member::
   :name: :permission:`contextualIdentities`
   :refid: contextual-identities-permission-contextual-identities
   :refname: contextualIdentities

   Grant access to some or all methods of the contextualIdentities API.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`contextualIdentities` is required to use ``messenger.contextualIdentities.*``.

.. rst-class:: api-main-section

Functions
=========

.. _contextual^identities.create:

create(details)
---------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Creates a contextual identity with the given data.

.. note::

   Before version 57, this method resolves its promise with :code:`false` if the contextual identities feature is disabled.

.. api-header::
   :label: Parameters

   .. _contextual^identities.create.details:

   .. api-member::
      :name: ``details``
      :refid: contextual-identities-create-details
      :refname: details
      :type: (object)

      Details about the contextual identity being created.

      .. _contextual^identities.create.details.color:

      .. api-member::
         :name: ``color``
         :refid: contextual-identities-create-details-color
         :refname: color
         :type: (string)

         The color of the contextual identity.

      .. _contextual^identities.create.details.icon:

      .. api-member::
         :name: ``icon``
         :refid: contextual-identities-create-details-icon
         :refname: icon
         :type: (string)

         The icon of the contextual identity.

      .. _contextual^identities.create.details.name:

      .. api-member::
         :name: ``name``
         :refid: contextual-identities-create-details-name
         :refname: name
         :type: (string)

         The name of the contextual identity.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.get:

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

   .. _contextual^identities.get.cookie^store^id:

   .. api-member::
      :name: ``cookieStoreId``
      :refid: contextual-identities-get-cookie-store-id
      :refname: cookieStoreId
      :type: (string)

      The ID of the contextual identity cookie store.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.get^site^association:

getSiteAssociation(details)
---------------------------

.. api-section-annotation-hack:: 

Retrieves the association of a site, or null if the site is not associated with any container.

.. api-header::
   :label: Parameters

   .. _contextual^identities.get^site^association.details:

   .. api-member::
      :name: ``details``
      :refid: contextual-identities-get-site-association-details
      :refname: details
      :type: (object)

      Details about the site to look up.

      .. _contextual^identities.get^site^association.details.site:

      .. api-member::
         :name: ``site``
         :refid: contextual-identities-get-site-association-details-site
         :refname: site
         :type: (string)

         The host to look up.

.. api-header::
   :label: Return type (`Promise`_)

   .. _contextual^identities.get^site^association.returns:

   .. api-member::
      :refid: contextual-identities-get-site-association-returns
      :refname: _returns
      :type: :ref:`contextual^identities.^site^association`

      The association of the site, null if the site is not associated with any container.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.get^supported^colors:

getSupportedColors()
--------------------

.. api-section-annotation-hack:: 

Retrieves the list of colors supported by contextual identities.

.. api-header::
   :label: Return type (`Promise`_)

   .. _contextual^identities.get^supported^colors.returns:

   .. api-member::
      :refid: contextual-identities-get-supported-colors-returns
      :refname: _returns
      :type: array of object

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.get^supported^icons:

getSupportedIcons()
-------------------

.. api-section-annotation-hack:: 

Retrieves the list of icons supported by contextual identities.

.. api-header::
   :label: Return type (`Promise`_)

   .. _contextual^identities.get^supported^icons.returns:

   .. api-member::
      :refid: contextual-identities-get-supported-icons-returns
      :refname: _returns
      :type: array of object

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.move:

move(cookieStoreIds, position)
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 123]

Reorder one or more contextual identities by their cookieStoreIDs to a given position.

.. api-header::
   :label: Parameters

   .. _contextual^identities.move.cookie^store^ids:

   .. api-member::
      :name: ``cookieStoreIds``
      :refid: contextual-identities-move-cookie-store-ids
      :refname: cookieStoreIds
      :type: (string or array of string)

      The ID or list of IDs of the contextual identity cookie stores.

   .. _contextual^identities.move.position:

   .. api-member::
      :name: ``position``
      :refid: contextual-identities-move-position
      :refname: position
      :type: (integer)

      The position the contextual identity should move to.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.query:

query(details)
--------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Retrieves all contextual identities

.. note::

   Before version 57, this method resolves its promise with :code:`false` if the contextual identities feature is disabled.

.. api-header::
   :label: Parameters

   .. _contextual^identities.query.details:

   .. api-member::
      :name: ``details``
      :refid: contextual-identities-query-details
      :refname: details
      :type: (object)

      Information to filter the contextual identities being retrieved.

      .. _contextual^identities.query.details.name:

      .. api-member::
         :name: [``name``]
         :refid: contextual-identities-query-details-name
         :refname: name
         :type: (string, optional)

         Filters the contextual identity by name.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.query^site^associations:

querySiteAssociations(details)
------------------------------

.. api-section-annotation-hack:: 

Retrieves the list of site-to-container associations.

.. api-header::
   :label: Parameters

   .. _contextual^identities.query^site^associations.details:

   .. api-member::
      :name: ``details``
      :refid: contextual-identities-query-site-associations-details
      :refname: details
      :type: (object)

      Information to filter the associations being retrieved.

      .. _contextual^identities.query^site^associations.details.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: contextual-identities-query-site-associations-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)

         If provided, only associations for this container are returned.

.. api-header::
   :label: Return type (`Promise`_)

   .. _contextual^identities.query^site^associations.returns:

   .. api-member::
      :refid: contextual-identities-query-site-associations-returns
      :refname: _returns
      :type: array of :ref:`contextual^identities.^site^association`

      The site-to-container associations.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.remove:

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

   .. _contextual^identities.remove.cookie^store^id:

   .. api-member::
      :name: ``cookieStoreId``
      :refid: contextual-identities-remove-cookie-store-id
      :refname: cookieStoreId
      :type: (string)

      The ID of the contextual identity cookie store.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.remove^site^association:

removeSiteAssociation(details)
------------------------------

.. api-section-annotation-hack:: 

Removes the container association for a site.

.. api-header::
   :label: Parameters

   .. _contextual^identities.remove^site^association.details:

   .. api-member::
      :name: ``details``
      :refid: contextual-identities-remove-site-association-details
      :refname: details
      :type: (object)

      Details about the site association to remove.

      .. _contextual^identities.remove^site^association.details.site:

      .. api-member::
         :name: ``site``
         :refid: contextual-identities-remove-site-association-details-site
         :refname: site
         :type: (string)

         The host whose container association should be removed.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.set^site^association:

setSiteAssociation(details)
---------------------------

.. api-section-annotation-hack:: 

Associates a site with a container. Top-level navigations to that site will load in the given container.

.. api-header::
   :label: Parameters

   .. _contextual^identities.set^site^association.details:

   .. api-member::
      :name: ``details``
      :refid: contextual-identities-set-site-association-details
      :refname: details
      :type: (object)

      Details about the site association.

      .. _contextual^identities.set^site^association.details.cookie^store^id:

      .. api-member::
         :name: ``cookieStoreId``
         :refid: contextual-identities-set-site-association-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string)

         The cookie store ID of the container to associate the site with.

      .. _contextual^identities.set^site^association.details.site:

      .. api-member::
         :name: ``site``
         :refid: contextual-identities-set-site-association-details-site
         :refname: site
         :type: (string)

         The host to associate with the container (matched as an exact host).

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.update:

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

   .. _contextual^identities.update.cookie^store^id:

   .. api-member::
      :name: ``cookieStoreId``
      :refid: contextual-identities-update-cookie-store-id
      :refname: cookieStoreId
      :type: (string)

      The ID of the contextual identity cookie store.

   .. _contextual^identities.update.details:

   .. api-member::
      :name: ``details``
      :refid: contextual-identities-update-details
      :refname: details
      :type: (object)

      Details about the contextual identity being created.

      .. _contextual^identities.update.details.color:

      .. api-member::
         :name: [``color``]
         :refid: contextual-identities-update-details-color
         :refname: color
         :type: (string, optional)

         The color of the contextual identity.

      .. _contextual^identities.update.details.icon:

      .. api-member::
         :name: [``icon``]
         :refid: contextual-identities-update-details-icon
         :refname: icon
         :type: (string, optional)

         The icon of the contextual identity.

      .. _contextual^identities.update.details.name:

      .. api-member::
         :name: [``name``]
         :refid: contextual-identities-update-details-name
         :refname: name
         :type: (string, optional)

         The name of the contextual identity.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. rst-class:: api-main-section

Events
======

.. _contextual^identities.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 57]

Fired when a new container is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _contextual^identities.on^created.listener(change^info):

   .. api-member::
      :name: ``listener(changeInfo)``
      :refid: contextual-identities-on-created-listener-change-info
      :refname: listener(changeInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _contextual^identities.on^created.change^info:

   .. api-member::
      :name: ``changeInfo``
      :refid: contextual-identities-on-created-change-info
      :refname: changeInfo
      :type: (object)

      .. _contextual^identities.on^created.change^info.contextual^identity:

      .. api-member::
         :name: ``contextualIdentity``
         :refid: contextual-identities-on-created-change-info-contextual-identity
         :refname: contextualIdentity
         :type: (:ref:`contextual^identities.^contextual^identity`)

         Contextual identity that has been created

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.on^removed:

onRemoved
---------

.. api-section-annotation-hack:: -- [Added in TB 57]

Fired when a container is removed.

.. api-header::
   :label: Parameters for onRemoved.addListener(listener)

   .. _contextual^identities.on^removed.listener(change^info):

   .. api-member::
      :name: ``listener(changeInfo)``
      :refid: contextual-identities-on-removed-listener-change-info
      :refname: listener(changeInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _contextual^identities.on^removed.change^info:

   .. api-member::
      :name: ``changeInfo``
      :refid: contextual-identities-on-removed-change-info
      :refname: changeInfo
      :type: (object)

      .. _contextual^identities.on^removed.change^info.contextual^identity:

      .. api-member::
         :name: ``contextualIdentity``
         :refid: contextual-identities-on-removed-change-info-contextual-identity
         :refname: contextualIdentity
         :type: (:ref:`contextual^identities.^contextual^identity`)

         Contextual identity that has been removed

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.on^site^association^changed:

onSiteAssociationChanged
------------------------

.. api-section-annotation-hack:: 

Fired when a site-to-container association is added, changed, or removed.

.. api-header::
   :label: Parameters for onSiteAssociationChanged.addListener(listener)

   .. _contextual^identities.on^site^association^changed.listener(change^info):

   .. api-member::
      :name: ``listener(changeInfo)``
      :refid: contextual-identities-on-site-association-changed-listener-change-info
      :refname: listener(changeInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _contextual^identities.on^site^association^changed.change^info:

   .. api-member::
      :name: ``changeInfo``
      :refid: contextual-identities-on-site-association-changed-change-info
      :refname: changeInfo
      :type: (object)

      .. _contextual^identities.on^site^association^changed.change^info.site:

      .. api-member::
         :name: ``site``
         :refid: contextual-identities-on-site-association-changed-change-info-site
         :refname: site
         :type: (string)

         The host whose association changed.

      .. _contextual^identities.on^site^association^changed.change^info.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: contextual-identities-on-site-association-changed-change-info-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)

         The cookie store ID of the now-associated container, or omitted if the association was removed.

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. _contextual^identities.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 57]

Fired when a container is updated.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. _contextual^identities.on^updated.listener(change^info):

   .. api-member::
      :name: ``listener(changeInfo)``
      :refid: contextual-identities-on-updated-listener-change-info
      :refname: listener(changeInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _contextual^identities.on^updated.change^info:

   .. api-member::
      :name: ``changeInfo``
      :refid: contextual-identities-on-updated-change-info
      :refname: changeInfo
      :type: (object)

      .. _contextual^identities.on^updated.change^info.contextual^identity:

      .. api-member::
         :name: ``contextualIdentity``
         :refid: contextual-identities-on-updated-change-info-contextual-identity
         :refname: contextualIdentity
         :type: (:ref:`contextual^identities.^contextual^identity`)

         Contextual identity that has been updated

.. api-header::
   :label: Required permissions

   - :permission:`contextualIdentities`

.. rst-class:: api-main-section

Types
=====

.. _contextual^identities.^contextual^identity:

ContextualIdentity
------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Represents information about a contextual identity.

.. api-header::
   :label: object

   .. _contextual^identities.^contextual^identity.color:

   .. api-member::
      :name: ``color``
      :refid: contextual-identities-contextual-identity-color
      :refname: color
      :type: (string)

      The color name of the contextual identity.

   .. _contextual^identities.^contextual^identity.color^code:

   .. api-member::
      :name: ``colorCode``
      :refid: contextual-identities-contextual-identity-color-code
      :refname: colorCode
      :type: (string)
      :annotation: -- [Added in TB 57]

      The color hash of the contextual identity.

   .. _contextual^identities.^contextual^identity.cookie^store^id:

   .. api-member::
      :name: ``cookieStoreId``
      :refid: contextual-identities-contextual-identity-cookie-store-id
      :refname: cookieStoreId
      :type: (string)

      The cookie store ID of the contextual identity.

   .. _contextual^identities.^contextual^identity.icon:

   .. api-member::
      :name: ``icon``
      :refid: contextual-identities-contextual-identity-icon
      :refname: icon
      :type: (string)

      The icon name of the contextual identity.

   .. _contextual^identities.^contextual^identity.icon^url:

   .. api-member::
      :name: ``iconUrl``
      :refid: contextual-identities-contextual-identity-icon-url
      :refname: iconUrl
      :type: (string)
      :annotation: -- [Added in TB 57]

      The icon url of the contextual identity.

   .. _contextual^identities.^contextual^identity.name:

   .. api-member::
      :name: ``name``
      :refid: contextual-identities-contextual-identity-name
      :refname: name
      :type: (string)

      The name of the contextual identity.

.. _contextual^identities.^site^association:

SiteAssociation
---------------

.. api-section-annotation-hack:: 

Represents the association between a site and a contextual identity.

.. api-header::
   :label: object

   .. _contextual^identities.^site^association.cookie^store^id:

   .. api-member::
      :name: ``cookieStoreId``
      :refid: contextual-identities-site-association-cookie-store-id
      :refname: cookieStoreId
      :type: (string)

      The cookie store ID of the contextual identity the host is associated with.

   .. _contextual^identities.^site^association.site:

   .. api-member::
      :name: ``site``
      :refid: contextual-identities-site-association-site
      :refname: site
      :type: (string)

      The associated host, normalized to lower case and encoded as ASCII.
