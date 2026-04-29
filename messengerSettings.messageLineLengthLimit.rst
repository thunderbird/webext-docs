.. container:: sticky-sidebar

  ≡ messageLineLengthLimit Setting

  * `Permissions`_
  * `Examples`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

==============================
messageLineLengthLimit Setting
==============================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. _messenger^settings.message^line^length^limit:

The line length limit for outgoing messages, to comply with requirements from RFC 2822. See description of :ref:`messagePlainTextFlowedOutputEnabled <messenger^settings.message^plain^text^flowed^output^enabled>`. This property is read-only.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _messenger^settings.message^line^length^limit.permission.messenger^settings:

.. api-member::
   :name: :permission:`messengerSettings`
   :refid: messenger-settings-message-line-length-limit-permission-messenger-settings
   :refname: messengerSettings

   Read Thunderbird settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messengerSettings` is required to use ``messenger.messengerSettings.messageLineLengthLimit.*``.

.. rst-class:: api-main-section

Examples
========

To read the :value:`messageLineLengthLimit` setting:

.. code-block:: javascript

   let { value } = await messenger.messengerSettings.messageLineLengthLimit.get({});

.. rst-class:: api-main-section

Functions
=========

.. _messenger^settings.message^line^length^limit.get:

get(details)
------------

.. api-section-annotation-hack:: 

Gets the value of a setting.

.. api-header::
   :label: Parameters

   .. _messenger^settings.message^line^length^limit.get.details:

   .. api-member::
      :name: ``details``
      :refid: messenger-settings-message-line-length-limit-get-details
      :refname: details
      :type: (object)

      Which setting to consider.

      .. _messenger^settings.message^line^length^limit.get.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: messenger-settings-message-line-length-limit-get-details-incognito
         :refname: incognito
         :type: (boolean, optional)

         Whether to return the value that applies to the incognito session (default false).

.. api-header::
   :label: Return type (`Promise`_)

   .. _messenger^settings.message^line^length^limit.get.returns:

   .. api-member::
      :refid: messenger-settings-message-line-length-limit-get-returns
      :refname: _returns
      :type: object

      Details of the currently effective value.

      .. _messenger^settings.message^line^length^limit.get.returns.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: messenger-settings-message-line-length-limit-get-returns-level-of-control
         :refname: levelOfControl
         :type: (:ref:`messenger^settings.message^line^length^limit.^level^of^control`)

         The level of control of the setting.

      .. _messenger^settings.message^line^length^limit.get.returns.value:

      .. api-member::
         :name: ``value``
         :refid: messenger-settings-message-line-length-limit-get-returns-value
         :refname: value
         :type: (any)

         The value of the setting.

      .. _messenger^settings.message^line^length^limit.get.returns.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: messenger-settings-message-line-length-limit-get-returns-incognito-specific
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

.. _messenger^settings.message^line^length^limit.on^change:

onChange
--------

.. api-section-annotation-hack:: 

Fired after the setting changes.

.. api-header::
   :label: Parameters for onChange.addListener(listener)

   .. _messenger^settings.message^line^length^limit.on^change.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: messenger-settings-message-line-length-limit-on-change-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _messenger^settings.message^line^length^limit.on^change.details:

   .. api-member::
      :name: ``details``
      :refid: messenger-settings-message-line-length-limit-on-change-details
      :refname: details
      :type: (object)

      .. _messenger^settings.message^line^length^limit.on^change.details.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: messenger-settings-message-line-length-limit-on-change-details-level-of-control
         :refname: levelOfControl
         :type: (:ref:`messenger^settings.message^line^length^limit.^level^of^control`)

         The level of control of the setting.

      .. _messenger^settings.message^line^length^limit.on^change.details.value:

      .. api-member::
         :name: ``value``
         :refid: messenger-settings-message-line-length-limit-on-change-details-value
         :refname: value
         :type: (any)

         The value of the setting after the change.

      .. _messenger^settings.message^line^length^limit.on^change.details.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: messenger-settings-message-line-length-limit-on-change-details-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the value that has changed is specific to the incognito session. This property will *only* be present if the user has enabled the extension in incognito mode.

.. api-header::
   :label: Required permissions

   - :permission:`messengerSettings`

.. rst-class:: api-main-section

Types
=====

.. _messenger^settings.message^line^length^limit.^level^of^control:

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

         .. _messenger^settings.message^line^length^limit.^level^of^control.controllable_by_this_extension:

         .. api-member::
            :name: :value:`controllable_by_this_extension`
            :refid: messenger-settings-message-line-length-limit-level-of-control-controllable-by-this-extension
            :refname: controllable_by_this_extension

         .. _messenger^settings.message^line^length^limit.^level^of^control.controlled_by_other_extensions:

         .. api-member::
            :name: :value:`controlled_by_other_extensions`
            :refid: messenger-settings-message-line-length-limit-level-of-control-controlled-by-other-extensions
            :refname: controlled_by_other_extensions

         .. _messenger^settings.message^line^length^limit.^level^of^control.controlled_by_this_extension:

         .. api-member::
            :name: :value:`controlled_by_this_extension`
            :refid: messenger-settings-message-line-length-limit-level-of-control-controlled-by-this-extension
            :refname: controlled_by_this_extension

         .. _messenger^settings.message^line^length^limit.^level^of^control.not_controllable:

         .. api-member::
            :name: :value:`not_controllable`
            :refid: messenger-settings-message-line-length-limit-level-of-control-not-controllable
            :refname: not_controllable
