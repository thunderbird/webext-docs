====
tabs
====
Use the ``browser.tabs`` API to interact with the browser's tab system. You can use this API to create, modify, and rearrange tabs in the browser.

Types
=====

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

TabStatus
---------
Whether the tabs have completed loading.

WindowType
----------
The type of window.

UpdatePropertyName
------------------
Event names supported in onUpdated.

UpdateFilter
------------
An object describing filters to apply to tabs.onUpdated events.

- [``properties``] (array) A list of property names. Events that do not match any of the names will be filtered out.
- [``tabId``] (integer)
- [``urls``] (array) A list of URLs or URL patterns. Events that cannot match any of the URLs will be filtered out.  Filtering with urls requires the ``"tabs"`` or  ``"activeTab"`` permission.
- [``windowId``] (integer)

Functions
=========

get(tabId, callback)
--------------------
Retrieves details about the specified tab.

- ``tabId`` (integer)
- ``callback`` (function)

getCurrent(callback)
--------------------
Gets the tab that this script call is being made from. May be undefined if called from a non-tab context (for example: a background page or popup view).

- ``callback`` (function)

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

duplicate(tabId, [callback])
----------------------------
Duplicates a tab.

- ``tabId`` (integer) The ID of the tab which is to be duplicated.
- [``callback``] (function)

query(queryInfo, callback)
--------------------------
Gets all tabs that have the specified properties, or all tabs if no properties are specified.

- ``queryInfo`` (object)

  - [``active``] (boolean) Whether the tabs are active in their windows.
  - [``currentWindow``] (boolean) Whether the tabs are in the $(topic:current-window)[current window].
  - [``highlighted``] (boolean) Whether the tabs are highlighted.  Works as an alias of active.
  - [``index``] (integer) The position of the tabs within their windows.
  - [``isMail3Pane``] (boolean)
  - [``lastFocusedWindow``] (boolean) Whether the tabs are in the last focused window.
  - [``status``] `TabStatus`_ Whether the tabs have completed loading.
  - [``title``] (string) Match page titles against a pattern.
  - [``url``] Match tabs against one or more $(topic:match_patterns)[URL patterns]. Note that fragment identifiers are not matched.
  - [``windowId``] (integer) The ID of the parent window, or $(ref:windows.WINDOW_ID_CURRENT) for the $(topic:current-window)[current window].
  - [``windowType``] `WindowType`_ The type of window the tabs are in.

- ``callback`` (function)

update([tabId], updateProperties, [callback])
---------------------------------------------
Modifies the properties of a tab. Properties that are not specified in ``updateProperties`` are not modified.

- [``tabId``] (integer) Defaults to the selected tab of the $(topic:current-window)[current window].
- ``updateProperties`` (object)

  - [``active``] (boolean) Whether the tab should be active. Does not affect whether the window is focused (see $(ref:windows.update)).
  - [``url``] (string) A URL to navigate the tab to.

- [``callback``] (function)

move(tabIds, moveProperties, [callback])
----------------------------------------
Moves one or more tabs to a new position within its window, or to a new window. Note that tabs can only be moved to and from normal (window.type === "normal") windows.

- ``tabIds`` The tab or list of tabs to move.
- ``moveProperties`` (object)

  - ``index`` (integer) The position to move the window to. -1 will place the tab at the end of the window.
  - [``windowId``] (integer) Defaults to the window the tab is currently in.

- [``callback``] (function)

reload([tabId], [reloadProperties], [callback])
-----------------------------------------------
Reload a tab.

- [``tabId``] (integer) The ID of the tab to reload; defaults to the selected tab of the current window.
- [``reloadProperties``] (object)

  - [``bypassCache``] (boolean) Whether using any local cache. Default is false.

- [``callback``] (function)

remove(tabIds, [callback])
--------------------------
Closes one or more tabs.

- ``tabIds`` The tab or list of tabs to close.
- [``callback``] (function)

executeScript([tabId], details, [callback])
-------------------------------------------
Injects JavaScript code into a page. For details, see the $(topic:content_scripts)[programmatic injection] section of the content scripts doc.

- [``tabId``] (integer) The ID of the tab in which to run the script; defaults to the active tab of the current window.
- ``details`` `extensionTypes.InjectDetails`_ Details of the script to run.
- [``callback``] (function) Called after all the JavaScript has been executed.

insertCSS([tabId], details, [callback])
---------------------------------------
Injects CSS into a page. For details, see the $(topic:content_scripts)[programmatic injection] section of the content scripts doc.

- [``tabId``] (integer) The ID of the tab in which to insert the CSS; defaults to the active tab of the current window.
- ``details`` `extensionTypes.InjectDetails`_ Details of the CSS text to insert.
- [``callback``] (function) Called when all the CSS has been inserted.

removeCSS([tabId], details, [callback])
---------------------------------------
Removes injected CSS from a page. For details, see the $(topic:content_scripts)[programmatic injection] section of the content scripts doc.

- [``tabId``] (integer) The ID of the tab from which to remove the injected CSS; defaults to the active tab of the current window.
- ``details`` `extensionTypes.InjectDetails`_ Details of the CSS text to remove.
- [``callback``] (function) Called when all the CSS has been removed.

