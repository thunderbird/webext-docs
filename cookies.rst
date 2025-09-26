.. container:: sticky-sidebar

  ≡ cookies API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

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

.. api-member::
   :name: :permission:`cookies`

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

   .. api-member::
      :name: ``details``
      :type: (object)

      Details to identify the cookie being retrieved.

      .. api-member::
         :name: ``name``
         :type: (string)

         The name of the cookie to retrieve.

      .. api-member::
         :name: ``url``
         :type: (string)

         The URL with which the cookie to retrieve is associated. This argument may be a full URL, in which case any data following the URL path (e.g. the query string) is simply ignored. If host permissions for this URL are not specified in the manifest file, the API call will fail.

      .. api-member::
         :name: [``firstPartyDomain``]
         :type: (string, optional)

         The first-party domain which the cookie to retrieve is associated. This attribute is required if First-Party Isolation is enabled.

      .. api-member::
         :name: [``partitionKey``]
         :type: (:ref:`cookies.PartitionKey`, optional)

         The storage partition, if the cookie is part of partitioned storage. By default, only non-partitioned cookies are returned.

      .. api-member::
         :name: [``storeId``]
         :type: (string, optional)

         The ID of the cookie store in which to look for the cookie. By default, the current execution context's cookie store will be used.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`cookies.Cookie`

      Contains details about the cookie. This parameter is null if no such cookie was found.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`cookies`

.. _cookies.getAll:

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

   .. api-member::
      :name: ``details``
      :type: (object)

      Information to filter the cookies being retrieved.

      .. api-member::
         :name: [``domain``]
         :type: (string, optional)

         Restricts the retrieved cookies to those whose domains match or are subdomains of this one.

      .. api-member::
         :name: [``firstPartyDomain``]
         :type: (string, optional)

         Restricts the retrieved cookies to those whose first-party domains match this one. This attribute is required if First-Party Isolation is enabled. To not filter by a specific first-party domain, use :value:`null` or :value:`undefined`.

      .. api-member::
         :name: [``name``]
         :type: (string, optional)

         Filters the cookies by name.

      .. api-member::
         :name: [``partitionKey``]
         :type: (:ref:`cookies.PartitionKey`, optional)

         Selects a specific storage partition to look up cookies. Defaults to null, in which case only non-partitioned cookies are retrieved. If an object iis passed, partitioned cookies are also included, and filtered based on the keys present in the given PartitionKey description. An empty object ({}) returns all cookies (partitioned + unpartitioned), a non-empty object (e.g. {topLevelSite: '...'}) only returns cookies whose partition match all given attributes.

      .. api-member::
         :name: [``path``]
         :type: (string, optional)

         Restricts the retrieved cookies to those whose path exactly matches this string.

      .. api-member::
         :name: [``secure``]
         :type: (boolean, optional)

         Filters the cookies by their Secure property.

      .. api-member::
         :name: [``session``]
         :type: (boolean, optional)

         Filters out session vs. persistent cookies.

      .. api-member::
         :name: [``storeId``]
         :type: (string, optional)

         The cookie store to retrieve cookies from. If omitted, the current execution context's cookie store will be used.

      .. api-member::
         :name: [``url``]
         :type: (string, optional)

         Restricts the retrieved cookies to those that would match the given URL.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`cookies.Cookie`

      All the existing, unexpired cookies that match the given cookie info.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`cookies`

.. _cookies.getAllCookieStores:

getAllCookieStores()
--------------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Lists all existing cookie stores.

