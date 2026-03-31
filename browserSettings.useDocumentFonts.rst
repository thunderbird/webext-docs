.. container:: sticky-sidebar

  ≡ browserSettings API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

===================
browserSettings API
===================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The browserSettings.useDocumentFonts API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/browserSettings/useDocumentFonts>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.browserSettings` API to control global settings of the browser.

.. raw:: html

   <section class="api-main-section" id="setting-property">
   <h2>Property: useDocumentFonts</h2>

.. _browser^settings.use^document^fonts:

This setting controls whether the document's fonts are used.

.. raw:: html

   </section>

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _browser^settings.use^document^fonts.permission.browser^settings:

.. api-member::
   :name: :permission:`browserSettings`
   :refid: browser-settings-use-document-fonts-permission-browser-settings
   :refname: browserSettings

   Read and modify browser settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`browserSettings` is required to use ``messenger.browserSettings.useDocumentFonts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _browser^settings.use^document^fonts.clear:

clear(details)
--------------

.. api-section-annotation-hack:: 

Clears the setting, restoring any default value.

.. api-header::
   :label: Parameters

   .. _browser^settings.use^document^fonts.clear.details:

   .. api-member::
      :name: ``details``
      :refid: browser-settings-use-document-fonts-clear-details
      :refname: details
      :type: (object)

      Which setting to clear.

      .. _browser^settings.use^document^fonts.clear.details.scope:

      .. api-member::
         :name: [``scope``]
         :refid: browser-settings-use-document-fonts-clear-details-scope
         :refname: scope
         :type: (:ref:`browser^settings.use^document^fonts.^setting^scope`, optional)

         Where to clear the setting (default: regular).

.. api-header::
   :label: Required permissions

   - :permission:`browserSettings`

.. _browser^settings.use^document^fonts.get:

get(details)
------------

.. api-section-annotation-hack:: 

Gets the value of a setting.

.. api-header::
   :label: Parameters

   .. _browser^settings.use^document^fonts.get.details:

   .. api-member::
      :name: ``details``
      :refid: browser-settings-use-document-fonts-get-details
      :refname: details
      :type: (object)

      Which setting to consider.

      .. _browser^settings.use^document^fonts.get.details.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: browser-settings-use-document-fonts-get-details-incognito
         :refname: incognito
         :type: (boolean, optional)

         Whether to return the value that applies to the incognito session (default false).

.. api-header::
   :label: Return type (`Promise`_)

   .. _browser^settings.use^document^fonts.get.returns:

   .. api-member::
      :refid: browser-settings-use-document-fonts-get-returns
      :refname: _returns
      :type: object

      Details of the currently effective value.

      .. _browser^settings.use^document^fonts.get.returns.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: browser-settings-use-document-fonts-get-returns-level-of-control
         :refname: levelOfControl
         :type: (:ref:`browser^settings.use^document^fonts.^level^of^control`)

         The level of control of the setting.

      .. _browser^settings.use^document^fonts.get.returns.value:

      .. api-member::
         :name: ``value``
         :refid: browser-settings-use-document-fonts-get-returns-value
         :refname: value
         :type: (any)

         The value of the setting.

      .. _browser^settings.use^document^fonts.get.returns.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: browser-settings-use-document-fonts-get-returns-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the effective value is specific to the incognito session.<br/>This property will *only* be present if the :value:`incognito` property in the :value:`details` parameter of :code:`get()` was true.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`browserSettings`

.. _browser^settings.use^document^fonts.set:

set(details)
------------

.. api-section-annotation-hack:: 

Sets the value of a setting.

.. api-header::
   :label: Parameters

   .. _browser^settings.use^document^fonts.set.details:

   .. api-member::
      :name: ``details``
      :refid: browser-settings-use-document-fonts-set-details
      :refname: details
      :type: (object)

      Which setting to change.

      .. _browser^settings.use^document^fonts.set.details.value:

      .. api-member::
         :name: ``value``
         :refid: browser-settings-use-document-fonts-set-details-value
         :refname: value
         :type: (any)

         The value of the setting. <br/>Note that every setting has a specific value type, which is described together with the setting. An extension should *not* set a value of a different type.

      .. _browser^settings.use^document^fonts.set.details.scope:

      .. api-member::
         :name: [``scope``]
         :refid: browser-settings-use-document-fonts-set-details-scope
         :refname: scope
         :type: (:ref:`browser^settings.use^document^fonts.^setting^scope`, optional)

         Where to set the setting (default: regular).

.. api-header::
   :label: Required permissions

   - :permission:`browserSettings`

.. rst-class:: api-main-section

Events
======

.. _browser^settings.use^document^fonts.on^change:

onChange
--------

.. api-section-annotation-hack:: 

Fired after the setting changes.

.. api-header::
   :label: Parameters for onChange.addListener(listener)

   .. _browser^settings.use^document^fonts.on^change.listener(details):

   .. api-member::
      :name: ``listener(details)``
      :refid: browser-settings-use-document-fonts-on-change-listener-details
      :refname: listener(details)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _browser^settings.use^document^fonts.on^change.details:

   .. api-member::
      :name: ``details``
      :refid: browser-settings-use-document-fonts-on-change-details
      :refname: details
      :type: (object)

      .. _browser^settings.use^document^fonts.on^change.details.level^of^control:

      .. api-member::
         :name: ``levelOfControl``
         :refid: browser-settings-use-document-fonts-on-change-details-level-of-control
         :refname: levelOfControl
         :type: (:ref:`browser^settings.use^document^fonts.^level^of^control`)

         The level of control of the setting.

      .. _browser^settings.use^document^fonts.on^change.details.value:

      .. api-member::
         :name: ``value``
         :refid: browser-settings-use-document-fonts-on-change-details-value
         :refname: value
         :type: (any)

         The value of the setting after the change.

      .. _browser^settings.use^document^fonts.on^change.details.incognito^specific:

      .. api-member::
         :name: [``incognitoSpecific``]
         :refid: browser-settings-use-document-fonts-on-change-details-incognito-specific
         :refname: incognitoSpecific
         :type: (boolean, optional)

         Whether the value that has changed is specific to the incognito session.<br/>This property will *only* be present if the user has enabled the extension in incognito mode.

.. api-header::
   :label: Required permissions

   - :permission:`browserSettings`

.. rst-class:: api-main-section

Types
=====

.. _browser^settings.use^document^fonts.^level^of^control:

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

         .. _browser^settings.use^document^fonts.^level^of^control.controllable_by_this_extension:

         .. api-member::
            :name: :value:`controllable_by_this_extension`
            :refid: browser-settings-use-document-fonts-level-of-control-controllable-by-this-extension
            :refname: controllable_by_this_extension

         .. _browser^settings.use^document^fonts.^level^of^control.controlled_by_other_extensions:

         .. api-member::
            :name: :value:`controlled_by_other_extensions`
            :refid: browser-settings-use-document-fonts-level-of-control-controlled-by-other-extensions
            :refname: controlled_by_other_extensions

         .. _browser^settings.use^document^fonts.^level^of^control.controlled_by_this_extension:

         .. api-member::
            :name: :value:`controlled_by_this_extension`
            :refid: browser-settings-use-document-fonts-level-of-control-controlled-by-this-extension
            :refname: controlled_by_this_extension

         .. _browser^settings.use^document^fonts.^level^of^control.not_controllable:

         .. api-member::
            :name: :value:`not_controllable`
            :refid: browser-settings-use-document-fonts-level-of-control-not-controllable
            :refname: not_controllable

.. _browser^settings.use^document^fonts.^setting^scope:

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

         .. _browser^settings.use^document^fonts.^setting^scope.incognito_persistent:

         .. api-member::
            :name: :value:`incognito_persistent`
            :refid: browser-settings-use-document-fonts-setting-scope-incognito-persistent
            :refname: incognito_persistent

         .. _browser^settings.use^document^fonts.^setting^scope.incognito_session_only:

         .. api-member::
            :name: :value:`incognito_session_only`
            :refid: browser-settings-use-document-fonts-setting-scope-incognito-session-only
            :refname: incognito_session_only

         .. _browser^settings.use^document^fonts.^setting^scope.regular:

         .. api-member::
            :name: :value:`regular`
            :refid: browser-settings-use-document-fonts-setting-scope-regular
            :refname: regular

         .. _browser^settings.use^document^fonts.^setting^scope.regular_only:

         .. api-member::
            :name: :value:`regular_only`
            :refid: browser-settings-use-document-fonts-setting-scope-regular-only
            :refname: regular_only
