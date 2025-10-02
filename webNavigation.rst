.. container:: sticky-sidebar

  ≡ webNavigation API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=================
webNavigation API
=================

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The webNavigation API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.webNavigation` API to receive notifications about the status of navigation requests in-flight.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _web^navigation.permission.web^navigation:

.. api-member::
   :name: :permission:`webNavigation`
   :refid: web-navigation-permission-web-navigation
   :refname: webNavigation

   Access browser activity during navigation.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`webNavigation` is required to use ``messenger.webNavigation.*``.

.. rst-class:: api-main-section

Functions
=========

.. _web^navigation.get^all^frames:

getAllFrames(details)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 47]

Retrieves information about all frames of a given tab.

.. note::

   The returned objects do not include the :code:`errorOccurred` property. See `bug 1248418 <https://bugzil.la/1248418>`__.

.. api-header::
   :label: Parameters

   .. _web^navigation.get^all^frames.details:

   .. api-member::
      :name: ``details``
      :refid: web-navigation-get-all-frames-details
      :refname: details
      :type: (object)

      Information about the tab to retrieve all frames from.

      .. _web^navigation.get^all^frames.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-get-all-frames-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab.

.. api-header::
   :label: Return type (`Promise`_)

   .. _web^navigation.get^all^frames.returns:

   .. api-member::
      :refid: web-navigation-get-all-frames-returns
      :refname: _returns
      :type: array of object

      A list of frames in the given tab, null if the specified tab ID is invalid.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`webNavigation`

.. _web^navigation.get^frame:

getFrame(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 47]

Retrieves information about the given frame. A frame refers to an &lt;iframe&gt; or a &lt;frame&gt; of a web page and is identified by a tab ID and a frame ID.

.. api-header::
   :label: Parameters

   .. _web^navigation.get^frame.details:

   .. api-member::
      :name: ``details``
      :refid: web-navigation-get-frame-details
      :refname: details
      :type: (object)

      Information about the frame to retrieve information about.

      .. _web^navigation.get^frame.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-navigation-get-frame-details-frame-id
         :refname: frameId
         :type: (integer)

         The ID of the frame in the given tab.

      .. _web^navigation.get^frame.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-get-frame-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the frame is.

      .. _web^navigation.get^frame.details.process^id:

      .. api-member::
         :name: [``processId``]
         :refid: web-navigation-get-frame-details-process-id
         :refname: processId
         :type: (integer, optional)

         The ID of the process runs the renderer for this tab.

.. api-header::
   :label: Return type (`Promise`_)

   .. _web^navigation.get^frame.returns:

   .. api-member::
      :refid: web-navigation-get-frame-returns
      :refname: _returns
      :type: object

      Information about the requested frame, null if the specified frame ID and/or tab ID are invalid.

      .. _web^navigation.get^frame.returns.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-navigation-get-frame-returns-frame-id
         :refname: frameId
         :type: (integer)

         The ID of the frame. 0 indicates that this is the main frame; a positive value indicates the ID of a subframe.

      .. _web^navigation.get^frame.returns.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: web-navigation-get-frame-returns-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame. Set to -1 of no parent frame exists.

      .. _web^navigation.get^frame.returns.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-get-frame-returns-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the frame is.

      .. _web^navigation.get^frame.returns.url:

      .. api-member::
         :name: ``url``
         :refid: web-navigation-get-frame-returns-url
         :refname: url
         :type: (string)

         The URL currently associated with this frame, if the frame identified by the frameId existed at one point in the given tab. The fact that an URL is associated with a given frameId does not imply that the corresponding frame still exists.

      .. _web^navigation.get^frame.returns.error^occurred:

      .. api-member::
         :name: [``errorOccurred``]
         :refid: web-navigation-get-frame-returns-error-occurred
         :refname: errorOccurred
         :type: (boolean, optional)

         True if the last navigation in this frame was interrupted by an error, i.e. the onErrorOccurred event fired.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`webNavigation`

.. rst-class:: api-main-section

Events
======

.. _web^navigation.on^before^navigate:

onBeforeNavigate
----------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when a navigation is about to occur.

.. note::

   Filtering is supported from version 50.

.. note::

   If the filter parameter is empty, Thunderbird raises an exception.