.. note::

   Before version 52, only the default cookie store was visible. From version 52 onwards, the cookie stores for private browsing mode and container tabs are also readable.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`cookies.CookieStore`

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

   .. api-member::
      :name: ``details``
      :type: (object)

      Information to identify the cookie to remove.

      .. api-member::
         :name: ``name``
         :type: (string)

         The name of the cookie to remove.

      .. api-member::
         :name: ``url``
         :type: (string)

         The URL associated with the cookie. If host permissions for this URL are not specified in the manifest file, the API call will fail.

      .. api-member::
         :name: [``firstPartyDomain``]
         :type: (string, optional)

         The first-party domain associated with the cookie. This attribute is required if First-Party Isolation is enabled.

      .. api-member::
         :name: [``partitionKey``]
         :type: (:ref:`cookies.PartitionKey`, optional)

         The storage partition, if the cookie is part of partitioned storage. By default, non-partitioned storage is used.

      .. api-member::
         :name: [``storeId``]
         :type: (string, optional)

         The ID of the cookie store to look in for the cookie. If unspecified, the cookie is looked for by default in the current execution context's cookie store.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: object

      Contains details about the cookie that's been removed.  If removal failed for any reason, this will be "null", and :ref:`runtime.lastError` will be set.

      .. api-member::
         :name: ``firstPartyDomain``
         :type: (string)

         The first-party domain associated with the cookie that's been removed.

      .. api-member::
         :name: ``name``
         :type: (string)

         The name of the cookie that's been removed.

      .. api-member::
         :name: ``storeId``
         :type: (string)

         The ID of the cookie store from which the cookie was removed.

      .. api-member::
         :name: ``url``
         :type: (string)

         The URL associated with the cookie that's been removed.

      .. api-member::
         :name: [``partitionKey``]
         :type: (:ref:`cookies.PartitionKey`, optional)

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

   .. api-member::
      :name: ``details``
      :type: (object)

      Details about the cookie being set.

      .. api-member::
         :name: ``url``
         :type: (string)

         The request-URI to associate with the setting of the cookie. This value can affect the default domain and path values of the created cookie. If host permissions for this URL are not specified in the manifest file, the API call will fail.

      .. api-member::
         :name: [``domain``]
         :type: (string, optional)

         The domain of the cookie. If omitted, the cookie becomes a host-only cookie.

      .. api-member::
         :name: [``expirationDate``]
         :type: (number, optional)

         The expiration date of the cookie as the number of seconds since the UNIX epoch. If omitted, the cookie becomes a session cookie.

      .. api-member::
         :name: [``firstPartyDomain``]
         :type: (string, optional)

         The first-party domain of the cookie. This attribute is required if First-Party Isolation is enabled.

      .. api-member::
         :name: [``httpOnly``]
         :type: (boolean, optional)

         Whether the cookie should be marked as HttpOnly. Defaults to false.

      .. api-member::
         :name: [``name``]
         :type: (string, optional)

         The name of the cookie. Empty by default if omitted.

      .. api-member::
         :name: [``partitionKey``]
         :type: (:ref:`cookies.PartitionKey`, optional)

         The storage partition, if the cookie is part of partitioned storage. By default, non-partitioned storage is used.

      .. api-member::
         :name: [``path``]
         :type: (string, optional)

         The path of the cookie. Defaults to the path portion of the url parameter.

      .. api-member::
         :name: [``sameSite``]
         :type: (:ref:`cookies.SameSiteStatus`, optional)

         The cookie's same-site status.

      .. api-member::
         :name: [``secure``]
         :type: (boolean, optional)

         Whether the cookie should be marked as Secure. Defaults to false.

      .. api-member::
         :name: [``storeId``]
         :type: (string, optional)

         The ID of the cookie store in which to set the cookie. By default, the cookie is set in the current execution context's cookie store.

      .. api-member::
         :name: [``value``]
         :type: (string, optional)

         The value of the cookie. Empty by default if omitted.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`cookies.Cookie`

      Contains details about the cookie that's been set.  If setting failed for any reason, this will be "null", and :ref:`runtime.lastError` will be set.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`cookies`

.. rst-class:: api-main-section

Events
======

.. _cookies.onChanged:

onChanged
---------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when a cookie is set or removed. As a special case, note that updating a cookie's properties is implemented as a two step process: the cookie to be updated is first removed entirely, generating a notification with "cause" of "overwrite" .  Afterwards, a new cookie is written with the updated values, generating a second notification with "cause" "explicit".

.. api-header::
   :label: Parameters for onChanged.addListener(listener)

   .. api-member::
      :name: ``listener(changeInfo)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``changeInfo``
      :type: (object)

      .. api-member::
         :name: ``cause``
         :type: (:ref:`cookies.OnChangedCause`)

         The underlying reason behind the cookie's change.

      .. api-member::
         :name: ``cookie``
         :type: (:ref:`cookies.Cookie`)

         Information about the cookie that was set or removed.

      .. api-member::
         :name: ``removed``
         :type: (boolean)

         True if a cookie was removed.

.. api-header::
   :label: Required permissions

   - :permission:`cookies`

.. rst-class:: api-main-section

Types
=====

.. _cookies.Cookie:

Cookie
------

.. api-section-annotation-hack:: -- [Added in TB 45]

Represents information about an HTTP cookie.

