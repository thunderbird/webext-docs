.. container:: sticky-sidebar

  ≡ notifications API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=================
notifications API
=================

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The notifications API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/notifications>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`notifications`

   Display notifications to you

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`notifications` is required to use ``messenger.notifications.*``.

.. rst-class:: api-main-section

Functions
=========

.. _notifications.clear:

clear(notificationId)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Clears an existing notification.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``notificationId``
      :type: (string)

      The id of the notification to be updated.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: boolean

      Indicates whether a matching notification existed.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.create:

create([notificationId], options)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Creates and displays a notification.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``notificationId``]
      :type: (string, optional)

      Identifier of the notification. If it is empty, this method generates an id. If it matches an existing notification, this method first clears that notification before proceeding with the create operation.

   .. api-member::
      :name: ``options``
      :type: (:ref:`notifications.CreateNotificationOptions`)

      Contents of the notification.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string

      The notification id (either supplied or generated) that represents the created notification.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.getAll:

getAll()
--------

.. api-section-annotation-hack:: -- [Added in TB 45]

Retrieves all the notifications.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: object

      The set of notifications currently in the system.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.getPermissionLevel:

getPermissionLevel()
--------------------

.. api-section-annotation-hack:: 

Retrieves whether the user has enabled notifications from this app or extension.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`notifications.PermissionLevel`

      The current permission level.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. rst-class:: api-main-section

Events
======

.. _notifications.onClicked:

onClicked
---------

.. api-section-annotation-hack:: -- [Added in TB 47]

Fired when the user clicked in a non-button area of the notification.

.. api-header::
   :label: Parameters for onClicked.addListener(listener)

   .. api-member::
      :name: ``listener(notificationId)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``notificationId``
      :type: (string)

      The notificationId of the clicked notification.

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.onClosed:

onClosed
--------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when the notification closed, either by the system or by user action.

.. api-header::
   :label: Parameters for onClosed.addListener(listener)

   .. api-member::
      :name: ``listener(notificationId, byUser)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``notificationId``
      :type: (string)

      The notificationId of the closed notification.

   .. api-member::
      :name: ``byUser``
      :type: (boolean)

      True if the notification was closed by the user.

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.onPermissionLevelChanged:

onPermissionLevelChanged
------------------------

.. api-section-annotation-hack:: 

Fired when the user changes the permission level.

.. api-header::
   :label: Parameters for onPermissionLevelChanged.addListener(listener)

   .. api-member::
      :name: ``listener(level)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``level``
      :type: (:ref:`notifications.PermissionLevel`)

      The new permission level.

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.onShown:

onShown
-------

.. api-section-annotation-hack:: -- [Added in TB 56]

Fired when the notification is shown.

.. api-header::
   :label: Parameters for onShown.addListener(listener)

   .. api-member::
      :name: ``listener(notificationId)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``notificationId``
      :type: (string)

      The notificationId of the shown notification.

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.onShowSettings:

onShowSettings
--------------

.. api-section-annotation-hack:: 

Fired when the user clicked on a link for the app's notification settings.

.. api-header::
   :label: Parameters for onShowSettings.addListener(listener)

   .. api-member::
      :name: ``listener()``

      A function that will be called when this event occurs.

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. rst-class:: api-main-section

Types
=====

.. _notifications.CreateNotificationOptions:

CreateNotificationOptions
-------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _notifications.CreateNotificationOptions.message:

   .. api-member::
      :name: ``message``
      :type: (string)

      Main notification content.

   .. _notifications.CreateNotificationOptions.title:

   .. api-member::
      :name: ``title``
      :type: (string)

      Title of the notification (e.g. sender name for email).

   .. _notifications.CreateNotificationOptions.type:

   .. api-member::
      :name: ``type``
      :type: (:ref:`notifications.TemplateType`)

      Which type of notification to display.

   .. _notifications.CreateNotificationOptions.appIconMaskUrl:

   .. api-member::
      :name: [``appIconMaskUrl``]
      :type: (string, optional)

      A URL to the app icon mask.

   .. _notifications.CreateNotificationOptions.buttons:

   .. api-member::
      :name: [``buttons``]
      :type: (array of object, optional) **Unsupported.**

      Text and icons for up to two notification action buttons.

   .. _notifications.CreateNotificationOptions.contextMessage:

   .. api-member::
      :name: [``contextMessage``]
      :type: (string, optional)

      Alternate notification content with a lower-weight font.

   .. _notifications.CreateNotificationOptions.eventTime:

   .. api-member::
      :name: [``eventTime``]
      :type: (number, optional)

      A timestamp associated with the notification, in milliseconds past the epoch.

   .. _notifications.CreateNotificationOptions.iconUrl:

   .. api-member::
      :name: [``iconUrl``]
      :type: (string, optional)

      A URL to the sender's avatar, app icon, or a thumbnail for image notifications.

   .. _notifications.CreateNotificationOptions.imageUrl:

   .. api-member::
      :name: [``imageUrl``]
      :type: (string, optional)

      A URL to the image thumbnail for image-type notifications.

   .. _notifications.CreateNotificationOptions.isClickable:

   .. api-member::
      :name: [``isClickable``]
      :type: (boolean, optional)

      Whether to show UI indicating that the app will visibly respond to clicks on the body of a notification.

   .. _notifications.CreateNotificationOptions.items:

   .. api-member::
      :name: [``items``]
      :type: (array of :ref:`notifications.NotificationItem`, optional)

      Items for multi-item notifications.

   .. _notifications.CreateNotificationOptions.priority:

   .. api-member::
      :name: [``priority``]
      :type: (integer, optional)

      Priority ranges from -2 to 2. -2 is lowest priority. 2 is highest. Zero is default.

   .. _notifications.CreateNotificationOptions.progress:

   .. api-member::
      :name: [``progress``]
      :type: (integer, optional)

      Current progress ranges from 0 to 100.

.. _notifications.NotificationItem:

NotificationItem
----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _notifications.NotificationItem.message:

   .. api-member::
      :name: ``message``
      :type: (string)

      Additional details about this item.

   .. _notifications.NotificationItem.title:

   .. api-member::
      :name: ``title``
      :type: (string)

      Title of one item of a list notification.

.. _notifications.PermissionLevel:

PermissionLevel
---------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`granted`

         .. api-member::
            :name: :value:`denied`

.. _notifications.TemplateType:

TemplateType
------------

.. api-section-annotation-hack:: -- [Added in TB 45]

.. note::

   Only the 'basic' type is supported.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`basic`

         .. api-member::
            :name: :value:`image`

         .. api-member::
            :name: :value:`list`

         .. api-member::
            :name: :value:`progress`
