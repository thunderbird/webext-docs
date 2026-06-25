.. container:: sticky-sidebar

  ≡ tabs API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

========
tabs API
========

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

The tabs API supports creating, modifying and interacting with tabs in Thunderbird windows.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _tabs.permission.active^tab:

.. api-member::
   :name: :permission:`activeTab`
   :refid: tabs-permission-active-tab
   :refname: activeTab

   Grant host permission to the currently active tab, allowing to read :value:`title`, :value:`url` and :value:`favIconUrl` properties, or to inject content scripts.

.. _tabs.permission.contextual^identities:

.. api-member::
   :name: :permission:`contextualIdentities`
   :refid: tabs-permission-contextual-identities
   :refname: contextualIdentities

   Grant access to some or all methods of the contextualIdentities API.

.. _tabs.permission.cookies:

.. api-member::
   :name: :permission:`cookies`
   :refid: tabs-permission-cookies
   :refname: cookies

   Grant access to some or all methods of the cookies API.

.. _tabs.permission.tabs:

.. api-member::
   :name: :permission:`tabs`
   :refid: tabs-permission-tabs
   :refname: tabs

   Grant host permission to all active and inactive tabs, allowing to read :value:`title`, :value:`url` and :value:`favIconUrl` properties, or to inject content scripts.

.. rst-class:: api-main-section

Functions
=========

.. _tabs.connect:

connect(tabId, [connectInfo])
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 82]

Connects to the content script(s) in the specified tab. The `runtime.onConnect <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect>`__ event is fired in each content script running in the specified tab for the current extension. For more details, see `Content Script Messaging <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`__.

.. api-header::
   :label: Parameters

   .. _tabs.connect.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: tabs-connect-tab-id
      :refname: tabId
      :type: (integer)

   .. _tabs.connect.connect^info:

   .. api-member::
      :name: [``connectInfo``]
      :refid: tabs-connect-connect-info
      :refname: connectInfo
      :type: (object, optional)

      .. _tabs.connect.connect^info.document^id:

      .. api-member::
         :name: [``documentId``]
         :refid: tabs-connect-connect-info-document-id
         :refname: documentId
         :type: (string, optional)
         :annotation: -- [Added in TB 153]

         Open a port to a specific document identified by :value:`documentId` instead of all frames in the tab.

      .. _tabs.connect.connect^info.frame^id:

      .. api-member::
         :name: [``frameId``]
         :refid: tabs-connect-connect-info-frame-id
         :refname: frameId
         :type: (integer, optional)

         Open a port to a specific frame identified by :value:`frameId` instead of all frames in the tab.

      .. _tabs.connect.connect^info.name:

      .. api-member::
         :name: [``name``]
         :refid: tabs-connect-connect-info-name
         :refname: name
         :type: (string, optional)

         Will be passed into onConnect for content scripts that are listening for the connection event.

.. api-header::
   :label: Return type (`Promise`_)

   .. _tabs.connect.returns:

   .. api-member::
      :refid: tabs-connect-returns
      :refname: _returns
      :type: `Port <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port>`__

      A port that can be used to communicate with the content scripts running in the specified tab.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.create:

create(createProperties)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Creates a new content tab. To create message tabs, use the :ref:`message^display.open`. Only supported in :value:`normal` windows. Same-site links in the loaded page are opened within Thunderbird, all other links are opened in the user's default browser. To override this behavior, add-ons have to register a `content script <https://bugzilla.mozilla.org/show_bug.cgi?id=1618828#c3>`__ , capture click events and handle them manually.

