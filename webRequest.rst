.. container:: sticky-sidebar

  ≡ webRequest API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

==============
webRequest API
==============

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The webRequest API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/webRequest>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.webRequest` API to observe and analyze traffic and to intercept, block, or modify requests in-flight.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _web^request.permission.web^request:

.. api-member::
   :name: :permission:`webRequest`
   :refid: web-request-permission-web-request
   :refname: webRequest

   Grant access to some or all methods of the webRequest API.

.. _web^request.permission.web^request^blocking:

.. api-member::
   :name: :permission:`webRequestBlocking`
   :refid: web-request-permission-web-request-blocking
   :refname: webRequestBlocking

   Allows to use the blocking features of the webRequest API. With this permission, listeners can synchronously modify or cancel requests before they are sent or before a response is delivered. Without it, listeners can only observe requests without blocking or altering them.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`webRequest` is required to use ``messenger.webRequest.*``.

.. rst-class:: api-main-section

Functions
=========

.. _web^request.filter^response^data:

filterResponseData(requestId)
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

...

.. api-header::
   :label: Parameters

   .. _web^request.filter^response^data.request^id:

   .. api-member::
      :name: ``requestId``
      :refid: web-request-filter-response-data-request-id
      :refname: requestId
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _web^request.filter^response^data.returns:

   .. api-member::
      :refid: web-request-filter-response-data-returns
      :refname: _returns
      :type: `StreamFilter <https://developer.mozilla.org/en-US/docs/Web/API/StreamFilter>`__

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`
   - :permission:`webRequestBlocking`

.. _web^request.get^security^info:

getSecurityInfo(requestId, [options])
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Retrieves the security information for the request.  Returns a promise that will resolve to a SecurityInfo object.

.. api-header::
   :label: Parameters

   .. _web^request.get^security^info.request^id:

   .. api-member::
      :name: ``requestId``
      :refid: web-request-get-security-info-request-id
      :refname: requestId
      :type: (string)

   .. _web^request.get^security^info.options:

   .. api-member::
      :name: [``options``]
      :refid: web-request-get-security-info-options
      :refname: options
      :type: (object, optional)

      .. _web^request.get^security^info.options.certificate^chain:

      .. api-member::
         :name: [``certificateChain``]
         :refid: web-request-get-security-info-options-certificate-chain
         :refname: certificateChain
         :type: (boolean, optional)

         Include the entire certificate chain.

      .. _web^request.get^security^info.options.raw^d^e^r:

      .. api-member::
         :name: [``rawDER``]
         :refid: web-request-get-security-info-options-raw-d-e-r
         :refname: rawDER
         :type: (boolean, optional)

         Include raw certificate data for processing by the extension.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _web^request.handler^behavior^changed:

handlerBehaviorChanged()
------------------------

.. api-section-annotation-hack:: 

Needs to be called when the behavior of the webRequest handlers has changed to prevent incorrect handling due to caching. This function call is expensive. Don't call it often.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. rst-class:: api-main-section

Events
======

.. _web^request.on^auth^required:

onAuthRequired
--------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when an authentication failure is received. The listener has three options: it can provide authentication credentials, it can cancel the request and display the error page, or it can take no action on the challenge. If bad user credentials are provided, this may be called multiple times for the same request.

.. note::

   To handle a request asynchronously, return a Promise from the listener.

.. api-header::
   :label: Parameters for onAuthRequired.addListener(listener, filter, extraInfoSpec)

   .. _web^request.on^auth^required.listener(details, async^callback):

   .. api-member::
      :name: ``listener(details, asyncCallback)``
      :refid: web-request-on-auth-required-listener-details-async-callback
      :refname: listener(details, asyncCallback)

      A function that will be called when this event occurs.

   .. _web^request.on^auth^required.filter:

   .. api-member::
      :name: ``filter``
      :refid: web-request-on-auth-required-filter
      :refname: filter
      :type: (:ref:`web^request.^request^filter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. _web^request.on^auth^required.extra^info^spec:

   .. api-member::
      :name: [``extraInfoSpec``]
      :refid: web-request-on-auth-required-extra-info-spec
      :refname: extraInfoSpec
      :type: (array of :ref:`web^request.^on^auth^required^options`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^request.on^auth^required.details:

   .. api-member::
      :name: ``details``
      :refid: web-request-on-auth-required-details
      :refname: details
      :type: (object)

      .. _web^request.on^auth^required.details.challenger:

      .. api-member::
         :name: ``challenger``
         :refid: web-request-on-auth-required-details-challenger
         :refname: challenger
         :type: (object)

         The server requesting authentication.

         .. note::

            Before version 57, when authenticating to a proxy server, the :code:`challenger.host` property contains the hostname for the requested URL rather than the hostname for the proxy.

         .. _web^request.on^auth^required.details.challenger.host:

         .. api-member::
            :name: ``host``
            :refid: web-request-on-auth-required-details-challenger-host
            :refname: host
            :type: (string)

         .. _web^request.on^auth^required.details.challenger.port:

         .. api-member::
            :name: ``port``
            :refid: web-request-on-auth-required-details-challenger-port
            :refname: port
            :type: (integer)

      .. _web^request.on^auth^required.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-request-on-auth-required-details-frame-id
         :refname: frameId
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. _web^request.on^auth^required.details.is^proxy:

      .. api-member::
         :name: ``isProxy``
         :refid: web-request-on-auth-required-details-is-proxy
         :refname: isProxy
         :type: (boolean)

         True for Proxy-Authenticate, false for WWW-Authenticate.

      .. _web^request.on^auth^required.details.method:

      .. api-member::
         :name: ``method``
         :refid: web-request-on-auth-required-details-method
         :refname: method
         :type: (string)

         Standard HTTP method.

      .. _web^request.on^auth^required.details.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: web-request-on-auth-required-details-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. _web^request.on^auth^required.details.request^id:

      .. api-member::
         :name: ``requestId``
         :refid: web-request-on-auth-required-details-request-id
         :refname: requestId
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. _web^request.on^auth^required.details.scheme:

      .. api-member::
         :name: ``scheme``
         :refid: web-request-on-auth-required-details-scheme
         :refname: scheme
         :type: (string)

         The authentication scheme, e.g. Basic or Digest.

      .. _web^request.on^auth^required.details.status^code:

      .. api-member::
         :name: ``statusCode``
         :refid: web-request-on-auth-required-details-status-code
         :refname: statusCode
         :type: (integer)

         Standard HTTP status code returned by the server.

      .. _web^request.on^auth^required.details.status^line:

      .. api-member::
         :name: ``statusLine``
         :refid: web-request-on-auth-required-details-status-line
         :refname: statusLine
         :type: (string)

         HTTP status line of the response or the 'HTTP/0.9 200 OK' string for HTTP/0.9 responses (i.e., responses that lack a status line) or an empty string if there are no headers.

      .. _web^request.on^auth^required.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-request-on-auth-required-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. _web^request.on^auth^required.details.third^party:

      .. api-member::
         :name: ``thirdParty``
         :refid: web-request-on-auth-required-details-third-party
         :refname: thirdParty
         :type: (boolean)
         :annotation: -- [Added in TB 78.0]

         Indicates if this request and its content window hierarchy is third party.

      .. _web^request.on^auth^required.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-request-on-auth-required-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. _web^request.on^auth^required.details.type:

      .. api-member::
         :name: ``type``
         :refid: web-request-on-auth-required-details-type
         :refname: type
         :type: (:ref:`web^request.^resource^type`)

         How the requested resource will be used.

      .. _web^request.on^auth^required.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-request-on-auth-required-details-url
         :refname: url
         :type: (string)

      .. _web^request.on^auth^required.details.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: web-request-on-auth-required-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0]

         The cookie store ID of the contextual identity.

      .. _web^request.on^auth^required.details.document^id:

      .. api-member::
         :name: [``documentId``]
         :refid: web-request-on-auth-required-details-document-id
         :refname: documentId
         :type: (string, optional)

         The UUID of the document making the request.

      .. _web^request.on^auth^required.details.document^url:

      .. api-member::
         :name: [``documentUrl``]
         :refid: web-request-on-auth-required-details-document-url
         :refname: documentUrl
         :type: (string, optional)

         URL of the page into which the requested resource will be loaded.

      .. _web^request.on^auth^required.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: web-request-on-auth-required-details-incognito
         :refname: incognito
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68.0]

         True for private browsing requests.

      .. _web^request.on^auth^required.details.origin^url:

      .. api-member::
         :name: [``originUrl``]
         :refid: web-request-on-auth-required-details-origin-url
         :refname: originUrl
         :type: (string, optional)

         URL of the resource that triggered this request.

      .. _web^request.on^auth^required.details.parent^document^id:

      .. api-member::
         :name: [``parentDocumentId``]
         :refid: web-request-on-auth-required-details-parent-document-id
         :refname: parentDocumentId
         :type: (string, optional)

         The UUID of the parent document owning this frame. This is not set if there is no parent.

      .. _web^request.on^auth^required.details.realm:

      .. api-member::
         :name: [``realm``]
         :refid: web-request-on-auth-required-details-realm
         :refname: realm
         :type: (string, optional)

         The authentication realm provided by the server, if there is one.

      .. _web^request.on^auth^required.details.response^headers:

      .. api-member::
         :name: [``responseHeaders``]
         :refid: web-request-on-auth-required-details-response-headers
         :refname: responseHeaders
         :type: (:ref:`web^request.^http^headers`, optional)

         The HTTP response headers that were received along with this response.

      .. _web^request.on^auth^required.details.url^classification:

      .. api-member::
         :name: [``urlClassification``]
         :refid: web-request-on-auth-required-details-url-classification
         :refname: urlClassification
         :type: (:ref:`web^request.^url^classification`, optional)
         :annotation: -- [Added in TB 78.0]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

   .. _web^request.on^auth^required.async^callback:

   .. api-member::
      :name: [``asyncCallback``]
      :refid: web-request-on-auth-required-async-callback
      :refname: asyncCallback
      :type: (function, optional)

.. api-header::
   :label: Expected return value of the listener function

   .. _web^request.on^auth^required.returns:

   .. api-member::
      :refid: web-request-on-auth-required-returns
      :type: :ref:`web^request.^blocking^response`

      If "blocking" is specified in the "extraInfoSpec" parameter, the event listener should return an object of this type.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _web^request.on^before^redirect:

