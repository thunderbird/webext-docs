.. container:: sticky-sidebar

  ≡ runtime API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

===========
runtime API
===========

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The runtime API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/runtime>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.runtime` API to retrieve the background page, return details about the manifest, and listen for and respond to events in the app or extension lifecycle. You can also use this API to convert the relative path of URLs to fully-qualified URLs.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _runtime.permission.native^messaging:

.. api-member::
   :name: :permission:`nativeMessaging`
   :refid: runtime-permission-native-messaging
   :refname: nativeMessaging

   Exchange messages with programs other than Thunderbird.

.. _runtime.permission.user^scripts:

.. api-member::
   :name: :permission:`userScripts`
   :refid: runtime-permission-user-scripts
   :refname: userScripts

   Allow unverified third-party scripts to access your data.

.. rst-class:: api-main-section

Functions
=========

.. _runtime.connect:

connect([extensionId], [connectInfo])
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Attempts to connect to connect listeners within an extension/app (such as the background page), or other extensions/apps. This is useful for content scripts connecting to their extension processes, inter-app/extension communication, and web messaging. Note that this does not connect to any listeners in a content script. Extensions may connect to content scripts embedded in tabs via :ref:`tabs.connect`.

.. api-header::
   :label: Parameters

   .. _runtime.connect.extension^id:

   .. api-member::
      :name: [``extensionId``]
      :refid: runtime-connect-extension-id
      :refname: extensionId
      :type: (string, optional)

      The ID of the extension or app to connect to. If omitted, a connection will be attempted with your own extension. Required if sending messages from a web page for web messaging.

   .. _runtime.connect.connect^info:

   .. api-member::
      :name: [``connectInfo``]
      :refid: runtime-connect-connect-info
      :refname: connectInfo
      :type: (object, optional)

      .. _runtime.connect.connect^info.include^tls^channel^id:

      .. api-member::
         :name: [``includeTlsChannelId``]
         :refid: runtime-connect-connect-info-include-tls-channel-id
         :refname: includeTlsChannelId
         :type: (boolean, optional)

         Whether the TLS channel ID will be passed into onConnectExternal for processes that are listening for the connection event.

      .. _runtime.connect.connect^info.name:

      .. api-member::
         :name: [``name``]
         :refid: runtime-connect-connect-info-name
         :refname: name
         :type: (string, optional)

         Will be passed into onConnect for processes that are listening for the connection event.

.. api-header::
   :label: Return type (`Promise`_)

   .. _runtime.connect.returns:

   .. api-member::
      :refid: runtime-connect-returns
      :refname: _returns
      :type: :ref:`runtime.^port`

      Port through which messages can be sent and received. The port's :ref:`runtime.^port on^disconnect` event is fired if the extension/app does not exist.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.connect^native:

connectNative(application)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Connects to a native application in the host machine.

.. api-header::
   :label: Parameters

   .. _runtime.connect^native.application:

   .. api-member::
      :name: ``application``
      :refid: runtime-connect-native-application
      :refname: application
      :type: (string)

      The name of the registered application to connect to.

.. api-header::
   :label: Return type (`Promise`_)

   .. _runtime.connect^native.returns:

   .. api-member::
      :refid: runtime-connect-native-returns
      :refname: _returns
      :type: :ref:`runtime.^port`

      Port through which messages can be sent and received with the application

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`nativeMessaging`

.. _runtime.get^background^page:

getBackgroundPage()
-------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Retrieves the JavaScript 'window' object for the background page running inside the current extension/app. If the background page is an event page, the system will ensure it is loaded before calling the callback. If there is no background page, an error is set.

.. note::

   If this is called from a page that is part of a private browsing window, such as a sidebar in a private window or a popup opened from a private window, then it will always return :code:`null`.

.. api-header::
   :label: Return type (`Promise`_)

   .. _runtime.get^background^page.returns:

   .. api-member::
      :refid: runtime-get-background-page-returns
      :refname: _returns
      :type: `Window <https://developer.mozilla.org/en-US/docs/Web/API/Window>`__

      The JavaScript 'window' object for the background page.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.get^browser^info:

getBrowserInfo()
----------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Returns information about the current browser.

.. api-header::
   :label: Return type (`Promise`_)

   .. _runtime.get^browser^info.returns:

   .. api-member::
      :refid: runtime-get-browser-info-returns
      :refname: _returns
      :type: :ref:`runtime.^browser^info`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.get^contexts:

getContexts(filter)
-------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Fetches information about active contexts associated with this extension

.. api-header::
   :label: Parameters

   .. _runtime.get^contexts.filter:

   .. api-member::
      :name: ``filter``
      :refid: runtime-get-contexts-filter
      :refname: filter
      :type: (:ref:`runtime.^context^filter`)

      A filter to find matching context.

.. api-header::
   :label: Return type (`Promise`_)

   .. _runtime.get^contexts.returns:

   .. api-member::
      :refid: runtime-get-contexts-returns
      :refname: _returns
      :type: array of :ref:`runtime.^extension^context`

      The matching contexts, if any.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.get^frame^id:

