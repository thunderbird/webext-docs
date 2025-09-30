.. container:: sticky-sidebar

  ≡ management API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

==============
management API
==============

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The management API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/management>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

The :code:`browser.management` API provides ways to manage the list of extensions that are installed and running.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`management`

   Monitor extension usage and manage themes.

.. rst-class:: api-main-section

Functions
=========

.. _management.get:

get(id)
-------

.. api-section-annotation-hack:: -- [Added in TB 56]

Returns information about the installed extension that has the given ID.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (:ref:`management.^extension^i^d`)

      The ID from an item of :ref:`management.^extension^info`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`management.^extension^info`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.get^all:

getAll()
--------

.. api-section-annotation-hack:: -- [Added in TB 55]

Returns a list of information about installed extensions.

.. note::

   Before version 56, only extensions whose 'type' is 'theme' are returned.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`management.^extension^info`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.get^self:

getSelf()
---------

.. api-section-annotation-hack:: -- [Added in TB 51]

Returns information about the calling extension. Note: This function can be used without requesting the 'management' permission in the manifest.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`management.^extension^info`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _management.install:

install(options)
----------------

.. api-section-annotation-hack:: -- [Added in TB 63]

Installs and enables a theme extension from the given url.

.. note::

   The installable file pointed to by :code:`url` must be a `theme <https://developer.mozilla.org/docs/Mozilla/Add-ons/Themes>`__, and not a normal browser extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (object)

      .. api-member::
         :name: ``url``
         :type: (:ref:`management.^http^u^r^l`)

         URL pointing to the XPI file on addons.mozilla.org or similar.

      .. api-member::
         :name: [``hash``]
         :type: (string, optional)

         A hash of the XPI file, using sha256 or stronger.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: object

      .. api-member::
         :name: ``id``
         :type: (:ref:`management.^extension^i^d`)

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.set^enabled:

setEnabled(id, enabled)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 55]

Enables or disables the given add-on.

.. note::

   Only extensions whose 'type' is 'theme' can be enabled and disabled.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``id``
      :type: (string)

      ID of the add-on to enable/disable.

   .. api-member::
      :name: ``enabled``
      :type: (boolean)

      Whether to enable or disable the add-on.

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.uninstall^self:

uninstallSelf([options])
------------------------

.. api-section-annotation-hack:: -- [Added in TB 51]

Uninstalls the calling extension. Note: This function can be used without requesting the 'management' permission in the manifest.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``options``]
      :type: (object, optional)

      .. api-member::
         :name: [``dialogMessage``]
         :type: (string, optional)

         The message to display to a user when being asked to confirm removal of the extension.

      .. api-member::
         :name: [``showConfirmDialog``]
         :type: (boolean, optional)

         Whether or not a confirm-uninstall dialog should prompt the user. Defaults to false.

.. rst-class:: api-main-section

Events
======

.. _management.on^disabled:

onDisabled
----------

.. api-section-annotation-hack:: -- [Added in TB 55]

Fired when an addon has been disabled.

.. note::

   Before version 56, only extensions whose :code:`type` is :code:`'theme'` are supported.

.. api-header::
   :label: Parameters for onDisabled.addListener(listener)

   .. api-member::
      :name: ``listener(info)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``info``
      :type: (:ref:`management.^extension^info`)

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.on^enabled:

onEnabled
---------

.. api-section-annotation-hack:: -- [Added in TB 55]

Fired when an addon has been enabled.

.. note::

   Before version 56, only extensions whose :code:`type` is :code:`'theme'` are supported.

.. api-header::
   :label: Parameters for onEnabled.addListener(listener)

   .. api-member::
      :name: ``listener(info)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``info``
      :type: (:ref:`management.^extension^info`)

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.on^installed:

onInstalled
-----------

.. api-section-annotation-hack:: -- [Added in TB 55]

Fired when an addon has been installed.

.. note::

   Before version 56, only extensions whose :code:`type` is :code:`'theme'` are supported.

.. api-header::
   :label: Parameters for onInstalled.addListener(listener)

   .. api-member::
      :name: ``listener(info)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``info``
      :type: (:ref:`management.^extension^info`)

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.on^uninstalled:

onUninstalled
-------------

.. api-section-annotation-hack:: -- [Added in TB 55]

Fired when an addon has been uninstalled.

.. note::

   Before version 56, only extensions whose :code:`type` is :code:`'theme'` are supported.

.. note::

   This event is not fired when the extension is in the "pending uninstall" state. The event is fired as expected once the extension is completely removed (for example, when the :code:`about:addons` tab is closed).

.. api-header::
   :label: Parameters for onUninstalled.addListener(listener)

   .. api-member::
      :name: ``listener(info)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``info``
      :type: (:ref:`management.^extension^info`)

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. rst-class:: api-main-section

Types
=====

.. _management.^extension^disabled^reason:

ExtensionDisabledReason
-----------------------

.. api-section-annotation-hack:: 

