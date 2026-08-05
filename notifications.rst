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

.. role:: small

.. hint::

   The notifications API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/notifications>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

The notifications API allows to display system notifications to the user.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _notifications.permission.notifications:

.. api-member::
   :name: :permission:`notifications`
   :refid: notifications-permission-notifications
   :refname: notifications

   Display notifications to you.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`notifications` is required to use ``messenger.notifications.*``.

.. rst-class:: api-main-section

Functions
=========

.. _notifications.clear:

clear(notificationId)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Clears an existing notification.

.. api-header::
   :label: Parameters

   .. _notifications.clear.notification^id:

   .. api-member::
      :name: ``notificationId``
      :refid: notifications-clear-notification-id
      :refname: notificationId
      :type: (string)

      The id of the notification to be updated.

.. api-header::
   :label: Return type (`Promise`_)

   .. _notifications.clear.returns:

   .. api-member::
      :refid: notifications-clear-returns
      :refname: _returns
      :type: boolean

      Indicates whether a matching notification existed.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.create:

create([notificationId], options)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Creates and displays a notification.

.. api-header::
   :label: Parameters

   .. _notifications.create.notification^id:

   .. api-member::
      :name: [``notificationId``]
      :refid: notifications-create-notification-id
      :refname: notificationId
      :type: (string, optional)

      Identifier of the notification. If it is empty, this method generates an id. If it matches an existing notification, this method first clears that notification before proceeding with the create operation.

   .. _notifications.create.options:

   .. api-member::
      :name: ``options``
      :refid: notifications-create-options
      :refname: options
      :type: (:ref:`notifications.^create^notification^options`)

      Contents of the notification.

.. api-header::
   :label: Return type (`Promise`_)

   .. _notifications.create.returns:

   .. api-member::
      :refid: notifications-create-returns
      :refname: _returns
      :type: string

      The notification id (either supplied or generated) that represents the created notification.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.get^all:

getAll()
--------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Retrieves all the notifications.

.. api-header::
   :label: Return type (`Promise`_)

   .. _notifications.get^all.returns:

   .. api-member::
      :refid: notifications-get-all-returns
      :refname: _returns
      :type: object

      The set of notifications currently in the system.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.get^permission^level:

getPermissionLevel()
--------------------

.. api-section-annotation-hack:: 

Retrieves whether the user has enabled notifications from this app or extension.

.. api-header::
   :label: Return type (`Promise`_)

   .. _notifications.get^permission^level.returns:

   .. api-member::
      :refid: notifications-get-permission-level-returns
      :refname: _returns
      :type: :ref:`notifications.^permission^level`

      The current permission level.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. rst-class:: api-main-section

Events
======

.. _notifications.on^clicked:

onClicked
---------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when the user clicked in a non-button area of the notification.

.. api-header::
   :label: Parameters for onClicked.addListener(listener)

   .. _notifications.on^clicked.listener(notification^id):

   .. api-member::
      :name: ``listener(notificationId)``
      :refid: notifications-on-clicked-listener-notification-id
      :refname: listener(notificationId)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _notifications.on^clicked.notification^id:

   .. api-member::
      :name: ``notificationId``
      :refid: notifications-on-clicked-notification-id
      :refname: notificationId
      :type: (string)

      The notificationId of the clicked notification.

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.on^closed:

onClosed
--------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when the notification closed, either by the system or by user action.

.. api-header::
   :label: Parameters for onClosed.addListener(listener)

   .. _notifications.on^closed.listener(notification^id, by^user):

   .. api-member::
      :name: ``listener(notificationId, byUser)``
      :refid: notifications-on-closed-listener-notification-id-by-user
      :refname: listener(notificationId, byUser)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _notifications.on^closed.notification^id:

   .. api-member::
      :name: ``notificationId``
      :refid: notifications-on-closed-notification-id
      :refname: notificationId
      :type: (string)

      The notificationId of the closed notification.

   .. _notifications.on^closed.by^user:

   .. api-member::
      :name: ``byUser``
      :refid: notifications-on-closed-by-user
      :refname: byUser
      :type: (boolean)

      True if the notification was closed by the user.

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.on^permission^level^changed:

onPermissionLevelChanged
------------------------

.. api-section-annotation-hack:: 

Fired when the user changes the permission level.

.. api-header::
   :label: Parameters for onPermissionLevelChanged.addListener(listener)

   .. _notifications.on^permission^level^changed.listener(level):

   .. api-member::
      :name: ``listener(level)``
      :refid: notifications-on-permission-level-changed-listener-level
      :refname: listener(level)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _notifications.on^permission^level^changed.level:

   .. api-member::
      :name: ``level``
      :refid: notifications-on-permission-level-changed-level
      :refname: level
      :type: (:ref:`notifications.^permission^level`)

      The new permission level.

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.on^shown:

