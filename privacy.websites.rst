.. container:: sticky-sidebar

  ≡ privacy.websites API

  * `Permissions`_
  * `Properties`_

  .. include:: /includes/developer-resources.rst

====================
privacy.websites API
====================

.. role:: permission

.. role:: value

.. role:: code

Use the :code:`browser.privacy` API to control usage of the features in the browser that can affect a user's privacy.

.. rst-class:: api-main-section

Permissions
===========

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.websites.*``.

.. rst-class:: api-main-section

Properties
==========

.. _privacy.websites.cookieConfig:

cookieConfig
------------

.. api-section-annotation-hack:: 

Allow users to specify the default settings for allowing cookies, as well as whether all cookies should be created as non-persistent cookies. This setting's value is of type CookieConfig.

.. _privacy.websites.firstPartyIsolate:

firstPartyIsolate
-----------------

.. api-section-annotation-hack:: 

If enabled, the browser will associate all data (including cookies, HSTS data, cached images, and more) for any third party domains with the domain in the address bar. This prevents third party trackers from using directly stored information to identify you across different websites, but may break websites where you login with a third party account (such as a Facebook or Google login.) The value of this preference is of type boolean, and the default value is :code:`false`.

.. _privacy.websites.hyperlinkAuditingEnabled:

hyperlinkAuditingEnabled
------------------------

.. api-section-annotation-hack:: 

If enabled, the browser sends auditing pings when requested by a website (:code:`&lt;a ping&gt;`). The value of this preference is of type boolean, and the default value is :code:`true`.

.. _privacy.websites.protectedContentEnabled:

protectedContentEnabled
-----------------------

.. api-section-annotation-hack:: 

<strong>Available on Windows and ChromeOS only</strong>: If enabled, the browser provides a unique ID to plugins in order to run protected content. The value of this preference is of type boolean, and the default value is :code:`true`.

.. _privacy.websites.referrersEnabled:

referrersEnabled
----------------

.. api-section-annotation-hack:: 

If enabled, the browser sends :code:`referer` headers with your requests. Yes, the name of this preference doesn't match the misspelled header. No, we're not going to change it. The value of this preference is of type boolean, and the default value is :code:`true`.

.. _privacy.websites.resistFingerprinting:

resistFingerprinting
--------------------

.. api-section-annotation-hack:: 

If enabled, the browser attempts to appear similar to other users by reporting generic information to websites. This can prevent websites from uniquely identifying users. Examples of data that is spoofed include number of CPU cores, precision of JavaScript timers, the local timezone, and disabling features such as GamePad support, and the WebSpeech and Navigator APIs. The value of this preference is of type boolean, and the default value is :code:`false`.

.. _privacy.websites.thirdPartyCookiesAllowed:

thirdPartyCookiesAllowed
------------------------

.. api-section-annotation-hack:: 

If disabled, the browser blocks third-party sites from setting cookies. The value of this preference is of type boolean, and the default value is :code:`true`.

.. _privacy.websites.trackingProtectionMode:

trackingProtectionMode
----------------------

.. api-section-annotation-hack:: 

Allow users to specify the mode for tracking protection. This setting's value is of type TrackingProtectionModeOption, defaulting to :code:`private_browsing_only`.
