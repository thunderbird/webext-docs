=====
menus
=====

The menus API first appeared in Thunderbird 66 (see `bug 1503421`__).
It is basically the same as the `Firefox menus API`__, but modified to suit Thunderbird.
Note that the similar ``contextMenus`` API will not be added to Thunderbird.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1503421
__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus

Use the browser.menus API to add items to the browser's menus. You can choose what types of objects your context menu additions apply to, such as images, hyperlinks, and pages.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: ``menus``
.. api-member::
   :name: ``menus.overrideContext``

.. rst-class:: api-permission-info

.. note::

  The permission ``menus`` is required to use ``menus``.

.. rst-class:: api-main-section

Functions
=========

.. _menus.create:

create(createProperties, [callback])
------------------------------------

.. api-section-annotation-hack:: 

Creates a new context menu item. Note that if an error occurs during creation, you may not find out until the creation callback fires (the details will be in `runtime.lastError <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError>`_).

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``createProperties``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``checked``]
         :type: (boolean)
         :annotation: 
         
         The initial state of a checkbox or radio item: true for selected and false for unselected. Only one radio item can be selected at a time in a given group of radio items.
      
      
      .. api-member::
         :name: [``command``]
         :type: (string)
         :annotation: 
         
         Specifies a command to issue for the context click.  Currently supports internal command _execute_browser_action.
      
      
      .. api-member::
         :name: [``contexts``]
         :type: (array of :ref:`menus.ContextType`)
         :annotation: 
         
         List of contexts this menu item will appear in. Defaults to ['page'] if not specified.
      
      
      .. api-member::
         :name: [``documentUrlPatterns``]
         :type: (array of string)
         :annotation: 
         
         Lets you restrict the item to apply only to documents whose URL matches one of the given patterns. (This applies to frames as well.) For details on the format of a pattern, see `Match Patterns <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns>`_.
      
      
      .. api-member::
         :name: [``enabled``]
         :type: (boolean)
         :annotation: 
         
         Whether this context menu item is enabled or disabled. Defaults to true.
      
      
      .. api-member::
         :name: [``icons``]
         :type: (object)
         :annotation: 
      
      
      .. api-member::
         :name: [``id``]
         :type: (string)
         :annotation: 
         
         The unique ID to assign to this item. Mandatory for event pages. Cannot be the same as another ID for this extension.
      
      
      .. api-member::
         :name: [``onclick``]
         :type: (function)
         :annotation: 
         
         A function that will be called back when the menu item is clicked. Event pages cannot use this.
      
      
      .. api-member::
         :name: [``parentId``]
         :type: (integer or string)
         :annotation: 
         
         The ID of a parent menu item; this makes the item a child of a previously added item.
      
      
      .. api-member::
         :name: [``targetUrlPatterns``]
         :type: (array of string)
         :annotation: 
         
         Similar to documentUrlPatterns, but lets you filter based on the src attribute of img/audio/video tags and the href of anchor tags.
      
      
      .. api-member::
         :name: [``title``]
         :type: (string)
         :annotation: 
         
         The text to be displayed in the item; this is *required* unless ``type`` is 'separator'. When the context is 'selection', you can use ``%s`` within the string to show the selected text. For example, if this parameter's value is "Translate '%s' to Pig Latin" and the user selects the word "cool", the context menu item for the selection is "Translate 'cool' to Pig Latin". To specify an access key for the new menu entry, include a ``&`` before the desired letter in the title. For example "&Help".
      
      
      .. api-member::
         :name: [``type``]
         :type: (:ref:`menus.ItemType`)
         :annotation: 
         
         The type of menu item. Defaults to 'normal' if not specified.
      
      
      .. api-member::
         :name: [``viewTypes``]
         :type: (array of `ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`_)
         :annotation: 
         
         List of view types where the menu item will be shown. Defaults to any view, including those without a viewType.
      
      
      .. api-member::
         :name: [``visible``]
         :type: (boolean)
         :annotation: 
         
         Whether the item is visible in the menu.
      
   
   
   .. api-member::
      :name: [``callback``]
      :type: (function)
      :annotation: 
      
      Called when the item has been created in the browser. If there were any problems creating the item, details will be available in `runtime.lastError <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError>`_.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: integer or string
      :annotation: 
      
      The ID of the newly created item.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

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
      :annotation: 
      
      The ID of the item to update.
   
   
   .. api-member::
      :name: ``updateProperties``
      :type: (object)
      :annotation: 
      
      The properties to update. Accepts the same values as the create function.
      
      .. api-member::
         :name: [``checked``]
         :type: (boolean)
         :annotation: 
      
      
      .. api-member::
         :name: [``contexts``]
         :type: (array of :ref:`menus.ContextType`)
         :annotation: 
      
      
      .. api-member::
         :name: [``documentUrlPatterns``]
         :type: (array of string)
         :annotation: 
      
      
      .. api-member::
         :name: [``enabled``]
         :type: (boolean)
         :annotation: 
      
      
      .. api-member::
         :name: [``icons``]
         :type: (object)
         :annotation: 
      
      
      .. api-member::
         :name: [``onclick``]
         :type: (function)
         :annotation: 
      
      
      .. api-member::
         :name: [``parentId``]
         :type: (integer or string)
         :annotation: 
         
         Note: You cannot change an item to be a child of one of its own descendants.
      
      
      .. api-member::
         :name: [``targetUrlPatterns``]
         :type: (array of string)
         :annotation: 
      
      
      .. api-member::
         :name: [``title``]
         :type: (string)
         :annotation: 
      
      
      .. api-member::
         :name: [``type``]
         :type: (:ref:`menus.ItemType`)
         :annotation: 
      
      
      .. api-member::
         :name: [``viewTypes``]
         :type: (array of `ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`_)
         :annotation: 
      
      
      .. api-member::
         :name: [``visible``]
         :type: (boolean)
         :annotation: 
         
         Whether the item is visible in the menu.
      
   

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
      :annotation: 
      
      The ID of the context menu item to remove.
   