onShown
-------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Fired when the notification is shown.

.. api-header::
   :label: Parameters for onShown.addListener(listener)

   .. _notifications.on^shown.listener(notification^id):

   .. api-member::
      :name: ``listener(notificationId)``
      :refid: notifications-on-shown-listener-notification-id
      :refname: listener(notificationId)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _notifications.on^shown.notification^id:

   .. api-member::
      :name: ``notificationId``
      :refid: notifications-on-shown-notification-id
      :refname: notificationId
      :type: (string)

      The notificationId of the shown notification.

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. _notifications.on^show^settings:

onShowSettings
--------------

.. api-section-annotation-hack:: 

Fired when the user clicked on a link for the app's notification settings.

.. api-header::
   :label: Parameters for onShowSettings.addListener(listener)

   .. _notifications.on^show^settings.listener():

   .. api-member::
      :name: ``listener()``
      :refid: notifications-on-show-settings-listener
      :refname: listener()

      A function that will be called when this event occurs.

.. api-header::
   :label: Required permissions

   - :permission:`notifications`

.. rst-class:: api-main-section

Types
=====

.. _notifications.^create^notification^options:

CreateNotificationOptions
-------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _notifications.^create^notification^options.message:

   .. api-member::
      :name: ``message``
      :refid: notifications-create-notification-options-message
      :refname: message
      :type: (string)

      Main notification content.

   .. _notifications.^create^notification^options.title:

   .. api-member::
      :name: ``title``
      :refid: notifications-create-notification-options-title
      :refname: title
      :type: (string)

      Title of the notification (e.g. sender name for email).

   .. _notifications.^create^notification^options.type:

   .. api-member::
      :name: ``type``
      :refid: notifications-create-notification-options-type
      :refname: type
      :type: (:ref:`notifications.^template^type`)

      Which type of notification to display.

   .. _notifications.^create^notification^options.app^icon^mask^url:

   .. api-member::
      :name: [``appIconMaskUrl``]
      :refid: notifications-create-notification-options-app-icon-mask-url
      :refname: appIconMaskUrl
      :type: (string, optional)

      A URL to the app icon mask.

   .. _notifications.^create^notification^options.buttons:

   .. api-member::
      :name: [``buttons``]
      :refid: notifications-create-notification-options-buttons
      :refname: buttons
      :type: (array of object, optional) **Unsupported.**

      Text and icons for up to two notification action buttons.

   .. _notifications.^create^notification^options.context^message:

   .. api-member::
      :name: [``contextMessage``]
      :refid: notifications-create-notification-options-context-message
      :refname: contextMessage
      :type: (string, optional)

      Alternate notification content with a lower-weight font.

   .. _notifications.^create^notification^options.event^time:

   .. api-member::
      :name: [``eventTime``]
      :refid: notifications-create-notification-options-event-time
      :refname: eventTime
      :type: (number, optional)

      A timestamp associated with the notification, in milliseconds past the epoch.

   .. _notifications.^create^notification^options.icon^url:

   .. api-member::
      :name: [``iconUrl``]
      :refid: notifications-create-notification-options-icon-url
      :refname: iconUrl
      :type: (string, optional)

      A URL to the sender's avatar, app icon, or a thumbnail for image notifications.

   .. _notifications.^create^notification^options.image^url:

   .. api-member::
      :name: [``imageUrl``]
      :refid: notifications-create-notification-options-image-url
      :refname: imageUrl
      :type: (string, optional)

      A URL to the image thumbnail for image-type notifications.

   .. _notifications.^create^notification^options.is^clickable:

   .. api-member::
      :name: [``isClickable``]
      :refid: notifications-create-notification-options-is-clickable
      :refname: isClickable
      :type: (boolean, optional)

      Whether to show UI indicating that the app will visibly respond to clicks on the body of a notification.

   .. _notifications.^create^notification^options.items:

   .. api-member::
      :name: [``items``]
      :refid: notifications-create-notification-options-items
      :refname: items
      :type: (array of :ref:`notifications.^notification^item`, optional)

      Items for multi-item notifications.

   .. _notifications.^create^notification^options.priority:

   .. api-member::
      :name: [``priority``]
      :refid: notifications-create-notification-options-priority
      :refname: priority
      :type: (integer, optional)

      Priority ranges from -2 to 2. -2 is lowest priority. 2 is highest. Zero is default.

   .. _notifications.^create^notification^options.progress:

   .. api-member::
      :name: [``progress``]
      :refid: notifications-create-notification-options-progress
      :refname: progress
      :type: (integer, optional)

      Current progress ranges from 0 to 100.

.. _notifications.^notification^item:

