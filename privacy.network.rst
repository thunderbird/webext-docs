.. container:: sticky-sidebar

  ≡ privacy.network API

  * `Permissions`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

===================
privacy.network API
===================

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The privacy.network API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/privacy/network>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`browser.privacy` API to control usage of the features in the browser that can affect a user's privacy.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _privacy.network.permission.privacy:

.. api-member::
   :name: :permission:`privacy`
   :refid: privacy-network-permission-privacy
   :refname: privacy

   Read and modify privacy settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.network.*``.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.network.*``.

.. rst-class:: api-main-section

Types
=====

.. _privacy.network.^h^t^t^p^s^only^mode^option:

HTTPSOnlyModeOption
-------------------

.. api-section-annotation-hack:: 

The mode for https-only mode.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _privacy.network.^h^t^t^p^s^only^mode^option.always:

         .. api-member::
            :name: :value:`always`
            :refid: privacy-network-h-t-t-p-s-only-mode-option-always
            :refname: always

         .. _privacy.network.^h^t^t^p^s^only^mode^option.never:

         .. api-member::
            :name: :value:`never`
            :refid: privacy-network-h-t-t-p-s-only-mode-option-never
            :refname: never

         .. _privacy.network.^h^t^t^p^s^only^mode^option.private_browsing:

         .. api-member::
            :name: :value:`private_browsing`
            :refid: privacy-network-h-t-t-p-s-only-mode-option-private-browsing
            :refname: private_browsing

.. _privacy.network.^i^p^handling^policy:

IPHandlingPolicy
----------------

.. api-section-annotation-hack:: 

The IP handling policy of WebRTC.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _privacy.network.^i^p^handling^policy.default:

         .. api-member::
            :name: :value:`default`
            :refid: privacy-network-i-p-handling-policy-default
            :refname: default

         .. _privacy.network.^i^p^handling^policy.default_public_and_private_interfaces:

         .. api-member::
            :name: :value:`default_public_and_private_interfaces`
            :refid: privacy-network-i-p-handling-policy-default-public-and-private-interfaces
            :refname: default_public_and_private_interfaces

         .. _privacy.network.^i^p^handling^policy.default_public_interface_only:

         .. api-member::
            :name: :value:`default_public_interface_only`
            :refid: privacy-network-i-p-handling-policy-default-public-interface-only
            :refname: default_public_interface_only

         .. _privacy.network.^i^p^handling^policy.disable_non_proxied_udp:

         .. api-member::
            :name: :value:`disable_non_proxied_udp`
            :refid: privacy-network-i-p-handling-policy-disable-non-proxied-udp
            :refname: disable_non_proxied_udp

         .. _privacy.network.^i^p^handling^policy.proxy_only:

         .. api-member::
            :name: :value:`proxy_only`
            :refid: privacy-network-i-p-handling-policy-proxy-only
            :refname: proxy_only

.. _privacy.network.tls^version^restriction^config:

tlsVersionRestrictionConfig
---------------------------

.. api-section-annotation-hack:: 

An object which describes TLS minimum and maximum versions.