getFrameId(target)
------------------

.. api-section-annotation-hack:: -- [Added in TB 102.0]

Get the frameId of any window global or frame element.

.. api-header::
   :label: Parameters

   .. _runtime.get^frame^id.target:

   .. api-member::
      :name: ``target``
      :refid: runtime-get-frame-id-target
      :refname: target
      :type: (any)

      A WindowProxy or a Browsing Context container element (IFrame, Frame, Embed, Object) for the target frame.

.. api-header::
   :label: Return type (`Promise`_)

   .. _runtime.get^frame^id.returns:

   .. api-member::
      :refid: runtime-get-frame-id-returns
      :refname: _returns
      :type: number

      The frameId of the target frame, or -1 if it doesn't exist.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.get^manifest:

getManifest()
-------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Returns details about the app or extension from the manifest. The object returned is a serialization of the full manifest file.

.. note::

   Returns null for missing values, and removes unsupported keys.

.. api-header::
   :label: Return type (`Promise`_)

   .. _runtime.get^manifest.returns:

   .. api-member::
      :refid: runtime-get-manifest-returns
      :refname: _returns
      :type: object

      The manifest details.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.get^platform^info:

getPlatformInfo()
-----------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Returns information about the current platform.

.. api-header::
   :label: Return type (`Promise`_)

   .. _runtime.get^platform^info.returns:

   .. api-member::
      :refid: runtime-get-platform-info-returns
      :refname: _returns
      :type: :ref:`runtime.^platform^info`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.get^u^r^l:

getURL(path)
------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Converts a relative path within an app/extension install directory to a fully-qualified URL.

.. api-header::
   :label: Parameters

   .. _runtime.get^u^r^l.path:

   .. api-member::
      :name: ``path``
      :refid: runtime-get-u-r-l-path
      :refname: path
      :type: (string)

      A path to a resource within an app/extension expressed relative to its install directory.

.. api-header::
   :label: Return type (`Promise`_)

   .. _runtime.get^u^r^l.returns:

   .. api-member::
      :refid: runtime-get-u-r-l-returns
      :refname: _returns
      :type: string

      The fully-qualified URL to the resource.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.open^options^page:

openOptionsPage()
-----------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Open your Extension's options page, if possible.The precise behavior may depend on your manifest's :code:`options_ui` or :code:`options_page` key, or what the browser happens to support at the time.If your Extension does not declare an options page, or the browser failed to create one for some other reason, the callback will set :ref:`runtime.last^error`.

.. _runtime.reload:

reload()
--------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Reloads the app or extension.

.. _runtime.restart:

restart()
---------

.. api-section-annotation-hack:: 

Restart the device when the app runs in kiosk mode. Otherwise, it's no-op.

.. _runtime.send^message:

sendMessage([extensionId], message, [options])
----------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Sends a single message to event listeners within your extension/app or a different extension/app. Similar to :ref:`runtime.connect` but only sends a single message, with an optional response. If sending to your extension, the :ref:`runtime.on^message` event will be fired in each page, or :ref:`runtime.on^message^external`, if a different extension. Note that extensions cannot send messages to content scripts using this method. To send messages to content scripts, use :ref:`tabs.send^message`.

.. api-header::
   :label: Parameters

   .. _runtime.send^message.extension^id:

   .. api-member::
      :name: [``extensionId``]
      :refid: runtime-send-message-extension-id
      :refname: extensionId
      :type: (string, optional)

      The ID of the extension/app to send the message to. If omitted, the message will be sent to your own extension/app. Required if sending messages from a web page for web messaging.

   .. _runtime.send^message.message:

   .. api-member::
      :name: ``message``
      :refid: runtime-send-message-message
      :refname: message
      :type: (any)

   .. _runtime.send^message.options:

   .. api-member::
      :name: [``options``]
      :refid: runtime-send-message-options
      :refname: options
      :type: (object, optional)

      .. _runtime.send^message.options.include^tls^channel^id:

      .. api-member::
         :name: [``includeTlsChannelId``]
         :refid: runtime-send-message-options-include-tls-channel-id
         :refname: includeTlsChannelId
         :type: (boolean, optional) **Unsupported.**

         Whether the TLS channel ID will be passed into onMessageExternal for processes that are listening for the connection event.

.. api-header::
   :label: Return type (`Promise`_)

   .. _runtime.send^message.returns:

   .. api-member::
      :refid: runtime-send-message-returns
      :refname: _returns
      :type: any

      The JSON response object sent by the handler of the message. If an error occurs while connecting to the extension, the callback will be called with no arguments and :ref:`runtime.last^error` will be set to the error message.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.send^native^message:

sendNativeMessage(application, message)
---------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Send a single message to a native application.

