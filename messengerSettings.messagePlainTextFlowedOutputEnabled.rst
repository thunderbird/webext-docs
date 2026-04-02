.. container:: sticky-sidebar

  ≡ messagePlainTextFlowedOutputEnabled Setting

  * `Permissions`_
  * `Examples`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

===========================================
messagePlainTextFlowedOutputEnabled Setting
===========================================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. _messenger^settings.message^plain^text^flowed^output^enabled:

Whether long lines in outgoing plain text messages will get soft line breaks (:value:`​ \\n`) or hard line breaks (:value:`\\n`), to comply with requirements from RFC 2822. Soft line breaks will be ignored when displayed by the receiving client. When flowed output is enabled, add-ons should not create plain text messages with manually inserted hard or soft line breaks to achieve a certain text width, as that will most probably interfere with the default line break handling and generate ridged text. When flowed output is disabled, add-ons could add hard line breaks to have control over the final message, but any line longer than the maximum line length will still receive additional hard line breaks. See :ref:`messageLineLengthLimit <messenger^settings.message^line^length^limit>`.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _messenger^settings.message^plain^text^flowed^output^enabled.permission.messenger^settings:

.. api-member::
   :name: :permission:`messengerSettings`
   :refid: messenger-settings-message-plain-text-flowed-output-enabled-permission-messenger-settings
   :refname: messengerSettings

   Read Thunderbird settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messengerSettings` is required to use ``messenger.messengerSettings.messagePlainTextFlowedOutputEnabled.*``.

.. rst-class:: api-main-section

Examples
========

To read the :value:`messagePlainTextFlowedOutputEnabled` setting:

.. code-block:: javascript

   let { value } = await messenger.messengerSettings.messagePlainTextFlowedOutputEnabled.get({});

To update the :value:`messagePlainTextFlowedOutputEnabled` setting:

.. code-block:: javascript

   await messenger.messengerSettings.messagePlainTextFlowedOutputEnabled.set({ value: <newValue> });

To clear the :value:`messagePlainTextFlowedOutputEnabled` setting and restore the default value:

.. code-block:: javascript

   await messenger.messengerSettings.messagePlainTextFlowedOutputEnabled.clear({});

.. rst-class:: api-main-section

Functions
=========

.. _messenger^settings.message^plain^text^flowed^output^enabled.clear:

clear(details)
--------------

.. api-section-annotation-hack:: 

Clears the setting, restoring any default value.

.. api-header::
   :label: Parameters

   .. _messenger^settings.message^plain^text^flowed^output^enabled.clear.details:

   .. api-member::
      :name: ``details``
      :refid: messenger-settings-message-plain-text-flowed-output-enabled-clear-details
      :refname: details
      :type: (object)

      Which setting to clear.

      .. _messenger^settings.message^plain^text^flowed^output^enabled.clear.details.scope:

      .. api-member::
         :name: [``scope``]
         :refid: messenger-settings-message-plain-text-flowed-output-enabled-clear-details-scope
         :refname: scope
         :type: (:ref:`messenger^settings.message^plain^text^flowed^output^enabled.^setting^scope`, optional)

         Where to clear the setting (default: regular).

.. api-header::
   :label: Required permissions

   - :permission:`messengerSettings`

.. _messenger^settings.message^plain^text^flowed^output^enabled.get:

get(details)
------------

.. api-section-annotation-hack:: 

Gets the value of a setting.

.. api-header::
   :label: Parameters

   .. _messenger^settings.message^plain^text^flowed^output^enabled.get.details:

   .. api-member::
      :name: ``details``
      :refid: messenger-settings-message-plain-text-flowed-output-enabled-get-details
      :refname: details
      :type: (object)

      Which setting to consider.

      .. _messenger^settings.message^plain^text^flowed^output^enabled.get.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: messenger-settings-message-plain-text-flowed-output-enabled-get-details-incognito
         :refname: incognito
         :type: (boolean, optional)

         Whether to return the value that applies to the incognito session (default false).

.. api-header::
   :label: Return type (`Promise`_)

   .. _messenger^settings.message^plain^text^flowed^output^enabled.get.returns:

   .. api-member::
      :refid: messenger-settings-message-plain-text-flowed-output-enabled-get-returns
      :refname: _returns
      :type: object

      Details of the currently effective value.

      .. _messenger^settings.message^plain^text^flowed^output^enabled.get.returns.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: messenger-settings-message-plain-text-flowed-output-enabled-get-returns-level-of-control
         :refname: levelOfControl
         :type: (:ref:`messenger^settings.message^plain^text^flowed^output^enabled.^level^of^control`)

         The level of control of the setting.

      .. _messenger^settings.message^plain^text^flowed^output^enabled.get.returns.value:

      .. api-member::
         :name: ``value``
         :refid: messenger-settings-message-plain-text-flowed-output-enabled-get-returns-value
         :refname: value
         :type: (any)

         The value of the setting.

      .. _messenger^settings.message^plain^text^flowed^output^enabled.get.returns.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: messenger-settings-message-plain-text-flowed-output-enabled-get-returns-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the effective value is specific to the incognito session. This property will *only* be present if the :value:`incognito` property in the :value:`details` parameter of :code:`get()` was true.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messengerSettings`

