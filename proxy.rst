.. container:: sticky-sidebar

  ≡ proxy API

  * `Permissions`_
  * `Events`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

=========
proxy API
=========

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The proxy API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/proxy>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Provides access to global proxy settings for Thunderbird and proxy event listeners to handle dynamic proxy implementations.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _proxy.permission.proxy:

.. api-member::
   :name: :permission:`proxy`
   :refid: proxy-permission-proxy
   :refname: proxy

   Control browser proxy settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`proxy` is required to use ``messenger.proxy.*``.

.. rst-class:: api-main-section

Events
======

.. _proxy.on^error:

onError
-------

.. api-section-annotation-hack:: 

Notifies about errors caused by the invalid use of the proxy API.

.. api-header::
   :label: Parameters for onError.addListener(listener)

   .. _proxy.on^error.listener(error):

   .. api-member::
      :name: ``listener(error)``
      :refid: proxy-on-error-listener-error
      :refname: listener(error)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _proxy.on^error.error:

   .. api-member::
      :name: ``error``
      :refid: proxy-on-error-error
      :refname: error
      :type: (object)

.. api-header::
   :label: Required permissions

   - :permission:`proxy`

.. _proxy.on^request:

onRequest
---------

.. api-section-annotation-hack:: -- [Added in TB 147]

Fired when proxy data is needed for a request.

.. note::

   Before version 78, the :code:`tabId` and :code:`windowId` filter properties are ignored.

