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

.. hint::

   The webRequest API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/webRequest>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.webRequest` API to observe and analyze traffic and to intercept, block, or modify requests in-flight.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`webRequest`

   Grant access to some or all methods of the webRequest API.

.. api-member::
   :name: :permission:`webRequestBlocking`

   Allows to use the blocking features of the webRequest API. With this permission, listeners can synchronously modify or cancel requests before they are sent or before a response is delivered. Without it, listeners can only observe requests without blocking or altering them.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`webRequest` is required to use ``messenger.webRequest.*``.

.. rst-class:: api-main-section

Functions
=========

.. _webRequest.filterResponseData:

filterResponseData(requestId)
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 57]

...

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``requestId``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: `StreamFilter <https://developer.mozilla.org/en-US/docs/Web/API/StreamFilter>`__

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`
   - :permission:`webRequestBlocking`

.. _webRequest.getSecurityInfo:

getSecurityInfo(requestId, [options])
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Retrieves the security information for the request.  Returns a promise that will resolve to a SecurityInfo object.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``requestId``
      :type: (string)

   .. api-member::
      :name: [``options``]
      :type: (object, optional)

      .. api-member::
         :name: [``certificateChain``]
         :type: (boolean, optional)

         Include the entire certificate chain.

      .. api-member::
         :name: [``rawDER``]
         :type: (boolean, optional)

         Include raw certificate data for processing by the extension.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _webRequest.handlerBehaviorChanged:

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

.. _webRequest.onAuthRequired:

onAuthRequired
--------------

.. api-section-annotation-hack:: -- [Added in TB 54]

Fired when an authentication failure is received. The listener has three options: it can provide authentication credentials, it can cancel the request and display the error page, or it can take no action on the challenge. If bad user credentials are provided, this may be called multiple times for the same request.

.. note::

   To handle a request asynchronously, return a Promise from the listener.

.. api-header::
   :label: Parameters for onAuthRequired.addListener(listener, filter, extraInfoSpec)

   .. api-member::
      :name: ``listener(details, asyncCallback)``

      A function that will be called when this event occurs.

   .. api-member::
      :name: ``filter``
      :type: (:ref:`webRequest.RequestFilter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. api-member::
      :name: [``extraInfoSpec``]
      :type: (array of :ref:`webRequest.OnAuthRequiredOptions`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``challenger``
         :type: (object)

         The server requesting authentication.

         .. note::

            Before version 57, when authenticating to a proxy server, the :code:`challenger.host` property contains the hostname for the requested URL rather than the hostname for the proxy.

         .. api-member::
            :name: ``host``
            :type: (string)

         .. api-member::
            :name: ``port``
            :type: (integer)

      .. api-member::
         :name: ``frameId``
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. api-member::
         :name: ``isProxy``
         :type: (boolean)

         True for Proxy-Authenticate, false for WWW-Authenticate.

      .. api-member::
         :name: ``method``
         :type: (string)

         Standard HTTP method.

      .. api-member::
         :name: ``parentFrameId``
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. api-member::
         :name: ``requestId``
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. api-member::
         :name: ``scheme``
         :type: (string)

         The authentication scheme, e.g. Basic or Digest.

      .. api-member::
         :name: ``statusCode``
         :type: (integer)

         Standard HTTP status code returned by the server.

      .. api-member::
         :name: ``statusLine``
         :type: (string)

         HTTP status line of the response or the 'HTTP/0.9 200 OK' string for HTTP/0.9 responses (i.e., responses that lack a status line) or an empty string if there are no headers.

      .. api-member::
         :name: ``tabId``
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. api-member::
         :name: ``thirdParty``
         :type: (boolean)
         :annotation: -- [Added in TB 72]

         Indicates if this request and its content window hierarchy is third party.

      .. api-member::
         :name: ``timeStamp``
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. api-member::
         :name: ``type``
         :type: (:ref:`webRequest.ResourceType`)

         How the requested resource will be used.

      .. api-member::
         :name: ``url``
         :type: (string)

      .. api-member::
         :name: [``cookieStoreId``]
         :type: (string, optional)
         :annotation: -- [Added in TB 68]

         The cookie store ID of the contextual identity.

      .. api-member::
         :name: [``documentUrl``]
         :type: (string, optional)

         URL of the page into which the requested resource will be loaded.

      .. api-member::
         :name: [``incognito``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68]

         True for private browsing requests.

      .. api-member::
         :name: [``originUrl``]
         :type: (string, optional)

         URL of the resource that triggered this request.

      .. api-member::
         :name: [``realm``]
         :type: (string, optional)

         The authentication realm provided by the server, if there is one.

      .. api-member::
         :name: [``responseHeaders``]
         :type: (:ref:`webRequest.HttpHeaders`, optional)

         The HTTP response headers that were received along with this response.

      .. api-member::
         :name: [``urlClassification``]
         :type: (:ref:`webRequest.UrlClassification`, optional)
         :annotation: -- [Added in TB 74]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

   .. api-member::
      :name: [``asyncCallback``]
      :type: (function, optional)

.. api-header::
   :label: Expected return value of the listener function

   .. api-member::
      :type: :ref:`webRequest.BlockingResponse`

      If "blocking" is specified in the "extraInfoSpec" parameter, the event listener should return an object of this type.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _webRequest.onBeforeRedirect:

onBeforeRedirect
----------------

.. api-section-annotation-hack:: -- [Added in TB 46]

Fired when a server-initiated redirect is about to occur.

.. api-header::
   :label: Parameters for onBeforeRedirect.addListener(listener, filter, extraInfoSpec)

   .. api-member::
      :name: ``listener(details)``

      A function that will be called when this event occurs.

   .. api-member::
      :name: ``filter``
      :type: (:ref:`webRequest.RequestFilter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. api-member::
      :name: [``extraInfoSpec``]
      :type: (array of :ref:`webRequest.OnBeforeRedirectOptions`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``frameId``
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. api-member::
         :name: ``fromCache``
         :type: (boolean)

         Indicates if this response was fetched from disk cache.

      .. api-member::
         :name: ``method``
         :type: (string)

         Standard HTTP method.

      .. api-member::
         :name: ``parentFrameId``
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. api-member::
         :name: ``redirectUrl``
         :type: (string)

         The new URL.

      .. api-member::
         :name: ``requestId``
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. api-member::
         :name: ``statusCode``
         :type: (integer)

         Standard HTTP status code returned by the server.

      .. api-member::
         :name: ``statusLine``
         :type: (string)

         HTTP status line of the response or the 'HTTP/0.9 200 OK' string for HTTP/0.9 responses (i.e., responses that lack a status line) or an empty string if there are no headers.

      .. api-member::
         :name: ``tabId``
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. api-member::
         :name: ``thirdParty``
         :type: (boolean)
         :annotation: -- [Added in TB 72]

         Indicates if this request and its content window hierarchy is third party.

      .. api-member::
         :name: ``timeStamp``
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. api-member::
         :name: ``type``
         :type: (:ref:`webRequest.ResourceType`)

         How the requested resource will be used.

      .. api-member::
         :name: ``url``
         :type: (string)

      .. api-member::
         :name: [``cookieStoreId``]
         :type: (string, optional)
         :annotation: -- [Added in TB 68]

         The cookie store ID of the contextual identity.

      .. api-member::
         :name: [``documentUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 54]

         URL of the page into which the requested resource will be loaded.

      .. api-member::
         :name: [``incognito``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68]

         True for private browsing requests.

      .. api-member::
         :name: [``ip``]
         :type: (string, optional)

         The server IP address that the request was actually sent to. Note that it may be a literal IPv6 address.

      .. api-member::
         :name: [``originUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 48]

         URL of the resource that triggered this request.

      .. api-member::
         :name: [``responseHeaders``]
         :type: (:ref:`webRequest.HttpHeaders`, optional)

         The HTTP response headers that were received along with this redirect.

      .. api-member::
         :name: [``urlClassification``]
         :type: (:ref:`webRequest.UrlClassification`, optional)
         :annotation: -- [Added in TB 74]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _webRequest.onBeforeRequest:

onBeforeRequest
---------------

.. api-section-annotation-hack:: -- [Added in TB 46]

Fired when a request is about to occur.

.. note::

   Asynchronous event listeners are supported from version 52.

.. api-header::
   :label: Parameters for onBeforeRequest.addListener(listener, filter, extraInfoSpec)

   .. api-member::
      :name: ``listener(details)``

      A function that will be called when this event occurs.

   .. api-member::
      :name: ``filter``
      :type: (:ref:`webRequest.RequestFilter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. api-member::
      :name: [``extraInfoSpec``]
      :type: (array of :ref:`webRequest.OnBeforeRequestOptions`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``frameId``
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. api-member::
         :name: ``method``
         :type: (string)

         Standard HTTP method.

      .. api-member::
         :name: ``parentFrameId``
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. api-member::
         :name: ``requestId``
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. api-member::
         :name: ``tabId``
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. api-member::
         :name: ``thirdParty``
         :type: (boolean)
         :annotation: -- [Added in TB 72]

         Indicates if this request and its content window hierarchy is third party.

      .. api-member::
         :name: ``timeStamp``
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. api-member::
         :name: ``type``
         :type: (:ref:`webRequest.ResourceType`)

         How the requested resource will be used.

      .. api-member::
         :name: ``url``
         :type: (string)

      .. api-member::
         :name: [``cookieStoreId``]
         :type: (string, optional)
         :annotation: -- [Added in TB 68]

         The cookie store ID of the contextual identity.

      .. api-member::
         :name: [``documentUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 54]

         URL of the page into which the requested resource will be loaded.

      .. api-member::
         :name: [``incognito``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68]

         True for private browsing requests.

      .. api-member::
         :name: [``originUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 48]

         URL of the resource that triggered this request.

      .. api-member::
         :name: [``requestBody``]
         :type: (object, optional)
         :annotation: -- [Added in TB 53]

         Contains the HTTP request body data. Only provided if extraInfoSpec contains 'requestBody'.

         .. api-member::
            :name: [``error``]
            :type: (string, optional)

            Errors when obtaining request body data.

         .. api-member::
            :name: [``formData``]
            :type: (object, optional)

            If the request method is POST and the body is a sequence of key-value pairs encoded in UTF8, encoded as either multipart/form-data, or application/x-www-form-urlencoded, this dictionary is present and for each key contains the list of all values for that key. If the data is of another media type, or if it is malformed, the dictionary is not present. An example value of this dictionary is {'key': ['value1', 'value2']}.

         .. api-member::
            :name: [``raw``]
            :type: (array of :ref:`webRequest.UploadData`, optional)

            If the request method is PUT or POST, and the body is not already parsed in formData, then the unparsed request body elements are contained in this array.

      .. api-member::
         :name: [``urlClassification``]
         :type: (:ref:`webRequest.UrlClassification`, optional)
         :annotation: -- [Added in TB 74]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Expected return value of the listener function

   .. api-member::
      :type: :ref:`webRequest.BlockingResponse`

      If "blocking" is specified in the "extraInfoSpec" parameter, the event listener should return an object of this type.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _webRequest.onBeforeSendHeaders:

onBeforeSendHeaders
-------------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired before sending an HTTP request, once the request headers are available. This may occur after a TCP connection is made to the server, but before any HTTP data is sent.

.. note::

   Asynchronous event listeners are supported from version 52.

.. api-header::
   :label: Parameters for onBeforeSendHeaders.addListener(listener, filter, extraInfoSpec)

   .. api-member::
      :name: ``listener(details)``

      A function that will be called when this event occurs.

   .. api-member::
      :name: ``filter``
      :type: (:ref:`webRequest.RequestFilter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. api-member::
      :name: [``extraInfoSpec``]
      :type: (array of :ref:`webRequest.OnBeforeSendHeadersOptions`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``frameId``
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. api-member::
         :name: ``method``
         :type: (string)

         Standard HTTP method.

      .. api-member::
         :name: ``parentFrameId``
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. api-member::
         :name: ``requestId``
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. api-member::
         :name: ``tabId``
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. api-member::
         :name: ``thirdParty``
         :type: (boolean)
         :annotation: -- [Added in TB 72]

         Indicates if this request and its content window hierarchy is third party.

      .. api-member::
         :name: ``timeStamp``
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. api-member::
         :name: ``type``
         :type: (:ref:`webRequest.ResourceType`)

         How the requested resource will be used.

      .. api-member::
         :name: ``url``
         :type: (string)

      .. api-member::
         :name: [``cookieStoreId``]
         :type: (string, optional)
         :annotation: -- [Added in TB 68]

         The cookie store ID of the contextual identity.

      .. api-member::
         :name: [``documentUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 54]

         URL of the page into which the requested resource will be loaded.

      .. api-member::
         :name: [``incognito``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68]

         True for private browsing requests.

      .. api-member::
         :name: [``originUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 48]

         URL of the resource that triggered this request.

      .. api-member::
         :name: [``requestHeaders``]
         :type: (:ref:`webRequest.HttpHeaders`, optional)
         :annotation: -- [Added in TB 53]

         The HTTP request headers that are going to be sent out with this request.

      .. api-member::
         :name: [``urlClassification``]
         :type: (:ref:`webRequest.UrlClassification`, optional)
         :annotation: -- [Added in TB 74]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Expected return value of the listener function

   .. api-member::
      :type: :ref:`webRequest.BlockingResponse`

      If "blocking" is specified in the "extraInfoSpec" parameter, the event listener should return an object of this type.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _webRequest.onCompleted:

onCompleted
-----------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when a request is completed.

.. api-header::
   :label: Parameters for onCompleted.addListener(listener, filter, extraInfoSpec)

   .. api-member::
      :name: ``listener(details)``

      A function that will be called when this event occurs.

   .. api-member::
      :name: ``filter``
      :type: (:ref:`webRequest.RequestFilter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. api-member::
      :name: [``extraInfoSpec``]
      :type: (array of :ref:`webRequest.OnCompletedOptions`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``frameId``
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. api-member::
         :name: ``fromCache``
         :type: (boolean)

         Indicates if this response was fetched from disk cache.

      .. api-member::
         :name: ``method``
         :type: (string)

         Standard HTTP method.

      .. api-member::
         :name: ``parentFrameId``
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. api-member::
         :name: ``requestId``
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. api-member::
         :name: ``requestSize``
         :type: (integer)

         For http requests, the bytes transferred in the request. Only available in onCompleted.

      .. api-member::
         :name: ``responseSize``
         :type: (integer)

         For http requests, the bytes received in the request. Only available in onCompleted.

      .. api-member::
         :name: ``statusCode``
         :type: (integer)

         Standard HTTP status code returned by the server.

      .. api-member::
         :name: ``statusLine``
         :type: (string)

         HTTP status line of the response or the 'HTTP/0.9 200 OK' string for HTTP/0.9 responses (i.e., responses that lack a status line) or an empty string if there are no headers.

      .. api-member::
         :name: ``tabId``
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. api-member::
         :name: ``thirdParty``
         :type: (boolean)
         :annotation: -- [Added in TB 72]

         Indicates if this request and its content window hierarchy is third party.

      .. api-member::
         :name: ``timeStamp``
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. api-member::
         :name: ``type``
         :type: (:ref:`webRequest.ResourceType`)

         How the requested resource will be used.

      .. api-member::
         :name: ``url``
         :type: (string)

      .. api-member::
         :name: ``urlClassification``
         :type: (:ref:`webRequest.UrlClassification`)
         :annotation: -- [Added in TB 74]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

      .. api-member::
         :name: [``cookieStoreId``]
         :type: (string, optional)
         :annotation: -- [Added in TB 68]

         The cookie store ID of the contextual identity.

      .. api-member::
         :name: [``documentUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 54]

         URL of the page into which the requested resource will be loaded.

      .. api-member::
         :name: [``incognito``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68]

         True for private browsing requests.

      .. api-member::
         :name: [``ip``]
         :type: (string, optional)

         The server IP address that the request was actually sent to. Note that it may be a literal IPv6 address.

      .. api-member::
         :name: [``originUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 48]

         URL of the resource that triggered this request.

      .. api-member::
         :name: [``responseHeaders``]
         :type: (:ref:`webRequest.HttpHeaders`, optional)

         The HTTP response headers that were received along with this response.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _webRequest.onErrorOccurred:

onErrorOccurred
---------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when an error occurs.

.. api-header::
   :label: Parameters for onErrorOccurred.addListener(listener, filter)

   .. api-member::
      :name: ``listener(details)``

      A function that will be called when this event occurs.

   .. api-member::
      :name: ``filter``
      :type: (:ref:`webRequest.RequestFilter`)

      A set of filters that restricts the events that will be sent to this listener.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``error``
         :type: (string)

         The error description. This string is *not* guaranteed to remain backwards compatible between releases. You must not parse and act based upon its content.

      .. api-member::
         :name: ``frameId``
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. api-member::
         :name: ``fromCache``
         :type: (boolean)

         Indicates if this response was fetched from disk cache.

      .. api-member::
         :name: ``method``
         :type: (string)

         Standard HTTP method.

      .. api-member::
         :name: ``parentFrameId``
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. api-member::
         :name: ``requestId``
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. api-member::
         :name: ``tabId``
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. api-member::
         :name: ``thirdParty``
         :type: (boolean)
         :annotation: -- [Added in TB 72]

         Indicates if this request and its content window hierarchy is third party.

      .. api-member::
         :name: ``timeStamp``
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. api-member::
         :name: ``type``
         :type: (:ref:`webRequest.ResourceType`)

         How the requested resource will be used.

      .. api-member::
         :name: ``url``
         :type: (string)

      .. api-member::
         :name: [``cookieStoreId``]
         :type: (string, optional)
         :annotation: -- [Added in TB 68]

         The cookie store ID of the contextual identity.

      .. api-member::
         :name: [``documentUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 54]

         URL of the page into which the requested resource will be loaded.

      .. api-member::
         :name: [``incognito``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68]

         True for private browsing requests.

      .. api-member::
         :name: [``ip``]
         :type: (string, optional)

         The server IP address that the request was actually sent to. Note that it may be a literal IPv6 address.

      .. api-member::
         :name: [``originUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 48]

         URL of the resource that triggered this request.

      .. api-member::
         :name: [``urlClassification``]
         :type: (:ref:`webRequest.UrlClassification`, optional)
         :annotation: -- [Added in TB 74]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _webRequest.onHeadersReceived:

onHeadersReceived
-----------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when HTTP response headers of a request have been received.

.. note::

   Modification of the 'Content-Type' header is supported from version 51.

.. note::

   Asynchronous event listeners are supported from version 52.

.. api-header::
   :label: Parameters for onHeadersReceived.addListener(listener, filter, extraInfoSpec)

   .. api-member::
      :name: ``listener(details)``

      A function that will be called when this event occurs.

   .. api-member::
      :name: ``filter``
      :type: (:ref:`webRequest.RequestFilter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. api-member::
      :name: [``extraInfoSpec``]
      :type: (array of :ref:`webRequest.OnHeadersReceivedOptions`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``frameId``
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. api-member::
         :name: ``method``
         :type: (string)

         Standard HTTP method.

      .. api-member::
         :name: ``parentFrameId``
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. api-member::
         :name: ``requestId``
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. api-member::
         :name: ``statusCode``
         :type: (integer)

         Standard HTTP status code returned by the server.

      .. api-member::
         :name: ``statusLine``
         :type: (string)

         HTTP status line of the response or the 'HTTP/0.9 200 OK' string for HTTP/0.9 responses (i.e., responses that lack a status line).

      .. api-member::
         :name: ``tabId``
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. api-member::
         :name: ``thirdParty``
         :type: (boolean)
         :annotation: -- [Added in TB 72]

         Indicates if this request and its content window hierarchy is third party.

      .. api-member::
         :name: ``timeStamp``
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. api-member::
         :name: ``type``
         :type: (:ref:`webRequest.ResourceType`)

         How the requested resource will be used.

      .. api-member::
         :name: ``url``
         :type: (string)

      .. api-member::
         :name: [``cookieStoreId``]
         :type: (string, optional)
         :annotation: -- [Added in TB 68]

         The cookie store ID of the contextual identity.

      .. api-member::
         :name: [``documentUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 54]

         URL of the page into which the requested resource will be loaded.

      .. api-member::
         :name: [``incognito``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68]

         True for private browsing requests.

      .. api-member::
         :name: [``originUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 48]

         URL of the resource that triggered this request.

      .. api-member::
         :name: [``responseHeaders``]
         :type: (:ref:`webRequest.HttpHeaders`, optional)

         The HTTP response headers that have been received with this response.

      .. api-member::
         :name: [``urlClassification``]
         :type: (:ref:`webRequest.UrlClassification`, optional)
         :annotation: -- [Added in TB 74]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Expected return value of the listener function

   .. api-member::
      :type: :ref:`webRequest.BlockingResponse`

      If "blocking" is specified in the "extraInfoSpec" parameter, the event listener should return an object of this type.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _webRequest.onResponseStarted:

onResponseStarted
-----------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when the first byte of the response body is received. For HTTP requests, this means that the status line and response headers are available.

.. api-header::
   :label: Parameters for onResponseStarted.addListener(listener, filter, extraInfoSpec)

   .. api-member::
      :name: ``listener(details)``

      A function that will be called when this event occurs.

   .. api-member::
      :name: ``filter``
      :type: (:ref:`webRequest.RequestFilter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. api-member::
      :name: [``extraInfoSpec``]
      :type: (array of :ref:`webRequest.OnResponseStartedOptions`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``frameId``
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. api-member::
         :name: ``fromCache``
         :type: (boolean)

         Indicates if this response was fetched from disk cache.

      .. api-member::
         :name: ``method``
         :type: (string)

         Standard HTTP method.

      .. api-member::
         :name: ``parentFrameId``
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. api-member::
         :name: ``requestId``
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. api-member::
         :name: ``statusCode``
         :type: (integer)

         Standard HTTP status code returned by the server.

      .. api-member::
         :name: ``statusLine``
         :type: (string)

         HTTP status line of the response or the 'HTTP/0.9 200 OK' string for HTTP/0.9 responses (i.e., responses that lack a status line) or an empty string if there are no headers.

      .. api-member::
         :name: ``tabId``
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. api-member::
         :name: ``thirdParty``
         :type: (boolean)
         :annotation: -- [Added in TB 72]

         Indicates if this request and its content window hierarchy is third party.

      .. api-member::
         :name: ``timeStamp``
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. api-member::
         :name: ``type``
         :type: (:ref:`webRequest.ResourceType`)

         How the requested resource will be used.

      .. api-member::
         :name: ``url``
         :type: (string)

      .. api-member::
         :name: [``cookieStoreId``]
         :type: (string, optional)
         :annotation: -- [Added in TB 68]

         The cookie store ID of the contextual identity.

      .. api-member::
         :name: [``documentUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 54]

         URL of the page into which the requested resource will be loaded.

      .. api-member::
         :name: [``incognito``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68]

         True for private browsing requests.

      .. api-member::
         :name: [``ip``]
         :type: (string, optional)

         The server IP address that the request was actually sent to. Note that it may be a literal IPv6 address.

      .. api-member::
         :name: [``originUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 48]

         URL of the resource that triggered this request.

      .. api-member::
         :name: [``responseHeaders``]
         :type: (:ref:`webRequest.HttpHeaders`, optional)

         The HTTP response headers that were received along with this response.

      .. api-member::
         :name: [``urlClassification``]
         :type: (:ref:`webRequest.UrlClassification`, optional)
         :annotation: -- [Added in TB 74]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. _webRequest.onSendHeaders:

onSendHeaders
-------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired just before a request is going to be sent to the server (modifications of previous onBeforeSendHeaders callbacks are visible by the time onSendHeaders is fired).

.. api-header::
   :label: Parameters for onSendHeaders.addListener(listener, filter, extraInfoSpec)

   .. api-member::
      :name: ``listener(details)``

      A function that will be called when this event occurs.

   .. api-member::
      :name: ``filter``
      :type: (:ref:`webRequest.RequestFilter`)

      A set of filters that restricts the events that will be sent to this listener.

   .. api-member::
      :name: [``extraInfoSpec``]
      :type: (array of :ref:`webRequest.OnSendHeadersOptions`, optional)

      Array of extra information that should be passed to the listener function.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``frameId``
         :type: (integer)

         The value 0 indicates that the request happens in the main frame; a positive value indicates the ID of a subframe in which the request happens. If the document of a (sub-)frame is loaded (:code:`type` is :code:`main_frame` or :code:`sub_frame`), :code:`frameId` indicates the ID of this frame, not the ID of the outer frame. Frame IDs are unique within a tab.

      .. api-member::
         :name: ``method``
         :type: (string)

         Standard HTTP method.

      .. api-member::
         :name: ``parentFrameId``
         :type: (integer)

         ID of frame that wraps the frame which sent the request. Set to -1 if no parent frame exists.

      .. api-member::
         :name: ``requestId``
         :type: (string)

         The ID of the request. Request IDs are unique within a browser session. As a result, they could be used to relate different events of the same request.

      .. api-member::
         :name: ``tabId``
         :type: (integer)

         The ID of the tab in which the request takes place. Set to -1 if the request isn't related to a tab.

      .. api-member::
         :name: ``thirdParty``
         :type: (boolean)
         :annotation: -- [Added in TB 72]

         Indicates if this request and its content window hierarchy is third party.

      .. api-member::
         :name: ``timeStamp``
         :type: (number)

         The time when this signal is triggered, in milliseconds since the epoch.

      .. api-member::
         :name: ``type``
         :type: (:ref:`webRequest.ResourceType`)

         How the requested resource will be used.

      .. api-member::
         :name: ``url``
         :type: (string)

      .. api-member::
         :name: [``cookieStoreId``]
         :type: (string, optional)
         :annotation: -- [Added in TB 68]

         The cookie store ID of the contextual identity.

      .. api-member::
         :name: [``documentUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 54]

         URL of the page into which the requested resource will be loaded.

      .. api-member::
         :name: [``incognito``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68]

         True for private browsing requests.

      .. api-member::
         :name: [``originUrl``]
         :type: (string, optional)
         :annotation: -- [Added in TB 48]

         URL of the resource that triggered this request.

      .. api-member::
         :name: [``requestHeaders``]
         :type: (:ref:`webRequest.HttpHeaders`, optional)

         The HTTP request headers that have been sent out with this request.

      .. api-member::
         :name: [``urlClassification``]
         :type: (:ref:`webRequest.UrlClassification`, optional)
         :annotation: -- [Added in TB 74]

         Tracking classification if the request has been classified.

         .. note::

            Classification flags :code:`emailtracking` and :code:`emailtracking_content` added in Thunderbird 104.

.. api-header::
   :label: Required permissions

   - :permission:`webRequest`

.. rst-class:: api-main-section

Types
=====

.. _webRequest.BlockingResponse:

BlockingResponse
----------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Returns value for event handlers that have the 'blocking' extraInfoSpec applied. Allows the event handler to modify network requests.

.. api-header::
   :label: object

   .. _webRequest.BlockingResponse.authCredentials:

   .. api-member::
      :name: [``authCredentials``]
      :type: (object, optional)

      Only used as a response to the onAuthRequired event. If set, the request is made using the supplied credentials.

      .. api-member::
         :name: ``password``
         :type: (string)

      .. api-member::
         :name: ``username``
         :type: (string)

   .. _webRequest.BlockingResponse.cancel:

   .. api-member::
      :name: [``cancel``]
      :type: (boolean, optional)

      If true, the request is cancelled. Used in onBeforeRequest, this prevents the request from being sent.

   .. _webRequest.BlockingResponse.redirectUrl:

   .. api-member::
      :name: [``redirectUrl``]
      :type: (string, optional)

      Only used as a response to the onBeforeRequest and onHeadersReceived events. If set, the original request is prevented from being sent/completed and is instead redirected to the given URL. Redirections to non-HTTP schemes such as data: are allowed. Redirects initiated by a redirect action use the original request method for the redirect, with one exception: If the redirect is initiated at the onHeadersReceived stage, then the redirect will be issued using the GET method.

   .. _webRequest.BlockingResponse.requestHeaders:

   .. api-member::
      :name: [``requestHeaders``]
      :type: (:ref:`webRequest.HttpHeaders`, optional)

      Only used as a response to the onBeforeSendHeaders event. If set, the request is made with these request headers instead.

   .. _webRequest.BlockingResponse.responseHeaders:

   .. api-member::
      :name: [``responseHeaders``]
      :type: (:ref:`webRequest.HttpHeaders`, optional)

      Only used as a response to the onHeadersReceived event. If set, the server is assumed to have responded with these response headers instead. Only return :code:`responseHeaders` if you really want to modify the headers in order to limit the number of conflicts (only one extension may modify :code:`responseHeaders` for each request).

   .. _webRequest.BlockingResponse.upgradeToSecure:

   .. api-member::
      :name: [``upgradeToSecure``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 59]

      Only used as a response to the onBeforeRequest event. If set, the original request is prevented from being sent/completed and is instead upgraded to a secure request.  If any extension returns :code:`redirectUrl` during onBeforeRequest, :code:`upgradeToSecure` will have no affect.

.. _webRequest.CertificateInfo:

CertificateInfo
---------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Contains the certificate properties of the request if it is a secure request.

.. api-header::
   :label: object

   .. _webRequest.CertificateInfo.fingerprint:

   .. api-member::
      :name: ``fingerprint``
      :type: (object)

      .. api-member::
         :name: ``sha1``
         :type: (string)

      .. api-member::
         :name: ``sha256``
         :type: (string)

   .. _webRequest.CertificateInfo.isBuiltInRoot:

   .. api-member::
      :name: ``isBuiltInRoot``
      :type: (boolean)

   .. _webRequest.CertificateInfo.issuer:

   .. api-member::
      :name: ``issuer``
      :type: (string)

   .. _webRequest.CertificateInfo.serialNumber:

   .. api-member::
      :name: ``serialNumber``
      :type: (string)

   .. _webRequest.CertificateInfo.subject:

   .. api-member::
      :name: ``subject``
      :type: (string)

   .. _webRequest.CertificateInfo.subjectPublicKeyInfoDigest:

   .. api-member::
      :name: ``subjectPublicKeyInfoDigest``
      :type: (object)

      .. api-member::
         :name: ``sha256``
         :type: (string)

   .. _webRequest.CertificateInfo.validity:

   .. api-member::
      :name: ``validity``
      :type: (object)

      Contains start and end timestamps.

      .. api-member::
         :name: ``end``
         :type: (integer)

      .. api-member::
         :name: ``start``
         :type: (integer)

   .. _webRequest.CertificateInfo.rawDER:

   .. api-member::
      :name: [``rawDER``]
      :type: (array of integer, optional)

.. _webRequest.CertificateTransparencyStatus:

CertificateTransparencyStatus
-----------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`not_applicable`

         .. api-member::
            :name: :value:`policy_compliant`

         .. api-member::
            :name: :value:`policy_not_enough_scts`

         .. api-member::
            :name: :value:`policy_not_diverse_scts`

.. _webRequest.HttpHeaders:

HttpHeaders
-----------

.. api-section-annotation-hack:: -- [Added in TB 45]

An array of HTTP headers. Each header is represented as a dictionary containing the keys :code:`name` and either :code:`value` or :code:`binaryValue`.

.. api-header::
   :label: array of object

.. _webRequest.OnAuthRequiredOptions:

OnAuthRequiredOptions
---------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`responseHeaders`

         .. api-member::
            :name: :value:`blocking`

         .. api-member::
            :name: :value:`asyncBlocking`

.. _webRequest.OnBeforeRedirectOptions:

OnBeforeRedirectOptions
-----------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`responseHeaders`

.. _webRequest.OnBeforeRequestOptions:

OnBeforeRequestOptions
----------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`blocking`

         .. api-member::
            :name: :value:`requestBody`

.. _webRequest.OnBeforeSendHeadersOptions:

OnBeforeSendHeadersOptions
--------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`requestHeaders`

         .. api-member::
            :name: :value:`blocking`

.. _webRequest.OnCompletedOptions:

OnCompletedOptions
------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`responseHeaders`

.. _webRequest.OnHeadersReceivedOptions:

OnHeadersReceivedOptions
------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`blocking`

         .. api-member::
            :name: :value:`responseHeaders`

.. _webRequest.OnResponseStartedOptions:

OnResponseStartedOptions
------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`responseHeaders`

.. _webRequest.OnSendHeadersOptions:

OnSendHeadersOptions
--------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`requestHeaders`

.. _webRequest.RequestFilter:

RequestFilter
-------------

.. api-section-annotation-hack:: -- [Added in TB 45]

An object describing filters to apply to webRequest events.

.. note::

   From Thunderbird 78 onwards, if a filter contains unrecognized values in its :code:`types` property, then these values are ignored and :code:`addListener()` proceeds.

.. note::

   Before Thunderbird 78, if a filter contains unrecognized values in its :code:`types` property, :code:`addListener()` throws an exception.

.. api-header::
   :label: object

   .. _webRequest.RequestFilter.urls:

   .. api-member::
      :name: ``urls``
      :type: (array of string)

      A list of URLs or URL patterns. Requests that cannot match any of the URLs will be filtered out.

      .. note::

         Before Thunderbird 56, moz-extension:// URLs were not allowed.

   .. _webRequest.RequestFilter.incognito:

   .. api-member::
      :name: [``incognito``]
      :type: (boolean, optional)

      If provided, requests that do not match the incognito state will be filtered out.

   .. _webRequest.RequestFilter.tabId:

   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)
      :annotation: -- [Added in TB 53]

   .. _webRequest.RequestFilter.types:

   .. api-member::
      :name: [``types``]
      :type: (array of :ref:`webRequest.ResourceType`, optional)

      A list of request types. Requests that cannot match any of the types will be filtered out.

   .. _webRequest.RequestFilter.windowId:

   .. api-member::
      :name: [``windowId``]
      :type: (integer, optional)
      :annotation: -- [Added in TB 53]

.. _webRequest.ResourceType:

ResourceType
------------

.. api-section-annotation-hack:: -- [Added in TB 45]

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`main_frame`

         .. api-member::
            :name: :value:`sub_frame`

         .. api-member::
            :name: :value:`stylesheet`

         .. api-member::
            :name: :value:`script`

         .. api-member::
            :name: :value:`image`

         .. api-member::
            :name: :value:`object`

         .. api-member::
            :name: :value:`xmlhttprequest`

         .. api-member::
            :name: :value:`xslt`

         .. api-member::
            :name: :value:`ping`

         .. api-member::
            :name: :value:`beacon`

         .. api-member::
            :name: :value:`xml_dtd`

         .. api-member::
            :name: :value:`font`

         .. api-member::
            :name: :value:`media`

         .. api-member::
            :name: :value:`websocket`

         .. api-member::
            :name: :value:`csp_report`

         .. api-member::
            :name: :value:`imageset`

         .. api-member::
            :name: :value:`web_manifest`

         .. api-member::
            :name: :value:`speculative`
            :annotation: -- [Added in TB 63]

         .. api-member::
            :name: :value:`json`
            :annotation: -- [Added in TB 138]

            .. note::

               The "json" property is supported from Thunderbird 135, but requests of this type are only available from Thunderbird 138.

         .. api-member::
            :name: :value:`other`

.. _webRequest.SecurityInfo:

SecurityInfo
------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Contains the security properties of the request (ie. SSL/TLS information).

.. api-header::
   :label: object

   .. _webRequest.SecurityInfo.certificates:

   .. api-member::
      :name: ``certificates``
      :type: (array of :ref:`webRequest.CertificateInfo`)

      Certificate data if state is "secure".  Will only contain one entry unless :code:`certificateChain` is passed as an option.

   .. _webRequest.SecurityInfo.state:

   .. api-member::
      :name: ``state``
      :type: (`string`)

      Supported values:

      .. api-member::
         :name: :value:`insecure`

      .. api-member::
         :name: :value:`weak`

      .. api-member::
         :name: :value:`broken`

      .. api-member::
         :name: :value:`secure`

   .. _webRequest.SecurityInfo.certificateTransparencyStatus:

   .. api-member::
      :name: [``certificateTransparencyStatus``]
      :type: (:ref:`webRequest.CertificateTransparencyStatus`, optional)

      Certificate transparency compliance per RFC 6962.  See :code:`https://www.certificate-transparency.org/what-is-ct` for more information.

   .. _webRequest.SecurityInfo.cipherSuite:

   .. api-member::
      :name: [``cipherSuite``]
      :type: (string, optional)

      The cipher suite used in this request if state is "secure".

   .. _webRequest.SecurityInfo.errorMessage:

   .. api-member::
      :name: [``errorMessage``]
      :type: (string, optional)

      Error message if state is "broken"

   .. _webRequest.SecurityInfo.hpkp:

   .. api-member::
      :name: [``hpkp``]
      :type: (string, optional)

      True if host uses Public Key Pinning and state is "secure".

   .. _webRequest.SecurityInfo.hsts:

   .. api-member::
      :name: [``hsts``]
      :type: (boolean, optional)

      True if host uses Strict Transport Security and state is "secure".

   .. _webRequest.SecurityInfo.isDomainMismatch:

   .. api-member::
      :name: [``isDomainMismatch``]
      :type: (boolean, optional) **Deprecated.**

      The domain name does not match the certificate domain.

   .. _webRequest.SecurityInfo.isExtendedValidation:

   .. api-member::
      :name: [``isExtendedValidation``]
      :type: (boolean, optional)

   .. _webRequest.SecurityInfo.isNotValidAtThisTime:

   .. api-member::
      :name: [``isNotValidAtThisTime``]
      :type: (boolean, optional) **Deprecated.**

      The certificate is either expired or is not yet valid.  See :code:`CertificateInfo.validity` for start and end dates.

   .. _webRequest.SecurityInfo.isUntrusted:

   .. api-member::
      :name: [``isUntrusted``]
      :type: (boolean, optional) **Deprecated.**

   .. _webRequest.SecurityInfo.keaGroupName:

   .. api-member::
      :name: [``keaGroupName``]
      :type: (string, optional)

      The key exchange algorithm used in this request if state is "secure".

   .. _webRequest.SecurityInfo.overridableErrorCategory:

   .. api-member::
      :name: [``overridableErrorCategory``]
      :type: (`string`, optional)

      The type of certificate error that was overridden for this connection, if any.

      Supported values:

      .. api-member::
         :name: :value:`trust_error`

      .. api-member::
         :name: :value:`domain_mismatch`

      .. api-member::
         :name: :value:`expired_or_not_yet_valid`

   .. _webRequest.SecurityInfo.protocolVersion:

   .. api-member::
      :name: [``protocolVersion``]
      :type: (`string`, optional)

      Protocol version if state is "secure"

      Supported values:

      .. api-member::
         :name: :value:`TLSv1`

      .. api-member::
         :name: :value:`TLSv1.1`

      .. api-member::
         :name: :value:`TLSv1.2`

      .. api-member::
         :name: :value:`TLSv1.3`

      .. api-member::
         :name: :value:`unknown`

   .. _webRequest.SecurityInfo.secretKeyLength:

   .. api-member::
      :name: [``secretKeyLength``]
      :type: (number, optional)
      :annotation: -- [Added in TB 109]

      The length (in bits) of the secret key.

   .. _webRequest.SecurityInfo.signatureSchemeName:

   .. api-member::
      :name: [``signatureSchemeName``]
      :type: (string, optional)

      The signature scheme used in this request if state is "secure".

   .. _webRequest.SecurityInfo.usedDelegatedCredentials:

   .. api-member::
      :name: [``usedDelegatedCredentials``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 112]

      True if the TLS connection used Delegated Credentials.

   .. _webRequest.SecurityInfo.usedEch:

   .. api-member::
      :name: [``usedEch``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 112]

      True if the TLS connection used Encrypted Client Hello.

   .. _webRequest.SecurityInfo.usedOcsp:

   .. api-member::
      :name: [``usedOcsp``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 112]

      True if the TLS connection made OCSP requests.

   .. _webRequest.SecurityInfo.usedPrivateDns:

   .. api-member::
      :name: [``usedPrivateDns``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 112]

      True if the TLS connection used a privacy-preserving DNS transport like DNS-over-HTTPS.

   .. _webRequest.SecurityInfo.weaknessReasons:

   .. api-member::
      :name: [``weaknessReasons``]
      :type: (array of :ref:`webRequest.TransportWeaknessReasons`, optional)

      list of reasons that cause the request to be considered weak, if state is "weak"

.. _webRequest.TransportWeaknessReasons:

TransportWeaknessReasons
------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`cipher`

.. _webRequest.UploadData:

UploadData
----------

.. api-section-annotation-hack:: -- [Added in TB 45]

Contains data uploaded in a URL request.

.. api-header::
   :label: object

   .. _webRequest.UploadData.bytes:

   .. api-member::
      :name: [``bytes``]
      :type: (any, optional)

      An ArrayBuffer with a copy of the data.

   .. _webRequest.UploadData.file:

   .. api-member::
      :name: [``file``]
      :type: (string, optional)

      A string with the file's path and name.

.. _webRequest.UrlClassification:

UrlClassification
-----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _webRequest.UrlClassification.firstParty:

   .. api-member::
      :name: ``firstParty``
      :type: (:ref:`webRequest.UrlClassificationParty`)

      Classification flags if the request has been classified and it is first party.

   .. _webRequest.UrlClassification.thirdParty:

   .. api-member::
      :name: ``thirdParty``
      :type: (:ref:`webRequest.UrlClassificationParty`)

      Classification flags if the request has been classified and it or its window hierarchy is third party.

.. _webRequest.UrlClassificationFlags:

UrlClassificationFlags
----------------------

.. api-section-annotation-hack:: 

Tracking flags that match our internal tracking classification

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`fingerprinting`

         .. api-member::
            :name: :value:`fingerprinting_content`

         .. api-member::
            :name: :value:`cryptomining`

         .. api-member::
            :name: :value:`cryptomining_content`

         .. api-member::
            :name: :value:`emailtracking`

         .. api-member::
            :name: :value:`emailtracking_content`

         .. api-member::
            :name: :value:`tracking`

         .. api-member::
            :name: :value:`tracking_ad`

         .. api-member::
            :name: :value:`tracking_analytics`

         .. api-member::
            :name: :value:`tracking_social`

         .. api-member::
            :name: :value:`tracking_content`

         .. api-member::
            :name: :value:`any_basic_tracking`

         .. api-member::
            :name: :value:`any_strict_tracking`

         .. api-member::
            :name: :value:`any_social_tracking`

         .. api-member::
            :name: :value:`consentmanager`

         .. api-member::
            :name: :value:`antifraud`

.. _webRequest.UrlClassificationParty:

UrlClassificationParty
----------------------

.. api-section-annotation-hack:: 

If the request has been classified this is an array of :ref:`webRequest.UrlClassificationFlags`.

.. api-header::
   :label: array of :ref:`webRequest.UrlClassificationFlags`

.. rst-class:: api-main-section

Properties
==========

.. _webRequest.MAX_HANDLER_BEHAVIOR_CHANGED_CALLS_PER_10_MINUTES:

MAX_HANDLER_BEHAVIOR_CHANGED_CALLS_PER_10_MINUTES
-------------------------------------------------

.. api-section-annotation-hack:: 

The maximum number of times that :code:`handlerBehaviorChanged` can be called per 10 minute sustained interval. :code:`handlerBehaviorChanged` is an expensive function call that shouldn't be called often.