.. _menus.removeAll:

removeAll()
-----------

.. api-section-annotation-hack:: 

Removes all context menu items added by this extension.

.. _menus.overrideContext:

overrideContext(contextOptions)
-------------------------------

.. api-section-annotation-hack:: 

Show the matching menu items from this extension instead of the default menu. This should be called during a 'contextmenu' DOM event handler, and only applies to the menu that opens after this event.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``contextOptions``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``context``]
         :type: (`string`)
         :annotation: 
         
         ContextType to override, to allow menu items from other extensions in the menu. Currently only 'tab' is supported. showDefaults cannot be used with this option.
         
         Supported values:
         
         .. api-member::
            :name: ``tab``
         
      
      
      .. api-member::
         :name: [``showDefaults``]
         :type: (boolean)
         :annotation: 
         
         Whether to also include default menu items in the menu.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         :annotation: 
         
         Required when context is 'tab'. Requires 'tabs' permission.
      
   

.. api-header::
   :label: Required permissions

   - ``menus.overrideContext``

.. _menus.refresh:

refresh()
---------

.. api-section-annotation-hack:: 

Updates the extension items in the shown menu, including changes that have been made since the menu was shown. Has no effect if the menu is hidden. Rebuilding a shown menu is an expensive operation, only invoke this method when necessary.

.. rst-class:: api-main-section

Events
======

.. _menus.onClicked:

onClicked(info, [tab])
----------------------

.. api-section-annotation-hack:: 

Fired when a context menu item is clicked.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``info``
      :type: (:ref:`menus.OnClickData`)
      :annotation: 
      
      Information about the item clicked and the context where the click happened.
   
   
   .. api-member::
      :name: [``tab``]
      :type: (:ref:`tabs.Tab`)
      :annotation: 
      
      The details of the tab where the click took place. If the click did not take place in a tab, this parameter will be missing.
   

.. _menus.onShown:

