.. container:: sticky-sidebar

  ≡ messageDisplayAction API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

========================
messageDisplayAction API
========================

.. role:: permission

.. role:: value

.. role:: code

Use a messageDisplayAction to put a button in the message display toolbar. In addition to its icon, a messageDisplayAction button can also have a tooltip, a badge, and a popup.

.. rst-class:: api-main-section

Manifest file properties
========================

.. _message^display^action.message_display_action:

.. api-member::
   :name: [``message_display_action``]
   :refid: message-display-action-message-display-action
   :refname: message_display_action
   :type: (object, optional)
   :annotation: -- [Added in TB 71]

   .. _message^display^action.message_display_action.browser_style:

   .. api-member::
      :name: [``browser_style``]
      :refid: message-display-action-message-display-action-browser-style
      :refname: browser_style
      :type: (boolean, optional)
      :annotation: -- [Added in TB 71]

      Enable browser styles. See the `MDN documentation on browser styles <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information.

   .. _message^display^action.message_display_action.default_area:

   .. api-member::
      :name: [``default_area``]
      :refid: message-display-action-message-display-action-default-area
      :refname: default_area
      :type: (string, optional)
      :annotation: -- [Added in TB 71]

      Currently unused.

   .. _message^display^action.message_display_action.default_icon:

   .. api-member::
      :name: [``default_icon``]
      :refid: message-display-action-message-display-action-default-icon
      :refname: default_icon
      :type: (:ref:`message^display^action.^icon^path`, optional)
      :annotation: -- [Added in TB 71]

      The paths to one or more icons for the messageDisplayAction button.

   .. _message^display^action.message_display_action.default_label:

   .. api-member::
      :name: [``default_label``]
      :refid: message-display-action-message-display-action-default-label
      :refname: default_label
      :type: (string, optional)
      :annotation: -- [Added in TB 84]

      The label of the messageDisplayAction button, defaults to its title. Can be set to an empty string to not display any label. If the containing toolbar is configured to display text only, the title will be used as fallback.

   .. _message^display^action.message_display_action.default_popup:

   .. api-member::
      :name: [``default_popup``]
      :refid: message-display-action-message-display-action-default-popup
      :refname: default_popup
      :type: (string, optional)
      :annotation: -- [Added in TB 71]

      The html document to be opened as a popup when the user clicks on the messageDisplayAction button. Ignored for action buttons with type :value:`menu`.

   .. _message^display^action.message_display_action.default_title:

   .. api-member::
      :name: [``default_title``]
      :refid: message-display-action-message-display-action-default-title
      :refname: default_title
      :type: (string, optional)
      :annotation: -- [Added in TB 71]

      The title of the messageDisplayAction button. This shows up in the tooltip and the label. Defaults to the add-on name.

   .. _message^display^action.message_display_action.theme_icons:

   .. api-member::
      :name: [``theme_icons``]
      :refid: message-display-action-message-display-action-theme-icons
      :refname: theme_icons
      :type: (array of :ref:`message^display^action.^theme^icons`, optional)
      :annotation: -- [Added in TB 71]

      Specifies dark and light icons to be used with themes. The :value:`light` icon is used on dark backgrounds and vice versa. The default theme uses the :value:`default_icon` for light backgrounds (if specified).

   .. _message^display^action.message_display_action.type:

   .. api-member::
      :name: [``type``]
      :refid: message-display-action-message-display-action-type
      :refname: type
      :type: (`string`, optional)
      :annotation: -- [Added in TB 90]

      Specifies the type of the button. Default type is :value:`button`.

      Supported values:

      .. _message^display^action.message_display_action.type.button:

      .. api-member::
         :name: :value:`button`
         :refid: message-display-action-message-display-action-type-button
         :refname: button

      .. _message^display^action.message_display_action.type.menu:

      .. api-member::
         :name: :value:`menu`
         :refid: message-display-action-message-display-action-type-menu
         :refname: menu

         The :ref:`menus.^context^type.message_display_action_menu` context of the :doc:`menus` can be used to add menu entries to a menu-typed messageDisplayAction button.

.. rst-class:: api-main-section

Permissions
===========

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`message_display_action` is required to use ``messenger.messageDisplayAction.*``.

.. rst-class:: api-main-section

Functions
=========

.. _message^display^action.disable:

disable([tabId])
----------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Disables the messageDisplayAction button for a specific tab (if a :value:`tabId` is provided), or for all tabs which do not have a custom enable state. Once the enable state of a tab has been updated individually, all further changes to its state have to be done individually as well.

.. api-header::
   :label: Parameters

   .. _message^display^action.disable.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: message-display-action-disable-tab-id
      :refname: tabId
      :type: (integer, optional)

      The id of the tab for which you want to modify the messageDisplayAction button.

.. _message^display^action.enable:

enable([tabId])
---------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Enables the messageDisplayAction button for a specific tab (if a :value:`tabId` is provided), or for all tabs which do not have a custom enable state. Once the enable state of a tab has been updated individually, all further changes to its state have to be done individually as well. By default, a messageDisplayAction button is enabled.

.. api-header::
   :label: Parameters

   .. _message^display^action.enable.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: message-display-action-enable-tab-id
      :refname: tabId
      :type: (integer, optional)

      The id of the tab for which you want to modify the messageDisplayAction button.

.. _message^display^action.get^badge^background^color:

getBadgeBackgroundColor(details)
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Gets the badge background color of the messageDisplayAction button.

.. api-header::
   :label: Parameters

   .. _message^display^action.get^badge^background^color.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-get-badge-background-color-details
      :refname: details
      :type: (object)

      .. _message^display^action.get^badge^background^color.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-get-badge-background-color-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the badge background color should be retrieved. If no tab is specified, the global value is retrieved.

      .. _message^display^action.get^badge^background^color.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-get-badge-background-color-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _message^display^action.get^badge^background^color.returns:

   .. api-member::
      :refid: message-display-action-get-badge-background-color-returns
      :refname: _returns
      :type: :ref:`message^display^action.^color^array`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _message^display^action.get^badge^text:

getBadgeText(details)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Gets the badge text of the messageDisplayAction button.

.. api-header::
   :label: Parameters

   .. _message^display^action.get^badge^text.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-get-badge-text-details
      :refname: details
      :type: (object)

      .. _message^display^action.get^badge^text.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-get-badge-text-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the badge text should be retrieved. If no tab is specified, the global value is retrieved.

      .. _message^display^action.get^badge^text.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-get-badge-text-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _message^display^action.get^badge^text.returns:

   .. api-member::
      :refid: message-display-action-get-badge-text-returns
      :refname: _returns
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _message^display^action.get^badge^text^color:

getBadgeTextColor(details)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Gets the text color of the badge.

.. api-header::
   :label: Parameters

   .. _message^display^action.get^badge^text^color.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-get-badge-text-color-details
      :refname: details
      :type: (object)

      .. _message^display^action.get^badge^text^color.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-get-badge-text-color-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Specifies for which tab the badge text color should be retrieved. If no tab is specified, the global value is retrieved.

      .. _message^display^action.get^badge^text^color.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-get-badge-text-color-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _message^display^action.get^badge^text^color.returns:

   .. api-member::
      :refid: message-display-action-get-badge-text-color-returns
      :refname: _returns
      :type: :ref:`message^display^action.^color^array`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _message^display^action.get^label:

getLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 84]

Gets the label of the messageDisplayAction button. Returns :value:`null`, if no label has been set and the title is used.

.. api-header::
   :label: Parameters

   .. _message^display^action.get^label.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-get-label-details
      :refname: details
      :type: (object)

      .. _message^display^action.get^label.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-get-label-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the label should be retrieved. If no tab is specified, the global value is retrieved.

      .. _message^display^action.get^label.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-get-label-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _message^display^action.get^label.returns:

   .. api-member::
      :refid: message-display-action-get-label-returns
      :refname: _returns
      :type: string or null

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _message^display^action.get^popup:

getPopup(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Gets the html document set as the popup for this messageDisplayAction button.

.. api-header::
   :label: Parameters

   .. _message^display^action.get^popup.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-get-popup-details
      :refname: details
      :type: (object)

      .. _message^display^action.get^popup.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-get-popup-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the popup document should be retrieved. If no tab is specified, the global value is retrieved.

      .. _message^display^action.get^popup.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-get-popup-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _message^display^action.get^popup.returns:

   .. api-member::
      :refid: message-display-action-get-popup-returns
      :refname: _returns
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _message^display^action.get^title:

getTitle(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Gets the title of the messageDisplayAction button.

.. api-header::
   :label: Parameters

   .. _message^display^action.get^title.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-get-title-details
      :refname: details
      :type: (object)

      .. _message^display^action.get^title.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-get-title-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the title should be retrieved. If no tab is specified, the global value is retrieved.

      .. _message^display^action.get^title.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-get-title-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _message^display^action.get^title.returns:

   .. api-member::
      :refid: message-display-action-get-title-returns
      :refname: _returns
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _message^display^action.is^enabled:

isEnabled(details)
------------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Checks whether the messageDisplayAction button is enabled.

.. api-header::
   :label: Parameters

   .. _message^display^action.is^enabled.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-is-enabled-details
      :refname: details
      :type: (object)

      .. _message^display^action.is^enabled.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-is-enabled-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the state should be retrieved. If no tab is specified, the global value is retrieved.

      .. _message^display^action.is^enabled.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-is-enabled-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _message^display^action.is^enabled.returns:

   .. api-member::
      :refid: message-display-action-is-enabled-returns
      :refname: _returns
      :type: boolean
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _message^display^action.open^popup:

openPopup([options])
--------------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Opens the action's popup window in the specified window. Defaults to the current window. Returns false if the popup could not be opened because the action has no popup, is of type :value:`menu`, is disabled or has been removed from the toolbar.

.. api-header::
   :label: Parameters

   .. _message^display^action.open^popup.options:

   .. api-member::
      :name: [``options``]
      :refid: message-display-action-open-popup-options
      :refname: options
      :type: (object, optional)
      :annotation: -- [Added in TB 113]

      An object with information about the popup to open.

      .. _message^display^action.open^popup.options.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-open-popup-options-window-id
         :refname: windowId
         :type: (integer, optional)
         :annotation: -- [Added in TB 113]

         Defaults to the current window.

.. api-header::
   :label: Return type (`Promise`_)

   .. _message^display^action.open^popup.returns:

   .. api-member::
      :refid: message-display-action-open-popup-returns
      :refname: _returns
      :type: boolean
      :annotation: -- [Added in TB 113]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _message^display^action.set^badge^background^color:

setBadgeBackgroundColor(details)
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Sets the background color for the badge.

.. api-header::
   :label: Parameters

   .. _message^display^action.set^badge^background^color.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-set-badge-background-color-details
      :refname: details
      :type: (object)

      .. _message^display^action.set^badge^background^color.details.color:

      .. api-member::
         :name: ``color``
         :refid: message-display-action-set-badge-background-color-details-color
         :refname: color
         :type: (string or :ref:`message^display^action.^color^array` or null)

         The color to use as background in the badge. Cleared by setting it to :value:`null`.

      .. _message^display^action.set^badge^background^color.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-set-badge-background-color-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the background color for the badge only for the given tab.

      .. _message^display^action.set^badge^background^color.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-set-badge-background-color-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _message^display^action.set^badge^text:

setBadgeText(details)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Sets the badge text for the messageDisplayAction button. The badge is displayed on top of the icon.

.. api-header::
   :label: Parameters

   .. _message^display^action.set^badge^text.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-set-badge-text-details
      :refname: details
      :type: (object)

      .. _message^display^action.set^badge^text.details.text:

      .. api-member::
         :name: ``text``
         :refid: message-display-action-set-badge-text-details-text
         :refname: text
         :type: (string or null)

         Any number of characters can be passed, but only about four can fit in the space. Cleared by setting it to :value:`null` or an empty string.

      .. _message^display^action.set^badge^text.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-set-badge-text-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the badge text only for the given tab.

      .. _message^display^action.set^badge^text.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-set-badge-text-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _message^display^action.set^badge^text^color:

setBadgeTextColor(details)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Sets the text color for the badge.

.. api-header::
   :label: Parameters

   .. _message^display^action.set^badge^text^color.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-set-badge-text-color-details
      :refname: details
      :type: (object)

      .. _message^display^action.set^badge^text^color.details.color:

      .. api-member::
         :name: ``color``
         :refid: message-display-action-set-badge-text-color-details-color
         :refname: color
         :type: (string or :ref:`message^display^action.^color^array` or null)

         The color to use as text color in the badge. Cleared by setting it to :value:`null`.

      .. _message^display^action.set^badge^text^color.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-set-badge-text-color-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the text color for the badge only for the given tab.

      .. _message^display^action.set^badge^text^color.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-set-badge-text-color-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _message^display^action.set^icon:

setIcon(details)
----------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Sets the icon for the messageDisplayAction button. Either the :value:`path` or the :value:`imageData` property must be specified.

.. api-header::
   :label: Parameters

   .. _message^display^action.set^icon.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-set-icon-details
      :refname: details
      :type: (object)

      .. _message^display^action.set^icon.details.image^data:

      .. api-member::
         :name: [``imageData``]
         :refid: message-display-action-set-icon-details-image-data
         :refname: imageData
         :type: (:ref:`message^display^action.^image^data^type` or :ref:`message^display^action.^image^data^dictionary`, optional)

         The image data for one or more icons for the composeAction button.

      .. _message^display^action.set^icon.details.path:

      .. api-member::
         :name: [``path``]
         :refid: message-display-action-set-icon-details-path
         :refname: path
         :type: (:ref:`message^display^action.^icon^path`, optional)

         The paths to one or more icons for the messageDisplayAction button.

      .. _message^display^action.set^icon.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-set-icon-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the icon only for the given tab.

      .. _message^display^action.set^icon.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-set-icon-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _message^display^action.set^label:

setLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 84]

Sets the label of the messageDisplayAction button. Can be used to set different values for the tooltip (defined by the title) and the label. Additionally, the label can be set to an empty string, not showing any label at all.

.. api-header::
   :label: Parameters

   .. _message^display^action.set^label.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-set-label-details
      :refname: details
      :type: (object)

      .. _message^display^action.set^label.details.label:

      .. api-member::
         :name: ``label``
         :refid: message-display-action-set-label-details-label
         :refname: label
         :type: (string or null)

         A string the messageDisplayAction button should use as its label, overriding the defined title. Can be set to an empty string to not display any label at all. If the containing toolbar is configured to display text only, its title will be used. Cleared by setting it to :value:`null`.

      .. _message^display^action.set^label.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-set-label-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the label only for the given tab.

      .. _message^display^action.set^label.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-set-label-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _message^display^action.set^popup:

setPopup(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Sets the html document to be opened as a popup when the user clicks on the messageDisplayAction button.

.. api-header::
   :label: Parameters

   .. _message^display^action.set^popup.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-set-popup-details
      :refname: details
      :type: (object)

      .. _message^display^action.set^popup.details.popup:

      .. api-member::
         :name: ``popup``
         :refid: message-display-action-set-popup-details-popup
         :refname: popup
         :type: (string or null)

         The html file to show in a popup. Can be set to an empty string to not open a popup. Cleared by setting it to :value:`null` (action will use the popup value defined in the manifest).

      .. _message^display^action.set^popup.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-set-popup-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the popup only for the given tab.

      .. _message^display^action.set^popup.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-set-popup-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _message^display^action.set^title:

setTitle(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Sets the title of the messageDisplayAction button. Is used as tooltip and as the label.

.. api-header::
   :label: Parameters

   .. _message^display^action.set^title.details:

   .. api-member::
      :name: ``details``
      :refid: message-display-action-set-title-details
      :refname: details
      :type: (object)

      .. _message^display^action.set^title.details.title:

      .. api-member::
         :name: ``title``
         :refid: message-display-action-set-title-details-title
         :refname: title
         :type: (string or null)

         A string the messageDisplayAction button should display as its label and when moused over. Cleared by setting it to :value:`null` or an empty string (title defined the manifest will be used).

      .. _message^display^action.set^title.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: message-display-action-set-title-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the title only for the given tab.

      .. _message^display^action.set^title.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-action-set-title-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. rst-class:: api-main-section

Events
======

.. _message^display^action.on^clicked:

onClicked
---------

.. api-section-annotation-hack:: -- [Added in TB 71]

Fired when a messageDisplayAction button is clicked. This event will not fire if the messageDisplayAction has a popup. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for onClicked.addListener(listener)

   .. _message^display^action.on^clicked.listener(tab, info):

   .. api-member::
      :name: ``listener(tab, info)``
      :refid: message-display-action-on-clicked-listener-tab-info
      :refname: listener(tab, info)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _message^display^action.on^clicked.tab:

   .. api-member::
      :name: ``tab``
      :refid: message-display-action-on-clicked-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

   .. _message^display^action.on^clicked.info:

   .. api-member::
      :name: [``info``]
      :refid: message-display-action-on-clicked-info
      :refname: info
      :type: (:ref:`message^display^action.^on^click^data`, optional)
      :annotation: -- [Added in TB 74]

.. rst-class:: api-main-section

Types
=====

.. _message^display^action.^color^array:

ColorArray
----------

.. api-section-annotation-hack:: -- [Added in TB 71]

An array of four integers in the range [0,255] that make up the RGBA color. For example, opaque red is :value:`[255, 0, 0, 255]`.

.. api-header::
   :label: array of integer

.. _message^display^action.^extension^file^url:

ExtensionFileUrl
----------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension, must not be empty and can be localized.

.. api-header::
   :label: string

.. _message^display^action.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _message^display^action.^icon^path:

IconPath
--------

.. api-section-annotation-hack:: 

Either a *string* to specify a relative path of a single icon to be used for all sizes, or a *dictionary object* to specify paths for multiple icons in different sizes, so the icon does not have to be scaled for a device with a different pixel density. Each entry is a *name-value* pair with *value* being a relative path to an icon file, and *name* its size. Example:

.. code-block:: JSON

   {
     "16": "icon16.png",
     "32": "icon32.png"
   }

See the `MDN documentation about choosing icon sizes <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action#choosing_icon_sizes>`__ for more information on this topic.

