.. container:: sticky-sidebar

  ≡ privacy.websites API

  * `Permissions`_
  * `Types`_
  * `Settings`_

  .. include:: /_includes/developer-resources.rst

====================
privacy.websites API
====================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The privacy.websites API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/privacy/websites>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.privacy` API to control usage of the features in the browser that can affect a user's privacy.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _privacy.websites.permission.privacy:

.. api-member::
   :name: :permission:`privacy`
   :refid: privacy-websites-permission-privacy
   :refname: privacy

   Read and modify privacy settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.websites.*``.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.websites.*``.

.. rst-class:: api-main-section

Types
=====

.. _privacy.websites.^cookie^config:

CookieConfig
------------

.. api-section-annotation-hack:: 

The settings for cookies.

.. api-header::
   :label: object

   .. _privacy.websites.^cookie^config.behavior:

   .. api-member::
      :name: [``behavior``]
      :refid: privacy-websites-cookie-config-behavior
      :refname: behavior
      :type: (`string`, optional)

      The type of cookies to allow.

      Supported values:

      .. _privacy.websites.^cookie^config.behavior.allow_all:

      .. api-member::
         :name: :value:`allow_all`
         :refid: privacy-websites-cookie-config-behavior-allow-all
         :refname: allow_all

      .. _privacy.websites.^cookie^config.behavior.allow_visited:

      .. api-member::
         :name: :value:`allow_visited`
         :refid: privacy-websites-cookie-config-behavior-allow-visited
         :refname: allow_visited

      .. _privacy.websites.^cookie^config.behavior.reject_all:

      .. api-member::
         :name: :value:`reject_all`
         :refid: privacy-websites-cookie-config-behavior-reject-all
         :refname: reject_all

      .. _privacy.websites.^cookie^config.behavior.reject_third_party:

      .. api-member::
         :name: :value:`reject_third_party`
         :refid: privacy-websites-cookie-config-behavior-reject-third-party
         :refname: reject_third_party

      .. _privacy.websites.^cookie^config.behavior.reject_trackers:

      .. api-member::
         :name: :value:`reject_trackers`
         :refid: privacy-websites-cookie-config-behavior-reject-trackers
         :refname: reject_trackers

      .. _privacy.websites.^cookie^config.behavior.reject_trackers_and_partition_foreign:

      .. api-member::
         :name: :value:`reject_trackers_and_partition_foreign`
         :refid: privacy-websites-cookie-config-behavior-reject-trackers-and-partition-foreign
         :refname: reject_trackers_and_partition_foreign

   .. _privacy.websites.^cookie^config.non^persistent^cookies:

   .. api-member::
      :name: [``nonPersistentCookies``]
      :refid: privacy-websites-cookie-config-non-persistent-cookies
      :refname: nonPersistentCookies
      :type: (boolean, optional) **Deprecated.**

      Whether to create all cookies as nonPersistent (i.e., session) cookies.

.. _privacy.websites.^tracking^protection^mode^option:

TrackingProtectionModeOption
----------------------------

.. api-section-annotation-hack:: 

The mode for tracking protection.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _privacy.websites.^tracking^protection^mode^option.always:

         .. api-member::
            :name: :value:`always`
            :refid: privacy-websites-tracking-protection-mode-option-always
            :refname: always

         .. _privacy.websites.^tracking^protection^mode^option.never:

         .. api-member::
            :name: :value:`never`
            :refid: privacy-websites-tracking-protection-mode-option-never
            :refname: never

         .. _privacy.websites.^tracking^protection^mode^option.private_browsing:

         .. api-member::
            :name: :value:`private_browsing`
            :refid: privacy-websites-tracking-protection-mode-option-private-browsing
            :refname: private_browsing

.. rst-class:: api-main-section

Settings
========

.. toctree::
  :hidden:

  cookieConfig <privacy.websites.cookieConfig>
  firstPartyIsolate <privacy.websites.firstPartyIsolate>
  hyperlinkAuditingEnabled <privacy.websites.hyperlinkAuditingEnabled>
  protectedContentEnabled <privacy.websites.protectedContentEnabled>
  referrersEnabled <privacy.websites.referrersEnabled>
  resistFingerprinting <privacy.websites.resistFingerprinting>
  thirdPartyCookiesAllowed <privacy.websites.thirdPartyCookiesAllowed>
  trackingProtectionMode <privacy.websites.trackingProtectionMode>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="privacy.websites.cookieConfig.html">cookieConfig</a>
   </div>

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Allow users to specify the default settings for allowing cookies, as well as whether all cookies should be created as non-persistent cookies. This setting's value is of type CookieConfig.

.. note::

   The :code:`behavior` property value "reject_trackers_and_partition_foreign" was introduced in version 78.

.. note::

   The :code:`behavior` property value "reject_trackers" was introduced in version 64.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="privacy.websites.firstPartyIsolate.html">firstPartyIsolate</a>
   </div>

.. api-section-annotation-hack:: -- [Added in TB 60.0]

If enabled, the browser will associate all data (including cookies, HSTS data, cached images, and more) for any third party domains with the domain in the address bar. This prevents third party trackers from using directly stored information to identify you across different websites, but may break websites where you login with a third party account (such as a Facebook or Google login.) The value of this preference is of type boolean, and the default value is :code:`false`.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="privacy.websites.hyperlinkAuditingEnabled.html">hyperlinkAuditingEnabled</a>
   </div>

.. api-section-annotation-hack:: -- [Added in TB 60.0]

If enabled, the browser sends auditing pings when requested by a website (:code:`&lt;a ping&gt;`). The value of this preference is of type boolean, and the default value is :code:`true`.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="privacy.websites.protectedContentEnabled.html">protectedContentEnabled</a>
   </div>

.. api-section-annotation-hack:: 

**Available on Windows and ChromeOS only**: If enabled, the browser provides a unique ID to plugins in order to run protected content. The value of this preference is of type boolean, and the default value is :code:`true`.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="privacy.websites.referrersEnabled.html">referrersEnabled</a>
   </div>

.. api-section-annotation-hack:: -- [Added in TB 60.0]

If enabled, the browser sends :code:`referer` headers with your requests. Yes, the name of this preference doesn't match the misspelled header. No, we're not going to change it. The value of this preference is of type boolean, and the default value is :code:`true`.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="privacy.websites.resistFingerprinting.html">resistFingerprinting</a>
   </div>

.. api-section-annotation-hack:: -- [Added in TB 60.0]

If enabled, the browser attempts to appear similar to other users by reporting generic information to websites. This can prevent websites from uniquely identifying users. Examples of data that is spoofed include number of CPU cores, precision of JavaScript timers, the local timezone, and disabling features such as GamePad support, and the WebSpeech and Navigator APIs. The value of this preference is of type boolean, and the default value is :code:`false`.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="privacy.websites.thirdPartyCookiesAllowed.html">thirdPartyCookiesAllowed</a>
   </div>

.. api-section-annotation-hack:: 

If disabled, the browser blocks third-party sites from setting cookies. The value of this preference is of type boolean, and the default value is :code:`true`.

.. raw:: html

   </section>

.. raw:: html

   <section class="setting-prop-header-section write">
   <div class="setting-prop-header">
     <span class="setting-prop-label">write</span>
     <a href="privacy.websites.trackingProtectionMode.html">trackingProtectionMode</a>
   </div>

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Allow users to specify the mode for tracking protection. This setting's value is of type TrackingProtectionModeOption, defaulting to :code:`private_browsing_only`.

.. raw:: html

   </section>
