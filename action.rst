.. container:: sticky-sidebar

  ≡ action API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

==========
action API
==========

.. role:: permission

.. role:: value

.. role:: code

Use the action API to add a button to Thunderbird's unified toolbar. In addition to its icon, an action button can also have a tooltip, a badge, and a popup.

.. rst-class:: api-main-section

Manifest file properties
========================

.. _action.action:

.. api-member::
   :name: [``action``]
   :refid: action-action
   :refname: action
   :type: (object, optional)
   :annotation: -- [Added in TB 105]

   .. _action.action.allowed_spaces:

   .. api-member::
      :name: [``allowed_spaces``]
      :refid: action-action-allowed-spaces
      :refname: allowed_spaces
      :type: (array of `string`, optional)
      :annotation: -- [Added in TB 115]

      Defines for which spaces the action button will be added to Thunderbird's unified toolbar. Defaults to only allowing the action in the :value:`mail` space. The :value:`default` space is for tabs that don't belong to any space. If this is an empty array, the action button is shown in all spaces.

      Supported values:

      .. api-member::
         :name: :value:`addressbook`
         :refname: addressbook

      .. api-member::
         :name: :value:`calendar`
         :refname: calendar

      .. api-member::
         :name: :value:`chat`
         :refname: chat

      .. api-member::
         :name: :value:`default`
         :refname: default

      .. api-member::
         :name: :value:`mail`
         :refname: mail

      .. api-member::
         :name: :value:`settings`
         :refname: settings

      .. api-member::
         :name: :value:`tasks`
         :refname: tasks

   .. _action.action.browser_style:

   .. api-member::
      :name: [``browser_style``]
      :refid: action-action-browser-style
      :refname: browser_style
      :type: (boolean, optional)
      :annotation: -- [Added in TB 115]

      Enable browser styles. See the `MDN documentation on browser styles <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information.

   .. _action.action.default_area:

   .. api-member::
      :name: [``default_area``]
      :refid: action-action-default-area
      :refname: default_area
      :type: (string, optional) **Deprecated.**
      :annotation: -- [Added in TB 128]

      Defines the location the action button will appear. Deprecated and ignored. Replaced by :value:`allowed_spaces`

   .. _action.action.default_icon:

   .. api-member::
      :name: [``default_icon``]
      :refid: action-action-default-icon
      :refname: default_icon
      :type: (:ref:`action.^icon^path`, optional)
      :annotation: -- [Added in TB 115]

      The paths to one or more icons for the action button.

   .. _action.action.default_label:

   .. api-member::
      :name: [``default_label``]
      :refid: action-action-default-label
      :refname: default_label
      :type: (string, optional)
      :annotation: -- [Added in TB 115]

      The label of the action button, defaults to its title. Can be set to an empty string to not display any label. If the containing toolbar is configured to display text only, the title will be used as fallback.

   .. _action.action.default_popup:

   .. api-member::
      :name: [``default_popup``]
      :refid: action-action-default-popup
      :refname: default_popup
      :type: (string, optional)
      :annotation: -- [Added in TB 115]

      The html document to be opened as a popup when the user clicks on the action button. Ignored for action buttons with type :value:`menu`.

   .. _action.action.default_title:

   .. api-member::
      :name: [``default_title``]
      :refid: action-action-default-title
      :refname: default_title
      :type: (string, optional)
      :annotation: -- [Added in TB 115]

      The title of the action button. This shows up in the tooltip and the label. Defaults to the add-on name.

   .. _action.action.default_windows:

   .. api-member::
      :name: [``default_windows``]
      :refid: action-action-default-windows
      :refname: default_windows
      :type: (array of `string`, optional)
      :annotation: -- [Added in TB 115]

      Defines the windows, the action button should appear in. Defaults to showing it only in the :value:`normal` Thunderbird window, but can also be shown in the :value:`messageDisplay` window.

      Supported values:

      .. api-member::
         :name: :value:`messageDisplay`
         :refname: messageDisplay

      .. api-member::
         :name: :value:`normal`
         :refname: normal

   .. _action.action.theme_icons:

   .. api-member::
      :name: [``theme_icons``]
      :refid: action-action-theme-icons
      :refname: theme_icons
      :type: (array of :ref:`action.^theme^icons`, optional)
      :annotation: -- [Added in TB 115]

      Specifies dark and light icons to be used with themes. The :value:`light` icon is used on dark backgrounds and vice versa. The default theme uses the :value:`default_icon` for light backgrounds (if specified).

   .. _action.action.type:

   .. api-member::
      :name: [``type``]
      :refid: action-action-type
      :refname: type
      :type: (`string`, optional)
      :annotation: -- [Added in TB 116]

      Specifies the type of the button. Default type is :value:`button`.

      Supported values:

      .. _action.action.type.button:

      .. api-member::
         :name: :value:`button`
         :refid: action-action-type-button
         :refname: button

      .. _action.action.type.menu:

      .. api-member::
         :name: :value:`menu`
         :refid: action-action-type-menu
         :refname: menu

         The :ref:`menus.^context^type.action_menu` context of the :doc:`menus` can be used to add menu entries to a menu-typed action button.

.. rst-class:: api-main-section

Permissions
===========

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`action` is required to use ``messenger.action.*``.

.. rst-class:: api-main-section

Functions
=========

.. _action.disable:

disable([tabId])
----------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Disables the action button for a specific tab (if a :value:`tabId` is provided), or for all tabs which do not have a custom enable state. Once the enable state of a tab has been updated individually, all further changes to its state have to be done individually as well.

.. api-header::
   :label: Parameters

   .. _action.disable.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: action-disable-tab-id
      :refname: tabId
      :type: (integer, optional)

      The id of the tab for which you want to modify the action button.

.. _action.enable:

enable([tabId])
---------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Enables the action button for a specific tab (if a :value:`tabId` is provided), or for all tabs which do not have a custom enable state. Once the enable state of a tab has been updated individually, all further changes to its state have to be done individually as well. By default, an action button is enabled.

.. api-header::
   :label: Parameters

   .. _action.enable.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: action-enable-tab-id
      :refname: tabId
      :type: (integer, optional)

      The id of the tab for which you want to modify the action button.

.. _action.get^badge^background^color:

getBadgeBackgroundColor(details)
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Gets the badge background color of the action button.

.. api-header::
   :label: Parameters

   .. _action.get^badge^background^color.details:

   .. api-member::
      :name: ``details``
      :refid: action-get-badge-background-color-details
      :refname: details
      :type: (object)

      .. _action.get^badge^background^color.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-get-badge-background-color-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the badge background color should be retrieved. If no tab is specified, the global value is retrieved.

      .. _action.get^badge^background^color.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-get-badge-background-color-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _action.get^badge^background^color.returns:

   .. api-member::
      :refid: action-get-badge-background-color-returns
      :refname: _returns
      :type: :ref:`action.^color^array`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.get^badge^text:

getBadgeText(details)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Gets the badge text of the action button.

.. api-header::
   :label: Parameters

   .. _action.get^badge^text.details:

   .. api-member::
      :name: ``details``
      :refid: action-get-badge-text-details
      :refname: details
      :type: (object)

      .. _action.get^badge^text.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-get-badge-text-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the badge text should be retrieved. If no tab is specified, the global value is retrieved.

      .. _action.get^badge^text.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-get-badge-text-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _action.get^badge^text.returns:

   .. api-member::
      :refid: action-get-badge-text-returns
      :refname: _returns
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.get^badge^text^color:

getBadgeTextColor(details)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Gets the text color of the badge.

.. api-header::
   :label: Parameters

   .. _action.get^badge^text^color.details:

   .. api-member::
      :name: ``details``
      :refid: action-get-badge-text-color-details
      :refname: details
      :type: (object)

      .. _action.get^badge^text^color.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-get-badge-text-color-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Specifies for which tab the badge text color should be retrieved. If no tab is specified, the global value is retrieved.

      .. _action.get^badge^text^color.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-get-badge-text-color-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _action.get^badge^text^color.returns:

   .. api-member::
      :refid: action-get-badge-text-color-returns
      :refname: _returns
      :type: :ref:`action.^color^array`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.get^label:

getLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Gets the label of the action button. Returns :value:`null`, if no label has been set and the title is used.

.. api-header::
   :label: Parameters

   .. _action.get^label.details:

   .. api-member::
      :name: ``details``
      :refid: action-get-label-details
      :refname: details
      :type: (object)

      .. _action.get^label.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-get-label-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the label should be retrieved. If no tab is specified, the global value is retrieved.

      .. _action.get^label.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-get-label-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _action.get^label.returns:

   .. api-member::
      :refid: action-get-label-returns
      :refname: _returns
      :type: string or null

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.get^popup:

getPopup(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Gets the html document set as the popup for this action button.

.. api-header::
   :label: Parameters

   .. _action.get^popup.details:

   .. api-member::
      :name: ``details``
      :refid: action-get-popup-details
      :refname: details
      :type: (object)

      .. _action.get^popup.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-get-popup-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the popup document should be retrieved. If no tab is specified, the global value is retrieved.

      .. _action.get^popup.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-get-popup-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _action.get^popup.returns:

   .. api-member::
      :refid: action-get-popup-returns
      :refname: _returns
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.get^title:

getTitle(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Gets the title of the action button.

.. api-header::
   :label: Parameters

   .. _action.get^title.details:

   .. api-member::
      :name: ``details``
      :refid: action-get-title-details
      :refname: details
      :type: (object)

      .. _action.get^title.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-get-title-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the title should be retrieved. If no tab is specified, the global value is retrieved.

      .. _action.get^title.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-get-title-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _action.get^title.returns:

   .. api-member::
      :refid: action-get-title-returns
      :refname: _returns
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.is^enabled:

isEnabled(details)
------------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Checks whether the action button is enabled.

.. api-header::
   :label: Parameters

   .. _action.is^enabled.details:

   .. api-member::
      :name: ``details``
      :refid: action-is-enabled-details
      :refname: details
      :type: (object)

      .. _action.is^enabled.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-is-enabled-details-tab-id
         :refname: tabId
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the state should be retrieved. If no tab is specified, the global value is retrieved.

      .. _action.is^enabled.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-is-enabled-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. _action.is^enabled.returns:

   .. api-member::
      :refid: action-is-enabled-returns
      :refname: _returns
      :type: boolean

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.open^popup:

openPopup([options])
--------------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Opens the action's popup window in the specified window. Defaults to the current window. Returns false if the popup could not be opened because the action has no popup, is of type :value:`menu`, is disabled or has been removed from the toolbar.

.. api-header::
   :label: Parameters

   .. _action.open^popup.options:

   .. api-member::
      :name: [``options``]
      :refid: action-open-popup-options
      :refname: options
      :type: (object, optional)
      :annotation: -- [Added in TB 113]

      An object with information about the popup to open.

      .. _action.open^popup.options.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-open-popup-options-window-id
         :refname: windowId
         :type: (integer, optional)
         :annotation: -- [Added in TB 113]

         Defaults to the current window.

.. api-header::
   :label: Return type (`Promise`_)

   .. _action.open^popup.returns:

   .. api-member::
      :refid: action-open-popup-returns
      :refname: _returns
      :type: boolean
      :annotation: -- [Added in TB 113]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.set^badge^background^color:

setBadgeBackgroundColor(details)
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Sets the background color for the badge.

.. api-header::
   :label: Parameters

   .. _action.set^badge^background^color.details:

   .. api-member::
      :name: ``details``
      :refid: action-set-badge-background-color-details
      :refname: details
      :type: (object)

      .. _action.set^badge^background^color.details.color:

      .. api-member::
         :name: ``color``
         :refid: action-set-badge-background-color-details-color
         :refname: color
         :type: (string or :ref:`action.^color^array` or null)

         The color to use as background in the badge. Cleared by setting it to :value:`null`.

      .. _action.set^badge^background^color.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-set-badge-background-color-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the background color for the badge only for the given tab.

      .. _action.set^badge^background^color.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-set-badge-background-color-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _action.set^badge^text:

setBadgeText(details)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Sets the badge text for the action button. The badge is displayed on top of the icon.

.. api-header::
   :label: Parameters

   .. _action.set^badge^text.details:

   .. api-member::
      :name: ``details``
      :refid: action-set-badge-text-details
      :refname: details
      :type: (object)

      .. _action.set^badge^text.details.text:

      .. api-member::
         :name: ``text``
         :refid: action-set-badge-text-details-text
         :refname: text
         :type: (string or null)

         Any number of characters can be passed, but only about four can fit in the space. Cleared by setting it to :value:`null` or an empty string.

      .. _action.set^badge^text.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-set-badge-text-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the badge text only for the given tab.

      .. _action.set^badge^text.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-set-badge-text-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _action.set^badge^text^color:

setBadgeTextColor(details)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Sets the text color for the badge.

.. api-header::
   :label: Parameters

   .. _action.set^badge^text^color.details:

   .. api-member::
      :name: ``details``
      :refid: action-set-badge-text-color-details
      :refname: details
      :type: (object)

      .. _action.set^badge^text^color.details.color:

      .. api-member::
         :name: ``color``
         :refid: action-set-badge-text-color-details-color
         :refname: color
         :type: (string or :ref:`action.^color^array` or null)

         The color to use as text color in the badge. Cleared by setting it to :value:`null`.

      .. _action.set^badge^text^color.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-set-badge-text-color-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the text color for the badge only for the given tab.

      .. _action.set^badge^text^color.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-set-badge-text-color-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _action.set^icon:

setIcon(details)
----------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Sets the icon for the action button. Either the :value:`path` or the :value:`imageData` property must be specified.

.. api-header::
   :label: Parameters

   .. _action.set^icon.details:

   .. api-member::
      :name: ``details``
      :refid: action-set-icon-details
      :refname: details
      :type: (object)

      .. _action.set^icon.details.image^data:

      .. api-member::
         :name: [``imageData``]
         :refid: action-set-icon-details-image-data
         :refname: imageData
         :type: (:ref:`action.^image^data^type` or :ref:`action.^image^data^dictionary`, optional)

         The image data for one or more icons for the action button.

      .. _action.set^icon.details.path:

      .. api-member::
         :name: [``path``]
         :refid: action-set-icon-details-path
         :refname: path
         :type: (:ref:`action.^icon^path`, optional)

         The paths to one or more icons for the action button.

      .. _action.set^icon.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-set-icon-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the icon only for the given tab.

      .. _action.set^icon.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-set-icon-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _action.set^label:

setLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Sets the label of the action button. Can be used to set different values for the tooltip (defined by the title) and the label. Additionally, the label can be set to an empty string, not showing any label at all.

.. api-header::
   :label: Parameters

   .. _action.set^label.details:

   .. api-member::
      :name: ``details``
      :refid: action-set-label-details
      :refname: details
      :type: (object)

      .. _action.set^label.details.label:

      .. api-member::
         :name: ``label``
         :refid: action-set-label-details-label
         :refname: label
         :type: (string or null)

         A string the action button should use as its label, overriding the defined title. Can be set to an empty string to not display any label at all. If the containing toolbar is configured to display text only, its title will be used. Cleared by setting it to :value:`null`.

      .. _action.set^label.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-set-label-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the label only for the given tab.

      .. _action.set^label.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-set-label-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _action.set^popup:

setPopup(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Sets the html document to be opened as a popup when the user clicks on the action button.

.. api-header::
   :label: Parameters

   .. _action.set^popup.details:

   .. api-member::
      :name: ``details``
      :refid: action-set-popup-details
      :refname: details
      :type: (object)

      .. _action.set^popup.details.popup:

      .. api-member::
         :name: ``popup``
         :refid: action-set-popup-details-popup
         :refname: popup
         :type: (string or null)

         The html file to show in a popup. Can be set to an empty string to not open a popup. Cleared by setting it to :value:`null` (popup value defined the manifest will be used).

      .. _action.set^popup.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-set-popup-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the popup only for the given tab.

      .. _action.set^popup.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-set-popup-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _action.set^title:

setTitle(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Sets the title of the action button. Is used as tooltip and as the label.

.. api-header::
   :label: Parameters

   .. _action.set^title.details:

   .. api-member::
      :name: ``details``
      :refid: action-set-title-details
      :refname: details
      :type: (object)

      .. _action.set^title.details.title:

      .. api-member::
         :name: ``title``
         :refid: action-set-title-details-title
         :refname: title
         :type: (string or null)

         A string the action button should display as its label and when moused over. Cleared by setting it to :value:`null` or an empty string (title defined the manifest will be used).

      .. _action.set^title.details.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: action-set-title-details-tab-id
         :refname: tabId
         :type: (integer, optional)

         Sets the title only for the given tab.

      .. _action.set^title.details.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: action-set-title-details-window-id
         :refname: windowId
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. rst-class:: api-main-section

Events
======

.. _action.on^clicked:

onClicked
---------

.. api-section-annotation-hack:: -- [Added in TB 105]

Fired when an action button is clicked. This event will not fire if the action has a popup. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for onClicked.addListener(listener)

   .. _action.on^clicked.listener(tab, info):

   .. api-member::
      :name: ``listener(tab, info)``
      :refid: action-on-clicked-listener-tab-info
      :refname: listener(tab, info)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _action.on^clicked.tab:

   .. api-member::
      :name: ``tab``
      :refid: action-on-clicked-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

   .. _action.on^clicked.info:

   .. api-member::
      :name: [``info``]
      :refid: action-on-clicked-info
      :refname: info
      :type: (:ref:`action.^on^click^data`, optional)

.. rst-class:: api-main-section

Types
=====

.. _action.^color^array:

ColorArray
----------

.. api-section-annotation-hack:: -- [Added in TB 105]

An array of four integers in the range [0,255] that make up the RGBA color. For example, opaque red is :value:`[255, 0, 0, 255]`.

.. api-header::
   :label: array of integer

.. _action.^extension^file^url:

ExtensionFileUrl
----------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension, must not be empty and can be localized.

.. api-header::
   :label: string

.. _action.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _action.^icon^path:

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
   :label: :ref:`action.^extension^file^url`

.. _action.^image^data^dictionary:

ImageDataDictionary
-------------------

.. api-section-annotation-hack:: -- [Added in TB 105]

A *dictionary object* to specify multiple `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__ objects in different sizes, so the icon does not have to be scaled for a device with a different pixel density. Each entry is a *name-value* pair with *value* being an `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__ object, and *name* its size.

.. api-header::
   :label: object

.. _action.^image^data^type:

ImageDataType
-------------

.. api-section-annotation-hack:: -- [Added in TB 105]

Pixel data for an image. Must be an `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__ object (for example, from a `canvas <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas>`__ element).

