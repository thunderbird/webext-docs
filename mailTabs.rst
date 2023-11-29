.. _mailTabs_api:

============
mailTabs API
============

The mailTabs API first appeared in Thunderbird 66 and allows to interact with Thunderbirds main mail window.

The `Filter`__  and `Layout`__ sample extensions use this API.

__ https://github.com/thunderbird/sample-extensions/tree/master/filter
__ https://github.com/thunderbird/sample-extensions/tree/master/layout

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Functions
=========

.. _mailTabs.query:

query(queryInfo)
----------------

.. api-section-annotation-hack:: 

Gets all mail tabs that have the specified properties, or all mail tabs if no properties are specified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``queryInfo``
      :type: (object)
      
      .. api-member::
         :name: [``active``]
         :type: (boolean)
         
         Whether the tabs are active in their windows.
      
      
      .. api-member::
         :name: [``currentWindow``]
         :type: (boolean)
         
         Whether the tabs are in the current window.
      
      
      .. api-member::
         :name: [``lastFocusedWindow``]
         :type: (boolean)
         
         Whether the tabs are in the last focused window.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer)
         
         The ID of the parent window, or :ref:`windows.WINDOW_ID_CURRENT` for the current window.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`mailTabs.MailTab`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mailTabs.get:

get(tabId)
----------

.. api-section-annotation-hack:: 

Get the properties of a mail tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      
      ID of the requested mail tab. Throws if the requested tab is not a mail tab.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`mailTabs.MailTab`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mailTabs.getCurrent:

getCurrent()
------------

.. api-section-annotation-hack:: 

Get the properties of the active mail tab, if the active tab is a mail tab. Returns undefined otherwise.

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`mailTabs.MailTab`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mailTabs.update:

update([tabId], updateProperties)
---------------------------------

.. api-section-annotation-hack:: 

Modifies the properties of a mail tab. Properties that are not specified in ``updateProperties`` are not modified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      Defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``updateProperties``
      :type: (object)
      
      .. api-member::
         :name: [``displayedFolder``]
         :type: (:ref:`folders.MailFolder`)
         
         Sets the folder displayed in the tab. The extension must have the :permission:`accountsRead` permission to do this.
      
      
      .. api-member::
         :name: [``folderPaneVisible``]
         :type: (boolean)
         
         Shows or hides the folder pane.
      
      
      .. api-member::
         :name: [``layout``]
         :type: (`string`)
         
         Sets the arrangement of the folder pane, message list pane, and message display pane. Note that setting this applies it to all mail tabs.
         
         Supported values:
         
         .. api-member::
            :name: :value:`standard`
         
         .. api-member::
            :name: :value:`wide`
         
         .. api-member::
            :name: :value:`vertical`
      
      
      .. api-member::
         :name: [``messagePaneVisible``]
         :type: (boolean)
         
         Shows or hides the message display pane.
      
      
      .. api-member::
         :name: [``sortOrder``]
         :type: (`string`)
         
         Sorts the list of messages. ``sortType`` must also be given.
         
         Supported values:
         
         .. api-member::
            :name: :value:`none`
         
         .. api-member::
            :name: :value:`ascending`
         
         .. api-member::
            :name: :value:`descending`
      
      
      .. api-member::
         :name: [``sortType``]
         :type: (`string`)
         
         Sorts the list of messages. ``sortOrder`` must also be given.
         
         Supported values:
         
         .. api-member::
            :name: :value:`none`
         
         .. api-member::
            :name: :value:`date`
         
         .. api-member::
            :name: :value:`subject`
         
         .. api-member::
            :name: :value:`author`
         
         .. api-member::
            :name: :value:`id`
         
         .. api-member::
            :name: :value:`thread`
         
         .. api-member::
            :name: :value:`priority`
         
         .. api-member::
            :name: :value:`status`
         
         .. api-member::
            :name: :value:`size`
         
         .. api-member::
            :name: :value:`flagged`
         
         .. api-member::
            :name: :value:`unread`
         
         .. api-member::
            :name: :value:`recipient`
         
         .. api-member::
            :name: :value:`location`
         
         .. api-member::
            :name: :value:`tags`
         
         .. api-member::
            :name: :value:`junkStatus`
         
         .. api-member::
            :name: :value:`attachments`
         
         .. api-member::
            :name: :value:`account`
         
         .. api-member::
            :name: :value:`custom`
         
         .. api-member::
            :name: :value:`received`
         
         .. api-member::
            :name: :value:`correspondent`
      
      
      .. api-member::
         :name: [``viewType``]
         :type: (`string`)
         :annotation: -- [Added in TB 91]
         
         Supported values:
         
         .. api-member::
            :name: :value:`ungrouped`
         
         .. api-member::
            :name: :value:`groupedByThread`
         
         .. api-member::
            :name: :value:`groupedBySortType`
      
   

