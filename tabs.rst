====
tabs
====

Use the ``browser.tabs`` API to interact with the browser's tab system. You can use this API to create, modify, and rearrange tabs in the browser.

Permissions
===========

- activeTab
- tabs "Access browser tabs"
- tabHide "Hide and show browser tabs"

Functions
=========

.. _tabs.get:

get(tabId)
----------

Retrieves details about the specified tab.

- ``tabId`` (integer)

Returns a `Promise`_ fulfilled with:

- :ref:`tabs.Tab`

.. _tabs.getCurrent:

getCurrent()
------------

Gets the tab that this script call is being made from. May be undefined if called from a non-tab context (for example: a background page or popup view).

Returns a `Promise`_ fulfilled with:

- :ref:`tabs.Tab`

.. _tabs.create:

create(createProperties)
------------------------

Creates a new tab.

- ``createProperties`` (object)

  - [``active``] (boolean) Whether the tab should become the active tab in the window. Does not affect whether the window is focused (see :ref:`windows.update`). Defaults to ``true``.
  - [``index``] (integer) The position the tab should take in the window. The provided value will be clamped to between zero and the number of tabs in the window.
  - [``selected``] (boolean) **Deprecated.** Whether the tab should become the selected tab in the window. Defaults to ``true``
  - [``url``] (string) The URL to navigate the tab to initially. Fully-qualified URLs must include a scheme (i.e. 'http://www.google.com', not 'www.google.com'). Relative URLs will be relative to the current page within the extension. Defaults to the New Tab Page.
  - [``windowId``] (integer) The window to create the new tab in. Defaults to the current window.

Returns a `Promise`_ fulfilled with:

- :ref:`tabs.Tab` Details about the created tab. Will contain the ID of the new tab.

.. _tabs.duplicate:

duplicate(tabId)
----------------

Duplicates a tab.

- ``tabId`` (integer) The ID of the tab which is to be duplicated.

Returns a `Promise`_ fulfilled with:

- :ref:`tabs.Tab` Details about the duplicated tab. The :ref:`tabs.Tab` object doesn't contain ``url``, ``title`` and ``favIconUrl`` if the ``"tabs"`` permission has not been requested.

.. _tabs.query:

query(queryInfo)
----------------

Gets all tabs that have the specified properties, or all tabs if no properties are specified.

- ``queryInfo`` (object)

  - [``active``] (boolean) Whether the tabs are active in their windows.
  - [``currentWindow``] (boolean) Whether the tabs are in the current window.
  - [``highlighted``] (boolean) Whether the tabs are highlighted.  Works as an alias of active.
  - [``index``] (integer) The position of the tabs within their windows.
  - [``lastFocusedWindow``] (boolean) Whether the tabs are in the last focused window.
  - [``mailTab``] (boolean) Whether the tab is a Thunderbird 3-pane tab.
  - [``status``] (:ref:`tabs.TabStatus`) Whether the tabs have completed loading.
  - [``title``] (string) Match page titles against a pattern.
  - [``url``] (string or array of string) Match tabs against one or more `URL Patterns <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns>`_. Note that fragment identifiers are not matched.
  - [``windowId``] (integer) The ID of the parent window, or :ref:`windows.WINDOW_ID_CURRENT` for the current window.
  - [``windowType``] (:ref:`tabs.WindowType`) The type of window the tabs are in.

Returns a `Promise`_ fulfilled with:

- array of :ref:`tabs.Tab`

.. _tabs.update:

update([tabId], updateProperties)
---------------------------------

Modifies the properties of a tab. Properties that are not specified in ``updateProperties`` are not modified.

- [``tabId``] (integer) Defaults to the selected tab of the current window.
- ``updateProperties`` (object)

  - [``active``] (boolean) Whether the tab should be active. Does not affect whether the window is focused (see :ref:`windows.update`).
  - [``url``] (string) A URL to navigate the tab to.

Returns a `Promise`_ fulfilled with:

- :ref:`tabs.Tab` Details about the updated tab. The :ref:`tabs.Tab` object doesn't contain ``url``, ``title`` and ``favIconUrl`` if the ``"tabs"`` permission has not been requested.

.. _tabs.move:

move(tabIds, moveProperties)
----------------------------

Moves one or more tabs to a new position within its window, or to a new window. Note that tabs can only be moved to and from normal (window.type === "normal") windows.

- ``tabIds`` (integer or array of integer) The tab or list of tabs to move.
- ``moveProperties`` (object)

  - ``index`` (integer) The position to move the window to. -1 will place the tab at the end of the window.
  - [``windowId``] (integer) Defaults to the window the tab is currently in.

Returns a `Promise`_ fulfilled with:

- :ref:`tabs.Tab` or array of :ref:`tabs.Tab` Details about the moved tabs.

.. _tabs.reload:

reload([tabId], [reloadProperties])
-----------------------------------

Reload a tab.

- [``tabId``] (integer) The ID of the tab to reload; defaults to the selected tab of the current window.
- [``reloadProperties``] (object)

  - [``bypassCache``] (boolean) Whether using any local cache. Default is false.

.. _tabs.remove:

remove(tabIds)
--------------

Closes one or more tabs.

- ``tabIds`` (integer or array of integer) The tab or list of tabs to close.

.. _tabs.executeScript:

executeScript([tabId], details)
-------------------------------

Injects JavaScript code into a page. For details, see the `programmatic injection <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`_ section of the content scripts doc.

- [``tabId``] (integer) The ID of the tab in which to run the script; defaults to the active tab of the current window.
- ``details`` (`InjectDetails <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/InjectDetails>`_) Details of the script to run.

Returns a `Promise`_ fulfilled with:

- array of any The result of the script in every injected frame.

.. _tabs.insertCSS:

insertCSS([tabId], details)
---------------------------

Injects CSS into a page. For details, see the `programmatic injection <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`_ section of the content scripts doc.

- [``tabId``] (integer) The ID of the tab in which to insert the CSS; defaults to the active tab of the current window.
- ``details`` (`InjectDetails <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/InjectDetails>`_) Details of the CSS text to insert.

.. _tabs.removeCSS:

removeCSS([tabId], details)
---------------------------

Removes injected CSS from a page. For details, see the `programmatic injection <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`_ section of the content scripts doc.

- [``tabId``] (integer) The ID of the tab from which to remove the injected CSS; defaults to the active tab of the current window.
- ``details`` (`InjectDetails <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/InjectDetails>`_) Details of the CSS text to remove.

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

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

Fired when a tab is moved within a window. Only one move event is fired, representing the tab the user directly moved. Move events are not fired for the other tabs that must move in response. This event is not fired when a tab is moved between windows. For that, see :ref:`tabs.onDetached`.

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

Properties
==========

.. _tabs.TAB_ID_NONE:

TAB_ID_NONE
-----------

An ID which represents the absence of a browser tab.

Types
=====

.. _tabs.Tab:

Tab
---

object

- ``active`` (boolean) Whether the tab is active in its window. (Does not necessarily mean the window is focused.)
- ``highlighted`` (boolean) Whether the tab is highlighted. Works as an alias of active
- ``index`` (integer) The zero-based index of the tab within its window.
- ``selected`` (boolean) **Deprecated.** Whether the tab is selected.
- [``favIconUrl``] (string) The URL of the tab's favicon. This property is only present if the extension's manifest includes the ``"tabs"`` permission. It may also be an empty string if the tab is loading.
- [``height``] (integer) The height of the tab in pixels.
- [``id``] (integer) The ID of the tab. Tab IDs are unique within a browser session. Under some circumstances a Tab may not be assigned an ID. Tab ID can also be set to :ref:`tabs.TAB_ID_NONE` for apps and devtools windows.
- [``mailTab``] (boolean) Whether the tab is a 3-pane tab.
- [``status``] (string) Either *loading* or *complete*.
- [``title``] (string) The title of the tab. This property is only present if the extension's manifest includes the ``"tabs"`` permission.
- [``url``] (string) The URL the tab is displaying. This property is only present if the extension's manifest includes the ``"tabs"`` permission.
- [``width``] (integer) The width of the tab in pixels.
- [``windowId``] (integer) The ID of the window the tab is contained within.

.. _tabs.TabStatus:

TabStatus
---------

Whether the tabs have completed loading.

`string <enum_TabStatus_66_>`_

.. _enum_TabStatus_66:

Values for TabStatus:

- ``loading``
- ``complete``

.. _tabs.UpdateFilter:

UpdateFilter
------------

An object describing filters to apply to tabs.onUpdated events.

object

- [``properties``] (array of :ref:`tabs.UpdatePropertyName`) A list of property names. Events that do not match any of the names will be filtered out.
- [``tabId``] (integer)
- [``urls``] (array of string) A list of URLs or URL patterns. Events that cannot match any of the URLs will be filtered out.  Filtering with urls requires the ``"tabs"`` or  ``"activeTab"`` permission.
- [``windowId``] (integer)

.. _tabs.UpdatePropertyName:

UpdatePropertyName
------------------

Event names supported in onUpdated.

`string <enum_UpdatePropertyName_70_>`_

.. _enum_UpdatePropertyName_70:

Values for UpdatePropertyName:

- ``favIconUrl``
- ``status``
- ``title``

.. _tabs.WindowType:

WindowType
----------

The type of window.

`string <enum_WindowType_70_>`_

.. _enum_WindowType_70:

Values for WindowType:

- ``normal``
- ``popup``
- ``panel``
- ``app``
- ``devtools``
