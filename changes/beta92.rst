=========================
Changes in Thunderbird 92
=========================

folders API
===========

* :ref:`folders.delete` now requires the :permission:`messagesDelete` permission
* added :ref:`folders.move` function
* added :ref:`folders.copy` function
* added :ref:`folders.getFolderInfo` function and :ref:`folders.MailFolderInfo` type to obtain additional folder information like ``totalMessageCounts`` or ``unreadMessageCounts``
* added :ref:`folders.onCreated` event
* added :ref:`folders.onRenamed` event
* added :ref:`folders.onMoved` event
* added :ref:`folders.onCopied` event
* added :ref:`folders.onDeleted` event
* added :ref:`folders.onFolderInfoChanged` event


tabs API
========

* added ``type`` property to :ref:`tabs.Tab`, supporting ``addressBook``, ``calendar``, ``calendarEvent``, ``calendarTask``, ``chat``, ``content``, ``mail``, ``messageCompose``, ``messageDisplay``, ``special`` and ``tasks``
