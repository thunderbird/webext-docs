.. _theme_api:

=====
theme
=====

The theme API was added in Thunderbird 86 and has been backported to Thunderbird 78.7.1 (see `bug 1684666`__). It’s more or less the same as the `Firefox theme API`__, but has been extended to better fit the needs of Thunderbird.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1684666
__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/theme

.. role:: permission

The theme API allows customizing of visual elements of Thunderbird.

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``theme``]
   :type: (:ref:`theme.ThemeType`)
   
   Properties for a static theme. A static theme must not contain any other WebExtension logic. If additional logic is required, request the :permission:`theme` permission and load/update the theme dynamically. More information about themes can be found in the `theme guide <https://developer.thunderbird.net/add-ons/web-extension-themes>`__.

.. api-member::
   :name: [``dark_theme``]
   :type: (:ref:`theme.ThemeType`)
   
   Fallback properties for the dark system theme in a static theme.

.. api-member::
   :name: [``theme_experiment``]
   :type: (:ref:`theme.ThemeExperiment`)
   
   A theme experiment allows modifying the user interface of Thunderbird beyond what is currently possible using the built-in color, image and property keys of :ref:`theme.ThemeType`. These experiments are a precursor to proposing new theme features for inclusion in Thunderbird. Experimentation is done by mapping internal CSS color, image and property variables to new theme keys and using them in :ref:`theme.ThemeType` and by loading additional style sheets to add new CSS variables, extending the theme-able areas of Thunderbird. Can be used in static and dynamic themes.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`theme`

   Dynamically apply themes to Thunderbird’s user interface.

.. rst-class:: api-main-section

Functions
=========

.. _theme.getCurrent:

getCurrent([windowId])
----------------------

.. api-section-annotation-hack:: 

Returns the current theme for the specified window or the last focused window.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``windowId``]
      :type: (integer)
      
      The window for which we want the theme.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`theme.ThemeType`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _theme.update:

update([windowId], details)
---------------------------

.. api-section-annotation-hack:: 

Make complete updates to the theme. Resolves when the update has completed.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``windowId``]
      :type: (integer)
      
      The id of the window to update. No id updates all windows.
   
   
   .. api-member::
      :name: ``details``
      :type: (:ref:`theme.ThemeType`)
      
      The properties of the theme to update.
   

.. api-header::
   :label: Required permissions

   - :permission:`theme`

.. _theme.reset:

reset([windowId])
-----------------

.. api-section-annotation-hack:: 

Removes the updates made to the theme.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``windowId``]
      :type: (integer)
      
      The id of the window to reset. No id resets all windows.
   

.. api-header::
   :label: Required permissions

   - :permission:`theme`

.. rst-class:: api-main-section

Events
======

.. _theme.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: 

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

.. _theme.ImageDataOrExtensionURL:

ImageDataOrExtensionURL
-----------------------

.. api-section-annotation-hack:: 

Defines an image resource.

.. api-header::
   :label: string

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         A relative URL for an image bundled with the extension. For example ``images/background.png``. The following image formats are supported: 
         
         * JPEG 
         
         * PNG 
         
         * APNG 
         
         * SVG (animated SVG is supported from Thunderbird 59) 
         
         * GIF (animated GIF isn’t supported)
   

OR

.. api-header::
   :label: string

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         A data URL using a base64 encoded representation of a PNG or JPG image. For example: 
         
         ::
         
           data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==
         
         
   

.. _theme.ThemeColor:

ThemeColor
----------

.. api-section-annotation-hack:: 

Defines a color value.

.. api-header::
   :label: string

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         A string containing a valid `CSS color string <https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#color_keywords>`__, including hexadecimal or functional representations. For example the color *crimson* can be specified as: 
         
         * ``crimson`` 
         
         * ``#dc143c`` 
         
         * ``rgb(220, 20, 60)`` (or ``rgba(220, 20, 60, 0.5)`` to set 50% opacity) 
         
         * ``hsl(348, 83%, 47%)`` (or ``hsla(348, 83%, 47%, 0.5)`` to set 50% opacity)
   

