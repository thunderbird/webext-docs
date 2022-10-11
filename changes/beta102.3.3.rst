==============================
Changes in Thunderbird 102.3.3
==============================

browserAction API
=================
* Added ``default_windows`` manifest key to :ref:`browserAction_api`, allowing to show the action button also in stand-alone message windows.

commands API
============
* Added ``tab`` parameter to the :ref:`commands.onCommand` event, returning the currently active tab. Since the event is a user input event handler, it was not possible to query the active tab (via `browser.tabs.query()`), without loosing this elevated status due to calling an asynchronous function. Solved by returning the tab as a parameter (similar to :ref:`menus.onClicked` and other user input event handlers).

mailTabs API
============
* Added :ref:`mailTabs.setSelectedMessages`.
