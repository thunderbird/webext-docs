.. container:: sticky-sidebar

  ≡ windows API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

===========
windows API
===========

.. role:: permission

.. role:: value

.. role:: code

The windows API supports creating, modifying and interacting with Thunderbird windows.

.. note::

   This API can be used with Thunderbird's main window and popup windows, both of which support web tabs, as well as with other window types like the composer window, which does not. Ensure your code handles each window type appropriately based on its capabilities.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _windows.permission.contextual^identities:

.. api-member::
   :name: :permission:`contextualIdentities`
   :refid: windows-permission-contextual-identities
   :refname: contextualIdentities

   Grant access to some or all methods of the contextualIdentities API.

.. _windows.permission.cookies:

.. api-member::
   :name: :permission:`cookies`
   :refid: windows-permission-cookies
   :refname: cookies

   Grant access to some or all methods of the cookies API.

.. _windows.permission.tabs:

.. api-member::
   :name: :permission:`tabs`
   :refid: windows-permission-tabs
   :refname: tabs

   Grant host permission to all active and inactive tabs, allowing to read :value:`title`, :value:`url` and :value:`favIconUrl` properties, or to inject content scripts.

.. rst-class:: api-main-section

Functions
=========

.. _windows.create:

create([createData])
--------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Creates (opens) a new window with any optional sizing, position or default URL provided. When loading a page into a popup window, same-site links are opened within the same window, all other links are opened in the user's default browser. To override this behavior, add-ons have to register a `content script <https://bugzilla.mozilla.org/show_bug.cgi?id=1618828#c3>`__ , capture click events and handle them manually. Same-site links with targets other than :value:`_self` are opened in a new tab in the most recent :value:`normal` Thunderbird window.

