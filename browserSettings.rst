.. container:: sticky-sidebar

  ≡ browserSettings API

  * `Permissions`_
  * `Properties`_

  .. include:: /includes/developer-resources.rst

===================
browserSettings API
===================

.. role:: permission

.. role:: value

.. role:: code

Use the :code:`browser.browserSettings` API to control global settings of the browser.

.. rst-class:: api-main-section

Permissions
===========

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`browserSettings` is required to use ``messenger.browserSettings.*``.

.. rst-class:: api-main-section

Properties
==========

.. _browserSettings.allowPopupsForUserEvents:

allowPopupsForUserEvents
------------------------

.. api-section-annotation-hack:: 

Allows or disallows pop-up windows from opening in response to user events.

.. _browserSettings.cacheEnabled:

cacheEnabled
------------

.. api-section-annotation-hack:: 

Enables or disables the browser cache.

.. _browserSettings.contextMenuShowEvent:

contextMenuShowEvent
--------------------

.. api-section-annotation-hack:: 

Controls after which mouse event context menus popup. This setting's value is of type ContextMenuMouseEvent, which has possible values of :code:`mouseup` and :code:`mousedown`.

.. _browserSettings.ftpProtocolEnabled:

ftpProtocolEnabled
------------------

.. api-section-annotation-hack:: 

Returns whether the FTP protocol is enabled. Read-only.

.. note::

   From version 88, this setting is read-only (see `bug 1626365 <https://bugzil.la/1626365>`__).

.. _browserSettings.imageAnimationBehavior:

imageAnimationBehavior
----------------------

.. api-section-annotation-hack:: 

Controls the behaviour of image animation in the browser. This setting's value is of type ImageAnimationBehavior, defaulting to :code:`normal`.

.. _browserSettings.overrideContentColorScheme:

overrideContentColorScheme
--------------------------

.. api-section-annotation-hack:: 

This setting controls whether a light or dark color scheme overrides the page's preferred color scheme.

.. _browserSettings.overrideDocumentColors:

overrideDocumentColors
----------------------

.. api-section-annotation-hack:: 

This setting controls whether the user-chosen colors override the page's colors.

.. _browserSettings.useDocumentFonts:

useDocumentFonts
----------------

.. api-section-annotation-hack:: 

This setting controls whether the document's fonts are used.

.. _browserSettings.verticalTabs:

verticalTabs
------------

.. api-section-annotation-hack:: 

This boolean setting controls whether vertical tabs are enabled.

.. _browserSettings.webNotificationsDisabled:

webNotificationsDisabled
------------------------

.. api-section-annotation-hack:: 

Disables webAPI notifications.

.. _browserSettings.zoomFullPage:

zoomFullPage
------------

.. api-section-annotation-hack:: 

This boolean setting controls whether zoom is applied to the full page or to text only.