.. _messenger^settings.message^plain^text^flowed^output^enabled.set:

set(details)
------------

.. api-section-annotation-hack:: 

Sets the value of a setting.

.. api-header::
   :label: Parameters

   .. _messenger^settings.message^plain^text^flowed^output^enabled.set.details:

   .. api-member::
      :name: ``details``
      :refid: messenger-settings-message-plain-text-flowed-output-enabled-set-details
      :refname: details
      :type: (object)

      Which setting to change.

      .. _messenger^settings.message^plain^text^flowed^output^enabled.set.details.value:

      .. api-member::
         :name: ``value``
         :refid: messenger-settings-message-plain-text-flowed-output-enabled-set-details-value
         :refname: value
         :type: (any)

         The value of the setting.  Note that every setting has a specific value type, which is described together with the setting. An extension should *not* set a value of a different type.

      .. _messenger^settings.message^plain^text^flowed^output^enabled.set.details.scope:

      .. api-member::
         :name: [``scope``]
         :refid: messenger-settings-message-plain-text-flowed-output-enabled-set-details-scope
         :refname: scope
         :type: (:ref:`messenger^settings.message^plain^text^flowed^output^enabled.^setting^scope`, optional)

         Where to set the setting (default: regular).

.. api-header::
   :label: Required permissions

   - :permission:`messengerSettings`

.. rst-class:: api-main-section

Events
======

.. _messenger^settings.message^plain^text^flowed^output^enabled.on^change:

onChange
--------

.. api-section-annotation-hack:: 

Fired after the setting changes.

.. api-header::
   :label: Parameters for onChange.addListener(listener)

   .. _messenger^settings.message^plain^text^flowed^output^enabled.on^change.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: messenger-settings-message-plain-text-flowed-output-enabled-on-change-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _messenger^settings.message^plain^text^flowed^output^enabled.on^change.details:

   .. api-member::
      :name: ``details``
      :refid: messenger-settings-message-plain-text-flowed-output-enabled-on-change-details
      :refname: details
      :type: (object)

      .. _messenger^settings.message^plain^text^flowed^output^enabled.on^change.details.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: messenger-settings-message-plain-text-flowed-output-enabled-on-change-details-level-of-control
         :refname: levelOfControl
         :type: (:ref:`messenger^settings.message^plain^text^flowed^output^enabled.^level^of^control`)

         The level of control of the setting.

      .. _messenger^settings.message^plain^text^flowed^output^enabled.on^change.details.value:

      .. api-member::
         :name: ``value``
         :refid: messenger-settings-message-plain-text-flowed-output-enabled-on-change-details-value
         :refname: value
         :type: (any)

         The value of the setting after the change.

      .. _messenger^settings.message^plain^text^flowed^output^enabled.on^change.details.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: messenger-settings-message-plain-text-flowed-output-enabled-on-change-details-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the value that has changed is specific to the incognito session. This property will *only* be present if the user has enabled the extension in incognito mode.

