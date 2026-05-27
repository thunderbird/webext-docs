.. container:: sticky-sidebar

  ≡ readerDisplayAttachmentsInline Setting

  * `Permissions`_
  * `Examples`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

======================================
readerDisplayAttachmentsInline Setting
======================================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. _messenger^settings.reader^display^attachments^inline:

Whether supported attachments (for example, media files) are shown inline within the body of displayed messages. This property is read-only.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _messenger^settings.reader^display^attachments^inline.permission.messenger^settings:

.. api-member::
   :name: :permission:`messengerSettings`
   :refid: messenger-settings-reader-display-attachments-inline-permission-messenger-settings
   :refname: messengerSettings

   Read Thunderbird settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messengerSettings` is required to use ``messenger.messengerSettings.readerDisplayAttachmentsInline.*``.

.. rst-class:: api-main-section

Examples
========

To read the :value:`readerDisplayAttachmentsInline` setting:

.. code-block:: javascript

   let { value } = await messenger.messengerSettings.readerDisplayAttachmentsInline.get({});

.. rst-class:: api-main-section

Functions
=========

.. _messenger^settings.reader^display^attachments^inline.get:

get(details)
------------

.. api-section-annotation-hack:: 

Gets the value of a setting.

.. api-header::
   :label: Parameters

   .. _messenger^settings.reader^display^attachments^inline.get.details:

   .. api-member::
      :name: ``details``
      :refid: messenger-settings-reader-display-attachments-inline-get-details
      :refname: details
      :type: (object)

      Which setting to consider.

      .. _messenger^settings.reader^display^attachments^inline.get.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: messenger-settings-reader-display-attachments-inline-get-details-incognito
         :refname: incognito
         :type: (boolean, optional)

         Whether to return the value that applies to the incognito session (default false).

.. api-header::
   :label: Return type (`Promise`_)

   .. _messenger^settings.reader^display^attachments^inline.get.returns:

   .. api-member::
      :refid: messenger-settings-reader-display-attachments-inline-get-returns
      :refname: _returns
      :type: object

      Details of the currently effective value.

      .. _messenger^settings.reader^display^attachments^inline.get.returns.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: messenger-settings-reader-display-attachments-inline-get-returns-level-of-control
         :refname: levelOfControl
         :type: (:ref:`messenger^settings.reader^display^attachments^inline.^level^of^control`)

         The level of control of the setting.

      .. _messenger^settings.reader^display^attachments^inline.get.returns.value:

      .. api-member::
         :name: ``value``
         :refid: messenger-settings-reader-display-attachments-inline-get-returns-value
         :refname: value
         :type: (any)

         The value of the setting.

      .. _messenger^settings.reader^display^attachments^inline.get.returns.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: messenger-settings-reader-display-attachments-inline-get-returns-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the effective value is specific to the incognito session. This property will *only* be present if the :value:`incognito` property in the :value:`details` parameter of :code:`get()` was true.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messengerSettings`

.. rst-class:: api-main-section

Events
======

.. _messenger^settings.reader^display^attachments^inline.on^change:

onChange
--------

.. api-section-annotation-hack:: 

Fired after the setting changes.

.. api-header::
   :label: Parameters for onChange.addListener(listener)

   .. _messenger^settings.reader^display^attachments^inline.on^change.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: messenger-settings-reader-display-attachments-inline-on-change-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _messenger^settings.reader^display^attachments^inline.on^change.details:

   .. api-member::
      :name: ``details``
      :refid: messenger-settings-reader-display-attachments-inline-on-change-details
      :refname: details
      :type: (object)

      .. _messenger^settings.reader^display^attachments^inline.on^change.details.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: messenger-settings-reader-display-attachments-inline-on-change-details-level-of-control
         :refname: levelOfControl
         :type: (:ref:`messenger^settings.reader^display^attachments^inline.^level^of^control`)

         The level of control of the setting.

      .. _messenger^settings.reader^display^attachments^inline.on^change.details.value:

      .. api-member::
         :name: ``value``
         :refid: messenger-settings-reader-display-attachments-inline-on-change-details-value
         :refname: value
         :type: (any)

         The value of the setting after the change.

      .. _messenger^settings.reader^display^attachments^inline.on^change.details.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: messenger-settings-reader-display-attachments-inline-on-change-details-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the value that has changed is specific to the incognito session. This property will *only* be present if the user has enabled the extension in incognito mode.

.. api-header::
   :label: Required permissions

   - :permission:`messengerSettings`

.. rst-class:: api-main-section

Types
=====

.. _messenger^settings.reader^display^attachments^inline.^level^of^control:

LevelOfControl
--------------

.. api-section-annotation-hack:: 

One of

 * :value:`not_controllable`: cannot be controlled by any extension

 * :value:`controlled_by_other_extensions`: controlled by extensions with higher precedence

 * :value:`controllable_by_this_extension`: can be controlled by this extension

 * :value:`controlled_by_this_extension`: controlled by this extension

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _messenger^settings.reader^display^attachments^inline.^level^of^control.controllable_by_this_extension:

         .. api-member::
            :name: :value:`controllable_by_this_extension`
            :refid: messenger-settings-reader-display-attachments-inline-level-of-control-controllable-by-this-extension
            :refname: controllable_by_this_extension

         .. _messenger^settings.reader^display^attachments^inline.^level^of^control.controlled_by_other_extensions:

         .. api-member::
            :name: :value:`controlled_by_other_extensions`
            :refid: messenger-settings-reader-display-attachments-inline-level-of-control-controlled-by-other-extensions
            :refname: controlled_by_other_extensions

         .. _messenger^settings.reader^display^attachments^inline.^level^of^control.controlled_by_this_extension:

         .. api-member::
            :name: :value:`controlled_by_this_extension`
            :refid: messenger-settings-reader-display-attachments-inline-level-of-control-controlled-by-this-extension
            :refname: controlled_by_this_extension

         .. _messenger^settings.reader^display^attachments^inline.^level^of^control.not_controllable:

         .. api-member::
            :name: :value:`not_controllable`
            :refid: messenger-settings-reader-display-attachments-inline-level-of-control-not-controllable
            :refname: not_controllable
