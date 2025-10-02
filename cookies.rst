.. container:: sticky-sidebar

  ≡ cookies API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

===========
cookies API
===========

.. role:: permission

.. role:: value

.. role:: code

Use the :code:`browser.cookies` API to query and modify cookies, and to be notified when they change.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _cookies.permission.cookies:

.. api-member::
   :name: :permission:`cookies`
   :refid: cookies-permission-cookies

   Grant access to some or all methods of the cookies API.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`cookies` is required to use ``messenger.cookies.*``.

.. rst-class:: api-main-section

Functions
=========

.. _cookies.get:

get(details)
------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Retrieves information about a single cookie. If more than one cookie of the same name exists for the given URL, the one with the longest path will be returned. For cookies with the same path length, the cookie with the earliest creation time will be returned.

.. note::

   Provides access to cookies from private browsing mode and container tabs since version 52.

.. note::

   From Thunderbird 133, sorts cookies according to `RFC 6265, section 5.4 <https://datatracker.ietf.org/doc/html/rfc6265#section-5.4>`__. This means the cookie with the longest matching path is returned; previously, the earliest created cookie was returned.

.. api-header::
   :label: Parameters

   .. _cookies.get.details:

   .. api-member::
      :name: ``details``
      :refid: cookies-get-details
      :type: (object)

      Details to identify the cookie being retrieved.

      .. _cookies.get.details.name:

      .. api-member::
         :name: ``name``
         :refid: cookies-get-details-name
         :type: (string)

         The name of the cookie to retrieve.

      .. _cookies.get.details.url:

      .. api-member::
         :name: ``url``
         :refid: cookies-get-details-url
         :type: (string)

         The URL with which the cookie to retrieve is associated. This argument may be a full URL, in which case any data following the URL path (e.g. the query string) is simply ignored. If host permissions for this URL are not specified in the manifest file, the API call will fail.

      .. _cookies.get.details.first^party^domain:

      .. api-member::
         :name: [``firstPartyDomain``]
         :refid: cookies-get-details-first-party-domain
         :type: (string, optional)

         The first-party domain which the cookie to retrieve is associated. This attribute is required if First-Party Isolation is enabled.

      .. _cookies.get.details.partition^key:

      .. api-member::
         :name: [``partitionKey``]
         :refid: cookies-get-details-partition-key
         :type: (:ref:`cookies.^partition^key`, optional)

         The storage partition, if the cookie is part of partitioned storage. By default, only non-partitioned cookies are returned.

      .. _cookies.get.details.store^id:

      .. api-member::
         :name: [``storeId``]
         :refid: cookies-get-details-store-id
         :type: (string, optional)

         The ID of the cookie store in which to look for the cookie. By default, the current execution context's cookie store will be used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _cookies.get.returns:

   .. api-member::
      :refid: cookies-get-returns
      :type: :ref:`cookies.^cookie`

      Contains details about the cookie. This parameter is null if no such cookie was found.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`cookies`

.. _cookies.get^all:

getAll(details)
---------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Retrieves all cookies from a single cookie store that match the given information.  The cookies returned will be sorted, with those with the longest path first.  If multiple cookies have the same path length, those with the earliest creation time will be first.

.. note::

   Before version 52, the 'tabIds' list was empty and only cookies from the default cookie store were returned. From version 52 onwards, this has been fixed and the result includes cookies from private browsing mode and container tabs.

.. note::

   From Thunderbird 133, sorts cookies according to `RFC 6265, section 5.4 <https://datatracker.ietf.org/doc/html/rfc6265#section-5.4>`__. This means the cookie with the longest matching path is returned first: previously, the earliest created cookie was returned first.

