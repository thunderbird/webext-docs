.. _messageDisplayAction_api:

====================
messageDisplayAction
====================

The messageDisplayAction API was added in Thunderbird 71, and was uplifted to Thunderbird 68.3
ESR. It is similar to Firefox's `browserAction API`__ and can be combined with the
:doc:`messageDisplay` API to determine the currently displayed message.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserAction

.. role:: permission

Use toolbar actions to put icons in the message display toolbar. In addition to its icon, a toolbar action can also have a tooltip, a badge, and a popup.

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``message_display_action``]
   :type: (object)
   
   .. api-member::
      :name: [``browser_style``]
      :type: (boolean)
   
   
   .. api-member::
      :name: [``default_area``]
      :type: (string)
      
      Currently unused.
   
   
   .. api-member::
      :name: [``default_icon``]
      :type: (string)
   
   
   .. api-member::
      :name: [``default_label``]
      :type: (string)
      :annotation: -- [Added in TB 84.0b3]
   
   
   .. api-member::
      :name: [``default_popup``]
      :type: (string)
   
   
   .. api-member::
      :name: [``default_title``]
      :type: (string)
   
   
   .. api-member::
      :name: [``theme_icons``]
      :type: (array of :ref:`messageDisplayAction.ThemeIcons`)
      
      Specifies icons to use for dark and light themes
   

.. rst-class:: api-permission-info

.. note::

   A manifest entry named ``message_display_action`` is required to use ``messageDisplayAction``.

.. rst-class:: api-main-section

Functions
=========

.. _messageDisplayAction.setTitle:

setTitle(details)
-----------------

.. api-section-annotation-hack:: 

Sets the title of the toolbar action. This shows up in the tooltip and the label. Defaults to the add-on name.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``title``
         :type: (string or null)
         
         The string the toolbar action should display as its label and when moused over.
      
   

.. _messageDisplayAction.getTitle:

getTitle(details)
-----------------

.. api-section-annotation-hack:: 

Gets the title of the toolbar action.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (:ref:`messageDisplayAction.Details`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messageDisplayAction.setLabel:

setLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 84.0b3]

Sets the label of the toolbar action, defaults to its title. Can be set to an empty string to not display any label. If the containing toolbar is configured to display text only, the title will be used as fallback.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``label``
         :type: (string or null)
         
         The string the toolbar action should use as label. Can be set to an empty string to not display any label. If the containing toolbar is configured to display text only, the title will be used as fallback.
      
   

.. _messageDisplayAction.getLabel:

getLabel(details)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 84.0b3]