OR

.. api-header::
   :label: array of integer

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         An RGB array of 3 integers. For example ``[220, 20, 60]`` for the color *crimson*.
   

OR

.. api-header::
   :label: array of number

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         An RGBA array of 3 integers and a fractional (a float between 0 and 1). For example ``[220, 20, 60, 0.5]`` for the color *crimson* with 50% opacity.
   

.. _theme.ThemeExperiment:

ThemeExperiment
---------------

.. api-section-annotation-hack:: 

Defines additional color, image and property keys to be used in :ref:`theme.ThemeType`, extending the theme-able areas of Thunderbird.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``colors``]
      :type: (object)
      
      Object with one or more key-value pairs to map new theme color keys to internal Thunderbird CSS color variables. The example shown below maps the theme color key ``popup_affordance`` to the CSS color variable ``--arrowpanel-dimmed``. The new color key is usable as a color reference in :ref:`theme.ThemeType`. 
      
      .. literalinclude:: includes/theme/theme_experiment_color.json
        :language: JSON
      
      
   
   
   .. api-member::
      :name: [``images``]
      :type: (object)
      
      Object with one or more key-value pairs to map new theme image keys to internal Thunderbird CSS image variables. The new image key is usable as an image reference in :ref:`theme.ThemeType`. Example: 
      
      .. literalinclude:: includes/theme/theme_experiment_image.json
        :language: JSON
      
      
   
   
   .. api-member::
      :name: [``properties``]
      :type: (object)
      
      Object with one or more key-value pairs to map new theme property keys to internal Thunderbird CSS property variables. The new property key is usable as a property reference in :ref:`theme.ThemeType`. Example: 
      
      .. literalinclude:: includes/theme/theme_experiment_property.json
        :language: JSON
      
      
   
   
   .. api-member::
      :name: [``stylesheet``]
      :type: (string)
      
      URL to a stylesheet introducing additional CSS variables, extending the theme-able areas of Thunderbird. The `theme_experiment add-on in our example repository <https://github.com/thundernest/sample-extensions/tree/master/theme_experiment>`__ is using the stylesheet shown below, to add the ``--chat-button-color`` CSS color variable: 
      
      .. literalinclude:: includes/theme/theme_experiment_style.css
        :language: CSS
      
      The following ``manifest.json`` file maps the ``--chat-button-color`` CSS color variable to the theme color key ``exp_chat_button`` and uses it to set a color for the chat button: 
      
      .. literalinclude:: includes/theme/theme_experiment_manifest.json
        :language: JSON
      
      
   

.. _theme.ThemeType:

ThemeType
---------

.. api-section-annotation-hack:: 

