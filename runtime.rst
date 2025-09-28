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

.. hint::

   The runtime API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/runtime>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.runtime` API to retrieve the background page, return details about the manifest, and listen for and respond to events in the app or extension lifecycle. You can also use this API to convert the relative path of URLs to fully-qualified URLs.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`nativeMessaging`

   Exchange messages with programs other than Thunderbird

.. api-member::
   :name: :permission:`userScripts`

   Allow unverified third-party scripts to access your data

Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. rst-class:: api-main-section

Functions
=========

.. _runtime.connect:

connect([extensionId], [connectInfo])
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Attempts to connect to connect listeners within an extension/app (such as the background page), or other extensions/apps. This is useful for content scripts connecting to their extension processes, inter-app/extension communication, and web messaging. Note that this does not connect to any listeners in a content script. Extensions may connect to content scripts embedded in tabs via :ref:`tabs.connect`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``extensionId``]
      :type: (string, optional)

      The ID of the extension or app to connect to. If omitted, a connection will be attempted with your own extension. Required if sending messages from a web page for web messaging.

   .. api-member::
      :name: [``connectInfo``]
      :type: (object, optional)

      .. api-member::
         :name: [``includeTlsChannelId``]
         :type: (boolean, optional)

         Whether the TLS channel ID will be passed into onConnectExternal for processes that are listening for the connection event.

      .. api-member::
         :name: [``name``]
         :type: (string, optional)

         Will be passed into onConnect for processes that are listening for the connection event.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`runtime.Port`

      Port through which messages can be sent and received. The port's :ref:`runtime.Port onDisconnect` event is fired if the extension/app does not exist.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.connectNative:

connectNative(application)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 50]

Connects to a native application in the host machine.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``application``
      :type: (string)

      The name of the registered application to connect to.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`runtime.Port`

      Port through which messages can be sent and received with the application

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`nativeMessaging`

.. _runtime.getBackgroundPage:

getBackgroundPage()
-------------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Retrieves the JavaScript 'window' object for the background page running inside the current extension/app. If the background page is an event page, the system will ensure it is loaded before calling the callback. If there is no background page, an error is set.

.. note::

   If this is called from a page that is part of a private browsing window, such as a sidebar in a private window or a popup opened from a private window, then it will always return :code:`null`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: `Window <https://developer.mozilla.org/en-US/docs/Web/API/Window>`__

      The JavaScript 'window' object for the background page.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.getBrowserInfo:

getBrowserInfo()
----------------

.. api-section-annotation-hack:: -- [Added in TB 51]

Returns information about the current browser.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`runtime.BrowserInfo`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.getContexts:

getContexts(filter)
-------------------

.. api-section-annotation-hack:: -- [Added in TB 127]

Fetches information about active contexts associated with this extension

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``filter``
      :type: (:ref:`runtime.ContextFilter`)

      A filter to find matching context.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`runtime.ExtensionContext`

      The matching contexts, if any.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.getFrameId:

getFrameId(target)
------------------

.. api-section-annotation-hack:: -- [Added in TB 96]

Get the frameId of any window global or frame element.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``target``
      :type: (any)

      A WindowProxy or a Browsing Context container element (IFrame, Frame, Embed, Object) for the target frame.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: number

      The frameId of the target frame, or -1 if it doesn't exist.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.getManifest:

getManifest()
-------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Returns details about the app or extension from the manifest. The object returned is a serialization of the full manifest file.

.. note::

   Returns null for missing values, and removes unsupported keys.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: object

      The manifest details.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.getPlatformInfo:

getPlatformInfo()
-----------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Returns information about the current platform.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`runtime.PlatformInfo`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.getURL:

getURL(path)
------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Converts a relative path within an app/extension install directory to a fully-qualified URL.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``path``
      :type: (string)

      A path to a resource within an app/extension expressed relative to its install directory.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string

      The fully-qualified URL to the resource.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.openOptionsPage:

openOptionsPage()
-----------------

.. api-section-annotation-hack:: -- [Added in TB 48]

Open your Extension's options page, if possible.The precise behavior may depend on your manifest's :code:`options_ui` or :code:`options_page` key, or what the browser happens to support at the time.If your Extension does not declare an options page, or the browser failed to create one for some other reason, the callback will set :ref:`runtime.lastError`.

.. _runtime.reload:

reload()
--------

