.. container:: sticky-sidebar

  ≡ theme API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=========
theme API
=========

.. role:: permission

.. role:: value

.. role:: code

The theme API allows for customization of Thunderbird's visual elements.

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``theme_experiment``]
   :type: (:ref:`theme.ThemeExperiment`, optional)
   :annotation: -- [Added in TB 86]

   A theme experiment allows modifying the user interface of Thunderbird beyond what is currently possible using the built-in color, image and property keys of :ref:`theme.ThemeType`. These experiments are a precursor to proposing new theme features for inclusion in Thunderbird. Experimentation is done by mapping internal CSS color, image and property variables to new theme keys and using them in :ref:`theme.ThemeType` and by loading additional style sheets to add new CSS variables, extending the theme-able areas of Thunderbird. Can be used in static and dynamic themes.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`theme`

.. rst-class:: api-main-section

Functions
=========

.. _theme.getCurrent:

getCurrent([windowId])
----------------------

.. api-section-annotation-hack:: -- [Added in TB 86]

Returns the current theme for the specified window or the last focused window.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``windowId``]
      :type: (integer, optional)

      The window for which we want the theme.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`theme.ThemeType`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _theme.reset:

reset([windowId])
-----------------

.. api-section-annotation-hack:: -- [Added in TB 86]

Removes the updates made to the theme.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``windowId``]
      :type: (integer, optional)

      The id of the window to reset. No id resets all windows.

.. api-header::
   :label: Required permissions

   - :permission:`theme`

.. _theme.update:

update([windowId], details)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 86]

Make complete updates to the theme. Resolves when the update has completed.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``windowId``]
      :type: (integer, optional)

      The id of the window to update. No id updates all windows.

   .. api-member::
      :name: ``details``
      :type: (:ref:`theme.ThemeType`)

      The properties of the theme to update.

.. api-header::
   :label: Required permissions

   - :permission:`theme`

.. rst-class:: api-main-section

Events
======

.. _theme.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 86]

Fired when a new theme has been applied

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. api-member::
      :name: ``listener(updateInfo)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``updateInfo``
      :type: (:ref:`theme.ThemeUpdateInfo`)

      Details of the theme update

.. rst-class:: api-main-section

Types
=====

.. _theme.ExtensionURL:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _theme.ImageDataOrExtensionURL:

ImageDataOrExtensionURL
-----------------------

.. api-section-annotation-hack:: 

Defines an image resource. Either a image URL relative the the extensions :value:`manifest.json` file (supported image formats are :value:`JPEG`, :value:`PNG`, :value:`APNG`, :value:`SVG` and :value:`GIF`), or a data URL using a base64 encoded representation of a :value:`PNG` or :value:`JPEG` image.

Example for a base64 encoded :value:`PNG` image:

.. code-block:: 

   data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==

.. api-header::
   :label: string

.. _theme.ThemeColor:

ThemeColor
----------

.. api-section-annotation-hack:: -- [Added in TB 86]

Defines a color value.

.. api-header::
   :label: string

   .. container:: api-member-node

      .. container:: api-member-description-only

         A string containing a valid `CSS color string <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_colors/Color_values>`__, including hexadecimal or functional representations. For example the color *crimson* can be specified as: 

          * :value:`crimson` 

          * :value:`#dc143c` 

          * :value:`rgb(220, 20, 60)` (or :value:`rgba(220, 20, 60, 0.5)` to set 50% opacity) 

          * :value:`hsl(348, 83%, 47%)` (or :value:`hsla(348, 83%, 47%, 0.5)` to set 50% opacity)

OR

.. api-header::
   :label: array of integer

   .. container:: api-member-node

      .. container:: api-member-description-only

         An RGB array of 3 integers. For example :value:`[220, 20, 60]` for the color *crimson*.

OR

