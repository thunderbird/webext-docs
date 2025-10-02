.. container:: sticky-sidebar

  ≡ messengerUtilities API

  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

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

.. _messenger^utilities.convert^to^plain^text:

convertToPlainText(body, [options])
-----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Converts the provided body to readable plain text, without tags and leading/trailing whitespace.

.. api-header::
   :label: Parameters

   .. _messenger^utilities.convert^to^plain^text.body:

   .. api-member::
      :name: ``body``
      :refid: messenger-utilities-convert-to-plain-text-body
      :type: (string)

      The to-be-converted body.

   .. _messenger^utilities.convert^to^plain^text.options:

   .. api-member::
      :name: [``options``]
      :refid: messenger-utilities-convert-to-plain-text-options
      :type: (object, optional)

      .. _messenger^utilities.convert^to^plain^text.options.flowed:

      .. api-member::
         :name: [``flowed``]
         :refid: messenger-utilities-convert-to-plain-text-options-flowed
         :type: (boolean, optional)

         The converted plain text will be wrapped to lines not longer than 72 characters and use format flowed, as defined by RFC 2646.

.. api-header::
   :label: Return type (`Promise`_)

   .. _messenger^utilities.convert^to^plain^text.returns:

   .. api-member::
      :refid: messenger-utilities-convert-to-plain-text-returns
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messenger^utilities.decode^mime^header:

decodeMimeHeader(headerName, headerValue, [isMailBoxHeader])
------------------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Decode the provided header into a readable format according to RFC 2047.

.. api-header::
   :label: Parameters

   .. _messenger^utilities.decode^mime^header.header^name:

   .. api-member::
      :name: ``headerName``
      :refid: messenger-utilities-decode-mime-header-header-name
      :type: (string)

   .. _messenger^utilities.decode^mime^header.header^value:

   .. api-member::
      :name: ``headerValue``
      :refid: messenger-utilities-decode-mime-header-header-value
      :type: (string or array of string)

   .. _messenger^utilities.decode^mime^header.is^mail^box^header:

   .. api-member::
      :name: [``isMailBoxHeader``]
      :refid: messenger-utilities-decode-mime-header-is-mail-box-header
      :type: (boolean, optional)

      Headers containing multiple mailbox strings need special handling. For example the header :value:`=?UTF-8?Q?H=C3=B6rst=2C_Kenny?= <K.Hoerst@invalid>, new@thunderbird.bug` will be wrongly decoded to :value:`Hörst, Kenny <K.Hoerst@invalid>, new@thunderbird.bug`, corrupting the structure of the first mailbox string. This option overrides the default behavior of treating the headers defined in :ref:`messenger^utilities.^mailbox^headers` as mailbox headers.

.. api-header::
   :label: Return type (`Promise`_)

   .. _messenger^utilities.decode^mime^header.returns:

   .. api-member::
      :refid: messenger-utilities-decode-mime-header-returns
      :type: array of string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messenger^utilities.encode^mime^header:

encodeMimeHeader(headerName, headerValue, [isMailBoxHeader])
------------------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Encode the provided header according to RFC 2047.

.. api-header::
   :label: Parameters

   .. _messenger^utilities.encode^mime^header.header^name:

   .. api-member::
      :name: ``headerName``
      :refid: messenger-utilities-encode-mime-header-header-name
      :type: (string)

   .. _messenger^utilities.encode^mime^header.header^value:

   .. api-member::
      :name: ``headerValue``
      :refid: messenger-utilities-encode-mime-header-header-value
      :type: (string or array of string)

   .. _messenger^utilities.encode^mime^header.is^mail^box^header:

   .. api-member::
      :name: [``isMailBoxHeader``]
      :refid: messenger-utilities-encode-mime-header-is-mail-box-header
      :type: (boolean, optional)

      Headers containing multiple mailbox strings need special handling. This option overrides the default behavior of treating the headers defined in :ref:`messenger^utilities.^mailbox^headers` as mailbox headers.

.. api-header::
   :label: Return type (`Promise`_)

   .. _messenger^utilities.encode^mime^header.returns:

   .. api-member::
      :refid: messenger-utilities-encode-mime-header-returns
      :type: array of string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messenger^utilities.format^file^size:

formatFileSize(sizeInBytes)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Returns the provided file size in a human readable format (e.g. :value:`12 bytes` or :value:`11,4 GB`).

.. api-header::
   :label: Parameters

   .. _messenger^utilities.format^file^size.size^in^bytes:

   .. api-member::
      :name: ``sizeInBytes``
      :refid: messenger-utilities-format-file-size-size-in-bytes
      :type: (integer)

      The size in bytes.

.. api-header::
   :label: Return type (`Promise`_)

   .. _messenger^utilities.format^file^size.returns:

   .. api-member::
      :refid: messenger-utilities-format-file-size-returns
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _messenger^utilities.parse^mailbox^string:

parseMailboxString(mailboxString, [preserveGroups])
---------------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Parse a mailbox string containing one or more email addresses (see RFC 5322, section 3.4).

