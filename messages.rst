.. _messages_api:

========
messages
========

The messages API first appeared in Thunderbird 66.

.. note::

  When the term ``messageId`` is used in these documents, it *doesn't* refer to the Message-ID
  email header. It is an internal tracking number that does not remain after a restart. Nor does
  it follow an email that has been moved to a different folder.

.. warning::

  Some functions in this API potentially return *a lot* of messages. Be careful what you wish for!
  See :doc:`how-to/messageLists` for more information.

.. role:: permission

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`messagesMove`

   Copy or move your email messages (including moving them to the trash folder)

.. api-member::
   :name: :permission:`messagesRead`

   Read your email messages and mark or tag them

.. api-member::
   :name: :permission:`messagesDelete`

   Permanently delete your email messages

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messagesRead` is required to use ``messages``.

.. rst-class:: api-main-section

Functions
=========

.. _messages.list:

list(folder)
------------

.. api-section-annotation-hack:: 

Gets all messages in a folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolder`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`messages.MessageList`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`accountsRead`

.. _messages.continueList:

continueList(messageListId)
---------------------------

.. api-section-annotation-hack:: 

Returns the next chunk of messages in a list. See :doc:`how-to/messageLists` for more information.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageListId``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`messages.MessageList`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.get:

get(messageId)
--------------

.. api-section-annotation-hack:: 

Returns a specified message.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`messages.MessageHeader`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.getFull:

getFull(messageId)
------------------

.. api-section-annotation-hack:: 

Returns a specified message, including all headers and MIME parts.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`messages.MessagePart`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.getRaw:

getRaw(messageId)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 72, backported to TB 68.7]

Returns the unmodified source of a message as a `binary string <https://developer.mozilla.org/en-US/docs/Web/API/DOMString/Binary>`__, which is a simple series of 8-bit values. If the message contains non-ASCII characters, the body parts in the binary string cannot be read directly and must be decoded according to their character sets. Use :ref:`messages.getFull` to get the correctly decoded parts. Manually decoding the raw message is probably too error-prone, especially if the message contains MIME parts with different character set encodings or attachments.

To get a readable version of the raw message as it appears in Thunderbird's message source view, it may be sufficient to decode the message according to the character set specified in its main ``content-type`` header (example: `text/html; charset=UTF-8`) using the following function (see MDN for `supported input encodings <https://developer.mozilla.org/en-US/docs/Web/API/Encoding_API/Encodings>`__): 

.. literalinclude:: includes/messages/decodeBinaryString.js
  :language: JavaScript

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.listAttachments:

listAttachments(messageId)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 88]

Lists all of the attachments of a message.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`messages.Attachment`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.getAttachmentFile:

getAttachmentFile(messageId, partName)
--------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 88]

