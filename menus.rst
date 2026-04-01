.. container:: sticky-sidebar

  ≡ menus API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

=========
menus API
=========

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

The part of the menus API that is available in all extension contexts, including content scripts.

Thunderbird's menus API is similar to the `Firefox menus API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/menus>`__, but has been adapted to better suit Thunderbird's specific needs.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _menus.permission.accounts^read:

.. api-member::
   :name: :permission:`accountsRead`
   :refid: menus-permission-accounts-read
   :refname: accountsRead

   See your mail accounts, their identities and their folders.

.. _menus.permission.active^tab:

.. api-member::
   :name: :permission:`activeTab`
   :refid: menus-permission-active-tab
   :refname: activeTab

   Grant host permission to the currently active tab, allowing to read :value:`title`, :value:`url` and :value:`favIconUrl` properties, or to inject content scripts.

.. _menus.permission.compose:

.. api-member::
   :name: :permission:`compose`
   :refid: menus-permission-compose
   :refname: compose

   Read and modify your email messages as you compose and send them.

.. _menus.permission.menus:

.. api-member::
   :name: :permission:`menus`
   :refid: menus-permission-menus
   :refname: menus

   Grant access to some or all methods of the menus API.

.. _menus.permission.menus.override^context:

.. api-member::
   :name: :permission:`menus.overrideContext`
   :refid: menus-permission-menus-override-context
   :refname: menus.overrideContext

   Grant access to the :code:`menus.overrideContext()` method, hiding all default context menu entries and overriding the entire context menu.

.. _menus.permission.messages^read:

.. api-member::
   :name: :permission:`messagesRead`
   :refid: menus-permission-messages-read
   :refname: messagesRead

   Read your email messages.

.. _menus.permission.tabs:

.. api-member::
   :name: :permission:`tabs`
   :refid: menus-permission-tabs
   :refname: tabs

   Grant host permission to all active and inactive tabs, allowing to read :value:`title`, :value:`url` and :value:`favIconUrl` properties, or to inject content scripts.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`menus` is required to use ``messenger.menus.*``.

.. rst-class:: api-main-section

Functions
=========

.. _menus.create:

create(createProperties, [callback])
------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Creates a new context menu item. Note that if an error occurs during creation, you may not find out until the creation callback fires (the details will be in `runtime.lastError <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError>`__).

.. api-header::
   :label: Parameters

   .. _menus.create.create^properties:

   .. api-member::
      :name: ``createProperties``
      :refid: menus-create-create-properties
      :refname: createProperties
      :type: (object)

      .. _menus.create.create^properties.checked:

      .. api-member::
         :name: [``checked``]
         :refid: menus-create-create-properties-checked
         :refname: checked
         :type: (boolean, optional)

         The initial state of a checkbox or radio item: :value:`true` for selected and :value:`false` for unselected. Only one radio item can be selected at a time in a given group of radio items.

      .. _menus.create.create^properties.command:

      .. api-member::
         :name: [``command``]
         :refid: menus-create-create-properties-command
         :refname: command
         :type: (string or :ref:`menus.^menu^action^command`, optional)

         Specifies a command to issue for the context click. Can either be a user defined command, or one of the predefined action commands.

      .. _menus.create.create^properties.contexts:

      .. api-member::
         :name: [``contexts``]
         :refid: menus-create-create-properties-contexts
         :refname: contexts
         :type: (array of :ref:`menus.^context^type`, optional)

         List of contexts this menu item will appear in. Defaults to :value:`['page']` if not specified.

      .. _menus.create.create^properties.document^url^patterns:

      .. api-member::
         :name: [``documentUrlPatterns``]
         :refid: menus-create-create-properties-document-url-patterns
         :refname: documentUrlPatterns
         :type: (array of string, optional)

         Lets you restrict the item to apply only to documents whose URL matches one of the given patterns. (This applies to frames as well.) For details on the format of a pattern, see `Match Patterns <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns>`__.

      .. _menus.create.create^properties.enabled:

      .. api-member::
         :name: [``enabled``]
         :refid: menus-create-create-properties-enabled
         :refname: enabled
         :type: (boolean, optional)

         Whether this context menu item is enabled or disabled. Defaults to true.

      .. _menus.create.create^properties.icons:

      .. api-member::
         :name: [``icons``]
         :refid: menus-create-create-properties-icons
         :refname: icons
         :type: (:ref:`menus.^menu^icon^path` or :ref:`menus.^menu^icon^dictionary`, optional)

         Custom icons to display next to the menu item. Custom icons can only be set for items appearing in submenus.

      .. _menus.create.create^properties.id:

      .. api-member::
         :name: [``id``]
         :refid: menus-create-create-properties-id
         :refname: id
         :type: (string, optional)

         The unique ID to assign to this item. Mandatory for event pages. Cannot be the same as another ID for this extension.

      .. _menus.create.create^properties.onclick:

      .. api-member::
         :name: [``onclick``]
         :refid: menus-create-create-properties-onclick
         :refname: onclick
         :type: (function, optional)

         A function that will be called back when the menu item is clicked. Event pages cannot use this.

      .. _menus.create.create^properties.parent^id:

      .. api-member::
         :name: [``parentId``]
         :refid: menus-create-create-properties-parent-id
         :refname: parentId
         :type: (integer or string, optional)

         The ID of a parent menu item; this makes the item a child of a previously added item.

      .. _menus.create.create^properties.target^url^patterns:

      .. api-member::
         :name: [``targetUrlPatterns``]
         :refid: menus-create-create-properties-target-url-patterns
         :refname: targetUrlPatterns
         :type: (array of string, optional)

         Similar to documentUrlPatterns, but lets you filter based on the src attribute of img/audio/video tags and the href of anchor tags.

      .. _menus.create.create^properties.title:

      .. api-member::
         :name: [``title``]
         :refid: menus-create-create-properties-title
         :refname: title
         :type: (string, optional)

         The text to be displayed in the item; this is *required* unless :value:`type` is :value:`separator`. When the context is :value:`selection`, you can use :value:`%s` within the string to show the selected text. For example, if this parameter's value is :value:`Translate '%s' to Latin` and the user selects the word :value:`cool`, the context menu item for the selection is :value:`Translate 'cool' to Latin`. To specify an access key for the new menu entry, include a :value:`&` before the desired letter in the title. For example :value:`&Help`.

      .. _menus.create.create^properties.type:

      .. api-member::
         :name: [``type``]
         :refid: menus-create-create-properties-type
         :refname: type
         :type: (:ref:`menus.^item^type`, optional)

         The type of menu item. Defaults to :value:`normal` if not specified.

      .. _menus.create.create^properties.view^types:

      .. api-member::
         :name: [``viewTypes``]
         :refid: menus-create-create-properties-view-types
         :refname: viewTypes
         :type: (array of :ref:`extension.^view^type`, optional)

         List of view types where the menu item will be shown. Defaults to any view, including those without a viewType.

      .. _menus.create.create^properties.visible:

      .. api-member::
         :name: [``visible``]
         :refid: menus-create-create-properties-visible
         :refname: visible
         :type: (boolean, optional)

         Whether the item is visible in the menu.

   .. _menus.create.callback:

   .. api-member::
      :name: [``callback``]
      :refid: menus-create-callback
      :refname: callback
      :type: (function, optional)

      Called when the item has been created in the browser. If there were any problems creating the item, details will be available in `runtime.lastError <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError>`__.