.. api-header::
   :label: Parameters

   .. _windows.create.create^data:

   .. api-member::
      :name: [``createData``]
      :refid: windows-create-create-data
      :refname: createData
      :type: (object, optional)

      .. _windows.create.create^data.allow^scripts^to^close:

      .. api-member::
         :name: [``allowScriptsToClose``]
         :refid: windows-create-create-data-allow-scripts-to-close
         :refname: allowScriptsToClose
         :type: (boolean, optional)

         Allow scripts running inside the window to close the window by calling :code:`window.close()`. Defaults to :value:`true` when the given URL points to an extension page (a page included with this extension and loaded with the :value:`moz-extension:` protocol), defaults to :value:`false` otherwise.

      .. _windows.create.create^data.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: windows-create-create-data-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)
         :annotation: -- [Added in TB 115]

         The `CookieStore <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities/ContextualIdentity#cookiestoreid>`__ id which all initially opened tabs should use. Either a custom id created using the `contextualIdentities API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities>`__, or a built-in one: :value:`firefox-default`, :value:`firefox-container-1`, :value:`firefox-container-2`, :value:`firefox-container-3`, :value:`firefox-container-4`, :value:`firefox-container-5`.

         .. note::

            The naming pattern of the built-in cookie stores was deliberately not changed for Thunderbird, but kept for compatibility reasons.

         .. note::

            The :permission:`cookies` permission is required to be able to specify this property. Furthermore, the :permission:`contextualIdentities` permission should be requested, to enable the contextual identities feature (enabled by default only on Thunderbird Daily).

      .. _windows.create.create^data.focused:

      .. api-member::
         :name: [``focused``]
         :refid: windows-create-create-data-focused
         :refname: focused
         :type: (boolean, optional) **Unsupported.**

         If true, opens an active window. If false, opens an inactive window.

      .. _windows.create.create^data.height:

      .. api-member::
         :name: [``height``]
         :refid: windows-create-create-data-height
         :refname: height
         :type: (integer, optional)

         The height in pixels of the new window, including the frame. If not specified defaults to a natural height.

      .. _windows.create.create^data.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: windows-create-create-data-incognito
         :refname: incognito
         :type: (boolean, optional) **Unsupported.**

      .. _windows.create.create^data.left:

      .. api-member::
         :name: [``left``]
         :refid: windows-create-create-data-left
         :refname: left
         :type: (integer, optional)

         The number of pixels to position the new window from the left edge of the screen. If not specified, the new window is offset naturally from the last focused window.

      .. _windows.create.create^data.link^handler:

      .. api-member::
         :name: [``linkHandler``]
         :refid: windows-create-create-data-link-handler
         :refname: linkHandler
         :type: (`string`, optional)
         :annotation: -- [Added in TB 136]

         Thunderbird is a mail client, not a browser. It is possible to load a web page, but opening follow-up pages through hyperlinks should be handled by the user's default browser. This property specifies to what extent this behavior should be enforced. The default :value:`balanced` link handler will open links to the same host directly in Thunderbird, everything else will be opened in the user's default browser. A :value:`relaxed` link handler will open all links inside of Thunderbird, a :value:`strict` link handler will open all links in the user's default browser, except links to the same page.

         Supported values:

         .. _windows.create.create^data.link^handler.balanced:

         .. api-member::
            :name: :value:`balanced`
            :refid: windows-create-create-data-link-handler-balanced
            :refname: balanced

         .. _windows.create.create^data.link^handler.relaxed:

         .. api-member::
            :name: :value:`relaxed`
            :refid: windows-create-create-data-link-handler-relaxed
            :refname: relaxed

         .. _windows.create.create^data.link^handler.strict:

         .. api-member::
            :name: :value:`strict`
            :refid: windows-create-create-data-link-handler-strict
            :refname: strict

      .. _windows.create.create^data.state:

      .. api-member::
         :name: [``state``]
         :refid: windows-create-create-data-state
         :refname: state
         :type: (:ref:`windows.^window^state`, optional)

         The initial state of the window. The :value:`minimized`, :value:`maximized` and :value:`fullscreen` states cannot be combined with :value:`left`, :value:`top`, :value:`width` or :value:`height`.

      .. _windows.create.create^data.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: windows-create-create-data-tab-id
         :refname: tabId
         :type: (integer, optional)

         The id of the tab for which you want to adopt to the new window.

      .. _windows.create.create^data.title^preface:

      .. api-member::
         :name: [``titlePreface``]
         :refid: windows-create-create-data-title-preface
         :refname: titlePreface
         :type: (string, optional)

         A string to add to the beginning of the window title.

      .. _windows.create.create^data.top:

      .. api-member::
         :name: [``top``]
         :refid: windows-create-create-data-top
         :refname: top
         :type: (integer, optional)

         The number of pixels to position the new window from the top edge of the screen. If not specified, the new window is offset naturally from the last focused window.

      .. _windows.create.create^data.type:

      .. api-member::
         :name: [``type``]
         :refid: windows-create-create-data-type
         :refname: type
         :type: (:ref:`windows.^create^type`, optional)

         Specifies what type of window to create. Thunderbird does not support :value:`panel` and :value:`detached_panel`, they are interpreted as :value:`popup`.

      .. _windows.create.create^data.url:

      .. api-member::
         :name: [``url``]
         :refid: windows-create-create-data-url
         :refname: url
         :type: (string or array of string, optional)

         A URL to be opened in a popup window, ignored in all other window types. This may also be an array, but only the first element is used (popup windows may not have multiple tabs). If the URL points to a content page (a web page, an extension page or a registered WebExtension protocol handler page), the popup window will navigate to the requested page. All other URLs will be opened externally after creating an empty popup window. Fully-qualified URLs must include a scheme (i.e. :value:`http://www.google.com`, not :value:`www.google.com`). Relative URLs will be relative to the root of the extension. Defaults to the New Tab Page.

      .. _windows.create.create^data.width:

      .. api-member::
         :name: [``width``]
         :refid: windows-create-create-data-width
         :refname: width
         :type: (integer, optional)

         The width in pixels of the new window, including the frame. If not specified defaults to a natural width.

