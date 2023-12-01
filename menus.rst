.. container:: sticky-sidebar

  ≡ menus API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_
  * `External Types`_
  * `Properties`_

  .. include:: /developer-resources.rst

  ≡ Related information
  
  * :doc:`/how-to/eventListeners`
  * `"Quickfilter" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v3/quickfilter>`__
  * `"Menu" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v2/menu>`__

=========
menus API
=========

The menus API first appeared in Thunderbird 66.
It is basically the same as the `Firefox menus API`__, but modified to suit Thunderbird.
Note that Thunderbird does not include the *contextMenus* alias for this API.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus

.. role:: permission

.. role:: value

.. role:: code

The menus API allows to add items to Thunderbird's menus. You can choose what types of objects your context menu additions apply to, such as images, hyperlinks, and pages.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`menus`

.. api-member::
   :name: :permission:`menus.overrideContext`

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`menus` is required to use ``messenger.menus.*``.

.. rst-class:: api-main-section

Functions
=========

.. _menus.create:

create(createProperties, [callback])
------------------------------------

.. api-section-annotation-hack:: 

Creates a new context menu item. Note that if an error occurs during creation, you may not find out until the creation callback fires (the details will be in `runtime.lastError <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError>`__).

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``createProperties``
      :type: (object)
      
      .. api-member::
         :name: [``checked``]
         :type: (boolean, optional)
         
         The initial state of a checkbox or radio item: :value:`true` for selected and :value:`false` for unselected. Only one radio item can be selected at a time in a given group of radio items.
      
      
      .. api-member::
         :name: [``command``]
         :type: (string, optional)
         
         Specifies a command to issue for the context click. Currently supports internal commands :value:`_execute_action`, :value:`_execute_compose_action` and :value:`_execute_message_display_action`.
      
      
      .. api-member::
         :name: [``contexts``]
         :type: (array of :ref:`menus.ContextType`, optional)
         
         List of contexts this menu item will appear in. Defaults to :value:`['page']` if not specified.
      
      
      .. api-member::
         :name: [``documentUrlPatterns``]
         :type: (array of string, optional)
         
         Lets you restrict the item to apply only to documents whose URL matches one of the given patterns. (This applies to frames as well.) For details on the format of a pattern, see `Match Patterns <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns>`__.
      
      
      .. api-member::
         :name: [``enabled``]
         :type: (boolean, optional)
         
         Whether this context menu item is enabled or disabled. Defaults to true.
      
      
      .. api-member::
         :name: [``icons``]
         :type: (:ref:`menus.IconPath`, optional)
         
         Custom icons to display next to the menu item. Custom icons can only be set for items appearing in submenus.
      
      
      .. api-member::
         :name: [``id``]
         :type: (string, optional)
         
         The unique ID to assign to this item. Mandatory for event pages. Cannot be the same as another ID for this extension.
      
      
      .. api-member::
         :name: [``onclick``]
         :type: (function, optional)
         
         A function that will be called back when the menu item is clicked. Event pages cannot use this.
      
      
      .. api-member::
         :name: [``parentId``]
         :type: (integer or string, optional)
         
         The ID of a parent menu item; this makes the item a child of a previously added item.
      
      
      .. api-member::
         :name: [``targetUrlPatterns``]
         :type: (array of string, optional)
         
         Similar to documentUrlPatterns, but lets you filter based on the src attribute of img/audio/video tags and the href of anchor tags.
      
      
      .. api-member::
         :name: [``title``]
         :type: (string, optional)
         
         The text to be displayed in the item; this is *required* unless ``type`` is :value:`separator`. When the context is :value:`selection`, you can use :value:`%s` within the string to show the selected text. For example, if this parameter's value is :value:`Translate '%s' to Latin` and the user selects the word :value:`cool`, the context menu item for the selection is :value:`Translate 'cool' to Latin`. To specify an access key for the new menu entry, include a :value:`&` before the desired letter in the title. For example :value:`&Help`.
      
      
      .. api-member::
         :name: [``type``]
         :type: (:ref:`menus.ItemType`, optional)
         
         The type of menu item. Defaults to :value:`normal` if not specified.
      
      
      .. api-member::
         :name: [``viewTypes``]
         :type: (array of `ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`__, optional)
         
         List of view types where the menu item will be shown. Defaults to any view, including those without a viewType.
      
      
      .. api-member::
         :name: [``visible``]
         :type: (boolean, optional)
         
         Whether the item is visible in the menu.
      
   
   
   .. api-member::
      :name: [``callback``]
      :type: (function, optional)
      
      Called when the item has been created in the browser. If there were any problems creating the item, details will be available in `runtime.lastError <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError>`__.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: integer or string
      
      The ID of the newly created item.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.getTargetElement:

