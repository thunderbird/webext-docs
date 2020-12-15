=====
menus
=====

The menus API first appeared in Thunderbird 66 (see `bug 1503421`__).
It is basically the same as the `Firefox menus API`__, but modified to suit Thunderbird.
Note that the similar ``contextMenus`` API will not be added to Thunderbird.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1503421
__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus

Use the browser.menus API to add items to the browser's menus. You can choose what types of objects your context menu additions apply to, such as images, hyperlinks, and pages.

Permissions
===========

- menus
- menus.overrideContext

.. note::

  The permission ``menus`` is required to use ``menus``.

Functions
=========

.. _menus.create:

create(createProperties, [callback])
------------------------------------

Creates a new context menu item. Note that if an error occurs during creation, you may not find out until the creation callback fires (the details will be in `runtime.lastError <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError>`_).

- ``createProperties`` (object)

  - [``checked``] (boolean) The initial state of a checkbox or radio item: true for selected and false for unselected. Only one radio item can be selected at a time in a given group of radio items.
  - [``command``] (string) Specifies a command to issue for the context click.  Currently supports internal command _execute_browser_action.
  - [``contexts``] (array of :ref:`menus.ContextType`) List of contexts this menu item will appear in. Defaults to ['page'] if not specified.
  - [``documentUrlPatterns``] (array of string) Lets you restrict the item to apply only to documents whose URL matches one of the given patterns. (This applies to frames as well.) For details on the format of a pattern, see `Match Patterns <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns>`_.
  - [``enabled``] (boolean) Whether this context menu item is enabled or disabled. Defaults to true.
  - [``icons``] (object)
  - [``id``] (string) The unique ID to assign to this item. Mandatory for event pages. Cannot be the same as another ID for this extension.
  - [``onclick``] (function) A function that will be called back when the menu item is clicked. Event pages cannot use this.
  - [``parentId``] (integer or string) The ID of a parent menu item; this makes the item a child of a previously added item.
  - [``targetUrlPatterns``] (array of string) Similar to documentUrlPatterns, but lets you filter based on the src attribute of img/audio/video tags and the href of anchor tags.
  - [``title``] (string) The text to be displayed in the item; this is *required* unless ``type`` is 'separator'. When the context is 'selection', you can use ``%s`` within the string to show the selected text. For example, if this parameter's value is "Translate '%s' to Pig Latin" and the user selects the word "cool", the context menu item for the selection is "Translate 'cool' to Pig Latin". To specify an access key for the new menu entry, include a ``&`` before the desired letter in the title. For example "&Help".
  - [``type``] (:ref:`menus.ItemType`) The type of menu item. Defaults to 'normal' if not specified.
  - [``viewTypes``] (array of `ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`_) List of view types where the menu item will be shown. Defaults to any view, including those without a viewType.
  - [``visible``] (boolean) Whether the item is visible in the menu.

- [``callback``] (function) Called when the item has been created in the browser. If there were any problems creating the item, details will be available in `runtime.lastError <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError>`_.

Returns a `Promise`_ fulfilled with:

- integer or string The ID of the newly created item.

.. _menus.update:

update(id, updateProperties)
----------------------------

Updates a previously created context menu item.

- ``id`` (integer or string) The ID of the item to update.
- ``updateProperties`` (object) The properties to update. Accepts the same values as the create function.

  - [``checked``] (boolean)
  - [``contexts``] (array of :ref:`menus.ContextType`)
  - [``documentUrlPatterns``] (array of string)
  - [``enabled``] (boolean)
  - [``icons``] (object)
  - [``onclick``] (function)
  - [``parentId``] (integer or string) Note: You cannot change an item to be a child of one of its own descendants.
  - [``targetUrlPatterns``] (array of string)
  - [``title``] (string)
  - [``type``] (:ref:`menus.ItemType`)
  - [``viewTypes``] (array of `ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`_)
  - [``visible``] (boolean) Whether the item is visible in the menu.

.. _menus.remove:

remove(menuItemId)
------------------

Removes a context menu item.

- ``menuItemId`` (integer or string) The ID of the context menu item to remove.

.. _menus.removeAll:

removeAll()
-----------

Removes all context menu items added by this extension.

.. _menus.overrideContext:

overrideContext(contextOptions)
-------------------------------

Show the matching menu items from this extension instead of the default menu. This should be called during a 'contextmenu' DOM event handler, and only applies to the menu that opens after this event.

- ``contextOptions`` (object)

  - [``context``] (`string <enum_context_32_>`_) ContextType to override, to allow menu items from other extensions in the menu. Currently only 'tab' is supported. showDefaults cannot be used with this option.
  - [``showDefaults``] (boolean) Whether to also include default menu items in the menu.
  - [``tabId``] (integer) Required when context is 'tab'. Requires 'tabs' permission.

.. _enum_context_32:

Values for context:

- ``tab``

.. note::

  The permission ``menus.overrideContext`` is required to use ``overrideContext``.

.. _menus.refresh:

refresh()
---------

Updates the extension items in the shown menu, including changes that have been made since the menu was shown. Has no effect if the menu is hidden. Rebuilding a shown menu is an expensive operation, only invoke this method when necessary.

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Events
======