.. api-header::
   :label: Parameters

   .. _tabs.create.create^properties:

   .. api-member::
      :name: ``createProperties``
      :refid: tabs-create-create-properties
      :refname: createProperties
      :type: (object)

      Properties for the new tab. Defaults to an empty tab, if no :value:`url` is provided.

      .. _tabs.create.create^properties.active:

      .. api-member::
         :name: [``active``]
         :refid: tabs-create-create-properties-active
         :refname: active
         :type: (boolean, optional)

         Whether the tab should become the active tab in the window. Does not affect whether the window is focused (see :ref:`windows.update`). Defaults to :value:`true`.

      .. _tabs.create.create^properties.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: tabs-create-create-properties-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)
         :annotation: -- [Added in TB 115]

         The `CookieStore <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities/ContextualIdentity#cookiestoreid>`__ id the new tab should use. Either a custom id created using the `contextualIdentities API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities>`__, or a built-in one: :value:`firefox-default`, :value:`firefox-container-1`, :value:`firefox-container-2`, :value:`firefox-container-3`, :value:`firefox-container-4`, :value:`firefox-container-5`.

         .. note::

            The naming pattern of the built-in cookie stores was deliberately not changed for Thunderbird, but kept for compatibility reasons.

         .. note::

            The :permission:`cookies` permission is required to be able to specify this property. Furthermore, the :permission:`contextualIdentities` permission should be requested, to enable the contextual identities feature (enabled by default only on Thunderbird Daily).

      .. _tabs.create.create^properties.index:

      .. api-member::
         :name: [``index``]
         :refid: tabs-create-create-properties-index
         :refname: index
         :type: (integer, optional)

         The position the tab should take in the window. The provided value will be clamped to between zero and the number of tabs in the window.

      .. _tabs.create.create^properties.link^handler:

      .. api-member::
         :name: [``linkHandler``]
         :refid: tabs-create-create-properties-link-handler
         :refname: linkHandler
         :type: (`string`, optional)
         :annotation: -- [Added in TB 136]

         Thunderbird is a mail client, not a browser. It is possible to load a web page, but opening follow-up pages through hyperlinks should be handled by the user's default browser. This property specifies to what extent this behavior should be enforced. The default :value:`balanced` link handler will open links to the same host directly in Thunderbird, everything else will be opened in the user's default browser. A :value:`relaxed` link handler will open all links inside of Thunderbird, a :value:`strict` link handler will open all links in the user's default browser, except links to the same page.

         Supported values:

         .. _tabs.create.create^properties.link^handler.balanced:

         .. api-member::
            :name: :value:`balanced`
            :refid: tabs-create-create-properties-link-handler-balanced
            :refname: balanced

         .. _tabs.create.create^properties.link^handler.relaxed:

         .. api-member::
            :name: :value:`relaxed`
            :refid: tabs-create-create-properties-link-handler-relaxed
            :refname: relaxed

         .. _tabs.create.create^properties.link^handler.strict:

         .. api-member::
            :name: :value:`strict`
            :refid: tabs-create-create-properties-link-handler-strict
            :refname: strict

      .. _tabs.create.create^properties.selected:

      .. api-member::
         :name: [``selected``]
         :refid: tabs-create-create-properties-selected
         :refname: selected
         :type: (boolean, optional) **Unsupported.**

         Whether the tab should become the selected tab in the window. Defaults to :value:`true`

      .. _tabs.create.create^properties.url:

      .. api-member::
         :name: [``url``]
         :refid: tabs-create-create-properties-url
         :refname: url
         :type: (string, optional)

         The URL to navigate the tab to initially. If the URL points to a content page (a web page, an extension page or a registered WebExtension protocol handler page), the tab will navigate to the requested page. All other URLs will be opened externally after creating an empty tab. Fully-qualified URLs must include a scheme (i.e. :value:`http://www.google.com`, not :value:`www.google.com`). Relative URLs will be relative to the root of the extension.

      .. _tabs.create.create^properties.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: tabs-create-create-properties-window-id
         :refname: windowId
         :type: (integer, optional)

         The window to create the new tab in. Defaults to the current window.

.. api-header::
   :label: Return type (`Promise`_)

   .. _tabs.create.returns:

   .. api-member::
      :refid: tabs-create-returns
      :refname: _returns
      :type: :ref:`tabs.^tab`

      A Promise that will be fulfilled with a :ref:`tabs.^tab` object containing details about the created tab. If the tab could not be created (for example, because it was added to a non-normal window) the promise will be rejected with an error message. The returned promise resolves as soon as the tab has been created. The tab may still be loading, with its title being :value:`loading...` and its URL being :value:`about:blank`. To detect when the tab has finished loading, listen to the :ref:`tabs.on^updated` event before creating the tab.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.duplicate:

duplicate(tabId)
----------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Duplicates a tab.

.. api-header::
   :label: Parameters

   .. _tabs.duplicate.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: tabs-duplicate-tab-id
      :refname: tabId
      :type: (integer)

      The ID of the tab which is to be duplicated.

.. api-header::
   :label: Return type (`Promise`_)

   .. _tabs.duplicate.returns:

   .. api-member::
      :refid: tabs-duplicate-returns
      :refname: _returns
      :type: :ref:`tabs.^tab`

      Details about the duplicated tab. The :ref:`tabs.^tab` object doesn't contain :value:`url`, :value:`title` and :value:`favIconUrl` if the :permission:`tabs` permission has not been requested.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.get:

get(tabId)
----------

.. api-section-annotation-hack:: -- [Added in TB 62]

Retrieves details about the specified tab.

.. api-header::
   :label: Parameters

   .. _tabs.get.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: tabs-get-tab-id
      :refname: tabId
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. _tabs.get.returns:

   .. api-member::
      :refid: tabs-get-returns
      :refname: _returns
      :type: :ref:`tabs.^tab`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.get^current:

getCurrent()
------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Gets the tab that this script call is being made from. Returns :value:`undefined` if called from a non-tab context (for example a background page or a popup view).

.. api-header::
   :label: Return type (`Promise`_)

   .. _tabs.get^current.returns:

   .. api-member::
      :refid: tabs-get-current-returns
      :refname: _returns
      :type: :ref:`tabs.^tab`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.move:

move(tabIds, moveProperties)
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Moves one or more tabs to a new position within its current window, or to a different window. Tabs can only be moved to and from windows of type :value:`normal`. The primary mail tab cannot be moved, attempting to actively reposition it will throw an *ExtensionError*. Other tabs also cannot be placed before the primary mail tab, they will automatically be positioned after it, ensuring that the primary mail tab always remains first.