.. api-header::
   :label: Return type (`Promise`_)

   .. _menus.create.returns:

   .. api-member::
      :refid: menus-create-returns
      :refname: _returns
      :type: integer or string

      The ID of the newly created item.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.get^target^element:

getTargetElement(targetElementId)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Retrieve the element that was associated with a recent `contextmenu <https://developer.mozilla.org/en-US/docs/Web/API/Element/contextmenu_event>`__ event.

.. api-header::
   :label: Parameters

   .. _menus.get^target^element.target^element^id:

   .. api-member::
      :name: ``targetElementId``
      :refid: menus-get-target-element-target-element-id
      :refname: targetElementId
      :type: (integer)

      The identifier of the clicked element, available as :value:`info.targetElementId` in the :ref:`menus.on^shown` and :ref:`menus.on^clicked` events.

.. api-header::
   :label: Return type (`Promise`_)

   .. _menus.get^target^element.returns:

   .. api-member::
      :refid: menus-get-target-element-returns
      :refname: _returns
      :type: `Element <https://developer.mozilla.org/en-US/docs/Web/API/Element>`__

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.override^context:

overrideContext(contextOptions)
-------------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Show the matching menu items from this extension instead of the default menu. This should be called during a `contextmenu <https://developer.mozilla.org/en-US/docs/Web/API/Element/contextmenu_event>`__ event handler, and only applies to the menu that opens after this event.

.. api-header::
   :label: Parameters

   .. _menus.override^context.context^options:

   .. api-member::
      :name: ``contextOptions``
      :refid: menus-override-context-context-options
      :refname: contextOptions
      :type: (object)

      .. _menus.override^context.context^options.context:

      .. api-member::
         :name: [``context``]
         :refid: menus-override-context-context-options-context
         :refname: context
         :type: (`string`, optional)

         ContextType to override, to allow menu items from other extensions in the menu. Currently only :value:`tab` is supported. :value:`contextOptions.showDefaults` cannot be used with this option.

         Supported values:

         .. _menus.override^context.context^options.context.tab:

         .. api-member::
            :name: :value:`tab`
            :refid: menus-override-context-context-options-context-tab
            :refname: tab

      .. _menus.override^context.context^options.show^defaults:

      .. api-member::
         :name: [``showDefaults``]
         :refid: menus-override-context-context-options-show-defaults
         :refname: showDefaults
         :type: (boolean, optional)

         Whether to also include default menu items in the menu.

      .. _menus.override^context.context^options.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: menus-override-context-context-options-tab-id
         :refname: tabId
         :type: (integer, optional)

         Required when context is :value:`tab`. Requires the :permission:`tabs` permission.

.. api-header::
   :label: Required permissions

   - :permission:`menus`
   - :permission:`menus.overrideContext`

.. _menus.refresh:

refresh()
---------

.. api-section-annotation-hack:: -- [Added in TB 66]

Updates the extension items in the shown menu, including changes that have been made since the menu was shown. Has no effect if the menu is hidden. Rebuilding a shown menu is an expensive operation, only invoke this method when necessary.

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.remove:

remove(menuItemId)
------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Removes a context menu item.

.. api-header::
   :label: Parameters

   .. _menus.remove.menu^item^id:

   .. api-member::
      :name: ``menuItemId``
      :refid: menus-remove-menu-item-id
      :refname: menuItemId
      :type: (integer or string)

      The ID of the context menu item to remove.

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.remove^all:

removeAll()
-----------

.. api-section-annotation-hack:: -- [Added in TB 66]

Removes all context menu items added by this extension.

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.update:

update(id, updateProperties)
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Updates a previously created context menu item.

.. api-header::
   :label: Parameters

   .. _menus.update.id:

   .. api-member::
      :name: ``id``
      :refid: menus-update-id
      :refname: id
      :type: (integer or string)

      The ID of the item to update.

   .. _menus.update.update^properties:

   .. api-member::
      :name: ``updateProperties``
      :refid: menus-update-update-properties
      :refname: updateProperties
      :type: (object)

      The properties to update. Accepts the same values as the create function.

      .. _menus.update.update^properties.checked:

      .. api-member::
         :name: [``checked``]
         :refid: menus-update-update-properties-checked
         :refname: checked
         :type: (boolean, optional)

      .. _menus.update.update^properties.contexts:

      .. api-member::
         :name: [``contexts``]
         :refid: menus-update-update-properties-contexts
         :refname: contexts
         :type: (array of :ref:`menus.^context^type`, optional)

      .. _menus.update.update^properties.document^url^patterns:

      .. api-member::
         :name: [``documentUrlPatterns``]
         :refid: menus-update-update-properties-document-url-patterns
         :refname: documentUrlPatterns
         :type: (array of string, optional)

      .. _menus.update.update^properties.enabled:

      .. api-member::
         :name: [``enabled``]
         :refid: menus-update-update-properties-enabled
         :refname: enabled
         :type: (boolean, optional)

      .. _menus.update.update^properties.icons:

      .. api-member::
         :name: [``icons``]
         :refid: menus-update-update-properties-icons
         :refname: icons
         :type: (:ref:`menus.^menu^icon^path` or :ref:`menus.^menu^icon^dictionary`, optional)

      .. _menus.update.update^properties.onclick:

      .. api-member::
         :name: [``onclick``]
         :refid: menus-update-update-properties-onclick
         :refname: onclick
         :type: (function, optional)

      .. _menus.update.update^properties.parent^id:

      .. api-member::
         :name: [``parentId``]
         :refid: menus-update-update-properties-parent-id
         :refname: parentId
         :type: (integer or string, optional)

         The hierarchical parent of the element. Updating an element to become a child of its own descendants is not supported.

      .. _menus.update.update^properties.target^url^patterns:

      .. api-member::
         :name: [``targetUrlPatterns``]
         :refid: menus-update-update-properties-target-url-patterns
         :refname: targetUrlPatterns
         :type: (array of string, optional)

      .. _menus.update.update^properties.title:

      .. api-member::
         :name: [``title``]
         :refid: menus-update-update-properties-title
         :refname: title
         :type: (string, optional)

      .. _menus.update.update^properties.type:

      .. api-member::
         :name: [``type``]
         :refid: menus-update-update-properties-type
         :refname: type
         :type: (:ref:`menus.^item^type`, optional)

      .. _menus.update.update^properties.view^types:

      .. api-member::
         :name: [``viewTypes``]
         :refid: menus-update-update-properties-view-types
         :refname: viewTypes
         :type: (array of :ref:`extension.^view^type`, optional)

      .. _menus.update.update^properties.visible:

      .. api-member::
         :name: [``visible``]
         :refid: menus-update-update-properties-visible
         :refname: visible
         :type: (boolean, optional)

         Whether the item is visible in the menu.

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. rst-class:: api-main-section

Events
======

.. _menus.on^clicked:

onClicked
---------

.. api-section-annotation-hack:: -- [Added in TB 66]