.. api-header::
   :label: Parameters

   .. _messenger^utilities.parse^mailbox^string.mailbox^string:

   .. api-member::
      :name: ``mailboxString``
      :refid: messenger-utilities-parse-mailbox-string-mailbox-string
      :type: (string)

      The string to be parsed (e.g. :value:`User <user@example.com>, other-user@example.com`)

   .. _messenger^utilities.parse^mailbox^string.preserve^groups:

   .. api-member::
      :name: [``preserveGroups``]
      :refid: messenger-utilities-parse-mailbox-string-preserve-groups
      :type: (boolean, optional)

      Keep grouped hierarchies. Groups may be specified in a mailbox string as follows: :value:`GroupName : user1 <user1@example.com>, user2@example,com ;`.

.. api-header::
   :label: Return type (`Promise`_)

   .. _messenger^utilities.parse^mailbox^string.returns:

   .. api-member::
      :refid: messenger-utilities-parse-mailbox-string-returns
      :type: array of :ref:`messenger^utilities.^parsed^mailbox`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Types
=====

.. _messenger^utilities.^mailbox^headers:

MailboxHeaders
--------------

.. api-section-annotation-hack:: -- [Added in TB 137]

MIME headers, which by default are treated as containing one or more mailbox strings.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _messenger^utilities.^mailbox^headers.approved:

         .. api-member::
            :name: :value:`approved`
            :refid: messenger-utilities-mailbox-headers-approved

         .. _messenger^utilities.^mailbox^headers.bcc:

         .. api-member::
            :name: :value:`bcc`
            :refid: messenger-utilities-mailbox-headers-bcc

         .. _messenger^utilities.^mailbox^headers.cc:

         .. api-member::
            :name: :value:`cc`
            :refid: messenger-utilities-mailbox-headers-cc

         .. _messenger^utilities.^mailbox^headers.delivered-to:

         .. api-member::
            :name: :value:`delivered-to`
            :refid: messenger-utilities-mailbox-headers-delivered-to

         .. _messenger^utilities.^mailbox^headers.disposition-notification-to:

         .. api-member::
            :name: :value:`disposition-notification-to`
            :refid: messenger-utilities-mailbox-headers-disposition-notification-to

         .. _messenger^utilities.^mailbox^headers.from:

         .. api-member::
            :name: :value:`from`
            :refid: messenger-utilities-mailbox-headers-from

         .. _messenger^utilities.^mailbox^headers.mail-followup-to:

         .. api-member::
            :name: :value:`mail-followup-to`
            :refid: messenger-utilities-mailbox-headers-mail-followup-to

         .. _messenger^utilities.^mailbox^headers.mail-reply-to:

         .. api-member::
            :name: :value:`mail-reply-to`
            :refid: messenger-utilities-mailbox-headers-mail-reply-to

         .. _messenger^utilities.^mailbox^headers.reply-to:

         .. api-member::
            :name: :value:`reply-to`
            :refid: messenger-utilities-mailbox-headers-reply-to

         .. _messenger^utilities.^mailbox^headers.resent-bcc:

         .. api-member::
            :name: :value:`resent-bcc`
            :refid: messenger-utilities-mailbox-headers-resent-bcc

         .. _messenger^utilities.^mailbox^headers.resent-cc:

         .. api-member::
            :name: :value:`resent-cc`
            :refid: messenger-utilities-mailbox-headers-resent-cc

         .. _messenger^utilities.^mailbox^headers.resent-from:

         .. api-member::
            :name: :value:`resent-from`
            :refid: messenger-utilities-mailbox-headers-resent-from

         .. _messenger^utilities.^mailbox^headers.resent-reply-to:

         .. api-member::
            :name: :value:`resent-reply-to`
            :refid: messenger-utilities-mailbox-headers-resent-reply-to

         .. _messenger^utilities.^mailbox^headers.resent-sender:

         .. api-member::
            :name: :value:`resent-sender`
            :refid: messenger-utilities-mailbox-headers-resent-sender

         .. _messenger^utilities.^mailbox^headers.resent-to:

         .. api-member::
            :name: :value:`resent-to`
            :refid: messenger-utilities-mailbox-headers-resent-to

         .. _messenger^utilities.^mailbox^headers.return-receipt-to:

         .. api-member::
            :name: :value:`return-receipt-to`
            :refid: messenger-utilities-mailbox-headers-return-receipt-to

         .. _messenger^utilities.^mailbox^headers.sender:

         .. api-member::
            :name: :value:`sender`
            :refid: messenger-utilities-mailbox-headers-sender

         .. _messenger^utilities.^mailbox^headers.to:

         .. api-member::
            :name: :value:`to`
            :refid: messenger-utilities-mailbox-headers-to

.. _messenger^utilities.^parsed^mailbox:

ParsedMailbox
-------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Representation of a parsed mailbox string (see RFC 5322, section 3.4).

.. api-header::
   :label: object

   .. _messenger^utilities.^parsed^mailbox.email:

   .. api-member::
      :name: [``email``]
      :refid: messenger-utilities-parsed-mailbox-email
      :type: (string, optional)

      The :value:`addr-spec` associated with the provided address, if available.

   .. _messenger^utilities.^parsed^mailbox.group:

   .. api-member::
      :name: [``group``]
      :refid: messenger-utilities-parsed-mailbox-group
      :type: (array of :ref:`messenger^utilities.^parsed^mailbox`, optional)

      The members of the group, if available.

   .. _messenger^utilities.^parsed^mailbox.name:

   .. api-member::
      :name: [``name``]
      :refid: messenger-utilities-parsed-mailbox-name
      :type: (string, optional)

      The :value:`display-name` associated with the provided address or group, if available.
