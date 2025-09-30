.. container:: sticky-sidebar

  ≡ composeAction API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=================
composeAction API
=================

.. role:: permission

.. role:: value

.. role:: code

Use a composeAction to put a button in the message composition toolbars. In addition to its icon, a composeAction button can also have a tooltip, a badge, and a popup.

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``compose_action``]
   :type: (object, optional)
   :annotation: -- [Added in TB 64]

   .. api-member::
      :name: [``browser_style``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 64]

      Enable browser styles. See the `MDN documentation on browser styles <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information.

   .. api-member::
      :name: [``default_area``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 64]

      Defines the location the composeAction button will appear. The default location is :value:`maintoolbar`.

      Supported values:

      .. api-member::
         :name: :value:`formattoolbar`

      .. api-member::
         :name: :value:`maintoolbar`

   .. api-member::
      :name: [``default_icon``]
      :type: (:ref:`compose^action.^icon^path`, optional)
      :annotation: -- [Added in TB 64]

      The paths to one or more icons for the composeAction button.

   .. api-member::
      :name: [``default_label``]
      :type: (string, optional)
      :annotation: -- [Added in TB 85]

      The label of the composeAction button, defaults to its title. Can be set to an empty string to not display any label. If the containing toolbar is configured to display text only, the title will be used as fallback.

   .. api-member::
      :name: [``default_popup``]
      :type: (string, optional)
      :annotation: -- [Added in TB 64]

      The html document to be opened as a popup when the user clicks on the composeAction button. Ignored for action buttons with type :value:`menu`.

   .. api-member::
      :name: [``default_title``]
      :type: (string, optional)
      :annotation: -- [Added in TB 64]

      The title of the composeAction button. This shows up in the tooltip and the label. Defaults to the add-on name.

   .. api-member::
      :name: [``theme_icons``]
      :type: (array of :ref:`compose^action.^theme^icons`, optional)
      :annotation: -- [Added in TB 64]

      Specifies dark and light icons to be used with themes. The :value:`light` icon is used on dark backgrounds and vice versa. The default theme uses the :value:`default_icon` for light backgrounds (if specified).

   .. api-member::
      :name: [``type``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 90]

      Specifies the type of the button. Default type is :value:`button`.

      Supported values:

      .. api-member::
         :name: :value:`button`

      .. api-member::
         :name: :value:`menu`

.. rst-class:: api-main-section

Permissions
===========

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`compose_action` is required to use ``messenger.composeAction.*``.

.. rst-class:: api-main-section

Functions
=========

.. _compose^action.disable:

disable([tabId])
----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Disables the composeAction button for a specific tab (if a :value:`tabId` is provided), or for all tabs which do not have a custom enable state. Once the enable state of a tab has been updated individually, all further changes to its state have to be done individually as well.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)

      The id of the tab for which you want to modify the composeAction button.

.. _compose^action.enable:

enable([tabId])
---------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Enables the composeAction button for a specific tab (if a :value:`tabId` is provided), or for all tabs which do not have a custom enable state. Once the enable state of a tab has been updated individually, all further changes to its state have to be done individually as well. By default, a composeAction button is enabled.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)

      The id of the tab for which you want to modify the composeAction button.

.. _compose^action.get^badge^background^color:

getBadgeBackgroundColor(details)
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Gets the badge background color of the composeAction button.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the badge background color should be retrieved. If no tab is specified, the global value is retrieved.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`compose^action.^color^array`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose^action.get^badge^text:

getBadgeText(details)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Gets the badge text of the composeAction button.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the badge text should be retrieved. If no tab is specified, the global value is retrieved.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose^action.get^badge^text^color:

getBadgeTextColor(details)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Gets the text color of the badge.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)

         Specifies for which tab the badge text color should be retrieved. If no tab is specified, the global value is retrieved.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`compose^action.^color^array`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose^action.get^label:

getLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 85]

Gets the label of the composeAction button. Returns :value:`null`, if no label has been set and the title is used.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the label should be retrieved. If no tab is specified, the global value is retrieved.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string or null

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose^action.get^popup:

getPopup(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Gets the html document set as the popup for this composeAction button.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the popup document should be retrieved. If no tab is specified, the global value is retrieved.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose^action.get^title:

getTitle(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Gets the title of the composeAction button.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the title should be retrieved. If no tab is specified, the global value is retrieved.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose^action.is^enabled:

isEnabled(details)
------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Checks whether the composeAction button is enabled.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)
         :annotation: -- [Added in TB 108]

         Specifies for which tab the state should be retrieved. If no tab is specified, the global value is retrieved.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**
         :annotation: -- [Added in TB 108]

         Will throw an error if used.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: boolean
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose^action.open^popup:

openPopup([options])
--------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Opens the action's popup window in the specified window. Defaults to the current window. Returns false if the popup could not be opened because the action has no popup, is of type :value:`menu`, is disabled or has been removed from the toolbar.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``options``]
      :type: (object, optional)
      :annotation: -- [Added in TB 113]

      An object with information about the popup to open.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional)
         :annotation: -- [Added in TB 113]

         Defaults to the current window.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: boolean
      :annotation: -- [Added in TB 113]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _compose^action.set^badge^background^color:

setBadgeBackgroundColor(details)
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Sets the background color for the badge.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``color``
         :type: (string or :ref:`compose^action.^color^array` or null)

         The color to use as background in the badge. Cleared by setting it to :value:`null`.

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)

         Sets the background color for the badge only for the given tab.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _compose^action.set^badge^text:

setBadgeText(details)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Sets the badge text for the composeAction button. The badge is displayed on top of the icon.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``text``
         :type: (string or null)

         Any number of characters can be passed, but only about four can fit in the space. Cleared by setting it to :value:`null` or an empty string.

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)

         Sets the badge text only for the given tab.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _compose^action.set^badge^text^color:

setBadgeTextColor(details)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Sets the text color for the badge.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``color``
         :type: (string or :ref:`compose^action.^color^array` or null)

         The color to use as text color in the badge. Cleared by setting it to :value:`null`.

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)

         Sets the text color for the badge only for the given tab.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _compose^action.set^icon:

setIcon(details)
----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Sets the icon for the composeAction button. Either the :value:`path` or the :value:`imageData` property must be specified.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: [``imageData``]
         :type: (:ref:`compose^action.^image^data^type` or :ref:`compose^action.^image^data^dictionary`, optional)

         The image data for one or more icons for the composeAction button.

      .. api-member::
         :name: [``path``]
         :type: (:ref:`compose^action.^icon^path`, optional)

         The paths to one or more icons for the composeAction button.

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)

         Sets the icon only for the given tab.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _compose^action.set^label:

setLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 85]

Sets the label of the composeAction button. Can be used to set different values for the tooltip (defined by the title) and the label. Additionally, the label can be set to an empty string, not showing any label at all.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``label``
         :type: (string or null)

         A string the composeAction button should use as its label, overriding the defined title. Can be set to an empty string to not display any label at all. If the containing toolbar is configured to display text only, its title will be used. Cleared by setting it to :value:`null`.

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)

         Sets the label only for the given tab.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _compose^action.set^popup:

setPopup(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Sets the html document to be opened as a popup when the user clicks on the composeAction button.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``popup``
         :type: (string or null)

         The html file to show in a popup. Can be set to an empty string to not open a popup. Cleared by setting it to :value:`null` (action will use the popup value defined in the manifest).

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)

         Sets the popup only for the given tab.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. _compose^action.set^title:

setTitle(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Sets the title of the composeAction button. Is used as tooltip and as the label.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``title``
         :type: (string or null)

         A string the composeAction button should display as its label and when moused over. Cleared by setting it to :value:`null` or an empty string (title defined the manifest will be used).

      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)

         Sets the title only for the given tab.

      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional) **Unsupported.**

         Will throw an error if used.

.. rst-class:: api-main-section

Events
======

.. _compose^action.on^clicked:

onClicked
---------

.. api-section-annotation-hack:: -- [Added in TB 64]

Fired when a composeAction button is clicked. This event will not fire if the composeAction has a popup. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for onClicked.addListener(listener)

   .. api-member::
      :name: ``listener(tab, info)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.^tab`)
      :annotation: -- [Added in TB 74]

   .. api-member::
      :name: [``info``]
      :type: (:ref:`compose^action.^on^click^data`, optional)
      :annotation: -- [Added in TB 74]