Fired when a context menu item is clicked. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for onClicked.addListener(listener)

   .. _menus.on^clicked.listener(info, tab):

   .. api-member::
      :name: ``listener(info, tab)``
      :refid: menus-on-clicked-listener-info-tab
      :refname: listener(info, tab)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _menus.on^clicked.info:

   .. api-member::
      :name: ``info``
      :refid: menus-on-clicked-info
      :refname: info
      :type: (:ref:`menus.^on^click^data`)

      Information about the item clicked and the context where the click happened.

   .. _menus.on^clicked.tab:

   .. api-member::
      :name: [``tab``]
      :refid: menus-on-clicked-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`, optional)

      The details of the tab where the click took place. If the click did not take place in a tab, this parameter will be missing.

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.on^hidden:

onHidden
--------

.. api-section-annotation-hack:: -- [Added in TB 66]

Fired when a menu is hidden. This event is only fired if onShown has fired before.

.. api-header::
   :label: Parameters for onHidden.addListener(listener)

   .. _menus.on^hidden.listener():

   .. api-member::
      :name: ``listener()``
      :refid: menus-on-hidden-listener
      :refname: listener()

      A function that will be called when this event occurs.

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. _menus.on^shown:

onShown
-------

.. api-section-annotation-hack:: -- [Added in TB 66]

Fired when a menu is shown. The extension can add, modify or remove menu items and call :ref:`menus.refresh` to update the menu.

.. api-header::
   :label: Parameters for onShown.addListener(listener)

   .. _menus.on^shown.listener(info, tab):

   .. api-member::
      :name: ``listener(info, tab)``
      :refid: menus-on-shown-listener-info-tab
      :refname: listener(info, tab)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _menus.on^shown.info:

   .. api-member::
      :name: ``info``
      :refid: menus-on-shown-info
      :refname: info
      :type: (:ref:`menus.^on^show^data`)

      Information about the context of the menu action and the created menu items.

   .. _menus.on^shown.tab:

   .. api-member::
      :name: ``tab``
      :refid: menus-on-shown-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

      The details of the tab where the menu was opened.

.. api-header::
   :label: Required permissions

   - :permission:`menus`

.. rst-class:: api-main-section

Types
=====

.. _menus.^context^type:

ContextType
-----------

.. api-section-annotation-hack:: -- [Added in TB 66]

The different contexts a menu can appear in. Specifying :value:`all` is equivalent to the combination of all other contexts excluding :value:`tab` and :value:`tools_menu`. More information about each context can be found in the `Supported UI Elements <https://developer.thunderbird.net/add-ons/mailextensions/supported-ui-elements#menu-items>`__ article on developer.thunderbird.net.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _menus.^context^type.action:

         .. api-member::
            :name: :value:`action`
            :refid: menus-context-type-action
            :refname: action
            :annotation: -- [Added in TB 110]

            Applies when the user context-clicks a browserAction button in a Manifest V3 extension.

         .. _menus.^context^type.action_menu:

         .. api-member::
            :name: :value:`action_menu`
            :refid: menus-context-type-action-menu
            :refname: action_menu
            :annotation: -- [Added in TB 116]

            Applies when the user opened a browserAction button of type :value:`menu` in a Manifest V3 extension.

         .. _menus.^context^type.all:

         .. api-member::
            :name: :value:`all`
            :refid: menus-context-type-all
            :refname: all

            Equivalent to the combination of all other contexts except for :value:`tab` and :value:`tools_menu`.

         .. _menus.^context^type.all_message_attachments:

         .. api-member::
            :name: :value:`all_message_attachments`
            :refid: menus-context-type-all-message-attachments
            :refname: all_message_attachments
            :annotation: -- [Added in TB 98]

            Applies when the user context-clicks the summary of the message attachments of a displayed message with more than one attachment.

         .. _menus.^context^type.audio:

         .. api-member::
            :name: :value:`audio`
            :refid: menus-context-type-audio
            :refname: audio

            Applies when the user context-clicks an audio element.

         .. _menus.^context^type.compose_action:

         .. api-member::
            :name: :value:`compose_action`
            :refid: menus-context-type-compose-action
            :refname: compose_action
            :annotation: -- [Added in TB 89]

            Applies when the user context-clicks a composeAction button.

         .. _menus.^context^type.compose_action_menu:

         .. api-member::
            :name: :value:`compose_action_menu`
            :refid: menus-context-type-compose-action-menu
            :refname: compose_action_menu
            :annotation: -- [Added in TB 90]

            Applies when the user opened a composeAction button of type :value:`menu`.

         .. _menus.^context^type.compose_attachments:

         .. api-member::
            :name: :value:`compose_attachments`
            :refid: menus-context-type-compose-attachments
            :refname: compose_attachments
            :annotation: -- [Added in TB 83]

            Applies when the user context-clicks an attachment in the compose window.

         .. _menus.^context^type.compose_body:

         .. api-member::
            :name: :value:`compose_body`
            :refid: menus-context-type-compose-body
            :refname: compose_body
            :annotation: -- [Added in TB 111]

            Applies when the user context-clicks in the compose editor.

         .. _menus.^context^type.editable:

         .. api-member::
            :name: :value:`editable`
            :refid: menus-context-type-editable
            :refname: editable

            Applies when the user context-clicks an editable element, like a textarea.

         .. _menus.^context^type.folder_pane:

         .. api-member::
            :name: :value:`folder_pane`
            :refid: menus-context-type-folder-pane
            :refname: folder_pane

            Applies when the user context-clicks in the folder pane of the main Thunderbird window.

         .. _menus.^context^type.frame:

         .. api-member::
            :name: :value:`frame`
            :refid: menus-context-type-frame
            :refname: frame

            Applies when the user context-clicks in a nested iframe.

         .. _menus.^context^type.header_pane_link:

         .. api-member::
            :name: :value:`header_pane_link`
            :refid: menus-context-type-header-pane-link
            :refname: header_pane_link
            :annotation: -- [Added in TB 137]

         .. _menus.^context^type.image:

         .. api-member::
            :name: :value:`image`
            :refid: menus-context-type-image
            :refname: image

            Applies when the user context-clicks an image.

         .. _menus.^context^type.link:

         .. api-member::
            :name: :value:`link`
            :refid: menus-context-type-link
            :refname: link

            Applies when the user context-clicks on a link.

         .. _menus.^context^type.message_attachments:

         .. api-member::
            :name: :value:`message_attachments`
            :refid: menus-context-type-message-attachments
            :refname: message_attachments
            :annotation: -- [Added in TB 98]

            Applies when the user context-clicks a single attachment of a displayed message.

         .. _menus.^context^type.message_display_action:

         .. api-member::
            :name: :value:`message_display_action`
            :refid: menus-context-type-message-display-action
            :refname: message_display_action
            :annotation: -- [Added in TB 89]

            Applies when the user context-clicks a messageDisplayAction button.

         .. _menus.^context^type.message_display_action_menu:

         .. api-member::
            :name: :value:`message_display_action_menu`
            :refid: menus-context-type-message-display-action-menu
            :refname: message_display_action_menu
            :annotation: -- [Added in TB 90]

            Applies when the user opened a messageDisplayAction button of type :value:`menu`.

         .. _menus.^context^type.message_list:

         .. api-member::
            :name: :value:`message_list`
            :refid: menus-context-type-message-list
            :refname: message_list

            Applies when the user context-clicks in the message list (a.k.a. thread pane) of the main Thunderbird window.

         .. _menus.^context^type.page:

         .. api-member::
            :name: :value:`page`
            :refid: menus-context-type-page
            :refname: page

            Applies when the user context-clicks in the page, but none of the other page contexts apply (for example, the click is not on an image or a nested iframe or a link).

         .. _menus.^context^type.password:

         .. api-member::
            :name: :value:`password`
            :refid: menus-context-type-password
            :refname: password

            Applies when the user context-clicks on a password input element.

         .. _menus.^context^type.selection:

         .. api-member::
            :name: :value:`selection`
            :refid: menus-context-type-selection
            :refname: selection

            Applies when part of the page is selected.

         .. _menus.^context^type.tab:

         .. api-member::
            :name: :value:`tab`
            :refid: menus-context-type-tab
            :refname: tab

            Applies when the user context-clicks on a tab (specifically, this refers to the tab-strip or other user interface element enabling the user to switch from one tab to another, not to the page itself).

         .. _menus.^context^type.tools_menu:

         .. api-member::
            :name: :value:`tools_menu`
            :refid: menus-context-type-tools-menu
            :refname: tools_menu
            :annotation: -- [Added in TB 88]

            Applies when the user opens the :value:`Tools` menu of Thunderbird's main menu.

         .. _menus.^context^type.video:

         .. api-member::
            :name: :value:`video`
            :refid: menus-context-type-video
            :refname: video

            Applies when the user context-clicks a video element.