.. api-header::
   :label: Required permissions

   - :permission:`messengerSettings`

.. rst-class:: api-main-section

Types
=====

.. _messenger^settings.message^plain^text^flowed^output^enabled.^level^of^control:

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

         .. _messenger^settings.message^plain^text^flowed^output^enabled.^level^of^control.controllable_by_this_extension:

         .. api-member::
            :name: :value:`controllable_by_this_extension`
            :refid: messenger-settings-message-plain-text-flowed-output-enabled-level-of-control-controllable-by-this-extension
            :refname: controllable_by_this_extension

         .. _messenger^settings.message^plain^text^flowed^output^enabled.^level^of^control.controlled_by_other_extensions:

         .. api-member::
            :name: :value:`controlled_by_other_extensions`
            :refid: messenger-settings-message-plain-text-flowed-output-enabled-level-of-control-controlled-by-other-extensions
            :refname: controlled_by_other_extensions

         .. _messenger^settings.message^plain^text^flowed^output^enabled.^level^of^control.controlled_by_this_extension:

         .. api-member::
            :name: :value:`controlled_by_this_extension`
            :refid: messenger-settings-message-plain-text-flowed-output-enabled-level-of-control-controlled-by-this-extension
            :refname: controlled_by_this_extension

         .. _messenger^settings.message^plain^text^flowed^output^enabled.^level^of^control.not_controllable:

         .. api-member::
            :name: :value:`not_controllable`
            :refid: messenger-settings-message-plain-text-flowed-output-enabled-level-of-control-not-controllable
            :refname: not_controllable

.. _messenger^settings.message^plain^text^flowed^output^enabled.^setting^scope:

SettingScope
------------

.. api-section-annotation-hack:: 

The scope of the Setting. One of

 * :value:`regular`: setting for the regular profile (which is inherited by the incognito profile if not overridden elsewhere),

 * :value:`regular_only`: setting for the regular profile only (not inherited by the incognito profile),

 * :value:`incognito_persistent`: setting for the incognito profile that survives browser restarts (overrides regular preferences),

 * :value:`incognito_session_only`: setting for the incognito profile that can only be set during an incognito session and is deleted when the incognito session ends (overrides regular and incognito_persistent preferences). Only :value:`regular` is supported by Thunderbird at this time.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _messenger^settings.message^plain^text^flowed^output^enabled.^setting^scope.incognito_persistent:

         .. api-member::
            :name: :value:`incognito_persistent`
            :refid: messenger-settings-message-plain-text-flowed-output-enabled-setting-scope-incognito-persistent
            :refname: incognito_persistent

         .. _messenger^settings.message^plain^text^flowed^output^enabled.^setting^scope.incognito_session_only:

         .. api-member::
            :name: :value:`incognito_session_only`
            :refid: messenger-settings-message-plain-text-flowed-output-enabled-setting-scope-incognito-session-only
            :refname: incognito_session_only

         .. _messenger^settings.message^plain^text^flowed^output^enabled.^setting^scope.regular:

         .. api-member::
            :name: :value:`regular`
            :refid: messenger-settings-message-plain-text-flowed-output-enabled-setting-scope-regular
            :refname: regular

         .. _messenger^settings.message^plain^text^flowed^output^enabled.^setting^scope.regular_only:

         .. api-member::
            :name: :value:`regular_only`
            :refid: messenger-settings-message-plain-text-flowed-output-enabled-setting-scope-regular-only
            :refname: regular_only
