.. container:: sticky-sidebar

  ≡ webRTCIPHandlingPolicy Setting

  * `Permissions`_
  * `Examples`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

==============================
webRTCIPHandlingPolicy Setting
==============================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. _privacy.network.web^r^t^c^i^p^handling^policy:

Allow users to specify the media performance/privacy tradeoffs which impacts how WebRTC traffic will be routed and how much local address information is exposed. This preference's value is of type IPHandlingPolicy, defaulting to :code:`default`.

.. note::

   Starting in Thunderbird 70, a value of :code:`disable_non_proxied_udp` requires a proxy if one is configured, but allows connections to go through if no proxy is set up. Previously, in this mode WebRTC could only be used if a proxy was configured and TURN over TCP was available; this behavior is now exposed as :code:`proxy_only`.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _privacy.network.web^r^t^c^i^p^handling^policy.permission.privacy:

.. api-member::
   :name: :permission:`privacy`
   :refid: privacy-network-web-r-t-c-i-p-handling-policy-permission-privacy
   :refname: privacy

   Read and modify privacy settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.network.webRTCIPHandlingPolicy.*``.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.network.webRTCIPHandlingPolicy.*``.

.. rst-class:: api-main-section

Examples
========

To read the :value:`webRTCIPHandlingPolicy` setting:

.. code-block:: javascript

   let { value } = await messenger.privacy.network.webRTCIPHandlingPolicy.get({});

To update the :value:`webRTCIPHandlingPolicy` setting:

.. code-block:: javascript

   await messenger.privacy.network.webRTCIPHandlingPolicy.set({ value: <newValue> });

To clear the :value:`webRTCIPHandlingPolicy` setting and restore the default value:

.. code-block:: javascript

   await messenger.privacy.network.webRTCIPHandlingPolicy.clear({});

.. rst-class:: api-main-section

Functions
=========

.. _privacy.network.web^r^t^c^i^p^handling^policy.clear:

clear(details)
--------------

.. api-section-annotation-hack:: 

Clears the setting, restoring any default value.

.. api-header::
   :label: Parameters

   .. _privacy.network.web^r^t^c^i^p^handling^policy.clear.details:

   .. api-member::
      :name: ``details``
      :refid: privacy-network-web-r-t-c-i-p-handling-policy-clear-details
      :refname: details
      :type: (object)

      Which setting to clear.

      .. _privacy.network.web^r^t^c^i^p^handling^policy.clear.details.scope:

      .. api-member::
         :name: [``scope``]
         :refid: privacy-network-web-r-t-c-i-p-handling-policy-clear-details-scope
         :refname: scope
         :type: (:ref:`privacy.network.web^r^t^c^i^p^handling^policy.^setting^scope`, optional)

         Where to clear the setting (default: regular).

.. api-header::
   :label: Required permissions

   - :permission:`privacy`

.. _privacy.network.web^r^t^c^i^p^handling^policy.get:

get(details)
------------

.. api-section-annotation-hack:: 

Gets the value of a setting.

.. api-header::
   :label: Parameters

   .. _privacy.network.web^r^t^c^i^p^handling^policy.get.details:

   .. api-member::
      :name: ``details``
      :refid: privacy-network-web-r-t-c-i-p-handling-policy-get-details
      :refname: details
      :type: (object)

      Which setting to consider.

      .. _privacy.network.web^r^t^c^i^p^handling^policy.get.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: privacy-network-web-r-t-c-i-p-handling-policy-get-details-incognito
         :refname: incognito
         :type: (boolean, optional)

         Whether to return the value that applies to the incognito session (default false).

.. api-header::
   :label: Return type (`Promise`_)

   .. _privacy.network.web^r^t^c^i^p^handling^policy.get.returns:

   .. api-member::
      :refid: privacy-network-web-r-t-c-i-p-handling-policy-get-returns
      :refname: _returns
      :type: object

      Details of the currently effective value.

      .. _privacy.network.web^r^t^c^i^p^handling^policy.get.returns.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: privacy-network-web-r-t-c-i-p-handling-policy-get-returns-level-of-control
         :refname: levelOfControl
         :type: (:ref:`privacy.network.web^r^t^c^i^p^handling^policy.^level^of^control`)

         The level of control of the setting.

      .. _privacy.network.web^r^t^c^i^p^handling^policy.get.returns.value:

      .. api-member::
         :name: ``value``
         :refid: privacy-network-web-r-t-c-i-p-handling-policy-get-returns-value
         :refname: value
         :type: (any)

         The value of the setting.

      .. _privacy.network.web^r^t^c^i^p^handling^policy.get.returns.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: privacy-network-web-r-t-c-i-p-handling-policy-get-returns-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the effective value is specific to the incognito session. This property will *only* be present if the :value:`incognito` property in the :value:`details` parameter of :code:`get()` was true.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`privacy`

.. _privacy.network.web^r^t^c^i^p^handling^policy.set:

set(details)
------------

.. api-section-annotation-hack:: 

Sets the value of a setting.