.. _menus.^item^type:

ItemType
--------

.. api-section-annotation-hack:: -- [Added in TB 66]

The type of menu item.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _menus.^item^type.checkbox:

         .. api-member::
            :name: :value:`checkbox`
            :refid: menus-item-type-checkbox
            :refname: checkbox

         .. _menus.^item^type.normal:

         .. api-member::
            :name: :value:`normal`
            :refid: menus-item-type-normal
            :refname: normal

         .. _menus.^item^type.radio:

         .. api-member::
            :name: :value:`radio`
            :refid: menus-item-type-radio
            :refname: radio

         .. _menus.^item^type.separator:

         .. api-member::
            :name: :value:`separator`
            :refid: menus-item-type-separator
            :refname: separator

.. _menus.^menu^action^command:

MenuActionCommand
-----------------

.. api-section-annotation-hack:: -- [Added in TB 131]

A predefined command to open an action popup.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _menus.^menu^action^command._execute_action:

         .. api-member::
            :name: :value:`_execute_action`
            :refid: menus-menu-action-command-execute-action
            :refname: _execute_action

         .. _menus.^menu^action^command._execute_compose_action:

         .. api-member::
            :name: :value:`_execute_compose_action`
            :refid: menus-menu-action-command-execute-compose-action
            :refname: _execute_compose_action

         .. _menus.^menu^action^command._execute_message_display_action:

         .. api-member::
            :name: :value:`_execute_message_display_action`
            :refid: menus-menu-action-command-execute-message-display-action
            :refname: _execute_message_display_action

.. _menus.^menu^icon^dictionary:

MenuIconDictionary
------------------

.. api-section-annotation-hack:: -- [Added in TB 124]

A *dictionary object* to specify paths for multiple icons in different sizes, so the best matching icon can be used, instead of scaling a standard icon to fit the pixel density of the user's display. Each entry is a *name-value* pair, with *name* being a size and *value* being a :ref:`menus.^menu^icon^path`.

Example:

.. code-block:: JSON

   {
     "16": "icon16.png",
     "32": "icon32.png"
   }

See the `MDN documentation about choosing icon sizes <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action#choosing_icon_sizes>`__ for more information on this topic.

.. api-header::
   :label: object

.. _menus.^menu^icon^path:

MenuIconPath
------------

.. api-section-annotation-hack:: -- [Added in TB 122]

The path for a menu icon may be a relative path to an icon file, a :value:`moz-extension:` URL, an image :value:`data:` URL, a :value:`blob:` URL, or a remote :value:`http(s):` URL.

.. api-header::
   :label: string

*or*

.. api-header::
   :label: string

.. _menus.^on^click^data:

OnClickData
-----------

.. api-section-annotation-hack:: -- [Added in TB 66]

Information sent when a context menu item is clicked.