onShown(info, tab)
------------------

.. api-section-annotation-hack:: 

Fired when a menu is shown. The extension can add, modify or remove menu items and call menus.refresh() to update the menu.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``info``
      :type: (object)
      :annotation: 
      
      Information about the context of the menu action and the created menu items. For more information about each property, see OnClickData. The following properties are only set if the extension has host permissions for the given context: linkUrl, linkText, srcUrl, pageUrl, frameUrl, selectionText.
      
      .. api-member::
         :name: ``contexts``
         :type: (array of :ref:`menus.ContextType`)
         :annotation: 
         
         A list of all contexts that apply to the menu.
      
      
      .. api-member::
         :name: ``editable``
         :type: (boolean)
         :annotation: 
      
      
      .. api-member::
         :name: ``menuIds``
         :type: (array of None)
         :annotation: 
         
         A list of IDs of the menu items that were shown.
      
      
      .. api-member::
         :name: [``frameUrl``]
         :type: (string)
         :annotation: 
      
      
      .. api-member::
         :name: [``linkText``]
         :type: (string)
         :annotation: 
      
      
      .. api-member::
         :name: [``linkUrl``]
         :type: (string)
         :annotation: 
      
      
      .. api-member::
         :name: [``mediaType``]
         :type: (string)
         :annotation: 
      
      
      .. api-member::
         :name: [``pageUrl``]
         :type: (string)
         :annotation: 
      
      
      .. api-member::
         :name: [``selectionText``]
         :type: (string)
         :annotation: 
      
      
      .. api-member::
         :name: [``srcUrl``]
         :type: (string)
         :annotation: 
      
      
      .. api-member::
         :name: [``targetElementId``]
         :type: (integer)
         :annotation: 
      
      
      .. api-member::
         :name: [``viewType``]
         :type: (`ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`_)
         :annotation: 
      
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: 
      
      The details of the tab where the menu was opened.
   

.. _menus.onHidden:

onHidden()
----------

.. api-section-annotation-hack:: 

Fired when a menu is hidden. This event is only fired if onShown has fired before.

.. rst-class:: api-main-section

Types
=====

.. _menus.ContextType:

ContextType
-----------

.. api-section-annotation-hack:: 

The different contexts a menu can appear in. Specifying ``all`` is equivalent to the combination of all other contexts except for ``tab``.

