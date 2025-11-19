.. container:: sticky-sidebar

  ≡ spacesToolbar API

  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=================
spacesToolbar API
=================

.. role:: permission

.. role:: value

.. role:: code

The spacesToolbar API allows to manage built-in and custom spaces, and to add buttons for custom spaces to Thunderbird's spaces toolbar.

.. rst-class:: api-main-section

Functions
=========

.. _spaces^toolbar.add^button:

addButton(id, properties)
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 100]

Adds a new button to the spaces toolbar. Throws an exception, if the used :value:`id` is not unique within the extension.

.. api-header::
   :label: Parameters

   .. _spaces^toolbar.add^button.id:

   .. api-member::
      :name: ``id``
      :refid: spaces-toolbar-add-button-id
      :refname: id
      :type: (string)

      The unique id to assign to this button. May only contain alphanumeric characters and underscores.

   .. _spaces^toolbar.add^button.properties:

   .. api-member::
      :name: ``properties``
      :refid: spaces-toolbar-add-button-properties
      :refname: properties
      :type: (:ref:`spaces^toolbar.^button^properties`)

      Properties of the new button. The :value:`url` is mandatory.

.. api-header::
   :label: Return type (`Promise`_)

   .. _spaces^toolbar.add^button.returns:

   .. api-member::
      :refid: spaces-toolbar-add-button-returns
      :refname: _returns
      :type: integer
      :annotation: -- [Added in TB 115]

      The id of the space belonging to the newly created button, as used by the tabs API.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _spaces^toolbar.click^button:

clickButton(id, [windowId])
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 114]

Trigger a click on the specified spaces toolbar button. Throws an exception if the requested spaces toolbar button does not exist or was not created by this extension.

.. api-header::
   :label: Parameters

   .. _spaces^toolbar.click^button.id:

   .. api-member::
      :name: ``id``
      :refid: spaces-toolbar-click-button-id
      :refname: id
      :type: (string)

      The id of the spaces toolbar button. May only contain alphanumeric characters and underscores.

   .. _spaces^toolbar.click^button.window^id:

   .. api-member::
      :name: [``windowId``]
      :refid: spaces-toolbar-click-button-window-id
      :refname: windowId
      :type: (integer, optional)

      The id of the normal window, where the spaces toolbar button should be clicked. Defaults to the most recent normal window.

.. api-header::
   :label: Return type (`Promise`_)

   .. _spaces^toolbar.click^button.returns:

   .. api-member::
      :refid: spaces-toolbar-click-button-returns
      :refname: _returns
      :type: :ref:`tabs.^tab`

      Details about the opened or activated tab.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _spaces^toolbar.remove^button:

removeButton(id)
----------------

.. api-section-annotation-hack:: -- [Added in TB 100]

Removes the specified button from the spaces toolbar. Throws an exception if the requested spaces toolbar button does not exist or was not created by this extension. If the tab of this button is currently open, it will be closed.

.. api-header::
   :label: Parameters

   .. _spaces^toolbar.remove^button.id:

   .. api-member::
      :name: ``id``
      :refid: spaces-toolbar-remove-button-id
      :refname: id
      :type: (string)

      The id of the spaces toolbar button, which is to be removed. May only contain alphanumeric characters and underscores.

.. _spaces^toolbar.update^button:

updateButton(id, properties)
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 100]

Updates properties of the specified spaces toolbar button. Throws an exception if the requested spaces toolbar button does not exist or was not created by this extension.

.. api-header::
   :label: Parameters

   .. _spaces^toolbar.update^button.id:

   .. api-member::
      :name: ``id``
      :refid: spaces-toolbar-update-button-id
      :refname: id
      :type: (string)

      The id of the spaces toolbar button, which is to be updated. May only contain alphanumeric characters and underscores.

   .. _spaces^toolbar.update^button.properties:

   .. api-member::
      :name: ``properties``
      :refid: spaces-toolbar-update-button-properties
      :refname: properties
      :type: (:ref:`spaces^toolbar.^button^properties`)

      Only specified properties will be updated.

.. rst-class:: api-main-section

Types
=====

.. _spaces^toolbar.^button^properties:

ButtonProperties
----------------

.. api-section-annotation-hack:: -- [Added in TB 100]