getTargetElement(targetElementId)
---------------------------------

.. api-section-annotation-hack:: 

Retrieve the element that was associated with a recent `contextmenu <https://developer.mozilla.org/en-US/docs/Web/API/Element/contextmenu_event>`__ event.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``targetElementId``
      :type: (integer)
      
      The identifier of the clicked element, available as ``info.targetElementId`` in the :ref:`menus.onShown` and :ref:`menus.onClicked` events.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: `Element <https://developer.mozilla.org/en-US/docs/Web/API/Element>`__
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.overrideContext:

overrideContext(contextOptions)
-------------------------------

.. api-section-annotation-hack:: 

Show the matching menu items from this extension instead of the default menu. This should be called during a `contextmenu <https://developer.mozilla.org/en-US/docs/Web/API/Element/contextmenu_event>`__ event handler, and only applies to the menu that opens after this event.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``contextOptions``
      :type: (object)
      
      .. api-member::
         :name: [``context``]
         :type: (`string`, optional)
         
         ContextType to override, to allow menu items from other extensions in the menu. Currently only :value:`tab` is supported. ``contextOptions.showDefaults`` cannot be used with this option.
         
         Supported values:
         
         .. api-member::
            :name: :value:`tab`
      
      
      .. api-member::
         :name: [``showDefaults``]
         :type: (boolean, optional)
         
         Whether to also include default menu items in the menu.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)
         
         Required when context is :value:`tab`. Requires the :permission:`tabs` permission.
      
   

.. api-header::
   :label: Required permissions

   - :permission:`menus`
   - :permission:`menus.overrideContext`

.. _menus.refresh:

refresh()
---------

.. api-section-annotation-hack:: 

Updates the extension items in the shown menu, including changes that have been made since the menu was shown. Has no effect if the menu is hidden. Rebuilding a shown menu is an expensive operation, only invoke this method when necessary.

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.remove:

remove(menuItemId)
------------------

.. api-section-annotation-hack:: 

Removes a context menu item.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``menuItemId``
      :type: (integer or string)
      
      The ID of the context menu item to remove.
   

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.removeAll:

removeAll()
-----------

.. api-section-annotation-hack:: 

Removes all context menu items added by this extension.

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.update:

update(id, updateProperties)
----------------------------

.. api-section-annotation-hack:: 

Updates a previously created context menu item.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (integer or string)
      
      The ID of the item to update.
   
   
   .. api-member::
      :name: ``updateProperties``
      :type: (object)
      
      The properties to update. Accepts the same values as the create function.
      
      .. api-member::
         :name: [``checked``]
         :type: (boolean, optional)
      
      
      .. api-member::
         :name: [``contexts``]
         :type: (array of :ref:`menus.ContextType`, optional)
      
      
      .. api-member::
         :name: [``documentUrlPatterns``]
         :type: (array of string, optional)
      
      
      .. api-member::
         :name: [``enabled``]
         :type: (boolean, optional)
      
      
      .. api-member::
         :name: [``icons``]
         :type: (:ref:`menus.IconPath`, optional)
      
      
      .. api-member::
         :name: [``onclick``]
         :type: (function, optional)
      
      
      .. api-member::
         :name: [``parentId``]
         :type: (integer or string, optional)
         
         **Note:** You cannot change an item to be a child of one of its own descendants.
      
      
      .. api-member::
         :name: [``targetUrlPatterns``]
         :type: (array of string, optional)
      
      
      .. api-member::
         :name: [``title``]
         :type: (string, optional)
      
      
      .. api-member::
         :name: [``type``]
         :type: (:ref:`menus.ItemType`, optional)
      
      
      .. api-member::
         :name: [``viewTypes``]
         :type: (array of `ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`__, optional)
      
      
      .. api-member::
         :name: [``visible``]
         :type: (boolean, optional)
         
         Whether the item is visible in the menu.
      
   

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. rst-class:: api-main-section

