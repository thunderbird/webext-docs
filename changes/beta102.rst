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

---

Bugzilla list of fixed WebExtension API defects in `Thunderbird 102 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=102%20Branch&o2=equals>`__.