.. api-header::
   :label: Parameters

   .. _runtime.send^native^message.application:

   .. api-member::
      :name: ``application``
      :refid: runtime-send-native-message-application
      :refname: application
      :type: (string)

      The name of the native messaging host.

   .. _runtime.send^native^message.message:

   .. api-member::
      :name: ``message``
      :refid: runtime-send-native-message-message
      :refname: message
      :type: (any)

      The message that will be passed to the native messaging host.

.. api-header::
   :label: Return type (`Promise`_)

   .. _runtime.send^native^message.returns:

   .. api-member::
      :refid: runtime-send-native-message-returns
      :refname: _returns
      :type: any

      The response message sent by the native messaging host. If an error occurs while connecting to the native messaging host, the callback will be called with no arguments and :ref:`runtime.last^error` will be set to the error message.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`nativeMessaging`

.. _runtime.set^uninstall^u^r^l:

setUninstallURL([url])
----------------------

.. api-section-annotation-hack:: 

Sets the URL to be visited upon uninstallation. This may be used to clean up server-side data, do analytics, and implement surveys. Maximum 1023 characters.

.. api-header::
   :label: Parameters

   .. _runtime.set^uninstall^u^r^l.url:

   .. api-member::
      :name: [``url``]
      :refid: runtime-set-uninstall-u-r-l-url
      :refname: url
      :type: (string, optional)

      URL to be opened after the extension is uninstalled. This URL must have an http: or https: scheme. Set an empty string to not open a new tab upon uninstallation.

.. rst-class:: api-main-section

Events
======

.. _runtime.on^connect:

onConnect
---------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when a connection is made from either an extension process or a content script.

.. api-header::
   :label: Parameters for onConnect.addListener(listener)

   .. _runtime.on^connect.listener(port):

   .. api-member::
      :name: ``listener(port)``
      :refid: runtime-on-connect-listener-port
      :refname: listener(port)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _runtime.on^connect.port:

   .. api-member::
      :name: ``port``
      :refid: runtime-on-connect-port
      :refname: port
      :type: (:ref:`runtime.^port`)

.. _runtime.on^connect^external:

onConnectExternal
-----------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when a connection is made from another extension.

.. api-header::
   :label: Parameters for onConnectExternal.addListener(listener)

   .. _runtime.on^connect^external.listener(port):

   .. api-member::
      :name: ``listener(port)``
      :refid: runtime-on-connect-external-listener-port
      :refname: listener(port)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _runtime.on^connect^external.port:

   .. api-member::
      :name: ``port``
      :refid: runtime-on-connect-external-port
      :refname: port
      :type: (:ref:`runtime.^port`)

.. _runtime.on^installed:

onInstalled
-----------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when the extension is first installed, when the extension is updated to a new version, and when the browser is updated to a new version.

.. note::

   Before version 55, this event is not triggered for temporarily installed add-ons.

.. api-header::
   :label: Parameters for onInstalled.addListener(listener)

   .. _runtime.on^installed.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: runtime-on-installed-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _runtime.on^installed.details:

   .. api-member::
      :name: ``details``
      :refid: runtime-on-installed-details
      :refname: details
      :type: (object)

      .. _runtime.on^installed.details.reason:

      .. api-member::
         :name: ``reason``
         :refid: runtime-on-installed-details-reason
         :refname: reason
         :type: (:ref:`runtime.^on^installed^reason`)

         The reason that this event is being dispatched.

      .. _runtime.on^installed.details.temporary:

      .. api-member::
         :name: ``temporary``
         :refid: runtime-on-installed-details-temporary
         :refname: temporary
         :type: (boolean)

         Indicates whether the addon is installed as a temporary extension.

      .. _runtime.on^installed.details.id:

      .. api-member::
         :name: [``id``]
         :refid: runtime-on-installed-details-id
         :refname: id
         :type: (string, optional) **Unsupported.**

         Indicates the ID of the imported shared module extension which updated. This is present only if 'reason' is 'shared_module_update'.

      .. _runtime.on^installed.details.previous^version:

      .. api-member::
         :name: [``previousVersion``]
         :refid: runtime-on-installed-details-previous-version
         :refname: previousVersion
         :type: (string, optional)

         Indicates the previous version of the extension, which has just been updated. This is present only if 'reason' is 'update'.

.. _runtime.on^message:

onMessage
---------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when a message is sent from either an extension process or a content script.

.. api-header::
   :label: Parameters for onMessage.addListener(listener)

   .. _runtime.on^message.listener(message, sender, send^response):

   .. api-member::
      :name: ``listener(message, sender, sendResponse)``
      :refid: runtime-on-message-listener-message-sender-send-response
      :refname: listener(message, sender, sendResponse)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _runtime.on^message.message:

   .. api-member::
      :name: [``message``]
      :refid: runtime-on-message-message
      :refname: message
      :type: (any, optional)

      The message sent by the calling script.

   .. _runtime.on^message.sender:

   .. api-member::
      :name: ``sender``
      :refid: runtime-on-message-sender
      :refname: sender
      :type: (:ref:`runtime.^message^sender`)

   .. _runtime.on^message.send^response:

   .. api-member::
      :name: ``sendResponse``
      :refid: runtime-on-message-send-response
      :refname: sendResponse
      :type: (function)

      Function to call (at most once) when you have a response. The argument should be any JSON-ifiable object. If you have more than one :code:`onMessage` listener in the same document, then only one may send a response. This function becomes invalid when the event listener returns, unless you return true from the event listener to indicate you wish to send a response asynchronously (this will keep the message channel open to the other end until :code:`sendResponse` is called).

