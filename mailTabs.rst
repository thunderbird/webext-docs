========
mailTabs
========

This is preliminary documentation for the mail tabs API being developed in `bug 1499617`__.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1499617

.. note::

  The permission ``mailTabs`` is required to use ``mailTabs``.

Functions
=========

getAll()
--------

Returns an array of all mail tabs in all windows.

getCurrent()
------------

Returns the current mail tab in the most recent window, or throws an exception if the current tab is not a mail tab.

update([tabId], updateProperties)
---------------------------------

Modifies the properties of a mail tab. Properties that are not specified in ``updateProperties`` are not modified.

- [``tabId``] (integer) Defaults to the selected tab of the current window.
- ``updateProperties`` (object)

  - [``displayedFolder``] (object) Sets the folder displayed in the tab. The extension must have an accounts permission to do this.
  - [``folderPaneVisible``] (boolean) Shows or hides the folder pane.
  - [``layout``] (`string <enum_layout_>`_) Sets the arrangement of the folder pane, message list pane, and message display pane. Note that setting this applies it to all mail tabs.
  - [``messagePaneVisible``] (boolean) Shows or hides the message display pane.
  - [``sortOrder``] (`string <enum_sortOrder_>`_) Sorts the list of messages. ``sortType`` must also be given.
  - [``sortType``] (`string <enum_sortType_>`_) Sorts the list of messages. ``sortOrder`` must also be given.

.. _enum_layout:

Values for layout:

- ``standard``
- ``wide``
- ``vertical``

.. _enum_sortOrder:

Values for sortOrder:

- ``none``
- ``ascending``
- ``descending``

.. _enum_sortType:

Values for sortType:

- ``byNone``
- ``byDate``
- ``bySubject``
- ``byAuthor``
- ``byId``
- ``byThread``
- ``byPriority``
- ``byStatus``
- ``bySize``
- ``byFlagged``
- ``byUnread``
- ``byRecipient``
- ``byLocation``
- ``byTags``
- ``byJunkStatus``
- ``byAttachments``
- ``byAccount``
- ``byCustom``
- ``byReceived``
- ``byCorrespondent``

getSelectedMessages([tabId])
----------------------------

Lists the selected messages in the current folder. A messages permission is required to do this.

- [``tabId``] (integer) Defaults to the selected tab of the current window.

setQuickFilter([tabId], properties)
-----------------------------------

Sets the Quick Filter user interface based on the options specified.

- [``tabId``] (integer) Defaults to the selected tab of the current window.
- ``properties`` (object)

  - [``addrBook``] (boolean) Shows only messages from people in the address book.
  - [``attachment``] (boolean) Shows only messages with attachments`.
  - [``body``] (boolean) Shows messages where ``text`` matches the message body.
  - [``recipients``] (boolean) Shows messages where ``text`` matches the recipients.
  - [``sender``] (boolean) Shows messages where ``text`` matches the sender.
  - [``show``] (boolean) Shows or hides the Quick Filter bar.
  - [``starred``] (boolean) Shows only starred messages.
  - [``subject``] (boolean) Shows messages where ``text`` matches the subject.
  - [``tags``] (boolean) Shows only messages with tags on them.
  - [``text``] (string) String to match against the ``recipients``, ``sender``, ``subject``, or ``body``.
  - [``unread``] (boolean) Shows only unread messages.

