.. container:: sticky-sidebar

  ≡ management API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

==============
management API
==============

.. role:: permission

.. role:: value

.. role:: code

The <code>browser.management</code> API provides ways to manage the list of extensions that are installed and running.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`management`

   Monitor extension usage and manage themes

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
      :type: (:ref:`management.ExtensionID`)

      The ID from an item of :ref:`management.ExtensionInfo`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`management.ExtensionInfo`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.getAll:

getAll()
--------

.. api-section-annotation-hack:: -- [Added in TB 55]

Returns a list of information about installed extensions.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`management.ExtensionInfo`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.getSelf:

getSelf()
---------

.. api-section-annotation-hack:: -- [Added in TB 51]

Returns information about the calling extension. Note: This function can be used without requesting the 'management' permission in the manifest.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`management.ExtensionInfo`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _management.install:

install(options)
----------------

.. api-section-annotation-hack:: -- [Added in TB 63]

Installs and enables a theme extension from the given url.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (object)

      .. api-member::
         :name: ``url``
         :type: (:ref:`management.HttpURL`)

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
         :type: (:ref:`management.ExtensionID`)

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.setEnabled:

setEnabled(id, enabled)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 55]

Enables or disables the given add-on.

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

.. _management.uninstallSelf:

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

.. _management.onDisabled:

onDisabled
----------

.. api-section-annotation-hack:: -- [Added in TB 55]

Fired when an addon has been disabled.

.. api-header::
   :label: Parameters for onDisabled.addListener(listener)

   .. api-member::
      :name: ``listener(info)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``info``
      :type: (:ref:`management.ExtensionInfo`)

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.onEnabled:

onEnabled
---------

.. api-section-annotation-hack:: -- [Added in TB 55]

Fired when an addon has been enabled.

.. api-header::
   :label: Parameters for onEnabled.addListener(listener)

   .. api-member::
      :name: ``listener(info)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``info``
      :type: (:ref:`management.ExtensionInfo`)

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.onInstalled:

onInstalled
-----------

.. api-section-annotation-hack:: -- [Added in TB 55]

Fired when an addon has been installed.

.. api-header::
   :label: Parameters for onInstalled.addListener(listener)

   .. api-member::
      :name: ``listener(info)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``info``
      :type: (:ref:`management.ExtensionInfo`)

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. _management.onUninstalled:

onUninstalled
-------------

.. api-section-annotation-hack:: -- [Added in TB 55]

Fired when an addon has been uninstalled.

.. api-header::
   :label: Parameters for onUninstalled.addListener(listener)

   .. api-member::
      :name: ``listener(info)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``info``
      :type: (:ref:`management.ExtensionInfo`)

.. api-header::
   :label: Required permissions

   - :permission:`management`

.. rst-class:: api-main-section

Types
=====

.. _management.ExtensionDisabledReason:

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
            :name: :value:`unknown`

         .. api-member::
            :name: :value:`permissions_increase`

.. _management.ExtensionInfo:

ExtensionInfo
-------------

.. api-section-annotation-hack:: -- [Added in TB 51]

Information about an installed extension.

.. api-header::
   :label: object

   .. api-member::
      :name: ``description``
      :type: (string)

      The description of this extension.

   .. api-member::
      :name: ``enabled``
      :type: (boolean)

      Whether it is currently enabled or disabled.

   .. api-member::
      :name: ``id``
      :type: (string)

      The extension's unique identifier.

   .. api-member::
      :name: ``installType``
      :type: (:ref:`management.ExtensionInstallType`)

      How the extension was installed.

   .. api-member::
      :name: ``mayDisable``
      :type: (boolean)

      Whether this extension can be disabled or uninstalled by the user.

   .. api-member::
      :name: ``name``
      :type: (string)

      The name of this extension.

   .. api-member::
      :name: ``optionsUrl``
      :type: (string)

      The url for the item's options page, if it has one.

   .. api-member::
      :name: ``type``
      :type: (:ref:`management.ExtensionType`)
      :annotation: -- [Added in TB 55]

      The type of this extension, 'extension' or 'theme'.

   .. api-member::
      :name: ``version``
      :type: (string)

      The `version <manifest/version>`__ of this extension.

   .. api-member::
      :name: [``disabledReason``]
      :type: (:ref:`management.ExtensionDisabledReason`, optional)

      A reason the item is disabled.

   .. api-member::
      :name: [``homepageUrl``]
      :type: (string, optional)

      The URL of the homepage of this extension.

   .. api-member::
      :name: [``hostPermissions``]
      :type: (array of string, optional)

      Returns a list of host based permissions.

   .. api-member::
      :name: [``icons``]
      :type: (array of :ref:`management.IconInfo`, optional)

      A list of icon information. Note that this just reflects what was declared in the manifest, and the actual image at that url may be larger or smaller than what was declared, so you might consider using explicit width and height attributes on img tags referencing these images. See the `manifest documentation on icons <manifest/icons>`__ for more details.

   .. api-member::
      :name: [``permissions``]
      :type: (array of string, optional)

      Returns a list of API based permissions.

   .. api-member::
      :name: [``shortName``]
      :type: (string, optional)

      A short version of the name of this extension.

   .. api-member::
      :name: [``updateUrl``]
      :type: (string, optional)

      The update URL of this extension.

   .. api-member::
      :name: [``versionName``]
      :type: (string, optional)

      The `version name <manifest/version#version_name>`__ of this extension if the manifest specified one.

.. _management.ExtensionInstallType:

ExtensionInstallType
--------------------

.. api-section-annotation-hack:: 

How the extension was installed. One of<br>:value:`development`: The extension was loaded unpacked in developer mode,<br>:value:`normal`: The extension was installed normally via an .xpi file,<br>:value:`sideload`: The extension was installed by other software on the machine,<br>:value:`admin`: The extension was installed by policy,<br>:value:`other`: The extension was installed by other means.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`development`

         .. api-member::
            :name: :value:`normal`

         .. api-member::
            :name: :value:`sideload`

         .. api-member::
            :name: :value:`admin`

         .. api-member::
            :name: :value:`other`

.. _management.ExtensionType:

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

.. _management.IconInfo:

IconInfo
--------

.. api-section-annotation-hack:: 

Information about an icon belonging to an extension.

.. api-header::
   :label: object

   .. api-member::
      :name: ``size``
      :type: (integer)

      A number representing the width and height of the icon. Likely values include (but are not limited to) 128, 48, 24, and 16.

   .. api-member::
      :name: ``url``
      :type: (string)

      The URL for this icon image. To display a grayscale version of the icon (to indicate that an extension is disabled, for example), append :code:`?grayscale=true` to the URL.

.. _management.ExtensionID:

ExtensionID
-----------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string

OR

.. api-header::
   :label: string

.. _management.HttpURL:

HttpURL
-------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string