.. api-header::
   :label: array of number

   .. container:: api-member-node

      .. container:: api-member-description-only

         An RGBA array of 3 integers and a fractional (a float between 0 and 1). For example :value:`[220, 20, 60, 0.5]` for the color *crimson* with 50% opacity.

.. _theme.ThemeExperiment:

ThemeExperiment
---------------

.. api-section-annotation-hack:: -- [Added in TB 86]

Defines additional color, image and property keys to be used in :ref:`theme.ThemeType`, extending the theme-able areas of Thunderbird.

.. api-header::
   :label: object

   .. _theme.ThemeExperiment.colors:

   .. api-member::
      :name: [``colors``]
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map new theme color keys to internal Thunderbird CSS color variables. The new color key is usable as a color reference in :ref:`theme.ThemeType`.

      The following example maps the theme color key :value:`popup_affordance` to the CSS variable `--arrowpanel-dimmed`:

      .. code-block:: JSON

         {
           "popup_affordance": "--arrowpanel-dimmed"
         }

   .. _theme.ThemeExperiment.images:

   .. api-member::
      :name: [``images``]
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map new theme image keys to internal Thunderbird CSS image variables. The new image key is usable as an image reference in :ref:`theme.ThemeType`.

      The following example maps the theme image key :value:`theme_toolbar` to the CSS variable `--toolbar-bgimage`:

      .. code-block:: JSON

         {
           "theme_toolbar": "--toolbar-bgimage"
         }

   .. _theme.ThemeExperiment.properties:

   .. api-member::
      :name: [``properties``]
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map new theme property keys to internal Thunderbird CSS property variables. The new property key is usable as a property reference in :ref:`theme.ThemeType`.

      The following example maps the theme property key :value:`toolbar_image_alignment` to the CSS variable `--toolbar-bgalignment`:

      .. code-block:: JSON

         {
           "toolbar_image_alignment": "--toolbar-bgalignment"
         }

   .. _theme.ThemeExperiment.stylesheet:

   .. api-member::
      :name: [``stylesheet``]
      :type: (:ref:`theme.ExtensionURL`, optional)

      URL to a stylesheet introducing additional CSS variables, extending the theme-able areas of Thunderbird.

      The `theme_experiment add-on in our example repository <https://github.com/thunderbird/webext-examples/tree/master/manifest_v2/theme_experiment>`__ is using the stylesheet shown below, to add the :value:`--chat-button-color` CSS variable:

      .. code-block:: CSS

         image.toolbarbutton-icon[label="Chat"] {
           fill: var(--chat-button-color);
         }

      The following *manifest.json* file maps the `--chat-button-color` CSS variable to the theme color key :value:`exp_chat_button` and uses it to set a color for the chat button:

      .. code-block:: JSON

         {
           "name": "Theme Experiment",
           "description": "Changing the color of the chat icon using a theme_experiment.",
           "version": "1",
           "applications": {
             "gecko": {
               "id": "theme_experiment@sample.extensions.thunderbird.net",
               "strict_min_version": "78.0"
             }
           },
           "manifest_version": 2,
           "theme_experiment": {
             "stylesheet": "style.css",
             "colors": {
               "exp_chat_button": "--chat-button-color"
             }
           },
           "theme": {
             "colors": {
               "exp_chat_button": "orange"
             }
           }
         }

.. _theme.ThemeType:

ThemeType
---------

.. api-section-annotation-hack:: -- [Added in TB 86]

Contains the color, image and property settings of a theme.