Events
======

.. _menus.onClicked:

onClicked
---------

.. api-section-annotation-hack:: 

Fired when a context menu item is clicked. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for onClicked.addListener(listener)

   
   .. api-member::
      :name: ``listener(info, tab)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``info``
      :type: (:ref:`menus.OnClickData`)
      
      Information about the item clicked and the context where the click happened.
   
   
   .. api-member::
      :name: [``tab``]
      :type: (:ref:`tabs.Tab`, optional)
      
      The details of the tab where the click took place. If the click did not take place in a tab, this parameter will be missing.
   

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.onHidden:

onHidden
--------

.. api-section-annotation-hack:: 

Fired when a menu is hidden. This event is only fired if onShown has fired before.

.. api-header::
   :label: Parameters for onHidden.addListener(listener)

   
   .. api-member::
      :name: ``listener()``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.onShown:

onShown
-------

.. api-section-annotation-hack:: 

Fired when a menu is shown. The extension can add, modify or remove menu items and call :ref:`menus.refresh` to update the menu.

.. api-header::
   :label: Parameters for onShown.addListener(listener)

   
   .. api-member::
      :name: ``listener(info, tab)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``info``
      :type: (:ref:`menus.OnShowData`)
      
      Information about the context of the menu action and the created menu items.
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      
      The details of the tab where the menu was opened.
   

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. rst-class:: api-main-section

Types
=====

.. _menus.ContextType:

ContextType
-----------

.. api-section-annotation-hack:: 

The different contexts a menu can appear in. More information about each context can be found in the `Supported UI Elements <https://developer.thunderbird.net/add-ons/mailextensions/supported-ui-elements#menu-items>`__ article on developer.thunderbird.net.

.. api-header::
   :label: `string`

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         Supported values:
         
         .. api-member::
            :name: :value:`all`
         
            Equivalent to the combination of all other contexts except for :value:`tab` and :value:`tools_menu`.
         
         .. api-member::
            :name: :value:`all_message_attachments`
         
            Applies when the user context-clicks the summary of the message attachments of a displayed message with more than one attachment.
         
         .. api-member::
            :name: :value:`audio`
         
            Applies when the user context-clicks an audio element.
         
         .. api-member::
            :name: :value:`compose_action`
            :annotation: -- [Added in TB 89]
         
            Applies when the user context-clicks a composeAction button.
         
         .. api-member::
            :name: :value:`compose_action_menu`
            :annotation: -- [Added in TB 115]
         
            Applies when the user opened a composeAction button of type :value:`menu`.
         
         .. api-member::
            :name: :value:`compose_attachments`
            :annotation: -- [Added in TB 83, backported to TB 78.5.0]
         
            Applies when the user context-clicks an attachment in the compose window.
         
         .. api-member::
            :name: :value:`compose_body`
            :annotation: -- [Added in TB 115]
         
            Applies when the user context-clicks in the compose editor.
         
         .. api-member::
            :name: :value:`editable`
         
            Applies when the user context-clicks an editable element, like a textarea.
         
         .. api-member::
            :name: :value:`folder_pane`
         
            Applies when the user context-clicks in the folder pane of the main Thunderbird window.
         
         .. api-member::
            :name: :value:`frame`
         
            Applies when the user context-clicks in a nested iframe.
         
         .. api-member::
            :name: :value:`image`
         
            Applies when the user context-clicks an image.
         
         .. api-member::
            :name: :value:`link`
         
            Applies when the user context-clicks on a link.
         
         .. api-member::
            :name: :value:`message_attachments`
         
            Applies when the user context-clicks a single attachment of a displayed message.
         
         .. api-member::
            :name: :value:`message_display_action`
            :annotation: -- [Added in TB 89]
         
            Applies when the user context-clicks a messageDisplayAction button.
         
         .. api-member::
            :name: :value:`message_display_action_menu`
            :annotation: -- [Added in TB 115]
         
            Applies when the user opened a messageDisplayAction button of type :value:`menu`.
         
         .. api-member::
            :name: :value:`message_list`
         
            Applies when the user context-clicks in the message list (a.k.a. thread pane) of the main Thunderbird window.
         
         .. api-member::
            :name: :value:`page`
         
            Applies when the user context-clicks in the page, but none of the other page contexts apply (for example, the click is not on an image or a nested iframe or a link).
         
         .. api-member::
            :name: :value:`password`
         
            Applies when the user context-clicks on a password input element.
         
         .. api-member::
            :name: :value:`selection`
         
            Applies when part of the page is selected.
         
         .. api-member::
            :name: :value:`tab`
         
            Applies when the user context-clicks on a tab (specifically, this refers to the tab-strip or other user interface element enabling the user to switch from one tab to another, not to the page itself).
         
         .. api-member::
            :name: :value:`tools_menu`
            :annotation: -- [Added in TB 88]
         
            Applies when the user opens the :value:`Tools` menu of Thunderbird's main menu.
         
         .. api-member::
            :name: :value:`video`
         
            Applies when the user context-clicks a video element.
   

