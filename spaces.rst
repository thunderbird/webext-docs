==========
spaces API
==========

The spaces API first appeared in Thunderbird 115. It allows to manage built-in and custom spaces, and to add buttons for custom spaces to Thunderbird's spaces toolbar.

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Functions
=========

.. _spaces.create:

create(name, defaultUrl, [buttonProperties])
--------------------------------------------

.. api-section-annotation-hack:: 

Creates a new space and adds its button to the spaces toolbar.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      The name to assign to this space. May only contain alphanumeric characters and underscores. Must be unique for this extension.
   
   
   .. api-member::
      :name: ``defaultUrl``
      :type: (string)
      
      The default space url, loaded into a tab when the button in the spaces toolbar is clicked. Supported are :value:`https://` and :value:`http://` links, as well as links to WebExtension pages.
   
   
   .. api-member::
      :name: [``buttonProperties``]
      :type: (:ref:`spaces.SpaceButtonProperties`, optional)
      
      Properties of the button for the new space.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`spaces.Space`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _spaces.get:

get(spaceId)
------------

.. api-section-annotation-hack:: 

Retrieves details about the specified space.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``spaceId``
      :type: (integer)
      
      The id of the space.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`spaces.Space`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _spaces.open:

open(spaceId, [windowId])
-------------------------

.. api-section-annotation-hack:: 

Opens or switches to the specified space. Throws an exception if the requested space does not exist or was not created by this extension.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``spaceId``
      :type: (integer)
      
      The id of the space.
   
   
   .. api-member::
      :name: [``windowId``]
      :type: (integer, optional)
      
      The id of the normal window, where the space should be opened. Defaults to the most recent normal window.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`tabs.Tab`
      
      Details about the opened or activated space tab.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _spaces.query:

query([queryInfo])
------------------

.. api-section-annotation-hack:: 

Gets all spaces that have the specified properties, or all spaces if no properties are specified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``queryInfo``]
      :type: (object, optional)
      
      .. api-member::
         :name: [``extensionId``]
         :type: (string, optional)
         
         Id of the extension which should own the spaces. The :permission:`management` permission is required to be able to match against extension ids.
      
      
      .. api-member::
         :name: [``id``]
         :type: (integer, optional)
         
         The id of the space.
      
      
      .. api-member::
         :name: [``isBuiltIn``]
         :type: (boolean, optional)
         
         Spaces should be default Thunderbird spaces.
      
      
      .. api-member::
         :name: [``isSelfOwned``]
         :type: (boolean, optional)
         
         Spaces should have been created by this extension.
      
      
      .. api-member::
         :name: [``name``]
         :type: (string, optional)
         
         The name of the spaces (names are not unique).
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`spaces.Space`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _spaces.remove:

remove(spaceId)
---------------

.. api-section-annotation-hack:: 

Removes the specified space, closes all its tabs and removes its button from the spaces toolbar. Throws an exception if the requested space does not exist or was not created by this extension.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``spaceId``
      :type: (integer)
      
      The id of the space.
   

.. _spaces.update:

update(spaceId, [defaultUrl], [buttonProperties])
-------------------------------------------------

.. api-section-annotation-hack:: 

Updates the specified space. Throws an exception if the requested space does not exist or was not created by this extension.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``spaceId``
      :type: (integer)
      
      The id of the space.
   
   
   .. api-member::
      :name: [``defaultUrl``]
      :type: (string, optional)
      
      The default space url, loaded into a tab when the button in the spaces toolbar is clicked. Supported are :value:`https://` and :value:`http://` links, as well as links to WebExtension pages.
   
   
   .. api-member::
      :name: [``buttonProperties``]
      :type: (:ref:`spaces.SpaceButtonProperties`, optional)
      
      Only specified button properties will be updated.
   

.. rst-class:: api-main-section

Types
=====

.. _spaces.ColorArray:

ColorArray
----------

.. api-section-annotation-hack:: 

An array of four integers in the range [0,255] that make up the RGBA color. For example, opaque red is :value:`[255, 0, 0, 255]`.

.. api-header::
   :label: array of integer

.. _spaces.Space:

Space
-----

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``id``
      :type: (integer)
      
      The id of the space.
   
   
   .. api-member::
      :name: ``isBuiltIn``
      :type: (boolean)
      
      Whether this space is one of the default Thunderbird spaces, or an extension space.
   
   
   .. api-member::
      :name: ``isSelfOwned``
      :type: (boolean)
      
      Whether this space was created by this extension.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      The name of the space. Names are unique for a single extension, but different extensions may use the same name.
   
   
   .. api-member::
      :name: [``extensionId``]
      :type: (string, optional)
      
      The id of the extension which owns the space. The :permission:`management` permission is required to include this property.
   

.. _spaces.SpaceButtonProperties:

SpaceButtonProperties
---------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``badgeBackgroundColor``]
      :type: (string or :ref:`spaces.ColorArray`, optional)
      
      Sets the background color of the badge. Can be specified as an array of four integers in the range [0,255] that make up the RGBA color of the badge. For example, opaque red is :value:`[255, 0, 0, 255]`. Can also be a string with an HTML color name (:value:`red`) or a HEX color value (:value:`#FF0000` or :value:`#F00`). Reset when set to an empty string.
   
   
   .. api-member::
      :name: [``badgeText``]
      :type: (string, optional)
      
      Sets the badge text for the button in the spaces toolbar. The badge is displayed on top of the icon. Any number of characters can be set, but only about four can fit in the space. Removed when set to an empty string.
   
   
   .. api-member::
      :name: [``defaultIcons``]
      :type: (string or :ref:`spaces.IconPath`, optional)
      
      The paths to one or more icons for the button in the spaces toolbar. Defaults to the extension icon, if set to an empty string.
   
   
   .. api-member::
      :name: [``themeIcons``]
      :type: (array of :ref:`spaces.ThemeIcons`, optional)
      
      Specifies dark and light icons for the button in the spaces toolbar to be used with themes: The ``light`` icons will be used on dark backgrounds and vice versa. At least the set for *16px* icons should be specified. The set for *32px* icons will be used on screens with a very high pixel density, if specified.
   
   
   .. api-member::
      :name: [``title``]
      :type: (string, optional)
      
      The title for the button in the spaces toolbar, used in the tooltip of the button and as the displayed name in the overflow menu. Defaults to the name of the extension, if set to an empty string.
   

.. rst-class:: api-main-section

External Types
==============

The following types are not defined by this API, but by the underlying Mozilla WebExtension code base. They are included here, because there is no other public documentation available.

.. _spaces.IconPath:

IconPath
--------

.. api-section-annotation-hack:: 

Either a *string* to specify a relative path of a single icon to be used for all sizes, or a *dictionary object* to specify paths for multiple icons in different sizes, so the icon does not have to be scaled for a device with a different pixel density. Each entry is a *name-value* pair with *value* being a relative path to an icon file, and *name* its size. Example: 

.. literalinclude:: includes/IconPath.json
  :language: JSON

See the `MDN documentation about choosing icon sizes <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/browser_action#choosing_icon_sizes>`__ for more information on this.

.. _spaces.ThemeIcons:

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
   
