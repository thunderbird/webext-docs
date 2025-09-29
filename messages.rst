.. container:: sticky-sidebar

  ≡ messages API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

============
messages API
============

.. role:: permission

.. role:: value

.. role:: code

The messages API allows to access and manage the user's messages.

.. note::

   When the term :value:`messageId` is used in these documents, it *doesn't* refer to the Message-ID email header. It is an internal tracking number that does not remain after a restart. Nor does it follow an email that has been moved to a different folder.

.. warning::

   Some functions in this API potentially return a lot of messages. See :doc:`guides/messageLists` for more information.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`accountsRead`

   See your mail accounts, their identities and their folders.

.. api-member::
   :name: :permission:`messagesDelete`

   Permanently delete your email messages.

.. api-member::
   :name: :permission:`messagesImport`

   Import messages into Thunderbird.

.. api-member::
   :name: :permission:`messagesModifyPermanent`

   Permanently modify the source of your messages (including headers, body and attachments).

.. api-member::
   :name: :permission:`messagesMove`

   Copy or move your email messages (including moving them to the trash folder).

.. api-member::
   :name: :permission:`messagesRead`

   Read your email messages.

.. api-member::
   :name: :permission:`messagesUpdate`

   Change properties and tags of your email messages.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messagesRead` is required to use ``messenger.messages.*``.

.. rst-class:: api-main-section

Functions
=========

.. _messages.abort^list:

abortList(messageListId)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 120]

Finalizes the specified list and terminates any process currently still adding messages.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageListId``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.archive:

archive(messageIds)
-------------------

.. api-section-annotation-hack:: -- [Added in TB 68]

Archives messages using the current settings. Archiving external messages will throw an *ExtensionError*.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageIds``
      :type: (array of :ref:`messages.^message^id`)

      The IDs of the messages to archive.

.. api-header::
   :label: Required permissions

   - :permission:`messagesMove`
   - :permission:`messagesRead`

.. _messages.continue^list:

continueList(messageListId)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Returns the next chunk of messages in a list. See :doc:`guides/messageLists` for more information.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageListId``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`messages.^message^list`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.copy:

copy(messageIds, folderId, [options])
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Copies messages to a specified folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageIds``
      :type: (array of :ref:`messages.^message^id`)

      The IDs of the messages to copy.

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`folders.^mail^folder^id`)

      The folder to copy the messages to.

   .. api-member::
      :name: [``options``]
      :type: (object, optional)
      :annotation: -- [Added in TB 137]

      .. api-member::
         :name: [``isUserAction``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 137]

         Whether this copy operation should be treated as a user action, for example allowing undo.

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesMove`
   - :permission:`messagesRead`

.. _messages.delete:

delete(messageIds, [options])
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Deletes messages permanently, or moves them to the trash folder (honoring the account's deletion behavior settings). Deleting external messages will throw an *ExtensionError*. The :value:`deletePermanently` parameter allows immediate permanent deletion, bypassing the trash folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageIds``
      :type: (array of :ref:`messages.^message^id`)

      The IDs of the messages to delete.

   .. api-member::
      :name: [``options``]
      :type: (boolean or object, optional)

.. api-header::
   :label: Required permissions

   - :permission:`messagesDelete`
   - :permission:`messagesRead`

.. _messages.delete^attachments:

deleteAttachments(messageId, partNames)
---------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 123]

Deletes the specified attachments and replaces them by placeholder text attachments with meta information about the original attachments and a :value:`text/x-moz-deleted` content type. This permanently modifies the message.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageId``
      :type: (integer)

   .. api-member::
      :name: ``partNames``
      :type: (array of string)

      An array of attachments, identifying the to be deleted attachments by their :value:`partName`.

.. api-header::
   :label: Required permissions

   - :permission:`messagesModifyPermanent`
   - :permission:`messagesRead`

.. _messages.get:

get(messageId)
--------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Returns the specified message.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageId``
      :type: (:ref:`messages.^message^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`messages.^message^header`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.get^attachment^file:

getAttachmentFile(messageId, partName)
--------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 88]

Gets the content of a :ref:`messages.^message^attachment` as a `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__ object.

The most simple way to get the content of an attachment is to use the `text() <https://developer.mozilla.org/en-US/docs/Web/API/Blob/text>`__ method of the returned `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__ object:

.. code-block:: JavaScript

   let attachments = await browser.messages.listAttachments(messageId);
   for (let att of attachments) {
     let file = await browser.messages.getAttachmentFile(messageId, att.partName);
     let content = await file.text();
   }

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageId``
      :type: (:ref:`messages.^message^id`)

   .. api-member::
      :name: ``partName``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.get^full:

getFull(messageId, [options])
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Returns the specified message, including all headers and MIME parts. Throws if the message could not be read, for example due to network issues.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageId``
      :type: (:ref:`messages.^message^id`)

   .. api-member::
      :name: [``options``]
      :type: (object, optional)
      :annotation: -- [Added in TB 96]

      .. api-member::
         :name: [``decodeContent``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 133]

         Whether to decode quoted-printable or base64 encoded content of message parts. Defaults to :value:`true`.

      .. api-member::
         :name: [``decodeHeaders``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 133]

         Whether to decode RFC 2047 encoded headers of message parts. Defaults to :value:`true`.

      .. api-member::
         :name: [``decrypt``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 125]

         Whether the message should be decrypted. If the message could not be decrypted, its parts are omitted. Defaults to :value:`true`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`messages.^message^part`
      :annotation: -- [Added in TB 125]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.get^raw:

getRaw(message, [options])
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 72]

Returns the raw content of a message. Throws if the message could not be read, for example due to network issues.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``message``
      :type: (:ref:`messages.^message^id` or :ref:`messages.^message^part`)

      Either a :ref:`messages.^message^id` of an existing message, or a :ref:`messages.^message^part` with raw header and raw content data representing a full RFC 822 message (the provided data will be used as-is without applying any further encoding). See the :value:`decodeHeaders` and :value:`decodeContent` options of :ref:`messages.get^full` for further details on how to retrieve a :ref:`messages.^message^part` with raw values. You can use :ref:`messenger^utilities.decode^mime^header` and :ref:`messenger^utilities.encode^mime^header` to manipulate a raw MessagePart.

   .. api-member::
      :name: [``options``]
      :type: (object, optional)
      :annotation: -- [Added in TB 96]

      .. api-member::
         :name: [``data_format``]
         :type: (`string`, optional)
         :annotation: -- [Added in TB 117]

         The message can either be returned as a DOM File (default) or as a `binary string <https://udn.realityripple.com/docs/Web/API/DOMString/Binary>`__. It is recommended to use the :value:`File` format, because the DOM File object can be used as-is with the downloads API and has useful methods to access the content, like `File.text() <https://developer.mozilla.org/en-US/docs/Web/API/Blob/text>`__ and `File.arrayBuffer() <https://developer.mozilla.org/en-US/docs/Web/API/Blob/arrayBuffer>`__.

         Working with binary strings is error prone and needs special handling:

         .. code-block:: JavaScript

            /**
             * Decodes a binary string using the given encoding format and returns a
             * JavaScript string. Produces mangled output if used with anything but a binary
             * input string.
             */
            function decodeBinaryString(binaryString, inputEncoding = "utf-8") {
              const buffer = new Uint8Array(binaryString.length);
              for (let i = 0; i < binaryString.length; i++) {
                buffer[i] = binaryString.charCodeAt(i) & 0xff;
              }
              const decoder = new TextDecoder(inputEncoding);
              return decoder.decode(buffer);
            }

          See MDN for `supported input encodings <https://developer.mozilla.org/en-US/docs/Web/API/Encoding_API/Encodings>`__.

         Supported values:

         .. api-member::
            :name: :value:`BinaryString`

         .. api-member::
            :name: :value:`File`

      .. api-member::
         :name: [``decrypt``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 125]

         Whether the message should be decrypted. Throws, if the message could not be decrypted.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string or `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__
      :annotation: -- [Added in TB 117]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.import:

import(file, folderId, [properties])
------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 106]

Imports a message into a folder. Supports local folders, POP and IMAP folders. Throws, if the destination folder already contains a message with the Message-ID of the message being imported.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``file``
      :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__)

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`folders.^mail^folder^id`)

      The folder to import the messages into.

   .. api-member::
      :name: [``properties``]
      :type: (:ref:`messages.^message^properties`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`messages.^message^header`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesImport`
   - :permission:`messagesRead`

.. _messages.list:

list(folderId)
--------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Gets all messages in a folder.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`folders.^mail^folder^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`messages.^message^list`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesRead`

.. _messages.list^attachments:

listAttachments(messageId)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 88]