.. api-header::
   :label: object

   .. _menus.^on^click^data.editable:

   .. api-member::
      :name: ``editable``
      :refid: menus-on-click-data-editable
      :refname: editable
      :type: (boolean)

      A flag indicating whether the element is editable (text input, textarea, etc.).

   .. _menus.^on^click^data.menu^item^id:

   .. api-member::
      :name: ``menuItemId``
      :refid: menus-on-click-data-menu-item-id
      :refname: menuItemId
      :type: (integer or string)

      The ID of the menu item that was clicked.

   .. _menus.^on^click^data.modifiers:

   .. api-member::
      :name: ``modifiers``
      :refid: menus-on-click-data-modifiers
      :refname: modifiers
      :type: (array of `string`)

      An array of keyboard modifiers that were held while the menu item was clicked.

      Supported values:

      .. api-member::
         :name: :value:`Alt`
         :refname: Alt

      .. api-member::
         :name: :value:`Command`
         :refname: Command

      .. api-member::
         :name: :value:`Ctrl`
         :refname: Ctrl

      .. api-member::
         :name: :value:`MacCtrl`
         :refname: MacCtrl

      .. api-member::
         :name: :value:`Shift`
         :refname: Shift

   .. _menus.^on^click^data.attachments:

   .. api-member::
      :name: [``attachments``]
      :refid: menus-on-click-data-attachments
      :refname: attachments
      :type: (array of :ref:`compose.^compose^attachment` or :ref:`messages.^message^attachment`, optional)
      :annotation: -- [Added in TB 83]

      The selected attachments. The :permission:`compose` permission is required to return attachments of a message being composed. The :permission:`messagesRead` permission is required to return attachments of displayed messages.

   .. _menus.^on^click^data.button:

   .. api-member::
      :name: [``button``]
      :refid: menus-on-click-data-button
      :refname: button
      :type: (integer, optional)

      An integer value of button by which menu item was clicked.

   .. _menus.^on^click^data.checked:

   .. api-member::
      :name: [``checked``]
      :refid: menus-on-click-data-checked
      :refname: checked
      :type: (boolean, optional)

      A flag indicating the state of a checkbox or radio item after it is clicked.

   .. _menus.^on^click^data.displayed^folder:

   .. api-member::
      :name: [``displayedFolder``]
      :refid: menus-on-click-data-displayed-folder
      :refname: displayedFolder
      :type: (:ref:`folders.^mail^folder`, optional)

      The displayed folder. Only available for the :value:`message_list` context. The :permission:`accountsRead` permission is required.

   .. _menus.^on^click^data.field^id:

   .. api-member::
      :name: [``fieldId``]
      :refid: menus-on-click-data-field-id
      :refname: fieldId
      :type: (`string`, optional)
      :annotation: -- [Added in TB 89]

      An identifier of the clicked Thunderbird UI element, if any.

      Supported values:

      .. _menus.^on^click^data.field^id.compose^bcc:

      .. api-member::
         :name: :value:`composeBcc`
         :refid: menus-on-click-data-field-id-compose-bcc
         :refname: composeBcc
         :annotation: -- [Added in TB 90]

      .. _menus.^on^click^data.field^id.compose^cc:

      .. api-member::
         :name: :value:`composeCc`
         :refid: menus-on-click-data-field-id-compose-cc
         :refname: composeCc
         :annotation: -- [Added in TB 90]

      .. _menus.^on^click^data.field^id.compose^newsgroup^to:

      .. api-member::
         :name: :value:`composeNewsgroupTo`
         :refid: menus-on-click-data-field-id-compose-newsgroup-to
         :refname: composeNewsgroupTo
         :annotation: -- [Added in TB 90]

      .. _menus.^on^click^data.field^id.compose^reply^to:

      .. api-member::
         :name: :value:`composeReplyTo`
         :refid: menus-on-click-data-field-id-compose-reply-to
         :refname: composeReplyTo
         :annotation: -- [Added in TB 90]

      .. _menus.^on^click^data.field^id.compose^subject:

      .. api-member::
         :name: :value:`composeSubject`
         :refid: menus-on-click-data-field-id-compose-subject
         :refname: composeSubject
         :annotation: -- [Added in TB 90]

      .. _menus.^on^click^data.field^id.compose^to:

      .. api-member::
         :name: :value:`composeTo`
         :refid: menus-on-click-data-field-id-compose-to
         :refname: composeTo
         :annotation: -- [Added in TB 90]

   .. _menus.^on^click^data.frame^id:

   .. api-member::
      :name: [``frameId``]
      :refid: menus-on-click-data-frame-id
      :refname: frameId
      :type: (integer, optional)

      The id of the frame of the element where the context menu was clicked.

   .. _menus.^on^click^data.frame^url:

   .. api-member::
      :name: [``frameUrl``]
      :refid: menus-on-click-data-frame-url
      :refname: frameUrl
      :type: (string, optional)

      The URL of the frame of the element where the context menu was clicked, if it was in a frame.

   .. _menus.^on^click^data.link^text:

   .. api-member::
      :name: [``linkText``]
      :refid: menus-on-click-data-link-text
      :refname: linkText
      :type: (string, optional)

      If the element is a link, the text of that link.

   .. _menus.^on^click^data.link^url:

   .. api-member::
      :name: [``linkUrl``]
      :refid: menus-on-click-data-link-url
      :refname: linkUrl
      :type: (string, optional)

      If the element is a link, the URL it points to.

   .. _menus.^on^click^data.media^type:

   .. api-member::
      :name: [``mediaType``]
      :refid: menus-on-click-data-media-type
      :refname: mediaType
      :type: (string, optional)

      One of :value:`image`, :value:`video`, or :value:`audio` if the context menu was activated on one of these types of elements.

   .. _menus.^on^click^data.page^url:

   .. api-member::
      :name: [``pageUrl``]
      :refid: menus-on-click-data-page-url
      :refname: pageUrl
      :type: (string, optional)

      The URL of the page where the menu item was clicked. This property is not set if the click occurred in a context where there is no current page, such as in a launcher context menu.

   .. _menus.^on^click^data.parent^menu^item^id:

   .. api-member::
      :name: [``parentMenuItemId``]
      :refid: menus-on-click-data-parent-menu-item-id
      :refname: parentMenuItemId
      :type: (integer or string, optional)

      The parent ID, if any, for the item clicked.

   .. _menus.^on^click^data.selected^folders:

   .. api-member::
      :name: [``selectedFolders``]
      :refid: menus-on-click-data-selected-folders
      :refname: selectedFolders
      :type: (array of :ref:`folders.^mail^folder`, optional)
      :annotation: -- [Added in TB 128]

      The selected folders in the folder pane. Only available for the :value:`folder_pane` context. The :permission:`accountsRead` permission is required. The returned selection includes the folders which would be affected by a context action through Thunderbird's UI, which may not be the currently selected folders. For example, if the user has multiple folders selected and opens the context menu for a folder outside that selection, only the folder for which the context menu was opened, is returned.

   .. _menus.^on^click^data.selected^messages:

   .. api-member::
      :name: [``selectedMessages``]
      :refid: menus-on-click-data-selected-messages
      :refname: selectedMessages
      :type: (:ref:`messages.^message^list`, optional)

      The selected message(s) in the message list (a.k.a. the thread pane). Only available for the :value:`message_list` context. The :permission:`messagesRead` permission is required. The returned selection includes the messages which would be affected by a context action through Thunderbird's UI, which may not be the currently selected messages. For example, if the user has multiple messages selected and opens the context menu for a message outside that selection, only the message for which the context menu was opened, is returned.

   .. _menus.^on^click^data.selection^text:

   .. api-member::
      :name: [``selectionText``]
      :refid: menus-on-click-data-selection-text
      :refname: selectionText
      :type: (string, optional)

      The text for the context selection, if any.

   .. _menus.^on^click^data.src^url:

   .. api-member::
      :name: [``srcUrl``]
      :refid: menus-on-click-data-src-url
      :refname: srcUrl
      :type: (string, optional)

      Will be present for elements with a *src* URL.

   .. _menus.^on^click^data.target^element^id:

   .. api-member::
      :name: [``targetElementId``]
      :refid: menus-on-click-data-target-element-id
      :refname: targetElementId
      :type: (integer, optional)

      An identifier of the clicked content element, if any. Use :ref:`menus.get^target^element` in the page to find the corresponding element.

   .. _menus.^on^click^data.view^type:

   .. api-member::
      :name: [``viewType``]
      :refid: menus-on-click-data-view-type
      :refname: viewType
      :type: (:ref:`extension.^view^type`, optional)

      The type of view where the menu is clicked. May be unset if the menu is not associated with a view.

   .. _menus.^on^click^data.was^checked:

   .. api-member::
      :name: [``wasChecked``]
      :refid: menus-on-click-data-was-checked
      :refname: wasChecked
      :type: (boolean, optional)

      A flag indicating the state of a checkbox or radio item before it was clicked.

