.. _messageDisplay_api:

==============
messageDisplay
==============

The message display API first appeared in Thunderbird 68.

A message can be displayed in either a 3-pane tab, a tab of its own, or in a window of its own.
All are referenced by ``tabId`` in this API. Display windows are considered to have exactly one
tab, which has limited functionality compared to tabs from the main window.

.. role:: permission

.. role:: value

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

Gets the currently displayed message in the specified tab (even if the tab itself is currently not visible). It returns null if no messages are displayed, or if multiple messages are displayed.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`messages.MessageHeader` or null
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messageDisplay.getDisplayedMessages:

getDisplayedMessages(tabId)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 81, backported to TB 78.4.0]

Gets an array of the currently displayed messages in the specified tab (even if the tab itself is currently not visible). The array is empty if no messages are displayed.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`messages.MessageHeader`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messageDisplay.open:

open(openProperties)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 102]

Opens a message in a new tab or in a new window.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``openProperties``
      :type: (object)
      
      Settings for opening the message. Exactly one of messageId or headerMessageId must be specified.
      
      .. api-member::
         :name: [``active``]
         :type: (boolean)
         
         Whether the new tab should become the active tab in the window. Only applicable to messages opened in tabs.
      
      
      .. api-member::
         :name: [``headerMessageId``]
         :type: (string)
         
         The headerMessageId of a message to be opened. Will throw an ``ExtensionError``, if the provided ``headerMessageId`` is unknown or invalid. Not supported for external messages.
      
      
      .. api-member::
         :name: [``location``]
         :type: (`string`)
         
         Where to open the message. If not specified, the users preference is honoured. Ignored for external messages, which are always opened in a new window.
         
         Supported values:
         
         .. api-member::
            :name: ``tab``
         
         .. api-member::
            :name: ``window``
      
      
      .. api-member::
         :name: [``messageId``]
         :type: (integer)
         
         The id of a message to be opened. Will throw an ``ExtensionError``, if the provided ``messageId`` is unknown or invalid.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer)
         
         The id of the window, where the new tab should be created. Defaults to the current window. Only applicable to messages opened in tabs.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`tabs.Tab`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. rst-class:: api-main-section

Events
======

.. _messageDisplay.onMessageDisplayed:

onMessageDisplayed
------------------

.. api-section-annotation-hack:: 

Fired when a message is displayed, whether in a 3-pane tab, a message tab, or a message window.

.. api-header::
   :label: Parameters for onMessageDisplayed.addListener(listener)

   
   .. api-member::
      :name: ``listener(tab, message)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      
      .. container:: api-member-inline-changes
      
         :Changes in TB 76: previously just the tab's ID
      
   
   
   .. api-member::
      :name: ``message``
      :type: (:ref:`messages.MessageHeader`)
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _messageDisplay.onMessagesDisplayed:

onMessagesDisplayed
-------------------

.. api-section-annotation-hack:: -- [Added in TB 81, backported to TB 78.4.0]

Fired when either a single message is displayed or when multiple messages are displayed, whether in a 3-pane tab, a message tab, or a message window.

.. api-header::
   :label: Parameters for onMessagesDisplayed.addListener(listener)

   
   .. api-member::
      :name: ``listener(tab, messages)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
   
   
   .. api-member::
      :name: ``messages``
      :type: (array of :ref:`messages.MessageHeader`)
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