.. api-header::
   :label: object

*or*

.. api-header::
   :label: :ref:`message^display^action.^extension^file^url`

.. _message^display^action.^image^data^dictionary:

ImageDataDictionary
-------------------

.. api-section-annotation-hack:: -- [Added in TB 90]

A *dictionary object* to specify multiple `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__ objects in different sizes, so the icon does not have to be scaled for a device with a different pixel density. Each entry is a *name-value* pair with *value* being an `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__ object, and *name* its size.

.. api-header::
   :label: object

.. _message^display^action.^image^data^type:

ImageDataType
-------------

.. api-section-annotation-hack:: -- [Added in TB 71]

Pixel data for an image. Must be an `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__ object (for example, from a `canvas <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas>`__ element).

.. api-header::
   :label: `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__

.. _message^display^action.^on^click^data:

OnClickData
-----------

.. api-section-annotation-hack:: -- [Added in TB 74]

Information sent when a messageDisplayAction button is clicked.

.. api-header::
   :label: object

   .. _message^display^action.^on^click^data.modifiers:

   .. api-member::
      :name: ``modifiers``
      :refid: message-display-action-on-click-data-modifiers
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

         Only available on macOS.

      .. api-member::
         :name: :value:`Ctrl`
         :refname: Ctrl

         Not available on macOS.

      .. api-member::
         :name: :value:`MacCtrl`
         :refname: MacCtrl

         Only available on macOS, but of limited use in a click event: Holding down the CTRL key while clicking with the mouse is referred to as a 'CTRL click' under macOS and is interpreted as a right mouse click. In a default profile  the :value:`dom.event.treat_ctrl_click_as_right_click.disabled` preference is not enabled and the :value:`MacCtrl` modifier key is not forwarded to the API.

      .. api-member::
         :name: :value:`Shift`
         :refname: Shift

   .. _message^display^action.^on^click^data.button:

   .. api-member::
      :name: [``button``]
      :refid: message-display-action-on-click-data-button
      :refname: button
      :type: (integer, optional)

      An integer value of button by which menu item was clicked.

.. _message^display^action.^theme^icons:

ThemeIcons
----------

.. api-section-annotation-hack:: 

Define a set of icons for themes depending on whether Thunderbird detects that the theme uses dark or light text. All provided URLs must be relative to the :value:`manifest.json` file.

.. api-header::
   :label: object

   .. _message^display^action.^theme^icons.dark:

   .. api-member::
      :name: ``dark``
      :refid: message-display-action-theme-icons-dark
      :refname: dark
      :type: (:ref:`message^display^action.^extension^u^r^l`)

      The dark icon to use for light themes

   .. _message^display^action.^theme^icons.light:

   .. api-member::
      :name: ``light``
      :refid: message-display-action-theme-icons-light
      :refname: light
      :type: (:ref:`message^display^action.^extension^u^r^l`)

      A light icon to use for dark themes

   .. _message^display^action.^theme^icons.size:

   .. api-member::
      :name: ``size``
      :refid: message-display-action-theme-icons-size
      :refname: size
      :type: (integer)

      The size of the icons
