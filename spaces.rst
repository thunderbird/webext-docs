.. container:: sticky-sidebar

  ≡ spaces API

  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

==========
spaces API
==========

.. role:: permission

.. role:: value

.. role:: code

The spaces API allows to manage built-in and custom spaces, and to add buttons for custom spaces to Thunderbird's spaces toolbar.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`contextualIdentities`

   Grant access to some or all methods of the contextualIdentities API.

.. api-member::
   :name: :permission:`cookies`

   Grant access to some or all methods of the cookies API.

.. api-member::
   :name: :permission:`management`

   Monitor extension usage and manage themes.

.. rst-class:: api-main-section

Functions
=========

.. _spaces.create:

create(name, tabProperties, [buttonProperties])
-----------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 115]

Creates a new space and adds its button to the spaces toolbar.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``name``
      :type: (string)

      The name to assign to this space. May only contain alphanumeric characters and underscores. Must be unique for this extension.

   .. api-member::
      :name: ``tabProperties``
      :type: (string or :ref:`spaces.^space^tab^properties`)

      The properties for the new tab being opened, when the associated button in the spaces toolbar is clicked. Either a *string* specifying the default URL, or a :ref:`spaces.^space^tab^properties` object. The URL may point to a WebExtension page or a web page.

   .. api-member::
      :name: [``buttonProperties``]
      :type: (:ref:`spaces.^space^button^properties`, optional)

      Properties of the button in the spaces toolbar for the new space.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`spaces.^space`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _spaces.get:

get(spaceId)
------------

.. api-section-annotation-hack:: -- [Added in TB 115]

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
      :type: :ref:`spaces.^space`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _spaces.open:

open(spaceId, [windowId])
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 115]

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
      :type: :ref:`tabs.^tab`

      Details about the opened or activated space tab.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _spaces.query:

query([queryInfo])
------------------

.. api-section-annotation-hack:: -- [Added in TB 115]

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
      :type: array of :ref:`spaces.^space`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _spaces.remove:

remove(spaceId)
---------------

.. api-section-annotation-hack:: -- [Added in TB 115]

Removes the specified space, closes all its tabs and removes its button from the spaces toolbar. Throws an exception if the requested space does not exist or was not created by this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``spaceId``
      :type: (integer)

      The id of the space.

.. _spaces.update:

update(spaceId, tabProperties, [buttonProperties])
--------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 115]

Updates the specified space. Throws an exception if the requested space does not exist or was not created by this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``spaceId``
      :type: (integer)

      The id of the space.

   .. api-member::
      :name: ``tabProperties``
      :type: (string or :ref:`spaces.^space^tab^properties` or :ref:`spaces.^space^button^properties`)

      The properties for the new tab being opened, when the associated button in the spaces toolbar is clicked. Either a *string* specifying the default URL, or a :ref:`spaces.^space^tab^properties` object. The URL may point to a WebExtension page or a web page.

   .. api-member::
      :name: [``buttonProperties``]
      :type: (:ref:`spaces.^space^button^properties`, optional)

      Properties of the button in the spaces toolbar for the specified space Only specified button properties will be updated.

.. rst-class:: api-main-section

Types
=====

.. _spaces.^color^array:

ColorArray
----------

.. api-section-annotation-hack:: -- [Added in TB 115]

An array of four integers in the range [0,255] that make up the RGBA color. For example, opaque red is :value:`[255, 0, 0, 255]`.

.. api-header::
   :label: array of integer

.. _spaces.^extension^file^url:

ExtensionFileUrl
----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string

.. _spaces.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _spaces.^icon^path:

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
   :label: :ref:`spaces.^extension^file^url`

.. _spaces.^space:

Space
-----

.. api-section-annotation-hack:: -- [Added in TB 115]

.. api-header::
   :label: object

   .. _spaces.^space.id:

   .. api-member::
      :name: ``id``
      :type: (integer)

      The id of the space.

   .. _spaces.^space.is^built^in:

   .. api-member::
      :name: ``isBuiltIn``
      :type: (boolean)

      Whether this space is one of the default Thunderbird spaces, or an extension space.

   .. _spaces.^space.is^self^owned:

   .. api-member::
      :name: ``isSelfOwned``
      :type: (boolean)

      Whether this space was created by this extension.

   .. _spaces.^space.name:

   .. api-member::
      :name: ``name``
      :type: (string)

      The name of the space. Names are unique for a single extension, but different extensions may use the same name.

   .. _spaces.^space.extension^id:

   .. api-member::
      :name: [``extensionId``]
      :type: (string, optional)

      The id of the extension which owns the space. The :permission:`management` permission is required to include this property.

.. _spaces.^space^button^properties:

SpaceButtonProperties
---------------------

.. api-section-annotation-hack:: -- [Added in TB 115]