.. api-header::
   :label: Parameters

   .. _cookies.get^all.details:

   .. api-member::
      :name: ``details``
      :refid: cookies-get-all-details
      :type: (object)

      Information to filter the cookies being retrieved.

      .. _cookies.get^all.details.domain:

      .. api-member::
         :name: [``domain``]
         :refid: cookies-get-all-details-domain
         :type: (string, optional)

         Restricts the retrieved cookies to those whose domains match or are subdomains of this one.

      .. _cookies.get^all.details.first^party^domain:

      .. api-member::
         :name: [``firstPartyDomain``]
         :refid: cookies-get-all-details-first-party-domain
         :type: (string, optional)

         Restricts the retrieved cookies to those whose first-party domains match this one. This attribute is required if First-Party Isolation is enabled. To not filter by a specific first-party domain, use :value:`null` or :value:`undefined`.

      .. _cookies.get^all.details.name:

      .. api-member::
         :name: [``name``]
         :refid: cookies-get-all-details-name
         :type: (string, optional)

         Filters the cookies by name.

      .. _cookies.get^all.details.partition^key:

      .. api-member::
         :name: [``partitionKey``]
         :refid: cookies-get-all-details-partition-key
         :type: (:ref:`cookies.^partition^key`, optional)

         Selects a specific storage partition to look up cookies. Defaults to null, in which case only non-partitioned cookies are retrieved. If an object iis passed, partitioned cookies are also included, and filtered based on the keys present in the given PartitionKey description. An empty object ({}) returns all cookies (partitioned + unpartitioned), a non-empty object (e.g. {topLevelSite: '...'}) only returns cookies whose partition match all given attributes.

      .. _cookies.get^all.details.path:

      .. api-member::
         :name: [``path``]
         :refid: cookies-get-all-details-path
         :type: (string, optional)

         Restricts the retrieved cookies to those whose path exactly matches this string.

      .. _cookies.get^all.details.secure:

      .. api-member::
         :name: [``secure``]
         :refid: cookies-get-all-details-secure
         :type: (boolean, optional)

         Filters the cookies by their Secure property.

      .. _cookies.get^all.details.session:

      .. api-member::
         :name: [``session``]
         :refid: cookies-get-all-details-session
         :type: (boolean, optional)

         Filters out session vs. persistent cookies.

      .. _cookies.get^all.details.store^id:

      .. api-member::
         :name: [``storeId``]
         :refid: cookies-get-all-details-store-id
         :type: (string, optional)

         The cookie store to retrieve cookies from. If omitted, the current execution context's cookie store will be used.

      .. _cookies.get^all.details.url:

      .. api-member::
         :name: [``url``]
         :refid: cookies-get-all-details-url
         :type: (string, optional)

         Restricts the retrieved cookies to those that would match the given URL.

.. api-header::
   :label: Return type (`Promise`_)

   .. _cookies.get^all.returns:

   .. api-member::
      :refid: cookies-get-all-returns
      :type: array of :ref:`cookies.^cookie`

      All the existing, unexpired cookies that match the given cookie info.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`cookies`

.. _cookies.get^all^cookie^stores:

getAllCookieStores()
--------------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Lists all existing cookie stores.

.. note::

   Before version 52, only the default cookie store was visible. From version 52 onwards, the cookie stores for private browsing mode and container tabs are also readable.

.. api-header::
   :label: Return type (`Promise`_)

   .. _cookies.get^all^cookie^stores.returns:

   .. api-member::
      :refid: cookies-get-all-cookie-stores-returns
      :type: array of :ref:`cookies.^cookie^store`

      All the existing cookie stores.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`cookies`

.. _cookies.remove:

remove(details)
---------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Deletes a cookie by name.

.. note::

   Before version 56, this function did not remove cookies from private browsing mode. From version 56 onwards this is fixed.

.. note::

   From Thunderbird 133, sorts cookies according to `RFC 6265, section 5.4 <https://datatracker.ietf.org/doc/html/rfc6265#section-5.4>`__. This means the cookie with the longest matching path is deleted: previously, the earliest created cookie was deleted.