Lists the attachments of a message.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageId``
      :type: (:ref:`messages.^message^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`messages.^message^attachment`
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.list^inline^text^parts:

listInlineTextParts(messageId)
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Lists all inline text parts of a message. These parts are not returned by :ref:`messages.list^attachments` and usually make up the readable content of the message, mostly with content type :value:`text/plain` or :value:`text/html`. If a message only includes a part with content type :value:`text/html`, the method :ref:`messenger^utilities.convert^to^plain^text` can be used to retreive a plain text version.

.. note::

   A message usually contains only one inline text part per subtype, but technically messages can contain multiple inline text parts per subtype.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageId``
      :type: (:ref:`messages.^message^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`messages.^inline^text^part`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.move:

move(messageIds, folderId, [options])
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Moves messages to a specified folder. If the messages cannot be removed from the source folder, they will be copied instead of moved. Moving external messages will throw an *ExtensionError*.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageIds``
      :type: (array of :ref:`messages.^message^id`)

      The IDs of the messages to move.

   .. api-member::
      :name: ``folderId``
      :type: (:ref:`folders.^mail^folder^id`)

      The folder to move the messages to.

   .. api-member::
      :name: [``options``]
      :type: (object, optional)
      :annotation: -- [Added in TB 137]

      .. api-member::
         :name: [``isUserAction``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 137]

         Whether this move operation should be treated as a user action, for example allowing undo.

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesMove`
   - :permission:`messagesRead`

.. _messages.open^attachment:

openAttachment(messageId, partName, tabId)
------------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 114]

Opens the specified attachment.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageId``
      :type: (:ref:`messages.^message^id`)

   .. api-member::
      :name: ``partName``
      :type: (string)

   .. api-member::
      :name: ``tabId``
      :type: (integer)

      The ID of the tab associated with the message opening.

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.query:

query([queryInfo])
------------------

.. api-section-annotation-hack:: -- [Added in TB 69]

Gets all messages that have the specified properties, or all messages if no properties are specified. Messages of unified mailbox folders are not included by default (as that could double the amount of returned messages), but explicitly specifying a unified mailbox folder is supported.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``queryInfo``]
      :type: (object, optional)

      .. api-member::
         :name: [``accountId``]
         :type: (:ref:`accounts.^mail^account^id` or array of :ref:`accounts.^mail^account^id`, optional)
         :annotation: -- [Added in TB 121]

         Limits the search to the specified account(s). Accounts are searched in the specified order.

      .. api-member::
         :name: [``attachment``]
         :type: (boolean or :ref:`messages.^query^range`, optional)
         :annotation: -- [Added in TB 96]

         Whether the message has attachments, or not. Supports to specify a :ref:`messages.^query^range` (min/max) instead of a simple boolean value (none/some).

      .. api-member::
         :name: [``author``]
         :type: (string, optional)

         Returns only messages with this value matching the author. The search value is a single email address, a name or a combination (e.g.: :value:`Name <user@domain.org>`). The address part of the search value (if provided) must match the author's address completely. The name part of the search value (if provided) must match the author's name partially. All matches are done case-insensitive.

      .. api-member::
         :name: [``autoPaginationTimeout``]
         :type: (integer, optional)
         :annotation: -- [Added in TB 120]

         Set the timeout in ms after which results should be returned, even if the nominal number of messages-per-page has not yet been reached. Defaults to :value:`1000` ms. Setting it to :value:`0` will disable auto-pagination.

      .. api-member::
         :name: [``body``]
         :type: (string, optional)

         Returns only messages with this value in the body of the mail.

      .. api-member::
         :name: [``flagged``]
         :type: (boolean, optional)

         Returns only flagged (or unflagged if false) messages.

      .. api-member::
         :name: [``folderId``]
         :type: (:ref:`folders.^mail^folder^id` or array of :ref:`folders.^mail^folder^id`, optional)
         :annotation: -- [Added in TB 121]

         Limits the search to the specified folder(s). Folders are searched in the specified order. The :permission:`accountsRead` permission is required.

      .. api-member::
         :name: [``fromDate``]
         :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)

         Returns only messages with a date after this value.

      .. api-member::
         :name: [``fromMe``]
         :type: (boolean, optional)

         Returns only messages with the author's address matching any configured identity.

      .. api-member::
         :name: [``fullText``]
         :type: (string, optional)

         Returns only messages with this value somewhere in the mail (subject, body or author).

      .. api-member::
         :name: [``headerMessageId``]
         :type: (string, optional)
         :annotation: -- [Added in TB 85]

         Returns only messages with a Message-ID header matching this value.

      .. api-member::
         :name: [``includeSubFolders``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 91]

         Search the specified folder recursively.

      .. api-member::
         :name: [``junk``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 121]

         Returns only messages whith the specified junk state.

      .. api-member::
         :name: [``junkScore``]
         :type: (:ref:`messages.^query^range`, optional)
         :annotation: -- [Added in TB 121]

         Returns only messages with a junk score in the specified range.

      .. api-member::
         :name: [``messagesPerPage``]
         :type: (integer, optional)
         :annotation: -- [Added in TB 120]

         Set the nominal number of messages-per-page for this query. Defaults to :value:`100` messages.

      .. api-member::
         :name: [``new``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 121]

         Returns only messages with the specified new state.

      .. api-member::
         :name: [``online``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 129]

         Query the server directly instead of the local message database. Online queries currently only support querying the :value:`headerMessageId` property. Currently only supported for NNTP accounts.

      .. api-member::
         :name: [``read``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 121]

         Returns only messages with the specified read state.

      .. api-member::
         :name: [``recipients``]
         :type: (string, optional)

         Returns only messages whose recipients match all specified addresses. The search value is a semicolon separated list of email addresses, names or combinations (e.g.: :value:`Name <user@domain.org>`). For a match, all specified addresses must equal a recipient's address completely and all specified names must match a recipient's name partially. All matches are done case-insensitive.

      .. api-member::
         :name: [``returnMessageListId``]
         :type: (boolean, optional)
         :annotation: -- [Added in TB 120]

         The *messageListId* is usually returned together with the first page, after some messages have been found. Enabling this option will change the return value of this function and return the *messageListId* directly.

      .. api-member::
         :name: [``size``]
         :type: (:ref:`messages.^query^range`, optional)
         :annotation: -- [Added in TB 121]

         Returns only messages with a size in the specified byte range.

      .. api-member::
         :name: [``subject``]
         :type: (string, optional)

         Returns only messages whose subject contains the provided string.

      .. api-member::
         :name: [``tags``]
         :type: (:ref:`messages.tags.^tags^detail`, optional)
         :annotation: -- [Added in TB 74]

         Returns only messages with the specified tags. For a list of available tags, call the :ref:`messages.tags.list` method.

      .. api-member::
         :name: [``toDate``]
         :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)

         Returns only messages with a date before this value.

      .. api-member::
         :name: [``toMe``]
         :type: (boolean, optional)

         Returns only messages with at least one recipient address matching any configured identity.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`messages.^message^list` or string
      :annotation: -- [Added in TB 96]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.update:

update(messageId, newProperties)
--------------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Updates message properties and tags. Updating external messages will throw an *ExtensionError*.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``messageId``
      :type: (:ref:`messages.^message^id`)

   .. api-member::
      :name: ``newProperties``
      :type: (:ref:`messages.^message^properties`)

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`messagesUpdate`

.. rst-class:: api-main-section

Events
======

.. _messages.on^copied:

onCopied
--------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when messages have been copied.

.. api-header::
   :label: Parameters for onCopied.addListener(listener)

   .. api-member::
      :name: ``listener(originalMessages, copiedMessages)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``originalMessages``
      :type: (:ref:`messages.^message^list`)

   .. api-member::
      :name: ``copiedMessages``
      :type: (:ref:`messages.^message^list`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesRead`

.. _messages.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when messages have been permanently deleted.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. api-member::
      :name: ``listener(messages)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``messages``
      :type: (:ref:`messages.^message^list`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesRead`

.. _messages.on^moved:

onMoved
-------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when messages have been moved.

.. api-header::
   :label: Parameters for onMoved.addListener(listener)

   .. api-member::
      :name: ``listener(originalMessages, movedMessages)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``originalMessages``
      :type: (:ref:`messages.^message^list`)

   .. api-member::
      :name: ``movedMessages``
      :type: (:ref:`messages.^message^list`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesRead`

.. _messages.on^new^mail^received:

onNewMailReceived
-----------------

.. api-section-annotation-hack:: -- [Added in TB 75]

Fired when a new message is received, and has been handled by message filters and junk classification. Filters running after junk classification may move the message again.

.. api-header::
   :label: Parameters for onNewMailReceived.addListener(listener, monitorAllFolders)

   .. api-member::
      :name: ``listener(folder, messages)``

      A function that will be called when this event occurs.

   .. api-member::
      :name: [``monitorAllFolders``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 121]

      Monitor all folders (including all special use folders as defined by :ref:`folders.^mail^folder^special^use`) instead of just inbox folders and normal folders.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.^mail^folder`)

   .. api-member::
      :name: ``messages``
      :type: (:ref:`messages.^message^list`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesRead`

.. _messages.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when one or more properties of a message have been updated.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. api-member::
      :name: ``listener(message, changedProperties, oldProperties)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``message``
      :type: (:ref:`messages.^message^header`)

   .. api-member::
      :name: ``changedProperties``
      :type: (:ref:`messages.^message^properties`)

   .. api-member::
      :name: ``oldProperties``
      :type: (:ref:`messages.^message^properties`)
      :annotation: -- [Added in TB 137]

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. rst-class:: api-main-section

Types
=====

.. _messages.^inline^text^part:

InlineTextPart
--------------

.. api-section-annotation-hack:: -- [Added in TB 128]

An inline part with content type :value:`text/*`. These parts are not returned by :ref:`messages.list^attachments` and usually make up the readable content of the message, mostly with content type :value:`text/plain` or :value:`text/html`

.. api-header::
   :label: object

   .. _messages.^inline^text^part.content:

   .. api-member::
      :name: ``content``
      :type: (string)

      The content of this inline text part.

   .. _messages.^inline^text^part.content^type:

   .. api-member::
      :name: ``contentType``
      :type: (string)

      The content type of the part. Most common types for inline text parts are :value:`text/plain` and :value:`text/html`. Possible other (deprecated) types are :value:`text/richtext` and :value:`text/enriched`. Some calendaring services include an inline text part with type :value:`text/calendar`.

.. _messages.^mail^box^header^string:

MailBoxHeaderString
-------------------

.. api-section-annotation-hack:: -- [Added in TB 131]

Content may either be a single email address, or a mailbox string (see RFC 5322, section 3.4). Use :ref:`messenger^utilities.parse^mailbox^string` to extract the name and/or the email from the mailbox string.

.. api-header::
   :label: string

.. _messages.^message^attachment:

MessageAttachment
-----------------

.. api-section-annotation-hack:: -- [Added in TB 98]

Represents an attachment in a message.

.. api-header::
   :label: object

   .. _messages.^message^attachment.content^disposition:

   .. api-member::
      :name: ``contentDisposition``
      :type: (string)
      :annotation: -- [Added in TB 135]

      The content disposition of the attachment, for example :value:`attachment` for normal attachments, or :value:`inline` for inline attachments.

   .. _messages.^message^attachment.content^type:

   .. api-member::
      :name: ``contentType``
      :type: (string)

      The content type of the attachment. A value of :value:`text/x-moz-deleted` indicates that the original attachment was permanently deleted and replaced by a placeholder text attachment with some meta information about the original attachment.

   .. _messages.^message^attachment.headers:

   .. api-member::
      :name: ``headers``
      :type: (object)
      :annotation: -- [Added in TB 135]

      A *dictionary object* of RFC 2047 decoded attachment headers as *key-value* pairs, with the header name as *key*, and an array of headers as *value*.

   .. _messages.^message^attachment.name:

   .. api-member::
      :name: ``name``
      :type: (string)

      The name, as displayed to the user, of this attachment. This is usually but not always the filename of the attached file.

   .. _messages.^message^attachment.part^name:

   .. api-member::
      :name: ``partName``
      :type: (string)

      Identifies the MIME part of the message associated with this attachment.

   .. _messages.^message^attachment.size:

   .. api-member::
      :name: ``size``
      :type: (integer)

      The size in bytes of this attachment.

   .. _messages.^message^attachment.content^id:

   .. api-member::
      :name: [``contentId``]
      :type: (string, optional)
      :annotation: -- [Added in TB 128]

      The content-id of this part. Available for related parts, which are referenced from other places inside the same message (e.g. inline images).

   .. _messages.^message^attachment.message:

   .. api-member::
      :name: [``message``]
      :type: (:ref:`messages.^message^header`, optional)
      :annotation: -- [Added in TB 106]

      A MessageHeader, if this attachment is a message.

.. _messages.^message^header:

MessageHeader
-------------

.. api-section-annotation-hack:: -- [Added in TB 89]

Basic information about a message.

.. api-header::
   :label: object

   .. _messages.^message^header.author:

   .. api-member::
      :name: ``author``
      :type: (:ref:`messages.^mail^box^header^string`)

   .. _messages.^message^header.bcc^list:

   .. api-member::
      :name: ``bccList``
      :type: (array of :ref:`messages.^mail^box^header^string`)

      The Bcc recipients. Not populated for news/nntp messages.

   .. _messages.^message^header.cc^list:

   .. api-member::
      :name: ``ccList``
      :type: (array of :ref:`messages.^mail^box^header^string`)

      The Cc recipients. Not populated for news/nntp messages.

   .. _messages.^message^header.date:

   .. api-member::
      :name: ``date``
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__)

   .. _messages.^message^header.external:

   .. api-member::
      :name: ``external``
      :type: (boolean)
      :annotation: -- [Added in TB 106]

      Whether this message is a real message or an external message (opened from a file or from an attachment).

   .. _messages.^message^header.flagged:

   .. api-member::
      :name: ``flagged``
      :type: (boolean)

      Whether this message is flagged (a.k.a. starred).

   .. _messages.^message^header.header^message^id:

   .. api-member::
      :name: ``headerMessageId``
      :type: (string)

      The message-id header of the message.

   .. _messages.^message^header.headers^only:

   .. api-member::
      :name: ``headersOnly``
      :type: (boolean)
      :annotation: -- [Added in TB 102]

      Some account types (for example :value:`pop3`) allow to download only the headers of the message, but not its body. The body of such messages will not be available.

   .. _messages.^message^header.id:

   .. api-member::
      :name: ``id``
      :type: (:ref:`messages.^message^id`)

   .. _messages.^message^header.junk:

   .. api-member::
      :name: ``junk``
      :type: (boolean)

      Whether the message has been marked as junk. Always :value:`false` for news/nntp messages and external messages.

   .. _messages.^message^header.junk^score:

   .. api-member::
      :name: ``junkScore``
      :type: (integer)

      The junk score associated with the message. Always :value:`0` for news/nntp messages and external messages.

   .. _messages.^message^header.new:

   .. api-member::
      :name: ``new``
      :type: (boolean)
      :annotation: -- [Added in TB 106]

      Whether the message has been received recently and is marked as new.

   .. _messages.^message^header.recipients:

   .. api-member::
      :name: ``recipients``
      :type: (array of :ref:`messages.^mail^box^header^string`)

      The To recipients. Not populated for news/nntp messages.

   .. _messages.^message^header.size:

   .. api-member::
      :name: ``size``
      :type: (integer)
      :annotation: -- [Added in TB 90]

      The total size of the message in bytes.

   .. _messages.^message^header.subject:

   .. api-member::
      :name: ``subject``
      :type: (string)

      The subject of the message.

   .. _messages.^message^header.tags:

   .. api-member::
      :name: ``tags``
      :type: (array of string)

      Tags associated with this message. For a list of available tags, use :ref:`messages.tags.list`.

   .. _messages.^message^header.folder:

   .. api-member::
      :name: [``folder``]
      :type: (:ref:`folders.^mail^folder`, optional)

      The :permission:`accountsRead` permission is required for this property to be included. Not available for external or attached messages.

   .. _messages.^message^header.read:

   .. api-member::
      :name: [``read``]
      :type: (boolean, optional)

      Whether the message has been marked as read. Not available for external or attached messages.

.. _messages.^message^id:

MessageId
---------

.. api-section-annotation-hack:: -- [Added in TB 122]

A unique id representing a :ref:`messages.^message^header` and the associated message. This id doesn’t refer to the Message-ID email header. It is an internal tracking number that does not remain after a restart. Nor does it follow an email that has been moved to a different folder.

.. api-header::
   :label: integer

.. _messages.^message^list:

MessageList
-----------

.. api-section-annotation-hack:: -- [Added in TB 89]

See :doc:`guides/messageLists` for more information.

.. api-header::
   :label: object

   .. _messages.^message^list.id:

   .. api-member::
      :name: ``id``
      :type: (string or null)

      Id of the message list, to be used with :ref:`messages.continue^list` or :ref:`messages.abort^list`.

   .. _messages.^message^list.messages:

   .. api-member::
      :name: ``messages``
      :type: (array of :ref:`messages.^message^header`)

.. _messages.^message^part:

MessagePart
-----------

.. api-section-annotation-hack:: -- [Added in TB 89]

Represents an email message "part", which could be the whole message.

.. api-header::
   :label: object

   .. _messages.^message^part.body:

   .. api-member::
      :name: [``body``]
      :type: (string, optional)

      The quoted-printable or base64 decoded content of the part. Only present for parts with a content type of :value:`text/*` and only if requested, see the :value:`decodeContent` option of :ref:`messages.get^full`. Use :ref:`messages.get^attachment^file` to retrieve the content of parts which have a content type other than :value:`text/*`.

   .. _messages.^message^part.content^type:

   .. api-member::
      :name: [``contentType``]
      :type: (string, optional)

   .. _messages.^message^part.decryption^status:

   .. api-member::
      :name: [``decryptionStatus``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 125]

      The decryption status, only available for the root part.

      Supported values:

      .. api-member::
         :name: :value:`none`

      .. api-member::
         :name: :value:`skipped`

      .. api-member::
         :name: :value:`success`

      .. api-member::
         :name: :value:`fail`

   .. _messages.^message^part.headers:

   .. api-member::
      :name: [``headers``]
      :type: (object, optional)

      A *dictionary object* of RFC 2047 decoded part headers as *key-value* pairs, with the header name as *key*, and an array of headers as *value*. Only present if requested, see the :value:`decodeHeaders` option of :ref:`messages.get^full`.

   .. _messages.^message^part.name:

   .. api-member::
      :name: [``name``]
      :type: (string, optional)

      Name of the part, if it is a file.

   .. _messages.^message^part.part^name:

   .. api-member::
      :name: [``partName``]
      :type: (string, optional)

      The identifier of this part, used in :ref:`messages.get^attachment^file`.

   .. _messages.^message^part.parts:

   .. api-member::
      :name: [``parts``]
      :type: (array of :ref:`messages.^message^part`, optional)

      Any sub-parts of this part.

   .. _messages.^message^part.raw^body:

   .. api-member::
      :name: [``rawBody``]
      :type: (string, optional)
      :annotation: -- [Added in TB 133]

      The raw content of the part. Only present if requested, see the :value:`decodeContent` option of :ref:`messages.get^full`.

   .. _messages.^message^part.raw^headers:

   .. api-member::
      :name: [``rawHeaders``]
      :type: (object, optional)
      :annotation: -- [Added in TB 133]

      A *dictionary object* of raw part headers as *key-value* pairs, with the header name as *key*, and an array of headers as *value*. Only present if requested, see the :value:`decodeHeaders` option of :ref:`messages.get^full`.

   .. _messages.^message^part.size:

   .. api-member::
      :name: [``size``]
      :type: (integer, optional)

      The size of this part. The size of parts with content type *message/rfc822* is not the actual message size (on disc), but the total size of its decoded body parts, excluding headers.

.. _messages.^message^properties:

MessageProperties
-----------------

.. api-section-annotation-hack:: -- [Added in TB 106]

Message properties used in :ref:`messages.update` and :ref:`messages.import`. They can also be monitored by :ref:`messages.on^updated`.

.. api-header::
   :label: object

   .. _messages.^message^properties.flagged:

   .. api-member::
      :name: [``flagged``]
      :type: (boolean, optional)

      Whether the message is flagged (a.k.a starred).

   .. _messages.^message^properties.junk:

   .. api-member::
      :name: [``junk``]
      :type: (boolean, optional)

      Whether the message is marked as junk. Only supported in :ref:`messages.update`.

   .. _messages.^message^properties.new:

   .. api-member::
      :name: [``new``]
      :type: (boolean, optional)

      Whether the message is marked as new. Only supported in :ref:`messages.import`.

   .. _messages.^message^properties.read:

   .. api-member::
      :name: [``read``]
      :type: (boolean, optional)

      Whether the message is marked as read.

   .. _messages.^message^properties.tags:

   .. api-member::
      :name: [``tags``]
      :type: (array of string, optional)

      Tags associated with this message. For a list of available tags, call the :ref:`messages.tags.list` method.

.. _messages.^query^range:

QueryRange
----------

.. api-section-annotation-hack:: -- [Added in TB 121]

An object defining a range.

.. api-header::
   :label: object

   .. _messages.^query^range.max:

   .. api-member::
      :name: [``max``]
      :type: (integer, optional)

      The maximum value required to match the query.

   .. _messages.^query^range.min:

   .. api-member::
      :name: [``min``]
      :type: (integer, optional)

      The minimum value required to match the query.
