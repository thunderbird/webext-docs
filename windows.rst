=======
windows
=======

Use the ``browser.windows`` API to interact with browser windows. You can use this API to create, modify, and rearrange windows in the browser.

Functions
=========

.. _windows.get:

get(windowId, [getInfo])
------------------------

Gets details about a window.

- ``windowId`` (integer)
- [``getInfo``] (object) 

  - [``populate``] (boolean) If true, the $(ref:windows.Window) object will have a ``tabs`` property that contains a list of the $(ref:tabs.Tab) objects. The ``Tab`` objects only contain the ``url``, ``title`` and ``favIconUrl`` properties if the extension's manifest file includes the ``"tabs"`` permission.
  - [``windowTypes``] (array of :ref:`windows.WindowType`) If set, the $(ref:windows.Window) returned will be filtered based on its type. If unset the default filter is set to ``['app', 'normal', 'panel', 'popup']``, with ``'app'`` and ``'panel'`` window types limited to the extension's own windows.

Returns:

- :ref:`windows.Window`

.. _windows.getCurrent:

getCurrent([getInfo])
---------------------

Gets the $(topic:current-window)[current window].

- [``getInfo``] (object) 

  - [``populate``] (boolean) If true, the $(ref:windows.Window) object will have a ``tabs`` property that contains a list of the $(ref:tabs.Tab) objects. The ``Tab`` objects only contain the ``url``, ``title`` and ``favIconUrl`` properties if the extension's manifest file includes the ``"tabs"`` permission.
  - [``windowTypes``] (array of :ref:`windows.WindowType`) If set, the $(ref:windows.Window) returned will be filtered based on its type. If unset the default filter is set to ``['app', 'normal', 'panel', 'popup']``, with ``'app'`` and ``'panel'`` window types limited to the extension's own windows.

Returns:

- :ref:`windows.Window`

.. _windows.getLastFocused:

getLastFocused([getInfo])
-------------------------

Gets the window that was most recently focused &mdash; typically the window 'on top'.

- [``getInfo``] (object) 

  - [``populate``] (boolean) If true, the $(ref:windows.Window) object will have a ``tabs`` property that contains a list of the $(ref:tabs.Tab) objects. The ``Tab`` objects only contain the ``url``, ``title`` and ``favIconUrl`` properties if the extension's manifest file includes the ``"tabs"`` permission.
  - [``windowTypes``] (array of :ref:`windows.WindowType`) If set, the $(ref:windows.Window) returned will be filtered based on its type. If unset the default filter is set to ``['app', 'normal', 'panel', 'popup']``, with ``'app'`` and ``'panel'`` window types limited to the extension's own windows.

Returns:

- :ref:`windows.Window`

.. _windows.getAll:

getAll([getInfo])
-----------------

Gets all windows.

- [``getInfo``] (object) 

  - [``populate``] (boolean) If true, each $(ref:windows.Window) object will have a ``tabs`` property that contains a list of the $(ref:tabs.Tab) objects for that window. The ``Tab`` objects only contain the ``url``, ``title`` and ``favIconUrl`` properties if the extension's manifest file includes the ``"tabs"`` permission.
  - [``windowTypes``] (array of :ref:`windows.WindowType`) If set, the $(ref:windows.Window) returned will be filtered based on its type. If unset the default filter is set to ``['app', 'normal', 'panel', 'popup']``, with ``'app'`` and ``'panel'`` window types limited to the extension's own windows.

Returns:

- array of :ref:`windows.Window`

.. _windows.create:

create([createData])
--------------------

Creates (opens) a new browser with any optional sizing, position or default URL provided.

- [``createData``] (object)

  - [``allowScriptsToClose``] (boolean) Allow scripts to close the window.
  - [``focused``] (boolean) If true, opens an active window. If false, opens an inactive window.
  - [``height``] (integer) The height in pixels of the new window, including the frame. If not specified defaults to a natural height.
  - [``incognito``] (boolean) Whether the new window should be an incognito window.
  - [``left``] (integer) The number of pixels to position the new window from the left edge of the screen. If not specified, the new window is offset naturally from the last focused window. This value is ignored for panels.
  - [``state``] (:ref:`windows.WindowState`) The initial state of the window. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined with 'left', 'top', 'width' or 'height'.
  - [``tabId``] (integer) The id of the tab for which you want to adopt to the new window.
  - [``titlePreface``] (string) A string to add to the beginning of the window title.
  - [``top``] (integer) The number of pixels to position the new window from the top edge of the screen. If not specified, the new window is offset naturally from the last focused window. This value is ignored for panels.
  - [``type``] (:ref:`windows.CreateType`) Specifies what type of browser window to create. The 'panel' and 'detached_panel' types create a popup unless the '--enable-panels' flag is set.
  - [``url``] (string or array of string) A URL or array of URLs to open as tabs in the window. Fully-qualified URLs must include a scheme (i.e. 'http://www.google.com', not 'www.google.com'). Relative URLs will be relative to the current page within the extension. Defaults to the New Tab Page.
  - [``width``] (integer) The width in pixels of the new window, including the frame. If not specified defaults to a natural width.