.. api-header::
   :label: `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__

.. _action.^on^click^data:

OnClickData
-----------

.. api-section-annotation-hack:: -- [Added in TB 105]

Information sent when an action button is clicked.

.. api-header::
   :label: object

   .. _action.^on^click^data.modifiers:

   .. api-member::
      :name: ``modifiers``
      :refid: action-on-click-data-modifiers
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

   .. _action.^on^click^data.button:

   .. api-member::
      :name: [``button``]
      :refid: action-on-click-data-button
      :refname: button
      :type: (integer, optional)

      An integer value of button by which menu item was clicked.

.. _action.^theme^icons:

ThemeIcons
----------

.. api-section-annotation-hack:: 

Define a set of icons for themes depending on whether Thunderbird detects that the theme uses dark or light text. All provided URLs must be relative to the :value:`manifest.json` file.

.. api-header::
   :label: object

   .. _action.^theme^icons.dark:

   .. api-member::
      :name: ``dark``
      :refid: action-theme-icons-dark
      :refname: dark
      :type: (:ref:`action.^extension^u^r^l`)

      The dark icon to use for light themes

   .. _action.^theme^icons.light:

   .. api-member::
      :name: ``light``
      :refid: action-theme-icons-light
      :refname: light
      :type: (:ref:`action.^extension^u^r^l`)

      A light icon to use for dark themes

   .. _action.^theme^icons.size:

   .. api-member::
      :name: ``size``
      :refid: action-theme-icons-size
      :refname: size
      :type: (integer)

      The size of the icons
