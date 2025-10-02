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

         .. _browser^settings.^color^management^mode.off:

         .. api-member::
            :name: :value:`off`
            :refid: browser-settings-color-management-mode-off

         .. _browser^settings.^color^management^mode.tagged_only:

         .. api-member::
            :name: :value:`tagged_only`
            :refid: browser-settings-color-management-mode-tagged-only

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

         .. _browser^settings.^context^menu^mouse^event.mouseup:

         .. api-member::
            :name: :value:`mouseup`
            :refid: browser-settings-context-menu-mouse-event-mouseup

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

         .. _browser^settings.^image^animation^behavior.normal:

         .. api-member::
            :name: :value:`normal`
            :refid: browser-settings-image-animation-behavior-normal

         .. _browser^settings.^image^animation^behavior.once:

         .. api-member::
            :name: :value:`once`
            :refid: browser-settings-image-animation-behavior-once

.. rst-class:: api-main-section

Properties
==========

.. _browser^settings.allow^popups^for^user^events:

allowPopupsForUserEvents
------------------------

.. api-section-annotation-hack:: 

Allows or disallows pop-up windows from opening in response to user events.

.. _browser^settings.cache^enabled:

cacheEnabled
------------

.. api-section-annotation-hack:: 

Enables or disables the browser cache.

.. _browser^settings.context^menu^show^event:

contextMenuShowEvent
--------------------

.. api-section-annotation-hack:: 

Controls after which mouse event context menus popup. This setting's value is of type ContextMenuMouseEvent, which has possible values of :code:`mouseup` and :code:`mousedown`.

.. _browser^settings.ftp^protocol^enabled:

ftpProtocolEnabled
------------------

.. api-section-annotation-hack:: 

Returns whether the FTP protocol is enabled. Read-only.

.. note::

   From version 88, this setting is read-only (see `bug 1626365 <https://bugzil.la/1626365>`__).

.. _browser^settings.image^animation^behavior:

imageAnimationBehavior
----------------------

.. api-section-annotation-hack:: 

Controls the behaviour of image animation in the browser. This setting's value is of type ImageAnimationBehavior, defaulting to :code:`normal`.

.. _browser^settings.override^content^color^scheme:

overrideContentColorScheme
--------------------------

.. api-section-annotation-hack:: 

This setting controls whether a light or dark color scheme overrides the page's preferred color scheme.

.. _browser^settings.override^document^colors:

overrideDocumentColors
----------------------

.. api-section-annotation-hack:: 

This setting controls whether the user-chosen colors override the page's colors.

.. _browser^settings.use^document^fonts:

useDocumentFonts
----------------

.. api-section-annotation-hack:: 

This setting controls whether the document's fonts are used.

.. _browser^settings.vertical^tabs:

verticalTabs
------------

.. api-section-annotation-hack:: 

This boolean setting controls whether vertical tabs are enabled.

.. _browser^settings.web^notifications^disabled:

webNotificationsDisabled
------------------------

.. api-section-annotation-hack:: 

Disables webAPI notifications.

.. _browser^settings.zoom^full^page:

zoomFullPage
------------

.. api-section-annotation-hack:: 

This boolean setting controls whether zoom is applied to the full page or to text only.
