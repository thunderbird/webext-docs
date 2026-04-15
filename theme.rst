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

.. role:: small

The theme API allows for customization of Thunderbird's visual elements.

.. rst-class:: api-main-section

Manifest file properties
========================

.. _theme.theme_experiment:

.. api-member::
   :name: [``theme_experiment``]
   :refid: theme-theme-experiment
   :refname: theme_experiment
   :type: (:ref:`theme.^theme^experiment`, optional)
   :annotation: -- [Added in TB 86]

   A theme experiment allows modifying the user interface of Thunderbird beyond what is currently possible using the built-in color, image and property keys of :ref:`theme.^theme^type`. These experiments are a precursor to proposing new theme features for inclusion in Thunderbird. Experimentation is done by mapping internal CSS color, image and property variables to new theme keys and using them in :ref:`theme.^theme^type` and by loading additional style sheets to add new CSS variables, extending the theme-able areas of Thunderbird. Can be used in static and dynamic themes.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _theme.permission.theme:

.. api-member::
   :name: :permission:`theme`
   :refid: theme-permission-theme
   :refname: theme

   Grant access to some or all methods of the theme API.

.. rst-class:: api-main-section

Functions
=========

.. _theme.get^current:

getCurrent([windowId])
----------------------

.. api-section-annotation-hack:: -- [Added in TB 86]

Returns the current theme for the specified window or the last focused window.

.. api-header::
   :label: Parameters

   .. _theme.get^current.window^id:

   .. api-member::
      :name: [``windowId``]
      :refid: theme-get-current-window-id
      :refname: windowId
      :type: (integer, optional)

      The window for which we want the theme.

.. api-header::
   :label: Return type (`Promise`_)

   .. _theme.get^current.returns:

   .. api-member::
      :refid: theme-get-current-returns
      :refname: _returns
      :type: :ref:`theme.^theme^type`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _theme.reset:

reset([windowId])
-----------------

.. api-section-annotation-hack:: -- [Added in TB 86]

Removes the updates made to the theme.

.. api-header::
   :label: Parameters

   .. _theme.reset.window^id:

   .. api-member::
      :name: [``windowId``]
      :refid: theme-reset-window-id
      :refname: windowId
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

   .. _theme.update.window^id:

   .. api-member::
      :name: [``windowId``]
      :refid: theme-update-window-id
      :refname: windowId
      :type: (integer, optional)

      The id of the window to update. No id updates all windows.

   .. _theme.update.details:

   .. api-member::
      :name: ``details``
      :refid: theme-update-details
      :refname: details
      :type: (:ref:`theme.^theme^type`)

      The properties of the theme to update.

.. api-header::
   :label: Required permissions

   - :permission:`theme`

.. rst-class:: api-main-section

Events
======

.. _theme.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 86]

