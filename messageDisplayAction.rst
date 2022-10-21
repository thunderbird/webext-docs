.. _messageDisplayAction_api:

====================
messageDisplayAction
====================

The messageDisplayAction API was added in Thunderbird 68. It is similar to Firefox's
`browserAction API`__ and can be combined with the :doc:`messageDisplay` API to determine
the currently displayed message.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction

.. role:: permission

.. role:: value

.. role:: code

Use a messageDisplayAction to put a button in the message display toolbar. In addition to its icon, a messageDisplayAction button can also have a tooltip, a badge, and a popup.

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``message_display_action``]
   :type: (object)
   
   .. api-member::
      :name: [``browser_style``]
      :type: (boolean)
      
      Enable browser styles. See the `MDN documentation on browser styles <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information.
   
   
   .. api-member::
      :name: [``default_area``]
      :type: (string)
      
      Currently unused.
   
   
   .. api-member::
      :name: [``default_icon``]
      :type: (:ref:`messageDisplayAction.IconPath`)
      
      The paths to one or more icons for the messageDisplayAction button.
   
   
   .. api-member::
      :name: [``default_label``]
      :type: (string)
      :annotation: -- [Added in TB 84.0b3, backported to TB 78.6.1]
      
      The label of the messageDisplayAction button, defaults to its title. Can be set to an empty string to not display any label. If the containing toolbar is configured to display text only, the title will be used as fallback.
   
   
   .. api-member::
      :name: [``default_popup``]
      :type: (string)
      
      The html document to be opened as a popup when the user clicks on the messageDisplayAction button.
   
   
   .. api-member::
      :name: [``default_title``]
      :type: (string)
      
      The title of the messageDisplayAction button. This shows up in the tooltip and the label. Defaults to the add-on name.
   
   
   .. api-member::
      :name: [``theme_icons``]
      :type: (array of :ref:`messageDisplayAction.ThemeIcons`)
      
      Specifies dark and light icons to be used with themes. The ``light`` icon is used on dark backgrounds and vice versa. **Note:** The default theme uses the ``default_icon`` for light backgrounds (if specified).
   

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`message_display_action` is required to use ``messenger.messageDisplayAction.*``.

.. rst-class:: api-main-section

Functions
=========

.. _messageDisplayAction.setTitle:

setTitle(details)
-----------------

.. api-section-annotation-hack:: 

Sets the title of the messageDisplayAction button. Is used as tooltip and as the label.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``title``
         :type: (string or null)
         
         The string the messageDisplayAction button should display as its label and when moused over. Cleared by setting it to :value:`null` or an empty string (title defined the manifest will be used).
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the title only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _messageDisplayAction.getTitle:

getTitle(details)
-----------------

.. api-section-annotation-hack:: 

Gets the title of the messageDisplayAction button.

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

.. _messageDisplayAction.setLabel:

setLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 84.0b3, backported to TB 78.6.1]

Sets the label of the messageDisplayAction button. Can be used to set different values for the tooltip (defined by the title) and the label. Additionally, the label can be set to an empty string, not showing any label at all.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``label``
         :type: (string or null)
         
         The string the messageDisplayAction button should use as its label, overriding the defined title. Can be set to an empty string to not display any label at all. If the containing toolbar is configured to display text only, its title will be used. Cleared by setting it to :value:`null`.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the label only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _messageDisplayAction.getLabel:

getLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 84.0b3, backported to TB 78.6.1]

Gets the label of the messageDisplayAction button.

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

.. _messageDisplayAction.setIcon:

setIcon(details)
----------------

.. api-section-annotation-hack:: 

Sets the icon for the messageDisplayAction button. Either the ``path`` or the ``imageData`` property must be specified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: [``imageData``]
         :type: (:ref:`messageDisplayAction.ImageDataType` or :ref:`messageDisplayAction.ImageDataDictionary`)
         
         The image data for one or more icons for the composeAction button.
      
      
      .. api-member::
         :name: [``path``]
         :type: (:ref:`messageDisplayAction.IconPath`)
         
         The paths to one or more icons for the messageDisplayAction button.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the icon only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _messageDisplayAction.setPopup:

setPopup(details)
-----------------

.. api-section-annotation-hack:: 

Sets the html document to be opened as a popup when the user clicks on the messageDisplayAction button.

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
         :type: (integer)
         
         Sets the popup only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _messageDisplayAction.getPopup:

getPopup(details)
-----------------

.. api-section-annotation-hack:: 

Gets the html document set as the popup for this messageDisplayAction button.

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

.. _messageDisplayAction.setBadgeText:

setBadgeText(details)
---------------------

.. api-section-annotation-hack:: 

Sets the badge text for the messageDisplayAction button. The badge is displayed on top of the icon.

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
         :type: (integer)
         
         Sets the badge text only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _messageDisplayAction.getBadgeText:

getBadgeText(details)
---------------------

.. api-section-annotation-hack:: 

Gets the badge text of the messageDisplayAction button.

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

.. _messageDisplayAction.setBadgeBackgroundColor:

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
         :type: (string or :ref:`messageDisplayAction.ColorArray` or null)
         
         The color to use as background in the badge. Cleared by setting it to :value:`null` or an empty string.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the background color for the badge only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _messageDisplayAction.getBadgeBackgroundColor:

getBadgeBackgroundColor(details)
--------------------------------

.. api-section-annotation-hack:: 

Gets the badge background color of the messageDisplayAction button.

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
      :type: :ref:`messageDisplayAction.ColorArray`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messageDisplayAction.enable:

enable([tabId])
---------------

.. api-section-annotation-hack:: 

Enables the messageDisplayAction button for a tab. By default, a messageDisplayAction button is enabled.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      The id of the tab for which you want to modify the messageDisplayAction button.
   

.. _messageDisplayAction.disable:

disable([tabId])
----------------

.. api-section-annotation-hack:: 

Disables the messageDisplayAction button for a tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      The id of the tab for which you want to modify the messageDisplayAction button.
   

.. _messageDisplayAction.isEnabled:

isEnabled(details)
------------------

.. api-section-annotation-hack:: 

Checks whether the messageDisplayAction button is enabled.

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

.. _messageDisplayAction.openPopup:

openPopup()
-----------

.. api-section-annotation-hack:: 

Opens the action's popup window in the active window.

.. rst-class:: api-main-section

Events
======

.. _messageDisplayAction.onClicked:

onClicked
---------

.. api-section-annotation-hack:: 

Fired when a messageDisplayAction button is clicked. This event will not fire if the messageDisplayAction has a popup. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

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
      :type: (:ref:`messageDisplayAction.OnClickData`)
      :annotation: -- [Added in TB 74.0b2]
   

.. rst-class:: api-main-section

Types
=====

.. _messageDisplayAction.ColorArray:

ColorArray
----------

.. api-section-annotation-hack:: 

An array of four integers in the range [0,255] that make up the RGBA color. For example, opaque red is :value:`[255, 0, 0, 255]`.

.. api-header::
   :label: array of integer

.. _messageDisplayAction.ImageDataDictionary:

ImageDataDictionary
-------------------

.. api-section-annotation-hack:: 

A :code:`{size: ImageDataType}` dictionary representing the icon to be set. The actual :ref:`messageDisplayAction.ImageDataType` to be used is chosen depending on the screen's pixel density. See the `MDN documentation on browser styles <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information on this. At least one :ref:`messageDisplayAction.ImageDataType` must be specified.

