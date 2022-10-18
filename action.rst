.. _action_api:

======
action
======

The action API was introduced as part of the manifest v3 specification and first appeared in Thunderbird 105.
It is identical to the old ``browserAction`` API and very similar to Firefox's `action API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/action>`__.

.. role:: permission

Use an action to put an icon in the mail window toolbar. In addition to its icon, an action can also have a tooltip, a badge, and a popup.

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``action``]
   :type: (:ref:`action.ActionManifest`)

.. rst-class:: api-permission-info

.. note::

   A manifest entry named ``action`` is required to use ``action``.

.. rst-class:: api-main-section

Functions
=========

.. _action.setTitle:

setTitle(details)
-----------------

.. api-section-annotation-hack:: 

Sets the title of the action. Is used as tooltip and as the label of the action button.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``title``
         :type: (string or null)
         
         The string the action should display as its label and when moused over. Cleared by setting it to ``null`` or an empty string (button will use the manifest value).
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the title only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _action.getTitle:

getTitle(details)
-----------------

.. api-section-annotation-hack:: 

Gets the title of the action.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Specifies for which tab the title should be retrieved. If no tab is specified, the global value is retrieved.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.setLabel:

setLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 84.0b3, backported to TB 78.6.1]

Sets the label of the action button. Can be used to set different values for the tooltip (defined by the title) and the label. Additionally, the label can be set to an empty string, not showing any label at all.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``label``
         :type: (string or null)
         
         The string the action should use as its label, overriding the defined title. Can be set to an empty string to not display any label at all. If the containing toolbar is configured to display text only, its title will be used. Cleared by setting it to ``null``.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the label only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _action.getLabel:

getLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 84.0b3, backported to TB 78.6.1]

Gets the label of the action.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Specifies for which tab the label should be retrieved. If no tab is specified, the global label is retrieved.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.setIcon:

setIcon(details)
----------------

.. api-section-annotation-hack:: 

Sets the icon for the action. Either the **path** or the **imageData** property must be specified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: [``imageData``]
         :type: (:ref:`action.ImageDataType` or :ref:`action.ImageDataDictionary`)
         
         The image data for one or more icons for the action.
      
      
      .. api-member::
         :name: [``path``]
         :type: (:ref:`action.IconPath`)
         
         The paths to one or more icons for the action.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the icon only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _action.setPopup:

setPopup(details)
-----------------

.. api-section-annotation-hack:: 

Sets the html document to be opened as a popup when the user clicks on the action's icon.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``popup``
         :type: (string or null)
         
         The html file to show in a popup. Can be set to an empty string to not open a popup. Cleared by setting it to ``null`` (button will use the manifest value).
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the popup only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _action.getPopup:

getPopup(details)
-----------------

.. api-section-annotation-hack:: 

Gets the html document set as the popup for this action.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Specifies for which tab the popup document should be retrieved. If no tab is specified, the global value is retrieved.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.setBadgeText:

setBadgeText(details)
---------------------

.. api-section-annotation-hack:: 

Sets the badge text for the action. The badge is displayed on top of the icon.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``text``
         :type: (string or null)
         
         Any number of characters can be passed, but only about four can fit in the space. Cleared by setting it to ``null`` or an empty string.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the badge text only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _action.getBadgeText:

getBadgeText(details)
---------------------

.. api-section-annotation-hack:: 

Gets the badge text of the action.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Specifies for which tab the badge text should be retrieved. If no tab is specified, the global label is retrieved.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.setBadgeBackgroundColor:

setBadgeBackgroundColor(details)
--------------------------------

.. api-section-annotation-hack:: 

Sets the background color for the badge.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``color``
         :type: (string or :ref:`action.ColorArray` or null)
         
         The color to use as background in the badge. Cleared by setting it to ``null`` or an empty string.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the background color for the badge only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _action.getBadgeBackgroundColor:

getBadgeBackgroundColor(details)
--------------------------------

.. api-section-annotation-hack:: 

Gets the badge background color of the action.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Specifies for which tab the badge background color should be retrieved. If no tab is specified, the global label is retrieved.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`action.ColorArray`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.enable:

enable([tabId])
---------------

.. api-section-annotation-hack:: 

Enables the action for a tab. By default, an action is enabled.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      The id of the tab for which you want to modify the action.
   

.. _action.disable:

disable([tabId])
----------------

.. api-section-annotation-hack:: 

Disables the action for a tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      The id of the tab for which you want to modify the action.
   

.. _action.isEnabled:

isEnabled(details)
------------------

.. api-section-annotation-hack:: 

Checks whether the action is enabled.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Specifies for which tab the state should be retrieved. If no tab is specified, the global value is retrieved.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: boolean
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _action.openPopup:

openPopup()
-----------

.. api-section-annotation-hack:: 

Opens the extension popup window in the active window.

.. rst-class:: api-main-section

Events
======

.. _action.onClicked:

onClicked
---------

.. api-section-annotation-hack:: 

Fired when an action icon is clicked. This event will not fire if the action has a popup. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for onClicked.addListener(listener)

   
   .. api-member::
      :name: ``listener(tab, info)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Added in TB 74.0b2]
   
   
   .. api-member::
      :name: [``info``]
      :type: (:ref:`action.OnClickData`)
      :annotation: -- [Added in TB 74.0b2]
   

.. rst-class:: api-main-section

Types
=====

.. _action.ActionManifest:

ActionManifest
--------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``browser_style``]
      :type: (boolean)
      
      Enable browser styles. See the `MDN documentation on browser styles <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information.
   
   
   .. api-member::
      :name: [``default_area``]
      :type: (`string`)
      
      Defines the location the action will appear. The default location is ``maintoolbar``.
      
      Supported values:
      
      .. api-member::
         :name: ``maintoolbar``
      
      .. api-member::
         :name: ``tabstoolbar``
         :annotation: -- [Added in TB 92, backported to TB 91.0.2]
   
   
   .. api-member::
      :name: [``default_icon``]
      :type: (:ref:`action.IconPath`)
      
      The paths to one or more icons for the action.
   
   
   .. api-member::
      :name: [``default_label``]
      :type: (string)
      :annotation: -- [Added in TB 84.0b3, backported to TB 78.6.1]
      
      The label of the action, defaults to its title. Can be set to an empty string to not display any label. If the containing toolbar is configured to display text only, the title will be used as fallback.
   
   
   .. api-member::
      :name: [``default_popup``]
      :type: (string)
      
      The html document to be opened as a popup when the user clicks on the action's icon.
   
   
   .. api-member::
      :name: [``default_title``]
      :type: (string)
      
      The title of the action. This shows up in the tooltip and the label. Defaults to the add-on name.
   
   
   .. api-member::
      :name: [``default_windows``]
      :type: (array of `string`)
      
      Defines the windows, the action should appear in. Defaults to showing it only in the ``normal`` Thunderbird window, but can also be shown in the ``messageDisplay`` window.
      
      Supported values:
      
      .. api-member::
         :name: ``normal``
      
      .. api-member::
         :name: ``messageDisplay``
   
   
   .. api-member::
      :name: [``theme_icons``]
      :type: (array of :ref:`action.ThemeIcons`)
      
      Specifies dark and light icons to be used with themes. The ``light`` icon is used on dark backgrounds and vice versa. **Note:** The default theme uses the ``default_icon`` for light backgrounds (if specified).
   

.. _action.ColorArray:

ColorArray
----------

.. api-section-annotation-hack:: 

An array of four integers in the range [0,255] that make up the RGBA color. For example, opaque red is ``[255, 0, 0, 255]``.

.. api-header::
   :label: array of integer

.. _action.ImageDataDictionary:

ImageDataDictionary
-------------------

.. api-section-annotation-hack:: 

A ``{size: ImageDataType}`` dictionary representing the icon to be set. The actual :ref:`action.ImageDataType` to be used is chosen depending on the screen's pixel density. See the `MDN documentation on browser styles <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information on this. At least one :ref:`action.ImageDataType` must be specified.

.. api-header::
   :label: object

.. _action.ImageDataType:

ImageDataType
-------------

.. api-section-annotation-hack:: 

Pixel data for an image. Must be an ImageData object (for example, from a ``canvas`` element).

.. api-header::
   :label: `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`_

.. _action.OnClickData:

OnClickData
-----------

.. api-section-annotation-hack:: -- [Added in TB 74.0b2]

Information sent when an action is clicked.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``modifiers``
      :type: (array of `string`)
      
      An array of keyboard modifiers that were held while the menu item was clicked.
      
      Supported values:
      
      .. api-member::
         :name: ``Shift``
      
      .. api-member::
         :name: ``Alt``
      
      .. api-member::
         :name: ``Command``
      
         Only available on macOS.
      
      .. api-member::
         :name: ``Ctrl``
      
         Not available on macOS.
      
      .. api-member::
         :name: ``MacCtrl``
      
         Only available on macOS, but of limited use in a click event: Holding down the CTRL key while clicking with the mouse is referred to as a 'CTRL click' under macOS and is interpreted as a right mouse click. In a default profile  the ``dom.event.treat_ctrl_click_as_right_click.disabled`` preference is not enabled and the ``MacCtrl`` modifier key is not forwarded to the API.
   
   
   .. api-member::
      :name: [``button``]
      :type: (integer)
      
      An integer value of button by which menu item was clicked.
   

.. rst-class:: api-main-section

External Types
==============

The following types are not defined by this API, but by the underlying Mozilla WebExtension code base. They are included here, because there is no other public documentation available.

.. _action.IconPath:

IconPath
--------

.. api-section-annotation-hack:: 

Either a simple ``string``, setting the path of an icon to be used for all sizes, or an ``object`` defining icons for different sizes. Example: 

.. literalinclude:: includes/IconPath.json
  :language: JSON

At least the ``16px`` icon should be specified. The ``32px`` icon will be used on screens with a very high pixel density, if specified. See the  `MDN documentation about choosing icon sizes <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action#choosing_icon_sizes>`__ for more information on this. All paths are relative to the root of the extension.

.. _action.ThemeIcons:

ThemeIcons
----------

.. api-section-annotation-hack:: 

Define a set of icons for themes depending on whether Thunderbird detects that the theme uses dark or light text. All provided URLs must be relative to the manifest.json file.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``dark``
      :type: (string)
      
      A URL pointing to an icon. This icon displays when a theme using dark text is active (such as the Light theme, and the Default theme if no ``default_icon`` is specified).
   
   
   .. api-member::
      :name: ``light``
      :type: (string)
      
      A URL pointing to an icon. This icon displays when a theme using light text is active (such as the Dark theme).
   
   
   .. api-member::
      :name: ``size``
      :type: (integer)
      
      The size of the two icons in pixels, for example ``16`` or ``32``.
   