onBeforeRedirect
----------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when a server-initiated redirect is about to occur.

.. api-header::
   :label: Parameters for onBeforeRedirect.addListener(listener, filter, extraInfoSpec)

   .. _web^request.on^before^redirect.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-request-on-before-redirect-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^request.on^before^redirect.filter:

   .. api-member::
      :name: ``filter``
      :refid: web-request-on-before-redirect-filter
      :refname: filter
      :type: (:ref:`web^request.^request^filter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. _web^request.on^before^redirect.extra^info^spec:

   .. api-member::
      :name: [``extraInfoSpec``]
      :refid: web-request-on-before-redirect-extra-info-spec
      :refname: extraInfoSpec
      :type: (array of :ref:`web^request.^on^before^redirect^options`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^request.on^before^redirect.details:

   .. api-member::
      :name: ``details``
      :refid: web-request-on-before-redirect-details
      :refname: details
      :type: (object)

      .. _web^request.on^before^redirect.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-request-on-before-redirect-details-frame-id
         :refname: frameId
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. _web^request.on^before^redirect.details.from^cache:

      .. api-member::
         :name: ``fromCache``
         :refid: web-request-on-before-redirect-details-from-cache
         :refname: fromCache
         :type: (boolean)

         Indicates if this response was fetched from disk cache.

      .. _web^request.on^before^redirect.details.method:

      .. api-member::
         :name: ``method``
         :refid: web-request-on-before-redirect-details-method
         :refname: method
         :type: (string)

         Standard HTTP method.

      .. _web^request.on^before^redirect.details.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: web-request-on-before-redirect-details-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. _web^request.on^before^redirect.details.redirect^url:

      .. api-member::
         :name: ``redirectUrl``
         :refid: web-request-on-before-redirect-details-redirect-url
         :refname: redirectUrl
         :type: (string)

         The new URL.

      .. _web^request.on^before^redirect.details.request^id:

      .. api-member::
         :name: ``requestId``
         :refid: web-request-on-before-redirect-details-request-id
         :refname: requestId
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. _web^request.on^before^redirect.details.status^code:

      .. api-member::
         :name: ``statusCode``
         :refid: web-request-on-before-redirect-details-status-code
         :refname: statusCode
         :type: (integer)

         Standard HTTP status code returned by the server.

      .. _web^request.on^before^redirect.details.status^line:

      .. api-member::
         :name: ``statusLine``
         :refid: web-request-on-before-redirect-details-status-line
         :refname: statusLine
         :type: (string)

         HTTP status line of the response or the 'HTTP/0.9 200 OK' string for HTTP/0.9 responses (i.e., responses that lack a status line) or an empty string if there are no headers.

      .. _web^request.on^before^redirect.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-request-on-before-redirect-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. _web^request.on^before^redirect.details.third^party:

      .. api-member::
         :name: ``thirdParty``
         :refid: web-request-on-before-redirect-details-third-party
         :refname: thirdParty
         :type: (boolean)
         :annotation: -- [Added in TB 78.0]

         Indicates if this request and its content window hierarchy is third party.

      .. _web^request.on^before^redirect.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-request-on-before-redirect-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. _web^request.on^before^redirect.details.type:

      .. api-member::
         :name: ``type``
         :refid: web-request-on-before-redirect-details-type
         :refname: type
         :type: (:ref:`web^request.^resource^type`)

         How the requested resource will be used.

      .. _web^request.on^before^redirect.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-request-on-before-redirect-details-url
         :refname: url
         :type: (string)

      .. _web^request.on^before^redirect.details.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: web-request-on-before-redirect-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0]

         The cookie store ID of the contextual identity.

      .. _web^request.on^before^redirect.details.document^id:

      .. api-member::
         :name: [``documentId``]
         :refid: web-request-on-before-redirect-details-document-id
         :refname: documentId
         :type: (string, optional)

         The UUID of the document making the request.

      .. _web^request.on^before^redirect.details.document^url:

      .. api-member::
         :name: [``documentUrl``]
         :refid: web-request-on-before-redirect-details-document-url
         :refname: documentUrl
         :type: (string, optional)

         URL of the page into which the requested resource will be loaded.

      .. _web^request.on^before^redirect.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: web-request-on-before-redirect-details-incognito
         :refname: incognito
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68.0]

         True for private browsing requests.

      .. _web^request.on^before^redirect.details.ip:

      .. api-member::
         :name: [``ip``]
         :refid: web-request-on-before-redirect-details-ip
         :refname: ip
         :type: (string, optional)

         The server IP address that the request was actually sent to. Note that it may be a literal IPv6 address.

      .. _web^request.on^before^redirect.details.origin^url:

      .. api-member::
         :name: [``originUrl``]
         :refid: web-request-on-before-redirect-details-origin-url
         :refname: originUrl
         :type: (string, optional)

         URL of the resource that triggered this request.

      .. _web^request.on^before^redirect.details.parent^document^id:

      .. api-member::
         :name: [``parentDocumentId``]
         :refid: web-request-on-before-redirect-details-parent-document-id
         :refname: parentDocumentId
         :type: (string, optional)

         The UUID of the parent document owning this frame. This is not set if there is no parent.

      .. _web^request.on^before^redirect.details.response^headers:

      .. api-member::
         :name: [``responseHeaders``]
         :refid: web-request-on-before-redirect-details-response-headers
         :refname: responseHeaders
         :type: (:ref:`web^request.^http^headers`, optional)

         The HTTP response headers that were received along with this redirect.

      .. _web^request.on^before^redirect.details.url^classification:

      .. api-member::
         :name: [``urlClassification``]
         :refid: web-request-on-before-redirect-details-url-classification
         :refname: urlClassification
         :type: (:ref:`web^request.^url^classification`, optional)
         :annotation: -- [Added in TB 78.0]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _web^request.on^before^request:

onBeforeRequest
---------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when a request is about to occur.

.. note::

   Asynchronous event listeners are supported from version 52.

.. api-header::
   :label: Parameters for onBeforeRequest.addListener(listener, filter, extraInfoSpec)

   .. _web^request.on^before^request.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-request-on-before-request-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^request.on^before^request.filter:

   .. api-member::
      :name: ``filter``
      :refid: web-request-on-before-request-filter
      :refname: filter
      :type: (:ref:`web^request.^request^filter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. _web^request.on^before^request.extra^info^spec:

   .. api-member::
      :name: [``extraInfoSpec``]
      :refid: web-request-on-before-request-extra-info-spec
      :refname: extraInfoSpec
      :type: (array of :ref:`web^request.^on^before^request^options`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^request.on^before^request.details:

   .. api-member::
      :name: ``details``
      :refid: web-request-on-before-request-details
      :refname: details
      :type: (object)

      .. _web^request.on^before^request.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-request-on-before-request-details-frame-id
         :refname: frameId
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. _web^request.on^before^request.details.method:

      .. api-member::
         :name: ``method``
         :refid: web-request-on-before-request-details-method
         :refname: method
         :type: (string)

         Standard HTTP method.

      .. _web^request.on^before^request.details.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: web-request-on-before-request-details-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. _web^request.on^before^request.details.request^id:

      .. api-member::
         :name: ``requestId``
         :refid: web-request-on-before-request-details-request-id
         :refname: requestId
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. _web^request.on^before^request.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-request-on-before-request-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. _web^request.on^before^request.details.third^party:

      .. api-member::
         :name: ``thirdParty``
         :refid: web-request-on-before-request-details-third-party
         :refname: thirdParty
         :type: (boolean)
         :annotation: -- [Added in TB 78.0]

         Indicates if this request and its content window hierarchy is third party.

      .. _web^request.on^before^request.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-request-on-before-request-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. _web^request.on^before^request.details.type:

      .. api-member::
         :name: ``type``
         :refid: web-request-on-before-request-details-type
         :refname: type
         :type: (:ref:`web^request.^resource^type`)

         How the requested resource will be used.

      .. _web^request.on^before^request.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-request-on-before-request-details-url
         :refname: url
         :type: (string)

      .. _web^request.on^before^request.details.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: web-request-on-before-request-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0]

         The cookie store ID of the contextual identity.

      .. _web^request.on^before^request.details.document^id:

      .. api-member::
         :name: [``documentId``]
         :refid: web-request-on-before-request-details-document-id
         :refname: documentId
         :type: (string, optional)

         The UUID of the document making the request.

      .. _web^request.on^before^request.details.document^url:

      .. api-member::
         :name: [``documentUrl``]
         :refid: web-request-on-before-request-details-document-url
         :refname: documentUrl
         :type: (string, optional)

         URL of the page into which the requested resource will be loaded.

      .. _web^request.on^before^request.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: web-request-on-before-request-details-incognito
         :refname: incognito
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68.0]

         True for private browsing requests.

      .. _web^request.on^before^request.details.origin^url:

      .. api-member::
         :name: [``originUrl``]
         :refid: web-request-on-before-request-details-origin-url
         :refname: originUrl
         :type: (string, optional)

         URL of the resource that triggered this request.

      .. _web^request.on^before^request.details.parent^document^id:

      .. api-member::
         :name: [``parentDocumentId``]
         :refid: web-request-on-before-request-details-parent-document-id
         :refname: parentDocumentId
         :type: (string, optional)

         The UUID of the parent document owning this frame. This is not set if there is no parent.

      .. _web^request.on^before^request.details.request^body:

      .. api-member::
         :name: [``requestBody``]
         :refid: web-request-on-before-request-details-request-body
         :refname: requestBody
         :type: (object, optional)

         Contains the HTTP request body data. Only provided if extraInfoSpec contains 'requestBody'.

         .. _web^request.on^before^request.details.request^body.error:

         .. api-member::
            :name: [``error``]
            :refid: web-request-on-before-request-details-request-body-error
            :refname: error
            :type: (string, optional)

            Errors when obtaining request body data.

         .. _web^request.on^before^request.details.request^body.form^data:

         .. api-member::
            :name: [``formData``]
            :refid: web-request-on-before-request-details-request-body-form-data
            :refname: formData
            :type: (object, optional)

            If the request method is POST and the body is a sequence of key-value pairs encoded in UTF8, encoded as either multipart/form-data, or application/x-www-form-urlencoded, this dictionary is present and for each key contains the list of all values for that key. If the data is of another media type, or if it is malformed, the dictionary is not present. An example value of this dictionary is {'key': ['value1', 'value2']}.

         .. _web^request.on^before^request.details.request^body.raw:

         .. api-member::
            :name: [``raw``]
            :refid: web-request-on-before-request-details-request-body-raw
            :refname: raw
            :type: (array of :ref:`web^request.^upload^data`, optional)

            If the request method is PUT or POST, and the body is not already parsed in formData, then the unparsed request body elements are contained in this array.

      .. _web^request.on^before^request.details.url^classification:

      .. api-member::
         :name: [``urlClassification``]
         :refid: web-request-on-before-request-details-url-classification
         :refname: urlClassification
         :type: (:ref:`web^request.^url^classification`, optional)
         :annotation: -- [Added in TB 78.0]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Expected return value of the listener function

   .. _web^request.on^before^request.returns:

   .. api-member::
      :refid: web-request-on-before-request-returns
      :type: :ref:`web^request.^blocking^response`

      If "blocking" is specified in the "extraInfoSpec" parameter, the event listener should return an object of this type.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _web^request.on^before^send^headers:

onBeforeSendHeaders
-------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired before sending an HTTP request, once the request headers are available. This may occur after a TCP connection is made to the server, but before any HTTP data is sent.

.. note::

   Asynchronous event listeners are supported from version 52.

.. api-header::
   :label: Parameters for onBeforeSendHeaders.addListener(listener, filter, extraInfoSpec)

   .. _web^request.on^before^send^headers.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-request-on-before-send-headers-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^request.on^before^send^headers.filter:

   .. api-member::
      :name: ``filter``
      :refid: web-request-on-before-send-headers-filter
      :refname: filter
      :type: (:ref:`web^request.^request^filter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. _web^request.on^before^send^headers.extra^info^spec:

   .. api-member::
      :name: [``extraInfoSpec``]
      :refid: web-request-on-before-send-headers-extra-info-spec
      :refname: extraInfoSpec
      :type: (array of :ref:`web^request.^on^before^send^headers^options`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^request.on^before^send^headers.details:

   .. api-member::
      :name: ``details``
      :refid: web-request-on-before-send-headers-details
      :refname: details
      :type: (object)

      .. _web^request.on^before^send^headers.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-request-on-before-send-headers-details-frame-id
         :refname: frameId
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. _web^request.on^before^send^headers.details.method:

      .. api-member::
         :name: ``method``
         :refid: web-request-on-before-send-headers-details-method
         :refname: method
         :type: (string)

         Standard HTTP method.

      .. _web^request.on^before^send^headers.details.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: web-request-on-before-send-headers-details-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. _web^request.on^before^send^headers.details.request^id:

      .. api-member::
         :name: ``requestId``
         :refid: web-request-on-before-send-headers-details-request-id
         :refname: requestId
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. _web^request.on^before^send^headers.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-request-on-before-send-headers-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. _web^request.on^before^send^headers.details.third^party:

      .. api-member::
         :name: ``thirdParty``
         :refid: web-request-on-before-send-headers-details-third-party
         :refname: thirdParty
         :type: (boolean)
         :annotation: -- [Added in TB 78.0]

         Indicates if this request and its content window hierarchy is third party.

      .. _web^request.on^before^send^headers.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-request-on-before-send-headers-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. _web^request.on^before^send^headers.details.type:

      .. api-member::
         :name: ``type``
         :refid: web-request-on-before-send-headers-details-type
         :refname: type
         :type: (:ref:`web^request.^resource^type`)

         How the requested resource will be used.

      .. _web^request.on^before^send^headers.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-request-on-before-send-headers-details-url
         :refname: url
         :type: (string)

      .. _web^request.on^before^send^headers.details.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: web-request-on-before-send-headers-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0]

         The cookie store ID of the contextual identity.

      .. _web^request.on^before^send^headers.details.document^id:

      .. api-member::
         :name: [``documentId``]
         :refid: web-request-on-before-send-headers-details-document-id
         :refname: documentId
         :type: (string, optional)

         The UUID of the document making the request.

      .. _web^request.on^before^send^headers.details.document^url:

      .. api-member::
         :name: [``documentUrl``]
         :refid: web-request-on-before-send-headers-details-document-url
         :refname: documentUrl
         :type: (string, optional)

         URL of the page into which the requested resource will be loaded.

      .. _web^request.on^before^send^headers.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: web-request-on-before-send-headers-details-incognito
         :refname: incognito
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68.0]

         True for private browsing requests.

      .. _web^request.on^before^send^headers.details.origin^url:

      .. api-member::
         :name: [``originUrl``]
         :refid: web-request-on-before-send-headers-details-origin-url
         :refname: originUrl
         :type: (string, optional)

         URL of the resource that triggered this request.

      .. _web^request.on^before^send^headers.details.parent^document^id:

      .. api-member::
         :name: [``parentDocumentId``]
         :refid: web-request-on-before-send-headers-details-parent-document-id
         :refname: parentDocumentId
         :type: (string, optional)

         The UUID of the parent document owning this frame. This is not set if there is no parent.

      .. _web^request.on^before^send^headers.details.request^headers:

      .. api-member::
         :name: [``requestHeaders``]
         :refid: web-request-on-before-send-headers-details-request-headers
         :refname: requestHeaders
         :type: (:ref:`web^request.^http^headers`, optional)

         The HTTP request headers that are going to be sent out with this request.

      .. _web^request.on^before^send^headers.details.url^classification:

      .. api-member::
         :name: [``urlClassification``]
         :refid: web-request-on-before-send-headers-details-url-classification
         :refname: urlClassification
         :type: (:ref:`web^request.^url^classification`, optional)
         :annotation: -- [Added in TB 78.0]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Expected return value of the listener function

   .. _web^request.on^before^send^headers.returns:

   .. api-member::
      :refid: web-request-on-before-send-headers-returns
      :type: :ref:`web^request.^blocking^response`

      If "blocking" is specified in the "extraInfoSpec" parameter, the event listener should return an object of this type.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _web^request.on^completed:

onCompleted
-----------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when a request is completed.

.. api-header::
   :label: Parameters for onCompleted.addListener(listener, filter, extraInfoSpec)

   .. _web^request.on^completed.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-request-on-completed-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^request.on^completed.filter:

   .. api-member::
      :name: ``filter``
      :refid: web-request-on-completed-filter
      :refname: filter
      :type: (:ref:`web^request.^request^filter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. _web^request.on^completed.extra^info^spec:

   .. api-member::
      :name: [``extraInfoSpec``]
      :refid: web-request-on-completed-extra-info-spec
      :refname: extraInfoSpec
      :type: (array of :ref:`web^request.^on^completed^options`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^request.on^completed.details:

   .. api-member::
      :name: ``details``
      :refid: web-request-on-completed-details
      :refname: details
      :type: (object)

      .. _web^request.on^completed.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-request-on-completed-details-frame-id
         :refname: frameId
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. _web^request.on^completed.details.from^cache:

      .. api-member::
         :name: ``fromCache``
         :refid: web-request-on-completed-details-from-cache
         :refname: fromCache
         :type: (boolean)

         Indicates if this response was fetched from disk cache.

      .. _web^request.on^completed.details.method:

      .. api-member::
         :name: ``method``
         :refid: web-request-on-completed-details-method
         :refname: method
         :type: (string)

         Standard HTTP method.

      .. _web^request.on^completed.details.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: web-request-on-completed-details-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. _web^request.on^completed.details.request^id:

      .. api-member::
         :name: ``requestId``
         :refid: web-request-on-completed-details-request-id
         :refname: requestId
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. _web^request.on^completed.details.request^size:

      .. api-member::
         :name: ``requestSize``
         :refid: web-request-on-completed-details-request-size
         :refname: requestSize
         :type: (integer)

         For http requests, the bytes transferred in the request. Only available in onCompleted.

      .. _web^request.on^completed.details.response^size:

      .. api-member::
         :name: ``responseSize``
         :refid: web-request-on-completed-details-response-size
         :refname: responseSize
         :type: (integer)

         For http requests, the bytes received in the request. Only available in onCompleted.

      .. _web^request.on^completed.details.status^code:

      .. api-member::
         :name: ``statusCode``
         :refid: web-request-on-completed-details-status-code
         :refname: statusCode
         :type: (integer)

         Standard HTTP status code returned by the server.

      .. _web^request.on^completed.details.status^line:

      .. api-member::
         :name: ``statusLine``
         :refid: web-request-on-completed-details-status-line
         :refname: statusLine
         :type: (string)

         HTTP status line of the response or the 'HTTP/0.9 200 OK' string for HTTP/0.9 responses (i.e., responses that lack a status line) or an empty string if there are no headers.

      .. _web^request.on^completed.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-request-on-completed-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. _web^request.on^completed.details.third^party:

      .. api-member::
         :name: ``thirdParty``
         :refid: web-request-on-completed-details-third-party
         :refname: thirdParty
         :type: (boolean)
         :annotation: -- [Added in TB 78.0]

         Indicates if this request and its content window hierarchy is third party.

      .. _web^request.on^completed.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-request-on-completed-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. _web^request.on^completed.details.type:

      .. api-member::
         :name: ``type``
         :refid: web-request-on-completed-details-type
         :refname: type
         :type: (:ref:`web^request.^resource^type`)

         How the requested resource will be used.

      .. _web^request.on^completed.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-request-on-completed-details-url
         :refname: url
         :type: (string)

      .. _web^request.on^completed.details.url^classification:

      .. api-member::
         :name: ``urlClassification``
         :refid: web-request-on-completed-details-url-classification
         :refname: urlClassification
         :type: (:ref:`web^request.^url^classification`)
         :annotation: -- [Added in TB 78.0]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

      .. _web^request.on^completed.details.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: web-request-on-completed-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0]

         The cookie store ID of the contextual identity.

      .. _web^request.on^completed.details.document^id:

      .. api-member::
         :name: [``documentId``]
         :refid: web-request-on-completed-details-document-id
         :refname: documentId
         :type: (string, optional)

         The UUID of the document making the request.

      .. _web^request.on^completed.details.document^url:

      .. api-member::
         :name: [``documentUrl``]
         :refid: web-request-on-completed-details-document-url
         :refname: documentUrl
         :type: (string, optional)

         URL of the page into which the requested resource will be loaded.

      .. _web^request.on^completed.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: web-request-on-completed-details-incognito
         :refname: incognito
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68.0]

         True for private browsing requests.

      .. _web^request.on^completed.details.ip:

      .. api-member::
         :name: [``ip``]
         :refid: web-request-on-completed-details-ip
         :refname: ip
         :type: (string, optional)

         The server IP address that the request was actually sent to. Note that it may be a literal IPv6 address.

      .. _web^request.on^completed.details.origin^url:

      .. api-member::
         :name: [``originUrl``]
         :refid: web-request-on-completed-details-origin-url
         :refname: originUrl
         :type: (string, optional)

         URL of the resource that triggered this request.

      .. _web^request.on^completed.details.parent^document^id:

      .. api-member::
         :name: [``parentDocumentId``]
         :refid: web-request-on-completed-details-parent-document-id
         :refname: parentDocumentId
         :type: (string, optional)

         The UUID of the parent document owning this frame. This is not set if there is no parent.

      .. _web^request.on^completed.details.response^headers:

      .. api-member::
         :name: [``responseHeaders``]
         :refid: web-request-on-completed-details-response-headers
         :refname: responseHeaders
         :type: (:ref:`web^request.^http^headers`, optional)

         The HTTP response headers that were received along with this response.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _web^request.on^error^occurred:

onErrorOccurred
---------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when an error occurs.

.. api-header::
   :label: Parameters for onErrorOccurred.addListener(listener, filter)

   .. _web^request.on^error^occurred.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-request-on-error-occurred-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^request.on^error^occurred.filter:

   .. api-member::
      :name: ``filter``
      :refid: web-request-on-error-occurred-filter
      :refname: filter
      :type: (:ref:`web^request.^request^filter`)

      A set of filters that restricts the events that will be sent to this listener.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^request.on^error^occurred.details:

   .. api-member::
      :name: ``details``
      :refid: web-request-on-error-occurred-details
      :refname: details
      :type: (object)

      .. _web^request.on^error^occurred.details.error:

      .. api-member::
         :name: ``error``
         :refid: web-request-on-error-occurred-details-error
         :refname: error
         :type: (string)

         The error description. This string is *not* guaranteed to remain backwards compatible between releases. You must not parse and act based upon its content.

      .. _web^request.on^error^occurred.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-request-on-error-occurred-details-frame-id
         :refname: frameId
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. _web^request.on^error^occurred.details.from^cache:

      .. api-member::
         :name: ``fromCache``
         :refid: web-request-on-error-occurred-details-from-cache
         :refname: fromCache
         :type: (boolean)

         Indicates if this response was fetched from disk cache.

      .. _web^request.on^error^occurred.details.method:

      .. api-member::
         :name: ``method``
         :refid: web-request-on-error-occurred-details-method
         :refname: method
         :type: (string)

         Standard HTTP method.

      .. _web^request.on^error^occurred.details.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: web-request-on-error-occurred-details-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. _web^request.on^error^occurred.details.request^id:

      .. api-member::
         :name: ``requestId``
         :refid: web-request-on-error-occurred-details-request-id
         :refname: requestId
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. _web^request.on^error^occurred.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-request-on-error-occurred-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. _web^request.on^error^occurred.details.third^party:

      .. api-member::
         :name: ``thirdParty``
         :refid: web-request-on-error-occurred-details-third-party
         :refname: thirdParty
         :type: (boolean)
         :annotation: -- [Added in TB 78.0]

         Indicates if this request and its content window hierarchy is third party.

      .. _web^request.on^error^occurred.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-request-on-error-occurred-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. _web^request.on^error^occurred.details.type:

      .. api-member::
         :name: ``type``
         :refid: web-request-on-error-occurred-details-type
         :refname: type
         :type: (:ref:`web^request.^resource^type`)

         How the requested resource will be used.

      .. _web^request.on^error^occurred.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-request-on-error-occurred-details-url
         :refname: url
         :type: (string)

      .. _web^request.on^error^occurred.details.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: web-request-on-error-occurred-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0]

         The cookie store ID of the contextual identity.

      .. _web^request.on^error^occurred.details.document^id:

      .. api-member::
         :name: [``documentId``]
         :refid: web-request-on-error-occurred-details-document-id
         :refname: documentId
         :type: (string, optional)

         The UUID of the document making the request. This value is not present if the request is a navigation of a frame.

      .. _web^request.on^error^occurred.details.document^url:

      .. api-member::
         :name: [``documentUrl``]
         :refid: web-request-on-error-occurred-details-document-url
         :refname: documentUrl
         :type: (string, optional)

         URL of the page into which the requested resource will be loaded.

      .. _web^request.on^error^occurred.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: web-request-on-error-occurred-details-incognito
         :refname: incognito
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68.0]

         True for private browsing requests.

      .. _web^request.on^error^occurred.details.ip:

      .. api-member::
         :name: [``ip``]
         :refid: web-request-on-error-occurred-details-ip
         :refname: ip
         :type: (string, optional)

         The server IP address that the request was actually sent to. Note that it may be a literal IPv6 address.

      .. _web^request.on^error^occurred.details.origin^url:

      .. api-member::
         :name: [``originUrl``]
         :refid: web-request-on-error-occurred-details-origin-url
         :refname: originUrl
         :type: (string, optional)

         URL of the resource that triggered this request.

      .. _web^request.on^error^occurred.details.parent^document^id:

      .. api-member::
         :name: [``parentDocumentId``]
         :refid: web-request-on-error-occurred-details-parent-document-id
         :refname: parentDocumentId
         :type: (string, optional)

         The UUID of the parent document owning this frame. This is not set if there is no parent.

      .. _web^request.on^error^occurred.details.url^classification:

      .. api-member::
         :name: [``urlClassification``]
         :refid: web-request-on-error-occurred-details-url-classification
         :refname: urlClassification
         :type: (:ref:`web^request.^url^classification`, optional)
         :annotation: -- [Added in TB 78.0]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _web^request.on^headers^received:

onHeadersReceived
-----------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when HTTP response headers of a request have been received.

.. note::

   Modification of the 'Content-Type' header is supported from version 51.

.. note::

   Asynchronous event listeners are supported from version 52.

