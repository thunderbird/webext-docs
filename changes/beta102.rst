==========================
Changes in Thunderbird 102
==========================

compose API
===========
* Added support for ``additionalFccFolder``, ``attachVCard``, ``deliveryFormat``, ``deliveryStatusNotification``, ``overrideDefaultFcc``, ``overrideDefaultFccFolder``, ``priority`` and ``returnReceipt`` in :ref:`compose.ComposeDetails`.
* Added :ref:`compose.getActiveDictionaries`, :ref:`compose.setActiveDictionaries` and :ref:`compose.onActiveDictionariesChanged`

folders API
============
* Subfolders are now being returned in the order used in Thunderbird's folder pane.

messages API
============
* Added support for ``headersOnly`` to :ref:`messages.MessageHeader`.
* Added :ref:`messages.createTag`, :ref:`messages.updateTag` and :ref:`messages.deleteTag`.

messageDisplay API
============
* Added :ref:`messagesDisplay.open` to open messages in tabs or windows
