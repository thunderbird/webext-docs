.. container:: sticky-sidebar

  ≡ trackingProtectionMode Setting

  * `Permissions`_
  * `Examples`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

==============================
trackingProtectionMode Setting
==============================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. _privacy.websites.tracking^protection^mode:

Allow users to specify the mode for tracking protection. This setting's value is of type TrackingProtectionModeOption, defaulting to :code:`private_browsing_only`.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _privacy.websites.tracking^protection^mode.permission.privacy:

.. api-member::
   :name: :permission:`privacy`
   :refid: privacy-websites-tracking-protection-mode-permission-privacy
   :refname: privacy

   Read and modify privacy settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.websites.trackingProtectionMode.*``.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.websites.trackingProtectionMode.*``.

.. rst-class:: api-main-section

Examples
========

To read the :value:`trackingProtectionMode` setting:

.. code-block:: javascript

   let { value } = await messenger.privacy.websites.trackingProtectionMode.get({});

To update the :value:`trackingProtectionMode` setting:

.. code-block:: javascript

   await messenger.privacy.websites.trackingProtectionMode.set({ value: <newValue> });

To clear the :value:`trackingProtectionMode` setting and restore the default value:

.. code-block:: javascript

   await messenger.privacy.websites.trackingProtectionMode.clear({});

.. rst-class:: api-main-section

Functions
=========

.. _privacy.websites.tracking^protection^mode.clear:

clear(details)
--------------

.. api-section-annotation-hack:: 

Clears the setting, restoring any default value.

.. api-header::
   :label: Parameters

   .. _privacy.websites.tracking^protection^mode.clear.details:

   .. api-member::
      :name: ``details``
      :refid: privacy-websites-tracking-protection-mode-clear-details
      :refname: details
      :type: (object)

      Which setting to clear.

      .. _privacy.websites.tracking^protection^mode.clear.details.scope:

      .. api-member::
         :name: [``scope``]
         :refid: privacy-websites-tracking-protection-mode-clear-details-scope
         :refname: scope
         :type: (:ref:`privacy.websites.tracking^protection^mode.^setting^scope`, optional)

         Where to clear the setting (default: regular).

.. api-header::
   :label: Required permissions

   - :permission:`privacy`

.. _privacy.websites.tracking^protection^mode.get:

get(details)
------------

.. api-section-annotation-hack:: 

Gets the value of a setting.

.. api-header::
   :label: Parameters

   .. _privacy.websites.tracking^protection^mode.get.details:

   .. api-member::
      :name: ``details``
      :refid: privacy-websites-tracking-protection-mode-get-details
      :refname: details
      :type: (object)

      Which setting to consider.

      .. _privacy.websites.tracking^protection^mode.get.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: privacy-websites-tracking-protection-mode-get-details-incognito
         :refname: incognito
         :type: (boolean, optional)

         Whether to return the value that applies to the incognito session (default false).

.. api-header::
   :label: Return type (`Promise`_)

   .. _privacy.websites.tracking^protection^mode.get.returns:

   .. api-member::
      :refid: privacy-websites-tracking-protection-mode-get-returns
      :refname: _returns
      :type: object

      Details of the currently effective value.

      .. _privacy.websites.tracking^protection^mode.get.returns.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: privacy-websites-tracking-protection-mode-get-returns-level-of-control
         :refname: levelOfControl
         :type: (:ref:`privacy.websites.tracking^protection^mode.^level^of^control`)

         The level of control of the setting.

      .. _privacy.websites.tracking^protection^mode.get.returns.value:

      .. api-member::
         :name: ``value``
         :refid: privacy-websites-tracking-protection-mode-get-returns-value
         :refname: value
         :type: (any)

         The value of the setting.

      .. _privacy.websites.tracking^protection^mode.get.returns.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: privacy-websites-tracking-protection-mode-get-returns-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the effective value is specific to the incognito session. This property will *only* be present if the :value:`incognito` property in the :value:`details` parameter of :code:`get()` was true.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`privacy`

.. _privacy.websites.tracking^protection^mode.set:

set(details)
------------

.. api-section-annotation-hack:: 

Sets the value of a setting.