.. api-header::
   :label: Parameters for onHeadersReceived.addListener(listener, filter, extraInfoSpec)

   .. _web^request.on^headers^received.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-request-on-headers-received-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^request.on^headers^received.filter:

   .. api-member::
      :name: ``filter``
      :refid: web-request-on-headers-received-filter
      :refname: filter
      :type: (:ref:`web^request.^request^filter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. _web^request.on^headers^received.extra^info^spec:

   .. api-member::
      :name: [``extraInfoSpec``]
      :refid: web-request-on-headers-received-extra-info-spec
      :refname: extraInfoSpec
      :type: (array of :ref:`web^request.^on^headers^received^options`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^request.on^headers^received.details:

   .. api-member::
      :name: ``details``
      :refid: web-request-on-headers-received-details
      :refname: details
      :type: (object)

      .. _web^request.on^headers^received.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-request-on-headers-received-details-frame-id
         :refname: frameId
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. _web^request.on^headers^received.details.method:

      .. api-member::
         :name: ``method``
         :refid: web-request-on-headers-received-details-method
         :refname: method
         :type: (string)

         Standard HTTP method.

      .. _web^request.on^headers^received.details.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: web-request-on-headers-received-details-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. _web^request.on^headers^received.details.request^id:

      .. api-member::
         :name: ``requestId``
         :refid: web-request-on-headers-received-details-request-id
         :refname: requestId
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. _web^request.on^headers^received.details.status^code:

      .. api-member::
         :name: ``statusCode``
         :refid: web-request-on-headers-received-details-status-code
         :refname: statusCode
         :type: (integer)

         Standard HTTP status code returned by the server.

      .. _web^request.on^headers^received.details.status^line:

      .. api-member::
         :name: ``statusLine``
         :refid: web-request-on-headers-received-details-status-line
         :refname: statusLine
         :type: (string)

         HTTP status line of the response or the 'HTTP/0.9 200 OK' string for HTTP/0.9 responses (i.e., responses that lack a status line).

      .. _web^request.on^headers^received.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-request-on-headers-received-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. _web^request.on^headers^received.details.third^party:

      .. api-member::
         :name: ``thirdParty``
         :refid: web-request-on-headers-received-details-third-party
         :refname: thirdParty
         :type: (boolean)
         :annotation: -- [Added in TB 78.0]

         Indicates if this request and its content window hierarchy is third party.

      .. _web^request.on^headers^received.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-request-on-headers-received-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. _web^request.on^headers^received.details.type:

      .. api-member::
         :name: ``type``
         :refid: web-request-on-headers-received-details-type
         :refname: type
         :type: (:ref:`web^request.^resource^type`)

         How the requested resource will be used.

      .. _web^request.on^headers^received.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-request-on-headers-received-details-url
         :refname: url
         :type: (string)

      .. _web^request.on^headers^received.details.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: web-request-on-headers-received-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0]

         The cookie store ID of the contextual identity.

      .. _web^request.on^headers^received.details.document^id:

      .. api-member::
         :name: [``documentId``]
         :refid: web-request-on-headers-received-details-document-id
         :refname: documentId
         :type: (string, optional)

         The UUID of the document making the request.

      .. _web^request.on^headers^received.details.document^url:

      .. api-member::
         :name: [``documentUrl``]
         :refid: web-request-on-headers-received-details-document-url
         :refname: documentUrl
         :type: (string, optional)

         URL of the page into which the requested resource will be loaded.

      .. _web^request.on^headers^received.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: web-request-on-headers-received-details-incognito
         :refname: incognito
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68.0]

         True for private browsing requests.

      .. _web^request.on^headers^received.details.origin^url:

      .. api-member::
         :name: [``originUrl``]
         :refid: web-request-on-headers-received-details-origin-url
         :refname: originUrl
         :type: (string, optional)

         URL of the resource that triggered this request.

      .. _web^request.on^headers^received.details.parent^document^id:

      .. api-member::
         :name: [``parentDocumentId``]
         :refid: web-request-on-headers-received-details-parent-document-id
         :refname: parentDocumentId
         :type: (string, optional)

         The UUID of the parent document owning this frame. This is not set if there is no parent.

      .. _web^request.on^headers^received.details.response^headers:

      .. api-member::
         :name: [``responseHeaders``]
         :refid: web-request-on-headers-received-details-response-headers
         :refname: responseHeaders
         :type: (:ref:`web^request.^http^headers`, optional)

         The HTTP response headers that have been received with this response.

      .. _web^request.on^headers^received.details.url^classification:

      .. api-member::
         :name: [``urlClassification``]
         :refid: web-request-on-headers-received-details-url-classification
         :refname: urlClassification
         :type: (:ref:`web^request.^url^classification`, optional)
         :annotation: -- [Added in TB 78.0]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Expected return value of the listener function

   .. _web^request.on^headers^received.returns:

   .. api-member::
      :refid: web-request-on-headers-received-returns
      :type: :ref:`web^request.^blocking^response`

      If "blocking" is specified in the "extraInfoSpec" parameter, the event listener should return an object of this type.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _web^request.on^response^started:

onResponseStarted
-----------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when the first byte of the response body is received. For HTTP requests, this means that the status line and response headers are available.

.. api-header::
   :label: Parameters for onResponseStarted.addListener(listener, filter, extraInfoSpec)

   .. _web^request.on^response^started.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-request-on-response-started-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^request.on^response^started.filter:

   .. api-member::
      :name: ``filter``
      :refid: web-request-on-response-started-filter
      :refname: filter
      :type: (:ref:`web^request.^request^filter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. _web^request.on^response^started.extra^info^spec:

   .. api-member::
      :name: [``extraInfoSpec``]
      :refid: web-request-on-response-started-extra-info-spec
      :refname: extraInfoSpec
      :type: (array of :ref:`web^request.^on^response^started^options`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^request.on^response^started.details:

   .. api-member::
      :name: ``details``
      :refid: web-request-on-response-started-details
      :refname: details
      :type: (object)

      .. _web^request.on^response^started.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-request-on-response-started-details-frame-id
         :refname: frameId
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. _web^request.on^response^started.details.from^cache:

      .. api-member::
         :name: ``fromCache``
         :refid: web-request-on-response-started-details-from-cache
         :refname: fromCache
         :type: (boolean)

         Indicates if this response was fetched from disk cache.

      .. _web^request.on^response^started.details.method:

      .. api-member::
         :name: ``method``
         :refid: web-request-on-response-started-details-method
         :refname: method
         :type: (string)

         Standard HTTP method.

      .. _web^request.on^response^started.details.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: web-request-on-response-started-details-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. _web^request.on^response^started.details.request^id:

      .. api-member::
         :name: ``requestId``
         :refid: web-request-on-response-started-details-request-id
         :refname: requestId
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. _web^request.on^response^started.details.status^code:

      .. api-member::
         :name: ``statusCode``
         :refid: web-request-on-response-started-details-status-code
         :refname: statusCode
         :type: (integer)

         Standard HTTP status code returned by the server.

      .. _web^request.on^response^started.details.status^line:

      .. api-member::
         :name: ``statusLine``
         :refid: web-request-on-response-started-details-status-line
         :refname: statusLine
         :type: (string)

         HTTP status line of the response or the 'HTTP/0.9 200 OK' string for HTTP/0.9 responses (i.e., responses that lack a status line) or an empty string if there are no headers.

      .. _web^request.on^response^started.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-request-on-response-started-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. _web^request.on^response^started.details.third^party:

      .. api-member::
         :name: ``thirdParty``
         :refid: web-request-on-response-started-details-third-party
         :refname: thirdParty
         :type: (boolean)
         :annotation: -- [Added in TB 78.0]

         Indicates if this request and its content window hierarchy is third party.

      .. _web^request.on^response^started.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-request-on-response-started-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. _web^request.on^response^started.details.type:

      .. api-member::
         :name: ``type``
         :refid: web-request-on-response-started-details-type
         :refname: type
         :type: (:ref:`web^request.^resource^type`)

         How the requested resource will be used.

      .. _web^request.on^response^started.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-request-on-response-started-details-url
         :refname: url
         :type: (string)

      .. _web^request.on^response^started.details.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: web-request-on-response-started-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0]

         The cookie store ID of the contextual identity.

      .. _web^request.on^response^started.details.document^id:

      .. api-member::
         :name: [``documentId``]
         :refid: web-request-on-response-started-details-document-id
         :refname: documentId
         :type: (string, optional)

         The UUID of the document making the request.

      .. _web^request.on^response^started.details.document^url:

      .. api-member::
         :name: [``documentUrl``]
         :refid: web-request-on-response-started-details-document-url
         :refname: documentUrl
         :type: (string, optional)

         URL of the page into which the requested resource will be loaded.

      .. _web^request.on^response^started.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: web-request-on-response-started-details-incognito
         :refname: incognito
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68.0]

         True for private browsing requests.

      .. _web^request.on^response^started.details.ip:

      .. api-member::
         :name: [``ip``]
         :refid: web-request-on-response-started-details-ip
         :refname: ip
         :type: (string, optional)

         The server IP address that the request was actually sent to. Note that it may be a literal IPv6 address.

      .. _web^request.on^response^started.details.origin^url:

      .. api-member::
         :name: [``originUrl``]
         :refid: web-request-on-response-started-details-origin-url
         :refname: originUrl
         :type: (string, optional)

         URL of the resource that triggered this request.

      .. _web^request.on^response^started.details.parent^document^id:

      .. api-member::
         :name: [``parentDocumentId``]
         :refid: web-request-on-response-started-details-parent-document-id
         :refname: parentDocumentId
         :type: (string, optional)

         The UUID of the parent document owning this frame. This is not set if there is no parent.

      .. _web^request.on^response^started.details.response^headers:

      .. api-member::
         :name: [``responseHeaders``]
         :refid: web-request-on-response-started-details-response-headers
         :refname: responseHeaders
         :type: (:ref:`web^request.^http^headers`, optional)

         The HTTP response headers that were received along with this response.

      .. _web^request.on^response^started.details.url^classification:

      .. api-member::
         :name: [``urlClassification``]
         :refid: web-request-on-response-started-details-url-classification
         :refname: urlClassification
         :type: (:ref:`web^request.^url^classification`, optional)
         :annotation: -- [Added in TB 78.0]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _web^request.on^send^headers:

onSendHeaders
-------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired just before a request is going to be sent to the server (modifications of previous onBeforeSendHeaders callbacks are visible by the time onSendHeaders is fired).