.. api-header::
   :label: Parameters

   .. _privacy.network.web^r^t^c^i^p^handling^policy.set.details:

   .. api-member::
      :name: ``details``
      :refid: privacy-network-web-r-t-c-i-p-handling-policy-set-details
      :refname: details
      :type: (object)

      Which setting to change.

      .. _privacy.network.web^r^t^c^i^p^handling^policy.set.details.value:

      .. api-member::
         :name: ``value``
         :refid: privacy-network-web-r-t-c-i-p-handling-policy-set-details-value
         :refname: value
         :type: (any)

         The value of the setting.  Note that every setting has a specific value type, which is described together with the setting. An extension should *not* set a value of a different type.

      .. _privacy.network.web^r^t^c^i^p^handling^policy.set.details.scope:

      .. api-member::
         :name: [``scope``]
         :refid: privacy-network-web-r-t-c-i-p-handling-policy-set-details-scope
         :refname: scope
         :type: (:ref:`privacy.network.web^r^t^c^i^p^handling^policy.^setting^scope`, optional)

         Where to set the setting (default: regular).

.. api-header::
   :label: Required permissions

   - :permission:`privacy`

.. rst-class:: api-main-section

Events
======

.. _privacy.network.web^r^t^c^i^p^handling^policy.on^change:

onChange
--------

.. api-section-annotation-hack:: 

Fired after the setting changes.

.. api-header::
   :label: Parameters for onChange.addListener(listener)

   .. _privacy.network.web^r^t^c^i^p^handling^policy.on^change.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: privacy-network-web-r-t-c-i-p-handling-policy-on-change-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _privacy.network.web^r^t^c^i^p^handling^policy.on^change.details:

   .. api-member::
      :name: ``details``
      :refid: privacy-network-web-r-t-c-i-p-handling-policy-on-change-details
      :refname: details
      :type: (object)

      .. _privacy.network.web^r^t^c^i^p^handling^policy.on^change.details.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: privacy-network-web-r-t-c-i-p-handling-policy-on-change-details-level-of-control
         :refname: levelOfControl
         :type: (:ref:`privacy.network.web^r^t^c^i^p^handling^policy.^level^of^control`)

         The level of control of the setting.

      .. _privacy.network.web^r^t^c^i^p^handling^policy.on^change.details.value:

      .. api-member::
         :name: ``value``
         :refid: privacy-network-web-r-t-c-i-p-handling-policy-on-change-details-value
         :refname: value
         :type: (any)

         The value of the setting after the change.

      .. _privacy.network.web^r^t^c^i^p^handling^policy.on^change.details.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: privacy-network-web-r-t-c-i-p-handling-policy-on-change-details-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the value that has changed is specific to the incognito session. This property will *only* be present if the user has enabled the extension in incognito mode.

.. api-header::
   :label: Required permissions

   - :permission:`privacy`

.. rst-class:: api-main-section

Types
=====

.. _privacy.network.web^r^t^c^i^p^handling^policy.^level^of^control:

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

         .. _privacy.network.web^r^t^c^i^p^handling^policy.^level^of^control.controllable_by_this_extension:

         .. api-member::
            :name: :value:`controllable_by_this_extension`
            :refid: privacy-network-web-r-t-c-i-p-handling-policy-level-of-control-controllable-by-this-extension
            :refname: controllable_by_this_extension

         .. _privacy.network.web^r^t^c^i^p^handling^policy.^level^of^control.controlled_by_other_extensions:

         .. api-member::
            :name: :value:`controlled_by_other_extensions`
            :refid: privacy-network-web-r-t-c-i-p-handling-policy-level-of-control-controlled-by-other-extensions
            :refname: controlled_by_other_extensions

         .. _privacy.network.web^r^t^c^i^p^handling^policy.^level^of^control.controlled_by_this_extension:

         .. api-member::
            :name: :value:`controlled_by_this_extension`
            :refid: privacy-network-web-r-t-c-i-p-handling-policy-level-of-control-controlled-by-this-extension
            :refname: controlled_by_this_extension

         .. _privacy.network.web^r^t^c^i^p^handling^policy.^level^of^control.not_controllable:

         .. api-member::
            :name: :value:`not_controllable`
            :refid: privacy-network-web-r-t-c-i-p-handling-policy-level-of-control-not-controllable
            :refname: not_controllable

.. _privacy.network.web^r^t^c^i^p^handling^policy.^setting^scope:

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

         .. _privacy.network.web^r^t^c^i^p^handling^policy.^setting^scope.incognito_persistent:

         .. api-member::
            :name: :value:`incognito_persistent`
            :refid: privacy-network-web-r-t-c-i-p-handling-policy-setting-scope-incognito-persistent
            :refname: incognito_persistent

         .. _privacy.network.web^r^t^c^i^p^handling^policy.^setting^scope.incognito_session_only:

         .. api-member::
            :name: :value:`incognito_session_only`
            :refid: privacy-network-web-r-t-c-i-p-handling-policy-setting-scope-incognito-session-only
            :refname: incognito_session_only

         .. _privacy.network.web^r^t^c^i^p^handling^policy.^setting^scope.regular:

         .. api-member::
            :name: :value:`regular`
            :refid: privacy-network-web-r-t-c-i-p-handling-policy-setting-scope-regular
            :refname: regular

         .. _privacy.network.web^r^t^c^i^p^handling^policy.^setting^scope.regular_only:

         .. api-member::
            :name: :value:`regular_only`
            :refid: privacy-network-web-r-t-c-i-p-handling-policy-setting-scope-regular-only
            :refname: regular_only
