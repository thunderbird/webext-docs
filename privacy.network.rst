.. container:: sticky-sidebar

  ≡ privacy.network API

  * `Permissions`_
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

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`privacy`

   Read and modify privacy settings

Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`privacy` is required to use ``messenger.privacy.network.*``.

.. rst-class:: api-main-section

Properties
==========

.. _privacy.network.globalPrivacyControl:

globalPrivacyControl
--------------------

.. api-section-annotation-hack:: 

Allow users to query the status of 'Global Privacy Control'. This setting's value is of type boolean, defaulting to :code:`false`.

.. _privacy.network.httpsOnlyMode:

httpsOnlyMode
-------------

.. api-section-annotation-hack:: 

Allow users to query the mode for 'HTTPS-Only Mode'. This setting's value is of type HTTPSOnlyModeOption, defaulting to :code:`never`.

.. _privacy.network.networkPredictionEnabled:

networkPredictionEnabled
------------------------

.. api-section-annotation-hack:: 

If enabled, the browser attempts to speed up your web browsing experience by pre-resolving DNS entries, prerendering sites (:code:`&lt;link rel='prefetch' ...&gt;`), and preemptively opening TCP and SSL connections to servers.  This preference's value is a boolean, defaulting to :code:`true`.

.. _privacy.network.peerConnectionEnabled:

peerConnectionEnabled
---------------------

.. api-section-annotation-hack:: 

Allow users to enable and disable RTCPeerConnections (aka WebRTC).

.. _privacy.network.tlsVersionRestriction:

tlsVersionRestriction
---------------------

.. api-section-annotation-hack:: 

This property controls the minimum and maximum TLS versions. This setting's value is an object of :ref:`privacy.network.tlsVersionRestrictionConfig`.

.. _privacy.network.webRTCIPHandlingPolicy:

webRTCIPHandlingPolicy
----------------------

.. api-section-annotation-hack:: 

Allow users to specify the media performance/privacy tradeoffs which impacts how WebRTC traffic will be routed and how much local address information is exposed. This preference's value is of type IPHandlingPolicy, defaulting to :code:`default`.

.. note::

   Starting in Thunderbird 70, a value of :code:`disable_non_proxied_udp` requires a proxy if one is configured, but allows connections to go through if no proxy is set up. Previously, in this mode WebRTC could only be used if a proxy was configured and TURN over TCP was available; this behavior is now exposed as :code:`proxy_only`.
