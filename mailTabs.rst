========
mailTabs
========

The messages API first appeared in Thunderbird 66 (see `bug 1499617`__).

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1499617

The `Filter`__  and `Layout`__ sample extensions use this API.

__ https://github.com/thundernest/sample-extensions/tree/master/filter
__ https://github.com/thundernest/sample-extensions/tree/master/layout

Functions
=========

.. _mailTabs.query:

query(queryInfo)
----------------

Gets all mail tabs that have the specified properties, or all mail tabs if no properties are specified.

- ``queryInfo`` (object)

  - [``active``] (boolean) Whether the tabs are active in their windows.
  - [``currentWindow``] (boolean) Whether the tabs are in the current window.
  - [``lastFocusedWindow``] (boolean) Whether the tabs are in the last focused window.
  - [``windowId``] (integer) The ID of the parent window, or :ref:`windows.WINDOW_ID_CURRENT` for the current window.

Returns a `Promise`_ fulfilled with:

- array of :ref:`mailTabs.MailTab`

.. _mailTabs.update:

update([tabId], updateProperties)
---------------------------------

Modifies the properties of a mail tab. Properties that are not specified in ``updateProperties`` are not modified.

- [``tabId``] (integer) Defaults to the active tab of the current window.
- ``updateProperties`` (object)

  - [``displayedFolder``] (:ref:`folders.MailFolder`) Sets the folder displayed in the tab. The extension must have an accounts permission to do this.
  - [``folderPaneVisible``] (boolean) Shows or hides the folder pane.
  - [``layout``] (`string <enum_layout_9_>`_) Sets the arrangement of the folder pane, message list pane, and message display pane. Note that setting this applies it to all mail tabs.
  - [``messagePaneVisible``] (boolean) Shows or hides the message display pane.
  - [``sortOrder``] (`string <enum_sortOrder_11_>`_) Sorts the list of messages. ``sortType`` must also be given.
  - [``sortType``] (`string <enum_sortType_12_>`_) Sorts the list of messages. ``sortOrder`` must also be given.

.. _enum_layout_9:

Values for layout:

- ``standard``
- ``wide``
- ``vertical``

.. _enum_sortOrder_11:

Values for sortOrder:

- ``none``
- ``ascending``
- ``descending``

.. _enum_sortType_12:

Values for sortType:

- ``none``
- ``date``
- ``subject``
- ``author``
- ``id``
- ``thread``
- ``priority``
- ``status``
- ``size``
- ``flagged``
- ``unread``
- ``recipient``
- ``location``
- ``tags``
- ``junkStatus``
- ``attachments``
- ``account``
- ``custom``
- ``received``
- ``correspondent``

.. _mailTabs.getSelectedMessages:

getSelectedMessages([tabId])
----------------------------

Lists the selected messages in the current folder. A messages permission is required to do this.

- [``tabId``] (integer) Defaults to the active tab of the current window.

Returns a `Promise`_ fulfilled with:

- :ref:`messages.MessageList`

.. _mailTabs.setQuickFilter:

setQuickFilter([tabId], properties)
-----------------------------------

Sets the Quick Filter user interface based on the options specified.

- [``tabId``] (integer) Defaults to the active tab of the current window.
- ``properties`` (object)

  - [``attachment``] (boolean) Shows only messages with attachments.
  - [``contact``] (boolean) Shows only messages from people in the address book.
  - [``flagged``] (boolean) Shows only flagged messages.
  - [``show``] (boolean) Shows or hides the Quick Filter bar.
  - [``starred``] (boolean) **Deprecated.** Use ``flagged`` instead.
  - [``tags``] (boolean or :ref:`mailTabs.QuickFilterTagsDetail`) Shows only messages with tags on them.
  - [``text``] (:ref:`mailTabs.QuickFilterTextDetail`) Shows only messages matching the supplied text.
  - [``unread``] (boolean) Shows only unread messages.

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Events
======

.. _mailTabs.onDisplayedFolderChanged:

onDisplayedFolderChanged()
--------------------------

Fired when the displayed folder changes in any mail tab.

.. note::

  The permission ``accountsRead`` is required to use ``onDisplayedFolderChanged``.

.. _mailTabs.onSelectedMessagesChanged:

onSelectedMessagesChanged()
---------------------------

Fired when the selected messages change in any mail tab.

.. note::

  The permission ``messagesRead`` is required to use ``onSelectedMessagesChanged``.

Types
=====

.. _mailTabs.MailTab:

MailTab
-------

object

- ``active`` (boolean)
- ``displayedFolder`` (accounts.MailFolder)
- ``folderPaneVisible`` (boolean)
- ``id`` (integer)
- ``layout`` (`string <enum_layout_29_>`_)
- ``messagePaneVisible`` (boolean)
- ``sortOrder`` (`string <enum_sortOrder_31_>`_)
- ``sortType`` (`string <enum_sortType_32_>`_)
- ``windowId`` (integer)

.. _enum_layout_29:

Values for layout:

- ``standard``
- ``wide``
- ``vertical``

.. _enum_sortOrder_31:

Values for sortOrder:

- ``none``
- ``ascending``
- ``descending``

.. _enum_sortType_32:

Values for sortType:

- ``none``
- ``date``
- ``subject``
- ``author``
- ``id``
- ``thread``
- ``priority``
- ``status``
- ``size``
- ``flagged``
- ``unread``
- ``recipient``
- ``location``
- ``tags``
- ``junkStatus``
- ``attachments``
- ``account``
- ``custom``
- ``received``
- ``correspondent``

.. _mailTabs.QuickFilterTagsDetail:

QuickFilterTagsDetail
---------------------

object

- ``mode`` (`string <enum_mode_34_>`_) Whether all of the tag filters must apply, or any of them.
- ``tags`` (object) Object keys are tags to filter on, values are ``true`` if the message must have the tag, or ``false`` if it must not have the tag. For a list of available tags, call the :ref:`messages.listTags` method.

.. _enum_mode_34:

Values for mode:

- ``all``
- ``any``

.. _mailTabs.QuickFilterTextDetail:

QuickFilterTextDetail
---------------------

object

- ``text`` (string) String to match against the ``recipients``, ``author``, ``subject``, or ``body``.
- [``author``] (boolean) Shows messages where ``text`` matches the author.
- [``body``] (boolean) Shows messages where ``text`` matches the message body.
- [``recipients``] (boolean) Shows messages where ``text`` matches the recipients.
- [``sender``] (boolean) **Deprecated.** Use ``author`` instead.
- [``subject``] (boolean) Shows messages where ``text`` matches the subject.