.. api-header::
   :label: Parameters

   .. _privacy.websites.tracking^protection^mode.set.details:

   .. api-member::
      :name: ``details``
      :refid: privacy-websites-tracking-protection-mode-set-details
      :refname: details
      :type: (object)

      Which setting to change.

      .. _privacy.websites.tracking^protection^mode.set.details.value:

      .. api-member::
         :name: ``value``
         :refid: privacy-websites-tracking-protection-mode-set-details-value
         :refname: value
         :type: (any)

         The value of the setting.  Note that every setting has a specific value type, which is described together with the setting. An extension should *not* set a value of a different type.

      .. _privacy.websites.tracking^protection^mode.set.details.scope:

      .. api-member::
         :name: [``scope``]
         :refid: privacy-websites-tracking-protection-mode-set-details-scope
         :refname: scope
         :type: (:ref:`privacy.websites.tracking^protection^mode.^setting^scope`, optional)

         Where to set the setting (default: regular).

.. api-header::
   :label: Required permissions

   - :permission:`privacy`

.. rst-class:: api-main-section

Events
======

.. _privacy.websites.tracking^protection^mode.on^change:

onChange
--------

.. api-section-annotation-hack:: 

Fired after the setting changes.

.. api-header::
   :label: Parameters for onChange.addListener(listener)

   .. _privacy.websites.tracking^protection^mode.on^change.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: privacy-websites-tracking-protection-mode-on-change-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _privacy.websites.tracking^protection^mode.on^change.details:

   .. api-member::
      :name: ``details``
      :refid: privacy-websites-tracking-protection-mode-on-change-details
      :refname: details
      :type: (object)

      .. _privacy.websites.tracking^protection^mode.on^change.details.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: privacy-websites-tracking-protection-mode-on-change-details-level-of-control
         :refname: levelOfControl
         :type: (:ref:`privacy.websites.tracking^protection^mode.^level^of^control`)

         The level of control of the setting.

      .. _privacy.websites.tracking^protection^mode.on^change.details.value:

      .. api-member::
         :name: ``value``
         :refid: privacy-websites-tracking-protection-mode-on-change-details-value
         :refname: value
         :type: (any)

         The value of the setting after the change.

      .. _privacy.websites.tracking^protection^mode.on^change.details.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: privacy-websites-tracking-protection-mode-on-change-details-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the value that has changed is specific to the incognito session. This property will *only* be present if the user has enabled the extension in incognito mode.

.. api-header::
   :label: Required permissions

   - :permission:`privacy`

.. rst-class:: api-main-section

Types
=====

.. _privacy.websites.tracking^protection^mode.^level^of^control:

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

         .. _privacy.websites.tracking^protection^mode.^level^of^control.controllable_by_this_extension:

         .. api-member::
            :name: :value:`controllable_by_this_extension`
            :refid: privacy-websites-tracking-protection-mode-level-of-control-controllable-by-this-extension
            :refname: controllable_by_this_extension

         .. _privacy.websites.tracking^protection^mode.^level^of^control.controlled_by_other_extensions:

         .. api-member::
            :name: :value:`controlled_by_other_extensions`
            :refid: privacy-websites-tracking-protection-mode-level-of-control-controlled-by-other-extensions
            :refname: controlled_by_other_extensions

         .. _privacy.websites.tracking^protection^mode.^level^of^control.controlled_by_this_extension:

         .. api-member::
            :name: :value:`controlled_by_this_extension`
            :refid: privacy-websites-tracking-protection-mode-level-of-control-controlled-by-this-extension
            :refname: controlled_by_this_extension

         .. _privacy.websites.tracking^protection^mode.^level^of^control.not_controllable:

         .. api-member::
            :name: :value:`not_controllable`
            :refid: privacy-websites-tracking-protection-mode-level-of-control-not-controllable
            :refname: not_controllable

.. _privacy.websites.tracking^protection^mode.^setting^scope:

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

         .. _privacy.websites.tracking^protection^mode.^setting^scope.incognito_persistent:

         .. api-member::
            :name: :value:`incognito_persistent`
            :refid: privacy-websites-tracking-protection-mode-setting-scope-incognito-persistent
            :refname: incognito_persistent

         .. _privacy.websites.tracking^protection^mode.^setting^scope.incognito_session_only:

         .. api-member::
            :name: :value:`incognito_session_only`
            :refid: privacy-websites-tracking-protection-mode-setting-scope-incognito-session-only
            :refname: incognito_session_only

         .. _privacy.websites.tracking^protection^mode.^setting^scope.regular:

         .. api-member::
            :name: :value:`regular`
            :refid: privacy-websites-tracking-protection-mode-setting-scope-regular
            :refname: regular

         .. _privacy.websites.tracking^protection^mode.^setting^scope.regular_only:

         .. api-member::
            :name: :value:`regular_only`
            :refid: privacy-websites-tracking-protection-mode-setting-scope-regular-only
            :refname: regular_only