.. api-header::
   :label: Parameters

   .. _tabs.move.tab^ids:

   .. api-member::
      :name: ``tabIds``
      :refid: tabs-move-tab-ids
      :refname: tabIds
      :type: (integer or array of integer)

      The tab or list of tabs to move.

   .. _tabs.move.move^properties:

   .. api-member::
      :name: ``moveProperties``
      :refid: tabs-move-move-properties
      :refname: moveProperties
      :type: (object)

      .. _tabs.move.move^properties.index:

      .. api-member::
         :name: ``index``
         :refid: tabs-move-move-properties-index
         :refname: index
         :type: (integer)

         The position to move the tab to. :value:`-1` will place the tab at the end of the window.

      .. _tabs.move.move^properties.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: tabs-move-move-properties-window-id
         :refname: windowId
         :type: (integer, optional)

         Defaults to the window the tab is currently in.

.. api-header::
   :label: Return type (`Promise`_)

   .. _tabs.move.returns:

   .. api-member::
      :refid: tabs-move-returns
      :refname: _returns
      :type: array of :ref:`tabs.^tab`

      Details about the moved tabs.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.query:

query([queryInfo])
------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Gets all tabs that have the specified properties, or all tabs if no properties are specified.

.. api-header::
   :label: Parameters

   .. _tabs.query.query^info:

   .. api-member::
      :name: [``queryInfo``]
      :refid: tabs-query-query-info
      :refname: queryInfo
      :type: (object, optional)

      .. _tabs.query.query^info.active:

      .. api-member::
         :name: [``active``]
         :refid: tabs-query-query-info-active
         :refname: active
         :type: (boolean, optional)

         Whether the tabs are active in their windows.

      .. _tabs.query.query^info.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: tabs-query-query-info-cookie-store-id
         :refname: cookieStoreId
         :type: (array of string or string, optional)
         :annotation: -- [Added in TB 115]

         The `CookieStore <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities/ContextualIdentity#cookiestoreid>`__ id(s) used by the tabs. Either custom ids created using the `contextualIdentities API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities>`__, or built-in ones: :value:`firefox-default`, :value:`firefox-container-1`, :value:`firefox-container-2`, :value:`firefox-container-3`, :value:`firefox-container-4`, :value:`firefox-container-5`.

         .. note::

            The naming pattern of the built-in cookie stores was deliberately not changed for Thunderbird, but kept for compatibility reasons.

      .. _tabs.query.query^info.current^window:

      .. api-member::
         :name: [``currentWindow``]
         :refid: tabs-query-query-info-current-window
         :refname: currentWindow
         :type: (boolean, optional)

         Whether the tabs are in the current window.

      .. _tabs.query.query^info.highlighted:

      .. api-member::
         :name: [``highlighted``]
         :refid: tabs-query-query-info-highlighted
         :refname: highlighted
         :type: (boolean, optional)

         Whether the tabs are highlighted. Works as an alias of active.

      .. _tabs.query.query^info.index:

      .. api-member::
         :name: [``index``]
         :refid: tabs-query-query-info-index
         :refname: index
         :type: (integer, optional)

         The position of the tabs within their windows.

      .. _tabs.query.query^info.last^focused^window:

      .. api-member::
         :name: [``lastFocusedWindow``]
         :refid: tabs-query-query-info-last-focused-window
         :refname: lastFocusedWindow
         :type: (boolean, optional)

         Whether the tabs are in the last focused window.

      .. _tabs.query.query^info.space^id:

      .. api-member::
         :name: [``spaceId``]
         :refid: tabs-query-query-info-space-id
         :refname: spaceId
         :type: (integer, optional)
         :annotation: -- [Added in TB 115]

         The id of the space the tabs should belong to.

      .. _tabs.query.query^info.status:

      .. api-member::
         :name: [``status``]
         :refid: tabs-query-query-info-status
         :refname: status
         :type: (:ref:`tabs.^tab^status`, optional)

         Whether the tabs have completed loading.

      .. _tabs.query.query^info.title:

      .. api-member::
         :name: [``title``]
         :refid: tabs-query-query-info-title
         :refname: title
         :type: (string, optional)

         Match page titles against a pattern. The :permission:`tabs` permission is required to use this property.

      .. _tabs.query.query^info.type:

      .. api-member::
         :name: [``type``]
         :refid: tabs-query-query-info-type
         :refname: type
         :type: (:ref:`tabs.^tab^type` or array of :ref:`tabs.^tab^type`, optional)
         :annotation: -- [Added in TB 92]

         Match tabs against the given tab type or types.

      .. _tabs.query.query^info.url:

      .. api-member::
         :name: [``url``]
         :refid: tabs-query-query-info-url
         :refname: url
         :type: (string or array of string, optional)

         Match tabs against one or more `URL Patterns <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns>`__. Fragment identifiers are not matched. The :permission:`tabs` permission is required to use this property.

      .. _tabs.query.query^info.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: tabs-query-query-info-window-id
         :refname: windowId
         :type: (integer, optional)

         The ID of the parent window, or :ref:`windows.^w^i^n^d^o^w_^i^d_^c^u^r^r^e^n^t` for the current window.

      .. _tabs.query.query^info.window^type:

      .. api-member::
         :name: [``windowType``]
         :refid: tabs-query-query-info-window-type
         :refname: windowType
         :type: (:ref:`tabs.^window^type`, optional)

         The type of window the tabs are in.