Gets the content of an attachment as a DOM ``File`` object.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``partName``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`_
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

The most simple way to get the content of an attachment is to use the ``text()`` method of the ``File`` object:

.. literalinclude:: includes/messages/file.js
  :language: JavaScript

.. _messages.query:

query(queryInfo)
----------------

.. api-section-annotation-hack:: -- [Added in TB 69, backported to TB 68.2]

Gets all messages that have the specified properties, or all messages if no properties are specified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``queryInfo``
      :type: (object)
      
      .. api-member::
         :name: [``author``]
         :type: (string)
         
         Returns only messages with this value matching the author. The search value is a single email address, a name or a combination (e.g.: ``Name <user@domain.org>``). The address part of the search value (if provided) must match the author's address completely. The name part of the search value (if provided) must match the author's name partially. All matches are done case-insensitive.
      
      
      .. api-member::
         :name: [``body``]
         :type: (string)
         
         Returns only messages with this value in the body of the mail.
      
      
      .. api-member::
         :name: [``flagged``]
         :type: (boolean)
         
         Returns only flagged (or unflagged if false) messages.
      
      
      .. api-member::
         :name: [``folder``]
         :type: (:ref:`folders.MailFolder`)
         
         Returns only messages from the specified folder. The :permission:`accountsRead` permission is required.
      
      
      .. api-member::
         :name: [``fromDate``]
         :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`_)
         
         Returns only messages with a date after this value.
      
      
      .. api-member::
         :name: [``fromMe``]
         :type: (boolean)
         
         Returns only messages with the author's address matching any configured identity.
      
      
      .. api-member::
         :name: [``fullText``]
         :type: (string)
         
         Returns only messages with this value somewhere in the mail (subject, body or author).
      
      
      .. api-member::
         :name: [``headerMessageId``]
         :type: (string)
         :annotation: -- [Added in TB 85]
         
         Returns only messages with a Message-ID header matching this value.
      
      
      .. api-member::
         :name: [``includeSubFolders``]
         :type: (boolean)
         :annotation: -- [Added in TB 91]
         
         Search the folder specified by ``queryInfo.folder`` recursively.
      
      
      .. api-member::
         :name: [``recipients``]
         :type: (string)
         
         Returns only messages whose recipients match all specified addresses. The search value is a semicolon separated list of email addresses, names or combinations (e.g.: ``Name <user@domain.org>``). For a match, all specified addresses must equal a recipient's address completely and all specified names must match a recipient's name partially. All matches are done case-insensitive.
      
      
      .. api-member::
         :name: [``subject``]
         :type: (string)
         
         Returns only messages with this value matching the subject.
      
      
      .. api-member::
         :name: [``tags``]
         :type: (:ref:`messages.TagsDetail`)
         :annotation: -- [Added in TB 74]
         
         Returns only messages with the specified tags. For a list of available tags, call the :ref:`messages.listTags` method.
      
      
      .. api-member::
         :name: [``toDate``]
         :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`_)
         
         Returns only messages with a date before this value.
      
      
      .. api-member::
         :name: [``toMe``]
         :type: (boolean)
         
         Returns only messages with at least one recipient address matching any configured identity.
      
      
      .. api-member::
         :name: [``unread``]
         :type: (boolean)
         
         Returns only unread (or read if false) messages.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`messages.MessageList`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.update:

update(messageId, newProperties)
--------------------------------

.. api-section-annotation-hack:: 

Marks or unmarks a message as junk, read, flagged, or tagged.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``newProperties``
      :type: (:ref:`messages.MessageChangeProperties`)
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.move:

move(messageIds, destination)
-----------------------------

.. api-section-annotation-hack:: 

Moves messages to a specified folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageIds``
      :type: (array of integer)
      
      The IDs of the messages to move.
   
   
   .. api-member::
      :name: ``destination``
      :type: (:ref:`folders.MailFolder`)
      
      The folder to move the messages to.
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`accountsRead`
   - :permission:`messagesMove`

.. _messages.copy:

copy(messageIds, destination)
-----------------------------

.. api-section-annotation-hack:: 

Copies messages to a specified folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageIds``
      :type: (array of integer)
      
      The IDs of the messages to copy.
   
   
   .. api-member::
      :name: ``destination``
      :type: (:ref:`folders.MailFolder`)
      
      The folder to copy the messages to.
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`accountsRead`
   - :permission:`messagesMove`

.. _messages.delete:

delete(messageIds, [skipTrash])
-------------------------------

.. api-section-annotation-hack:: 

Deletes messages permanently, or moves them to the trash folder (honoring the account's deletion behavior settings). The ``skipTrash`` parameter allows immediate permanent deletion, bypassing the trash folder.

**Note**: Consider using :ref:`messages.move` to manually move messages to the account's trash folder, instead of requesting the overly powerful permission to actually delete messages. The account's trash folder can be extracted as follows: 

.. literalinclude:: includes/messages/getTrash.js
  :language: JavaScript

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageIds``
      :type: (array of integer)
      
      The IDs of the messages to delete.
   
   
   .. api-member::
      :name: [``skipTrash``]
      :type: (boolean)
      
      If true, the message will be deleted permanently, regardless of the account's deletion behavior settings.
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`messagesDelete`

.. _messages.archive:

archive(messageIds)
-------------------

.. api-section-annotation-hack:: 

Archives messages using the current settings.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageIds``
      :type: (array of integer)
      
      The IDs of the messages to archive.
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`messagesMove`

.. _messages.listTags:

listTags()
----------

.. api-section-annotation-hack:: 

Returns a list of tags that can be set on messages, and their human-friendly name, colour, and sort order.

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`messages.MessageTag`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. rst-class:: api-main-section

Events
======

.. _messages.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when one or more properties of a message have been updated.

.. api-header::
   :label: Parameters for messages.onUpdated.addListener(listener)

   
   .. api-member::
      :name: ``listener(message, changedProperties)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``message``
      :type: (:ref:`messages.MessageHeader`)
   
   
   .. api-member::
      :name: ``changedProperties``
      :type: (:ref:`messages.MessageChangeProperties`)
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messages.onMoved:

onMoved
-------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when messages have been moved.

.. api-header::
   :label: Parameters for messages.onMoved.addListener(listener)

   
   .. api-member::
      :name: ``listener(originalMessages, movedMessages)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``originalMessages``
      :type: (:ref:`messages.MessageList`)
   
   
   .. api-member::
      :name: ``movedMessages``
      :type: (:ref:`messages.MessageList`)
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`accountsRead`

.. _messages.onCopied:

onCopied
--------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when messages have been copied.

.. api-header::
   :label: Parameters for messages.onCopied.addListener(listener)

   
   .. api-member::
      :name: ``listener(originalMessages, copiedMessages)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``originalMessages``
      :type: (:ref:`messages.MessageList`)
   
   
   .. api-member::
      :name: ``copiedMessages``
      :type: (:ref:`messages.MessageList`)
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`accountsRead`

.. _messages.onDeleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when messages have been permanently deleted.

.. api-header::
   :label: Parameters for messages.onDeleted.addListener(listener)

   
   .. api-member::
      :name: ``listener(messages)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``messages``
      :type: (:ref:`messages.MessageList`)
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`accountsRead`

.. _messages.onNewMailReceived:

onNewMailReceived
-----------------

.. api-section-annotation-hack:: -- [Added in TB 75]

Fired when a new message is received, and has been through junk classification and message filters.

.. api-header::
   :label: Parameters for messages.onNewMailReceived.addListener(listener)

   
   .. api-member::
      :name: ``listener(folder, messages)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolder`)
   
   
   .. api-member::
      :name: ``messages``
      :type: (:ref:`messages.MessageList`)
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`accountsRead`