Gets the label of the toolbar action.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (:ref:`messageDisplayAction.Details`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messageDisplayAction.setIcon:

setIcon(details)
----------------

.. api-section-annotation-hack:: 

Sets the icon for the toolbar action. The icon can be specified either as the path to an image file or as the pixel data from a canvas element, or as dictionary of either one of those. Either the **path** or the **imageData** property must be specified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: [``imageData``]
         :type: (:ref:`messageDisplayAction.ImageDataType` or object)
         
         Either an ImageData object or a dictionary {size -> ImageData} representing icon to be set. If the icon is specified as a dictionary, the actual image to be used is chosen depending on screen's pixel density. If the number of image pixels that fit into one screen space unit equals ``scale``, then image with size ``scale`` * 19 will be selected. Initially only scales 1 and 2 will be supported. At least one image must be specified. Note that 'details.imageData = foo' is equivalent to 'details.imageData = {'19': foo}'
      
      
      .. api-member::
         :name: [``path``]
         :type: (string or object)
         
         Either a relative image path or a dictionary {size -> relative image path} pointing to icon to be set. If the icon is specified as a dictionary, the actual image to be used is chosen depending on screen's pixel density. If the number of image pixels that fit into one screen space unit equals ``scale``, then image with size ``scale`` * 19 will be selected. Initially only scales 1 and 2 will be supported. At least one image must be specified. Note that 'details.path = foo' is equivalent to 'details.imageData = {'19': foo}'
      
   

.. _messageDisplayAction.setPopup:

setPopup(details)
-----------------

.. api-section-annotation-hack:: 

Sets the html document to be opened as a popup when the user clicks on the toolbar action's icon.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``popup``
         :type: (string or null)
         
         The html file to show in a popup.  If set to the empty string (''), no popup is shown.
      
   

.. _messageDisplayAction.getPopup:

getPopup(details)
-----------------

.. api-section-annotation-hack:: 

Gets the html document set as the popup for this toolbar action.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (:ref:`messageDisplayAction.Details`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messageDisplayAction.setBadgeText:

setBadgeText(details)
---------------------

.. api-section-annotation-hack:: 

Sets the badge text for the toolbar action. The badge is displayed on top of the icon.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (object)
      
      .. api-member::
         :name: ``text``
         :type: (string or null)
         
         Any number of characters can be passed, but only about four can fit in the space.
      
   

.. _messageDisplayAction.getBadgeText:

getBadgeText(details)
---------------------

.. api-section-annotation-hack:: 

Gets the badge text of the toolbar action. If no tab nor window is specified is specified, the global badge text is returned.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (:ref:`messageDisplayAction.Details`)
   

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
         
         An array of four integers in the range [0,255] that make up the RGBA color of the badge. For example, opaque red is ``[255, 0, 0, 255]``. Can also be a string with a CSS value, with opaque red being ``#FF0000`` or ``#F00``.
      
   

.. _messageDisplayAction.getBadgeBackgroundColor:

getBadgeBackgroundColor(details)
--------------------------------

.. api-section-annotation-hack:: 

Gets the background color of the toolbar action.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (:ref:`messageDisplayAction.Details`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`messageDisplayAction.ColorArray`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messageDisplayAction.enable:

enable([tabId])
---------------

.. api-section-annotation-hack:: 

Enables the toolbar action for a tab. By default, toolbar actions are enabled.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      The id of the tab for which you want to modify the toolbar action.
   

.. _messageDisplayAction.disable:

disable([tabId])
----------------

.. api-section-annotation-hack:: 

Disables the toolbar action for a tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      The id of the tab for which you want to modify the toolbar action.
   

.. _messageDisplayAction.isEnabled:

isEnabled(details)
------------------

.. api-section-annotation-hack:: 

Checks whether the toolbar action is enabled.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``details``
      :type: (:ref:`messageDisplayAction.Details`)
   

.. _messageDisplayAction.openPopup:

openPopup()
-----------

.. api-section-annotation-hack:: 

Opens the extension popup window in the active window.

.. rst-class:: api-main-section

Events
======

.. _messageDisplayAction.onClicked:

onClicked(tab, [info])
----------------------

.. api-section-annotation-hack:: 

Fired when a toolbar action icon is clicked.  This event will not fire if the toolbar action has a popup.

.. api-header::
   :label: Parameters for event listeners

   
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

.. api-header::
   :label: array of integer

.. _messageDisplayAction.Details:

Details
-------

.. api-section-annotation-hack:: 

Specifies to which tab or window the value should be set, or from which one it should be retrieved. If no tab nor window is specified, the global value is set or retrieved.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      When setting a value, it will be specific to the specified tab, and will automatically reset when the tab navigates. When getting, specifies the tab to get the value from; if there is no tab-specific value, the window one will be inherited.
   
   
   .. api-member::
      :name: [``windowId``]
      :type: (integer)
      
      When setting a value, it will be specific to the specified window. When getting, specifies the window to get the value from; if there is no window-specific value, the global one will be inherited.
   

.. _messageDisplayAction.ImageDataType:

ImageDataType
-------------

.. api-section-annotation-hack:: 

Pixel data for an image. Must be an ImageData object (for example, from a ``canvas`` element).

.. api-header::
   :label: `ImageData <https://developer.mozilla.org/en-US/docs/Web/API/ImageData>`_

.. _messageDisplayAction.OnClickData:

OnClickData
-----------

.. api-section-annotation-hack:: -- [Added in TB 74.0b2]

Information sent when a message display action is clicked.

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
      
      .. api-member::
         :name: ``Ctrl``
      
      .. api-member::
         :name: ``MacCtrl``
   
   
   .. api-member::
      :name: [``button``]
      :type: (integer)
      
      An integer value of button by which menu item was clicked.
   

.. rst-class:: api-main-section

External Types
==============

The following types are not defined by this API, but by the underlying Mozilla WebExtension code base. They are included here, because there is no other public documentation available.

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
      
      The size of the two icons in pixels, for example ``16`` or ``32``.
   
