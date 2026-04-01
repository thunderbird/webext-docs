.. container:: sticky-sidebar

  ≡ messageDisplay API

  * `Permissions`_
  * `Functions`_
  * `Events`_

  .. include:: /_includes/developer-resources.rst

==================
messageDisplay API
==================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

A message can be displayed in either Thunderbird's main mail tab (a.k.a 3-pane tab), a tab of its own, or in a window of its own. All are referenced by :value:`tabId` in this API. Display windows are considered to have exactly one tab, which has limited functionality compared to tabs from the main window.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _message^display.permission.messages^read:

.. api-member::
   :name: :permission:`messagesRead`
   :refid: message-display-permission-messages-read
   :refname: messagesRead

   Read your email messages.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messagesRead` is required to use ``messenger.messageDisplay.*``.

.. rst-class:: api-main-section

Functions
=========

.. _message^display.get^displayed^messages:

getDisplayedMessages([tabId])
-----------------------------

.. api-section-annotation-hack:: 

Gets an array of the currently displayed messages in the specified tab (even if the tab itself is currently not visible), or the currently active tab. The array is empty if no messages are displayed.

.. api-header::
   :label: Parameters

   .. _message^display.get^displayed^messages.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: message-display-get-displayed-messages-tab-id
      :refname: tabId
      :type: (integer, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _message^display.get^displayed^messages.returns:

   .. api-member::
      :refid: message-display-get-displayed-messages-returns
      :refname: _returns
      :type: :ref:`messages.^message^list`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _message^display.open:

open(openProperties)
--------------------

.. api-section-annotation-hack:: 

Opens a message in a new tab or in a new window.

.. api-header::
   :label: Parameters

   .. _message^display.open.open^properties:

   .. api-member::
      :name: ``openProperties``
      :refid: message-display-open-open-properties
      :refname: openProperties
      :type: (object)

      Settings for opening the message. Exactly one of messageId, headerMessageId or file must be specified.

      .. _message^display.open.open^properties.active:

      .. api-member::
         :name: [``active``]
         :refid: message-display-open-open-properties-active
         :refname: active
         :type: (boolean, optional)

         Whether the new tab should become the active tab in the window. Only applicable to messages opened in tabs.

      .. _message^display.open.open^properties.file:

      .. api-member::
         :name: [``file``]
         :refid: message-display-open-open-properties-file
         :refname: file
         :type: (`File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__, optional)

         The DOM file object of a message to be opened.

      .. _message^display.open.open^properties.header^message^id:

      .. api-member::
         :name: [``headerMessageId``]
         :refid: message-display-open-open-properties-header-message-id
         :refname: headerMessageId
         :type: (string, optional)

         The headerMessageId of a message to be opened. Will throw an *ExtensionError*, if the provided :value:`headerMessageId` is unknown or invalid. Not supported for external messages.

      .. _message^display.open.open^properties.location:

      .. api-member::
         :name: [``location``]
         :refid: message-display-open-open-properties-location
         :refname: location
         :type: (`string`, optional)

         Where to open the message. If not specified, the users preference is honoured.

         Supported values:

         .. _message^display.open.open^properties.location.tab:

         .. api-member::
            :name: :value:`tab`
            :refid: message-display-open-open-properties-location-tab
            :refname: tab

         .. _message^display.open.open^properties.location.window:

         .. api-member::
            :name: :value:`window`
            :refid: message-display-open-open-properties-location-window
            :refname: window

      .. _message^display.open.open^properties.message^id:

      .. api-member::
         :name: [``messageId``]
         :refid: message-display-open-open-properties-message-id
         :refname: messageId
         :type: (:ref:`messages.^message^id`, optional)

         The id of a message to be opened. Will throw an *ExtensionError*, if the provided :value:`messageId` is unknown or invalid.

      .. _message^display.open.open^properties.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: message-display-open-open-properties-window-id
         :refname: windowId
         :type: (integer, optional)

         The id of the window, where the new tab should be created. Defaults to the current window. Only applicable to messages opened in tabs.

.. api-header::
   :label: Return type (`Promise`_)

   .. _message^display.open.returns:

   .. api-member::
      :refid: message-display-open-returns
      :refname: _returns
      :type: :ref:`tabs.^tab`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. rst-class:: api-main-section

Events
======

.. _message^display.on^messages^displayed:

onMessagesDisplayed
-------------------

.. api-section-annotation-hack:: 

Fired when either a single message is displayed or when multiple messages are displayed, whether in a 3-pane tab, a message tab, or a message window.

.. api-header::
   :label: Parameters for onMessagesDisplayed.addListener(listener)

   .. _message^display.on^messages^displayed.listener(tab, displayed^messages):

   .. api-member::
      :name: ``listener(tab, displayedMessages)``
      :refid: message-display-on-messages-displayed-listener-tab-displayed-messages
      :refname: listener(tab, displayedMessages)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _message^display.on^messages^displayed.tab:

   .. api-member::
      :name: ``tab``
      :refid: message-display-on-messages-displayed-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)

   .. _message^display.on^messages^displayed.displayed^messages:

   .. api-member::
      :name: ``displayedMessages``
      :refid: message-display-on-messages-displayed-displayed-messages
      :refname: displayedMessages
      :type: (:ref:`messages.^message^list`)

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`