Properties of a button in the spaces toolbar.

.. api-header::
   :label: object

   .. _spaces.^space^button^properties.badge^background^color:

   .. api-member::
      :name: [``badgeBackgroundColor``]
      :type: (string or :ref:`spaces.^color^array`, optional)

      Sets the background color of the badge. Can be specified as an array of four integers in the range [0,255] that make up the RGBA color of the badge. For example, opaque red is :value:`[255, 0, 0, 255]`. Can also be a string with an HTML color name (:value:`red`) or a HEX color value (:value:`#FF0000` or :value:`#F00`). Reset when set to an empty string.

   .. _spaces.^space^button^properties.badge^text:

   .. api-member::
      :name: [``badgeText``]
      :type: (string, optional)

      Sets the badge text for the button in the spaces toolbar. The badge is displayed on top of the icon. Any number of characters can be set, but only about four can fit in the space. Removed when set to an empty string.

   .. _spaces.^space^button^properties.default^icons:

   .. api-member::
      :name: [``defaultIcons``]
      :type: (string or :ref:`spaces.^icon^path`, optional)

      The paths to one or more icons for the button in the spaces toolbar. Reset to the extension icon, when set to an empty string.

   .. _spaces.^space^button^properties.theme^icons:

   .. api-member::
      :name: [``themeIcons``]
      :type: (array of :ref:`spaces.^theme^icons`, optional)

      Specifies dark and light icons for the button in the spaces toolbar to be used with themes: The :value:`light` icons will be used on dark backgrounds and vice versa. At least the set for *16px* icons should be specified. The set for *32px* icons will be used on screens with a very high pixel density, if specified. Reset when set to an empty array.

   .. _spaces.^space^button^properties.title:

   .. api-member::
      :name: [``title``]
      :type: (string, optional)

      The title for the button in the spaces toolbar, used in the tooltip of the button and as the displayed name in the overflow menu. Reset to the name of the extension, when set to an empty string.

.. _spaces.^space^tab^properties:

SpaceTabProperties
------------------

.. api-section-annotation-hack:: -- [Added in TB 135]

Properties for the new tab being opened by clicking on the associated button in the spaces toolbar.

.. api-header::
   :label: object

   .. _spaces.^space^tab^properties.cookie^store^id:

   .. api-member::
      :name: [``cookieStoreId``]
      :type: (string, optional)

      The `CookieStore <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities/ContextualIdentity#cookiestoreid>`__ id used by the tab. Either a custom id created using the `contextualIdentities API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contextualIdentities>`__, or a built-in one: :value:`firefox-default`, :value:`firefox-container-1`, :value:`firefox-container-2`, :value:`firefox-container-3`, :value:`firefox-container-4`, :value:`firefox-container-5`.

      .. note::

         The naming pattern of the built-in cookie stores was deliberately not changed for Thunderbird, but kept for compatibility reasons.

      .. note::

          The :permission:`cookies` permission is required to be able to specify this property. Furthermore, the :permission:`contextualIdentities` permission should be requested, to enable the contextual identities feature (enabled by default only on Thunderbird Daily).

   .. _spaces.^space^tab^properties.link^handler:

   .. api-member::
      :name: [``linkHandler``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 136]

      Thunderbird is a mail client, not a browser. It is possible to load a web page, but opening follow-up pages through hyperlinks should be handled by the user's default browser. This property specifies to what extent this behavior should be enforced. The default :value:`balanced` link handler will open links to the same host directly in Thunderbird, everything else will be opened in the user's default browser. A :value:`relaxed` link handler will open all links inside of Thunderbird, a :value:`strict` link handler will open all links in the user's default browser, except links to the same page.

      Supported values:

      .. api-member::
         :name: :value:`balanced`

      .. api-member::
         :name: :value:`relaxed`

      .. api-member::
         :name: :value:`strict`

   .. _spaces.^space^tab^properties.url:

   .. api-member::
      :name: [``url``]
      :type: (string, optional)

      The default URL. May point to a WebExtension page or a web page.

.. _spaces.^theme^icons:

ThemeIcons
----------

.. api-section-annotation-hack:: 

Define a set of icons for themes depending on whether Thunderbird detects that the theme uses dark or light text. All provided URLs must be relative to the :value:`manifest.json` file.

.. api-header::
   :label: object

   .. _spaces.^theme^icons.dark:

   .. api-member::
      :name: ``dark``
      :type: (:ref:`spaces.^extension^u^r^l`)

      The dark icon to use for light themes

   .. _spaces.^theme^icons.light:

   .. api-member::
      :name: ``light``
      :type: (:ref:`spaces.^extension^u^r^l`)

      A light icon to use for dark themes

   .. _spaces.^theme^icons.size:

   .. api-member::
      :name: ``size``
      :type: (integer)

      The size of the icons
