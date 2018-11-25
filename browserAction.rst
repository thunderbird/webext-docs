=============
browserAction
=============

The browserAction and :doc:`composeAction` APIs first appeared in Thunderbird 64.

Manifest file properties
========================

- [``browser_action``] (object)

  - [``browser_style``] (boolean)
  - [``default_area``] (string) Currently unused.
  - [``default_icon``] (:ref:`IconPath`)
  - [``default_popup``] (string)
  - [``default_title``] (string)
  - [``theme_icons``] (array) Specifies icons to use for dark and light themes

Use toolbar actions to put icons in the mail window toolbar. In addition to its icon, a toolbar action can also have a tooltip, a badge, and a popup. This namespace is called browserAction for compatibility with browser WebExtensions.

Functions
=========

.. _browserAction.setTitle:

setTitle(details, [callback])
-----------------------------

Sets the title of the toolbar action. This shows up in the tooltip.

- ``details`` (object)

  - ``title`` (string or null) The string the toolbar action should display when moused over.

- [``callback``] (function)

.. _browserAction.getTitle:

getTitle(details, callback)
---------------------------

Gets the title of the toolbar action.

- ``details`` (:ref:`browserAction.Details`)
- ``callback`` (function)

.. _browserAction.setIcon:

setIcon(details, [callback])
----------------------------

Sets the icon for the toolbar action. The icon can be specified either as the path to an image file or as the pixel data from a canvas element, or as dictionary of either one of those. Either the **path** or the **imageData** property must be specified.

- ``details`` (object)

  - [``imageData``] (:ref:`browserAction.ImageDataType` or object) Either an ImageData object or a dictionary {size -> ImageData} representing icon to be set. If the icon is specified as a dictionary, the actual image to be used is chosen depending on screen's pixel density. If the number of image pixels that fit into one screen space unit equals ``scale``, then image with size ``scale`` * 19 will be selected. Initially only scales 1 and 2 will be supported. At least one image must be specified. Note that 'details.imageData = foo' is equivalent to 'details.imageData = {'19': foo}'
  - [``path``] (string or object) Either a relative image path or a dictionary {size -> relative image path} pointing to icon to be set. If the icon is specified as a dictionary, the actual image to be used is chosen depending on screen's pixel density. If the number of image pixels that fit into one screen space unit equals ``scale``, then image with size ``scale`` * 19 will be selected. Initially only scales 1 and 2 will be supported. At least one image must be specified. Note that 'details.path = foo' is equivalent to 'details.imageData = {'19': foo}'

- [``callback``] (function)

.. _browserAction.setPopup:

setPopup(details, [callback])
-----------------------------

Sets the html document to be opened as a popup when the user clicks on the toolbar action's icon.

- ``details`` (object)

  - ``popup`` (string or null) The html file to show in a popup.  If set to the empty string (''), no popup is shown.

- [``callback``] (function)

.. _browserAction.getPopup:

getPopup(details, callback)
---------------------------

Gets the html document set as the popup for this toolbar action.

- ``details`` (:ref:`browserAction.Details`)
- ``callback`` (function)

.. _browserAction.setBadgeText:

setBadgeText(details, [callback])
---------------------------------

Sets the badge text for the toolbar action. The badge is displayed on top of the icon.

- ``details`` (object)

  - ``text`` (string or null) Any number of characters can be passed, but only about four can fit in the space.

- [``callback``] (function)

.. _browserAction.getBadgeText:

getBadgeText(details, callback)
-------------------------------

Gets the badge text of the toolbar action. If no tab nor window is specified is specified, the global badge text is returned.

- ``details`` (:ref:`browserAction.Details`)
- ``callback`` (function)

.. _browserAction.setBadgeBackgroundColor:

setBadgeBackgroundColor(details, [callback])
--------------------------------------------

Sets the background color for the badge.

- ``details`` (object)

  - ``color`` (string or :ref:`browserAction.ColorArray` or null) An array of four integers in the range [0,255] that make up the RGBA color of the badge. For example, opaque red is ``[255, 0, 0, 255]``. Can also be a string with a CSS value, with opaque red being ``#FF0000`` or ``#F00``.

- [``callback``] (function)

.. _browserAction.getBadgeBackgroundColor:

getBadgeBackgroundColor(details, callback)
------------------------------------------

Gets the background color of the toolbar action.

- ``details`` (:ref:`browserAction.Details`)
- ``callback`` (function)

.. _browserAction.enable:

enable([tabId], [callback])
---------------------------

Enables the toolbar action for a tab. By default, toolbar actions are enabled.

- [``tabId``] (integer) The id of the tab for which you want to modify the toolbar action.
- [``callback``] (function)

.. _browserAction.disable:

disable([tabId], [callback])
----------------------------

Disables the toolbar action for a tab.

- [``tabId``] (integer) The id of the tab for which you want to modify the toolbar action.
- [``callback``] (function)

.. _browserAction.isEnabled:

isEnabled(details)
------------------

Checks whether the toolbar action is enabled.

- ``details`` (:ref:`browserAction.Details`)

.. _browserAction.openPopup:

openPopup()
-----------

Opens the extension popup window in the active window.

Types
=====

.. _browserAction.Details:

Details
-------

Specifies to which tab or window the value should be set, or from which one it should be retrieved. If no tab nor window is specified, the global value is set or retrieved.

- [``tabId``] (integer) When setting a value, it will be specific to the specified tab, and will automatically reset when the tab navigates. When getting, specifies the tab to get the value from; if there is no tab-specific value, the window one will be inherited.
- [``windowId``] (integer) When setting a value, it will be specific to the specified window. When getting, specifies the window to get the value from; if there is no window-specific value, the global one will be inherited.

.. _browserAction.ColorArray:

ColorArray
----------

.. _browserAction.ImageDataType:

ImageDataType
-------------

Pixel data for an image. Must be an ImageData object (for example, from a ``canvas`` element).

Events
======

.. _browserAction.onClicked:

onClicked()
-----------

Fired when a toolbar action icon is clicked.  This event will not fire if the toolbar action has a popup.