.. api-header::
   :label: Expected return value of the listener function

   .. _runtime.on^message.returns:

   .. api-member::
      :refid: runtime-on-message-returns
      :type: boolean

      Return true from the event listener if you wish to call :code:`sendResponse` after the event listener returns.

.. _runtime.on^message^external:

onMessageExternal
-----------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when a message is sent from another extension/app. Cannot be used in a content script.

.. api-header::
   :label: Parameters for onMessageExternal.addListener(listener)

   .. _runtime.on^message^external.listener(message, sender, send^response):

   .. api-member::
      :name: ``listener(message, sender, sendResponse)``
      :refid: runtime-on-message-external-listener-message-sender-send-response
      :refname: listener(message, sender, sendResponse)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _runtime.on^message^external.message:

   .. api-member::
      :name: [``message``]
      :refid: runtime-on-message-external-message
      :refname: message
      :type: (any, optional)

      The message sent by the calling script.

   .. _runtime.on^message^external.sender:

   .. api-member::
      :name: ``sender``
      :refid: runtime-on-message-external-sender
      :refname: sender
      :type: (:ref:`runtime.^message^sender`)

   .. _runtime.on^message^external.send^response:

   .. api-member::
      :name: ``sendResponse``
      :refid: runtime-on-message-external-send-response
      :refname: sendResponse
      :type: (function)

      Function to call (at most once) when you have a response. The argument should be any JSON-ifiable object. If you have more than one :code:`onMessage` listener in the same document, then only one may send a response. This function becomes invalid when the event listener returns, unless you return true from the event listener to indicate you wish to send a response asynchronously (this will keep the message channel open to the other end until :code:`sendResponse` is called).

.. api-header::
   :label: Expected return value of the listener function

   .. _runtime.on^message^external.returns:

   .. api-member::
      :refid: runtime-on-message-external-returns
      :type: boolean

      Return true from the event listener if you wish to call :code:`sendResponse` after the event listener returns.

.. _runtime.on^performance^warning:

onPerformanceWarning
--------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Fired when a runtime performance issue is detected with the extension. Observe this event to be proactively notified of runtime performance problems with the extension.

.. api-header::
   :label: Parameters for onPerformanceWarning.addListener(listener)

   .. _runtime.on^performance^warning.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: runtime-on-performance-warning-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _runtime.on^performance^warning.details:

   .. api-member::
      :name: ``details``
      :refid: runtime-on-performance-warning-details
      :refname: details
      :type: (object)

      .. _runtime.on^performance^warning.details.category:

      .. api-member::
         :name: ``category``
         :refid: runtime-on-performance-warning-details-category
         :refname: category
         :type: (:ref:`runtime.^on^performance^warning^category`)

         The performance warning event category, e.g. 'content_script'.

      .. _runtime.on^performance^warning.details.description:

      .. api-member::
         :name: ``description``
         :refid: runtime-on-performance-warning-details-description
         :refname: description
         :type: (string)

         An explanation of what the warning means, and hopefully how to address it.

      .. _runtime.on^performance^warning.details.severity:

      .. api-member::
         :name: ``severity``
         :refid: runtime-on-performance-warning-details-severity
         :refname: severity
         :type: (:ref:`runtime.^on^performance^warning^severity`)

         The performance warning event severity, e.g. 'high'.

      .. _runtime.on^performance^warning.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: runtime-on-performance-warning-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         The :ref:`tabs.^tab` that the performance warning relates to, if any.

.. _runtime.on^startup:

onStartup
---------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when a profile that has this extension installed first starts up. This event is not fired for incognito profiles.

.. api-header::
   :label: Parameters for onStartup.addListener(listener)

   .. _runtime.on^startup.listener():

   .. api-member::
      :name: ``listener()``
      :refid: runtime-on-startup-listener
      :refname: listener()

      A function that will be called when this event occurs.

.. _runtime.on^suspend:

onSuspend
---------

.. api-section-annotation-hack:: -- [Added in TB 102.0]

Sent to the event page just before it is unloaded. This gives the extension opportunity to do some clean up. Note that since the page is unloading, any asynchronous operations started while handling this event are not guaranteed to complete. If more activity for the event page occurs before it gets unloaded the onSuspendCanceled event will be sent and the page won't be unloaded.

.. note::

   This event does not fire until Thunderbird 106, when event pages are available.

.. api-header::
   :label: Parameters for onSuspend.addListener(listener)

   .. _runtime.on^suspend.listener():

   .. api-member::
      :name: ``listener()``
      :refid: runtime-on-suspend-listener
      :refname: listener()

      A function that will be called when this event occurs.