.. api-header::
   :label: Parameters for onBeforeNavigate.addListener(listener, filters)

   .. _web^navigation.on^before^navigate.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-navigation-on-before-navigate-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^navigation.on^before^navigate.filters:

   .. api-member::
      :name: [``filters``]
      :refid: web-navigation-on-before-navigate-filters
      :refname: filters
      :type: (:ref:`web^navigation.^event^url^filters`, optional)

      Conditions that the URL being navigated to must satisfy. The 'schemes' and 'ports' fields of UrlFilter are ignored for this event.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^navigation.on^before^navigate.details:

   .. api-member::
      :name: ``details``
      :refid: web-navigation-on-before-navigate-details
      :refname: details
      :type: (object)

      .. _web^navigation.on^before^navigate.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-navigation-on-before-navigate-details-frame-id
         :refname: frameId
         :type: (integer)

         0 indicates the navigation happens in the tab content window; a positive value indicates navigation in a subframe. Frame IDs are unique for a given tab and process.

      .. _web^navigation.on^before^navigate.details.parent^frame^id:

      .. api-member::
         :name: ``parentFrameId``
         :refid: web-navigation-on-before-navigate-details-parent-frame-id
         :refname: parentFrameId
         :type: (integer)

         ID of frame that wraps the frame. Set to -1 of no parent frame exists.

      .. _web^navigation.on^before^navigate.details.process^id:

      .. api-member::
         :name: ``processId``
         :refid: web-navigation-on-before-navigate-details-process-id
         :refname: processId
         :type: (integer) **Unsupported.**

         The ID of the process runs the renderer for this tab.

      .. _web^navigation.on^before^navigate.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-on-before-navigate-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the navigation is about to occur.

      .. _web^navigation.on^before^navigate.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-navigation-on-before-navigate-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when the browser was about to start the navigation, in milliseconds since the epoch.

      .. _web^navigation.on^before^navigate.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-navigation-on-before-navigate-details-url
         :refname: url
         :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`webNavigation`

.. _web^navigation.on^committed:

onCommitted
-----------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when a navigation is committed. The document (and the resources it refers to, such as images and subframes) might still be downloading, but at least part of the document has been received from the server and the browser has decided to switch to the new document.

.. note::

   Filtering is supported from version 50.

.. note::

   If the filter parameter is empty, Thunderbird raises an exception.

.. api-header::
   :label: Parameters for onCommitted.addListener(listener, filters)

   .. _web^navigation.on^committed.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-navigation-on-committed-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^navigation.on^committed.filters:

   .. api-member::
      :name: [``filters``]
      :refid: web-navigation-on-committed-filters
      :refname: filters
      :type: (:ref:`web^navigation.^event^url^filters`, optional)

      Conditions that the URL being navigated to must satisfy. The 'schemes' and 'ports' fields of UrlFilter are ignored for this event.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^navigation.on^committed.details:

   .. api-member::
      :name: ``details``
      :refid: web-navigation-on-committed-details
      :refname: details
      :type: (object)

      .. _web^navigation.on^committed.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-navigation-on-committed-details-frame-id
         :refname: frameId
         :type: (integer)

         0 indicates the navigation happens in the tab content window; a positive value indicates navigation in a subframe. Frame IDs are unique within a tab.

      .. _web^navigation.on^committed.details.process^id:

      .. api-member::
         :name: ``processId``
         :refid: web-navigation-on-committed-details-process-id
         :refname: processId
         :type: (integer) **Unsupported.**

         The ID of the process runs the renderer for this tab.

      .. _web^navigation.on^committed.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-on-committed-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the navigation occurs.

      .. _web^navigation.on^committed.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-navigation-on-committed-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when the navigation was committed, in milliseconds since the epoch.

      .. _web^navigation.on^committed.details.transition^qualifiers:

      .. api-member::
         :name: ``transitionQualifiers``
         :refid: web-navigation-on-committed-details-transition-qualifiers
         :refname: transitionQualifiers
         :type: (array of :ref:`web^navigation.^transition^qualifier`)

         A list of transition qualifiers.

      .. _web^navigation.on^committed.details.transition^type:

      .. api-member::
         :name: ``transitionType``
         :refid: web-navigation-on-committed-details-transition-type
         :refname: transitionType
         :type: (:ref:`web^navigation.^transition^type`)

         Cause of the navigation.

      .. _web^navigation.on^committed.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-navigation-on-committed-details-url
         :refname: url
         :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`webNavigation`

.. _web^navigation.on^completed:

onCompleted
-----------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when a document, including the resources it refers to, is completely loaded and initialized.

.. note::

   Filtering is supported from version 50.