.. rst-class:: api-main-section

Types
=====

.. _messages.Attachment:

Attachment
----------

.. api-section-annotation-hack:: 

Represents an attachment in a message.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``contentType``
      :type: (string)
      
      The content type of the attachment.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      The name, as displayed to the user, of this attachment. This is usually but not always the filename of the attached file.
   
   
   .. api-member::
      :name: ``partName``
      :type: (string)
      
      Identifies the MIME part of the message associated with this attachment.
   
   
   .. api-member::
      :name: ``size``
      :type: (integer)
      
      The size in bytes of this attachment.
   

.. _messages.MessageChangeProperties:

MessageChangeProperties
-----------------------

.. api-section-annotation-hack:: 

Message properties that can be updated by the :ref:`messages.update` and that are monitored by :ref:`messages.onUpdated`.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``flagged``]
      :type: (boolean)
      
      Message is flagged.
   
   
   .. api-member::
      :name: [``junk``]
      :type: (boolean)
      
      Message is junk.
   
   
   .. api-member::
      :name: [``read``]
      :type: (boolean)
      
      Message is read.
   
   
   .. api-member::
      :name: [``tags``]
      :type: (array of string)
      
      Tags associated with this message. For a list of available tags, call the listTags method.
   

.. _messages.MessageHeader:

MessageHeader
-------------