.. rst-class:: api-main-section

Types
=====

.. _compose^action.^color^array:

ColorArray
----------

.. api-section-annotation-hack:: -- [Added in TB 64]

An array of four integers in the range [0,255] that make up the RGBA color. For example, opaque red is :value:`[255, 0, 0, 255]`.

.. api-header::
   :label: array of integer

.. _compose^action.^extension^file^url:

ExtensionFileUrl
----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string

.. _compose^action.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _compose^action.^icon^path:

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
   :label: :ref:`compose^action.^extension^file^url`

.. _compose^action.^image^data^dictionary:

ImageDataDictionary
-------------------

.. api-section-annotation-hack:: -- [Added in TB 90]

A *dictionary object* to specify multiple `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__ objects in different sizes, so the icon does not have to be scaled for a device with a different pixel density. Each entry is a *name-value* pair with *value* being an `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__ object, and *name* its size.

.. api-header::
   :label: object

.. _compose^action.^image^data^type:

ImageDataType
-------------

.. api-section-annotation-hack:: -- [Added in TB 64]

Pixel data for an image. Must be an `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__ object (for example, from a `canvas <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas>`__ element).

.. api-header::
   :label: `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`__

.. _compose^action.^on^click^data:

OnClickData
-----------

.. api-section-annotation-hack:: -- [Added in TB 74]

Information sent when a composeAction button is clicked.

.. api-header::
   :label: object

   .. _compose^action.^on^click^data.modifiers:

   .. api-member::
      :name: ``modifiers``
      :type: (array of `string`)

      An array of keyboard modifiers that were held while the menu item was clicked.

      Supported values:

      .. api-member::
         :name: :value:`Alt`

      .. api-member::
         :name: :value:`Command`

         Only available on macOS.

      .. api-member::
         :name: :value:`Ctrl`

         Not available on macOS.

      .. api-member::
         :name: :value:`MacCtrl`

         Only available on macOS, but of limited use in a click event: Holding down the CTRL key while clicking with the mouse is referred to as a 'CTRL click' under macOS and is interpreted as a right mouse click. In a default profile  the :value:`dom.event.treat_ctrl_click_as_right_click.disabled` preference is not enabled and the :value:`MacCtrl` modifier key is not forwarded to the API.

      .. api-member::
         :name: :value:`Shift`

   .. _compose^action.^on^click^data.button:

   .. api-member::
      :name: [``button``]
      :type: (integer, optional)

      An integer value of button by which menu item was clicked.

.. _compose^action.^theme^icons:

ThemeIcons
----------

.. api-section-annotation-hack:: 

Define a set of icons for themes depending on whether Thunderbird detects that the theme uses dark or light text. All provided URLs must be relative to the :value:`manifest.json` file.

.. api-header::
   :label: object

   .. _compose^action.^theme^icons.dark:

   .. api-member::
      :name: ``dark``
      :type: (:ref:`compose^action.^extension^u^r^l`)

      The dark icon to use for light themes

   .. _compose^action.^theme^icons.light:

   .. api-member::
      :name: ``light``
      :type: (:ref:`compose^action.^extension^u^r^l`)

      A light icon to use for dark themes

   .. _compose^action.^theme^icons.size:

   .. api-member::
      :name: ``size``
      :type: (integer)

      The size of the icons