NotificationItem
----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _notifications.^notification^item.message:

   .. api-member::
      :name: ``message``
      :refid: notifications-notification-item-message
      :refname: message
      :type: (string)

      Additional details about this item.

   .. _notifications.^notification^item.title:

   .. api-member::
      :name: ``title``
      :refid: notifications-notification-item-title
      :refname: title
      :type: (string)

      Title of one item of a list notification.

.. _notifications.^permission^level:

PermissionLevel
---------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _notifications.^permission^level.denied:

         .. api-member::
            :name: :value:`denied`
            :refid: notifications-permission-level-denied
            :refname: denied

         .. _notifications.^permission^level.granted:

         .. api-member::
            :name: :value:`granted`
            :refid: notifications-permission-level-granted
            :refname: granted

.. _notifications.^template^type:

TemplateType
------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

.. note::

   Only the 'basic' type is supported.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _notifications.^template^type.basic:

         .. api-member::
            :name: :value:`basic`
            :refid: notifications-template-type-basic
            :refname: basic

         .. _notifications.^template^type.image:

         .. api-member::
            :name: :value:`image`
            :refid: notifications-template-type-image
            :refname: image

         .. _notifications.^template^type.list:

         .. api-member::
            :name: :value:`list`
            :refid: notifications-template-type-list
            :refname: list

         .. _notifications.^template^type.progress:

         .. api-member::
            :name: :value:`progress`
            :refid: notifications-template-type-progress
            :refname: progress

.. _notifications.^update^notification^options:

UpdateNotificationOptions
-------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _notifications.^update^notification^options.app^icon^mask^url:

   .. api-member::
      :name: [``appIconMaskUrl``]
      :refid: notifications-update-notification-options-app-icon-mask-url
      :refname: appIconMaskUrl
      :type: (string, optional)

      A URL to the app icon mask.

   .. _notifications.^update^notification^options.buttons:

   .. api-member::
      :name: [``buttons``]
      :refid: notifications-update-notification-options-buttons
      :refname: buttons
      :type: (array of object, optional) **Unsupported.**

      Text and icons for up to two notification action buttons.

   .. _notifications.^update^notification^options.context^message:

   .. api-member::
      :name: [``contextMessage``]
      :refid: notifications-update-notification-options-context-message
      :refname: contextMessage
      :type: (string, optional)

      Alternate notification content with a lower-weight font.

   .. _notifications.^update^notification^options.event^time:

   .. api-member::
      :name: [``eventTime``]
      :refid: notifications-update-notification-options-event-time
      :refname: eventTime
      :type: (number, optional)

      A timestamp associated with the notification, in milliseconds past the epoch.

   .. _notifications.^update^notification^options.icon^url:

   .. api-member::
      :name: [``iconUrl``]
      :refid: notifications-update-notification-options-icon-url
      :refname: iconUrl
      :type: (string, optional)

      A URL to the sender's avatar, app icon, or a thumbnail for image notifications.

   .. _notifications.^update^notification^options.image^url:

   .. api-member::
      :name: [``imageUrl``]
      :refid: notifications-update-notification-options-image-url
      :refname: imageUrl
      :type: (string, optional)

      A URL to the image thumbnail for image-type notifications.

   .. _notifications.^update^notification^options.is^clickable:

   .. api-member::
      :name: [``isClickable``]
      :refid: notifications-update-notification-options-is-clickable
      :refname: isClickable
      :type: (boolean, optional)

      Whether to show UI indicating that the app will visibly respond to clicks on the body of a notification.

   .. _notifications.^update^notification^options.items:

   .. api-member::
      :name: [``items``]
      :refid: notifications-update-notification-options-items
      :refname: items
      :type: (array of :ref:`notifications.^notification^item`, optional)

      Items for multi-item notifications.

   .. _notifications.^update^notification^options.message:

   .. api-member::
      :name: [``message``]
      :refid: notifications-update-notification-options-message
      :refname: message
      :type: (string, optional)

      Main notification content.

   .. _notifications.^update^notification^options.priority:

   .. api-member::
      :name: [``priority``]
      :refid: notifications-update-notification-options-priority
      :refname: priority
      :type: (integer, optional)

      Priority ranges from -2 to 2. -2 is lowest priority. 2 is highest. Zero is default.

   .. _notifications.^update^notification^options.progress:

   .. api-member::
      :name: [``progress``]
      :refid: notifications-update-notification-options-progress
      :refname: progress
      :type: (integer, optional)

      Current progress ranges from 0 to 100.

   .. _notifications.^update^notification^options.title:

   .. api-member::
      :name: [``title``]
      :refid: notifications-update-notification-options-title
      :refname: title
      :type: (string, optional)

      Title of the notification (e.g. sender name for email).

   .. _notifications.^update^notification^options.type:

   .. api-member::
      :name: [``type``]
      :refid: notifications-update-notification-options-type
      :refname: type
      :type: (:ref:`notifications.^template^type`, optional)

      Which type of notification to display.