Fired when a new theme has been applied

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. _theme.on^updated.listener(update^info):

   .. api-member::
      :name: ``listener(updateInfo)``
      :refid: theme-on-updated-listener-update-info
      :refname: listener(updateInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _theme.on^updated.update^info:

   .. api-member::
      :name: ``updateInfo``
      :refid: theme-on-updated-update-info
      :refname: updateInfo
      :type: (:ref:`theme.^theme^update^info`)

      Details of the theme update

.. rst-class:: api-main-section

Types
=====

.. _theme.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _theme.^image^data^or^extension^u^r^l:

ImageDataOrExtensionURL
-----------------------

.. api-section-annotation-hack:: 

Defines an image resource. Either a image URL relative the the extensions :value:`manifest.json` file (supported image formats are :value:`JPEG`, :value:`PNG`, :value:`APNG`, :value:`SVG` and :value:`GIF`), or a data URL using a base64 encoded representation of a :value:`PNG` or :value:`JPEG` image.

Example for a base64 encoded :value:`PNG` image:

.. code-block:: 

   data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==

.. api-header::
   :label: string

.. _theme.^theme^color:

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

*or*

.. api-header::
   :label: array of integer

   .. container:: api-member-node

      .. container:: api-member-description-only

         An RGB array of 3 integers. For example :value:`[220, 20, 60]` for the color *crimson*.

*or*

.. api-header::
   :label: array of number

   .. container:: api-member-node

      .. container:: api-member-description-only

         An RGBA array of 3 integers and a fractional (a float between 0 and 1). For example :value:`[220, 20, 60, 0.5]` for the color *crimson* with 50% opacity.

.. _theme.^theme^experiment:

ThemeExperiment
---------------

.. api-section-annotation-hack:: -- [Added in TB 86]

Defines additional color, image and property keys to be used in :ref:`theme.^theme^type`, extending the theme-able areas of Thunderbird.

.. api-header::
   :label: object

   .. _theme.^theme^experiment.colors:

   .. api-member::
      :name: [``colors``]
      :refid: theme-theme-experiment-colors
      :refname: colors
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map new theme color keys to internal Thunderbird CSS color variables. The new color key is usable as a color reference in :ref:`theme.^theme^type`.

      The following example maps the theme color key :value:`popup_affordance` to the CSS variable :value:`--arrowpanel-dimmed`:

      .. code-block:: JSON

         {
           "popup_affordance": "--arrowpanel-dimmed"
         }

   .. _theme.^theme^experiment.images:

   .. api-member::
      :name: [``images``]
      :refid: theme-theme-experiment-images
      :refname: images
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map new theme image keys to internal Thunderbird CSS image variables. The new image key is usable as an image reference in :ref:`theme.^theme^type`.

      The following example maps the theme image key :value:`theme_toolbar` to the CSS variable :value:`--toolbar-bgimage`:

      .. code-block:: JSON

         {
           "theme_toolbar": "--toolbar-bgimage"
         }

   .. _theme.^theme^experiment.properties:

   .. api-member::
      :name: [``properties``]
      :refid: theme-theme-experiment-properties
      :refname: properties
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map new theme property keys to internal Thunderbird CSS property variables. The new property key is usable as a property reference in :ref:`theme.^theme^type`.

      The following example maps the theme property key :value:`toolbar_image_alignment` to the CSS variable :value:`--toolbar-bgalignment`:

      .. code-block:: JSON

         {
           "toolbar_image_alignment": "--toolbar-bgalignment"
         }

   .. _theme.^theme^experiment.stylesheet:

   .. api-member::
      :name: [``stylesheet``]
      :refid: theme-theme-experiment-stylesheet
      :refname: stylesheet
      :type: (:ref:`theme.^extension^u^r^l`, optional)

      URL to a stylesheet introducing additional CSS variables, extending the theme-able areas of Thunderbird.

      The `theme_experiment add-on in our example repository <https://github.com/thunderbird/webext-examples/tree/master/manifest_v2/theme_experiment>`__ is using the stylesheet shown below, to add the :value:`--chat-button-color` CSS variable:

      .. code-block:: CSS

         image.toolbarbutton-icon[label="Chat"] {
           fill: var(--chat-button-color);
         }

      The following *manifest.json* file maps the :value:`--chat-button-color` CSS variable to the theme color key :value:`exp_chat_button` and uses it to set a color for the chat button:

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

.. _theme.^theme^manifest:

ThemeManifest
-------------

.. api-section-annotation-hack:: -- [Added in TB 86]

Contents of manifest.json for a static theme

.. api-header::
   :label: object

   .. _theme.^theme^manifest.theme:

   .. api-member::
      :name: ``theme``
      :refid: theme-theme-manifest-theme
      :refname: theme
      :type: (:ref:`theme.^theme^type`)

      Properties for a static theme. A static theme must not contain any other WebExtension logic. If additional logic is required, request the :permission:`theme` permission and load/update the theme dynamically. More information about themes can be found in the `theme guide <https://developer.thunderbird.net/add-ons/web-extension-themes>`__

   .. _theme.^theme^manifest.dark_theme:

   .. api-member::
      :name: [``dark_theme``]
      :refid: theme-theme-manifest-dark-theme
      :refname: dark_theme
      :type: (:ref:`theme.^theme^type`, optional)

      Fallback properties for the dark system theme in a static theme.

   .. _theme.^theme^manifest.default_locale:

   .. api-member::
      :name: [``default_locale``]
      :refid: theme-theme-manifest-default-locale
      :refname: default_locale
      :type: (string, optional)

   .. _theme.^theme^manifest.icons:

   .. api-member::
      :name: [``icons``]
      :refid: theme-theme-manifest-icons
      :refname: icons
      :type: (object, optional)

      Icons shown in the Add-ons Manager.

   .. _theme.^theme^manifest.theme_experiment:

   .. api-member::
      :name: [``theme_experiment``]
      :refid: theme-theme-manifest-theme-experiment
      :refname: theme_experiment
      :type: (:ref:`theme.^theme^experiment`, optional)

      CSS file with additional styles.

.. _theme.^theme^type:

ThemeType
---------

.. api-section-annotation-hack:: -- [Added in TB 86]

Contains the color, image and property settings of a theme.

.. api-header::
   :label: object

   .. _theme.^theme^type.colors:

   .. api-member::
      :name: [``colors``]
      :refid: theme-theme-type-colors
      :refname: colors
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map color values to theme color keys. The following built-in theme color keys are supported:

      .. _theme.^theme^type.colors.accentcolor:

      .. api-member::
         :name: [``accentcolor``]
         :refid: theme-theme-type-colors-accentcolor
         :refname: accentcolor
         :type: (:ref:`theme.^theme^color`, optional) **Deprecated.**

      .. _theme.^theme^type.colors.bookmark_text:

      .. api-member::
         :name: [``bookmark_text``]
         :refid: theme-theme-type-colors-bookmark-text
         :refname: bookmark_text
         :type: (:ref:`theme.^theme^color`, optional)

         Not used in Thunderbird.

      .. _theme.^theme^type.colors.button_background_active:

      .. api-member::
         :name: [``button_background_active``]
         :refid: theme-theme-type-colors-button-background-active
         :refname: button_background_active
         :type: (:ref:`theme.^theme^color`, optional)

         The color of the background of the pressed toolbar buttons.

      .. _theme.^theme^type.colors.button_background_hover:

      .. api-member::
         :name: [``button_background_hover``]
         :refid: theme-theme-type-colors-button-background-hover
         :refname: button_background_hover
         :type: (:ref:`theme.^theme^color`, optional)

         The color of the background of the toolbar buttons on hover.

      .. _theme.^theme^type.colors.frame:

      .. api-member::
         :name: [``frame``]
         :refid: theme-theme-type-colors-frame
         :refname: frame
         :type: (:ref:`theme.^theme^color`, optional)

         The background color of the header area.

      .. _theme.^theme^type.colors.frame_inactive:

      .. api-member::
         :name: [``frame_inactive``]
         :refid: theme-theme-type-colors-frame-inactive
         :refname: frame_inactive
         :type: (:ref:`theme.^theme^color`, optional)

         The background color of the header area when the window is inactive.

      .. _theme.^theme^type.colors.icons:

      .. api-member::
         :name: [``icons``]
         :refid: theme-theme-type-colors-icons
         :refname: icons
         :type: (:ref:`theme.^theme^color`, optional)

         The color of the toolbar icons. Defaults to the color specified by :value:`toolbar_text`.

      .. _theme.^theme^type.colors.icons_attention:

      .. api-member::
         :name: [``icons_attention``]
         :refid: theme-theme-type-colors-icons-attention
         :refname: icons_attention
         :type: (:ref:`theme.^theme^color`, optional)

         The color of the toolbar icons in attention state such as the chat icon with new messages.

      .. _theme.^theme^type.colors.ntp_background:

      .. api-member::
         :name: [``ntp_background``]
         :refid: theme-theme-type-colors-ntp-background
         :refname: ntp_background
         :type: (:ref:`theme.^theme^color`, optional)

         Not used in Thunderbird.

      .. _theme.^theme^type.colors.ntp_text:

      .. api-member::
         :name: [``ntp_text``]
         :refid: theme-theme-type-colors-ntp-text
         :refname: ntp_text
         :type: (:ref:`theme.^theme^color`, optional)

         Not used in Thunderbird.

      .. _theme.^theme^type.colors.popup:

      .. api-member::
         :name: [``popup``]
         :refid: theme-theme-type-colors-popup
         :refname: popup
         :type: (:ref:`theme.^theme^color`, optional)

         The background color of popups such as the AppMenu.

      .. _theme.^theme^type.colors.popup_border:

      .. api-member::
         :name: [``popup_border``]
         :refid: theme-theme-type-colors-popup-border
         :refname: popup_border
         :type: (:ref:`theme.^theme^color`, optional)

         The border color of popups.

      .. _theme.^theme^type.colors.popup_highlight:

      .. api-member::
         :name: [``popup_highlight``]
         :refid: theme-theme-type-colors-popup-highlight
         :refname: popup_highlight
         :type: (:ref:`theme.^theme^color`, optional)

         The background color of items highlighted using the keyboard inside popups.

      .. _theme.^theme^type.colors.popup_highlight_text:

      .. api-member::
         :name: [``popup_highlight_text``]
         :refid: theme-theme-type-colors-popup-highlight-text
         :refname: popup_highlight_text
         :type: (:ref:`theme.^theme^color`, optional)

         The text color of items highlighted using the keyboard inside popups.

      .. _theme.^theme^type.colors.popup_text:

      .. api-member::
         :name: [``popup_text``]
         :refid: theme-theme-type-colors-popup-text
         :refname: popup_text
         :type: (:ref:`theme.^theme^color`, optional)

         The text color of popups.

      .. _theme.^theme^type.colors.sidebar:

      .. api-member::
         :name: [``sidebar``]
         :refid: theme-theme-type-colors-sidebar
         :refname: sidebar
         :type: (:ref:`theme.^theme^color`, optional)

         The background color of the trees.

      .. _theme.^theme^type.colors.sidebar_border:

      .. api-member::
         :name: [``sidebar_border``]
         :refid: theme-theme-type-colors-sidebar-border
         :refname: sidebar_border
         :type: (:ref:`theme.^theme^color`, optional)

         The border color of the trees.

      .. _theme.^theme^type.colors.sidebar_highlight:

      .. api-member::
         :name: [``sidebar_highlight``]
         :refid: theme-theme-type-colors-sidebar-highlight
         :refname: sidebar_highlight
         :type: (:ref:`theme.^theme^color`, optional)

         The background color of highlighted rows in trees.

      .. _theme.^theme^type.colors.sidebar_highlight_border:

      .. api-member::
         :name: [``sidebar_highlight_border``]
         :refid: theme-theme-type-colors-sidebar-highlight-border
         :refname: sidebar_highlight_border
         :type: (:ref:`theme.^theme^color`, optional)

         The border color of highlighted rows in trees.

      .. _theme.^theme^type.colors.sidebar_highlight_text:

      .. api-member::
         :name: [``sidebar_highlight_text``]
         :refid: theme-theme-type-colors-sidebar-highlight-text
         :refname: sidebar_highlight_text
         :type: (:ref:`theme.^theme^color`, optional)

         The text color of highlighted rows in trees.

      .. _theme.^theme^type.colors.sidebar_text:

      .. api-member::
         :name: [``sidebar_text``]
         :refid: theme-theme-type-colors-sidebar-text
         :refname: sidebar_text
         :type: (:ref:`theme.^theme^color`, optional)

         The text color of the trees. Needed to enable the tree theming.

      .. _theme.^theme^type.colors.tab_background_separator:

      .. api-member::
         :name: [``tab_background_separator``]
         :refid: theme-theme-type-colors-tab-background-separator
         :refname: tab_background_separator
         :type: (:ref:`theme.^theme^color`, optional)

         The color of the vertical separator of the background tabs.

      .. _theme.^theme^type.colors.tab_background_text:

      .. api-member::
         :name: [``tab_background_text``]
         :refid: theme-theme-type-colors-tab-background-text
         :refname: tab_background_text
         :type: (:ref:`theme.^theme^color`, optional)

         The text color of the unselected tabs.

      .. _theme.^theme^type.colors.tab_line:

      .. api-member::
         :name: [``tab_line``]
         :refid: theme-theme-type-colors-tab-line
         :refname: tab_line
         :type: (:ref:`theme.^theme^color`, optional)

         The color of the selected tab line.

      .. _theme.^theme^type.colors.tab_loading:

      .. api-member::
         :name: [``tab_loading``]
         :refid: theme-theme-type-colors-tab-loading
         :refname: tab_loading
         :type: (:ref:`theme.^theme^color`, optional)

         The color of the tab loading indicator.

      .. _theme.^theme^type.colors.tab_selected:

      .. api-member::
         :name: [``tab_selected``]
         :refid: theme-theme-type-colors-tab-selected
         :refname: tab_selected
         :type: (:ref:`theme.^theme^color`, optional)

         Background color of the selected tab. Defaults to the color specified by :value:`toolbar`.

      .. _theme.^theme^type.colors.tab_text:

      .. api-member::
         :name: [``tab_text``]
         :refid: theme-theme-type-colors-tab-text
         :refname: tab_text
         :type: (:ref:`theme.^theme^color`, optional)

         The text color for the selected tab. Defaults to the color specified by :value:`toolbar_text`.

      .. _theme.^theme^type.colors.textcolor:

      .. api-member::
         :name: [``textcolor``]
         :refid: theme-theme-type-colors-textcolor
         :refname: textcolor
         :type: (:ref:`theme.^theme^color`, optional) **Deprecated.**

      .. _theme.^theme^type.colors.toolbar:

      .. api-member::
         :name: [``toolbar``]
         :refid: theme-theme-type-colors-toolbar
         :refname: toolbar
         :type: (:ref:`theme.^theme^color`, optional)

         The background color of the toolbars. Also used as default value for :value:`tab_selected`.

      .. _theme.^theme^type.colors.toolbar_bottom_separator:

      .. api-member::
         :name: [``toolbar_bottom_separator``]
         :refid: theme-theme-type-colors-toolbar-bottom-separator
         :refname: toolbar_bottom_separator
         :type: (:ref:`theme.^theme^color`, optional)

         The color of the line separating the bottom of the toolbar from the region below.

      .. _theme.^theme^type.colors.toolbar_field:

      .. api-member::
         :name: [``toolbar_field``]
         :refid: theme-theme-type-colors-toolbar-field
         :refname: toolbar_field
         :type: (:ref:`theme.^theme^color`, optional)

         The background color for fields in the toolbar, such as the search field.

      .. _theme.^theme^type.colors.toolbar_field_border:

      .. api-member::
         :name: [``toolbar_field_border``]
         :refid: theme-theme-type-colors-toolbar-field-border
         :refname: toolbar_field_border
         :type: (:ref:`theme.^theme^color`, optional)

         The border color for fields in the toolbar.

      .. _theme.^theme^type.colors.toolbar_field_border_focus:

      .. api-member::
         :name: [``toolbar_field_border_focus``]
         :refid: theme-theme-type-colors-toolbar-field-border-focus
         :refname: toolbar_field_border_focus
         :type: (:ref:`theme.^theme^color`, optional)

         The focused border color for fields in the toolbar.

      .. _theme.^theme^type.colors.toolbar_field_focus:

      .. api-member::
         :name: [``toolbar_field_focus``]
         :refid: theme-theme-type-colors-toolbar-field-focus
         :refname: toolbar_field_focus
         :type: (:ref:`theme.^theme^color`, optional)

         The focused background color for fields in the toolbar.

      .. _theme.^theme^type.colors.toolbar_field_highlight:

      .. api-member::
         :name: [``toolbar_field_highlight``]
         :refid: theme-theme-type-colors-toolbar-field-highlight
         :refname: toolbar_field_highlight
         :type: (:ref:`theme.^theme^color`, optional)

         The background color used to indicate the current selection of text in the search field.

      .. _theme.^theme^type.colors.toolbar_field_highlight_text:

      .. api-member::
         :name: [``toolbar_field_highlight_text``]
         :refid: theme-theme-type-colors-toolbar-field-highlight-text
         :refname: toolbar_field_highlight_text
         :type: (:ref:`theme.^theme^color`, optional)

         The color used to draw text that's currently selected in the search field.

      .. _theme.^theme^type.colors.toolbar_field_separator:

      .. api-member::
         :name: [``toolbar_field_separator``]
         :refid: theme-theme-type-colors-toolbar-field-separator
         :refname: toolbar_field_separator
         :type: (:ref:`theme.^theme^color`, optional) **Deprecated.**

         Not used in Thunderbird.

      .. _theme.^theme^type.colors.toolbar_field_text:

      .. api-member::
         :name: [``toolbar_field_text``]
         :refid: theme-theme-type-colors-toolbar-field-text
         :refname: toolbar_field_text
         :type: (:ref:`theme.^theme^color`, optional)

         The text color for fields in the toolbar.

      .. _theme.^theme^type.colors.toolbar_field_text_focus:

      .. api-member::
         :name: [``toolbar_field_text_focus``]
         :refid: theme-theme-type-colors-toolbar-field-text-focus
         :refname: toolbar_field_text_focus
         :type: (:ref:`theme.^theme^color`, optional)

         The text color in the focused fields in the toolbar.

      .. _theme.^theme^type.colors.toolbar_text:

      .. api-member::
         :name: [``toolbar_text``]
         :refid: theme-theme-type-colors-toolbar-text
         :refname: toolbar_text
         :type: (:ref:`theme.^theme^color`, optional)

         The text color in the main Thunderbird toolbar. Also used as default value for :value:`icons` and :value:`tab_text`.

      .. _theme.^theme^type.colors.toolbar_top_separator:

      .. api-member::
         :name: [``toolbar_top_separator``]
         :refid: theme-theme-type-colors-toolbar-top-separator
         :refname: toolbar_top_separator
         :type: (:ref:`theme.^theme^color`, optional)

         The color of the line separating the top of the toolbar from the region above.

      .. _theme.^theme^type.colors.toolbar_vertical_separator:

      .. api-member::
         :name: [``toolbar_vertical_separator``]
         :refid: theme-theme-type-colors-toolbar-vertical-separator
         :refname: toolbar_vertical_separator
         :type: (:ref:`theme.^theme^color`, optional)

         The color of the vertical separators on the toolbars.

   .. _theme.^theme^type.images:

   .. api-member::
      :name: [``images``]
      :refid: theme-theme-type-images
      :refname: images
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map images to theme image keys. The following built-in theme image keys are supported:

      .. _theme.^theme^type.images.additional_backgrounds:

      .. api-member::
         :name: [``additional_backgrounds``]
         :refid: theme-theme-type-images-additional-backgrounds
         :refname: additional_backgrounds
         :type: (array of :ref:`theme.^image^data^or^extension^u^r^l`, optional)

         Additional images added to the header area and displayed behind the :value:`theme_frame` image.

      .. _theme.^theme^type.images.header^u^r^l:

      .. api-member::
         :name: [``headerURL``]
         :refid: theme-theme-type-images-header-u-r-l
         :refname: headerURL
         :type: (:ref:`theme.^image^data^or^extension^u^r^l`, optional) **Deprecated.**

      .. _theme.^theme^type.images.theme_frame:

      .. api-member::
         :name: [``theme_frame``]
         :refid: theme-theme-type-images-theme-frame
         :refname: theme_frame
         :type: (:ref:`theme.^image^data^or^extension^u^r^l`, optional)

         Foreground image on the header area.

   .. _theme.^theme^type.properties:

   .. api-member::
      :name: [``properties``]
      :refid: theme-theme-type-properties
      :refname: properties
      :type: (object, optional)

      A *dictionary object* with one or more *key-value* pairs to map property values to theme property keys. The following built-in theme property keys are supported:

      .. _theme.^theme^type.properties.additional_backgrounds_alignment:

      .. api-member::
         :name: [``additional_backgrounds_alignment``]
         :refid: theme-theme-type-properties-additional-backgrounds-alignment
         :refname: additional_backgrounds_alignment
         :type: (array of `string`, optional)

         An array of alignment values, one for each image in :value:`additional_backgrounds`.

         Supported values:

         .. api-member::
            :name: :value:`bottom`
            :refname: bottom

            Align to the bottom.

         .. api-member::
            :name: :value:`center`
            :refname: center

            Align to the center horizontally.

         .. api-member::
            :name: :value:`center bottom`
            :refname: center bottom

            Align to the center bottom.

         .. api-member::
            :name: :value:`center center`
            :refname: center center

            Align to the center horizontally and vertically.

         .. api-member::
            :name: :value:`center top`
            :refname: center top

            Align to the center top.

         .. api-member::
            :name: :value:`left`
            :refname: left

            Align to the left.

         .. api-member::
            :name: :value:`left bottom`
            :refname: left bottom

            Align to the left bottom.

         .. api-member::
            :name: :value:`left center`
            :refname: left center

            Align to the left center.

         .. api-member::
            :name: :value:`left top`
            :refname: left top

            Align to the left top.

         .. api-member::
            :name: :value:`right`
            :refname: right

            Align to the right.

         .. api-member::
            :name: :value:`right bottom`
            :refname: right bottom

            Align to the right bottom.

         .. api-member::
            :name: :value:`right center`
            :refname: right center

            Align to the right center.

         .. api-member::
            :name: :value:`right top`
            :refname: right top

            Align to the right top.

         .. api-member::
            :name: :value:`top`
            :refname: top

            Align to the top.

      .. _theme.^theme^type.properties.additional_backgrounds_tiling:

      .. api-member::
         :name: [``additional_backgrounds_tiling``]
         :refid: theme-theme-type-properties-additional-backgrounds-tiling
         :refname: additional_backgrounds_tiling
         :type: (array of `string`, optional)

         An array of tiling values, one for each image in :value:`additional_backgrounds`.

         Supported values:

         .. api-member::
            :name: :value:`no-repeat`
            :refname: no-repeat

            The background image is not repeated.

         .. api-member::
            :name: :value:`repeat`
            :refname: repeat

            The background image is repeated both horizontally and vertically.

         .. api-member::
            :name: :value:`repeat-x`
            :refname: repeat-x

            The background image is repeated horizontally.

         .. api-member::
            :name: :value:`repeat-y`
            :refname: repeat-y

            The background image is repeated vertically.

      .. _theme.^theme^type.properties.color_scheme:

      .. api-member::
         :name: [``color_scheme``]
         :refid: theme-theme-type-properties-color-scheme
         :refname: color_scheme
         :type: (`string`, optional)
         :annotation: -- [Added in TB 100]

         If set, overrides the general theme (context menus, toolbars, content area).

         Supported values:

         .. _theme.^theme^type.properties.color_scheme.auto:

         .. api-member::
            :name: :value:`auto`
            :refid: theme-theme-type-properties-color-scheme-auto
            :refname: auto

            Automatically determine the color scheme.

         .. _theme.^theme^type.properties.color_scheme.dark:

         .. api-member::
            :name: :value:`dark`
            :refid: theme-theme-type-properties-color-scheme-dark
            :refname: dark

            Use a dark color scheme.

         .. _theme.^theme^type.properties.color_scheme.light:

         .. api-member::
            :name: :value:`light`
            :refid: theme-theme-type-properties-color-scheme-light
            :refname: light

            Use a light color scheme.

         .. _theme.^theme^type.properties.color_scheme.system:

         .. api-member::
            :name: :value:`system`
            :refid: theme-theme-type-properties-color-scheme-system
            :refname: system
            :annotation: -- [Added in TB 148]

            Use the system color scheme.

      .. _theme.^theme^type.properties.content_color_scheme:

      .. api-member::
         :name: [``content_color_scheme``]
         :refid: theme-theme-type-properties-content-color-scheme
         :refname: content_color_scheme
         :type: (`string`, optional)
         :annotation: -- [Added in TB 100]

         If set, overrides the color scheme for the content area.

         Supported values:

         .. _theme.^theme^type.properties.content_color_scheme.auto:

         .. api-member::
            :name: :value:`auto`
            :refid: theme-theme-type-properties-content-color-scheme-auto
            :refname: auto

            Automatically determine the color scheme.

         .. _theme.^theme^type.properties.content_color_scheme.dark:

         .. api-member::
            :name: :value:`dark`
            :refid: theme-theme-type-properties-content-color-scheme-dark
            :refname: dark

            Use a dark color scheme.

         .. _theme.^theme^type.properties.content_color_scheme.light:

         .. api-member::
            :name: :value:`light`
            :refid: theme-theme-type-properties-content-color-scheme-light
            :refname: light

            Use a light color scheme.

         .. _theme.^theme^type.properties.content_color_scheme.system:

         .. api-member::
            :name: :value:`system`
            :refid: theme-theme-type-properties-content-color-scheme-system
            :refname: system
            :annotation: -- [Added in TB 148]

            Use the system color scheme.

.. _theme.^theme^update^info:

ThemeUpdateInfo
---------------

.. api-section-annotation-hack:: -- [Added in TB 86]

Info provided in the onUpdated listener.

.. api-header::
   :label: object

   .. _theme.^theme^update^info.theme:

   .. api-member::
      :name: ``theme``
      :refid: theme-theme-update-info-theme
      :refname: theme
      :type: (:ref:`theme.^theme^type`)

      The new theme after update

   .. _theme.^theme^update^info.window^id:

   .. api-member::
      :name: [``windowId``]
      :refid: theme-theme-update-info-window-id
      :refname: windowId
      :type: (integer, optional)

      The id of the window the theme has been applied to