.. api-header::
   :label: object

   .. _privacy.network.tls^version^restriction^config.maximum:

   .. api-member::
      :name: [``maximum``]
      :refid: privacy-network-tls-version-restriction-config-maximum
      :refname: maximum
      :type: (`string`, optional)

      The maximum TLS version supported.

      Supported values:

      .. _privacy.network.tls^version^restriction^config.maximum.^t^l^sv1:

      .. api-member::
         :name: :value:`TLSv1`
         :refid: privacy-network-tls-version-restriction-config-maximum-t-l-sv1
         :refname: TLSv1

      .. _privacy.network.tls^version^restriction^config.maximum.^t^l^sv1.1:

      .. api-member::
         :name: :value:`TLSv1.1`
         :refid: privacy-network-tls-version-restriction-config-maximum-t-l-sv1-1
         :refname: TLSv1.1

      .. _privacy.network.tls^version^restriction^config.maximum.^t^l^sv1.2:

      .. api-member::
         :name: :value:`TLSv1.2`
         :refid: privacy-network-tls-version-restriction-config-maximum-t-l-sv1-2
         :refname: TLSv1.2

      .. _privacy.network.tls^version^restriction^config.maximum.^t^l^sv1.3:

      .. api-member::
         :name: :value:`TLSv1.3`
         :refid: privacy-network-tls-version-restriction-config-maximum-t-l-sv1-3
         :refname: TLSv1.3

      .. _privacy.network.tls^version^restriction^config.maximum.unknown:

      .. api-member::
         :name: :value:`unknown`
         :refid: privacy-network-tls-version-restriction-config-maximum-unknown
         :refname: unknown

   .. _privacy.network.tls^version^restriction^config.minimum:

   .. api-member::
      :name: [``minimum``]
      :refid: privacy-network-tls-version-restriction-config-minimum
      :refname: minimum
      :type: (`string`, optional)

      The minimum TLS version supported.

      Supported values:

      .. _privacy.network.tls^version^restriction^config.minimum.^t^l^sv1:

      .. api-member::
         :name: :value:`TLSv1`
         :refid: privacy-network-tls-version-restriction-config-minimum-t-l-sv1
         :refname: TLSv1

      .. _privacy.network.tls^version^restriction^config.minimum.^t^l^sv1.1:

      .. api-member::
         :name: :value:`TLSv1.1`
         :refid: privacy-network-tls-version-restriction-config-minimum-t-l-sv1-1
         :refname: TLSv1.1

      .. _privacy.network.tls^version^restriction^config.minimum.^t^l^sv1.2:

      .. api-member::
         :name: :value:`TLSv1.2`
         :refid: privacy-network-tls-version-restriction-config-minimum-t-l-sv1-2
         :refname: TLSv1.2

      .. _privacy.network.tls^version^restriction^config.minimum.^t^l^sv1.3:

      .. api-member::
         :name: :value:`TLSv1.3`
         :refid: privacy-network-tls-version-restriction-config-minimum-t-l-sv1-3
         :refname: TLSv1.3

      .. _privacy.network.tls^version^restriction^config.minimum.unknown:

      .. api-member::
         :name: :value:`unknown`
         :refid: privacy-network-tls-version-restriction-config-minimum-unknown
         :refname: unknown

.. rst-class:: api-main-section

Properties
==========

.. _privacy.network.global^privacy^control:

globalPrivacyControl
--------------------

.. api-section-annotation-hack:: 

Allow users to query the status of 'Global Privacy Control'. This setting's value is of type boolean, defaulting to :code:`false`.

.. _privacy.network.https^only^mode:

httpsOnlyMode
-------------

.. api-section-annotation-hack:: 

Allow users to query the mode for 'HTTPS-Only Mode'. This setting's value is of type HTTPSOnlyModeOption, defaulting to :code:`never`.

.. _privacy.network.network^prediction^enabled:

networkPredictionEnabled
------------------------

.. api-section-annotation-hack:: 

If enabled, the browser attempts to speed up your web browsing experience by pre-resolving DNS entries, prerendering sites (:code:`&lt;link rel='prefetch' ...&gt;`), and preemptively opening TCP and SSL connections to servers.  This preference's value is a boolean, defaulting to :code:`true`.

.. _privacy.network.peer^connection^enabled:

peerConnectionEnabled
---------------------

.. api-section-annotation-hack:: 

Allow users to enable and disable RTCPeerConnections (aka WebRTC).

.. _privacy.network.tls^version^restriction:

tlsVersionRestriction
---------------------

.. api-section-annotation-hack:: 

This property controls the minimum and maximum TLS versions. This setting's value is an object of :ref:`privacy.network.tls^version^restriction^config`.

.. _privacy.network.web^r^t^c^i^p^handling^policy:

webRTCIPHandlingPolicy
----------------------

.. api-section-annotation-hack:: 

Allow users to specify the media performance/privacy tradeoffs which impacts how WebRTC traffic will be routed and how much local address information is exposed. This preference's value is of type IPHandlingPolicy, defaulting to :code:`default`.

.. note::

   Starting in Thunderbird 70, a value of :code:`disable_non_proxied_udp` requires a proxy if one is configured, but allows connections to go through if no proxy is set up. Previously, in this mode WebRTC could only be used if a proxy was configured and TURN over TCP was available; this behavior is now exposed as :code:`proxy_only`.