.. api-header::
   :label: Parameters

   .. _cookies.remove.details:

   .. api-member::
      :name: ``details``
      :refid: cookies-remove-details
      :type: (object)

      Information to identify the cookie to remove.

      .. _cookies.remove.details.name:

      .. api-member::
         :name: ``name``
         :refid: cookies-remove-details-name
         :type: (string)

         The name of the cookie to remove.

      .. _cookies.remove.details.url:

      .. api-member::
         :name: ``url``
         :refid: cookies-remove-details-url
         :type: (string)

         The URL associated with the cookie. If host permissions for this URL are not specified in the manifest file, the API call will fail.

      .. _cookies.remove.details.first^party^domain:

      .. api-member::
         :name: [``firstPartyDomain``]
         :refid: cookies-remove-details-first-party-domain
         :type: (string, optional)

         The first-party domain associated with the cookie. This attribute is required if First-Party Isolation is enabled.

      .. _cookies.remove.details.partition^key:

      .. api-member::
         :name: [``partitionKey``]
         :refid: cookies-remove-details-partition-key
         :type: (:ref:`cookies.^partition^key`, optional)

         The storage partition, if the cookie is part of partitioned storage. By default, non-partitioned storage is used.

      .. _cookies.remove.details.store^id:

      .. api-member::
         :name: [``storeId``]
         :refid: cookies-remove-details-store-id
         :type: (string, optional)

         The ID of the cookie store to look in for the cookie. If unspecified, the cookie is looked for by default in the current execution context's cookie store.

.. api-header::
   :label: Return type (`Promise`_)

   .. _cookies.remove.returns:

   .. api-member::
      :refid: cookies-remove-returns
      :type: object

      Contains details about the cookie that's been removed.  If removal failed for any reason, this will be "null", and :ref:`runtime.last^error` will be set.

      .. _cookies.remove.returns.first^party^domain:

      .. api-member::
         :name: ``firstPartyDomain``
         :refid: cookies-remove-returns-first-party-domain
         :type: (string)

         The first-party domain associated with the cookie that's been removed.

      .. _cookies.remove.returns.name:

      .. api-member::
         :name: ``name``
         :refid: cookies-remove-returns-name
         :type: (string)

         The name of the cookie that's been removed.

      .. _cookies.remove.returns.store^id:

      .. api-member::
         :name: ``storeId``
         :refid: cookies-remove-returns-store-id
         :type: (string)

         The ID of the cookie store from which the cookie was removed.

      .. _cookies.remove.returns.url:

      .. api-member::
         :name: ``url``
         :refid: cookies-remove-returns-url
         :type: (string)

         The URL associated with the cookie that's been removed.

      .. _cookies.remove.returns.partition^key:

      .. api-member::
         :name: [``partitionKey``]
         :refid: cookies-remove-returns-partition-key
         :type: (:ref:`cookies.^partition^key`, optional)

         The storage partition, if the cookie is part of partitioned storage. null if not partitioned.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`cookies`

.. _cookies.set:

set(details)
------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.

.. note::

   Before version 56, this function did not modify cookies in private browsing mode. From version 56 onwards this is fixed.

.. note::

   From Thunderbird 133, sorts cookies according to `RFC 6265, section 5.4 <https://datatracker.ietf.org/doc/html/rfc6265#section-5.4>`__. This means the cookie returned by the promise is the one with the longest matching path: previously, the earliest created cookie was returned.