.. api-section-annotation-hack:: -- [Added in TB 51]

Reloads the app or extension.

.. _runtime.restart:

restart()
---------

.. api-section-annotation-hack:: 

Restart the device when the app runs in kiosk mode. Otherwise, it's no-op.

.. _runtime.sendMessage:

sendMessage([extensionId], message, [options])
----------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Sends a single message to event listeners within your extension/app or a different extension/app. Similar to :ref:`runtime.connect` but only sends a single message, with an optional response. If sending to your extension, the :ref:`runtime.onMessage` event will be fired in each page, or :ref:`runtime.onMessageExternal`, if a different extension. Note that extensions cannot send messages to content scripts using this method. To send messages to content scripts, use :ref:`tabs.sendMessage`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``extensionId``]
      :type: (string, optional)

      The ID of the extension/app to send the message to. If omitted, the message will be sent to your own extension/app. Required if sending messages from a web page for web messaging.

   .. api-member::
      :name: ``message``
      :type: (any)

   .. api-member::
      :name: [``options``]
      :type: (object, optional)

      .. api-member::
         :name: [``includeTlsChannelId``]
         :type: (boolean, optional) **Unsupported.**

         Whether the TLS channel ID will be passed into onMessageExternal for processes that are listening for the connection event.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: any

      The JSON response object sent by the handler of the message. If an error occurs while connecting to the extension, the callback will be called with no arguments and :ref:`runtime.lastError` will be set to the error message.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _runtime.sendNativeMessage:

sendNativeMessage(application, message)
---------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 50]

Send a single message to a native application.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``application``
      :type: (string)

      The name of the native messaging host.

   .. api-member::
      :name: ``message``
      :type: (any)

      The message that will be passed to the native messaging host.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: any

      The response message sent by the native messaging host. If an error occurs while connecting to the native messaging host, the callback will be called with no arguments and :ref:`runtime.lastError` will be set to the error message.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`nativeMessaging`

.. _runtime.setUninstallURL:

setUninstallURL([url])
----------------------

.. api-section-annotation-hack:: 

Sets the URL to be visited upon uninstallation. This may be used to clean up server-side data, do analytics, and implement surveys. Maximum 1023 characters.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``url``]
      :type: (string, optional)

      URL to be opened after the extension is uninstalled. This URL must have an http: or https: scheme. Set an empty string to not open a new tab upon uninstallation.

.. rst-class:: api-main-section

Events
======

.. _runtime.onConnect:

onConnect
---------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when a connection is made from either an extension process or a content script.

.. api-header::
   :label: Parameters for onConnect.addListener(listener)

   .. api-member::
      :name: ``listener(port)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``port``
      :type: (:ref:`runtime.Port`)

.. _runtime.onConnectExternal:

onConnectExternal
-----------------

.. api-section-annotation-hack:: -- [Added in TB 54]

Fired when a connection is made from another extension.

.. api-header::
   :label: Parameters for onConnectExternal.addListener(listener)

   .. api-member::
      :name: ``listener(port)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``port``
      :type: (:ref:`runtime.Port`)

.. _runtime.onInstalled:

onInstalled
-----------

.. api-section-annotation-hack:: -- [Added in TB 52]

Fired when the extension is first installed, when the extension is updated to a new version, and when the browser is updated to a new version.

.. note::

   Before version 55, this event is not triggered for temporarily installed add-ons.

.. api-header::
   :label: Parameters for onInstalled.addListener(listener)

   .. api-member::
      :name: ``listener(details)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``reason``
         :type: (:ref:`runtime.OnInstalledReason`)

         The reason that this event is being dispatched.

      .. api-member::
         :name: ``temporary``
         :type: (boolean)
         :annotation: -- [Added in TB 55]

         Indicates whether the addon is installed as a temporary extension.

      .. api-member::
         :name: [``id``]
         :type: (string, optional) **Unsupported.**

         Indicates the ID of the imported shared module extension which updated. This is present only if 'reason' is 'shared_module_update'.

      .. api-member::
         :name: [``previousVersion``]
         :type: (string, optional)
         :annotation: -- [Added in TB 55]

         Indicates the previous version of the extension, which has just been updated. This is present only if 'reason' is 'update'.

.. _runtime.onMessage:

onMessage
---------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when a message is sent from either an extension process or a content script.