.. api-header::
   :label: Parameters for onRequest.addListener(listener, filter, extraInfoSpec)

   .. _proxy.on^request.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: proxy-on-request-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _proxy.on^request.filter:

   .. api-member::
      :name: ``filter``
      :refid: proxy-on-request-filter
      :refname: filter
      :type: (:ref:`web^request.^request^filter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. _proxy.on^request.extra^info^spec:

   .. api-member::
      :name: [``extraInfoSpec``]
      :refid: proxy-on-request-extra-info-spec
      :refname: extraInfoSpec
      :type: (array of `string`, optional)

      Array of extra information that should be passed to the listener function.

      Supported values:

      .. api-member::
         :name: :value:`requestHeaders`
         :refname: requestHeaders

.. api-header::
   :label: Parameters passed to the listener function

   .. _proxy.on^request.details:

   .. api-member::
      :name: ``details``
      :refid: proxy-on-request-details
      :refname: details
      :type: (object)

      .. _proxy.on^request.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: proxy-on-request-details-frame-id
         :refname: frameId
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. _proxy.on^request.details.from^cache:

      .. api-member::
         :name: ``fromCache``
         :refid: proxy-on-request-details-from-cache
         :refname: fromCache
         :type: (boolean)

         Indicates if this response was fetched from disk cache.

      .. _proxy.on^request.details.method:

      .. api-member::
         :name: ``method``
         :refid: proxy-on-request-details-method
         :refname: method
         :type: (string)

         Standard HTTP method.

      .. _proxy.on^request.details.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: proxy-on-request-details-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. _proxy.on^request.details.request^id:

      .. api-member::
         :name: ``requestId``
         :refid: proxy-on-request-details-request-id
         :refname: requestId
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. _proxy.on^request.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: proxy-on-request-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. _proxy.on^request.details.third^party:

      .. api-member::
         :name: ``thirdParty``
         :refid: proxy-on-request-details-third-party
         :refname: thirdParty
         :type: (boolean)

         Indicates if this request and its content window hierarchy is third party.

      .. _proxy.on^request.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: proxy-on-request-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. _proxy.on^request.details.type:

      .. api-member::
         :name: ``type``
         :refid: proxy-on-request-details-type
         :refname: type
         :type: (:ref:`web^request.^resource^type`)

         How the requested resource will be used.

      .. _proxy.on^request.details.url:

      .. api-member::
         :name: ``url``
         :refid: proxy-on-request-details-url
         :refname: url
         :type: (string)

      .. _proxy.on^request.details.url^classification:

      .. api-member::
         :name: ``urlClassification``
         :refid: proxy-on-request-details-url-classification
         :refname: urlClassification
         :type: (:ref:`web^request.^url^classification`)

         Url classification if the request has been classified.

      .. _proxy.on^request.details.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: proxy-on-request-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)

         The cookie store ID of the contextual identity.

      .. _proxy.on^request.details.document^url:

      .. api-member::
         :name: [``documentUrl``]
         :refid: proxy-on-request-details-document-url
         :refname: documentUrl
         :type: (string, optional)

         URL of the page into which the requested resource will be loaded.

      .. _proxy.on^request.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: proxy-on-request-details-incognito
         :refname: incognito
         :type: (boolean, optional)

         True for private browsing requests.

      .. _proxy.on^request.details.origin^url:

      .. api-member::
         :name: [``originUrl``]
         :refid: proxy-on-request-details-origin-url
         :refname: originUrl
         :type: (string, optional)

         URL of the resource that triggered this request.

      .. _proxy.on^request.details.request^headers:

      .. api-member::
         :name: [``requestHeaders``]
         :refid: proxy-on-request-details-request-headers
         :refname: requestHeaders
         :type: (:ref:`web^request.^http^headers`, optional)

         The HTTP request headers that are going to be sent out with this request.

.. api-header::
   :label: Required permissions

   - :permission:`proxy`

.. rst-class:: api-main-section

Types
=====

.. _proxy.^proxy^config:

ProxyConfig
-----------

.. api-section-annotation-hack:: 

An object which describes proxy settings.

.. api-header::
   :label: object

   .. _proxy.^proxy^config.auto^config^url:

   .. api-member::
      :name: [``autoConfigUrl``]
      :refid: proxy-proxy-config-auto-config-url
      :refname: autoConfigUrl
      :type: (string, optional)

      A URL to use to configure the proxy.

   .. _proxy.^proxy^config.auto^login:

   .. api-member::
      :name: [``autoLogin``]
      :refid: proxy-proxy-config-auto-login
      :refname: autoLogin
      :type: (boolean, optional)

      Do not prompt for authentication if password is saved.

   .. _proxy.^proxy^config.ftp:

   .. api-member::
      :name: [``ftp``]
      :refid: proxy-proxy-config-ftp
      :refname: ftp
      :type: (string, optional) **Deprecated.**

      The address of the ftp proxy, can include a port.  Deprecated since Thunderbird 88.

   .. _proxy.^proxy^config.http:

   .. api-member::
      :name: [``http``]
      :refid: proxy-proxy-config-http
      :refname: http
      :type: (string, optional)

      The address of the http proxy, can include a port.

   .. _proxy.^proxy^config.http^proxy^all:

   .. api-member::
      :name: [``httpProxyAll``]
      :refid: proxy-proxy-config-http-proxy-all
      :refname: httpProxyAll
      :type: (boolean, optional)

      Use the http proxy server for all protocols.

   .. _proxy.^proxy^config.passthrough:

   .. api-member::
      :name: [``passthrough``]
      :refid: proxy-proxy-config-passthrough
      :refname: passthrough
      :type: (string, optional)

      A list of hosts which should not be proxied.

   .. _proxy.^proxy^config.proxy^d^n^s:

   .. api-member::
      :name: [``proxyDNS``]
      :refid: proxy-proxy-config-proxy-d-n-s
      :refname: proxyDNS
      :type: (boolean, optional)

      Proxy DNS when using SOCKS. DNS queries get leaked to the network when set to false. True by default for SOCKS v5. False by default for SOCKS v4.

   .. _proxy.^proxy^config.proxy^type:

   .. api-member::
      :name: [``proxyType``]
      :refid: proxy-proxy-config-proxy-type
      :refname: proxyType
      :type: (`string`, optional)

      The type of proxy to use.

      Supported values:

      .. _proxy.^proxy^config.proxy^type.auto^config:

      .. api-member::
         :name: :value:`autoConfig`
         :refid: proxy-proxy-config-proxy-type-auto-config
         :refname: autoConfig

      .. _proxy.^proxy^config.proxy^type.auto^detect:

      .. api-member::
         :name: :value:`autoDetect`
         :refid: proxy-proxy-config-proxy-type-auto-detect
         :refname: autoDetect

      .. _proxy.^proxy^config.proxy^type.manual:

      .. api-member::
         :name: :value:`manual`
         :refid: proxy-proxy-config-proxy-type-manual
         :refname: manual

      .. _proxy.^proxy^config.proxy^type.none:

      .. api-member::
         :name: :value:`none`
         :refid: proxy-proxy-config-proxy-type-none
         :refname: none

      .. _proxy.^proxy^config.proxy^type.system:

      .. api-member::
         :name: :value:`system`
         :refid: proxy-proxy-config-proxy-type-system
         :refname: system

   .. _proxy.^proxy^config.respect^be^conservative:

   .. api-member::
      :name: [``respectBeConservative``]
      :refid: proxy-proxy-config-respect-be-conservative
      :refname: respectBeConservative
      :type: (boolean, optional)

      If true (the default value), do not use newer TLS protocol features that might have interoperability problems on the Internet. This is intended only for use with critical infrastructure like the updates, and is only available to privileged addons.

   .. _proxy.^proxy^config.socks:

   .. api-member::
      :name: [``socks``]
      :refid: proxy-proxy-config-socks
      :refname: socks
      :type: (string, optional)

      The address of the socks proxy, can include a port.

   .. _proxy.^proxy^config.socks^version:

   .. api-member::
      :name: [``socksVersion``]
      :refid: proxy-proxy-config-socks-version
      :refname: socksVersion
      :type: (integer, optional)

      The version of the socks proxy.

   .. _proxy.^proxy^config.ssl:

   .. api-member::
      :name: [``ssl``]
      :refid: proxy-proxy-config-ssl
      :refname: ssl
      :type: (string, optional)

      The address of the ssl proxy, can include a port.

.. rst-class:: api-main-section

Properties
==========

.. _proxy.settings:

settings
--------

.. api-section-annotation-hack:: 

Configures proxy settings. This setting's value is an object of type ProxyConfig.

.. note::

   Not supported in Thunderbird because it depends on private browsing functionality, which Thunderbird does not fully implement.

.. note::

   From version 88, the :code:`ftp` setting has no effect because FTP is no longer supported (see `bug 1626365 <https://bugzil.la/1626365>`__).