.. api-header::
   :label: Parameters

   .. _cookies.set.details:

   .. api-member::
      :name: ``details``
      :refid: cookies-set-details
      :type: (object)

      Details about the cookie being set.

      .. _cookies.set.details.url:

      .. api-member::
         :name: ``url``
         :refid: cookies-set-details-url
         :type: (string)

         The request-URI to associate with the setting of the cookie. This value can affect the default domain and path values of the created cookie. If host permissions for this URL are not specified in the manifest file, the API call will fail.

      .. _cookies.set.details.domain:

      .. api-member::
         :name: [``domain``]
         :refid: cookies-set-details-domain
         :type: (string, optional)

         The domain of the cookie. If omitted, the cookie becomes a host-only cookie.

      .. _cookies.set.details.expiration^date:

      .. api-member::
         :name: [``expirationDate``]
         :refid: cookies-set-details-expiration-date
         :type: (number, optional)

         The expiration date of the cookie as the number of seconds since the UNIX epoch. If omitted, the cookie becomes a session cookie.

      .. _cookies.set.details.first^party^domain:

      .. api-member::
         :name: [``firstPartyDomain``]
         :refid: cookies-set-details-first-party-domain
         :type: (string, optional)

         The first-party domain of the cookie. This attribute is required if First-Party Isolation is enabled.

      .. _cookies.set.details.http^only:

      .. api-member::
         :name: [``httpOnly``]
         :refid: cookies-set-details-http-only
         :type: (boolean, optional)

         Whether the cookie should be marked as HttpOnly. Defaults to false.

      .. _cookies.set.details.name:

      .. api-member::
         :name: [``name``]
         :refid: cookies-set-details-name
         :type: (string, optional)

         The name of the cookie. Empty by default if omitted.

      .. _cookies.set.details.partition^key:

      .. api-member::
         :name: [``partitionKey``]
         :refid: cookies-set-details-partition-key
         :type: (:ref:`cookies.^partition^key`, optional)

         The storage partition, if the cookie is part of partitioned storage. By default, non-partitioned storage is used.

      .. _cookies.set.details.path:

      .. api-member::
         :name: [``path``]
         :refid: cookies-set-details-path
         :type: (string, optional)

         The path of the cookie. Defaults to the path portion of the url parameter.

      .. _cookies.set.details.same^site:

      .. api-member::
         :name: [``sameSite``]
         :refid: cookies-set-details-same-site
         :type: (:ref:`cookies.^same^site^status`, optional)

         The cookie's same-site status.

      .. _cookies.set.details.secure:

      .. api-member::
         :name: [``secure``]
         :refid: cookies-set-details-secure
         :type: (boolean, optional)

         Whether the cookie should be marked as Secure. Defaults to false.

      .. _cookies.set.details.store^id:

      .. api-member::
         :name: [``storeId``]
         :refid: cookies-set-details-store-id
         :type: (string, optional)

         The ID of the cookie store in which to set the cookie. By default, the cookie is set in the current execution context's cookie store.

      .. _cookies.set.details.value:

      .. api-member::
         :name: [``value``]
         :refid: cookies-set-details-value
         :type: (string, optional)

         The value of the cookie. Empty by default if omitted.

.. api-header::
   :label: Return type (`Promise`_)

   .. _cookies.set.returns:

   .. api-member::
      :refid: cookies-set-returns
      :type: :ref:`cookies.^cookie`

      Contains details about the cookie that's been set.  If setting failed for any reason, this will be "null", and :ref:`runtime.last^error` will be set.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`cookies`

.. rst-class:: api-main-section

Events
======

.. _cookies.on^changed:

onChanged
---------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when a cookie is set or removed. As a special case, note that updating a cookie's properties is implemented as a two step process: the cookie to be updated is first removed entirely, generating a notification with "cause" of "overwrite" .  Afterwards, a new cookie is written with the updated values, generating a second notification with "cause" "explicit".

.. api-header::
   :label: Parameters for onChanged.addListener(listener)

   .. _cookies.on^changed.listener(change^info):

   .. api-member::
      :name: ``listener(changeInfo)``
      :refid: cookies-on-changed-listener-change-info

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _cookies.on^changed.change^info:

   .. api-member::
      :name: ``changeInfo``
      :refid: cookies-on-changed-change-info
      :type: (object)

      .. _cookies.on^changed.change^info.cause:

      .. api-member::
         :name: ``cause``
         :refid: cookies-on-changed-change-info-cause
         :type: (:ref:`cookies.^on^changed^cause`)

         The underlying reason behind the cookie's change.

      .. _cookies.on^changed.change^info.cookie:

      .. api-member::
         :name: ``cookie``
         :refid: cookies-on-changed-change-info-cookie
         :type: (:ref:`cookies.^cookie`)

         Information about the cookie that was set or removed.

      .. _cookies.on^changed.change^info.removed:

      .. api-member::
         :name: ``removed``
         :refid: cookies-on-changed-change-info-removed
         :type: (boolean)

         True if a cookie was removed.