.. api-header::
   :label: object

   .. api-member::
      :name: ``domain``
      :type: (string)

      The domain of the cookie (e.g. "www.google.com", "example.com").

   .. api-member::
      :name: ``firstPartyDomain``
      :type: (string)
      :annotation: -- [Added in TB 59]

      The first-party domain of the cookie.

   .. api-member::
      :name: ``hostOnly``
      :type: (boolean)

      True if the cookie is a host-only cookie (i.e. a request's host must exactly match the domain of the cookie).

   .. api-member::
      :name: ``httpOnly``
      :type: (boolean)

      True if the cookie is marked as HttpOnly (i.e. the cookie is inaccessible to client-side scripts).

   .. api-member::
      :name: ``name``
      :type: (string)

      The name of the cookie.

   .. api-member::
      :name: ``path``
      :type: (string)

      The path of the cookie.

   .. api-member::
      :name: ``sameSite``
      :type: (:ref:`cookies.SameSiteStatus`)
      :annotation: -- [Added in TB 63]

      The cookie's same-site status (i.e. whether the cookie is sent with cross-site requests).

   .. api-member::
      :name: ``secure``
      :type: (boolean)

      True if the cookie is marked as Secure (i.e. its scope is limited to secure channels, typically HTTPS).

   .. api-member::
      :name: ``session``
      :type: (boolean)

      True if the cookie is a session cookie, as opposed to a persistent cookie with an expiration date.

   .. api-member::
      :name: ``storeId``
      :type: (string)

      The ID of the cookie store containing this cookie, as provided in getAllCookieStores().

   .. api-member::
      :name: ``value``
      :type: (string)

      The value of the cookie.

   .. api-member::
      :name: [``expirationDate``]
      :type: (number, optional)

      The expiration date of the cookie as the number of seconds since the UNIX epoch. Not provided for session cookies.

   .. api-member::
      :name: [``partitionKey``]
      :type: (:ref:`cookies.PartitionKey`, optional)
      :annotation: -- [Added in TB 94]

      The cookie's storage partition, if any. null if not partitioned.

.. _cookies.CookieStore:

CookieStore
-----------

.. api-section-annotation-hack:: -- [Added in TB 45]

Represents a cookie store in the browser. An incognito mode window, for instance, uses a separate cookie store from a non-incognito window.

.. api-header::
   :label: object

   .. api-member::
      :name: ``id``
      :type: (string)

      The unique identifier for the cookie store.

   .. api-member::
      :name: ``incognito``
      :type: (boolean)
      :annotation: -- [Added in TB 52]

      Indicates if this is an incognito cookie store

   .. api-member::
      :name: ``tabIds``
      :type: (array of integer)
      :annotation: -- [Added in TB 52]

      Identifiers of all the browser tabs that share this cookie store.

.. _cookies.OnChangedCause:

OnChangedCause
--------------

.. api-section-annotation-hack:: -- [Added in TB 45]

The underlying reason behind the cookie's change. If a cookie was inserted, or removed via an explicit call to :ref:`cookies.remove`, "cause" will be "explicit". If a cookie was automatically removed due to expiry, "cause" will be "expired". If a cookie was removed due to being overwritten with an already-expired expiration date, "cause" will be set to "expired_overwrite".  If a cookie was automatically removed due to garbage collection, "cause" will be "evicted".  If a cookie was automatically removed due to a "set" call that overwrote it, "cause" will be "overwrite". Plan your response accordingly.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`evicted`

         .. api-member::
            :name: :value:`expired`

         .. api-member::
            :name: :value:`explicit`

         .. api-member::
            :name: :value:`expired_overwrite`

         .. api-member::
            :name: :value:`overwrite`

.. _cookies.PartitionKey:

PartitionKey
------------

.. api-section-annotation-hack:: 

The description of the storage partition of a cookie. This object may be omitted (null) if a cookie is not partitioned.

.. api-header::
   :label: object

   .. api-member::
      :name: [``hasCrossSiteAncestor``]
      :type: (boolean, optional)

      Whether or not the cookie is in a third-party context, respecting ancestor chains.

   .. api-member::
      :name: [``topLevelSite``]
      :type: (string, optional)

      The first-party URL of the cookie, if the cookie is in storage partitioned by the top-level site.

.. _cookies.SameSiteStatus:

SameSiteStatus
--------------

.. api-section-annotation-hack:: 

A cookie's 'SameSite' state (https://tools.ietf.org/html/draft-west-first-party-cookies). 'no_restriction' corresponds to a cookie set without a 'SameSite' attribute, 'lax' to 'SameSite=Lax', and 'strict' to 'SameSite=Strict'.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`unspecified`

         .. api-member::
            :name: :value:`no_restriction`

         .. api-member::
            :name: :value:`lax`

         .. api-member::
            :name: :value:`strict`