.. _mailTabs.getSelectedMessages:

getSelectedMessages([tabId])
----------------------------

.. api-section-annotation-hack:: 

Lists the selected messages in the current folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      Defaults to the active tab of the current window.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`messages.MessageList`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _mailTabs.setSelectedMessages:

setSelectedMessages([tabId], messageIds)
----------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 106, backported to TB 102.3.3]

Selects none, one or multiple messages.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      Defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``messageIds``
      :type: (array of integer)
      
      The IDs of the messages, which should be selected. The mailTab will switch to the folder of the selected messages. Throws if they belong to different folders. Array can be empty to deselect any currently selected message.
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesRead`

.. _mailTabs.setQuickFilter:

setQuickFilter([tabId], properties)
-----------------------------------

.. api-section-annotation-hack:: 

Sets the Quick Filter user interface based on the options specified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      Defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``properties``
      :type: (object)
      
      .. api-member::
         :name: [``attachment``]
         :type: (boolean)
         
         Shows only messages with attachments.
      
      
      .. api-member::
         :name: [``contact``]
         :type: (boolean)
         
         Shows only messages from people in the address book.
      
      
      .. api-member::
         :name: [``flagged``]
         :type: (boolean)
         
         Shows only flagged messages.
      
      
      .. api-member::
         :name: [``show``]
         :type: (boolean)
         
         Shows or hides the Quick Filter bar.
      
      
      .. api-member::
         :name: [``tags``]
         :type: (boolean or :ref:`messages.TagsDetail`)
         
         Shows only messages with tags on them.
      
      
      .. api-member::
         :name: [``text``]
         :type: (:ref:`mailTabs.QuickFilterTextDetail`)
         
         Shows only messages matching the supplied text.
      
      
      .. api-member::
         :name: [``unread``]
         :type: (boolean)
         
         Shows only unread messages.
      
   

.. rst-class:: api-main-section

Events
======

.. _mailTabs.onDisplayedFolderChanged:

onDisplayedFolderChanged
------------------------

.. api-section-annotation-hack:: 

Fired when the displayed folder changes in any mail tab.

.. api-header::
   :label: Parameters for onDisplayedFolderChanged.addListener(listener)

   
   .. api-member::
      :name: ``listener(tab, displayedFolder)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      
      .. container:: api-member-inline-changes
      
         :Changes in TB 76: previously just the tab's ID
      
   
   
   .. api-member::
      :name: ``displayedFolder``
      :type: (:ref:`folders.MailFolder`)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _mailTabs.onSelectedMessagesChanged:

onSelectedMessagesChanged
-------------------------

.. api-section-annotation-hack:: 

Fired when the selected messages change in any mail tab.

.. api-header::
   :label: Parameters for onSelectedMessagesChanged.addListener(listener)

   
   .. api-member::
      :name: ``listener(tab, selectedMessages)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      
      .. container:: api-member-inline-changes
      
         :Changes in TB 76: previously just the tab's ID
      
   
   
   .. api-member::
      :name: ``selectedMessages``
      :type: (:ref:`messages.MessageList`)
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. rst-class:: api-main-section

Types
=====

.. _mailTabs.MailTab:

MailTab
-------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``active``
      :type: (boolean)
   
   
   .. api-member::
      :name: ``id``
      :type: (integer)
   
   
   .. api-member::
      :name: ``layout``
      :type: (`string`)
      
      Supported values:
      
      .. api-member::
         :name: :value:`standard`
      
      .. api-member::
         :name: :value:`wide`
      
      .. api-member::
         :name: :value:`vertical`
   
   
   .. api-member::
      :name: ``windowId``
      :type: (integer)
   
   
   .. api-member::
      :name: [``displayedFolder``]
      :type: (:ref:`folders.MailFolder`)
      
      The :permission:`accountsRead` permission is required for this property to be included.
   
   
   .. api-member::
      :name: [``folderPaneVisible``]
      :type: (boolean)
   
   
   .. api-member::
      :name: [``messagePaneVisible``]
      :type: (boolean)
   
   
   .. api-member::
      :name: [``sortOrder``]
      :type: (`string`)
      
      **Note:** ``sortType`` and ``sortOrder`` depend on each other, so both should be present, or neither.
      
      Supported values:
      
      .. api-member::
         :name: :value:`none`
      
      .. api-member::
         :name: :value:`ascending`
      
      .. api-member::
         :name: :value:`descending`
   
   
   .. api-member::
      :name: [``sortType``]
      :type: (`string`)
      
      **Note:** ``sortType`` and ``sortOrder`` depend on each other, so both should be present, or neither.
      
      Supported values:
      
      .. api-member::
         :name: :value:`none`
      
      .. api-member::
         :name: :value:`date`
      
      .. api-member::
         :name: :value:`subject`
      
      .. api-member::
         :name: :value:`author`
      
      .. api-member::
         :name: :value:`id`
      
      .. api-member::
         :name: :value:`thread`
      
      .. api-member::
         :name: :value:`priority`
      
      .. api-member::
         :name: :value:`status`
      
      .. api-member::
         :name: :value:`size`
      
      .. api-member::
         :name: :value:`flagged`
      
      .. api-member::
         :name: :value:`unread`
      
      .. api-member::
         :name: :value:`recipient`
      
      .. api-member::
         :name: :value:`location`
      
      .. api-member::
         :name: :value:`tags`
      
      .. api-member::
         :name: :value:`junkStatus`
      
      .. api-member::
         :name: :value:`attachments`
      
      .. api-member::
         :name: :value:`account`
      
      .. api-member::
         :name: :value:`custom`
      
      .. api-member::
         :name: :value:`received`
      
      .. api-member::
         :name: :value:`correspondent`
   
   
   .. api-member::
      :name: [``viewType``]
      :type: (`string`)
      :annotation: -- [Added in TB 91]
      
      Supported values:
      
      .. api-member::
         :name: :value:`ungrouped`
      
      .. api-member::
         :name: :value:`groupedByThread`
      
      .. api-member::
         :name: :value:`groupedBySortType`
   

.. _mailTabs.QuickFilterTextDetail:

QuickFilterTextDetail
---------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``text``
      :type: (string)
      
      String to match against the ``recipients``, ``author``, ``subject``, or ``body``.
   
   
   .. api-member::
      :name: [``author``]
      :type: (boolean)
      
      Shows messages where ``text`` matches the author.
   
   
   .. api-member::
      :name: [``body``]
      :type: (boolean)
      
      Shows messages where ``text`` matches the message body.
   
   
   .. api-member::
      :name: [``recipients``]
      :type: (boolean)
      
      Shows messages where ``text`` matches the recipients.
   
   
   .. api-member::
      :name: [``subject``]
      :type: (boolean)
      
      Shows messages where ``text`` matches the subject.
   
