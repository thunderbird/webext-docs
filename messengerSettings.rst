.. container:: sticky-sidebar

  ≡ messengerSettings API

  * `Permissions`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

=====================
messengerSettings API
=====================

.. role:: permission

.. role:: value

.. role:: code

The messengerSettings API allows to access global messenger settings.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _messenger^settings.permission.messenger^settings:

.. api-member::
   :name: :permission:`messengerSettings`
   :refid: messenger-settings-permission-messenger-settings

   Read Thunderbird settings.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messengerSettings` is required to use ``messenger.messengerSettings.*``.

.. rst-class:: api-main-section

Properties
==========

.. _messenger^settings.message^line^length^limit:

messageLineLengthLimit
----------------------

.. api-section-annotation-hack:: 

The line length limit for outgoing messages, to comply with requirements from RFC 2822. See description of :ref:`messenger^settings.message^plain^text^flowed^output^enabled`.

.. _messenger^settings.message^plain^text^flowed^output^enabled:

messagePlainTextFlowedOutputEnabled
-----------------------------------

.. api-section-annotation-hack:: 

Whether long lines in outgoing plain text messages will get soft line breaks (:value:`​ \\n`) or hard line breaks (:value:`\\n`), to comply with requirements from RFC 2822. Soft line breaks will be ignored when displayed by the receiving client. When flowed output is enabled, add-ons should not create plain text messages with manually inserted hard or soft line breaks to achieve a certain text width, as that will most probably interfere with the default line break handling and generate ridged text. When flowed output is disabled, add-ons could add hard line breaks to have control over the final message, but any line longer than the maximum line length will still receive additional hard line breaks. See :ref:`messenger^settings.message^line^length^limit`.
