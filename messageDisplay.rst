.. _messageDisplay_api:

==============
messageDisplay
==============

The message display API first appeared in Thunderbird 70 and was backported to Thunderbird 68.2.

A message can be displayed in either a 3-pane tab, a tab of its own, or in a window of its own.
All are referenced by ``tabId`` in this API. Display windows are considered to have exactly one
tab, which has limited functionality compared to tabs from the main window.

More functions are planned for this API for adding to the user interface, as well as a message
display action (similar to :doc:`browserAction` and :doc:`composeAction`).

.. role:: permission

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messagesRead` is required to use ``messageDisplay``.

.. rst-class:: api-main-section

Functions
=========

.. _messageDisplay.getDisplayedMessage:

getDisplayedMessage(tabId)
--------------------------

.. api-section-annotation-hack:: 

Gets the currently displayed message in the specified tab, or null if no message is displayed.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`messages.MessageHeader`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. rst-class:: api-main-section

Events
======

.. _messageDisplay.onMessageDisplayed:

onMessageDisplayed(tabId, message)
----------------------------------

.. api-section-annotation-hack:: 

Fired when a message is displayed, whether in a 3-pane tab, a message tab, or a message window.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``message``
      :type: (:ref:`messages.MessageHeader`)
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