OR

.. api-header::
   :label: `string`

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         Supported values:
         
         .. api-member::
            :name: :value:`action`
         
            Applies when the user context-clicks a browserAction button in a Manifest V3 extension.
         
         .. api-member::
            :name: :value:`action_menu`
            :annotation: -- [Added in TB 115]
         
            Applies when the user opened a browserAction button of type :value:`menu` in a Manifest V3 extension.
   

.. _menus.ItemType:

ItemType
--------

.. api-section-annotation-hack:: 

The type of menu item.

.. api-header::
   :label: `string`

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         Supported values:
         
         .. api-member::
            :name: :value:`normal`
         
         .. api-member::
            :name: :value:`checkbox`
         
         .. api-member::
            :name: :value:`radio`
         
         .. api-member::
            :name: :value:`separator`
   

.. _menus.OnClickData:

OnClickData
-----------

.. api-section-annotation-hack:: 

Information sent when a context menu item is clicked.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``editable``
      :type: (boolean)
      
      A flag indicating whether the element is editable (text input, textarea, etc.).
   
   
   .. api-member::
      :name: ``menuItemId``
      :type: (integer or string)
      
      The ID of the menu item that was clicked.
   
   
   .. api-member::
      :name: ``modifiers``
      :type: (array of `string`)
      
      An array of keyboard modifiers that were held while the menu item was clicked.
      
      Supported values:
      
      .. api-member::
         :name: :value:`Shift`
      
      .. api-member::
         :name: :value:`Alt`
      
      .. api-member::
         :name: :value:`Command`
      
      .. api-member::
         :name: :value:`Ctrl`
      
      .. api-member::
         :name: :value:`MacCtrl`
   
   
   .. api-member::
      :name: [``attachments``]
      :type: (array of :ref:`compose.ComposeAttachment` or :ref:`messages.MessageAttachment`, optional)
      :annotation: -- [Added in TB 83]
      
      The selected attachments. The :permission:`compose` permission is required to return attachments of a message being composed. The :permission:`messagesRead` permission is required to return attachments of displayed messages.
   
   
   .. api-member::
      :name: [``button``]
      :type: (integer, optional)
      
      An integer value of button by which menu item was clicked.
   
   
   .. api-member::
      :name: [``checked``]
      :type: (boolean, optional)
      
      A flag indicating the state of a checkbox or radio item after it is clicked.
   
   
   .. api-member::
      :name: [``displayedFolder``]
      :type: (:ref:`folders.MailFolder`, optional)
      
      The displayed folder, if the context menu was opened in the message list. The :permission:`accountsRead` permission is required.
   
   
   .. api-member::
      :name: [``fieldId``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 89]
      
      An identifier of the clicked Thunderbird UI element, if any.
      
      Supported values:
      
      .. api-member::
         :name: :value:`composeSubject`
      
      .. api-member::
         :name: :value:`composeTo`
      
      .. api-member::
         :name: :value:`composeCc`
      
      .. api-member::
         :name: :value:`composeBcc`
      
      .. api-member::
         :name: :value:`composeReplyTo`
      
      .. api-member::
         :name: :value:`composeNewsgroupTo`
   
   
   .. api-member::
      :name: [``frameId``]
      :type: (integer, optional)
      
      The id of the frame of the element where the context menu was clicked.
   
   
   .. api-member::
      :name: [``frameUrl``]
      :type: (string, optional)
      
      The URL of the frame of the element where the context menu was clicked, if it was in a frame.
   
   
   .. api-member::
      :name: [``linkText``]
      :type: (string, optional)
      
      If the element is a link, the text of that link.
   
   
   .. api-member::
      :name: [``linkUrl``]
      :type: (string, optional)
      
      If the element is a link, the URL it points to.
   
   
   .. api-member::
      :name: [``mediaType``]
      :type: (string, optional)
      
      One of :value:`image`, :value:`video`, or :value:`audio` if the context menu was activated on one of these types of elements.
   
   
   .. api-member::
      :name: [``pageUrl``]
      :type: (string, optional)
      
      The URL of the page where the menu item was clicked. This property is not set if the click occurred in a context where there is no current page, such as in a launcher context menu.
   
   
   .. api-member::
      :name: [``parentMenuItemId``]
      :type: (integer or string, optional)
      
      The parent ID, if any, for the item clicked.
   
   
   .. api-member::
      :name: [``selectedAccount``]
      :type: (:ref:`accounts.MailAccount`, optional)
      :annotation: -- [Added in TB 88]
      
      The selected account, if the context menu was opened on an account entry in the folder pane. The :permission:`accountsRead` permission is required.
   
   
   .. api-member::
      :name: [``selectedFolder``]
      :type: (:ref:`folders.MailFolder`, optional)
      
      The selected folder, if the context menu was opened in the folder pane. The :permission:`accountsRead` permission is required.
   
   
   .. api-member::
      :name: [``selectedMessages``]
      :type: (:ref:`messages.MessageList`, optional)
      
      The selected messages, if the context menu was opened in the message list. The :permission:`messagesRead` permission is required.
   
   
   .. api-member::
      :name: [``selectionText``]
      :type: (string, optional)
      
      The text for the context selection, if any.
   
   
   .. api-member::
      :name: [``srcUrl``]
      :type: (string, optional)
      
      Will be present for elements with a *src* URL.
   
   
   .. api-member::
      :name: [``targetElementId``]
      :type: (integer, optional)
      
      An identifier of the clicked content element, if any. Use :ref:`menus.getTargetElement` in the page to find the corresponding element.
   
   
   .. api-member::
      :name: [``viewType``]
      :type: (`ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`__, optional)
      
      The type of view where the menu is clicked. May be unset if the menu is not associated with a view.
   
   
   .. api-member::
      :name: [``wasChecked``]
      :type: (boolean, optional)
      
      A flag indicating the state of a checkbox or radio item before it was clicked.
   

