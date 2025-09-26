.. container:: sticky-sidebar

  ≡ messengerUtilities API

  * `Functions`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

======================
messengerUtilities API
======================

.. role:: permission

.. role:: value

.. role:: code

The messengerUtilities API provides helpful methods for working with messages and emails.

.. rst-class:: api-main-section

Functions
=========

.. _messengerUtilities.convertToPlainText:

convertToPlainText(body, [options])
-----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Converts the provided body to readable plain text, without tags and leading/trailing whitespace.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``body``
      :type: (string)

      The to-be-converted body.

   .. api-member::
      :name: [``options``]
      :type: (object, optional)

      .. api-member::
         :name: [``flowed``]
         :type: (boolean, optional)

         The converted plain text will be wrapped to lines not longer than 72 characters and use format flowed, as defined by RFC 2646.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messengerUtilities.decodeMimeHeader:

decodeMimeHeader(headerName, headerValue, [isMailBoxHeader])
------------------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Decode the provided header into a readable format according to RFC 2047.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``headerName``
      :type: (string)

   .. api-member::
      :name: ``headerValue``
      :type: (string or array of string)

   .. api-member::
      :name: [``isMailBoxHeader``]
      :type: (boolean, optional)

      Headers containing multiple mailbox strings need special handling. For example the header :value:`=?UTF-8?Q?H=C3=B6rst=2C_Kenny?= <K.Hoerst@invalid>, new@thunderbird.bug` will be wrongly decoded to :value:`Hörst, Kenny <K.Hoerst@invalid>, new@thunderbird.bug`, corrupting the structure of the first mailbox string. This option overrides the default behavior of treating the headers defined in :ref:`messengerUtilities.MailboxHeaders` as mailbox headers.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messengerUtilities.encodeMimeHeader:

encodeMimeHeader(headerName, headerValue, [isMailBoxHeader])
------------------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Encode the provided header according to RFC 2047.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``headerName``
      :type: (string)

   .. api-member::
      :name: ``headerValue``
      :type: (string or array of string)

   .. api-member::
      :name: [``isMailBoxHeader``]
      :type: (boolean, optional)

      Headers containing multiple mailbox strings need special handling. This option overrides the default behavior of treating the headers defined in :ref:`messengerUtilities.MailboxHeaders` as mailbox headers.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messengerUtilities.formatFileSize:

formatFileSize(sizeInBytes)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Returns the provided file size in a human readable format (e.g. :value:`12 bytes` or :value:`11,4 GB`).

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``sizeInBytes``
      :type: (integer)

      The size in bytes.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messengerUtilities.parseMailboxString:

parseMailboxString(mailboxString, [preserveGroups])
---------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Parse a mailbox string containing one or more email addresses (see RFC 5322, section 3.4).

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``mailboxString``
      :type: (string)

      The string to be parsed (e.g. :value:`User <user@example.com>, other-user@example.com`)

   .. api-member::
      :name: [``preserveGroups``]
      :type: (boolean, optional)

      Keep grouped hierarchies. Groups may be specified in a mailbox string as follows: :value:`GroupName : user1 <user1@example.com>, user2@example,com ;`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`ParsedMailbox`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Types
=====

.. _messengerUtilities.ParsedMailbox:

ParsedMailbox
-------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Representation of a parsed mailbox string (see RFC 5322, section 3.4).

.. api-header::
   :label: object

   .. _messengerUtilities.ParsedMailbox.email:

   .. api-member::
      :name: [``email``]
      :type: (string, optional)

      The :value:`addr-spec` associated with the provided address, if available.

   .. _messengerUtilities.ParsedMailbox.group:

   .. api-member::
      :name: [``group``]
      :type: (array of :ref:`ParsedMailbox`, optional)

      The members of the group, if available.

   .. _messengerUtilities.ParsedMailbox.name:

   .. api-member::
      :name: [``name``]
      :type: (string, optional)

      The :value:`display-name` associated with the provided address or group, if available.