.. note::

   If the filter parameter is empty, Thunderbird raises an exception.

.. api-header::
   :label: Parameters for onCompleted.addListener(listener, filters)

   .. _web^navigation.on^completed.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-navigation-on-completed-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^navigation.on^completed.filters:

   .. api-member::
      :name: [``filters``]
      :refid: web-navigation-on-completed-filters
      :refname: filters
      :type: (:ref:`web^navigation.^event^url^filters`, optional)

      Conditions that the URL being navigated to must satisfy. The 'schemes' and 'ports' fields of UrlFilter are ignored for this event.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^navigation.on^completed.details:

   .. api-member::
      :name: ``details``
      :refid: web-navigation-on-completed-details
      :refname: details
      :type: (object)

      .. _web^navigation.on^completed.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-navigation-on-completed-details-frame-id
         :refname: frameId
         :type: (integer)

         0 indicates the navigation happens in the tab content window; a positive value indicates navigation in a subframe. Frame IDs are unique within a tab.

      .. _web^navigation.on^completed.details.process^id:

      .. api-member::
         :name: ``processId``
         :refid: web-navigation-on-completed-details-process-id
         :refname: processId
         :type: (integer) **Unsupported.**

         The ID of the process runs the renderer for this tab.

      .. _web^navigation.on^completed.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-on-completed-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the navigation occurs.

      .. _web^navigation.on^completed.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-navigation-on-completed-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when the document finished loading, in milliseconds since the epoch.

      .. _web^navigation.on^completed.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-navigation-on-completed-details-url
         :refname: url
         :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`webNavigation`

.. _web^navigation.on^created^navigation^target:

onCreatedNavigationTarget
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 54]

Fired when a new window, or a new tab in an existing window, is created to host a navigation.

.. note::

   If the filter parameter is empty, Thunderbird raises an exception.

.. note::

   If a blocked popup is unblocked by the user, the event is then sent.

.. api-header::
   :label: Parameters for onCreatedNavigationTarget.addListener(listener, filters)

   .. _web^navigation.on^created^navigation^target.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-navigation-on-created-navigation-target-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^navigation.on^created^navigation^target.filters:

   .. api-member::
      :name: [``filters``]
      :refid: web-navigation-on-created-navigation-target-filters
      :refname: filters
      :type: (:ref:`web^navigation.^event^url^filters`, optional)

      Conditions that the URL being navigated to must satisfy. The 'schemes' and 'ports' fields of UrlFilter are ignored for this event.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^navigation.on^created^navigation^target.details:

   .. api-member::
      :name: ``details``
      :refid: web-navigation-on-created-navigation-target-details
      :refname: details
      :type: (object)

      .. _web^navigation.on^created^navigation^target.details.source^frame^id:

      .. api-member::
         :name: ``sourceFrameId``
         :refid: web-navigation-on-created-navigation-target-details-source-frame-id
         :refname: sourceFrameId
         :type: (integer)

         The ID of the frame with sourceTabId in which the navigation is triggered. 0 indicates the main frame.

      .. _web^navigation.on^created^navigation^target.details.source^process^id:

      .. api-member::
         :name: ``sourceProcessId``
         :refid: web-navigation-on-created-navigation-target-details-source-process-id
         :refname: sourceProcessId
         :type: (integer)

         The ID of the process runs the renderer for the source tab.

      .. _web^navigation.on^created^navigation^target.details.source^tab^id:

      .. api-member::
         :name: ``sourceTabId``
         :refid: web-navigation-on-created-navigation-target-details-source-tab-id
         :refname: sourceTabId
         :type: (integer)

         The ID of the tab in which the navigation is triggered.

      .. _web^navigation.on^created^navigation^target.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-on-created-navigation-target-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the url is opened

      .. _web^navigation.on^created^navigation^target.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-navigation-on-created-navigation-target-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when the browser was about to create a new view, in milliseconds since the epoch.

      .. _web^navigation.on^created^navigation^target.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-navigation-on-created-navigation-target-details-url
         :refname: url
         :type: (string)

         The URL to be opened in the new window.

.. api-header::
   :label: Required permissions

   - :permission:`webNavigation`

.. _web^navigation.on^d^o^m^content^loaded:

onDOMContentLoaded
------------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when the page's DOM is fully constructed, but the referenced resources may not finish loading.

.. note::

   Filtering is supported from version 50.

.. note::

   If the filter parameter is empty, Thunderbird raises an exception.

