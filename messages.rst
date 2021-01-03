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

   Move, copy, or delete your email messages

.. api-member::
   :name: :permission:`messagesRead`

   Read your email messages and mark or tag them

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

Returns the unmodified source of a message.

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
         
         Returns only messages with this value matching the author.
      
      
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
         
         Returns only messages with the author matching any configured identity.
      
      
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
         :name: [``recipients``]
         :type: (string)
         
         Returns only messages with this value matching one or more recipients.
      
      
      .. api-member::
         :name: [``subject``]
         :type: (string)
         
         Returns only messages with this value matching the subject.
      
      
      .. api-member::
         :name: [``tags``]
         :type: (:ref:`messages.TagsDetail`)
         :annotation: -- [Added in TB 74]
         
         Returns only messages with the specified tags. For a list of available tags, call the listTags method. Querying for messages that must *not* have a tag does not work.
      
      
      .. api-member::
         :name: [``toDate``]
         :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`_)
         
         Returns only messages with a date before this value.
      
      
      .. api-member::
         :name: [``toMe``]
         :type: (boolean)
         
         Returns only messages with one or more recipients matching any configured identity.
      
      
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

Marks or unmarks a message as read, flagged, or tagged.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``newProperties``
      :type: (object)
      
      .. api-member::
         :name: [``flagged``]
         :type: (boolean)
         
         Marks the message as flagged or unflagged.
      
      
      .. api-member::
         :name: [``junk``]
         :type: (boolean)
         :annotation: -- [Added in TB 73, backported to TB 68.7]
         
         Marks the message as junk or not junk.
      
      
      .. api-member::
         :name: [``read``]
         :type: (boolean)
         
         Marks the message as read or unread.
      
      
      .. api-member::
         :name: [``tags``]
         :type: (array of string)
         
         Sets the tags on the message. For a list of available tags, call the listTags method.
      
   

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

Deletes messages, or moves them to the trash folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageIds``
      :type: (array of integer)
      
      The IDs of the messages to delete.
   
   
   .. api-member::
      :name: [``skipTrash``]
      :type: (boolean)
      
      If true, the message will be permanently deleted without warning the user. If false or not specified, it will be moved to the trash folder.
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
   - :permission:`messagesMove`

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

.. _messages.onNewMailReceived:

onNewMailReceived(folder, messages)
-----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 75]

Fired when a new message is received, and has been through junk classification and message filters.

.. api-header::
   :label: Parameters for event listeners

   
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

.. _messages.MessageHeader:

MessageHeader
-------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``author``
      :type: (string)
   
   
   .. api-member::
      :name: ``bccList``
      :type: (array of string)
   
   
   .. api-member::
      :name: ``ccList``
      :type: (array of string)
   
   
   .. api-member::
      :name: ``date``
      :type: (date)
   
   
   .. api-member::
      :name: ``flagged``
      :type: (boolean)
   
   
   .. api-member::
      :name: ``folder``
      :type: (:ref:`folders.MailFolder`)
      
      The :permission:`accountsRead` permission is required for this property to be included.
   
   
   .. api-member::
      :name: ``id``
      :type: (integer)
   
   
   .. api-member::
      :name: ``junk``
      :type: (boolean)
      :annotation: -- [Added in TB 74]
   
   
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
      :name: ``id``
      :type: (string)
   
   
   .. api-member::
      :name: ``messages``
      :type: (array of :ref:`messages.MessageHeader`)
   

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
   
