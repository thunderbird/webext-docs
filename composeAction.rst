=============
composeAction
=============

The :doc:`browserAction` and composeAction APIs first appeared in Thunderbird 64.

Use toolbar actions to put icons in the message composition toolbars. In addition to its icon, a toolbar action can also have a tooltip, a badge, and a popup.

Types
=====

.. _composeAction.Details:

Details
-------

Specifies to which tab or window the value should be set, or from which one it should be retrieved. If no tab nor window is specified, the global value is set or retrieved.

- [``tabId``] (integer) When setting a value, it will be specific to the specified tab, and will automatically reset when the tab navigates. When getting, specifies the tab to get the value from; if there is no tab-specific value, the window one will be inherited.
- [``windowId``] (integer) When setting a value, it will be specific to the specified window. When getting, specifies the window to get the value from; if there is no window-specific value, the global one will be inherited.

.. _composeAction.ColorArray:

ColorArray
----------

.. _composeAction.ImageDataType:

ImageDataType
-------------

Pixel data for an image. Must be an ImageData object (for example, from a ``canvas`` element).

Functions
=========

setTitle(details, [callback])
-----------------------------

Sets the title of the toolbar action. This shows up in the tooltip.

- ``details`` (object)

  - ``title`` The string the toolbar action should display when moused over.

- [``callback``] (function)

getTitle(details, callback)
---------------------------

Gets the title of the toolbar action.

- ``details`` (:ref:`composeAction.Details`)
- ``callback`` (function)

setIcon(details, [callback])
----------------------------

Sets the icon for the toolbar action. The icon can be specified either as the path to an image file or as the pixel data from a canvas element, or as dictionary of either one of those. Either the **path** or the **imageData** property must be specified.

- ``details`` (object)

  - [``imageData``] Either an ImageData object or a dictionary {size -> ImageData} representing icon to be set. If the icon is specified as a dictionary, the actual image to be used is chosen depending on screen's pixel density. If the number of image pixels that fit into one screen space unit equals ``scale``, then image with size ``scale`` * 19 will be selected. Initially only scales 1 and 2 will be supported. At least one image must be specified. Note that 'details.imageData = foo' is equivalent to 'details.imageData = {'19': foo}'
  - [``path``] Either a relative image path or a dictionary {size -> relative image path} pointing to icon to be set. If the icon is specified as a dictionary, the actual image to be used is chosen depending on screen's pixel density. If the number of image pixels that fit into one screen space unit equals ``scale``, then image with size ``scale`` * 19 will be selected. Initially only scales 1 and 2 will be supported. At least one image must be specified. Note that 'details.path = foo' is equivalent to 'details.imageData = {'19': foo}'

- [``callback``] (function)

setPopup(details, [callback])
-----------------------------

Sets the html document to be opened as a popup when the user clicks on the toolbar action's icon.

- ``details`` (object)

  - ``popup`` The html file to show in a popup.  If set to the empty string (''), no popup is shown.

- [``callback``] (function)

getPopup(details, callback)
---------------------------

Gets the html document set as the popup for this toolbar action.

- ``details`` (:ref:`composeAction.Details`)
- ``callback`` (function)

setBadgeText(details, [callback])
---------------------------------

Sets the badge text for the toolbar action. The badge is displayed on top of the icon.

- ``details`` (object)

  - ``text`` Any number of characters can be passed, but only about four can fit in the space.

- [``callback``] (function)

getBadgeText(details, callback)
-------------------------------

Gets the badge text of the toolbar action. If no tab nor window is specified is specified, the global badge text is returned.

- ``details`` (:ref:`composeAction.Details`)
- ``callback`` (function)

setBadgeBackgroundColor(details, [callback])
--------------------------------------------

Sets the background color for the badge.

- ``details`` (object)

  - ``color`` An array of four integers in the range [0,255] that make up the RGBA color of the badge. For example, opaque red is ``[255, 0, 0, 255]``. Can also be a string with a CSS value, with opaque red being ``#FF0000`` or ``#F00``.

- [``callback``] (function)

getBadgeBackgroundColor(details, callback)
------------------------------------------

Gets the background color of the toolbar action.

- ``details`` (:ref:`composeAction.Details`)
- ``callback`` (function)

enable([tabId], [callback])
---------------------------

Enables the toolbar action for a tab. By default, toolbar actions are enabled.

- [``tabId``] (integer) The id of the tab for which you want to modify the toolbar action.
- [``callback``] (function)

disable([tabId], [callback])
----------------------------

Disables the toolbar action for a tab.

- [``tabId``] (integer) The id of the tab for which you want to modify the toolbar action.
- [``callback``] (function)

isEnabled(details)
------------------

Checks whether the toolbar action is enabled.

- ``details`` (:ref:`composeAction.Details`)

openPopup()
-----------

Opens the extension popup window in the active window.

Events
======

onClicked()
-----------

Fired when a toolbar action icon is clicked.  This event will not fire if the toolbar action has a popup.