.. _menus.OnShowData:

OnShowData
----------

.. api-section-annotation-hack:: 

Information sent when a context menu is being shown. Some properties are only included if the extension has host permission for the given context, for example :permission:`activeTab` for content tabs, :permission:`compose` for compose tabs and :permission:`messagesRead` for message display tabs.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``contexts``
      :type: (array of :ref:`menus.ContextType`)
      
      A list of all contexts that apply to the menu.
   
   
   .. api-member::
      :name: ``editable``
      :type: (boolean)
      
      A flag indicating whether the element is editable (text input, textarea, etc.).
   
   
   .. api-member::
      :name: ``menuIds``
      :type: (array of integer or string)
      
      A list of IDs of the menu items that were shown.
   
   
   .. api-member::
      :name: [``attachments``]
      :type: (array of :ref:`compose.ComposeAttachment` or :ref:`messages.MessageAttachment`, optional)
      :annotation: -- [Added in TB 83]
      
      The selected attachments. The :permission:`compose` permission is required to return attachments of a message being composed. The :permission:`messagesRead` permission is required to return attachments of displayed messages.
   
   
   .. api-member::
      :name: [``displayedFolder``]
      :type: (:ref:`folders.MailFolder`, optional)
      
      The displayed folder, if the context menu was opened in the message list. The :permission:`accountsRead` permission is required.
   
   
   .. api-member::
      :name: [``fieldId``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 89]
      
      An identifier of the clicked Thunderbird UI element, if any.
      
      Supported values:
      
      .. api-member::
         :name: :value:`composeSubject`
      
      .. api-member::
         :name: :value:`composeTo`
      
      .. api-member::
         :name: :value:`composeCc`
      
      .. api-member::
         :name: :value:`composeBcc`
      
      .. api-member::
         :name: :value:`composeReplyTo`
      
      .. api-member::
         :name: :value:`composeNewsgroupTo`
   
   
   .. api-member::
      :name: [``frameUrl``]
      :type: (string, optional)
      
      The URL of the frame of the element where the context menu was clicked, if it was in a frame. **Note:** Host permission is required.
   
   
   .. api-member::
      :name: [``linkText``]
      :type: (string, optional)
      
      If the element is a link, the text of that link. **Note:** Host permission is required.
   
   
   .. api-member::
      :name: [``linkUrl``]
      :type: (string, optional)
      
      If the element is a link, the URL it points to. **Note:** Host permission is required.
   
   
   .. api-member::
      :name: [``mediaType``]
      :type: (string, optional)
      
      One of :value:`image`, :value:`video`, or :value:`audio` if the context menu was activated on one of these types of elements.
   
   
   .. api-member::
      :name: [``pageUrl``]
      :type: (string, optional)
      
      The URL of the page where the menu item was clicked. This property is not set if the click occurred in a context where there is no current page, such as in a launcher context menu. **Note:** Host permission is required.
   
   
   .. api-member::
      :name: [``selectedAccount``]
      :type: (:ref:`accounts.MailAccount`, optional)
      :annotation: -- [Added in TB 88]
      
      The selected account, if the context menu was opened on an account entry in the folder pane. The :permission:`accountsRead` permission is required.
   
   
   .. api-member::
      :name: [``selectedFolder``]
      :type: (:ref:`folders.MailFolder`, optional)
      
      The selected folder, if the context menu was opened in the folder pane. The :permission:`accountsRead` permission is required.
   
   
   .. api-member::
      :name: [``selectedMessages``]
      :type: (:ref:`messages.MessageList`, optional)
      
      The selected messages, if the context menu was opened in the message list. The :permission:`messagesRead` permission is required.
   
   
   .. api-member::
      :name: [``selectionText``]
      :type: (string, optional)
      
      The text for the context selection, if any. **Note:** Host permission is required.
   
   
   .. api-member::
      :name: [``srcUrl``]
      :type: (string, optional)
      
      Will be present for elements with a *src* URL. **Note:** Host permission is required.
   
   
   .. api-member::
      :name: [``targetElementId``]
      :type: (integer, optional)
      
      An identifier of the clicked content element, if any. Use :ref:`menus.getTargetElement` in the page to find the corresponding element.
   
   
   .. api-member::
      :name: [``viewType``]
      :type: (`ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`__, optional)
      
      The type of view where the menu is shown. May be unset if the menu is not associated with a view.
   

.. rst-class:: api-main-section

External Types
==============

The following types are not defined by this API, but by the underlying Mozilla WebExtension code base. They are included here, because there is no other public documentation available.

.. _menus.IconPath:

IconPath
--------

.. api-section-annotation-hack:: 

Either a *string* to specify a relative path of a single icon to be used for all sizes, or a *dictionary object* to specify paths for multiple icons in different sizes, so the icon does not have to be scaled for a device with a different pixel density. Each entry is a *name-value* pair with *value* being a relative path to an icon file, and *name* its size. Example: 

.. literalinclude:: includes/IconPath.json
  :language: JSON

See the `MDN documentation about choosing icon sizes <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action#choosing_icon_sizes>`__ for more information on this.

.. rst-class:: api-main-section

Properties
==========

.. _menus.ACTION_MENU_TOP_LEVEL_LIMIT:

ACTION_MENU_TOP_LEVEL_LIMIT
---------------------------

.. api-section-annotation-hack:: 

The maximum number of top level extension items that can be added to an extension action context menu. Any items beyond this limit will be ignored.