.. api-section-annotation-hack:: 

Basic information about a message.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``author``
      :type: (string)
   
   
   .. api-member::
      :name: ``bccList``
      :type: (array of string)
      
      The Bcc recipients. Not populated for news/nntp messages.
   
   
   .. api-member::
      :name: ``ccList``
      :type: (array of string)
      
      The Cc recipients. Not populated for news/nntp messages.
   
   
   .. api-member::
      :name: ``date``
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`_)
   
   
   .. api-member::
      :name: ``flagged``
      :type: (boolean)
   
   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolder`)
      
      The :permission:`accountsRead` permission is required for this property to be included.
   
   
   .. api-member::
      :name: ``headerMessageId``
      :type: (string)
      :annotation: -- [Added in TB 85]
      
      The message-id header of the message.
   
   
   .. api-member::
      :name: ``id``
      :type: (integer)
   
   
   .. api-member::
      :name: ``junk``
      :type: (boolean)
      :annotation: -- [Added in TB 74]
      
      Not populated for news/nntp messages.
   
   
   .. api-member::
      :name: ``junkScore``
      :type: (integer)
      :annotation: -- [Added in TB 74]
   
   
   .. api-member::
      :name: ``read``
      :type: (boolean)
   
   
   .. api-member::
      :name: ``recipients``
      :type: (array of string)
      
      The To recipients. Not populated for news/nntp messages.
   
   
   .. api-member::
      :name: ``size``
      :type: (integer)
      :annotation: -- [Added in TB 90]
      
      The total size of the message in bytes.
   
   
   .. api-member::
      :name: ``subject``
      :type: (string)
   
   
   .. api-member::
      :name: ``tags``
      :type: (array of string)
   

.. _messages.MessageList:

MessageList
-----------

.. api-section-annotation-hack:: 

See :doc:`how-to/messageLists` for more information.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``messages``
      :type: (array of :ref:`messages.MessageHeader`)
   
   
   .. api-member::
      :name: [``id``]
      :type: (string)
   

.. _messages.MessagePart:

MessagePart
-----------

.. api-section-annotation-hack:: 

Represents an email message "part", which could be the whole message

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``body``]
      :type: (string)
      
      The content of the part
   
   
   .. api-member::
      :name: [``contentType``]
      :type: (string)
   
   
   .. api-member::
      :name: [``headers``]
      :type: (object)
      
      An object of part headers, with the header name as key, and an array of header values as value
   
   
   .. api-member::
      :name: [``name``]
      :type: (string)
      
      Name of the part, if it is a file
   
   
   .. api-member::
      :name: [``partName``]
      :type: (string)
   
   
   .. api-member::
      :name: [``parts``]
      :type: (array of :ref:`messages.MessagePart`)
      
      Any sub-parts of this part
   
   
   .. api-member::
      :name: [``size``]
      :type: (integer)
   

.. _messages.MessageTag:

MessageTag
----------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``color``
      :type: (string)
      
      Tag color
   
   
   .. api-member::
      :name: ``key``
      :type: (string)
      
      Distinct tag identifier – use this string when referring to a tag
   
   
   .. api-member::
      :name: ``ordinal``
      :type: (string)
      
      Custom sort string (usually empty)
   
   
   .. api-member::
      :name: ``tag``
      :type: (string)
      
      Human-readable tag name
   

.. _messages.TagsDetail:

TagsDetail
----------

.. api-section-annotation-hack:: 

Used for filtering messages by tag in various methods. Note that functions using this type may have a partial implementation.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``mode``
      :type: (`string`)
      
      Whether all of the tag filters must apply, or any of them.
      
      Supported values:
      
      .. api-member::
         :name: ``all``
      
      .. api-member::
         :name: ``any``
   
   
   .. api-member::
      :name: ``tags``
      :type: (object)
      
      Object keys are tags to filter on, values are ``true`` if the message must have the tag, or ``false`` if it must not have the tag. For a list of available tags, call the :ref:`messages.listTags` method.
   