.. api-header::
   :label: Parameters for onSendHeaders.addListener(listener, filter, extraInfoSpec)

   .. _web^request.on^send^headers.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-request-on-send-headers-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^request.on^send^headers.filter:

   .. api-member::
      :name: ``filter``
      :refid: web-request-on-send-headers-filter
      :refname: filter
      :type: (:ref:`web^request.^request^filter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. _web^request.on^send^headers.extra^info^spec:

   .. api-member::
      :name: [``extraInfoSpec``]
      :refid: web-request-on-send-headers-extra-info-spec
      :refname: extraInfoSpec
      :type: (array of :ref:`web^request.^on^send^headers^options`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^request.on^send^headers.details:

   .. api-member::
      :name: ``details``
      :refid: web-request-on-send-headers-details
      :refname: details
      :type: (object)

      .. _web^request.on^send^headers.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-request-on-send-headers-details-frame-id
         :refname: frameId
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. _web^request.on^send^headers.details.method:

      .. api-member::
         :name: ``method``
         :refid: web-request-on-send-headers-details-method
         :refname: method
         :type: (string)

         Standard HTTP method.

      .. _web^request.on^send^headers.details.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: web-request-on-send-headers-details-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. _web^request.on^send^headers.details.request^id:

      .. api-member::
         :name: ``requestId``
         :refid: web-request-on-send-headers-details-request-id
         :refname: requestId
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. _web^request.on^send^headers.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-request-on-send-headers-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. _web^request.on^send^headers.details.third^party:

      .. api-member::
         :name: ``thirdParty``
         :refid: web-request-on-send-headers-details-third-party
         :refname: thirdParty
         :type: (boolean)
         :annotation: -- [Added in TB 78.0]

         Indicates if this request and its content window hierarchy is third party.

      .. _web^request.on^send^headers.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-request-on-send-headers-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. _web^request.on^send^headers.details.type:

      .. api-member::
         :name: ``type``
         :refid: web-request-on-send-headers-details-type
         :refname: type
         :type: (:ref:`web^request.^resource^type`)

         How the requested resource will be used.

      .. _web^request.on^send^headers.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-request-on-send-headers-details-url
         :refname: url
         :type: (string)

      .. _web^request.on^send^headers.details.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: web-request-on-send-headers-details-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0]

         The cookie store ID of the contextual identity.

      .. _web^request.on^send^headers.details.document^id:

      .. api-member::
         :name: [``documentId``]
         :refid: web-request-on-send-headers-details-document-id
         :refname: documentId
         :type: (string, optional)

         The UUID of the document making the request.

      .. _web^request.on^send^headers.details.document^url:

      .. api-member::
         :name: [``documentUrl``]
         :refid: web-request-on-send-headers-details-document-url
         :refname: documentUrl
         :type: (string, optional)

         URL of the page into which the requested resource will be loaded.

      .. _web^request.on^send^headers.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: web-request-on-send-headers-details-incognito
         :refname: incognito
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68.0]

         True for private browsing requests.

      .. _web^request.on^send^headers.details.origin^url:

      .. api-member::
         :name: [``originUrl``]
         :refid: web-request-on-send-headers-details-origin-url
         :refname: originUrl
         :type: (string, optional)

         URL of the resource that triggered this request.

      .. _web^request.on^send^headers.details.parent^document^id:

      .. api-member::
         :name: [``parentDocumentId``]
         :refid: web-request-on-send-headers-details-parent-document-id
         :refname: parentDocumentId
         :type: (string, optional)

         The UUID of the parent document owning this frame. This is not set if there is no parent.

      .. _web^request.on^send^headers.details.request^headers:

      .. api-member::
         :name: [``requestHeaders``]
         :refid: web-request-on-send-headers-details-request-headers
         :refname: requestHeaders
         :type: (:ref:`web^request.^http^headers`, optional)

         The HTTP request headers that have been sent out with this request.

      .. _web^request.on^send^headers.details.url^classification:

      .. api-member::
         :name: [``urlClassification``]
         :refid: web-request-on-send-headers-details-url-classification
         :refname: urlClassification
         :type: (:ref:`web^request.^url^classification`, optional)
         :annotation: -- [Added in TB 78.0]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. rst-class:: api-main-section

Types
=====

.. _web^request.^blocking^response:

BlockingResponse
----------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Returns value for event handlers that have the 'blocking' extraInfoSpec applied. Allows the event handler to modify network requests.

.. api-header::
   :label: object

   .. _web^request.^blocking^response.auth^credentials:

   .. api-member::
      :name: [``authCredentials``]
      :refid: web-request-blocking-response-auth-credentials
      :refname: authCredentials
      :type: (object, optional)

      Only used as a response to the onAuthRequired event. If set, the request is made using the supplied credentials.

      .. _web^request.^blocking^response.auth^credentials.password:

      .. api-member::
         :name: ``password``
         :refid: web-request-blocking-response-auth-credentials-password
         :refname: password
         :type: (string)

      .. _web^request.^blocking^response.auth^credentials.username:

      .. api-member::
         :name: ``username``
         :refid: web-request-blocking-response-auth-credentials-username
         :refname: username
         :type: (string)

   .. _web^request.^blocking^response.cancel:

   .. api-member::
      :name: [``cancel``]
      :refid: web-request-blocking-response-cancel
      :refname: cancel
      :type: (boolean, optional)

      If true, the request is cancelled. Used in onBeforeRequest, this prevents the request from being sent.

   .. _web^request.^blocking^response.redirect^url:

   .. api-member::
      :name: [``redirectUrl``]
      :refid: web-request-blocking-response-redirect-url
      :refname: redirectUrl
      :type: (string, optional)

      Only used as a response to the onBeforeRequest and onHeadersReceived events. If set, the original request is prevented from being sent/completed and is instead redirected to the given URL. Redirections to non-HTTP schemes such as data: are allowed. Redirects initiated by a redirect action use the original request method for the redirect, with one exception: If the redirect is initiated at the onHeadersReceived stage, then the redirect will be issued using the GET method.

   .. _web^request.^blocking^response.request^headers:

   .. api-member::
      :name: [``requestHeaders``]
      :refid: web-request-blocking-response-request-headers
      :refname: requestHeaders
      :type: (:ref:`web^request.^http^headers`, optional)

      Only used as a response to the onBeforeSendHeaders event. If set, the request is made with these request headers instead.

   .. _web^request.^blocking^response.response^headers:

   .. api-member::
      :name: [``responseHeaders``]
      :refid: web-request-blocking-response-response-headers
      :refname: responseHeaders
      :type: (:ref:`web^request.^http^headers`, optional)

      Only used as a response to the onHeadersReceived event. If set, the server is assumed to have responded with these response headers instead. Only return :code:`responseHeaders` if you really want to modify the headers in order to limit the number of conflicts (only one extension may modify :code:`responseHeaders` for each request).

   .. _web^request.^blocking^response.upgrade^to^secure:

   .. api-member::
      :name: [``upgradeToSecure``]
      :refid: web-request-blocking-response-upgrade-to-secure
      :refname: upgradeToSecure
      :type: (boolean, optional)

      Only used as a response to the onBeforeRequest event. If set, the original request is prevented from being sent/completed and is instead upgraded to a secure request.  If any extension returns :code:`redirectUrl` during onBeforeRequest, :code:`upgradeToSecure` will have no affect.

.. _web^request.^certificate^info:

CertificateInfo
---------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Contains the certificate properties of the request if it is a secure request.

.. api-header::
   :label: object

   .. _web^request.^certificate^info.fingerprint:

   .. api-member::
      :name: ``fingerprint``
      :refid: web-request-certificate-info-fingerprint
      :refname: fingerprint
      :type: (object)

      .. _web^request.^certificate^info.fingerprint.sha1:

      .. api-member::
         :name: ``sha1``
         :refid: web-request-certificate-info-fingerprint-sha1
         :refname: sha1
         :type: (string)

      .. _web^request.^certificate^info.fingerprint.sha256:

      .. api-member::
         :name: ``sha256``
         :refid: web-request-certificate-info-fingerprint-sha256
         :refname: sha256
         :type: (string)

   .. _web^request.^certificate^info.is^built^in^root:

   .. api-member::
      :name: ``isBuiltInRoot``
      :refid: web-request-certificate-info-is-built-in-root
      :refname: isBuiltInRoot
      :type: (boolean)

   .. _web^request.^certificate^info.issuer:

   .. api-member::
      :name: ``issuer``
      :refid: web-request-certificate-info-issuer
      :refname: issuer
      :type: (string)

   .. _web^request.^certificate^info.serial^number:

   .. api-member::
      :name: ``serialNumber``
      :refid: web-request-certificate-info-serial-number
      :refname: serialNumber
      :type: (string)

   .. _web^request.^certificate^info.subject:

   .. api-member::
      :name: ``subject``
      :refid: web-request-certificate-info-subject
      :refname: subject
      :type: (string)

   .. _web^request.^certificate^info.subject^public^key^info^digest:

   .. api-member::
      :name: ``subjectPublicKeyInfoDigest``
      :refid: web-request-certificate-info-subject-public-key-info-digest
      :refname: subjectPublicKeyInfoDigest
      :type: (object)

      .. _web^request.^certificate^info.subject^public^key^info^digest.sha256:

      .. api-member::
         :name: ``sha256``
         :refid: web-request-certificate-info-subject-public-key-info-digest-sha256
         :refname: sha256
         :type: (string)

   .. _web^request.^certificate^info.validity:

   .. api-member::
      :name: ``validity``
      :refid: web-request-certificate-info-validity
      :refname: validity
      :type: (object)

      Contains start and end timestamps.

      .. _web^request.^certificate^info.validity.end:

      .. api-member::
         :name: ``end``
         :refid: web-request-certificate-info-validity-end
         :refname: end
         :type: (integer)

      .. _web^request.^certificate^info.validity.start:

      .. api-member::
         :name: ``start``
         :refid: web-request-certificate-info-validity-start
         :refname: start
         :type: (integer)

   .. _web^request.^certificate^info.raw^d^e^r:

   .. api-member::
      :name: [``rawDER``]
      :refid: web-request-certificate-info-raw-d-e-r
      :refname: rawDER
      :type: (array of integer, optional)

.. _web^request.^certificate^transparency^status:

CertificateTransparencyStatus
-----------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^certificate^transparency^status.not_applicable:

         .. api-member::
            :name: :value:`not_applicable`
            :refid: web-request-certificate-transparency-status-not-applicable
            :refname: not_applicable

         .. _web^request.^certificate^transparency^status.policy_compliant:

         .. api-member::
            :name: :value:`policy_compliant`
            :refid: web-request-certificate-transparency-status-policy-compliant
            :refname: policy_compliant

         .. _web^request.^certificate^transparency^status.policy_not_diverse_scts:

         .. api-member::
            :name: :value:`policy_not_diverse_scts`
            :refid: web-request-certificate-transparency-status-policy-not-diverse-scts
            :refname: policy_not_diverse_scts

         .. _web^request.^certificate^transparency^status.policy_not_enough_scts:

         .. api-member::
            :name: :value:`policy_not_enough_scts`
            :refid: web-request-certificate-transparency-status-policy-not-enough-scts
            :refname: policy_not_enough_scts

.. _web^request.^http^headers:

HttpHeaders
-----------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

An array of HTTP headers. Each header is represented as a dictionary containing the keys :code:`name` and either :code:`value` or :code:`binaryValue`.

.. api-header::
   :label: array of object

.. _web^request.^on^auth^required^options:

OnAuthRequiredOptions
---------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^on^auth^required^options.async^blocking:

         .. api-member::
            :name: :value:`asyncBlocking`
            :refid: web-request-on-auth-required-options-async-blocking
            :refname: asyncBlocking

         .. _web^request.^on^auth^required^options.blocking:

         .. api-member::
            :name: :value:`blocking`
            :refid: web-request-on-auth-required-options-blocking
            :refname: blocking

         .. _web^request.^on^auth^required^options.response^headers:

         .. api-member::
            :name: :value:`responseHeaders`
            :refid: web-request-on-auth-required-options-response-headers
            :refname: responseHeaders

.. _web^request.^on^before^redirect^options:

OnBeforeRedirectOptions
-----------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^on^before^redirect^options.response^headers:

         .. api-member::
            :name: :value:`responseHeaders`
            :refid: web-request-on-before-redirect-options-response-headers
            :refname: responseHeaders

.. _web^request.^on^before^request^options:

OnBeforeRequestOptions
----------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^on^before^request^options.blocking:

         .. api-member::
            :name: :value:`blocking`
            :refid: web-request-on-before-request-options-blocking
            :refname: blocking

         .. _web^request.^on^before^request^options.request^body:

         .. api-member::
            :name: :value:`requestBody`
            :refid: web-request-on-before-request-options-request-body
            :refname: requestBody

.. _web^request.^on^before^send^headers^options:

OnBeforeSendHeadersOptions
--------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^on^before^send^headers^options.blocking:

         .. api-member::
            :name: :value:`blocking`
            :refid: web-request-on-before-send-headers-options-blocking
            :refname: blocking

         .. _web^request.^on^before^send^headers^options.request^headers:

         .. api-member::
            :name: :value:`requestHeaders`
            :refid: web-request-on-before-send-headers-options-request-headers
            :refname: requestHeaders

.. _web^request.^on^completed^options:

OnCompletedOptions
------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^on^completed^options.response^headers:

         .. api-member::
            :name: :value:`responseHeaders`
            :refid: web-request-on-completed-options-response-headers
            :refname: responseHeaders

.. _web^request.^on^headers^received^options:

OnHeadersReceivedOptions
------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^on^headers^received^options.blocking:

         .. api-member::
            :name: :value:`blocking`
            :refid: web-request-on-headers-received-options-blocking
            :refname: blocking

         .. _web^request.^on^headers^received^options.response^headers:

         .. api-member::
            :name: :value:`responseHeaders`
            :refid: web-request-on-headers-received-options-response-headers
            :refname: responseHeaders

.. _web^request.^on^response^started^options:

OnResponseStartedOptions
------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^on^response^started^options.response^headers:

         .. api-member::
            :name: :value:`responseHeaders`
            :refid: web-request-on-response-started-options-response-headers
            :refname: responseHeaders

.. _web^request.^on^send^headers^options:

OnSendHeadersOptions
--------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^on^send^headers^options.request^headers:

         .. api-member::
            :name: :value:`requestHeaders`
            :refid: web-request-on-send-headers-options-request-headers
            :refname: requestHeaders

.. _web^request.^request^filter:

RequestFilter
-------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

An object describing filters to apply to webRequest events.

.. note::

   From Thunderbird 78 onwards, if a filter contains unrecognized values in its :code:`types` property, then these values are ignored and :code:`addListener()` proceeds.

.. note::

   Before Thunderbird 78, if a filter contains unrecognized values in its :code:`types` property, :code:`addListener()` throws an exception.

.. api-header::
   :label: object

   .. _web^request.^request^filter.urls:

   .. api-member::
      :name: ``urls``
      :refid: web-request-request-filter-urls
      :refname: urls
      :type: (array of string)

      A list of URLs or URL patterns. Requests that cannot match any of the URLs will be filtered out.

      .. note::

         Before Thunderbird 56, moz-extension:// URLs were not allowed.

   .. _web^request.^request^filter.incognito:

   .. api-member::
      :name: [``incognito``]
      :refid: web-request-request-filter-incognito
      :refname: incognito
      :type: (boolean, optional)

      If provided, requests that do not match the incognito state will be filtered out.

   .. _web^request.^request^filter.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: web-request-request-filter-tab-id
      :refname: tabId
      :type: (integer, optional)

   .. _web^request.^request^filter.types:

   .. api-member::
      :name: [``types``]
      :refid: web-request-request-filter-types
      :refname: types
      :type: (array of :ref:`web^request.^resource^type`, optional)

      A list of request types. Requests that cannot match any of the types will be filtered out.

   .. _web^request.^request^filter.window^id:

   .. api-member::
      :name: [``windowId``]
      :refid: web-request-request-filter-window-id
      :refname: windowId
      :type: (integer, optional)

.. _web^request.^resource^type:

ResourceType
------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^resource^type.beacon:

         .. api-member::
            :name: :value:`beacon`
            :refid: web-request-resource-type-beacon
            :refname: beacon

         .. _web^request.^resource^type.csp_report:

         .. api-member::
            :name: :value:`csp_report`
            :refid: web-request-resource-type-csp-report
            :refname: csp_report

         .. _web^request.^resource^type.font:

         .. api-member::
            :name: :value:`font`
            :refid: web-request-resource-type-font
            :refname: font

         .. _web^request.^resource^type.image:

         .. api-member::
            :name: :value:`image`
            :refid: web-request-resource-type-image
            :refname: image

         .. _web^request.^resource^type.imageset:

         .. api-member::
            :name: :value:`imageset`
            :refid: web-request-resource-type-imageset
            :refname: imageset

         .. _web^request.^resource^type.json:

         .. api-member::
            :name: :value:`json`
            :refid: web-request-resource-type-json
            :refname: json
            :annotation: -- [Added in TB 140.0]

            .. note::

               The "json" property is supported from Thunderbird 135, but requests of this type are only available from Thunderbird 138.

         .. _web^request.^resource^type.main_frame:

         .. api-member::
            :name: :value:`main_frame`
            :refid: web-request-resource-type-main-frame
            :refname: main_frame

         .. _web^request.^resource^type.media:

         .. api-member::
            :name: :value:`media`
            :refid: web-request-resource-type-media
            :refname: media

         .. _web^request.^resource^type.object:

         .. api-member::
            :name: :value:`object`
            :refid: web-request-resource-type-object
            :refname: object

         .. _web^request.^resource^type.other:

         .. api-member::
            :name: :value:`other`
            :refid: web-request-resource-type-other
            :refname: other

         .. _web^request.^resource^type.ping:

         .. api-member::
            :name: :value:`ping`
            :refid: web-request-resource-type-ping
            :refname: ping

         .. _web^request.^resource^type.script:

         .. api-member::
            :name: :value:`script`
            :refid: web-request-resource-type-script
            :refname: script

         .. _web^request.^resource^type.speculative:

         .. api-member::
            :name: :value:`speculative`
            :refid: web-request-resource-type-speculative
            :refname: speculative
            :annotation: -- [Added in TB 68.0]

         .. _web^request.^resource^type.stylesheet:

         .. api-member::
            :name: :value:`stylesheet`
            :refid: web-request-resource-type-stylesheet
            :refname: stylesheet

         .. _web^request.^resource^type.sub_frame:

         .. api-member::
            :name: :value:`sub_frame`
            :refid: web-request-resource-type-sub-frame
            :refname: sub_frame

         .. _web^request.^resource^type.web_manifest:

         .. api-member::
            :name: :value:`web_manifest`
            :refid: web-request-resource-type-web-manifest
            :refname: web_manifest

         .. _web^request.^resource^type.websocket:

         .. api-member::
            :name: :value:`websocket`
            :refid: web-request-resource-type-websocket
            :refname: websocket

         .. _web^request.^resource^type.xml_dtd:

         .. api-member::
            :name: :value:`xml_dtd`
            :refid: web-request-resource-type-xml-dtd
            :refname: xml_dtd

         .. _web^request.^resource^type.xmlhttprequest:

         .. api-member::
            :name: :value:`xmlhttprequest`
            :refid: web-request-resource-type-xmlhttprequest
            :refname: xmlhttprequest

         .. _web^request.^resource^type.xslt:

         .. api-member::
            :name: :value:`xslt`
            :refid: web-request-resource-type-xslt
            :refname: xslt

.. _web^request.^security^info:

SecurityInfo
------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Contains the security properties of the request (ie. SSL/TLS information).

.. api-header::
   :label: object

   .. _web^request.^security^info.certificates:

   .. api-member::
      :name: ``certificates``
      :refid: web-request-security-info-certificates
      :refname: certificates
      :type: (array of :ref:`web^request.^certificate^info`)

      Certificate data if state is "secure".  Will only contain one entry unless :code:`certificateChain` is passed as an option.

   .. _web^request.^security^info.state:

   .. api-member::
      :name: ``state``
      :refid: web-request-security-info-state
      :refname: state
      :type: (`string`)

      Supported values:

      .. _web^request.^security^info.state.broken:

      .. api-member::
         :name: :value:`broken`
         :refid: web-request-security-info-state-broken
         :refname: broken

      .. _web^request.^security^info.state.insecure:

      .. api-member::
         :name: :value:`insecure`
         :refid: web-request-security-info-state-insecure
         :refname: insecure

      .. _web^request.^security^info.state.secure:

      .. api-member::
         :name: :value:`secure`
         :refid: web-request-security-info-state-secure
         :refname: secure

      .. _web^request.^security^info.state.weak:

      .. api-member::
         :name: :value:`weak`
         :refid: web-request-security-info-state-weak
         :refname: weak

   .. _web^request.^security^info.certificate^transparency^status:

   .. api-member::
      :name: [``certificateTransparencyStatus``]
      :refid: web-request-security-info-certificate-transparency-status
      :refname: certificateTransparencyStatus
      :type: (:ref:`web^request.^certificate^transparency^status`, optional)

      Certificate transparency compliance per RFC 6962.  See :code:`https://www.certificate-transparency.org/what-is-ct` for more information.

   .. _web^request.^security^info.cipher^suite:

   .. api-member::
      :name: [``cipherSuite``]
      :refid: web-request-security-info-cipher-suite
      :refname: cipherSuite
      :type: (string, optional)

      The cipher suite used in this request if state is "secure".

   .. _web^request.^security^info.error^message:

   .. api-member::
      :name: [``errorMessage``]
      :refid: web-request-security-info-error-message
      :refname: errorMessage
      :type: (string, optional)

      Error message if state is "broken"

   .. _web^request.^security^info.hpkp:

   .. api-member::
      :name: [``hpkp``]
      :refid: web-request-security-info-hpkp
      :refname: hpkp
      :type: (string, optional)

      True if host uses Public Key Pinning and state is "secure".

   .. _web^request.^security^info.hsts:

   .. api-member::
      :name: [``hsts``]
      :refid: web-request-security-info-hsts
      :refname: hsts
      :type: (boolean, optional)

      True if host uses Strict Transport Security and state is "secure".

   .. _web^request.^security^info.is^domain^mismatch:

   .. api-member::
      :name: [``isDomainMismatch``]
      :refid: web-request-security-info-is-domain-mismatch
      :refname: isDomainMismatch
      :type: (boolean, optional) **Deprecated.**

      The domain name does not match the certificate domain.

   .. _web^request.^security^info.is^extended^validation:

   .. api-member::
      :name: [``isExtendedValidation``]
      :refid: web-request-security-info-is-extended-validation
      :refname: isExtendedValidation
      :type: (boolean, optional)

   .. _web^request.^security^info.is^not^valid^at^this^time:

   .. api-member::
      :name: [``isNotValidAtThisTime``]
      :refid: web-request-security-info-is-not-valid-at-this-time
      :refname: isNotValidAtThisTime
      :type: (boolean, optional) **Deprecated.**

      The certificate is either expired or is not yet valid.  See :code:`CertificateInfo.validity` for start and end dates.

   .. _web^request.^security^info.is^untrusted:

   .. api-member::
      :name: [``isUntrusted``]
      :refid: web-request-security-info-is-untrusted
      :refname: isUntrusted
      :type: (boolean, optional) **Deprecated.**

   .. _web^request.^security^info.kea^group^name:

   .. api-member::
      :name: [``keaGroupName``]
      :refid: web-request-security-info-kea-group-name
      :refname: keaGroupName
      :type: (string, optional)

      The key exchange algorithm used in this request if state is "secure".

   .. _web^request.^security^info.overridable^error^category:

   .. api-member::
      :name: [``overridableErrorCategory``]
      :refid: web-request-security-info-overridable-error-category
      :refname: overridableErrorCategory
      :type: (`string`, optional)

      The type of certificate error that was overridden for this connection, if any.

      Supported values:

      .. _web^request.^security^info.overridable^error^category.domain_mismatch:

      .. api-member::
         :name: :value:`domain_mismatch`
         :refid: web-request-security-info-overridable-error-category-domain-mismatch
         :refname: domain_mismatch

      .. _web^request.^security^info.overridable^error^category.expired_or_not_yet_valid:

      .. api-member::
         :name: :value:`expired_or_not_yet_valid`
         :refid: web-request-security-info-overridable-error-category-expired-or-not-yet-valid
         :refname: expired_or_not_yet_valid

      .. _web^request.^security^info.overridable^error^category.trust_error:

      .. api-member::
         :name: :value:`trust_error`
         :refid: web-request-security-info-overridable-error-category-trust-error
         :refname: trust_error

   .. _web^request.^security^info.protocol^version:

   .. api-member::
      :name: [``protocolVersion``]
      :refid: web-request-security-info-protocol-version
      :refname: protocolVersion
      :type: (`string`, optional)

      Protocol version if state is "secure"

      Supported values:

      .. _web^request.^security^info.protocol^version.^t^l^sv1:

      .. api-member::
         :name: :value:`TLSv1`
         :refid: web-request-security-info-protocol-version-t-l-sv1
         :refname: TLSv1

      .. _web^request.^security^info.protocol^version.^t^l^sv1.1:

      .. api-member::
         :name: :value:`TLSv1.1`
         :refid: web-request-security-info-protocol-version-t-l-sv1-1
         :refname: TLSv1.1

      .. _web^request.^security^info.protocol^version.^t^l^sv1.2:

      .. api-member::
         :name: :value:`TLSv1.2`
         :refid: web-request-security-info-protocol-version-t-l-sv1-2
         :refname: TLSv1.2

      .. _web^request.^security^info.protocol^version.^t^l^sv1.3:

      .. api-member::
         :name: :value:`TLSv1.3`
         :refid: web-request-security-info-protocol-version-t-l-sv1-3
         :refname: TLSv1.3

      .. _web^request.^security^info.protocol^version.unknown:

      .. api-member::
         :name: :value:`unknown`
         :refid: web-request-security-info-protocol-version-unknown
         :refname: unknown

   .. _web^request.^security^info.secret^key^length:

   .. api-member::
      :name: [``secretKeyLength``]
      :refid: web-request-security-info-secret-key-length
      :refname: secretKeyLength
      :type: (number, optional)
      :annotation: -- [Added in TB 115.0]

      The length (in bits) of the secret key.

   .. _web^request.^security^info.signature^scheme^name:

   .. api-member::
      :name: [``signatureSchemeName``]
      :refid: web-request-security-info-signature-scheme-name
      :refname: signatureSchemeName
      :type: (string, optional)

      The signature scheme used in this request if state is "secure".

   .. _web^request.^security^info.used^delegated^credentials:

   .. api-member::
      :name: [``usedDelegatedCredentials``]
      :refid: web-request-security-info-used-delegated-credentials
      :refname: usedDelegatedCredentials
      :type: (boolean, optional)
      :annotation: -- [Added in TB 115.0]

      True if the TLS connection used Delegated Credentials.

   .. _web^request.^security^info.used^ech:

   .. api-member::
      :name: [``usedEch``]
      :refid: web-request-security-info-used-ech
      :refname: usedEch
      :type: (boolean, optional)
      :annotation: -- [Added in TB 115.0]

      True if the TLS connection used Encrypted Client Hello.

   .. _web^request.^security^info.used^ocsp:

   .. api-member::
      :name: [``usedOcsp``]
      :refid: web-request-security-info-used-ocsp
      :refname: usedOcsp
      :type: (boolean, optional)
      :annotation: -- [Added in TB 115.0]

      True if the TLS connection made OCSP requests.

   .. _web^request.^security^info.used^private^dns:

   .. api-member::
      :name: [``usedPrivateDns``]
      :refid: web-request-security-info-used-private-dns
      :refname: usedPrivateDns
      :type: (boolean, optional)
      :annotation: -- [Added in TB 115.0]

      True if the TLS connection used a privacy-preserving DNS transport like DNS-over-HTTPS.

   .. _web^request.^security^info.weakness^reasons:

   .. api-member::
      :name: [``weaknessReasons``]
      :refid: web-request-security-info-weakness-reasons
      :refname: weaknessReasons
      :type: (array of :ref:`web^request.^transport^weakness^reasons`, optional)

      list of reasons that cause the request to be considered weak, if state is "weak"

.. _web^request.^transport^weakness^reasons:

TransportWeaknessReasons
------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^transport^weakness^reasons.cipher:

         .. api-member::
            :name: :value:`cipher`
            :refid: web-request-transport-weakness-reasons-cipher
            :refname: cipher

.. _web^request.^upload^data:

UploadData
----------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Contains data uploaded in a URL request.

.. api-header::
   :label: object

   .. _web^request.^upload^data.bytes:

   .. api-member::
      :name: [``bytes``]
      :refid: web-request-upload-data-bytes
      :refname: bytes
      :type: (any, optional)

      An ArrayBuffer with a copy of the data.

   .. _web^request.^upload^data.file:

   .. api-member::
      :name: [``file``]
      :refid: web-request-upload-data-file
      :refname: file
      :type: (string, optional)

      A string with the file's path and name.

.. _web^request.^url^classification:

UrlClassification
-----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _web^request.^url^classification.first^party:

   .. api-member::
      :name: ``firstParty``
      :refid: web-request-url-classification-first-party
      :refname: firstParty
      :type: (:ref:`web^request.^url^classification^party`)

      Classification flags if the request has been classified and it is first party.

   .. _web^request.^url^classification.third^party:

   .. api-member::
      :name: ``thirdParty``
      :refid: web-request-url-classification-third-party
      :refname: thirdParty
      :type: (:ref:`web^request.^url^classification^party`)

      Classification flags if the request has been classified and it or its window hierarchy is third party.

.. _web^request.^url^classification^flags:

UrlClassificationFlags
----------------------

.. api-section-annotation-hack:: 

Tracking flags that match our internal tracking classification

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^request.^url^classification^flags.antifraud:

         .. api-member::
            :name: :value:`antifraud`
            :refid: web-request-url-classification-flags-antifraud
            :refname: antifraud

         .. _web^request.^url^classification^flags.any_basic_tracking:

         .. api-member::
            :name: :value:`any_basic_tracking`
            :refid: web-request-url-classification-flags-any-basic-tracking
            :refname: any_basic_tracking

         .. _web^request.^url^classification^flags.any_social_tracking:

         .. api-member::
            :name: :value:`any_social_tracking`
            :refid: web-request-url-classification-flags-any-social-tracking
            :refname: any_social_tracking

         .. _web^request.^url^classification^flags.any_strict_tracking:

         .. api-member::
            :name: :value:`any_strict_tracking`
            :refid: web-request-url-classification-flags-any-strict-tracking
            :refname: any_strict_tracking

         .. _web^request.^url^classification^flags.consentmanager:

         .. api-member::
            :name: :value:`consentmanager`
            :refid: web-request-url-classification-flags-consentmanager
            :refname: consentmanager

         .. _web^request.^url^classification^flags.cryptomining:

         .. api-member::
            :name: :value:`cryptomining`
            :refid: web-request-url-classification-flags-cryptomining
            :refname: cryptomining

         .. _web^request.^url^classification^flags.cryptomining_content:

         .. api-member::
            :name: :value:`cryptomining_content`
            :refid: web-request-url-classification-flags-cryptomining-content
            :refname: cryptomining_content

         .. _web^request.^url^classification^flags.emailtracking:

         .. api-member::
            :name: :value:`emailtracking`
            :refid: web-request-url-classification-flags-emailtracking
            :refname: emailtracking

         .. _web^request.^url^classification^flags.emailtracking_content:

         .. api-member::
            :name: :value:`emailtracking_content`
            :refid: web-request-url-classification-flags-emailtracking-content
            :refname: emailtracking_content

         .. _web^request.^url^classification^flags.fingerprinting:

         .. api-member::
            :name: :value:`fingerprinting`
            :refid: web-request-url-classification-flags-fingerprinting
            :refname: fingerprinting

         .. _web^request.^url^classification^flags.fingerprinting_content:

         .. api-member::
            :name: :value:`fingerprinting_content`
            :refid: web-request-url-classification-flags-fingerprinting-content
            :refname: fingerprinting_content

         .. _web^request.^url^classification^flags.tracking:

         .. api-member::
            :name: :value:`tracking`
            :refid: web-request-url-classification-flags-tracking
            :refname: tracking

         .. _web^request.^url^classification^flags.tracking_ad:

         .. api-member::
            :name: :value:`tracking_ad`
            :refid: web-request-url-classification-flags-tracking-ad
            :refname: tracking_ad

         .. _web^request.^url^classification^flags.tracking_analytics:

         .. api-member::
            :name: :value:`tracking_analytics`
            :refid: web-request-url-classification-flags-tracking-analytics
            :refname: tracking_analytics

         .. _web^request.^url^classification^flags.tracking_content:

         .. api-member::
            :name: :value:`tracking_content`
            :refid: web-request-url-classification-flags-tracking-content
            :refname: tracking_content

         .. _web^request.^url^classification^flags.tracking_social:

         .. api-member::
            :name: :value:`tracking_social`
            :refid: web-request-url-classification-flags-tracking-social
            :refname: tracking_social

.. _web^request.^url^classification^party:

UrlClassificationParty
----------------------

.. api-section-annotation-hack:: 

If the request has been classified this is an array of :ref:`web^request.^url^classification^flags`.

.. api-header::
   :label: array of :ref:`web^request.^url^classification^flags`

.. rst-class:: api-main-section

Properties
==========

.. _web^request.^m^a^x_^h^a^n^d^l^e^r_^b^e^h^a^v^i^o^r_^c^h^a^n^g^e^d_^c^a^l^l^s_^p^e^r_10_^m^i^n^u^t^e^s:

MAX_HANDLER_BEHAVIOR_CHANGED_CALLS_PER_10_MINUTES
-------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

The maximum number of times that :code:`handlerBehaviorChanged` can be called per 10 minute sustained interval. :code:`handlerBehaviorChanged` is an expensive function call that shouldn't be called often.