.. api-header::
   :label: object

   .. _spaces^toolbar.^button^properties.badge^background^color:

   .. api-member::
      :name: [``badgeBackgroundColor``]
      :refid: spaces-toolbar-button-properties-badge-background-color
      :refname: badgeBackgroundColor
      :type: (string or :ref:`spaces^toolbar.^color^array`, optional)

      Sets the background color of the badge. Can be specified as an array of four integers in the range [0,255] that make up the RGBA color of the badge. For example, opaque red is :value:`[255, 0, 0, 255]`. Can also be a string with an HTML color name (:value:`red`) or a HEX color value (:value:`#FF0000` or :value:`#F00`). Reset when set to an empty string.

   .. _spaces^toolbar.^button^properties.badge^text:

   .. api-member::
      :name: [``badgeText``]
      :refid: spaces-toolbar-button-properties-badge-text
      :refname: badgeText
      :type: (string, optional)

      Sets the badge text for the spaces toolbar button. The badge is displayed on top of the icon. Any number of characters can be set, but only about four can fit in the space. Removed when set to an empty string.

   .. _spaces^toolbar.^button^properties.default^icons:

   .. api-member::
      :name: [``defaultIcons``]
      :refid: spaces-toolbar-button-properties-default-icons
      :refname: defaultIcons
      :type: (string or :ref:`spaces^toolbar.^icon^path`, optional)

      The paths to one or more icons for the button in the spaces toolbar. Defaults to the extension icon, if set to an empty string.

   .. _spaces^toolbar.^button^properties.theme^icons:

   .. api-member::
      :name: [``themeIcons``]
      :refid: spaces-toolbar-button-properties-theme-icons
      :refname: themeIcons
      :type: (array of :ref:`spaces^toolbar.^theme^icons`, optional)

      Specifies dark and light icons for the spaces toolbar button to be used with themes: The :value:`light` icons will be used on dark backgrounds and vice versa. At least the set for *16px* icons should be specified. The set for *32px* icons will be used on screens with a very high pixel density, if specified.

   .. _spaces^toolbar.^button^properties.title:

   .. api-member::
      :name: [``title``]
      :refid: spaces-toolbar-button-properties-title
      :refname: title
      :type: (string, optional)

      The title for the spaces toolbar button, used in the tooltip of the button and as the displayed name in the overflow menu. Defaults to the name of the extension, if set to an empty string.

   .. _spaces^toolbar.^button^properties.url:

   .. api-member::
      :name: [``url``]
      :refid: spaces-toolbar-button-properties-url
      :refname: url
      :type: (string, optional)

      The page url, loaded into a tab when the button is clicked. Supported are :value:`https://` and :value:`http://` links, as well as links to WebExtension pages.

.. _spaces^toolbar.^color^array:

ColorArray
----------

.. api-section-annotation-hack:: -- [Added in TB 100]

An array of four integers in the range [0,255] that make up the RGBA color. For example, opaque red is :value:`[255, 0, 0, 255]`.

.. api-header::
   :label: array of integer

.. _spaces^toolbar.^extension^file^url:

ExtensionFileUrl
----------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension, must not be empty and can be localized.

.. api-header::
   :label: string

.. _spaces^toolbar.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _spaces^toolbar.^icon^path:

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
   :label: :ref:`spaces^toolbar.^extension^file^url`

.. _spaces^toolbar.^theme^icons:

ThemeIcons
----------

.. api-section-annotation-hack:: 

Define a set of icons for themes depending on whether Thunderbird detects that the theme uses dark or light text. All provided URLs must be relative to the :value:`manifest.json` file.

.. api-header::
   :label: object

   .. _spaces^toolbar.^theme^icons.dark:

   .. api-member::
      :name: ``dark``
      :refid: spaces-toolbar-theme-icons-dark
      :refname: dark
      :type: (:ref:`spaces^toolbar.^extension^u^r^l`)

      The dark icon to use for light themes

   .. _spaces^toolbar.^theme^icons.light:

   .. api-member::
      :name: ``light``
      :refid: spaces-toolbar-theme-icons-light
      :refname: light
      :type: (:ref:`spaces^toolbar.^extension^u^r^l`)

      A light icon to use for dark themes

   .. _spaces^toolbar.^theme^icons.size:

   .. api-member::
      :name: ``size``
      :refid: spaces-toolbar-theme-icons-size
      :refname: size
      :type: (integer)

      The size of the icons