A reason the item is disabled.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`permissions_increase`

         .. api-member::
            :name: :value:`unknown`

.. _management.^extension^i^d:

ExtensionID
-----------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string

*or*

.. api-header::
   :label: string

.. _management.^extension^info:

ExtensionInfo
-------------

.. api-section-annotation-hack:: -- [Added in TB 51]

Information about an installed extension.

.. api-header::
   :label: object

   .. _management.^extension^info.description:

   .. api-member::
      :name: ``description``
      :type: (string)

      The description of this extension.

   .. _management.^extension^info.enabled:

   .. api-member::
      :name: ``enabled``
      :type: (boolean)

      Whether it is currently enabled or disabled.

   .. _management.^extension^info.id:

   .. api-member::
      :name: ``id``
      :type: (string)

      The extension's unique identifier.

   .. _management.^extension^info.install^type:

   .. api-member::
      :name: ``installType``
      :type: (:ref:`management.^extension^install^type`)

      How the extension was installed.

   .. _management.^extension^info.may^disable:

   .. api-member::
      :name: ``mayDisable``
      :type: (boolean)

      Whether this extension can be disabled or uninstalled by the user.

   .. _management.^extension^info.name:

   .. api-member::
      :name: ``name``
      :type: (string)

      The name of this extension.

   .. _management.^extension^info.options^url:

   .. api-member::
      :name: ``optionsUrl``
      :type: (string)

      The url for the item's options page, if it has one.

   .. _management.^extension^info.type:

   .. api-member::
      :name: ``type``
      :type: (:ref:`management.^extension^type`)
      :annotation: -- [Added in TB 55]

      The type of this extension, 'extension' or 'theme'.

   .. _management.^extension^info.version:

   .. api-member::
      :name: ``version``
      :type: (string)

      The `version <manifest/version>`__ of this extension.

   .. _management.^extension^info.disabled^reason:

   .. api-member::
      :name: [``disabledReason``]
      :type: (:ref:`management.^extension^disabled^reason`, optional)

      A reason the item is disabled.

   .. _management.^extension^info.homepage^url:

   .. api-member::
      :name: [``homepageUrl``]
      :type: (string, optional)

      The URL of the homepage of this extension.

   .. _management.^extension^info.host^permissions:

   .. api-member::
      :name: [``hostPermissions``]
      :type: (array of string, optional)

      Returns a list of host based permissions.

   .. _management.^extension^info.icons:

   .. api-member::
      :name: [``icons``]
      :type: (array of :ref:`management.^icon^info`, optional)

      A list of icon information. Note that this just reflects what was declared in the manifest, and the actual image at that url may be larger or smaller than what was declared, so you might consider using explicit width and height attributes on img tags referencing these images. See the `manifest documentation on icons <manifest/icons>`__ for more details.

   .. _management.^extension^info.permissions:

   .. api-member::
      :name: [``permissions``]
      :type: (array of string, optional)

      Returns a list of API based permissions.

   .. _management.^extension^info.short^name:

   .. api-member::
      :name: [``shortName``]
      :type: (string, optional)

      A short version of the name of this extension.

   .. _management.^extension^info.update^url:

   .. api-member::
      :name: [``updateUrl``]
      :type: (string, optional)

      The update URL of this extension.

   .. _management.^extension^info.version^name:

   .. api-member::
      :name: [``versionName``]
      :type: (string, optional)

      The `version name <manifest/version#version_name>`__ of this extension if the manifest specified one.

.. _management.^extension^install^type:

ExtensionInstallType
--------------------

.. api-section-annotation-hack:: 

How the extension was installed. One of :value:`development`: The extension was loaded unpacked in developer mode, :value:`normal`: The extension was installed normally via an .xpi file, :value:`sideload`: The extension was installed by other software on the machine, :value:`admin`: The extension was installed by policy, :value:`other`: The extension was installed by other means.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`admin`

         .. api-member::
            :name: :value:`development`

         .. api-member::
            :name: :value:`normal`

         .. api-member::
            :name: :value:`other`

         .. api-member::
            :name: :value:`sideload`

.. _management.^extension^type:

ExtensionType
-------------

.. api-section-annotation-hack:: 

The type of this extension, 'extension' or 'theme'.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`extension`

         .. api-member::
            :name: :value:`theme`

.. _management.^http^u^r^l:

HttpURL
-------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string

.. _management.^icon^info:

IconInfo
--------

.. api-section-annotation-hack:: 

Information about an icon belonging to an extension.

.. api-header::
   :label: object

   .. _management.^icon^info.size:

   .. api-member::
      :name: ``size``
      :type: (integer)

      A number representing the width and height of the icon. Likely values include (but are not limited to) 128, 48, 24, and 16.

   .. _management.^icon^info.url:

   .. api-member::
      :name: ``url``
      :type: (string)

      The URL for this icon image. To display a grayscale version of the icon (to indicate that an extension is disabled, for example), append :code:`?grayscale=true` to the URL.