.. api-header::
   :label: Parameters for onDOMContentLoaded.addListener(listener, filters)

   .. _web^navigation.on^d^o^m^content^loaded.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-navigation-on-d-o-m-content-loaded-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^navigation.on^d^o^m^content^loaded.filters:

   .. api-member::
      :name: [``filters``]
      :refid: web-navigation-on-d-o-m-content-loaded-filters
      :refname: filters
      :type: (:ref:`web^navigation.^event^url^filters`, optional)

      Conditions that the URL being navigated to must satisfy. The 'schemes' and 'ports' fields of UrlFilter are ignored for this event.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^navigation.on^d^o^m^content^loaded.details:

   .. api-member::
      :name: ``details``
      :refid: web-navigation-on-d-o-m-content-loaded-details
      :refname: details
      :type: (object)

      .. _web^navigation.on^d^o^m^content^loaded.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-navigation-on-d-o-m-content-loaded-details-frame-id
         :refname: frameId
         :type: (integer)

         0 indicates the navigation happens in the tab content window; a positive value indicates navigation in a subframe. Frame IDs are unique within a tab.

      .. _web^navigation.on^d^o^m^content^loaded.details.process^id:

      .. api-member::
         :name: ``processId``
         :refid: web-navigation-on-d-o-m-content-loaded-details-process-id
         :refname: processId
         :type: (integer) **Unsupported.**

         The ID of the process runs the renderer for this tab.

      .. _web^navigation.on^d^o^m^content^loaded.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-on-d-o-m-content-loaded-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the navigation occurs.

      .. _web^navigation.on^d^o^m^content^loaded.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-navigation-on-d-o-m-content-loaded-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when the page's DOM was fully constructed, in milliseconds since the epoch.

      .. _web^navigation.on^d^o^m^content^loaded.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-navigation-on-d-o-m-content-loaded-details-url
         :refname: url
         :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`webNavigation`

.. _web^navigation.on^error^occurred:

onErrorOccurred
---------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when an error occurs and the navigation is aborted. This can happen if either a network error occurred, or the user aborted the navigation.

.. note::

   Filtering is supported from version 50.

.. note::

   If the filter parameter is empty, Thunderbird raises an exception.

.. api-header::
   :label: Parameters for onErrorOccurred.addListener(listener, filters)

   .. _web^navigation.on^error^occurred.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-navigation-on-error-occurred-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^navigation.on^error^occurred.filters:

   .. api-member::
      :name: [``filters``]
      :refid: web-navigation-on-error-occurred-filters
      :refname: filters
      :type: (:ref:`web^navigation.^event^url^filters`, optional)

      Conditions that the URL being navigated to must satisfy. The 'schemes' and 'ports' fields of UrlFilter are ignored for this event.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^navigation.on^error^occurred.details:

   .. api-member::
      :name: ``details``
      :refid: web-navigation-on-error-occurred-details
      :refname: details
      :type: (object)

      .. _web^navigation.on^error^occurred.details.error:

      .. api-member::
         :name: ``error``
         :refid: web-navigation-on-error-occurred-details-error
         :refname: error
         :type: (string) **Unsupported.**

         The error description.

      .. _web^navigation.on^error^occurred.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-navigation-on-error-occurred-details-frame-id
         :refname: frameId
         :type: (integer)

         0 indicates the navigation happens in the tab content window; a positive value indicates navigation in a subframe. Frame IDs are unique within a tab.

      .. _web^navigation.on^error^occurred.details.process^id:

      .. api-member::
         :name: ``processId``
         :refid: web-navigation-on-error-occurred-details-process-id
         :refname: processId
         :type: (integer) **Unsupported.**

         The ID of the process runs the renderer for this tab.

      .. _web^navigation.on^error^occurred.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-on-error-occurred-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the navigation occurs.

      .. _web^navigation.on^error^occurred.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-navigation-on-error-occurred-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when the error occurred, in milliseconds since the epoch.

      .. _web^navigation.on^error^occurred.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-navigation-on-error-occurred-details-url
         :refname: url
         :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`webNavigation`

.. _web^navigation.on^history^state^updated:

onHistoryStateUpdated
---------------------

.. api-section-annotation-hack:: -- [Added in TB 47]

Fired when the frame's history was updated to a new URL. All future events for that frame will use the updated URL.