.. api-header::
   :label: Parameters for onMessage.addListener(listener)

   .. api-member::
      :name: ``listener(message, sender, sendResponse)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: [``message``]
      :type: (any, optional)

      The message sent by the calling script.

   .. api-member::
      :name: ``sender``
      :type: (:ref:`runtime.MessageSender`)

   .. api-member::
      :name: ``sendResponse``
      :type: (function)

      Function to call (at most once) when you have a response. The argument should be any JSON-ifiable object. If you have more than one :code:`onMessage` listener in the same document, then only one may send a response. This function becomes invalid when the event listener returns, unless you return true from the event listener to indicate you wish to send a response asynchronously (this will keep the message channel open to the other end until :code:`sendResponse` is called).

.. api-header::
   :label: Expected return value of the listener function

   .. api-member::
      :type: boolean

      Return true from the event listener if you wish to call :code:`sendResponse` after the event listener returns.

.. _runtime.onMessageExternal:

onMessageExternal
-----------------

.. api-section-annotation-hack:: -- [Added in TB 54]

Fired when a message is sent from another extension/app. Cannot be used in a content script.

.. api-header::
   :label: Parameters for onMessageExternal.addListener(listener)

   .. api-member::
      :name: ``listener(message, sender, sendResponse)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: [``message``]
      :type: (any, optional)

      The message sent by the calling script.

   .. api-member::
      :name: ``sender``
      :type: (:ref:`runtime.MessageSender`)

   .. api-member::
      :name: ``sendResponse``
      :type: (function)

      Function to call (at most once) when you have a response. The argument should be any JSON-ifiable object. If you have more than one :code:`onMessage` listener in the same document, then only one may send a response. This function becomes invalid when the event listener returns, unless you return true from the event listener to indicate you wish to send a response asynchronously (this will keep the message channel open to the other end until :code:`sendResponse` is called).

.. api-header::
   :label: Expected return value of the listener function

   .. api-member::
      :type: boolean

      Return true from the event listener if you wish to call :code:`sendResponse` after the event listener returns.

.. _runtime.onPerformanceWarning:

onPerformanceWarning
--------------------

.. api-section-annotation-hack:: -- [Added in TB 124]

Fired when a runtime performance issue is detected with the extension. Observe this event to be proactively notified of runtime performance problems with the extension.

.. api-header::
   :label: Parameters for onPerformanceWarning.addListener(listener)

   .. api-member::
      :name: ``listener(details)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``category``
         :type: (:ref:`runtime.OnPerformanceWarningCategory`)

         The performance warning event category, e.g. 'content_script'.

      .. api-member::
         :name: ``description``
         :type: (string)

         An explanation of what the warning means, and hopefully how to address it.

      .. api-member::
         :name: ``severity``
         :type: (:ref:`runtime.OnPerformanceWarningSeverity`)

         The performance warning event severity, e.g. 'high'.

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)

         The :ref:`tabs.Tab` that the performance warning relates to, if any.

.. _runtime.onStartup:

onStartup
---------

.. api-section-annotation-hack:: -- [Added in TB 52]

Fired when a profile that has this extension installed first starts up. This event is not fired for incognito profiles.

.. api-header::
   :label: Parameters for onStartup.addListener(listener)

   .. api-member::
      :name: ``listener()``

      A function that will be called when this event occurs.

.. _runtime.onSuspend:

onSuspend
---------

.. api-section-annotation-hack:: -- [Added in TB 100]

Sent to the event page just before it is unloaded. This gives the extension opportunity to do some clean up. Note that since the page is unloading, any asynchronous operations started while handling this event are not guaranteed to complete. If more activity for the event page occurs before it gets unloaded the onSuspendCanceled event will be sent and the page won't be unloaded.

.. note::

   This event does not fire until Thunderbird 106, when event pages are available.

.. api-header::
   :label: Parameters for onSuspend.addListener(listener)

   .. api-member::
      :name: ``listener()``

      A function that will be called when this event occurs.

.. _runtime.onSuspendCanceled:

onSuspendCanceled
-----------------

.. api-section-annotation-hack:: -- [Added in TB 100]

Sent after onSuspend to indicate that the app won't be unloaded after all.

.. note::

   This event does not fire until Thunderbird 106, when event pages are available.

.. api-header::
   :label: Parameters for onSuspendCanceled.addListener(listener)

   .. api-member::
      :name: ``listener()``

      A function that will be called when this event occurs.

