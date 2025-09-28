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

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`messengerSettings`

   Read Thunderbird settings

Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messengerSettings` is required to use ``messenger.messengerSettings.*``.

.. rst-class:: api-main-section

Properties
==========

.. _messengerSettings.messageLineLengthLimit:

messageLineLengthLimit
----------------------

.. api-section-annotation-hack:: 

The line length limit for outgoing messages, to comply with requirements from RFC 2822. See description of :ref:`messengerSettings.messagePlainTextFlowedOutputEnabled`.

.. _messengerSettings.messagePlainTextFlowedOutputEnabled:

messagePlainTextFlowedOutputEnabled
-----------------------------------

.. api-section-annotation-hack:: 

Whether long lines in outgoing plain text messages will get soft line breaks (:value:`​ \\n`) or hard line breaks (:value:`\\n`), to comply with requirements from RFC 2822. Soft line breaks will be ignored when displayed by the receiving client. When flowed output is enabled, add-ons should not create plain text messages with manually inserted hard or soft line breaks to achieve a certain text width, as that will most probably interfere with the default line break handling and generate ridged text. When flowed output is disabled, add-ons could add hard line breaks to have control over the final message, but any line longer than the maximum line length will still receive additional hard line breaks. See :ref:`messengerSettings.messageLineLengthLimit`.