.. _menus.^on^show^data:

OnShowData
----------

.. api-section-annotation-hack:: -- [Added in TB 88]

Information sent when a context menu is being shown. Some properties are only included if the extension has host permission for the given context, for example :permission:`activeTab` for content tabs, :permission:`compose` for compose tabs and :permission:`messagesRead` for message display tabs.

.. api-header::
   :label: object

   .. _menus.^on^show^data.contexts:

   .. api-member::
      :name: ``contexts``
      :refid: menus-on-show-data-contexts
      :refname: contexts
      :type: (array of :ref:`menus.^context^type`)

      A list of all contexts that apply to the menu.

   .. _menus.^on^show^data.editable:

   .. api-member::
      :name: ``editable``
      :refid: menus-on-show-data-editable
      :refname: editable
      :type: (boolean)

      A flag indicating whether the element is editable (text input, textarea, etc.).

   .. _menus.^on^show^data.menu^ids:

   .. api-member::
      :name: ``menuIds``
      :refid: menus-on-show-data-menu-ids
      :refname: menuIds
      :type: (array of integer or string)

      A list of IDs of the menu items that were shown.

   .. _menus.^on^show^data.attachments:

   .. api-member::
      :name: [``attachments``]
      :refid: menus-on-show-data-attachments
      :refname: attachments
      :type: (array of :ref:`compose.^compose^attachment` or :ref:`messages.^message^attachment`, optional)

      The selected attachments. The :permission:`compose` permission is required to return attachments of a message being composed. The :permission:`messagesRead` permission is required to return attachments of displayed messages.

   .. _menus.^on^show^data.displayed^folder:

   .. api-member::
      :name: [``displayedFolder``]
      :refid: menus-on-show-data-displayed-folder
      :refname: displayedFolder
      :type: (:ref:`folders.^mail^folder`, optional)

      The displayed folder. Only available for the :value:`message_list` context. The :permission:`accountsRead` permission is required.

   .. _menus.^on^show^data.field^id:

   .. api-member::
      :name: [``fieldId``]
      :refid: menus-on-show-data-field-id
      :refname: fieldId
      :type: (`string`, optional)
      :annotation: -- [Added in TB 89]

      An identifier of the clicked Thunderbird UI element, if any.

      Supported values:

      .. _menus.^on^show^data.field^id.compose^bcc:

      .. api-member::
         :name: :value:`composeBcc`
         :refid: menus-on-show-data-field-id-compose-bcc
         :refname: composeBcc
         :annotation: -- [Added in TB 98]

      .. _menus.^on^show^data.field^id.compose^cc:

      .. api-member::
         :name: :value:`composeCc`
         :refid: menus-on-show-data-field-id-compose-cc
         :refname: composeCc
         :annotation: -- [Added in TB 98]

      .. _menus.^on^show^data.field^id.compose^newsgroup^to:

      .. api-member::
         :name: :value:`composeNewsgroupTo`
         :refid: menus-on-show-data-field-id-compose-newsgroup-to
         :refname: composeNewsgroupTo
         :annotation: -- [Added in TB 98]

      .. _menus.^on^show^data.field^id.compose^reply^to:

      .. api-member::
         :name: :value:`composeReplyTo`
         :refid: menus-on-show-data-field-id-compose-reply-to
         :refname: composeReplyTo
         :annotation: -- [Added in TB 98]

      .. _menus.^on^show^data.field^id.compose^subject:

      .. api-member::
         :name: :value:`composeSubject`
         :refid: menus-on-show-data-field-id-compose-subject
         :refname: composeSubject
         :annotation: -- [Added in TB 98]

      .. _menus.^on^show^data.field^id.compose^to:

      .. api-member::
         :name: :value:`composeTo`
         :refid: menus-on-show-data-field-id-compose-to
         :refname: composeTo
         :annotation: -- [Added in TB 98]

   .. _menus.^on^show^data.frame^url:

   .. api-member::
      :name: [``frameUrl``]
      :refid: menus-on-show-data-frame-url
      :refname: frameUrl
      :type: (string, optional)

      The URL of the frame of the element where the context menu was clicked, if it was in a frame.

      .. note::

         Host permission is required.

   .. _menus.^on^show^data.link^text:

   .. api-member::
      :name: [``linkText``]
      :refid: menus-on-show-data-link-text
      :refname: linkText
      :type: (string, optional)

      If the element is a link, the text of that link.

      .. note::

         Host permission is required.

   .. _menus.^on^show^data.link^url:

   .. api-member::
      :name: [``linkUrl``]
      :refid: menus-on-show-data-link-url
      :refname: linkUrl
      :type: (string, optional)

      If the element is a link, the URL it points to.

      .. note::

         Host permission is required.

   .. _menus.^on^show^data.media^type:

   .. api-member::
      :name: [``mediaType``]
      :refid: menus-on-show-data-media-type
      :refname: mediaType
      :type: (string, optional)

      One of :value:`image`, :value:`video`, or :value:`audio` if the context menu was activated on one of these types of elements.

   .. _menus.^on^show^data.page^url:

   .. api-member::
      :name: [``pageUrl``]
      :refid: menus-on-show-data-page-url
      :refname: pageUrl
      :type: (string, optional)

      The URL of the page where the menu item was clicked. This property is not set if the click occurred in a context where there is no current page, such as in a launcher context menu.

      .. note::

         Host permission is required.

   .. _menus.^on^show^data.selected^folders:

   .. api-member::
      :name: [``selectedFolders``]
      :refid: menus-on-show-data-selected-folders
      :refname: selectedFolders
      :type: (array of :ref:`folders.^mail^folder`, optional)
      :annotation: -- [Added in TB 128]

      The selected folders in the folder pane. Only available for the :value:`folder_pane` context. The :permission:`accountsRead` permission is required. The returned selection includes the folders which would be affected by a context action through Thunderbird's UI, which may not be the currently selected folders. For example, if the user has multiple folders selected and opens the context menu for a folder outside that selection, only the folder for which the context menu was opened, is returned.

   .. _menus.^on^show^data.selected^messages:

   .. api-member::
      :name: [``selectedMessages``]
      :refid: menus-on-show-data-selected-messages
      :refname: selectedMessages
      :type: (:ref:`messages.^message^list`, optional)

      The selected message(s) in the message list (a.k.a. the thread pane). Only available for the :value:`message_list` context. The :permission:`messagesRead` permission is required. The returned selection includes the messages which would be affected by a context action through Thunderbird's UI, which may not be the currently selected messages. For example, if the user has multiple messages selected and opens the context menu for a message outside that selection, only the message for which the context menu was opened, is returned.

   .. _menus.^on^show^data.selection^text:

   .. api-member::
      :name: [``selectionText``]
      :refid: menus-on-show-data-selection-text
      :refname: selectionText
      :type: (string, optional)

      The text for the context selection, if any.

      .. note::

         Host permission is required.

   .. _menus.^on^show^data.src^url:

   .. api-member::
      :name: [``srcUrl``]
      :refid: menus-on-show-data-src-url
      :refname: srcUrl
      :type: (string, optional)

      Will be present for elements with a *src* URL.

      .. note::

         Host permission is required.

   .. _menus.^on^show^data.target^element^id:

   .. api-member::
      :name: [``targetElementId``]
      :refid: menus-on-show-data-target-element-id
      :refname: targetElementId
      :type: (integer, optional)

      An identifier of the clicked content element, if any. Use :ref:`menus.get^target^element` in the page to find the corresponding element.

   .. _menus.^on^show^data.view^type:

   .. api-member::
      :name: [``viewType``]
      :refid: menus-on-show-data-view-type
      :refname: viewType
      :type: (:ref:`extension.^view^type`, optional)

      The type of view where the menu is shown. May be unset if the menu is not associated with a view.

.. rst-class:: api-main-section

Properties
==========

.. _menus.^a^c^t^i^o^n_^m^e^n^u_^t^o^p_^l^e^v^e^l_^l^i^m^i^t:

ACTION_MENU_TOP_LEVEL_LIMIT
---------------------------

.. api-section-annotation-hack:: 

The maximum number of top level extension items that can be added to an extension action context menu. Any items beyond this limit will be ignored.