.. api-header::
   :label: Return type (`Promise`_)

   .. _tabs.query.returns:

   .. api-member::
      :refid: tabs-query-returns
      :refname: _returns
      :type: array of :ref:`tabs.^tab`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.reload:

reload([tabId], [reloadProperties])
-----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Reload a tab. Only applicable for tabs which display a content page.

.. api-header::
   :label: Parameters

   .. _tabs.reload.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: tabs-reload-tab-id
      :refname: tabId
      :type: (integer, optional)

      The ID of the tab to reload; defaults to the selected tab of the current window.

   .. _tabs.reload.reload^properties:

   .. api-member::
      :name: [``reloadProperties``]
      :refid: tabs-reload-reload-properties
      :refname: reloadProperties
      :type: (object, optional)

      .. _tabs.reload.reload^properties.bypass^cache:

      .. api-member::
         :name: [``bypassCache``]
         :refid: tabs-reload-reload-properties-bypass-cache
         :refname: bypassCache
         :type: (boolean, optional)

         Whether using any local cache. Default is false.

.. _tabs.remove:

remove(tabIds)
--------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Closes one or more tabs.

.. api-header::
   :label: Parameters

   .. _tabs.remove.tab^ids:

   .. api-member::
      :name: ``tabIds``
      :refid: tabs-remove-tab-ids
      :refname: tabIds
      :type: (integer or array of integer)

      The tab or list of tabs to close.

.. _tabs.send^message:

sendMessage(tabId, message, [options])
--------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 82]

Sends a single message to the content script(s) in the specified tab, with an optional callback to run when a response is sent back. The `runtime.onMessage <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage>`__ event is fired in each content script running in the specified tab for the current extension.

.. api-header::
   :label: Parameters

   .. _tabs.send^message.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: tabs-send-message-tab-id
      :refname: tabId
      :type: (integer)

   .. _tabs.send^message.message:

   .. api-member::
      :name: ``message``
      :refid: tabs-send-message-message
      :refname: message
      :type: (any)

   .. _tabs.send^message.options:

   .. api-member::
      :name: [``options``]
      :refid: tabs-send-message-options
      :refname: options
      :type: (object, optional)

      .. _tabs.send^message.options.document^id:

      .. api-member::
         :name: [``documentId``]
         :refid: tabs-send-message-options-document-id
         :refname: documentId
         :type: (string, optional)
         :annotation: -- [Added in TB 153]

         Send a message to a specific document identified by :value:`documentId` instead of all frames in the tab.

      .. _tabs.send^message.options.frame^id:

      .. api-member::
         :name: [``frameId``]
         :refid: tabs-send-message-options-frame-id
         :refname: frameId
         :type: (integer, optional)

         Send a message to a specific frame identified by :value:`frameId` instead of all frames in the tab.

.. api-header::
   :label: Return type (`Promise`_)

   .. _tabs.send^message.returns:

   .. api-member::
      :refid: tabs-send-message-returns
      :refname: _returns
      :type: any

      The JSON response object sent by the handler of the message. If an error occurs while connecting to the specified tab, the callback will be called with no arguments and `runtime.lastError <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError>`__ will be set to the error message.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.update:

update([tabId], updateProperties)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Modifies the properties of a tab. Properties that are not specified in :value:`updateProperties` are not modified.

.. api-header::
   :label: Parameters

   .. _tabs.update.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: tabs-update-tab-id
      :refname: tabId
      :type: (integer, optional)

      Defaults to the selected tab of the current window.

   .. _tabs.update.update^properties:

   .. api-member::
      :name: ``updateProperties``
      :refid: tabs-update-update-properties
      :refname: updateProperties
      :type: (object)

      Properties which should to be updated.

      .. _tabs.update.update^properties.active:

      .. api-member::
         :name: [``active``]
         :refid: tabs-update-update-properties-active
         :refname: active
         :type: (boolean, optional)

         Set this to :value:`true`, if the tab should become active. Does not affect whether the window is focused (see :ref:`windows.update`). Setting this to :value:`false` has no effect.

      .. _tabs.update.update^properties.url:

      .. api-member::
         :name: [``url``]
         :refid: tabs-update-update-properties-url
         :refname: url
         :type: (string, optional)

         A URL of a page to load. If the URL points to a content page (a web page, an extension page or a registered WebExtension protocol handler page), the tab will navigate to the requested page. All other URLs will be opened externally without changing the tab.

         .. note::

            This function will throw an error, if a content page is loaded into a non-content tab (its type must be either :value:`content` or :value:`mail`).

.. api-header::
   :label: Return type (`Promise`_)

   .. _tabs.update.returns:

   .. api-member::
      :refid: tabs-update-returns
      :refname: _returns
      :type: :ref:`tabs.^tab`

      Details about the updated tab. The :ref:`tabs.^tab` object doesn't contain :value:`url`, :value:`title` and :value:`favIconUrl` if the :permission:`tabs` permission has not been requested.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _tabs.on^activated:

onActivated
-----------

.. api-section-annotation-hack:: -- [Added in TB 62]

