==============
messageDisplay
==============

The message display API first appeared in Thunderbird 70 and was backported to Thunderbird 68.2.

A message can be displayed in either a 3-pane tab, a tab of its own, or in a window of its own.
All are referenced by ``tabId`` in this API. Display windows are considered to have exactly one
tab, which has limited functionality compared to tabs from the main window.

More functions are planned for this API for adding to the user interface, as well as a message
display action (similar to :doc:`browserAction` and :doc:`composeAction`).

.. note::

  The permission ``messagesRead`` is required to use ``messageDisplay``.

Functions
=========

.. _messageDisplay.getDisplayedMessage:

getDisplayedMessage(tabId)
--------------------------

Gets the currently displayed message in the specified tab. It returns null if no messages are selected, or if multiple messages are selected.

- ``tabId`` (integer)

Returns a `Promise`_ fulfilled with:

- :ref:`messages.MessageHeader`

.. _messageDisplay.getDisplayedMessages:

getDisplayedMessages(tabId)
---------------------------

*Added in Thunderbird 81, backported to 78.4*

Gets an array of the currently displayed messages in the specified tab. The array is empty if no messages are displayed.

- ``tabId`` (integer)

Returns a `Promise`_ fulfilled with:

- array of :ref:`messages.MessageHeader`

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Events
======

.. _messageDisplay.onMessageDisplayed:

onMessageDisplayed(tab, message)
--------------------------------

Fired when a message is displayed, whether in a 3-pane tab, a message tab, or a message window.

- ``tab`` (:ref:`tabs.Tab`) *Changed in Thunderbird 76, previously just the tab's ID*
- ``message`` (:ref:`messages.MessageHeader`)

.. _messageDisplay.onMessagesDisplayed:

onMessagesDisplayed(tab, messages)
----------------------------------

*Added in Thunderbird 81, backported to 78.4*

Fired when either a single message is displayed or when multiple messages are displayed, whether in a 3-pane tab, a message tab, or a message window.

- ``tab`` (:ref:`tabs.Tab`)
- ``messages`` (array of :ref:`messages.MessageHeader`)