Contains the color, image and property settings of a theme.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``colors``]
      :type: (object)
      
      Object with one or more key-value pairs to map color values to theme color keys. The following built-in theme color keys are supported:
      
      .. api-member::
         :name: [``button_background_active``]
         :type: (:ref:`theme.ThemeColor`)
         
         The color of the background of the pressed toolbar buttons.
      
      
      .. api-member::
         :name: [``button_background_hover``]
         :type: (:ref:`theme.ThemeColor`)
         
         The color of the background of the toolbar buttons on hover.
      
      
      .. api-member::
         :name: [``frame``]
         :type: (:ref:`theme.ThemeColor`)
         
         The background color of the header area.
      
      
      .. api-member::
         :name: [``frame_inactive``]
         :type: (:ref:`theme.ThemeColor`)
         
         The background color of the header area when the window is inactive.
      
      
      .. api-member::
         :name: [``icons``]
         :type: (:ref:`theme.ThemeColor`)
         
         The color of the toolbar icons. Defaults to the color specified by ``toolbar_text``.
      
      
      .. api-member::
         :name: [``icons_attention``]
         :type: (:ref:`theme.ThemeColor`)
         
         The color of the toolbar icons in attention state such as the chat icon whith new messages.
      
      
      .. api-member::
         :name: [``popup``]
         :type: (:ref:`theme.ThemeColor`)
         
         The background color of popups such as the AppMenu.
      
      
      .. api-member::
         :name: [``popup_border``]
         :type: (:ref:`theme.ThemeColor`)
         
         The border color of popups.
      
      
      .. api-member::
         :name: [``popup_highlight``]
         :type: (:ref:`theme.ThemeColor`)
         
         The background color of items highlighted using the keyboard inside popups.
      
      
      .. api-member::
         :name: [``popup_highlight_text``]
         :type: (:ref:`theme.ThemeColor`)
         
         The text color of items highlighted using the keyboard inside popups.
      
      
      .. api-member::
         :name: [``popup_text``]
         :type: (:ref:`theme.ThemeColor`)
         
         The text color of popups.
      
      
      .. api-member::
         :name: [``sidebar``]
         :type: (:ref:`theme.ThemeColor`)
         
         The background color of the trees.
      
      
      .. api-member::
         :name: [``sidebar_border``]
         :type: (:ref:`theme.ThemeColor`)
         
         The border color of the trees.
      
      
      .. api-member::
         :name: [``sidebar_highlight``]
         :type: (:ref:`theme.ThemeColor`)
         
         The background color of highlighted rows in trees.
      
      
      .. api-member::
         :name: [``sidebar_highlight_border``]
         :type: (:ref:`theme.ThemeColor`)
         :annotation: -- [Added in TB 86, backported to TB 78.7.1]
         
         The border color of highlighted rows in trees.
      
      
      .. api-member::
         :name: [``sidebar_highlight_text``]
         :type: (:ref:`theme.ThemeColor`)
         
         The text color of highlighted rows in trees.
      
      
      .. api-member::
         :name: [``sidebar_text``]
         :type: (:ref:`theme.ThemeColor`)
         
         The text color of the trees. Needed to enable the tree theming.
      
      
      .. api-member::
         :name: [``tab_background_separator``]
         :type: (:ref:`theme.ThemeColor`)
         
         The color of the vertical separator of the background tabs.
      
      
      .. api-member::
         :name: [``tab_background_text``]
         :type: (:ref:`theme.ThemeColor`)
         
         The text color of the unselected tabs.
      
      
      .. api-member::
         :name: [``tab_line``]
         :type: (:ref:`theme.ThemeColor`)
         
         The color of the selected tab line.
      
      
      .. api-member::
         :name: [``tab_loading``]
         :type: (:ref:`theme.ThemeColor`)
         
         The color of the tab loading indicator.
      
      
      .. api-member::
         :name: [``tab_selected``]
         :type: (:ref:`theme.ThemeColor`)
         
         Background color of the selected tab. Defaults to the color specified by ``toolbar``.
      
      
      .. api-member::
         :name: [``tab_text``]
         :type: (:ref:`theme.ThemeColor`)
         
         The text color for the selected tab.  Defaults to the color specified by ``toolbar_text``.
      
      
      .. api-member::
         :name: [``toolbar``]
         :type: (:ref:`theme.ThemeColor`)
         
         The background color of the toolbars. Also used as default value for ``tab_selected``.
      
      
      .. api-member::
         :name: [``toolbar_bottom_separator``]
         :type: (:ref:`theme.ThemeColor`)
         
         The color of the line separating the bottom of the toolbar from the region below.
      
      
      .. api-member::
         :name: [``toolbar_field``]
         :type: (:ref:`theme.ThemeColor`)
         
         The background color for fields in the toolbar, such as the search field.
      
      
      .. api-member::
         :name: [``toolbar_field_border``]
         :type: (:ref:`theme.ThemeColor`)
         
         The border color for fields in the toolbar.
      
      
      .. api-member::
         :name: [``toolbar_field_border_focus``]
         :type: (:ref:`theme.ThemeColor`)
         
         The focused border color for fields in the toolbar.
      
      
      .. api-member::
         :name: [``toolbar_field_focus``]
         :type: (:ref:`theme.ThemeColor`)
         
         The focused background color for fields in the toolbar.
      
      
      .. api-member::
         :name: [``toolbar_field_highlight``]
         :type: (:ref:`theme.ThemeColor`)
         
         The background color used to indicate the current selection of text in the search field.
      
      
      .. api-member::
         :name: [``toolbar_field_highlight_text``]
         :type: (:ref:`theme.ThemeColor`)
         
         The color used to draw text that's currently selected in the search field.
      
      
      .. api-member::
         :name: [``toolbar_field_text``]
         :type: (:ref:`theme.ThemeColor`)
         
         The text color for fields in the toolbar.
      
      
      .. api-member::
         :name: [``toolbar_field_text_focus``]
         :type: (:ref:`theme.ThemeColor`)
         
         The text color in the focused fields in the toolbar.
      
      
      .. api-member::
         :name: [``toolbar_text``]
         :type: (:ref:`theme.ThemeColor`)
         
         The text color in the main Thunderbird toolbar. Also used as default value for ``icons`` and ``tab_text``.
      
      
      .. api-member::
         :name: [``toolbar_top_separator``]
         :type: (:ref:`theme.ThemeColor`)
         
         The color of the line separating the top of the toolbar from the region above.
      
      
      .. api-member::
         :name: [``toolbar_vertical_separator``]
         :type: (:ref:`theme.ThemeColor`)
         
         The color of the vertical separators on the toolbars.
      
   
   
   .. api-member::
      :name: [``images``]
      :type: (object)
      
      Object with one or more key-value pairs to map images to theme image keys. The following built-in theme image keys are supported:
      
      .. api-member::
         :name: [``additional_backgrounds``]
         :type: (array of :ref:`theme.ImageDataOrExtensionURL`)
         
         Additional images added to the header area and displayed behind the 'theme_frame' image.
      
      
      .. api-member::
         :name: [``theme_frame``]
         :type: (:ref:`theme.ImageDataOrExtensionURL`)
         
         Foreground image on the header area.
      
   
   
   .. api-member::
      :name: [``properties``]
      :type: (object)
      
      Object with one or more key-value pairs to map property values to theme property keys. The following built-in theme property keys are supported:
      
      .. api-member::
         :name: [``additional_backgrounds_alignment``]
         :type: (array of `string`)
         
         Supported values:
         
         .. api-member::
            :name: ``bottom``
         
         .. api-member::
            :name: ``center``
         
         .. api-member::
            :name: ``left``
         
         .. api-member::
            :name: ``right``
         
         .. api-member::
            :name: ``top``
         
         .. api-member::
            :name: ``center bottom``
         
         .. api-member::
            :name: ``center center``
         
         .. api-member::
            :name: ``center top``
         
         .. api-member::
            :name: ``left bottom``
         
         .. api-member::
            :name: ``left center``
         
         .. api-member::
            :name: ``left top``
         
         .. api-member::
            :name: ``right bottom``
         
         .. api-member::
            :name: ``right center``
         
         .. api-member::
            :name: ``right top``
      
      
      .. api-member::
         :name: [``additional_backgrounds_tiling``]
         :type: (array of `string`)
         
         Supported values:
         
         .. api-member::
            :name: ``no-repeat``
         
         .. api-member::
            :name: ``repeat``
         
         .. api-member::
            :name: ``repeat-x``
         
         .. api-member::
            :name: ``repeat-y``
      
   

.. _theme.ThemeUpdateInfo:

ThemeUpdateInfo
---------------

.. api-section-annotation-hack:: 

Info provided in the onUpdated listener.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``theme``
      :type: (:ref:`theme.ThemeType`)
      
      The new theme after update
   
   
   .. api-member::
      :name: [``windowId``]
      :type: (integer)
      
      The id of the window the theme has been applied to
   
