.. container:: sticky-sidebar

  ≡ browserSettings API

  * `Permissions`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

===================
browserSettings API
===================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The browserSettings API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/browserSettings>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.browserSettings` API to control global settings of the browser.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _browser^settings.permission.browser^settings:

.. api-member::
   :name: :permission:`browserSettings`
   :refid: browser-settings-permission-browser-settings
   :refname: browserSettings

   Read and modify browser settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`browserSettings` is required to use ``messenger.browserSettings.*``.

.. rst-class:: api-main-section

Types
=====

.. _browser^settings.^color^management^mode:

ColorManagementMode
-------------------

.. api-section-annotation-hack:: 

Color management mode.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _browser^settings.^color^management^mode.full:

         .. api-member::
            :name: :value:`full`
            :refid: browser-settings-color-management-mode-full
            :refname: full

         .. _browser^settings.^color^management^mode.off:

         .. api-member::
            :name: :value:`off`
            :refid: browser-settings-color-management-mode-off
            :refname: off

         .. _browser^settings.^color^management^mode.tagged_only:

         .. api-member::
            :name: :value:`tagged_only`
            :refid: browser-settings-color-management-mode-tagged-only
            :refname: tagged_only

.. _browser^settings.^context^menu^mouse^event:

ContextMenuMouseEvent
---------------------

.. api-section-annotation-hack:: 

After which mouse event context menus should popup.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _browser^settings.^context^menu^mouse^event.mousedown:

         .. api-member::
            :name: :value:`mousedown`
            :refid: browser-settings-context-menu-mouse-event-mousedown
            :refname: mousedown

         .. _browser^settings.^context^menu^mouse^event.mouseup:

         .. api-member::
            :name: :value:`mouseup`
            :refid: browser-settings-context-menu-mouse-event-mouseup
            :refname: mouseup

.. _browser^settings.^image^animation^behavior:

ImageAnimationBehavior
----------------------

.. api-section-annotation-hack:: 

How images should be animated in the browser.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _browser^settings.^image^animation^behavior.none:

         .. api-member::
            :name: :value:`none`
            :refid: browser-settings-image-animation-behavior-none
            :refname: none

         .. _browser^settings.^image^animation^behavior.normal:

         .. api-member::
            :name: :value:`normal`
            :refid: browser-settings-image-animation-behavior-normal
            :refname: normal

         .. _browser^settings.^image^animation^behavior.once:

         .. api-member::
            :name: :value:`once`
            :refid: browser-settings-image-animation-behavior-once
            :refname: once

.. rst-class:: api-main-section

Properties
==========

.. toctree::
  :hidden:

  allowPopupsForUserEvents <browserSettings.allowPopupsForUserEvents>
  cacheEnabled <browserSettings.cacheEnabled>
  closeTabsByDoubleClick <browserSettings.closeTabsByDoubleClick>
  contextMenuShowEvent <browserSettings.contextMenuShowEvent>
  ftpProtocolEnabled <browserSettings.ftpProtocolEnabled>
  homepageOverride <browserSettings.homepageOverride>
  imageAnimationBehavior <browserSettings.imageAnimationBehavior>
  newTabPageOverride <browserSettings.newTabPageOverride>
  newTabPosition <browserSettings.newTabPosition>
  openBookmarksInNewTabs <browserSettings.openBookmarksInNewTabs>
  openSearchResultsInNewTabs <browserSettings.openSearchResultsInNewTabs>
  openUrlbarResultsInNewTabs <browserSettings.openUrlbarResultsInNewTabs>
  overrideContentColorScheme <browserSettings.overrideContentColorScheme>
  overrideDocumentColors <browserSettings.overrideDocumentColors>
  useDocumentFonts <browserSettings.useDocumentFonts>
  verticalTabs <browserSettings.verticalTabs>
  webNotificationsDisabled <browserSettings.webNotificationsDisabled>
  zoomFullPage <browserSettings.zoomFullPage>
  zoomSiteSpecific <browserSettings.zoomSiteSpecific>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.allowPopupsForUserEvents.html">allowPopupsForUserEvents</a>
   </div>
   </section><section class="api-section-body">

Allows or disallows pop-up windows from opening in response to user events.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.cacheEnabled.html">cacheEnabled</a>
   </div>
   </section><section class="api-section-body">

Enables or disables the browser cache.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.closeTabsByDoubleClick.html">closeTabsByDoubleClick</a>
   </div>
   </section><section class="api-section-body">

This boolean setting controls whether the selected tab can be closed with a double click.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.contextMenuShowEvent.html">contextMenuShowEvent</a>
   </div>
   </section><section class="api-section-body">

Controls after which mouse event context menus popup. This setting's value is of type ContextMenuMouseEvent, which has possible values of :code:`mouseup` and :code:`mousedown`.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.ftpProtocolEnabled.html">ftpProtocolEnabled</a>
   </div>
   </section><section class="api-section-body">

Returns whether the FTP protocol is enabled. Read-only.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.homepageOverride.html">homepageOverride</a>
   </div>
   </section><section class="api-section-body">

Returns the value of the overridden home page. Read-only.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.imageAnimationBehavior.html">imageAnimationBehavior</a>
   </div>
   </section><section class="api-section-body">

Controls the behaviour of image animation in the browser. This setting's value is of type ImageAnimationBehavior, defaulting to :code:`normal`.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.newTabPageOverride.html">newTabPageOverride</a>
   </div>
   </section><section class="api-section-body">

Returns the value of the overridden new tab page. Read-only.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.newTabPosition.html">newTabPosition</a>
   </div>
   </section><section class="api-section-body">

Controls where new tabs are opened. :value:`afterCurrent` will open all new tabs next to the current tab, :value:`relatedAfterCurrent` will open only related tabs next to the current tab, and :value:`atEnd` will open all tabs at the end of the tab strip. The default is :value:`relatedAfterCurrent`.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.openBookmarksInNewTabs.html">openBookmarksInNewTabs</a>
   </div>
   </section><section class="api-section-body">

This boolean setting controls whether bookmarks are opened in the current tab or in a new tab.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.openSearchResultsInNewTabs.html">openSearchResultsInNewTabs</a>
   </div>
   </section><section class="api-section-body">

This boolean setting controls whether search results are opened in the current tab or in a new tab.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.openUrlbarResultsInNewTabs.html">openUrlbarResultsInNewTabs</a>
   </div>
   </section><section class="api-section-body">

This boolean setting controls whether urlbar results are opened in the current tab or in a new tab.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.overrideContentColorScheme.html">overrideContentColorScheme</a>
   </div>
   </section><section class="api-section-body">

This setting controls whether a light or dark color scheme overrides the page's preferred color scheme.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.overrideDocumentColors.html">overrideDocumentColors</a>
   </div>
   </section><section class="api-section-body">

This setting controls whether the user-chosen colors override the page's colors.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.useDocumentFonts.html">useDocumentFonts</a>
   </div>
   </section><section class="api-section-body">

This setting controls whether the document's fonts are used.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.verticalTabs.html">verticalTabs</a>
   </div>
   </section><section class="api-section-body">

This boolean setting controls whether vertical tabs are enabled.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.webNotificationsDisabled.html">webNotificationsDisabled</a>
   </div>
   </section><section class="api-section-body">

Disables webAPI notifications.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.zoomFullPage.html">zoomFullPage</a>
   </div>
   </section><section class="api-section-body">

This boolean setting controls whether zoom is applied to the full page or to text only.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="browserSettings.zoomSiteSpecific.html">zoomSiteSpecific</a>
   </div>
   </section><section class="api-section-body">

This boolean setting controls whether zoom is applied on a per-site basis or to the current tab only. If privacy.resistFingerprinting is true, this setting has no effect and zoom is applied to the current tab only.

.. raw:: html

   </section>
