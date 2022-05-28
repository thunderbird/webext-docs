==========================
Changes in Thunderbird 102
==========================

compose API
===========
* Added support for ``additionalFccFolder``, ``attachVCard``, ``deliveryFormat``, ``deliveryStatusNotification``, ``overrideDefaultFcc``, ``overrideDefaultFccFolder``, ``priority`` and ``returnReceipt`` in :ref:`compose.ComposeDetails`.
* Added :ref:`compose.getActiveDictionaries`, :ref:`compose.setActiveDictionaries` and :ref:`compose.onActiveDictionariesChanged`
* Added :ref:`compose.saveMessage` and changed the return value of :ref:`compose.sendMessage` from a boolean to a complex object with information about the sent message and its local copies - both functions return a Promise which resolves once the message operation has finished

folders API
============
* Subfolders are now being returned in the order used in Thunderbird's folder pane.

messages API
============
* Added support for ``headersOnly`` to :ref:`messages.MessageHeader`.
* Added :ref:`messages.createTag`, :ref:`messages.updateTag` and :ref:`messages.deleteTag`.

messageDisplay API
==================
* Added :ref:`messageDisplay.open` to open messages in tabs or windows.