.. api-header::
   :label: object

   .. _theme.ThemeType.colors:

   .. api-member::
      :name: [``colors``]
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map color values to theme color keys. The following built-in theme color keys are supported:

      .. api-member::
         :name: [``accentcolor``]
         :type: (:ref:`theme.ThemeColor`, optional) **Deprecated.**

      .. api-member::
         :name: [``bookmark_text``]
         :type: (:ref:`theme.ThemeColor`, optional)

         Not used in Thunderbird.

      .. api-member::
         :name: [``button_background_active``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The color of the background of the pressed toolbar buttons.

      .. api-member::
         :name: [``button_background_hover``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The color of the background of the toolbar buttons on hover.

      .. api-member::
         :name: [``frame``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The background color of the header area.

      .. api-member::
         :name: [``frame_inactive``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The background color of the header area when the window is inactive.

      .. api-member::
         :name: [``icons``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The color of the toolbar icons. Defaults to the color specified by :value:`toolbar_text`.

      .. api-member::
         :name: [``icons_attention``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The color of the toolbar icons in attention state such as the chat icon with new messages.

      .. api-member::
         :name: [``ntp_background``]
         :type: (:ref:`theme.ThemeColor`, optional)

         Not used in Thunderbird.

      .. api-member::
         :name: [``ntp_text``]
         :type: (:ref:`theme.ThemeColor`, optional)

         Not used in Thunderbird.

      .. api-member::
         :name: [``popup``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The background color of popups such as the AppMenu.

      .. api-member::
         :name: [``popup_border``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The border color of popups.

      .. api-member::
         :name: [``popup_highlight``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The background color of items highlighted using the keyboard inside popups.

      .. api-member::
         :name: [``popup_highlight_text``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The text color of items highlighted using the keyboard inside popups.

      .. api-member::
         :name: [``popup_text``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The text color of popups.

      .. api-member::
         :name: [``sidebar``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The background color of the trees.

      .. api-member::
         :name: [``sidebar_border``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The border color of the trees.

      .. api-member::
         :name: [``sidebar_highlight``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The background color of highlighted rows in trees.

      .. api-member::
         :name: [``sidebar_highlight_border``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The border color of highlighted rows in trees.

      .. api-member::
         :name: [``sidebar_highlight_text``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The text color of highlighted rows in trees.

      .. api-member::
         :name: [``sidebar_text``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The text color of the trees. Needed to enable the tree theming.

      .. api-member::
         :name: [``tab_background_separator``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The color of the vertical separator of the background tabs.

      .. api-member::
         :name: [``tab_background_text``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The text color of the unselected tabs.

      .. api-member::
         :name: [``tab_line``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The color of the selected tab line.

      .. api-member::
         :name: [``tab_loading``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The color of the tab loading indicator.

      .. api-member::
         :name: [``tab_selected``]
         :type: (:ref:`theme.ThemeColor`, optional)

         Background color of the selected tab. Defaults to the color specified by :value:`toolbar`.

      .. api-member::
         :name: [``tab_text``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The text color for the selected tab. Defaults to the color specified by :value:`toolbar_text`.

      .. api-member::
         :name: [``textcolor``]
         :type: (:ref:`theme.ThemeColor`, optional) **Deprecated.**

      .. api-member::
         :name: [``toolbar``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The background color of the toolbars. Also used as default value for :value:`tab_selected`.

      .. api-member::
         :name: [``toolbar_bottom_separator``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The color of the line separating the bottom of the toolbar from the region below.

      .. api-member::
         :name: [``toolbar_field``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The background color for fields in the toolbar, such as the search field.

      .. api-member::
         :name: [``toolbar_field_border``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The border color for fields in the toolbar.

      .. api-member::
         :name: [``toolbar_field_border_focus``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The focused border color for fields in the toolbar.

      .. api-member::
         :name: [``toolbar_field_focus``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The focused background color for fields in the toolbar.

      .. api-member::
         :name: [``toolbar_field_highlight``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The background color used to indicate the current selection of text in the search field.

      .. api-member::
         :name: [``toolbar_field_highlight_text``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The color used to draw text that's currently selected in the search field.

      .. api-member::
         :name: [``toolbar_field_separator``]
         :type: (:ref:`theme.ThemeColor`, optional) **Deprecated.**

         Not used in Thunderbird.

      .. api-member::
         :name: [``toolbar_field_text``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The text color for fields in the toolbar.

      .. api-member::
         :name: [``toolbar_field_text_focus``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The text color in the focused fields in the toolbar.

      .. api-member::
         :name: [``toolbar_text``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The text color in the main Thunderbird toolbar. Also used as default value for :value:`icons` and :value:`tab_text`.

      .. api-member::
         :name: [``toolbar_top_separator``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The color of the line separating the top of the toolbar from the region above.

      .. api-member::
         :name: [``toolbar_vertical_separator``]
         :type: (:ref:`theme.ThemeColor`, optional)

         The color of the vertical separators on the toolbars.

   .. _theme.ThemeType.images:

   .. api-member::
      :name: [``images``]
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map images to theme image keys. The following built-in theme image keys are supported:

      .. api-member::
         :name: [``additional_backgrounds``]
         :type: (array of :ref:`theme.ImageDataOrExtensionURL`, optional)

         Additional images added to the header area and displayed behind the :value:`theme_frame` image.

      .. api-member::
         :name: [``headerURL``]
         :type: (:ref:`theme.ImageDataOrExtensionURL`, optional) **Deprecated.**

      .. api-member::
         :name: [``theme_frame``]
         :type: (:ref:`theme.ImageDataOrExtensionURL`, optional)

         Foreground image on the header area.

   .. _theme.ThemeType.properties:

   .. api-member::
      :name: [``properties``]
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map property values to theme property keys. The following built-in theme property keys are supported:

      .. api-member::
         :name: [``additional_backgrounds_alignment``]
         :type: (array of `string`, optional)

         Supported values:

         .. api-member::
            :name: :value:`bottom`

         .. api-member::
            :name: :value:`center`

         .. api-member::
            :name: :value:`left`

         .. api-member::
            :name: :value:`right`

         .. api-member::
            :name: :value:`top`

         .. api-member::
            :name: :value:`center bottom`

         .. api-member::
            :name: :value:`center center`

         .. api-member::
            :name: :value:`center top`

         .. api-member::
            :name: :value:`left bottom`

         .. api-member::
            :name: :value:`left center`

         .. api-member::
            :name: :value:`left top`

         .. api-member::
            :name: :value:`right bottom`

         .. api-member::
            :name: :value:`right center`

         .. api-member::
            :name: :value:`right top`

      .. api-member::
         :name: [``additional_backgrounds_tiling``]
         :type: (array of `string`, optional)

         Supported values:

         .. api-member::
            :name: :value:`no-repeat`

         .. api-member::
            :name: :value:`repeat`

         .. api-member::
            :name: :value:`repeat-x`

         .. api-member::
            :name: :value:`repeat-y`

      .. api-member::
         :name: [``color_scheme``]
         :type: (`string`, optional)
         :annotation: -- [Added in TB 100]

         If set, overrides the general theme (context menus, toolbars, content area).

         Supported values:

         .. api-member::
            :name: :value:`light`

         .. api-member::
            :name: :value:`dark`

         .. api-member::
            :name: :value:`auto`

      .. api-member::
         :name: [``content_color_scheme``]
         :type: (`string`, optional)
         :annotation: -- [Added in TB 100]

         If set, overrides the color scheme for the content area.

         Supported values:

         .. api-member::
            :name: :value:`light`

         .. api-member::
            :name: :value:`dark`

         .. api-member::
            :name: :value:`auto`

.. _theme.ThemeUpdateInfo:

ThemeUpdateInfo
---------------

.. api-section-annotation-hack:: -- [Added in TB 86]

Info provided in the onUpdated listener.

.. api-header::
   :label: object

   .. _theme.ThemeUpdateInfo.theme:

   .. api-member::
      :name: ``theme``
      :type: (:ref:`theme.ThemeType`)

      The new theme after update

   .. _theme.ThemeUpdateInfo.windowId:

   .. api-member::
      :name: [``windowId``]
      :type: (integer, optional)

      The id of the window the theme has been applied to
