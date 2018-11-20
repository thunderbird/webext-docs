====
tabs
====

Use the ``browser.tabs`` API to interact with the browser's tab system. You can use this API to create, modify, and rearrange tabs in the browser.

Types
=====

.. _tabs.Tab:

Tab
---

- ``active`` (boolean) Whether the tab is active in its window. (Does not necessarily mean the window is focused.)
- ``highlighted`` (boolean) Whether the tab is highlighted. Works as an alias of active
- ``index`` (integer) The zero-based index of the tab within its window.
- ``selected`` (boolean) Whether the tab is selected.
- [``favIconUrl``] (string) The URL of the tab's favicon. This property is only present if the extension's manifest includes the ``"tabs"`` permission. It may also be an empty string if the tab is loading.
- [``height``] (integer) The height of the tab in pixels.
- [``id``] (integer) The ID of the tab. Tab IDs are unique within a browser session. Under some circumstances a Tab may not be assigned an ID, for example when querying foreign tabs using the $(ref:sessions) API, in which case a session ID may be present. Tab ID can also be set to $(ref:tabs.TAB_ID_NONE) for apps and devtools windows.
- [``lastAccessed``] (integer) The last time the tab was accessed as the number of milliseconds since epoch.
- [``status``] (string) Either *loading* or *complete*.
- [``title``] (string) The title of the tab. This property is only present if the extension's manifest includes the ``"tabs"`` permission.
- [``url``] (string) The URL the tab is displaying. This property is only present if the extension's manifest includes the ``"tabs"`` permission.
- [``width``] (integer) The width of the tab in pixels.
- [``windowId``] (integer) The ID of the window the tab is contained within.

.. _tabs.TabStatus:

TabStatus
---------

Whether the tabs have completed loading.

.. _tabs.WindowType:

WindowType
----------

The type of window.

.. _tabs.UpdatePropertyName:

UpdatePropertyName
------------------

Event names supported in onUpdated.

.. _tabs.UpdateFilter:

UpdateFilter
------------

An object describing filters to apply to tabs.onUpdated events.

- [``properties``] (array) A list of property names. Events that do not match any of the names will be filtered out.
- [``tabId``] (integer)
- [``urls``] (array) A list of URLs or URL patterns. Events that cannot match any of the URLs will be filtered out.  Filtering with urls requires the ``"tabs"`` or  ``"activeTab"`` permission.
- [``windowId``] (integer)

Functions
=========

.. _tabs.get:

get(tabId, callback)
--------------------

Retrieves details about the specified tab.

- ``tabId`` (integer)
- ``callback`` (function)

.. _tabs.getCurrent:

getCurrent(callback)
--------------------

Gets the tab that this script call is being made from. May be undefined if called from a non-tab context (for example: a background page or popup view).

- ``callback`` (function)

.. _tabs.create:

create(createProperties, [callback])
------------------------------------

Creates a new tab.

- ``createProperties`` (object)

  - [``active``] (boolean) Whether the tab should become the active tab in the window. Does not affect whether the window is focused (see $(ref:windows.update)). Defaults to ``true``.
  - [``index``] (integer) The position the tab should take in the window. The provided value will be clamped to between zero and the number of tabs in the window.
  - [``selected``] (boolean) Whether the tab should become the selected tab in the window. Defaults to ``true``
  - [``url``] (string) The URL to navigate the tab to initially. Fully-qualified URLs must include a scheme (i.e. 'http://www.google.com', not 'www.google.com'). Relative URLs will be relative to the current page within the extension. Defaults to the New Tab Page.
  - [``windowId``] (integer) The window to create the new tab in. Defaults to the $(topic:current-window)[current window].

- [``callback``] (function)

.. _tabs.duplicate:

duplicate(tabId, [callback])
----------------------------

Duplicates a tab.

- ``tabId`` (integer) The ID of the tab which is to be duplicated.
- [``callback``] (function)

.. _tabs.query:

query(queryInfo, callback)
--------------------------

Gets all tabs that have the specified properties, or all tabs if no properties are specified.

- ``queryInfo`` (object)

  - [``active``] (boolean) Whether the tabs are active in their windows.
  - [``currentWindow``] (boolean) Whether the tabs are in the $(topic:current-window)[current window].
  - [``highlighted``] (boolean) Whether the tabs are highlighted.  Works as an alias of active.
  - [``index``] (integer) The position of the tabs within their windows.
  - [``isMail3Pane``] (boolean) Whether the tab is a Thunderbird 3-pane tab.
  - [``lastFocusedWindow``] (boolean) Whether the tabs are in the last focused window.
  - [``status``] (:ref:`tabs.TabStatus`) Whether the tabs have completed loading.
  - [``title``] (string) Match page titles against a pattern.
  - [``url``] (string or array) Match tabs against one or more $(topic:match_patterns)[URL patterns]. Note that fragment identifiers are not matched.
  - [``windowId``] (integer) The ID of the parent window, or $(ref:windows.WINDOW_ID_CURRENT) for the $(topic:current-window)[current window].
  - [``windowType``] (:ref:`tabs.WindowType`) The type of window the tabs are in.

- ``callback`` (function)

.. _tabs.update:

update([tabId], updateProperties, [callback])
---------------------------------------------

Modifies the properties of a tab. Properties that are not specified in ``updateProperties`` are not modified.