Returns:

- :ref:`windows.Window` Contains details about the created window.

.. _windows.update:

update(windowId, updateInfo)
----------------------------

Updates the properties of a window. Specify only the properties that you want to change; unspecified properties will be left unchanged.

- ``windowId`` (integer)
- ``updateInfo`` (object)

  - [``drawAttention``] (boolean) If true, causes the window to be displayed in a manner that draws the user's attention to the window, without changing the focused window. The effect lasts until the user changes focus to the window. This option has no effect if the window already has focus. Set to false to cancel a previous draw attention request.
  - [``focused``] (boolean) If true, brings the window to the front. If false, brings the next window in the z-order to the front.
  - [``height``] (integer) The height to resize the window to in pixels. This value is ignored for panels.
  - [``left``] (integer) The offset from the left edge of the screen to move the window to in pixels. This value is ignored for panels.
  - [``state``] (:ref:`windows.WindowState`) The new state of the window. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined with 'left', 'top', 'width' or 'height'.
  - [``titlePreface``] (string) A string to add to the beginning of the window title.
  - [``top``] (integer) The offset from the top edge of the screen to move the window to in pixels. This value is ignored for panels.
  - [``width``] (integer) The width to resize the window to in pixels. This value is ignored for panels.

Returns:

- :ref:`windows.Window`

.. _windows.remove:

remove(windowId)
----------------

Removes (closes) a window, and all the tabs inside it.

- ``windowId`` (integer)

Events
======

.. _windows.onCreated:

onCreated(window)
-----------------

Fired when a window is created.

- ``window`` (:ref:`windows.Window`) Details of the window that was created.

.. _windows.onRemoved:

onRemoved(windowId)
-------------------

Fired when a window is removed (closed).

- ``windowId`` (integer) ID of the removed window.

.. _windows.onFocusChanged:

onFocusChanged(windowId)
------------------------

Fired when the currently focused window changes. Will be $(ref:windows.WINDOW_ID_NONE) if all browser windows have lost focus. Note: On some Linux window managers, WINDOW_ID_NONE will always be sent immediately preceding a switch from one browser window to another.

- ``windowId`` (integer) ID of the newly focused window.

Types
=====

.. _windows.CreateType:

CreateType
----------

Specifies what type of browser window to create. The 'panel' and 'detached_panel' types create a popup unless the '--enable-panels' flag is set.

.. _windows.Window:

Window
------

- ``alwaysOnTop`` (boolean) Whether the window is set to be always on top.
- ``focused`` (boolean) Whether the window is currently the focused window.
- ``incognito`` (boolean) Whether the window is incognito.
- [``height``] (integer) The height of the window, including the frame, in pixels. Under some circumstances a Window may not be assigned height property, for example when querying closed windows from the $(ref:sessions) API.
- [``id``] (integer) The ID of the window. Window IDs are unique within a browser session. Under some circumstances a Window may not be assigned an ID, for example when querying windows using the $(ref:sessions) API, in which case a session ID may be present.
- [``left``] (integer) The offset of the window from the left edge of the screen in pixels. Under some circumstances a Window may not be assigned left property, for example when querying closed windows from the $(ref:sessions) API.
- [``sessionId``] (string) The session ID used to uniquely identify a Window obtained from the $(ref:sessions) API.
- [``state``] (:ref:`windows.WindowState`) The state of this browser window.
- [``tabs``] (array of :ref:`tabs.Tab`) Array of $(ref:tabs.Tab) objects representing the current tabs in the window.
- [``title``] (string) The title of the window. Read-only.
- [``top``] (integer) The offset of the window from the top edge of the screen in pixels. Under some circumstances a Window may not be assigned top property, for example when querying closed windows from the $(ref:sessions) API.
- [``type``] (:ref:`windows.WindowType`) The type of browser window this is.
- [``width``] (integer) The width of the window, including the frame, in pixels. Under some circumstances a Window may not be assigned width property, for example when querying closed windows from the $(ref:sessions) API.

.. _windows.WindowState:

WindowState
-----------

The state of this browser window. Under some circumstances a Window may not be assigned state property, for example when querying closed windows from the $(ref:sessions) API.

.. _windows.WindowType:

WindowType
----------

The type of browser window this is. Under some circumstances a Window may not be assigned type property, for example when querying closed windows from the $(ref:sessions) API.