.. api-header::
   :label: Required permissions

   - :permission:`cookies`

.. rst-class:: api-main-section

Types
=====

.. _cookies.^cookie:

Cookie
------

.. api-section-annotation-hack:: -- [Added in TB 45]

Represents information about an HTTP cookie.

.. api-header::
   :label: object

   .. _cookies.^cookie.domain:

   .. api-member::
      :name: ``domain``
      :refid: cookies-cookie-domain
      :type: (string)

      The domain of the cookie (e.g. "www.google.com", "example.com").

   .. _cookies.^cookie.first^party^domain:

   .. api-member::
      :name: ``firstPartyDomain``
      :refid: cookies-cookie-first-party-domain
      :type: (string)
      :annotation: -- [Added in TB 59]

      The first-party domain of the cookie.

   .. _cookies.^cookie.host^only:

   .. api-member::
      :name: ``hostOnly``
      :refid: cookies-cookie-host-only
      :type: (boolean)

      True if the cookie is a host-only cookie (i.e. a request's host must exactly match the domain of the cookie).

   .. _cookies.^cookie.http^only:

   .. api-member::
      :name: ``httpOnly``
      :refid: cookies-cookie-http-only
      :type: (boolean)

      True if the cookie is marked as HttpOnly (i.e. the cookie is inaccessible to client-side scripts).

   .. _cookies.^cookie.name:

   .. api-member::
      :name: ``name``
      :refid: cookies-cookie-name
      :type: (string)

      The name of the cookie.

   .. _cookies.^cookie.path:

   .. api-member::
      :name: ``path``
      :refid: cookies-cookie-path
      :type: (string)

      The path of the cookie.

   .. _cookies.^cookie.same^site:

   .. api-member::
      :name: ``sameSite``
      :refid: cookies-cookie-same-site
      :type: (:ref:`cookies.^same^site^status`)
      :annotation: -- [Added in TB 63]

      The cookie's same-site status (i.e. whether the cookie is sent with cross-site requests).

   .. _cookies.^cookie.secure:

   .. api-member::
      :name: ``secure``
      :refid: cookies-cookie-secure
      :type: (boolean)

      True if the cookie is marked as Secure (i.e. its scope is limited to secure channels, typically HTTPS).

   .. _cookies.^cookie.session:

   .. api-member::
      :name: ``session``
      :refid: cookies-cookie-session
      :type: (boolean)

      True if the cookie is a session cookie, as opposed to a persistent cookie with an expiration date.

   .. _cookies.^cookie.store^id:

   .. api-member::
      :name: ``storeId``
      :refid: cookies-cookie-store-id
      :type: (string)

      The ID of the cookie store containing this cookie, as provided in getAllCookieStores().

   .. _cookies.^cookie.value:

   .. api-member::
      :name: ``value``
      :refid: cookies-cookie-value
      :type: (string)

      The value of the cookie.

   .. _cookies.^cookie.expiration^date:

   .. api-member::
      :name: [``expirationDate``]
      :refid: cookies-cookie-expiration-date
      :type: (number, optional)

      The expiration date of the cookie as the number of seconds since the UNIX epoch. Not provided for session cookies.

   .. _cookies.^cookie.partition^key:

   .. api-member::
      :name: [``partitionKey``]
      :refid: cookies-cookie-partition-key
      :type: (:ref:`cookies.^partition^key`, optional)
      :annotation: -- [Added in TB 94]

      The cookie's storage partition, if any. null if not partitioned.

.. _cookies.^cookie^store:

CookieStore
-----------

.. api-section-annotation-hack:: -- [Added in TB 45]

Represents a cookie store in the browser. An incognito mode window, for instance, uses a separate cookie store from a non-incognito window.

.. api-header::
   :label: object

   .. _cookies.^cookie^store.id:

   .. api-member::
      :name: ``id``
      :refid: cookies-cookie-store-id
      :type: (string)

      The unique identifier for the cookie store.

   .. _cookies.^cookie^store.incognito:

   .. api-member::
      :name: ``incognito``
      :refid: cookies-cookie-store-incognito
      :type: (boolean)
      :annotation: -- [Added in TB 52]

      Indicates if this is an incognito cookie store

   .. _cookies.^cookie^store.tab^ids:

   .. api-member::
      :name: ``tabIds``
      :refid: cookies-cookie-store-tab-ids
      :type: (array of integer)
      :annotation: -- [Added in TB 52]

      Identifiers of all the browser tabs that share this cookie store.

.. _cookies.^on^changed^cause:

OnChangedCause
--------------

.. api-section-annotation-hack:: -- [Added in TB 45]

The underlying reason behind the cookie's change. If a cookie was inserted, or removed via an explicit call to :ref:`cookies.remove`, "cause" will be "explicit". If a cookie was automatically removed due to expiry, "cause" will be "expired". If a cookie was removed due to being overwritten with an already-expired expiration date, "cause" will be set to "expired_overwrite".  If a cookie was automatically removed due to garbage collection, "cause" will be "evicted".  If a cookie was automatically removed due to a "set" call that overwrote it, "cause" will be "overwrite". Plan your response accordingly.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _cookies.^on^changed^cause.evicted:

         .. api-member::
            :name: :value:`evicted`
            :refid: cookies-on-changed-cause-evicted

         .. _cookies.^on^changed^cause.expired:

         .. api-member::
            :name: :value:`expired`
            :refid: cookies-on-changed-cause-expired

         .. _cookies.^on^changed^cause.expired_overwrite:

         .. api-member::
            :name: :value:`expired_overwrite`
            :refid: cookies-on-changed-cause-expired-overwrite

         .. _cookies.^on^changed^cause.explicit:

         .. api-member::
            :name: :value:`explicit`
            :refid: cookies-on-changed-cause-explicit

         .. _cookies.^on^changed^cause.overwrite:

         .. api-member::
            :name: :value:`overwrite`
            :refid: cookies-on-changed-cause-overwrite

.. _cookies.^partition^key:

PartitionKey
------------

.. api-section-annotation-hack:: 

The description of the storage partition of a cookie. This object may be omitted (null) if a cookie is not partitioned.

.. api-header::
   :label: object

   .. _cookies.^partition^key.has^cross^site^ancestor:

   .. api-member::
      :name: [``hasCrossSiteAncestor``]
      :refid: cookies-partition-key-has-cross-site-ancestor
      :type: (boolean, optional)

      Whether or not the cookie is in a third-party context, respecting ancestor chains.

   .. _cookies.^partition^key.top^level^site:

   .. api-member::
      :name: [``topLevelSite``]
      :refid: cookies-partition-key-top-level-site
      :type: (string, optional)

      The first-party URL of the cookie, if the cookie is in storage partitioned by the top-level site.

.. _cookies.^same^site^status:

SameSiteStatus
--------------

.. api-section-annotation-hack:: 

A cookie's 'SameSite' state (https://tools.ietf.org/html/draft-west-first-party-cookies). 'no_restriction' corresponds to a cookie set without a 'SameSite' attribute, 'lax' to 'SameSite=Lax', and 'strict' to 'SameSite=Strict'.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _cookies.^same^site^status.lax:

         .. api-member::
            :name: :value:`lax`
            :refid: cookies-same-site-status-lax

         .. _cookies.^same^site^status.no_restriction:

         .. api-member::
            :name: :value:`no_restriction`
            :refid: cookies-same-site-status-no-restriction

         .. _cookies.^same^site^status.strict:

         .. api-member::
            :name: :value:`strict`
            :refid: cookies-same-site-status-strict

         .. _cookies.^same^site^status.unspecified:

         .. api-member::
            :name: :value:`unspecified`
            :refid: cookies-same-site-status-unspecified