- [``tabId``] (integer) Defaults to the selected tab of the $(topic:current-window)[current window].
- ``updateProperties`` (object)

  - [``active``] (boolean) Whether the tab should be active. Does not affect whether the window is focused (see $(ref:windows.update)).
  - [``url``] (string) A URL to navigate the tab to.

- [``callback``] (function)

.. _tabs.move:

move(tabIds, moveProperties, [callback])
----------------------------------------

Moves one or more tabs to a new position within its window, or to a new window. Note that tabs can only be moved to and from normal (window.type === "normal") windows.

- ``tabIds`` (integer or array) The tab or list of tabs to move.
- ``moveProperties`` (object)

  - ``index`` (integer) The position to move the window to. -1 will place the tab at the end of the window.
  - [``windowId``] (integer) Defaults to the window the tab is currently in.

- [``callback``] (function)

.. _tabs.reload:

reload([tabId], [reloadProperties], [callback])
-----------------------------------------------

Reload a tab.

- [``tabId``] (integer) The ID of the tab to reload; defaults to the selected tab of the current window.
- [``reloadProperties``] (object)

  - [``bypassCache``] (boolean) Whether using any local cache. Default is false.

- [``callback``] (function)

.. _tabs.remove:

remove(tabIds, [callback])
--------------------------

Closes one or more tabs.

- ``tabIds`` (integer or array) The tab or list of tabs to close.
- [``callback``] (function)

.. _tabs.executeScript:

executeScript([tabId], details, [callback])
-------------------------------------------

Injects JavaScript code into a page. For details, see the $(topic:content_scripts)[programmatic injection] section of the content scripts doc.

- [``tabId``] (integer) The ID of the tab in which to run the script; defaults to the active tab of the current window.
- ``details`` (:ref:`extensionTypes.InjectDetails`) Details of the script to run.
- [``callback``] (function) Called after all the JavaScript has been executed.

.. _tabs.insertCSS:

insertCSS([tabId], details, [callback])
---------------------------------------

Injects CSS into a page. For details, see the $(topic:content_scripts)[programmatic injection] section of the content scripts doc.

- [``tabId``] (integer) The ID of the tab in which to insert the CSS; defaults to the active tab of the current window.
- ``details`` (:ref:`extensionTypes.InjectDetails`) Details of the CSS text to insert.
- [``callback``] (function) Called when all the CSS has been inserted.

.. _tabs.removeCSS:

removeCSS([tabId], details, [callback])
---------------------------------------

Removes injected CSS from a page. For details, see the $(topic:content_scripts)[programmatic injection] section of the content scripts doc.

- [``tabId``] (integer) The ID of the tab from which to remove the injected CSS; defaults to the active tab of the current window.
- ``details`` (:ref:`extensionTypes.InjectDetails`) Details of the CSS text to remove.
- [``callback``] (function) Called when all the CSS has been removed.

Events
======

.. _tabs.onCreated:

onCreated(tab)
--------------

Fired when a tab is created. Note that the tab's URL may not be set at the time this event fired, but you can listen to onUpdated events to be notified when a URL is set.

- ``tab`` (:ref:`tabs.Tab`) Details of the tab that was created.

.. _tabs.onUpdated:

onUpdated(tabId, changeInfo, tab)
---------------------------------

Fired when a tab is updated.

- ``tabId`` (integer)
- ``changeInfo`` (object) Lists the changes to the state of the tab that was updated.

  - [``favIconUrl``] (string) The tab's new favicon URL.
  - [``status``] (string) The status of the tab. Can be either *loading* or *complete*.
  - [``url``] (string) The tab's URL if it has changed.

- ``tab`` (:ref:`tabs.Tab`) Gives the state of the tab that was updated.

.. _tabs.onMoved:

onMoved(tabId, moveInfo)
------------------------

Fired when a tab is moved within a window. Only one move event is fired, representing the tab the user directly moved. Move events are not fired for the other tabs that must move in response. This event is not fired when a tab is moved between windows. For that, see $(ref:tabs.onDetached).

- ``tabId`` (integer)
- ``moveInfo`` (object)

  - ``fromIndex`` (integer)
  - ``toIndex`` (integer)
  - ``windowId`` (integer)

.. _tabs.onActivated:

onActivated(activeInfo)
-----------------------

Fires when the active tab in a window changes. Note that the tab's URL may not be set at the time this event fired, but you can listen to onUpdated events to be notified when a URL is set.

- ``activeInfo`` (object)

  - ``tabId`` (integer) The ID of the tab that has become active.
  - ``windowId`` (integer) The ID of the window the active tab changed inside of.

.. _tabs.onDetached:

onDetached(tabId, detachInfo)
-----------------------------

Fired when a tab is detached from a window, for example because it is being moved between windows.

- ``tabId`` (integer)
- ``detachInfo`` (object)

  - ``oldPosition`` (integer)
  - ``oldWindowId`` (integer)

.. _tabs.onAttached:

onAttached(tabId, attachInfo)
-----------------------------

Fired when a tab is attached to a window, for example because it was moved between windows.

- ``tabId`` (integer)
- ``attachInfo`` (object)

  - ``newPosition`` (integer)
  - ``newWindowId`` (integer)

.. _tabs.onRemoved:

onRemoved(tabId, removeInfo)
----------------------------

Fired when a tab is closed.

- ``tabId`` (integer)
- ``removeInfo`` (object)

  - ``isWindowClosing`` (boolean) True when the tab is being closed because its window is being closed.
  - ``windowId`` (integer) The window whose tab is closed.
