==========================
Changes in Thunderbird 106
==========================

browserAction API
=================
* Introduced a ``default_windows`` manifest property, to allow a browserAction buttons to be displayed in stand alone message windows.

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

messageDisplay API
==================
* Fixed :ref:`messageDisplay.onMessageDisplayed` to be triggered for external messages.

____

Bugzilla list of all fixed WebExtension API bugs in `Thunderbird 103 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=103%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__, `Thunderbird 104 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=104%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__, `Thunderbird 105 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=105%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__ and `Thunderbird 106 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=106%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__.