.. api-header::
   :label: Parameters for onHistoryStateUpdated.addListener(listener, filters)

   .. _web^navigation.on^history^state^updated.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-navigation-on-history-state-updated-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^navigation.on^history^state^updated.filters:

   .. api-member::
      :name: [``filters``]
      :refid: web-navigation-on-history-state-updated-filters
      :refname: filters
      :type: (:ref:`web^navigation.^event^url^filters`, optional)

      Conditions that the URL being navigated to must satisfy. The 'schemes' and 'ports' fields of UrlFilter are ignored for this event.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^navigation.on^history^state^updated.details:

   .. api-member::
      :name: ``details``
      :refid: web-navigation-on-history-state-updated-details
      :refname: details
      :type: (object)

      .. _web^navigation.on^history^state^updated.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-navigation-on-history-state-updated-details-frame-id
         :refname: frameId
         :type: (integer)

         0 indicates the navigation happens in the tab content window; a positive value indicates navigation in a subframe. Frame IDs are unique within a tab.

      .. _web^navigation.on^history^state^updated.details.process^id:

      .. api-member::
         :name: ``processId``
         :refid: web-navigation-on-history-state-updated-details-process-id
         :refname: processId
         :type: (integer) **Unsupported.**

         The ID of the process runs the renderer for this tab.

      .. _web^navigation.on^history^state^updated.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-on-history-state-updated-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the navigation occurs.

      .. _web^navigation.on^history^state^updated.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-navigation-on-history-state-updated-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when the navigation was committed, in milliseconds since the epoch.

      .. _web^navigation.on^history^state^updated.details.transition^qualifiers:

      .. api-member::
         :name: ``transitionQualifiers``
         :refid: web-navigation-on-history-state-updated-details-transition-qualifiers
         :refname: transitionQualifiers
         :type: (array of :ref:`web^navigation.^transition^qualifier`)

         A list of transition qualifiers.

      .. _web^navigation.on^history^state^updated.details.transition^type:

      .. api-member::
         :name: ``transitionType``
         :refid: web-navigation-on-history-state-updated-details-transition-type
         :refname: transitionType
         :type: (:ref:`web^navigation.^transition^type`)

         Cause of the navigation.

      .. _web^navigation.on^history^state^updated.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-navigation-on-history-state-updated-details-url
         :refname: url
         :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`webNavigation`

.. _web^navigation.on^reference^fragment^updated:

onReferenceFragmentUpdated
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when the reference fragment of a frame was updated. All future events for that frame will use the updated URL.

.. note::

   Filtering is supported from version 50.

.. note::

   If the filter parameter is empty, Thunderbird raises an exception.

.. api-header::
   :label: Parameters for onReferenceFragmentUpdated.addListener(listener, filters)

   .. _web^navigation.on^reference^fragment^updated.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-navigation-on-reference-fragment-updated-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

   .. _web^navigation.on^reference^fragment^updated.filters:

   .. api-member::
      :name: [``filters``]
      :refid: web-navigation-on-reference-fragment-updated-filters
      :refname: filters
      :type: (:ref:`web^navigation.^event^url^filters`, optional)

      Conditions that the URL being navigated to must satisfy. The 'schemes' and 'ports' fields of UrlFilter are ignored for this event.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^navigation.on^reference^fragment^updated.details:

   .. api-member::
      :name: ``details``
      :refid: web-navigation-on-reference-fragment-updated-details
      :refname: details
      :type: (object)

      .. _web^navigation.on^reference^fragment^updated.details.frame^id:

      .. api-member::
         :name: ``frameId``
         :refid: web-navigation-on-reference-fragment-updated-details-frame-id
         :refname: frameId
         :type: (integer)

         0 indicates the navigation happens in the tab content window; a positive value indicates navigation in a subframe. Frame IDs are unique within a tab.

      .. _web^navigation.on^reference^fragment^updated.details.process^id:

      .. api-member::
         :name: ``processId``
         :refid: web-navigation-on-reference-fragment-updated-details-process-id
         :refname: processId
         :type: (integer) **Unsupported.**

         The ID of the process runs the renderer for this tab.

      .. _web^navigation.on^reference^fragment^updated.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-on-reference-fragment-updated-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab in which the navigation occurs.

      .. _web^navigation.on^reference^fragment^updated.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-navigation-on-reference-fragment-updated-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when the navigation was committed, in milliseconds since the epoch.

      .. _web^navigation.on^reference^fragment^updated.details.transition^qualifiers:

      .. api-member::
         :name: ``transitionQualifiers``
         :refid: web-navigation-on-reference-fragment-updated-details-transition-qualifiers
         :refname: transitionQualifiers
         :type: (array of :ref:`web^navigation.^transition^qualifier`)

         A list of transition qualifiers.

      .. _web^navigation.on^reference^fragment^updated.details.transition^type:

      .. api-member::
         :name: ``transitionType``
         :refid: web-navigation-on-reference-fragment-updated-details-transition-type
         :refname: transitionType
         :type: (:ref:`web^navigation.^transition^type`)

         Cause of the navigation.

      .. _web^navigation.on^reference^fragment^updated.details.url:

      .. api-member::
         :name: ``url``
         :refid: web-navigation-on-reference-fragment-updated-details-url
         :refname: url
         :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`webNavigation`