.. _runtime.on^suspend^canceled:

onSuspendCanceled
-----------------

.. api-section-annotation-hack:: -- [Added in TB 102.0]

Sent after onSuspend to indicate that the app won't be unloaded after all.

.. note::

   This event does not fire until Thunderbird 106, when event pages are available.

.. api-header::
   :label: Parameters for onSuspendCanceled.addListener(listener)

   .. _runtime.on^suspend^canceled.listener():

   .. api-member::
      :name: ``listener()``
      :refid: runtime-on-suspend-canceled-listener
      :refname: listener()

      A function that will be called when this event occurs.

.. _runtime.on^update^available:

onUpdateAvailable
-----------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when an update is available, but isn't installed immediately because the app is currently running. If you do nothing, the update will be installed the next time the background page gets unloaded, if you want it to be installed sooner you can explicitly call :ref:`runtime.reload`. If your extension is using a persistent background page, the background page of course never gets unloaded, so unless you call :ref:`runtime.reload` manually in response to this event the update will not get installed until the next time the browser itself restarts. If no handlers are listening for this event, and your extension has a persistent background page, it behaves as if :ref:`runtime.reload` is called in response to this event.

.. api-header::
   :label: Parameters for onUpdateAvailable.addListener(listener)

   .. _runtime.on^update^available.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: runtime-on-update-available-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _runtime.on^update^available.details:

   .. api-member::
      :name: ``details``
      :refid: runtime-on-update-available-details
      :refname: details
      :type: (object)

      The manifest details of the available update.

      .. _runtime.on^update^available.details.version:

      .. api-member::
         :name: ``version``
         :refid: runtime-on-update-available-details-version
         :refname: version
         :type: (string)

         The version number of the available update.

.. _runtime.on^user^script^connect:

onUserScriptConnect
-------------------

.. api-section-annotation-hack:: -- [Added in TB 140.0]

Fired when a connection is made from a USER_SCRIPT world registered through the userScripts API.

.. note::

   Available for use with Manifest V3 only.

.. note::

   Requires the `userScripts permission <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/userScripts#permissions>`__.

.. api-header::
   :label: Parameters for onUserScriptConnect.addListener(listener)

   .. _runtime.on^user^script^connect.listener(port):

   .. api-member::
      :name: ``listener(port)``
      :refid: runtime-on-user-script-connect-listener-port
      :refname: listener(port)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _runtime.on^user^script^connect.port:

   .. api-member::
      :name: ``port``
      :refid: runtime-on-user-script-connect-port
      :refname: port
      :type: (:ref:`runtime.^port`)

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _runtime.on^user^script^message:

onUserScriptMessage
-------------------

.. api-section-annotation-hack:: -- [Added in TB 140.0]

Fired when a message is sent from a USER_SCRIPT world registered through the userScripts API.

.. note::

   Available for use with Manifest V3 only.

.. note::

   Requires the `userScripts permission <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/userScripts#permissions>`__.

.. api-header::
   :label: Parameters for onUserScriptMessage.addListener(listener)

   .. _runtime.on^user^script^message.listener(message, sender, send^response):

   .. api-member::
      :name: ``listener(message, sender, sendResponse)``
      :refid: runtime-on-user-script-message-listener-message-sender-send-response
      :refname: listener(message, sender, sendResponse)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _runtime.on^user^script^message.message:

   .. api-member::
      :name: [``message``]
      :refid: runtime-on-user-script-message-message
      :refname: message
      :type: (any, optional)

      The message sent by the calling script.

   .. _runtime.on^user^script^message.sender:

   .. api-member::
      :name: ``sender``
      :refid: runtime-on-user-script-message-sender
      :refname: sender
      :type: (:ref:`runtime.^message^sender`)

   .. _runtime.on^user^script^message.send^response:

   .. api-member::
      :name: ``sendResponse``
      :refid: runtime-on-user-script-message-send-response
      :refname: sendResponse
      :type: (function)

      Function to call (at most once) when you have a response. The argument should be any JSON-ifiable object. If you have more than one :code:`onMessage` listener in the same document, then only one may send a response. This function becomes invalid when the event listener returns, unless you return true from the event listener to indicate you wish to send a response asynchronously (this will keep the message channel open to the other end until :code:`sendResponse` is called).

.. api-header::
   :label: Expected return value of the listener function

   .. _runtime.on^user^script^message.returns:

   .. api-member::
      :refid: runtime-on-user-script-message-returns
      :type: boolean

      Return true from the event listener if you wish to call :code:`sendResponse` after the event listener returns.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. rst-class:: api-main-section

Types
=====

.. _runtime.^browser^info:

BrowserInfo
-----------

.. api-section-annotation-hack:: 

An object containing information about the current browser.