.. _menus.onClicked:

onClicked(info, [tab])
----------------------

Fired when a context menu item is clicked.

- ``info`` (:ref:`menus.OnClickData`) Information about the item clicked and the context where the click happened.
- [``tab``] (:ref:`tabs.Tab`) The details of the tab where the click took place. If the click did not take place in a tab, this parameter will be missing.

.. _menus.onShown:

onShown(info, tab)
------------------

Fired when a menu is shown. The extension can add, modify or remove menu items and call menus.refresh() to update the menu.

- ``info`` (object) Information about the context of the menu action and the created menu items. For more information about each property, see OnClickData. The following properties are only set if the extension has host permissions for the given context: linkUrl, linkText, srcUrl, pageUrl, frameUrl, selectionText.

  - ``contexts`` (array of :ref:`menus.ContextType`) A list of all contexts that apply to the menu.
  - ``editable`` (boolean)
  - ``menuIds`` (array of None) A list of IDs of the menu items that were shown.
  - [``frameUrl``] (string)
  - [``linkText``] (string)
  - [``linkUrl``] (string)
  - [``mediaType``] (string)
  - [``pageUrl``] (string)
  - [``selectionText``] (string)
  - [``srcUrl``] (string)
  - [``targetElementId``] (integer)
  - [``viewType``] (`ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`_)

- ``tab`` (:ref:`tabs.Tab`) The details of the tab where the menu was opened.

.. _menus.onHidden:

onHidden()
----------

Fired when a menu is hidden. This event is only fired if onShown has fired before.

Properties
==========

.. _menus.ACTION_MENU_TOP_LEVEL_LIMIT:

ACTION_MENU_TOP_LEVEL_LIMIT
---------------------------

The maximum number of top level extension items that can be added to an extension action context menu. Any items beyond this limit will be ignored.

Types
=====

.. _menus.ContextType:

ContextType
-----------

The different contexts a menu can appear in. Specifying 'all' is equivalent to the combination of all other contexts except for 'tab'.

`string <enum_ContextType_48_>`_

.. _enum_ContextType_48:

Values for ContextType:

- ``all``
- ``page``
- ``frame``
- ``selection``
- ``link``
- ``editable``
- ``password``
- ``image``
- ``video``
- ``audio``
- ``browser_action``
- ``tab``
- ``message_list``
- ``folder_pane``
- ``compose_attachments`` *Added in Thunderbird 83, backported to 78.5.0*

.. _menus.ItemType:

ItemType
--------

The type of menu item.

`string <enum_ItemType_48_>`_

.. _enum_ItemType_48:

Values for ItemType:

- ``normal``
- ``checkbox``
- ``radio``
- ``separator``

.. _menus.OnClickData:

OnClickData
-----------

Information sent when a context menu item is clicked.

object:

- ``editable`` (boolean) A flag indicating whether the element is editable (text input, textarea, etc.).
- ``menuItemId`` (integer or string) The ID of the menu item that was clicked.
- ``modifiers`` (array of `string <enum_modifiers_50_>`_) An array of keyboard modifiers that were held while the menu item was clicked.
- [``attachments``] (array of :ref:`compose.ComposeAttachment`) The selected attachments of a message being composed.
- [``button``] (integer) An integer value of button by which menu item was clicked.
- [``checked``] (boolean) A flag indicating the state of a checkbox or radio item after it is clicked.
- [``displayedFolder``] (:ref:`folders.MailFolder`) The displayed folder, if the context menu was opened in the message list. The ``accountsRead`` permission is required.
- [``frameId``] (integer) The id of the frame of the element where the context menu was clicked.
- [``frameUrl``] (string)  The URL of the frame of the element where the context menu was clicked, if it was in a frame.
- [``linkText``] (string) If the element is a link, the text of that link.
- [``linkUrl``] (string) If the element is a link, the URL it points to.
- [``mediaType``] (string) One of 'image', 'video', or 'audio' if the context menu was activated on one of these types of elements.
- [``pageUrl``] (string) The URL of the page where the menu item was clicked. This property is not set if the click occurred in a context where there is no current page, such as in a launcher context menu.
- [``parentMenuItemId``] (integer or string) The parent ID, if any, for the item clicked.
- [``selectedFolder``] (:ref:`folders.MailFolder`) The selected folder, if the context menu was opened in the folder pane. The ``accountsRead`` permission is required.
- [``selectedMessages``] (:ref:`messages.MessageList`) The selected messages, if the context menu was opened in the message list. The ``messagesRead`` permission is required.
- [``selectionText``] (string) The text for the context selection, if any.
- [``srcUrl``] (string) Will be present for elements with a 'src' URL.
- [``targetElementId``] (integer) An identifier of the clicked element, if any. Use menus.getTargetElement in the page to find the corresponding element.
- [``viewType``] (`ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`_) The type of view where the menu is clicked. May be unset if the menu is not associated with a view.
- [``wasChecked``] (boolean) A flag indicating the state of a checkbox or radio item before it was clicked.

.. _enum_modifiers_50:

Values for modifiers:

- ``Shift``
- ``Alt``
- ``Command``
- ``Ctrl``
- ``MacCtrl``