Fires when the active tab in a window changes. The tab's URL may not be set at the time this event fired, listen to the :ref:`tabs.on^updated` event instead to be notified when a URL is set.

.. api-header::
   :label: Parameters for onActivated.addListener(listener)

   .. _tabs.on^activated.listener(active^info):

   .. api-member::
      :name: ``listener(activeInfo)``
      :refid: tabs-on-activated-listener-active-info
      :refname: listener(activeInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _tabs.on^activated.active^info:

   .. api-member::
      :name: ``activeInfo``
      :refid: tabs-on-activated-active-info
      :refname: activeInfo
      :type: (object)

      .. _tabs.on^activated.active^info.tab^id:

      .. api-member::
         :name: ``tabId``
         :refid: tabs-on-activated-active-info-tab-id
         :refname: tabId
         :type: (integer)

         The ID of the tab that has become active.

      .. _tabs.on^activated.active^info.window^id:

      .. api-member::
         :name: ``windowId``
         :refid: tabs-on-activated-active-info-window-id
         :refname: windowId
         :type: (integer)

         The ID of the window the active tab changed inside of.

      .. _tabs.on^activated.active^info.previous^tab^id:

      .. api-member::
         :name: [``previousTabId``]
         :refid: tabs-on-activated-active-info-previous-tab-id
         :refname: previousTabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 114]

         The ID of the tab that was previously active, if that tab is still open.

.. _tabs.on^attached:

onAttached
----------

.. api-section-annotation-hack:: -- [Added in TB 62]

Fired when a tab is attached to a window, for example because it was moved between windows.

.. api-header::
   :label: Parameters for onAttached.addListener(listener)

   .. _tabs.on^attached.listener(tab^id, attach^info):

   .. api-member::
      :name: ``listener(tabId, attachInfo)``
      :refid: tabs-on-attached-listener-tab-id-attach-info
      :refname: listener(tabId, attachInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _tabs.on^attached.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: tabs-on-attached-tab-id
      :refname: tabId
      :type: (integer)

   .. _tabs.on^attached.attach^info:

   .. api-member::
      :name: ``attachInfo``
      :refid: tabs-on-attached-attach-info
      :refname: attachInfo
      :type: (object)

      .. _tabs.on^attached.attach^info.new^position:

      .. api-member::
         :name: ``newPosition``
         :refid: tabs-on-attached-attach-info-new-position
         :refname: newPosition
         :type: (integer)

      .. _tabs.on^attached.attach^info.new^window^id:

      .. api-member::
         :name: ``newWindowId``
         :refid: tabs-on-attached-attach-info-new-window-id
         :refname: newWindowId
         :type: (integer)

.. _tabs.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 62]

Fired when a tab is created. The tab may still be loading, with its title being :value:`loading...` and its URL being :value:`about:blank`. To detect when the tab has finished loading, listen to the :ref:`tabs.on^updated` event.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _tabs.on^created.listener(tab):

   .. api-member::
      :name: ``listener(tab)``
      :refid: tabs-on-created-listener-tab
      :refname: listener(tab)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _tabs.on^created.tab:

   .. api-member::
      :name: ``tab``
      :refid: tabs-on-created-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

      Details of the tab that was created.

.. _tabs.on^detached:

onDetached
----------

.. api-section-annotation-hack:: -- [Added in TB 62]

Fired when a tab is detached from a window, for example because it is being moved between windows.