.. api-header::
   :label: `string`

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         Supported values:
         
         .. api-member::
            :name: ``all``
         
         .. api-member::
            :name: ``page``
         
         .. api-member::
            :name: ``frame``
         
         .. api-member::
            :name: ``selection``
         
         .. api-member::
            :name: ``link``
         
         .. api-member::
            :name: ``editable``
         
         .. api-member::
            :name: ``password``
         
         .. api-member::
            :name: ``image``
         
         .. api-member::
            :name: ``video``
         
         .. api-member::
            :name: ``audio``
         
         .. api-member::
            :name: ``browser_action``
         
         .. api-member::
            :name: ``tab``
         
         .. api-member::
            :name: ``message_list``
         
         .. api-member::
            :name: ``folder_pane``
         
         .. api-member::
            :name: ``compose_attachments``
            :annotation: -- [Added in TB 83, backported to TB 78.5.0]
         
   

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
            :name: ``normal``
         
         .. api-member::
            :name: ``checkbox``
         
         .. api-member::
            :name: ``radio``
         
         .. api-member::
            :name: ``separator``
         
   

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
      :annotation: 
      
      A flag indicating whether the element is editable (text input, textarea, etc.).
   
   
   .. api-member::
      :name: ``menuItemId``
      :type: (integer or string)
      :annotation: 
      
      The ID of the menu item that was clicked.
   
   
   .. api-member::
      :name: ``modifiers``
      :type: (array of `string`)
      :annotation: 
      
      An array of keyboard modifiers that were held while the menu item was clicked.
      
      Supported values:
      
      .. api-member::
         :name: ``Shift``
      
      .. api-member::
         :name: ``Alt``
      
      .. api-member::
         :name: ``Command``
      
      .. api-member::
         :name: ``Ctrl``
      
      .. api-member::
         :name: ``MacCtrl``
      
   
   
   .. api-member::
      :name: [``attachments``]
      :type: (array of :ref:`compose.ComposeAttachment`)
      :annotation: 
      
      The selected attachments of a message being composed.
   
   
   .. api-member::
      :name: [``button``]
      :type: (integer)
      :annotation: 
      
      An integer value of button by which menu item was clicked.
   
   
   .. api-member::
      :name: [``checked``]
      :type: (boolean)
      :annotation: 
      
      A flag indicating the state of a checkbox or radio item after it is clicked.
   
   
   .. api-member::
      :name: [``displayedFolder``]
      :type: (:ref:`folders.MailFolder`)
      :annotation: 
      
      The displayed folder, if the context menu was opened in the message list. The ``accountsRead`` permission is required.
   
   
   .. api-member::
      :name: [``frameId``]
      :type: (integer)
      :annotation: 
      
      The id of the frame of the element where the context menu was clicked.
   
   
   .. api-member::
      :name: [``frameUrl``]
      :type: (string)
      :annotation: 
      
      The URL of the frame of the element where the context menu was clicked, if it was in a frame.
   
   
   .. api-member::
      :name: [``linkText``]
      :type: (string)
      :annotation: 
      
      If the element is a link, the text of that link.
   
   
   .. api-member::
      :name: [``linkUrl``]
      :type: (string)
      :annotation: 
      
      If the element is a link, the URL it points to.
   
   
   .. api-member::
      :name: [``mediaType``]
      :type: (string)
      :annotation: 
      
      One of 'image', 'video', or 'audio' if the context menu was activated on one of these types of elements.
   
   
   .. api-member::
      :name: [``pageUrl``]
      :type: (string)
      :annotation: 
      
      The URL of the page where the menu item was clicked. This property is not set if the click occurred in a context where there is no current page, such as in a launcher context menu.
   
   
   .. api-member::
      :name: [``parentMenuItemId``]
      :type: (integer or string)
      :annotation: 
      
      The parent ID, if any, for the item clicked.
   
   
   .. api-member::
      :name: [``selectedFolder``]
      :type: (:ref:`folders.MailFolder`)
      :annotation: 
      
      The selected folder, if the context menu was opened in the folder pane. The ``accountsRead`` permission is required.
   
   
   .. api-member::
      :name: [``selectedMessages``]
      :type: (:ref:`messages.MessageList`)
      :annotation: 
      
      The selected messages, if the context menu was opened in the message list. The ``messagesRead`` permission is required.
   
   
   .. api-member::
      :name: [``selectionText``]
      :type: (string)
      :annotation: 
      
      The text for the context selection, if any.
   
   
   .. api-member::
      :name: [``srcUrl``]
      :type: (string)
      :annotation: 
      
      Will be present for elements with a 'src' URL.
   
   
   .. api-member::
      :name: [``targetElementId``]
      :type: (integer)
      :annotation: 
      
      An identifier of the clicked element, if any. Use menus.getTargetElement in the page to find the corresponding element.
   
   
   .. api-member::
      :name: [``viewType``]
      :type: (`ViewType <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension/ViewType>`_)
      :annotation: 
      
      The type of view where the menu is clicked. May be unset if the menu is not associated with a view.
   
   
   .. api-member::
      :name: [``wasChecked``]
      :type: (boolean)
      :annotation: 
      
      A flag indicating the state of a checkbox or radio item before it was clicked.
   

.. rst-class:: api-main-section

Properties
==========

.. _menus.ACTION_MENU_TOP_LEVEL_LIMIT:

ACTION_MENU_TOP_LEVEL_LIMIT
---------------------------

.. api-section-annotation-hack:: 

The maximum number of top level extension items that can be added to an extension action context menu. Any items beyond this limit will be ignored.