.. api-header::
   :label: Return type (`Promise`_)

   .. _windows.create.returns:

   .. api-member::
      :refid: windows-create-returns
      :refname: _returns
      :type: :ref:`windows.^window`

      Contains details about the created window.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.get:

get(windowId, [getInfo])
------------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Gets details about a window.

.. api-header::
   :label: Parameters

   .. _windows.get.window^id:

   .. api-member::
      :name: ``windowId``
      :refid: windows-get-window-id
      :refname: windowId
      :type: (integer)

   .. _windows.get.get^info:

   .. api-member::
      :name: [``getInfo``]
      :refid: windows-get-get-info
      :refname: getInfo
      :type: (:ref:`windows.^get^info`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _windows.get.returns:

   .. api-member::
      :refid: windows-get-returns
      :refname: _returns
      :type: :ref:`windows.^window`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.get^all:

getAll([getInfo])
-----------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Gets all windows.

.. api-header::
   :label: Parameters

   .. _windows.get^all.get^info:

   .. api-member::
      :name: [``getInfo``]
      :refid: windows-get-all-get-info
      :refname: getInfo
      :type: (:ref:`windows.^get^info`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _windows.get^all.returns:

   .. api-member::
      :refid: windows-get-all-returns
      :refname: _returns
      :type: array of :ref:`windows.^window`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.get^current:

getCurrent([getInfo])
---------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Gets the active or topmost window.

.. api-header::
   :label: Parameters

   .. _windows.get^current.get^info:

   .. api-member::
      :name: [``getInfo``]
      :refid: windows-get-current-get-info
      :refname: getInfo
      :type: (:ref:`windows.^get^info`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _windows.get^current.returns:

   .. api-member::
      :refid: windows-get-current-returns
      :refname: _returns
      :type: :ref:`windows.^window`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.get^last^focused:

getLastFocused([getInfo])
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Gets the window that was most recently focused — typically the window 'on top'.

.. api-header::
   :label: Parameters

   .. _windows.get^last^focused.get^info:

   .. api-member::
      :name: [``getInfo``]
      :refid: windows-get-last-focused-get-info
      :refname: getInfo
      :type: (:ref:`windows.^get^info`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _windows.get^last^focused.returns:

   .. api-member::
      :refid: windows-get-last-focused-returns
      :refname: _returns
      :type: :ref:`windows.^window`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.open^default^browser:

openDefaultBrowser(url)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 84]

Opens the provided URL in the default system browser.

.. api-header::
   :label: Parameters

   .. _windows.open^default^browser.url:

   .. api-member::
      :name: ``url``
      :refid: windows-open-default-browser-url
      :refname: url
      :type: (string)

.. _windows.remove:

remove(windowId)
----------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Removes (closes) a window, and all the tabs inside it.

.. api-header::
   :label: Parameters

   .. _windows.remove.window^id:

   .. api-member::
      :name: ``windowId``
      :refid: windows-remove-window-id
      :refname: windowId
      :type: (integer)

.. _windows.update:

update(windowId, updateInfo)
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Updates the properties of a window. Specify only the properties that you want to change; unspecified properties will be left unchanged.

.. api-header::
   :label: Parameters

   .. _windows.update.window^id:

   .. api-member::
      :name: ``windowId``
      :refid: windows-update-window-id
      :refname: windowId
      :type: (integer)

   .. _windows.update.update^info:

   .. api-member::
      :name: ``updateInfo``
      :refid: windows-update-update-info
      :refname: updateInfo
      :type: (object)

      .. _windows.update.update^info.draw^attention:

      .. api-member::
         :name: [``drawAttention``]
         :refid: windows-update-update-info-draw-attention
         :refname: drawAttention
         :type: (boolean, optional)

         Setting this to :value:`true` will cause the window to be displayed in a manner that draws the user's attention to the window, without changing the focused window. The effect lasts until the user changes focus to the window. This option has no effect if the window already has focus.

      .. _windows.update.update^info.focused:

      .. api-member::
         :name: [``focused``]
         :refid: windows-update-update-info-focused
         :refname: focused
         :type: (boolean, optional)

         If true, brings the window to the front. If false, brings the next window in the z-order to the front.

      .. _windows.update.update^info.height:

      .. api-member::
         :name: [``height``]
         :refid: windows-update-update-info-height
         :refname: height
         :type: (integer, optional)

         The height to resize the window to in pixels.

      .. _windows.update.update^info.left:

      .. api-member::
         :name: [``left``]
         :refid: windows-update-update-info-left
         :refname: left
         :type: (integer, optional)

         The offset from the left edge of the screen to move the window to in pixels. This value is ignored for panels.

      .. _windows.update.update^info.state:

      .. api-member::
         :name: [``state``]
         :refid: windows-update-update-info-state
         :refname: state
         :type: (:ref:`windows.^window^state`, optional)

         The new state of the window. The :value:`minimized`, :value:`maximized` and :value:`fullscreen` states cannot be combined with :value:`left`, :value:`top`, :value:`width` or :value:`height`.

      .. _windows.update.update^info.title^preface:

      .. api-member::
         :name: [``titlePreface``]
         :refid: windows-update-update-info-title-preface
         :refname: titlePreface
         :type: (string, optional)

         A string to add to the beginning of the window title.

      .. _windows.update.update^info.top:

      .. api-member::
         :name: [``top``]
         :refid: windows-update-update-info-top
         :refname: top
         :type: (integer, optional)

         The offset from the top edge of the screen to move the window to in pixels. This value is ignored for panels.

      .. _windows.update.update^info.width:

      .. api-member::
         :name: [``width``]
         :refid: windows-update-update-info-width
         :refname: width
         :type: (integer, optional)

         The width to resize the window to in pixels.

.. api-header::
   :label: Return type (`Promise`_)

   .. _windows.update.returns:

   .. api-member::
      :refid: windows-update-returns
      :refname: _returns
      :type: :ref:`windows.^window`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _windows.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 62]

Fired when a window is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _windows.on^created.listener(window):

   .. api-member::
      :name: ``listener(window)``
      :refid: windows-on-created-listener-window
      :refname: listener(window)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _windows.on^created.window:

   .. api-member::
      :name: ``window``
      :refid: windows-on-created-window
      :refname: window
      :type: (:ref:`windows.^window`)

      Details of the window that was created.

.. _windows.on^focus^changed:

onFocusChanged
--------------

.. api-section-annotation-hack:: -- [Added in TB 62]

Fired when the currently focused window changes. Will be :ref:`windows.^w^i^n^d^o^w_^i^d_^n^o^n^e`, if all windows have lost focus.

.. note::

   On some Linux window managers, WINDOW_ID_NONE will always be sent immediately preceding a switch from one window to another.

.. api-header::
   :label: Parameters for onFocusChanged.addListener(listener)

   .. _windows.on^focus^changed.listener(window^id):

   .. api-member::
      :name: ``listener(windowId)``
      :refid: windows-on-focus-changed-listener-window-id
      :refname: listener(windowId)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _windows.on^focus^changed.window^id:

   .. api-member::
      :name: ``windowId``
      :refid: windows-on-focus-changed-window-id
      :refname: windowId
      :type: (integer)

      ID of the newly focused window.

.. _windows.on^removed:

onRemoved
---------

.. api-section-annotation-hack:: -- [Added in TB 62]

Fired when a window is removed (closed).

.. api-header::
   :label: Parameters for onRemoved.addListener(listener)

   .. _windows.on^removed.listener(window^id):

   .. api-member::
      :name: ``listener(windowId)``
      :refid: windows-on-removed-listener-window-id
      :refname: listener(windowId)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _windows.on^removed.window^id:

   .. api-member::
      :name: ``windowId``
      :refid: windows-on-removed-window-id
      :refname: windowId
      :type: (integer)

      ID of the removed window.

.. rst-class:: api-main-section

Types
=====

.. _windows.^create^type:

CreateType
----------

.. api-section-annotation-hack:: -- [Added in TB 62]

Specifies what type of window to create. Thunderbird does not support :value:`panel` and :value:`detached_panel`, they are interpreted as :value:`popup`.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _windows.^create^type.detached_panel:

         .. api-member::
            :name: :value:`detached_panel`
            :refid: windows-create-type-detached-panel
            :refname: detached_panel

            Not supported, same as :value:`popup`

         .. _windows.^create^type.normal:

         .. api-member::
            :name: :value:`normal`
            :refid: windows-create-type-normal
            :refname: normal

            A normal Thunderbird window, a.k.a. 3-pane-window (folder pane, message pane and preview pane).

         .. _windows.^create^type.panel:

         .. api-member::
            :name: :value:`panel`
            :refid: windows-create-type-panel
            :refname: panel

            Not supported, same as :value:`popup`

         .. _windows.^create^type.popup:

         .. api-member::
            :name: :value:`popup`
            :refid: windows-create-type-popup
            :refname: popup

            A non-modal stand-alone popup window.

.. _windows.^get^info:

GetInfo
-------

.. api-section-annotation-hack:: -- [Added in TB 78]

Specifies additional requirements for the returned windows.

.. api-header::
   :label: object

   .. _windows.^get^info.populate:

   .. api-member::
      :name: [``populate``]
      :refid: windows-get-info-populate
      :refname: populate
      :type: (boolean, optional)

      If true, the :ref:`windows.^window` returned will have a :value:`tabs` property that contains an array of :ref:`tabs.^tab` objects representing the tabs inside the window. The :ref:`tabs.^tab` objects only contain the :value:`url`, :value:`title` and :value:`favIconUrl` properties if the extension's manifest file includes the :permission:`tabs` permission.

   .. _windows.^get^info.window^types:

   .. api-member::
      :name: [``windowTypes``]
      :refid: windows-get-info-window-types
      :refname: windowTypes
      :type: (array of :ref:`windows.^window^type`, optional)

      If set, the :ref:`windows.^window` returned will be filtered based on its type. Supported by :ref:`windows.get^all` only, ignored in all other functions.

.. _windows.^window:

Window
------

.. api-section-annotation-hack:: -- [Added in TB 62]

.. api-header::
   :label: object

   .. _windows.^window.always^on^top:

   .. api-member::
      :name: ``alwaysOnTop``
      :refid: windows-window-always-on-top
      :refname: alwaysOnTop
      :type: (boolean)

      Whether the window is set to be always on top.

   .. _windows.^window.focused:

   .. api-member::
      :name: ``focused``
      :refid: windows-window-focused
      :refname: focused
      :type: (boolean)

      Whether the window is currently the focused window.

   .. _windows.^window.incognito:

   .. api-member::
      :name: ``incognito``
      :refid: windows-window-incognito
      :refname: incognito
      :type: (boolean)

      Whether the window is incognito. Since Thunderbird does not support the incognito mode, this is always :value:`false`.

   .. _windows.^window.height:

   .. api-member::
      :name: [``height``]
      :refid: windows-window-height
      :refname: height
      :type: (integer, optional)

      The height of the window, including the frame, in pixels.

   .. _windows.^window.id:

   .. api-member::
      :name: [``id``]
      :refid: windows-window-id
      :refname: id
      :type: (integer, optional)

      The ID of the window. Window IDs are unique within a session.

   .. _windows.^window.left:

   .. api-member::
      :name: [``left``]
      :refid: windows-window-left
      :refname: left
      :type: (integer, optional)

      The offset of the window from the left edge of the screen in pixels.

   .. _windows.^window.state:

   .. api-member::
      :name: [``state``]
      :refid: windows-window-state
      :refname: state
      :type: (:ref:`windows.^window^state`, optional)

      The state of this window.

   .. _windows.^window.tabs:

   .. api-member::
      :name: [``tabs``]
      :refid: windows-window-tabs
      :refname: tabs
      :type: (array of :ref:`tabs.^tab`, optional)

      Array of :ref:`tabs.^tab` objects representing the current tabs in the window. Only included if requested by :ref:`windows.get`, :ref:`windows.get^current`, :ref:`windows.get^all` or :ref:`windows.get^last^focused`, and the optional :ref:`windows.^get^info` parameter has its :value:`populate` member set to :value:`true`.

   .. _windows.^window.title:

   .. api-member::
      :name: [``title``]
      :refid: windows-window-title
      :refname: title
      :type: (string, optional)

      The title of the window. Read-only.

   .. _windows.^window.top:

   .. api-member::
      :name: [``top``]
      :refid: windows-window-top
      :refname: top
      :type: (integer, optional)

      The offset of the window from the top edge of the screen in pixels.

   .. _windows.^window.type:

   .. api-member::
      :name: [``type``]
      :refid: windows-window-type
      :refname: type
      :type: (:ref:`windows.^window^type`, optional)

      The type of window this is.

   .. _windows.^window.width:

   .. api-member::
      :name: [``width``]
      :refid: windows-window-width
      :refname: width
      :type: (integer, optional)

      The width of the window, including the frame, in pixels.

.. _windows.^window^state:

WindowState
-----------

.. api-section-annotation-hack:: -- [Added in TB 62]

The state of this window.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _windows.^window^state.docked:

         .. api-member::
            :name: :value:`docked`
            :refid: windows-window-state-docked
            :refname: docked

         .. _windows.^window^state.fullscreen:

         .. api-member::
            :name: :value:`fullscreen`
            :refid: windows-window-state-fullscreen
            :refname: fullscreen

         .. _windows.^window^state.maximized:

         .. api-member::
            :name: :value:`maximized`
            :refid: windows-window-state-maximized
            :refname: maximized

         .. _windows.^window^state.minimized:

         .. api-member::
            :name: :value:`minimized`
            :refid: windows-window-state-minimized
            :refname: minimized

         .. _windows.^window^state.normal:

         .. api-member::
            :name: :value:`normal`
            :refid: windows-window-state-normal
            :refname: normal

.. _windows.^window^type:

WindowType
----------

.. api-section-annotation-hack:: -- [Added in TB 62]

The type of a window. Under some circumstances a window may not be assigned a type property.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _windows.^window^type.message^compose:

         .. api-member::
            :name: :value:`messageCompose`
            :refid: windows-window-type-message-compose
            :refname: messageCompose
            :annotation: -- [Added in TB 70]

            A non-modal stand-alone message compose window.

         .. _windows.^window^type.message^display:

         .. api-member::
            :name: :value:`messageDisplay`
            :refid: windows-window-type-message-display
            :refname: messageDisplay
            :annotation: -- [Added in TB 70]

            A non-modal stand-alone message display window, viewing a single message.

         .. _windows.^window^type.normal:

         .. api-member::
            :name: :value:`normal`
            :refid: windows-window-type-normal
            :refname: normal

            A normal Thunderbird window, a.k.a. 3-pane-window (folder pane, message pane and preview pane).

         .. _windows.^window^type.popup:

         .. api-member::
            :name: :value:`popup`
            :refid: windows-window-type-popup
            :refname: popup

            A non-modal stand-alone popup window.

.. rst-class:: api-main-section

Properties
==========

.. _windows.^w^i^n^d^o^w_^i^d_^c^u^r^r^e^n^t:

WINDOW_ID_CURRENT
-----------------

.. api-section-annotation-hack:: 

The windowId value that represents the current window.

.. _windows.^w^i^n^d^o^w_^i^d_^n^o^n^e:

WINDOW_ID_NONE
--------------

.. api-section-annotation-hack:: 

The windowId value that represents the absence of a window.