.. _runtime.onUpdateAvailable:

onUpdateAvailable
-----------------

.. api-section-annotation-hack:: -- [Added in TB 51]

Fired when an update is available, but isn't installed immediately because the app is currently running. If you do nothing, the update will be installed the next time the background page gets unloaded, if you want it to be installed sooner you can explicitly call :ref:`runtime.reload`. If your extension is using a persistent background page, the background page of course never gets unloaded, so unless you call :ref:`runtime.reload` manually in response to this event the update will not get installed until the next time the browser itself restarts. If no handlers are listening for this event, and your extension has a persistent background page, it behaves as if :ref:`runtime.reload` is called in response to this event.

.. api-header::
   :label: Parameters for onUpdateAvailable.addListener(listener)

   .. api-member::
      :name: ``listener(details)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``details``
      :type: (object)

      The manifest details of the available update.

      .. api-member::
         :name: ``version``
         :type: (string)

         The version number of the available update.

.. _runtime.onUserScriptConnect:

onUserScriptConnect
-------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Fired when a connection is made from a USER_SCRIPT world registered through the userScripts API.

.. note::

   Available for use with Manifest V3 only.

.. note::

   Requires the `:code:`userScripts` permission <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/userScripts#permissions>`__.

.. api-header::
   :label: Parameters for onUserScriptConnect.addListener(listener)

   .. api-member::
      :name: ``listener(port)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``port``
      :type: (:ref:`runtime.Port`)

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _runtime.onUserScriptMessage:

onUserScriptMessage
-------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Fired when a message is sent from a USER_SCRIPT world registered through the userScripts API.

.. note::

   Available for use with Manifest V3 only.

.. note::

   Requires the `:code:`userScripts` permission <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/userScripts#permissions>`__.

.. api-header::
   :label: Parameters for onUserScriptMessage.addListener(listener)

   .. api-member::
      :name: ``listener(message, sender, sendResponse)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: [``message``]
      :type: (any, optional)

      The message sent by the calling script.

   .. api-member::
      :name: ``sender``
      :type: (:ref:`runtime.MessageSender`)

   .. api-member::
      :name: ``sendResponse``
      :type: (function)

      Function to call (at most once) when you have a response. The argument should be any JSON-ifiable object. If you have more than one :code:`onMessage` listener in the same document, then only one may send a response. This function becomes invalid when the event listener returns, unless you return true from the event listener to indicate you wish to send a response asynchronously (this will keep the message channel open to the other end until :code:`sendResponse` is called).

.. api-header::
   :label: Expected return value of the listener function

   .. api-member::
      :type: boolean

      Return true from the event listener if you wish to call :code:`sendResponse` after the event listener returns.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. rst-class:: api-main-section

Types
=====

.. _runtime.BrowserInfo:

BrowserInfo
-----------

.. api-section-annotation-hack:: 

An object containing information about the current browser.

.. api-header::
   :label: object

   .. _runtime.BrowserInfo.buildID:

   .. api-member::
      :name: ``buildID``
      :type: (string)

      The browser's build ID/date, for example '20160101'.

   .. _runtime.BrowserInfo.name:

   .. api-member::
      :name: ``name``
      :type: (string)

      The name of the browser, for example 'Thunderbird'.

   .. _runtime.BrowserInfo.vendor:

   .. api-member::
      :name: ``vendor``
      :type: (string)

      The name of the browser vendor, for example 'Mozilla'.

   .. _runtime.BrowserInfo.version:

   .. api-member::
      :name: ``version``
      :type: (string)

      The browser's version, for example '42.0.0' or '0.8.1pre'.

.. _runtime.ContextFilter:

ContextFilter
-------------

.. api-section-annotation-hack:: 

A filter to match against existing extension context. Matching contexts must match all specified filters.

