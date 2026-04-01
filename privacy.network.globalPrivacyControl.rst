.. container:: sticky-sidebar

  ≡ privacy.network API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

===================
privacy.network API
===================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

Use the :code:`browser.privacy` API to control usage of the features in the browser that can affect a user's privacy.

.. raw:: html

   <section class="api-main-section" id="setting-property">
   <h2>Property: globalPrivacyControl</h2>

.. _privacy.network.global^privacy^control:

Allow users to query the status of 'Global Privacy Control'. This setting's value is of type boolean, defaulting to :code:`false`.

.. raw:: html

   </section>

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _privacy.network.global^privacy^control.permission.privacy:

.. api-member::
   :name: :permission:`privacy`
   :refid: privacy-network-global-privacy-control-permission-privacy
   :refname: privacy

   Read and modify privacy settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.network.globalPrivacyControl.*``.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.network.globalPrivacyControl.*``.

.. rst-class:: api-main-section

Functions
=========

.. _privacy.network.global^privacy^control.get:

get(details)
------------

.. api-section-annotation-hack:: 

Gets the value of a setting.

.. api-header::
   :label: Parameters

   .. _privacy.network.global^privacy^control.get.details:

   .. api-member::
      :name: ``details``
      :refid: privacy-network-global-privacy-control-get-details
      :refname: details
      :type: (object)

      Which setting to consider.

      .. _privacy.network.global^privacy^control.get.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: privacy-network-global-privacy-control-get-details-incognito
         :refname: incognito
         :type: (boolean, optional)

         Whether to return the value that applies to the incognito session (default false).

.. api-header::
   :label: Return type (`Promise`_)

   .. _privacy.network.global^privacy^control.get.returns:

   .. api-member::
      :refid: privacy-network-global-privacy-control-get-returns
      :refname: _returns
      :type: object

      Details of the currently effective value.

      .. _privacy.network.global^privacy^control.get.returns.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: privacy-network-global-privacy-control-get-returns-level-of-control
         :refname: levelOfControl
         :type: (:ref:`privacy.network.global^privacy^control.^level^of^control`)

         The level of control of the setting.

      .. _privacy.network.global^privacy^control.get.returns.value:

      .. api-member::
         :name: ``value``
         :refid: privacy-network-global-privacy-control-get-returns-value
         :refname: value
         :type: (any)

         The value of the setting.

      .. _privacy.network.global^privacy^control.get.returns.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: privacy-network-global-privacy-control-get-returns-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the effective value is specific to the incognito session.<br/>This property will *only* be present if the :value:`incognito` property in the :value:`details` parameter of :code:`get()` was true.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`privacy`

.. rst-class:: api-main-section

Events
======

.. _privacy.network.global^privacy^control.on^change:

onChange
--------

.. api-section-annotation-hack:: 

Fired after the setting changes.

.. api-header::
   :label: Parameters for onChange.addListener(listener)

   .. _privacy.network.global^privacy^control.on^change.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: privacy-network-global-privacy-control-on-change-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _privacy.network.global^privacy^control.on^change.details:

   .. api-member::
      :name: ``details``
      :refid: privacy-network-global-privacy-control-on-change-details
      :refname: details
      :type: (object)

      .. _privacy.network.global^privacy^control.on^change.details.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: privacy-network-global-privacy-control-on-change-details-level-of-control
         :refname: levelOfControl
         :type: (:ref:`privacy.network.global^privacy^control.^level^of^control`)

         The level of control of the setting.

      .. _privacy.network.global^privacy^control.on^change.details.value:

      .. api-member::
         :name: ``value``
         :refid: privacy-network-global-privacy-control-on-change-details-value
         :refname: value
         :type: (any)

         The value of the setting after the change.

      .. _privacy.network.global^privacy^control.on^change.details.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: privacy-network-global-privacy-control-on-change-details-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the value that has changed is specific to the incognito session.<br/>This property will *only* be present if the user has enabled the extension in incognito mode.

.. api-header::
   :label: Required permissions

   - :permission:`privacy`

.. rst-class:: api-main-section

Types
=====

.. _privacy.network.global^privacy^control.^level^of^control:

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

         .. _privacy.network.global^privacy^control.^level^of^control.controllable_by_this_extension:

         .. api-member::
            :name: :value:`controllable_by_this_extension`
            :refid: privacy-network-global-privacy-control-level-of-control-controllable-by-this-extension
            :refname: controllable_by_this_extension

         .. _privacy.network.global^privacy^control.^level^of^control.controlled_by_other_extensions:

         .. api-member::
            :name: :value:`controlled_by_other_extensions`
            :refid: privacy-network-global-privacy-control-level-of-control-controlled-by-other-extensions
            :refname: controlled_by_other_extensions

         .. _privacy.network.global^privacy^control.^level^of^control.controlled_by_this_extension:

         .. api-member::
            :name: :value:`controlled_by_this_extension`
            :refid: privacy-network-global-privacy-control-level-of-control-controlled-by-this-extension
            :refname: controlled_by_this_extension

         .. _privacy.network.global^privacy^control.^level^of^control.not_controllable:

         .. api-member::
            :name: :value:`not_controllable`
            :refid: privacy-network-global-privacy-control-level-of-control-not-controllable
            :refname: not_controllable
