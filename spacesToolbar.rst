.. _spacesToolbar_api:

=============
spacesToolbar
=============

The spacesToolbar API first appeared in Thunderbird 100. It allows to add buttons to Thunderbird's spaces toolbar.
These buttons are shortcuts to open html pages in a new tab.

.. warning::

  This API will change in future releases of Thunderbird.

.. role:: permission

.. rst-class:: api-main-section

Functions
=========

.. _spacesToolbar.addButton:

addButton(id, properties)
-------------------------

.. api-section-annotation-hack:: 

Adds a new button to the spaces toolbar. Throws an exception, if the used ``id`` is not unique within the extension.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
      
      The unique id to assign to this button. May only contain alphanumeric characters and underscores.
   
   
   .. api-member::
      :name: ``properties``
      :type: (:ref:`spacesToolbar.ButtonProperties`)
      
      Properties of the new button. The ``url`` is mandatory.
   

.. _spacesToolbar.removeButton:

removeButton(id)
----------------

.. api-section-annotation-hack:: 

Removes the specified button from the spaces toolbar. Throws an exception if the requested spaces toolbar button does not exist. If the tab of this button is currently open, it will be closed.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
      
      The id of the button which is to be removed. May only contain alphanumeric characters and underscores.
   

.. _spacesToolbar.updateButton:

updateButton(id, properties)
----------------------------

.. api-section-annotation-hack:: 

Updates properties of the specified spaces toolbar button. Throws an exception if the requested spaces toolbar button does not exist.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``id``
      :type: (string)
      
      The id of the button which is to be updated. May only contain alphanumeric characters and underscores.
   
   
   .. api-member::
      :name: ``properties``
      :type: (:ref:`spacesToolbar.ButtonProperties`)
      
      Only specified properties will be updated.
   

.. rst-class:: api-main-section

Types
=====

.. _spacesToolbar.ButtonProperties:

ButtonProperties
----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``badgeBackgroundColor``]
      :type: (string or :ref:`spacesToolbar.ColorArray`)
      
      Sets the background color of the badge. Can be specified as an array of four integers in the range [0,255] that make up the RGBA color of the badge. For example, opaque red is ``[255, 0, 0, 255]``. Can also be a string with an HTML color name (``red``) or a HEX color value (``#FF0000`` or ``#F00``). Reset when set to an empty string.
   
   
   .. api-member::
      :name: [``badgeText``]
      :type: (string)
      
      Sets the badge text for the spaces toolbar button. The badge is displayed on top of the icon. Any number of characters can be set, but only about four can fit in the space. Removed when set to an empty string.
   
   
   .. api-member::
      :name: [``defaultIcons``]
      :type: (string or :ref:`spacesToolbar.IconPathDictionary`)
      
      Either a relative image path defining a single icon used for all sizes or an IconPathDictionary object defining dedicated icons for different sizes. At least the ``16px`` icon should be specified. The ``32px`` icon will be used on screens with a very high pixel density, if specified. Defaults to the extension icon, if set to an empty string.
   
   
   .. api-member::
      :name: [``themeIcons``]
      :type: (array of :ref:`spacesToolbar.ThemeIcons`)
      
      Specifies dark and light icons for the spaces toolbar button to be used with themes: The ``light`` icons will be used on dark backgrounds and vice versa. At least the set for ``16px`` icons should be specified. The set for ``32px`` icons will be used on screens with a very high pixel density, if specified.
   
   
   .. api-member::
      :name: [``title``]
      :type: (string)
      
      The title for the spaces toolbar button, used in the tooltip of the button and as the displayed name in the overflow menu. Defaults to the name of the extension, if set to an empty string.
   
   
   .. api-member::
      :name: [``url``]
      :type: (string)
      
      The page url, loaded into a tab when the button is clicked. Supported are ``https://`` and ``http://`` links, as well as links to WebExtension pages.
   

.. _spacesToolbar.ColorArray:

ColorArray
----------

.. api-section-annotation-hack:: 

An array of four integers in the range [0,255] that make up the RGBA color. For example, opaque red is ``[255, 0, 0, 255]``.

.. api-header::
   :label: array of integer

.. rst-class:: api-main-section

External Types
==============

The following types are not defined by this API, but by the underlying Mozilla WebExtension code base. They are included here, because there is no other public documentation available.

.. _spacesToolbar.IconPathDictionary:

IconPathDictionary
------------------

.. api-section-annotation-hack:: 

A ``{size: path}`` dictionary representing the icon to be set. The actual image to be used is chosen depending on the screen's pixel density. See the  `MDN documentation about choosing icon sizes <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action#choosing_icon_sizes>`__ for more information on this. At least one icon must be specified. Example: 

.. literalinclude:: includes/IconPath.json
  :language: JSON

.. _spacesToolbar.ThemeIcons:

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
   