.. api-header::
   :label: object

.. _messageDisplayAction.ImageDataType:

ImageDataType
-------------

.. api-section-annotation-hack:: 

Pixel data for an image. Must be an ImageData object (for example, from a `canvas <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas>`__ element).

.. api-header::
   :label: `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`_

.. _messageDisplayAction.OnClickData:

OnClickData
-----------

.. api-section-annotation-hack:: -- [Added in TB 74.0b2]

Information sent when a messageDisplayAction button is clicked.

.. api-header::
   :label: object

   
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
      
         Only available on macOS.
      
      .. api-member::
         :name: :value:`Ctrl`
      
         Not available on macOS.
      
      .. api-member::
         :name: :value:`MacCtrl`
      
         Only available on macOS, but of limited use in a click event: Holding down the CTRL key while clicking with the mouse is referred to as a 'CTRL click' under macOS and is interpreted as a right mouse click. In a default profile  the <value>dom.event.treat_ctrl_click_as_right_click.disabled</value> preference is not enabled and the <value>MacCtrl</value> modifier key is not forwarded to the API.
   
   
   .. api-member::
      :name: [``button``]
      :type: (integer)
      
      An integer value of button by which menu item was clicked.
   

.. rst-class:: api-main-section

External Types
==============

The following types are not defined by this API, but by the underlying Mozilla WebExtension code base. They are included here, because there is no other public documentation available.

.. _messageDisplayAction.IconPath:

IconPath
--------

.. api-section-annotation-hack:: 

Either a simple *string*, setting the path of an icon to be used for all sizes, or an *object* defining icons for different sizes. Example: 

.. literalinclude:: includes/IconPath.json
  :language: JSON

At least the *16px* icon should be specified. The *32px* icon will be used on screens with a very high pixel density, if specified. See the  `MDN documentation about choosing icon sizes <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action#choosing_icon_sizes>`__ for more information on this. All paths are relative to the root of the extension.

.. _messageDisplayAction.ThemeIcons:

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
      
      The size of the two icons in pixels, for example :value:`16` or :value:`32`.
   