.. api-header::
   :label: object

   .. _runtime.ContextFilter.contextIds:

   .. api-member::
      :name: [``contextIds``]
      :type: (array of string, optional)

   .. _runtime.ContextFilter.contextTypes:

   .. api-member::
      :name: [``contextTypes``]
      :type: (array of :ref:`runtime.ContextType`, optional)

   .. _runtime.ContextFilter.documentIds:

   .. api-member::
      :name: [``documentIds``]
      :type: (array of string, optional)

   .. _runtime.ContextFilter.documentOrigins:

   .. api-member::
      :name: [``documentOrigins``]
      :type: (array of string, optional)

   .. _runtime.ContextFilter.documentUrls:

   .. api-member::
      :name: [``documentUrls``]
      :type: (array of string, optional)

   .. _runtime.ContextFilter.frameIds:

   .. api-member::
      :name: [``frameIds``]
      :type: (array of integer, optional)

   .. _runtime.ContextFilter.incognito:

   .. api-member::
      :name: [``incognito``]
      :type: (boolean, optional)

   .. _runtime.ContextFilter.tabIds:

   .. api-member::
      :name: [``tabIds``]
      :type: (array of integer, optional)

   .. _runtime.ContextFilter.windowIds:

   .. api-member::
      :name: [``windowIds``]
      :type: (array of integer, optional)

.. _runtime.ContextType:

ContextType
-----------

.. api-section-annotation-hack:: 

The type of extension view.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`BACKGROUND`

         .. api-member::
            :name: :value:`POPUP`

         .. api-member::
            :name: :value:`SIDE_PANEL`

         .. api-member::
            :name: :value:`TAB`

.. _runtime.ExtensionContext:

ExtensionContext
----------------

.. api-section-annotation-hack:: 

A context hosting extension content

.. api-header::
   :label: object

   .. _runtime.ExtensionContext.contextId:

   .. api-member::
      :name: ``contextId``
      :type: (string)

      An unique identifier associated to this context

   .. _runtime.ExtensionContext.contextType:

   .. api-member::
      :name: ``contextType``
      :type: (:ref:`runtime.ContextType`)

      The type of the context

   .. _runtime.ExtensionContext.frameId:

   .. api-member::
      :name: ``frameId``
      :type: (integer)

      The frame ID for this context, or -1 if it is not hosted in a frame.

   .. _runtime.ExtensionContext.incognito:

   .. api-member::
      :name: ``incognito``
      :type: (boolean)

      Whether the context is associated with an private browsing context.

   .. _runtime.ExtensionContext.tabId:

   .. api-member::
      :name: ``tabId``
      :type: (integer)

      The tab ID for this context, or -1 if it is not hosted in a tab.

   .. _runtime.ExtensionContext.windowId:

   .. api-member::
      :name: ``windowId``
      :type: (integer)

      The window ID for this context, or -1 if it is not hosted in a window.

   .. _runtime.ExtensionContext.documentId:

   .. api-member::
      :name: [``documentId``]
      :type: (string, optional) **Unsupported.**

      An UUID for the document associated with this context, or undefined if it is not hosted in a document

   .. _runtime.ExtensionContext.documentOrigin:

   .. api-member::
      :name: [``documentOrigin``]
      :type: (string, optional)

      The origin of the document associated with this context, or undefined if it is not hosted in a document

   .. _runtime.ExtensionContext.documentUrl:

   .. api-member::
      :name: [``documentUrl``]
      :type: (string, optional)

      The URL of the document associated with this context, or undefined if it is not hosted in a document

.. _runtime.MessageSender:

MessageSender
-------------

.. api-section-annotation-hack:: -- [Added in TB 45]

An object containing information about the script context that sent a message or request.

.. note::

   Before version 54, 'id' was the add-on's internal UUID, not the add-on ID.

.. api-header::
   :label: object

   .. _runtime.MessageSender.frameId:

   .. api-member::
      :name: [``frameId``]
      :type: (integer, optional)

      The frame that opened the connection. 0 for top-level frames, positive for child frames. This will only be set when :code:`tab` is set.

   .. _runtime.MessageSender.id:

   .. api-member::
      :name: [``id``]
      :type: (string, optional)

      The ID of the extension or app that opened the connection, if any.

   .. _runtime.MessageSender.tab:

   .. api-member::
      :name: [``tab``]
      :type: (:ref:`tabs.Tab`, optional)

      The :ref:`tabs.Tab` which opened the connection, if any. This property will <strong>only</strong> be present when the connection was opened from a tab (including content scripts), and <strong>only</strong> if the receiver is an extension, not an app.

   .. _runtime.MessageSender.tlsChannelId:

   .. api-member::
      :name: [``tlsChannelId``]
      :type: (string, optional) **Unsupported.**

      The TLS channel ID of the page or frame that opened the connection, if requested by the extension or app, and if available.

   .. _runtime.MessageSender.url:

   .. api-member::
      :name: [``url``]
      :type: (string, optional)

      The URL of the page or frame that opened the connection. If the sender is in an iframe, it will be iframe's URL not the URL of the page which hosts it.

   .. _runtime.MessageSender.userScriptWorldId:

   .. api-member::
      :name: [``userScriptWorldId``]
      :type: (string, optional)

      The worldId of the USER_SCRIPT world that sent the message. Only present on onUserScriptMessage and onUserScriptConnect (in port.sender) events.