.. api-header::
   :label: object

   .. _runtime.^browser^info.build^i^d:

   .. api-member::
      :name: ``buildID``
      :refid: runtime-browser-info-build-i-d
      :refname: buildID
      :type: (string)

      The browser's build ID/date, for example '20160101'.

   .. _runtime.^browser^info.name:

   .. api-member::
      :name: ``name``
      :refid: runtime-browser-info-name
      :refname: name
      :type: (string)

      The name of the browser, for example 'Thunderbird'.

   .. _runtime.^browser^info.vendor:

   .. api-member::
      :name: ``vendor``
      :refid: runtime-browser-info-vendor
      :refname: vendor
      :type: (string)

      The name of the browser vendor, for example 'Mozilla'.

   .. _runtime.^browser^info.version:

   .. api-member::
      :name: ``version``
      :refid: runtime-browser-info-version
      :refname: version
      :type: (string)

      The browser's version, for example '42.0.0' or '0.8.1pre'.

.. _runtime.^context^type:

ContextType
-----------

.. api-section-annotation-hack:: 

The type of extension view.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _runtime.^context^type.^b^a^c^k^g^r^o^u^n^d:

         .. api-member::
            :name: :value:`BACKGROUND`
            :refid: runtime-context-type-b-a-c-k-g-r-o-u-n-d
            :refname: BACKGROUND

         .. _runtime.^context^type.^p^o^p^u^p:

         .. api-member::
            :name: :value:`POPUP`
            :refid: runtime-context-type-p-o-p-u-p
            :refname: POPUP

         .. _runtime.^context^type.^s^i^d^e_^p^a^n^e^l:

         .. api-member::
            :name: :value:`SIDE_PANEL`
            :refid: runtime-context-type-s-i-d-e-p-a-n-e-l
            :refname: SIDE_PANEL

         .. _runtime.^context^type.^t^a^b:

         .. api-member::
            :name: :value:`TAB`
            :refid: runtime-context-type-t-a-b
            :refname: TAB

.. _runtime.^event:

Event
-----

.. api-section-annotation-hack:: -- [Added in TB ≤53]

An object which allows the addition and removal of listeners for a Chrome event.

.. api-header::
   :label: object

.. _runtime.^extension^context:

ExtensionContext
----------------

.. api-section-annotation-hack:: 

A context hosting extension content

.. api-header::
   :label: object

   .. _runtime.^extension^context.context^id:

   .. api-member::
      :name: ``contextId``
      :refid: runtime-extension-context-context-id
      :refname: contextId
      :type: (string)

      An unique identifier associated to this context

   .. _runtime.^extension^context.context^type:

   .. api-member::
      :name: ``contextType``
      :refid: runtime-extension-context-context-type
      :refname: contextType
      :type: (:ref:`runtime.^context^type`)

      The type of the context

   .. _runtime.^extension^context.frame^id:

   .. api-member::
      :name: ``frameId``
      :refid: runtime-extension-context-frame-id
      :refname: frameId
      :type: (integer)

      The frame ID for this context, or -1 if it is not hosted in a frame.

   .. _runtime.^extension^context.incognito:

   .. api-member::
      :name: ``incognito``
      :refid: runtime-extension-context-incognito
      :refname: incognito
      :type: (boolean)

      Whether the context is associated with an private browsing context.

   .. _runtime.^extension^context.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: runtime-extension-context-tab-id
      :refname: tabId
      :type: (integer)

      The tab ID for this context, or -1 if it is not hosted in a tab.

   .. _runtime.^extension^context.window^id:

   .. api-member::
      :name: ``windowId``
      :refid: runtime-extension-context-window-id
      :refname: windowId
      :type: (integer)

      The window ID for this context, or -1 if it is not hosted in a window.

   .. _runtime.^extension^context.document^id:

   .. api-member::
      :name: [``documentId``]
      :refid: runtime-extension-context-document-id
      :refname: documentId
      :type: (string, optional) **Unsupported.**

      An UUID for the document associated with this context, or undefined if it is not hosted in a document

   .. _runtime.^extension^context.document^origin:

   .. api-member::
      :name: [``documentOrigin``]
      :refid: runtime-extension-context-document-origin
      :refname: documentOrigin
      :type: (string, optional)

      The origin of the document associated with this context, or undefined if it is not hosted in a document

   .. _runtime.^extension^context.document^url:

   .. api-member::
      :name: [``documentUrl``]
      :refid: runtime-extension-context-document-url
      :refname: documentUrl
      :type: (string, optional)

      The URL of the document associated with this context, or undefined if it is not hosted in a document

.. _runtime.^message^sender:

MessageSender
-------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

An object containing information about the script context that sent a message or request.

.. note::

   Before version 54, 'id' was the add-on's internal UUID, not the add-on ID.