.. _web^navigation.on^tab^replaced:

onTabReplaced
-------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when the contents of the tab is replaced by a different (usually previously pre-rendered) tab.

.. note::

   Although you can add listeners for this event, it will never fire because the underlying functionality is not supported.

.. api-header::
   :label: Parameters for onTabReplaced.addListener(listener)

   .. _web^navigation.on^tab^replaced.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: web-navigation-on-tab-replaced-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _web^navigation.on^tab^replaced.details:

   .. api-member::
      :name: ``details``
      :refid: web-navigation-on-tab-replaced-details
      :refname: details
      :type: (object)

      .. _web^navigation.on^tab^replaced.details.replaced^tab^id:

      .. api-member::
         :name: ``replacedTabId``
         :refid: web-navigation-on-tab-replaced-details-replaced-tab-id
         :refname: replacedTabId
         :type: (integer)

         The ID of the tab that was replaced.

      .. _web^navigation.on^tab^replaced.details.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: web-navigation-on-tab-replaced-details-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab that replaced the old tab.

      .. _web^navigation.on^tab^replaced.details.time^stamp:

      .. api-member::
         :name: ``timeStamp``
         :refid: web-navigation-on-tab-replaced-details-time-stamp
         :refname: timeStamp
         :type: (number)

         The time when the replacement happened, in milliseconds since the epoch.

.. api-header::
   :label: Required permissions

   - :permission:`webNavigation`

.. rst-class:: api-main-section

Types
=====

.. _web^navigation.^event^url^filters:

EventUrlFilters
---------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _web^navigation.^event^url^filters.url:

   .. api-member::
      :name: ``url``
      :refid: web-navigation-event-url-filters-url
      :refname: url
      :type: (array of :ref:`web^navigation.^url^filter`)

.. _web^navigation.^transition^qualifier:

TransitionQualifier
-------------------

.. api-section-annotation-hack:: -- [Added in TB 48]

.. note::

   'server_redirect' is limited to top-level frames and 'client_redirect' is not supplied when redirections are created by JavaScript.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^navigation.^transition^qualifier.client_redirect:

         .. api-member::
            :name: :value:`client_redirect`
            :refid: web-navigation-transition-qualifier-client-redirect
            :refname: client_redirect

         .. _web^navigation.^transition^qualifier.forward_back:

         .. api-member::
            :name: :value:`forward_back`
            :refid: web-navigation-transition-qualifier-forward-back
            :refname: forward_back

         .. _web^navigation.^transition^qualifier.from_address_bar:

         .. api-member::
            :name: :value:`from_address_bar`
            :refid: web-navigation-transition-qualifier-from-address-bar
            :refname: from_address_bar
            :annotation: -- [Added in TB 49]

         .. _web^navigation.^transition^qualifier.server_redirect:

         .. api-member::
            :name: :value:`server_redirect`
            :refid: web-navigation-transition-qualifier-server-redirect
            :refname: server_redirect

.. _web^navigation.^transition^type:

TransitionType
--------------

.. api-section-annotation-hack:: -- [Added in TB 48]

