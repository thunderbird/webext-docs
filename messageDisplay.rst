==============
messageDisplay
==============

The message display API first appeared in Thunderbird 70.

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