.. _runtime.OnInstalledReason:

OnInstalledReason
-----------------

.. api-section-annotation-hack:: -- [Added in TB 45]

The reason that this event is being dispatched.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`install`

         .. api-member::
            :name: :value:`update`

         .. api-member::
            :name: :value:`browser_update`

.. _runtime.OnPerformanceWarningCategory:

OnPerformanceWarningCategory
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 124]

The performance warning event category, e.g. 'content_script'.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`content_script`

.. _runtime.OnPerformanceWarningSeverity:

OnPerformanceWarningSeverity
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 124]

The performance warning event severity. Will be 'high' for serious and user-visible issues.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`low`

         .. api-member::
            :name: :value:`medium`

         .. api-member::
            :name: :value:`high`

.. _runtime.PlatformArch:

PlatformArch
------------

.. api-section-annotation-hack:: -- [Added in TB 45]

The machine's processor architecture.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`aarch64`

         .. api-member::
            :name: :value:`arm`

         .. api-member::
            :name: :value:`ppc64`

         .. api-member::
            :name: :value:`riscv64`

         .. api-member::
            :name: :value:`s390x`

         .. api-member::
            :name: :value:`sparc64`

         .. api-member::
            :name: :value:`x86-32`

         .. api-member::
            :name: :value:`x86-64`

         .. api-member::
            :name: :value:`noarch`

.. _runtime.PlatformInfo:

PlatformInfo
------------

.. api-section-annotation-hack:: -- [Added in TB 45]

An object containing information about the current platform.

.. api-header::
   :label: object

   .. _runtime.PlatformInfo.arch:

   .. api-member::
      :name: ``arch``
      :type: (:ref:`runtime.PlatformArch`)

      The machine's processor architecture.

   .. _runtime.PlatformInfo.nacl_arch:

   .. api-member::
      :name: ``nacl_arch``
      :type: (:ref:`runtime.PlatformNaclArch`) **Unsupported.**

      The native client architecture. This may be different from arch on some platforms.

   .. _runtime.PlatformInfo.os:

   .. api-member::
      :name: ``os``
      :type: (:ref:`runtime.PlatformOs`)

      The operating system the browser is running on.

.. _runtime.PlatformOs:

PlatformOs
----------

.. api-section-annotation-hack:: -- [Added in TB 45]

The operating system the browser is running on.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`mac`

         .. api-member::
            :name: :value:`win`

         .. api-member::
            :name: :value:`android`

         .. api-member::
            :name: :value:`cros`

         .. api-member::
            :name: :value:`linux`

         .. api-member::
            :name: :value:`openbsd`

.. _runtime.Port:

Port
----

.. api-section-annotation-hack:: -- [Added in TB 45]

An object which allows two way communication with other pages.

.. api-header::
   :label: object

   .. _runtime.Port.disconnect:

   .. api-member::
      :name: ``disconnect``
      :type: (function)

   .. _runtime.Port.name:

   .. api-member::
      :name: ``name``
      :type: (string)

   .. _runtime.Port.onDisconnect:

   .. api-member::
      :name: ``onDisconnect``
      :type: (:ref:`events.Event`)

   .. _runtime.Port.onMessage:

   .. api-member::
      :name: ``onMessage``
      :type: (:ref:`events.Event`)

   .. _runtime.Port.postMessage:

   .. api-member::
      :name: ``postMessage``
      :type: (function)

   .. _runtime.Port.sender:

   .. api-member::
      :name: [``sender``]
      :type: (:ref:`runtime.MessageSender`, optional)

      This property will **only** be present on ports passed to onConnect/onConnectExternal listeners.

.. rst-class:: api-main-section

Properties
==========

.. _runtime.id:

id
--

.. api-section-annotation-hack:: 

The ID of the extension/app.

.. _runtime.lastError:

lastError
---------

.. api-section-annotation-hack:: 

This will be defined during an API method callback if there was an error
