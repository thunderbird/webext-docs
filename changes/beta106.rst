==========================
Changes in Thunderbird 106
==========================

commands API
============
* Added the ``tab`` parameter to :ref:`commands.onCommand`, to get information about the active tab, when a command occurs.

compose API
===========
* Added :ref:`compose.onAfterSave` event, to be notified when saving a message as a draft or a template succeeded or failed.
* Added :ref:`compose.onAfterSend` event, to be notified when sending a message succeeded or failed.

contacts API
============
* Added :ref:`contacts.getPhoto` to be able to retrieve the photo of a contact.

mailTabs API
============
* Added :ref:`mailTabs.setSelectedMessages`.

messages API
============
* Added the ``message`` member to the :ref:`messages.MessageAttachment` type, to provide access to attached messages.
* Added the ``external`` member to the :ref:`messages.MessageHeader` type, to indicate if a message is an external message, not stored in a message folder (message attachments or messages opened from file).
* Added the ``new`` member to the :ref:`messages.MessageHeader` type, to indicate if a message has been received recently and is marked as new.
* Added :ref:`messages.import` to import messages into Thunderbird (currently only supported for local folders).
* Renamed ``MessageChangeProperties`` to :ref:`messages.MessageProperties`, as it is now also used by :ref:`messages.import`, to define the properties of the imported message.
* Added the ``new`` member to the :ref:`messages.MessageProperties` type (currently only supported by :ref:`messages.import`).

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 103 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=103%20Branch&o2=equals>`__, `Thunderbird 104 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=104%20Branch&o2=equals>`__, `Thunderbird 105 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=105%20Branch&o2=equals>`__ and `Thunderbird 106 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=106%20Branch&o2=equals>`__.