Cause of the navigation. The same transition types as defined in the history API are used. These are the same transition types as defined in the history API except with :code:`"start_page"` in place of :code:`"auto_toplevel"` (for backwards compatibility).

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _web^navigation.^transition^type.auto_bookmark:

         .. api-member::
            :name: :value:`auto_bookmark`
            :refid: web-navigation-transition-type-auto-bookmark
            :refname: auto_bookmark
            :annotation: -- [Added in TB 49]

         .. _web^navigation.^transition^type.auto_subframe:

         .. api-member::
            :name: :value:`auto_subframe`
            :refid: web-navigation-transition-type-auto-subframe
            :refname: auto_subframe

            .. note::

               Partially supported as the default transition type for subframes.

         .. _web^navigation.^transition^type.form_submit:

         .. api-member::
            :name: :value:`form_submit`
            :refid: web-navigation-transition-type-form-submit
            :refname: form_submit

         .. _web^navigation.^transition^type.generated:

         .. api-member::
            :name: :value:`generated`
            :refid: web-navigation-transition-type-generated
            :refname: generated
            :annotation: -- [Added in TB 49]

         .. _web^navigation.^transition^type.keyword:

         .. api-member::
            :name: :value:`keyword`
            :refid: web-navigation-transition-type-keyword
            :refname: keyword
            :annotation: -- [Added in TB 49]

         .. _web^navigation.^transition^type.keyword_generated:

         .. api-member::
            :name: :value:`keyword_generated`
            :refid: web-navigation-transition-type-keyword-generated
            :refname: keyword_generated

         .. _web^navigation.^transition^type.link:

         .. api-member::
            :name: :value:`link`
            :refid: web-navigation-transition-type-link
            :refname: link

            .. note::

               Partially supported as the default transition type for top-level frames.

         .. _web^navigation.^transition^type.manual_subframe:

         .. api-member::
            :name: :value:`manual_subframe`
            :refid: web-navigation-transition-type-manual-subframe
            :refname: manual_subframe

         .. _web^navigation.^transition^type.reload:

         .. api-member::
            :name: :value:`reload`
            :refid: web-navigation-transition-type-reload
            :refname: reload

         .. _web^navigation.^transition^type.start_page:

         .. api-member::
            :name: :value:`start_page`
            :refid: web-navigation-transition-type-start-page
            :refname: start_page

         .. _web^navigation.^transition^type.typed:

         .. api-member::
            :name: :value:`typed`
            :refid: web-navigation-transition-type-typed
            :refname: typed
            :annotation: -- [Added in TB 49]

.. _web^navigation.^url^filter:

UrlFilter
---------

.. api-section-annotation-hack:: -- [Added in TB 50]

Filters URLs for various criteria. See `event filtering <events#filtered>`__. All criteria are case sensitive.