.. api-header::
   :label: Parameters for onDetached.addListener(listener)

   .. _tabs.on^detached.listener(tab^id, detach^info):

   .. api-member::
      :name: ``listener(tabId, detachInfo)``
      :refid: tabs-on-detached-listener-tab-id-detach-info
      :refname: listener(tabId, detachInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _tabs.on^detached.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: tabs-on-detached-tab-id
      :refname: tabId
      :type: (integer)

   .. _tabs.on^detached.detach^info:

   .. api-member::
      :name: ``detachInfo``
      :refid: tabs-on-detached-detach-info
      :refname: detachInfo
      :type: (object)

      .. _tabs.on^detached.detach^info.old^position:

      .. api-member::
         :name: ``oldPosition``
         :refid: tabs-on-detached-detach-info-old-position
         :refname: oldPosition
         :type: (integer)

      .. _tabs.on^detached.detach^info.old^window^id:

      .. api-member::
         :name: ``oldWindowId``
         :refid: tabs-on-detached-detach-info-old-window-id
         :refname: oldWindowId
         :type: (integer)

.. _tabs.on^moved:

onMoved
-------

.. api-section-annotation-hack:: -- [Added in TB 62]

Fired when a tab is moved within a window. Only one move event is fired, representing the tab the user directly moved. Move events are not fired for the other tabs that must move in response. This event is not fired when a tab is moved between windows. For that, see :ref:`tabs.on^detached`.

.. api-header::
   :label: Parameters for onMoved.addListener(listener)

   .. _tabs.on^moved.listener(tab^id, move^info):

   .. api-member::
      :name: ``listener(tabId, moveInfo)``
      :refid: tabs-on-moved-listener-tab-id-move-info
      :refname: listener(tabId, moveInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _tabs.on^moved.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: tabs-on-moved-tab-id
      :refname: tabId
      :type: (integer)

   .. _tabs.on^moved.move^info:

   .. api-member::
      :name: ``moveInfo``
      :refid: tabs-on-moved-move-info
      :refname: moveInfo
      :type: (object)

      .. _tabs.on^moved.move^info.from^index:

      .. api-member::
         :name: ``fromIndex``
         :refid: tabs-on-moved-move-info-from-index
         :refname: fromIndex
         :type: (integer)

      .. _tabs.on^moved.move^info.to^index:

      .. api-member::
         :name: ``toIndex``
         :refid: tabs-on-moved-move-info-to-index
         :refname: toIndex
         :type: (integer)

      .. _tabs.on^moved.move^info.window^id:

      .. api-member::
         :name: ``windowId``
         :refid: tabs-on-moved-move-info-window-id
         :refname: windowId
         :type: (integer)

.. _tabs.on^removed:

onRemoved
---------

.. api-section-annotation-hack:: -- [Added in TB 62]

Fired when a tab is closed.

.. api-header::
   :label: Parameters for onRemoved.addListener(listener)

   .. _tabs.on^removed.listener(tab^id, remove^info):

   .. api-member::
      :name: ``listener(tabId, removeInfo)``
      :refid: tabs-on-removed-listener-tab-id-remove-info
      :refname: listener(tabId, removeInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _tabs.on^removed.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: tabs-on-removed-tab-id
      :refname: tabId
      :type: (integer)

   .. _tabs.on^removed.remove^info:

   .. api-member::
      :name: ``removeInfo``
      :refid: tabs-on-removed-remove-info
      :refname: removeInfo
      :type: (object)

      .. _tabs.on^removed.remove^info.is^window^closing:

      .. api-member::
         :name: ``isWindowClosing``
         :refid: tabs-on-removed-remove-info-is-window-closing
         :refname: isWindowClosing
         :type: (boolean)

         Is :value:`true` when the tab is being closed because its window is being closed.

      .. _tabs.on^removed.remove^info.window^id:

      .. api-member::
         :name: ``windowId``
         :refid: tabs-on-removed-remove-info-window-id
         :refname: windowId
         :type: (integer)

         The window whose tab is closed.

.. _tabs.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 62]

Fired when a tab is updated.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener, filter)

   .. _tabs.on^updated.listener(tab^id, change^info, tab):

   .. api-member::
      :name: ``listener(tabId, changeInfo, tab)``
      :refid: tabs-on-updated-listener-tab-id-change-info-tab
      :refname: listener(tabId, changeInfo, tab)

      A function that will be called when this event occurs.

   .. _tabs.on^updated.filter:

   .. api-member::
      :name: [``filter``]
      :refid: tabs-on-updated-filter
      :refname: filter
      :type: (:ref:`tabs.^update^filter`, optional)

      A set of filters that restricts the events that will be sent to this listener.

.. api-header::
   :label: Parameters passed to the listener function

   .. _tabs.on^updated.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: tabs-on-updated-tab-id
      :refname: tabId
      :type: (integer)

   .. _tabs.on^updated.change^info:

   .. api-member::
      :name: ``changeInfo``
      :refid: tabs-on-updated-change-info
      :refname: changeInfo
      :type: (object)

      Lists the changes to the state of the tab that was updated.

      .. _tabs.on^updated.change^info.fav^icon^url:

      .. api-member::
         :name: [``favIconUrl``]
         :refid: tabs-on-updated-change-info-fav-icon-url
         :refname: favIconUrl
         :type: (string, optional)

         The tab's new favicon URL.

      .. _tabs.on^updated.change^info.status:

      .. api-member::
         :name: [``status``]
         :refid: tabs-on-updated-change-info-status
         :refname: status
         :type: (string, optional)

         The status of the tab. Can be either :value:`loading` or :value:`complete`.

      .. _tabs.on^updated.change^info.url:

      .. api-member::
         :name: [``url``]
         :refid: tabs-on-updated-change-info-url
         :refname: url
         :type: (string, optional)

         The tab's URL if it has changed.

   .. _tabs.on^updated.tab:

   .. api-member::
      :name: ``tab``
      :refid: tabs-on-updated-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

      Gives the state of the tab that was updated.

.. rst-class:: api-main-section

Types
=====

.. _tabs.^tab:

Tab
---

.. api-section-annotation-hack:: -- [Added in TB 62]

.. api-header::
   :label: object

   .. _tabs.^tab.active:

   .. api-member::
      :name: ``active``
      :refid: tabs-tab-active
      :refname: active
      :type: (boolean)

      Whether the tab is active in its window. (Does not necessarily mean the window is focused.)

   .. _tabs.^tab.highlighted:

   .. api-member::
      :name: ``highlighted``
      :refid: tabs-tab-highlighted
      :refname: highlighted
      :type: (boolean)

      Whether the tab is highlighted. Works as an alias of active

   .. _tabs.^tab.index:

   .. api-member::
      :name: ``index``
      :refid: tabs-tab-index
      :refname: index
      :type: (integer)

      The zero-based index of the tab within its window.

   .. _tabs.^tab.selected:

   .. api-member::
      :name: ``selected``
      :refid: tabs-tab-selected
      :refname: selected
      :type: (boolean) **Unsupported.**

      Whether the tab is selected.

   .. _tabs.^tab.cookie^store^id:

   .. api-member::
      :name: [``cookieStoreId``]
      :refid: tabs-tab-cookie-store-id
      :refname: cookieStoreId
      :type: (string, optional)
      :annotation: -- [Added in TB 115]

      The `CookieStore <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities/ContextualIdentity#cookiestoreid>`__ id used by the tab. Either a custom id created using the `contextualIdentities API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities>`__, or a built-in one: :value:`firefox-default`, :value:`firefox-container-1`, :value:`firefox-container-2`, :value:`firefox-container-3`, :value:`firefox-container-4`, :value:`firefox-container-5`.

      .. note::

         The naming pattern of the built-in cookie stores was deliberately not changed for Thunderbird, but kept for compatibility reasons.

   .. _tabs.^tab.fav^icon^url:

   .. api-member::
      :name: [``favIconUrl``]
      :refid: tabs-tab-fav-icon-url
      :refname: favIconUrl
      :type: (string, optional)

      The URL of the tab's favicon. This property is only present if the extension's manifest includes the :permission:`tabs` permission. It may also be an empty string if the tab is loading.

   .. _tabs.^tab.group^id:

   .. api-member::
      :name: [``groupId``]
      :refid: tabs-tab-group-id
      :refname: groupId
      :type: (integer, optional)
      :annotation: -- [Added in TB 139]

      The ID of the group that the tab belongs to. -1 if the tab does not belong to a tab group.

      .. note::

         Thunderbird does not support tab groups. This property will always be :code:`-1` and cannot be changed.

   .. _tabs.^tab.height:

   .. api-member::
      :name: [``height``]
      :refid: tabs-tab-height
      :refname: height
      :type: (integer, optional)

      The height of the tab in pixels.

   .. _tabs.^tab.id:

   .. api-member::
      :name: [``id``]
      :refid: tabs-tab-id
      :refname: id
      :type: (integer, optional)

      The ID of the tab. Tab IDs are unique within a session. Under some circumstances a Tab may not be assigned an ID. Tab ID can also be set to :ref:`tabs.^t^a^b_^i^d_^n^o^n^e` for apps and devtools windows.

   .. _tabs.^tab.space^id:

   .. api-member::
      :name: [``spaceId``]
      :refid: tabs-tab-space-id
      :refname: spaceId
      :type: (integer, optional)
      :annotation: -- [Added in TB 115]

      The id of the space.

   .. _tabs.^tab.split^view^id:

   .. api-member::
      :name: [``splitViewId``]
      :refid: tabs-tab-split-view-id
      :refname: splitViewId
      :type: (integer, optional)
      :annotation: -- [Added in TB 149]

      The ID of the Split View that the tab belongs to. -1 if the tab does not belong to a split view.

      .. note::

         Thunderbird does not support Split View. This property will always be :code:`-1` and cannot be changed.

   .. _tabs.^tab.status:

   .. api-member::
      :name: [``status``]
      :refid: tabs-tab-status
      :refname: status
      :type: (string, optional)

      Either :value:`loading` or :value:`complete`.

   .. _tabs.^tab.title:

   .. api-member::
      :name: [``title``]
      :refid: tabs-tab-title
      :refname: title
      :type: (string, optional)

      The title of the tab. This property is only present if the extension's manifest includes the :permission:`tabs` permission.

   .. _tabs.^tab.type:

   .. api-member::
      :name: [``type``]
      :refid: tabs-tab-type
      :refname: type
      :type: (:ref:`tabs.^tab^type`, optional)
      :annotation: -- [Added in TB 92]

   .. _tabs.^tab.url:

   .. api-member::
      :name: [``url``]
      :refid: tabs-tab-url
      :refname: url
      :type: (string, optional)

      The URL the tab is displaying. This property is only present if the extension's manifest includes the :permission:`tabs` permission.

   .. _tabs.^tab.width:

   .. api-member::
      :name: [``width``]
      :refid: tabs-tab-width
      :refname: width
      :type: (integer, optional)

      The width of the tab in pixels.

   .. _tabs.^tab.window^id:

   .. api-member::
      :name: [``windowId``]
      :refid: tabs-tab-window-id
      :refname: windowId
      :type: (integer, optional)

      The ID of the window the tab is contained within.

.. _tabs.^tab^status:

TabStatus
---------

.. api-section-annotation-hack:: -- [Added in TB 62]

Whether the tabs have completed loading.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _tabs.^tab^status.complete:

         .. api-member::
            :name: :value:`complete`
            :refid: tabs-tab-status-complete
            :refname: complete

         .. _tabs.^tab^status.loading:

         .. api-member::
            :name: :value:`loading`
            :refid: tabs-tab-status-loading
            :refname: loading

.. _tabs.^tab^type:

TabType
-------

.. api-section-annotation-hack:: -- [Added in TB 121]

Tab types supported by the tabs API.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _tabs.^tab^type.address^book:

         .. api-member::
            :name: :value:`addressBook`
            :refid: tabs-tab-type-address-book
            :refname: addressBook

         .. _tabs.^tab^type.calendar:

         .. api-member::
            :name: :value:`calendar`
            :refid: tabs-tab-type-calendar
            :refname: calendar

         .. _tabs.^tab^type.calendar^event:

         .. api-member::
            :name: :value:`calendarEvent`
            :refid: tabs-tab-type-calendar-event
            :refname: calendarEvent

         .. _tabs.^tab^type.calendar^task:

         .. api-member::
            :name: :value:`calendarTask`
            :refid: tabs-tab-type-calendar-task
            :refname: calendarTask

         .. _tabs.^tab^type.chat:

         .. api-member::
            :name: :value:`chat`
            :refid: tabs-tab-type-chat
            :refname: chat

         .. _tabs.^tab^type.content:

         .. api-member::
            :name: :value:`content`
            :refid: tabs-tab-type-content
            :refname: content

         .. _tabs.^tab^type.mail:

         .. api-member::
            :name: :value:`mail`
            :refid: tabs-tab-type-mail
            :refname: mail

         .. _tabs.^tab^type.message^compose:

         .. api-member::
            :name: :value:`messageCompose`
            :refid: tabs-tab-type-message-compose
            :refname: messageCompose

         .. _tabs.^tab^type.message^display:

         .. api-member::
            :name: :value:`messageDisplay`
            :refid: tabs-tab-type-message-display
            :refname: messageDisplay

         .. _tabs.^tab^type.special:

         .. api-member::
            :name: :value:`special`
            :refid: tabs-tab-type-special
            :refname: special

         .. _tabs.^tab^type.tasks:

         .. api-member::
            :name: :value:`tasks`
            :refid: tabs-tab-type-tasks
            :refname: tasks

.. _tabs.^update^filter:

UpdateFilter
------------

.. api-section-annotation-hack:: -- [Added in TB 62]

An object describing filters to apply to :ref:`tabs.on^updated` events.

.. api-header::
   :label: object

   .. _tabs.^update^filter.properties:

   .. api-member::
      :name: [``properties``]
      :refid: tabs-update-filter-properties
      :refname: properties
      :type: (array of :ref:`tabs.^update^property^name`, optional)

      A list of property names. Events that do not match any of the names will be filtered out.

   .. _tabs.^update^filter.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: tabs-update-filter-tab-id
      :refname: tabId
      :type: (integer, optional)

   .. _tabs.^update^filter.urls:

   .. api-member::
      :name: [``urls``]
      :refid: tabs-update-filter-urls
      :refname: urls
      :type: (array of string, optional)

      A list of URLs or URL patterns. Events that cannot match any of the URLs will be filtered out. Filtering with urls requires the :permission:`tabs` or :permission:`activeTab` permission.

   .. _tabs.^update^filter.window^id:

   .. api-member::
      :name: [``windowId``]
      :refid: tabs-update-filter-window-id
      :refname: windowId
      :type: (integer, optional)

.. _tabs.^update^property^name:

UpdatePropertyName
------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Event names supported in :ref:`tabs.on^updated`.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _tabs.^update^property^name.fav^icon^url:

         .. api-member::
            :name: :value:`favIconUrl`
            :refid: tabs-update-property-name-fav-icon-url
            :refname: favIconUrl

         .. _tabs.^update^property^name.status:

         .. api-member::
            :name: :value:`status`
            :refid: tabs-update-property-name-status
            :refname: status

         .. _tabs.^update^property^name.title:

         .. api-member::
            :name: :value:`title`
            :refid: tabs-update-property-name-title
            :refname: title

.. _tabs.^window^type:

WindowType
----------

.. api-section-annotation-hack:: -- [Added in TB 62]

The type of a window. Under some circumstances a Window may not be assigned a type property.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _tabs.^window^type.app:

         .. api-member::
            :name: :value:`app`
            :refid: tabs-window-type-app
            :refname: app

         .. _tabs.^window^type.devtools:

         .. api-member::
            :name: :value:`devtools`
            :refid: tabs-window-type-devtools
            :refname: devtools

         .. _tabs.^window^type.message^compose:

         .. api-member::
            :name: :value:`messageCompose`
            :refid: tabs-window-type-message-compose
            :refname: messageCompose
            :annotation: -- [Added in TB 88]

         .. _tabs.^window^type.message^display:

         .. api-member::
            :name: :value:`messageDisplay`
            :refid: tabs-window-type-message-display
            :refname: messageDisplay
            :annotation: -- [Added in TB 88]

         .. _tabs.^window^type.normal:

         .. api-member::
            :name: :value:`normal`
            :refid: tabs-window-type-normal
            :refname: normal

         .. _tabs.^window^type.panel:

         .. api-member::
            :name: :value:`panel`
            :refid: tabs-window-type-panel
            :refname: panel

         .. _tabs.^window^type.popup:

         .. api-member::
            :name: :value:`popup`
            :refid: tabs-window-type-popup
            :refname: popup

.. rst-class:: api-main-section

Properties
==========

.. _tabs.^t^a^b_^i^d_^n^o^n^e:

TAB_ID_NONE
-----------

.. api-section-annotation-hack:: -- [Added in TB 62]

An ID which represents the absence of a tab.
