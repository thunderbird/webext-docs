.. _browserAction_api:

=============
browserAction
=============

The browserAction API first appeared in Thunderbird 64. It is very similar to Firefox's `browserAction API`__.

Many of our `sample extensions`__ use a browserAction.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction
__ https://github.com/thundernest/sample-extensions

.. important::

  This API will be replaced in Manifest v3 by the `action API <https://webextension-api.thunderbird.net/en/latest-mv3/action.html>`__.

.. role:: permission

.. role:: value

Use a browserAction to put a button in the mail window toolbar. In addition to its icon, a browserAction button can also have a tooltip, a badge, and a popup. This namespace is called browserAction for compatibility with browser WebExtensions.

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``browser_action``]
   :type: (object)
   
   .. api-member::
      :name: [``browser_style``]
      :type: (boolean)
      
      Enable browser styles. See the `MDN documentation on browser styles <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information.
   
   
   .. api-member::
      :name: [``default_area``]
      :type: (`string`)
      
      Defines the location the browserAction button will appear. The default location is ``maintoolbar``.
      
      Supported values:
      
      .. api-member::
         :name: ``maintoolbar``
      
      .. api-member::
         :name: ``tabstoolbar``
         :annotation: -- [Added in TB 92, backported to TB 91.0.2]
   
   
   .. api-member::
      :name: [``default_icon``]
      :type: (string or :ref:`browserAction.IconPathDictionary`)
      
      The icon for the browserAction button.
   
   
   .. api-member::
      :name: [``default_label``]
      :type: (string)
      :annotation: -- [Added in TB 84.0b3, backported to TB 78.6.1]
      
      The label of the browserAction button, defaults to its title. Can be set to an empty string to not display any label. If the containing toolbar is configured to display text only, the title will be used as fallback.
   
   
   .. api-member::
      :name: [``default_popup``]
      :type: (string)
      
      The html document to be opened as a popup when the user clicks on the browserAction button.
   
   
   .. api-member::
      :name: [``default_title``]
      :type: (string)
      
      The title of the browserAction button. This shows up in the tooltip and the label. Defaults to the add-on name.
   
   
   .. api-member::
      :name: [``default_windows``]
      :type: (array of `string`)
      :annotation: -- [Added in TB 106, backported to TB 102.3.3]
      
      Defines the windows, the browserAction should appear in. Defaults to showing it only in the ``normal`` Thunderbird window, but can also be shown in the ``messageDisplay`` window.
      
      Supported values:
      
      .. api-member::
         :name: ``normal``
      
      .. api-member::
         :name: ``messageDisplay``
   
   
   .. api-member::
      :name: [``theme_icons``]
      :type: (array of :ref:`browserAction.ThemeIcons`)
      
      Specifies dark and light icons to be used with themes. The ``light`` icon is used on dark backgrounds and vice versa. **Note:** The default theme uses the ``default_icon`` for light backgrounds (if specified).
   

.. rst-class:: api-permission-info

.. note::

   A manifest entry named ``browser_action`` is required to use ``browserAction``.

.. rst-class:: api-main-section

Functions
=========

.. _browserAction.setTitle:

setTitle(details)
-----------------

.. api-section-annotation-hack:: 

Sets the title of the browserAction button. Is used as tooltip and as the label of the browserAction button.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``title``
         :type: (string or null)
         
         The string the browserAction button should display as its label and when moused over. Cleared by setting it to :value:`null` or an empty string (title defined the manifest will be used).
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the title only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _browserAction.getTitle:

getTitle(details)
-----------------

.. api-section-annotation-hack:: 

Gets the title of the browserAction button.

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

.. _browserAction.setLabel:

setLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 84.0b3, backported to TB 78.6.1]

Sets the label of the browserAction button. Can be used to set different values for the tooltip (defined by the title) and the label. Additionally, the label can be set to an empty string, not showing any label at all.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``label``
         :type: (string or null)
         
         The string the browserAction button should use as its label, overriding the defined title. Can be set to an empty string to not display any label at all. If the containing toolbar is configured to display text only, its title will be used. Cleared by setting it to :value:`null`.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the label only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _browserAction.getLabel:

getLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 84.0b3, backported to TB 78.6.1]

Gets the label of the browserAction button.

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

.. _browserAction.setIcon:

setIcon(details)
----------------

.. api-section-annotation-hack:: 

Sets the icon for the browserAction button. Either the ``path`` or the ``imageData`` property must be specified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: [``imageData``]
         :type: (:ref:`browserAction.ImageDataType` or :ref:`browserAction.ImageDataDictionary`)
         
         Either an ImageDataType object defining a single icon used for all sizes or an ImageDataDictionary object defining dedicated icons for different sizes.
      
      
      .. api-member::
         :name: [``path``]
         :type: (string or :ref:`browserAction.IconPathDictionary`)
         
         Either a relative image path defining a single icon used for all sizes or an IconPathDictionary object defining dedicated icons for different sizes.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the icon only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _browserAction.setPopup:

setPopup(details)
-----------------

.. api-section-annotation-hack:: 

Sets the html document to be opened as a popup when the user clicks on the browserAction button.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``popup``
         :type: (string or null)
         
         The html file to show in a popup. Can be set to an empty string to not open a popup. Cleared by setting it to :value:`null` (popup value defined the manifest will be used).
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the popup only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _browserAction.getPopup:

getPopup(details)
-----------------

.. api-section-annotation-hack:: 

Gets the html document set as the popup for this browserAction button.

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

.. _browserAction.setBadgeText:

setBadgeText(details)
---------------------

.. api-section-annotation-hack:: 

Sets the badge text for the browserAction button. The badge is displayed on top of the icon.

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
      
   

.. _browserAction.getBadgeText:

getBadgeText(details)
---------------------

.. api-section-annotation-hack:: 

Gets the badge text of the browserAction button.

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

.. _browserAction.setBadgeBackgroundColor:

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
         :type: (string or :ref:`browserAction.ColorArray` or null)
         
         The color to use as background in the badge. Cleared by setting it to :value:`null` or an empty string.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         
         Sets the background color for the badge only for the given tab.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer) **Unsupported.**
         
         Will throw an error if used.
      
   

.. _browserAction.getBadgeBackgroundColor:

getBadgeBackgroundColor(details)
--------------------------------

.. api-section-annotation-hack:: 

Gets the badge background color of the browserAction button.

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
      :type: :ref:`browserAction.ColorArray`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _browserAction.enable:

enable([tabId])
---------------

.. api-section-annotation-hack:: 

Enables the browserAction button for a tab. By default, an browserAction button is enabled.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      The id of the tab for which you want to modify the browserAction button.
   

.. _browserAction.disable:

disable([tabId])
----------------

.. api-section-annotation-hack:: 

Disables the browserAction button for a tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      The id of the tab for which you want to modify the browserAction button.
   

.. _browserAction.isEnabled:

isEnabled(details)
------------------

.. api-section-annotation-hack:: 

Checks whether the browserAction button is enabled.

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

.. _browserAction.openPopup:

openPopup()
-----------

.. api-section-annotation-hack:: 

Opens the browserAction's popup window in the active window.

.. rst-class:: api-main-section

Events
======

.. _browserAction.onClicked:

onClicked
---------

.. api-section-annotation-hack:: 

Fired when an browserAction button is clicked. This event will not fire if the browserAction has a popup. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

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
      :type: (:ref:`browserAction.OnClickData`)
      :annotation: -- [Added in TB 74.0b2]
   

.. rst-class:: api-main-section

Types
=====

.. _browserAction.ColorArray:

ColorArray
----------

.. api-section-annotation-hack:: 

An array of four integers in the range [0,255] that make up the RGBA color. For example, opaque red is :value:`[255, 0, 0, 255]`.

.. api-header::
   :label: array of integer

.. _browserAction.ImageDataDictionary:

ImageDataDictionary
-------------------

.. api-section-annotation-hack:: 

A ``{size: ImageDataType}`` dictionary representing the icon to be set. The actual :ref:`browserAction.ImageDataType` to be used is chosen depending on the screen's pixel density. See the `MDN documentation on browser styles <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/user_interface/Browser_styles>`__ for more information on this. At least one :ref:`browserAction.ImageDataType` must be specified.

.. api-header::
   :label: object

.. _browserAction.ImageDataType:

ImageDataType
-------------

.. api-section-annotation-hack:: 

Pixel data for an image. Must be an ImageData object (for example, from a ``canvas`` element).

.. api-header::
   :label: `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`_

.. _browserAction.OnClickData:

OnClickData
-----------

.. api-section-annotation-hack:: -- [Added in TB 74.0b2]

Information sent when a browserAction button is clicked.

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

.. _browserAction.IconPathDictionary:

IconPathDictionary
------------------

.. api-section-annotation-hack:: 

A ``{size: path}`` dictionary representing the icon to be set. The actual image to be used is chosen depending on the screen's pixel density. See the  `MDN documentation about choosing icon sizes <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action#choosing_icon_sizes>`__ for more information on this. At least one icon must be specified. Example: 

.. literalinclude:: includes/IconPath.json
  :language: JSON

.. _browserAction.ThemeIcons:

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
   