.. api-header::
   :label: object

   .. _web^navigation.^url^filter.host^contains:

   .. api-member::
      :name: [``hostContains``]
      :refid: web-navigation-url-filter-host-contains
      :refname: hostContains
      :type: (string, optional)

      Matches if the host name of the URL contains a specified string. To test whether a host name component has a prefix 'foo', use hostContains: '.foo'. This matches 'www.foobar.com' and 'foo.com', because an implicit dot is added at the beginning of the host name. Similarly, hostContains can be used to match against component suffix ('foo.') and to exactly match against components ('.foo.'). Suffix- and exact-matching for the last components need to be done separately using hostSuffix, because no implicit dot is added at the end of the host name.

   .. _web^navigation.^url^filter.host^equals:

   .. api-member::
      :name: [``hostEquals``]
      :refid: web-navigation-url-filter-host-equals
      :refname: hostEquals
      :type: (string, optional)

      Matches if the host name of the URL is equal to a specified string.

   .. _web^navigation.^url^filter.host^prefix:

   .. api-member::
      :name: [``hostPrefix``]
      :refid: web-navigation-url-filter-host-prefix
      :refname: hostPrefix
      :type: (string, optional)

      Matches if the host name of the URL starts with a specified string.

   .. _web^navigation.^url^filter.host^suffix:

   .. api-member::
      :name: [``hostSuffix``]
      :refid: web-navigation-url-filter-host-suffix
      :refname: hostSuffix
      :type: (string, optional)

      Matches if the host name of the URL ends with a specified string.

   .. _web^navigation.^url^filter.origin^and^path^matches:

   .. api-member::
      :name: [``originAndPathMatches``]
      :refid: web-navigation-url-filter-origin-and-path-matches
      :refname: originAndPathMatches
      :type: (string, optional)

      Matches if the URL without query segment and fragment identifier matches a specified regular expression. Port numbers are stripped from the URL if they match the default port number. The regular expressions use the `RE2 syntax <https://github.com/google/re2/blob/master/doc/syntax.txt>`__.

   .. _web^navigation.^url^filter.path^contains:

   .. api-member::
      :name: [``pathContains``]
      :refid: web-navigation-url-filter-path-contains
      :refname: pathContains
      :type: (string, optional)

      Matches if the path segment of the URL contains a specified string.

   .. _web^navigation.^url^filter.path^equals:

   .. api-member::
      :name: [``pathEquals``]
      :refid: web-navigation-url-filter-path-equals
      :refname: pathEquals
      :type: (string, optional)

      Matches if the path segment of the URL is equal to a specified string.

   .. _web^navigation.^url^filter.path^prefix:

   .. api-member::
      :name: [``pathPrefix``]
      :refid: web-navigation-url-filter-path-prefix
      :refname: pathPrefix
      :type: (string, optional)

      Matches if the path segment of the URL starts with a specified string.

   .. _web^navigation.^url^filter.path^suffix:

   .. api-member::
      :name: [``pathSuffix``]
      :refid: web-navigation-url-filter-path-suffix
      :refname: pathSuffix
      :type: (string, optional)

      Matches if the path segment of the URL ends with a specified string.

   .. _web^navigation.^url^filter.ports:

   .. api-member::
      :name: [``ports``]
      :refid: web-navigation-url-filter-ports
      :refname: ports
      :type: (array of integer or array of integer, optional)

      Matches if the port of the URL is contained in any of the specified port lists. For example :code:`[80, 443, [1000, 1200]]` matches all requests on port 80, 443 and in the range 1000-1200.

   .. _web^navigation.^url^filter.query^contains:

   .. api-member::
      :name: [``queryContains``]
      :refid: web-navigation-url-filter-query-contains
      :refname: queryContains
      :type: (string, optional)

      Matches if the query segment of the URL contains a specified string.

   .. _web^navigation.^url^filter.query^equals:

   .. api-member::
      :name: [``queryEquals``]
      :refid: web-navigation-url-filter-query-equals
      :refname: queryEquals
      :type: (string, optional)

      Matches if the query segment of the URL is equal to a specified string.

   .. _web^navigation.^url^filter.query^prefix:

   .. api-member::
      :name: [``queryPrefix``]
      :refid: web-navigation-url-filter-query-prefix
      :refname: queryPrefix
      :type: (string, optional)

      Matches if the query segment of the URL starts with a specified string.

   .. _web^navigation.^url^filter.query^suffix:

   .. api-member::
      :name: [``querySuffix``]
      :refid: web-navigation-url-filter-query-suffix
      :refname: querySuffix
      :type: (string, optional)

      Matches if the query segment of the URL ends with a specified string.

   .. _web^navigation.^url^filter.schemes:

   .. api-member::
      :name: [``schemes``]
      :refid: web-navigation-url-filter-schemes
      :refname: schemes
      :type: (array of string, optional)

      Matches if the scheme of the URL is equal to any of the schemes specified in the array.

   .. _web^navigation.^url^filter.url^contains:

   .. api-member::
      :name: [``urlContains``]
      :refid: web-navigation-url-filter-url-contains
      :refname: urlContains
      :type: (string, optional)

      Matches if the URL (without fragment identifier) contains a specified string. Port numbers are stripped from the URL if they match the default port number.

   .. _web^navigation.^url^filter.url^equals:

   .. api-member::
      :name: [``urlEquals``]
      :refid: web-navigation-url-filter-url-equals
      :refname: urlEquals
      :type: (string, optional)

      Matches if the URL (without fragment identifier) is equal to a specified string. Port numbers are stripped from the URL if they match the default port number.

   .. _web^navigation.^url^filter.url^matches:

   .. api-member::
      :name: [``urlMatches``]
      :refid: web-navigation-url-filter-url-matches
      :refname: urlMatches
      :type: (string, optional)

      Matches if the URL (without fragment identifier) matches a specified regular expression. Port numbers are stripped from the URL if they match the default port number. The regular expressions use the `RE2 syntax <https://github.com/google/re2/blob/master/doc/syntax.txt>`__.

   .. _web^navigation.^url^filter.url^prefix:

   .. api-member::
      :name: [``urlPrefix``]
      :refid: web-navigation-url-filter-url-prefix
      :refname: urlPrefix
      :type: (string, optional)

      Matches if the URL (without fragment identifier) starts with a specified string. Port numbers are stripped from the URL if they match the default port number.

   .. _web^navigation.^url^filter.url^suffix:

   .. api-member::
      :name: [``urlSuffix``]
      :refid: web-navigation-url-filter-url-suffix
      :refname: urlSuffix
      :type: (string, optional)

      Matches if the URL (without fragment identifier) ends with a specified string. Port numbers are stripped from the URL if they match the default port number.
