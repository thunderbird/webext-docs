==============
messageDisplay
==============

The message display API first appeared in Thunderbird 70.

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

Gets the currently displayed message in the specified tab, or null if no message is displayed.

- ``tabId`` (integer)

Returns a `Promise`_ fulfilled with:

- :ref:`messages.MessageHeader`

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Events
======

.. _messageDisplay.onMessageDisplayed:

onMessageDisplayed(tabId, message)
----------------------------------

Fired when a message is displayed, whether in a 3-pane tab, a message tab, or a message window.

- ``tabId`` (integer)
- ``message`` (:ref:`messages.MessageHeader`)