.. api-header::
   :label: object

   .. _runtime.^message^sender.frame^id:

   .. api-member::
      :name: [``frameId``]
      :refid: runtime-message-sender-frame-id
      :refname: frameId
      :type: (integer, optional)

      The frame that opened the connection. 0 for top-level frames, positive for child frames. This will only be set when :code:`tab` is set.

   .. _runtime.^message^sender.id:

   .. api-member::
      :name: [``id``]
      :refid: runtime-message-sender-id
      :refname: id
      :type: (string, optional)

      The ID of the extension or app that opened the connection, if any.

   .. _runtime.^message^sender.tab:

   .. api-member::
      :name: [``tab``]
      :refid: runtime-message-sender-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`, optional)

      The :ref:`tabs.^tab` which opened the connection, if any. This property will **only** be present when the connection was opened from a tab (including content scripts), and **only** if the receiver is an extension, not an app.

   .. _runtime.^message^sender.tls^channel^id:

   .. api-member::
      :name: [``tlsChannelId``]
      :refid: runtime-message-sender-tls-channel-id
      :refname: tlsChannelId
      :type: (string, optional) **Unsupported.**

      The TLS channel ID of the page or frame that opened the connection, if requested by the extension or app, and if available.

   .. _runtime.^message^sender.url:

   .. api-member::
      :name: [``url``]
      :refid: runtime-message-sender-url
      :refname: url
      :type: (string, optional)

      The URL of the page or frame that opened the connection. If the sender is in an iframe, it will be iframe's URL not the URL of the page which hosts it.

   .. _runtime.^message^sender.user^script^world^id:

   .. api-member::
      :name: [``userScriptWorldId``]
      :refid: runtime-message-sender-user-script-world-id
      :refname: userScriptWorldId
      :type: (string, optional)

      The worldId of the USER_SCRIPT world that sent the message. Only present on onUserScriptMessage and onUserScriptConnect (in port.sender) events.

.. _runtime.^on^installed^reason:

OnInstalledReason
-----------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

The reason that this event is being dispatched.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _runtime.^on^installed^reason.browser_update:

         .. api-member::
            :name: :value:`browser_update`
            :refid: runtime-on-installed-reason-browser-update
            :refname: browser_update

         .. _runtime.^on^installed^reason.install:

         .. api-member::
            :name: :value:`install`
            :refid: runtime-on-installed-reason-install
            :refname: install

         .. _runtime.^on^installed^reason.update:

         .. api-member::
            :name: :value:`update`
            :refid: runtime-on-installed-reason-update
            :refname: update

.. _runtime.^on^performance^warning^category:

OnPerformanceWarningCategory
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

The performance warning event category, e.g. 'content_script'.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _runtime.^on^performance^warning^category.content_script:

         .. api-member::
            :name: :value:`content_script`
            :refid: runtime-on-performance-warning-category-content-script
            :refname: content_script

.. _runtime.^on^performance^warning^severity:

OnPerformanceWarningSeverity
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

The performance warning event severity. Will be 'high' for serious and user-visible issues.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _runtime.^on^performance^warning^severity.high:

         .. api-member::
            :name: :value:`high`
            :refid: runtime-on-performance-warning-severity-high
            :refname: high

         .. _runtime.^on^performance^warning^severity.low:

         .. api-member::
            :name: :value:`low`
            :refid: runtime-on-performance-warning-severity-low
            :refname: low

         .. _runtime.^on^performance^warning^severity.medium:

         .. api-member::
            :name: :value:`medium`
            :refid: runtime-on-performance-warning-severity-medium
            :refname: medium

.. _runtime.^on^restart^required^reason:

OnRestartRequiredReason
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

The reason that the event is being dispatched. 'app_update' is used when the restart is needed because the application is updated to a newer version. 'os_update' is used when the restart is needed because the browser/OS is updated to a newer version. 'periodic' is used when the system runs for more than the permitted uptime set in the enterprise policy.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _runtime.^on^restart^required^reason.app_update:

         .. api-member::
            :name: :value:`app_update`
            :refid: runtime-on-restart-required-reason-app-update
            :refname: app_update

         .. _runtime.^on^restart^required^reason.os_update:

         .. api-member::
            :name: :value:`os_update`
            :refid: runtime-on-restart-required-reason-os-update
            :refname: os_update

         .. _runtime.^on^restart^required^reason.periodic:

         .. api-member::
            :name: :value:`periodic`
            :refid: runtime-on-restart-required-reason-periodic
            :refname: periodic

.. _runtime.^platform^arch:

PlatformArch
------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

The machine's processor architecture.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _runtime.^platform^arch.aarch64:

         .. api-member::
            :name: :value:`aarch64`
            :refid: runtime-platform-arch-aarch64
            :refname: aarch64

         .. _runtime.^platform^arch.arm:

         .. api-member::
            :name: :value:`arm`
            :refid: runtime-platform-arch-arm
            :refname: arm

         .. _runtime.^platform^arch.noarch:

         .. api-member::
            :name: :value:`noarch`
            :refid: runtime-platform-arch-noarch
            :refname: noarch

         .. _runtime.^platform^arch.ppc64:

         .. api-member::
            :name: :value:`ppc64`
            :refid: runtime-platform-arch-ppc64
            :refname: ppc64

         .. _runtime.^platform^arch.s390x:

         .. api-member::
            :name: :value:`s390x`
            :refid: runtime-platform-arch-s390x
            :refname: s390x

         .. _runtime.^platform^arch.sparc64:

         .. api-member::
            :name: :value:`sparc64`
            :refid: runtime-platform-arch-sparc64
            :refname: sparc64

         .. _runtime.^platform^arch.x86-32:

         .. api-member::
            :name: :value:`x86-32`
            :refid: runtime-platform-arch-x86-32
            :refname: x86-32

         .. _runtime.^platform^arch.x86-64:

         .. api-member::
            :name: :value:`x86-64`
            :refid: runtime-platform-arch-x86-64
            :refname: x86-64

.. _runtime.^platform^info:

PlatformInfo
------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

An object containing information about the current platform.

.. api-header::
   :label: object

   .. _runtime.^platform^info.arch:

   .. api-member::
      :name: ``arch``
      :refid: runtime-platform-info-arch
      :refname: arch
      :type: (:ref:`runtime.^platform^arch`)

      The machine's processor architecture.

   .. _runtime.^platform^info.nacl_arch:

   .. api-member::
      :name: ``nacl_arch``
      :refid: runtime-platform-info-nacl-arch
      :refname: nacl_arch
      :type: (:ref:`runtime.^platform^nacl^arch`) **Unsupported.**

      The native client architecture. This may be different from arch on some platforms.

   .. _runtime.^platform^info.os:

   .. api-member::
      :name: ``os``
      :refid: runtime-platform-info-os
      :refname: os
      :type: (:ref:`runtime.^platform^os`)

      The operating system the browser is running on.

.. _runtime.^platform^os:

PlatformOs
----------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

The operating system the browser is running on.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _runtime.^platform^os.android:

         .. api-member::
            :name: :value:`android`
            :refid: runtime-platform-os-android
            :refname: android

         .. _runtime.^platform^os.cros:

         .. api-member::
            :name: :value:`cros`
            :refid: runtime-platform-os-cros
            :refname: cros

         .. _runtime.^platform^os.linux:

         .. api-member::
            :name: :value:`linux`
            :refid: runtime-platform-os-linux
            :refname: linux

         .. _runtime.^platform^os.mac:

         .. api-member::
            :name: :value:`mac`
            :refid: runtime-platform-os-mac
            :refname: mac

         .. _runtime.^platform^os.openbsd:

         .. api-member::
            :name: :value:`openbsd`
            :refid: runtime-platform-os-openbsd
            :refname: openbsd

         .. _runtime.^platform^os.win:

         .. api-member::
            :name: :value:`win`
            :refid: runtime-platform-os-win
            :refname: win

.. _runtime.^port:

Port
----

.. api-section-annotation-hack:: -- [Added in TB 60.0]

An object which allows two way communication with other pages.

.. api-header::
   :label: object

   .. _runtime.^port.disconnect:

   .. api-member::
      :name: ``disconnect``
      :refid: runtime-port-disconnect
      :refname: disconnect
      :type: (function)

   .. _runtime.^port.name:

   .. api-member::
      :name: ``name``
      :refid: runtime-port-name
      :refname: name
      :type: (string)

   .. _runtime.^port.on^disconnect:

   .. api-member::
      :name: ``onDisconnect``
      :refid: runtime-port-on-disconnect
      :refname: onDisconnect
      :type: (:ref:`runtime.^event`)

   .. _runtime.^port.on^message:

   .. api-member::
      :name: ``onMessage``
      :refid: runtime-port-on-message
      :refname: onMessage
      :type: (:ref:`runtime.^event`)

   .. _runtime.^port.post^message:

   .. api-member::
      :name: ``postMessage``
      :refid: runtime-port-post-message
      :refname: postMessage
      :type: (function)

   .. _runtime.^port.sender:

   .. api-member::
      :name: [``sender``]
      :refid: runtime-port-sender
      :refname: sender
      :type: (:ref:`runtime.^message^sender`, optional)

      This property will **only** be present on ports passed to onConnect/onConnectExternal listeners.

.. _runtime.^request^update^check^status:

RequestUpdateCheckStatus
------------------------

.. api-section-annotation-hack:: 

Result of the update check.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _runtime.^request^update^check^status.no_update:

         .. api-member::
            :name: :value:`no_update`
            :refid: runtime-request-update-check-status-no-update
            :refname: no_update

         .. _runtime.^request^update^check^status.throttled:

         .. api-member::
            :name: :value:`throttled`
            :refid: runtime-request-update-check-status-throttled
            :refname: throttled

         .. _runtime.^request^update^check^status.update_available:

         .. api-member::
            :name: :value:`update_available`
            :refid: runtime-request-update-check-status-update-available
            :refname: update_available

.. rst-class:: api-main-section

Properties
==========

.. _runtime.id:

id
--

.. api-section-annotation-hack:: -- [Added in TB 60.0]

The ID of the extension/app.

.. _runtime.last^error:

lastError
---------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

This will be defined during an API method callback if there was an error
