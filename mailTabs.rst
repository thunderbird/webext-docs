.. container:: sticky-sidebar

  ≡ mailTabs API

  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /overlay/developer-resources.rst

  ≡ Related information
  
  * :doc:`/examples/eventListeners`

  ≡ Related examples on Github

  * `"Quickfilter" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v2/quickfilter>`__
  * `"MailTab Layout" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v2/mailtabs>`__

============
mailTabs API
============

The mailTabs API allows to interact with Thunderbird's main mail window.

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Functions
=========

.. _mailTabs.create:

create([createProperties])
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Creates a new mail tab. Standard tab properties can be adjusted via :ref:`tabs.update` after the mail tab has been created. **Note:** A new mail window can be created via :ref:`windows.create`.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``createProperties``]
      :type: (:ref:`mailTabs.MailTabProperties`, optional)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`mailTabs.MailTab`
      
      Details about the created mail tab. Will contain the ID of the new tab.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mailTabs.get:

get(tabId)
----------

.. api-section-annotation-hack:: 

Get the :ref:`mailTabs.MailTab` properties of a mail tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      
      ID of the requested mail tab. Throws if the requested :value:`tabId` does not belong to a mail tab.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`mailTabs.MailTab`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mailTabs.getCurrent:

getCurrent()
------------

.. api-section-annotation-hack:: 

Get the :ref:`mailTabs.MailTab` properties of the active mail tab. Returns :value:`undefined`, if the active tab is not a mail tab.

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`mailTabs.MailTab`
      
      This may return undefined
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mailTabs.getListedMessages:

getListedMessages([tabId])
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Lists the messages in the current view, honoring sort order and filters.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)
      
      Defaults to the active tab of the current window.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`messages.MessageList`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _mailTabs.getSelectedFolders:

getSelectedFolders([tabId])
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Lists the selected folders in the folder pane.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)
      
      Defaults to the active tab of the current window.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`folders.MailFolder`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _mailTabs.getSelectedMessages:

getSelectedMessages([tabId])
----------------------------

.. api-section-annotation-hack:: 

Lists the selected messages in the current folder.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)
      
      Defaults to the active tab of the current window.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`messages.MessageList`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _mailTabs.query:

query([queryInfo])
------------------

.. api-section-annotation-hack:: 

Gets all mail tabs that have the specified properties, or all mail tabs if no properties are specified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``queryInfo``]
      :type: (object, optional)
      
      .. api-member::
         :name: [``active``]
         :type: (boolean, optional)
         
         Whether the tabs are active in their windows.
      
      
      .. api-member::
         :name: [``currentWindow``]
         :type: (boolean, optional)
         
         Whether the tabs are in the current window.
      
      
      .. api-member::
         :name: [``lastFocusedWindow``]
         :type: (boolean, optional)
         
         Whether the tabs are in the last focused window.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer, optional)
         
         The ID of the parent window, or :ref:`windows.WINDOW_ID_CURRENT` for the current window.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`mailTabs.MailTab`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mailTabs.setQuickFilter:

setQuickFilter([tabId], properties)
-----------------------------------

.. api-section-annotation-hack:: 

Sets the Quick Filter user interface based on the options specified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)
      
      Defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``properties``
      :type: (object)
      
      .. api-member::
         :name: [``attachment``]
         :type: (boolean, optional)
         
         Shows only messages with attachments.
      
      
      .. api-member::
         :name: [``contact``]
         :type: (boolean, optional)
         
         Shows only messages from people in the address book.
      
      
      .. api-member::
         :name: [``flagged``]
         :type: (boolean, optional)
         
         Shows only flagged messages.
      
      
      .. api-member::
         :name: [``show``]
         :type: (boolean, optional)
         
         Shows or hides the Quick Filter bar.
      
      
      .. api-member::
         :name: [``tags``]
         :type: (boolean or :ref:`messages.tags.TagsDetail`, optional)
         
         Shows only messages with tags on them.
      
      
      .. api-member::
         :name: [``text``]
         :type: (:ref:`mailTabs.QuickFilterTextDetail`, optional)
         
         Shows only messages matching the supplied text.
      
      
      .. api-member::
         :name: [``unread``]
         :type: (boolean, optional)
         
         Shows only unread messages.
      
   

.. _mailTabs.setSelectedMessages:

setSelectedMessages([tabId], messageIds)
----------------------------------------

.. api-section-annotation-hack:: 

Selects none, one or multiple messages.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)
      
      Defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``messageIds``
      :type: (array of :ref:`messages.MessageId`)
      
      The IDs of the messages, which should be selected. The mail tab will switch to the folder of the selected messages. Throws if they belong to different folders. Array can be empty to deselect any currently selected message.
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesRead`

.. _mailTabs.update:

update([tabId], updateProperties)
---------------------------------

.. api-section-annotation-hack:: 

Modifies the properties of a mail tab. Properties that are not specified in :value:`updateProperties` are not modified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)
      
      Defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``updateProperties``
      :type: (:ref:`mailTabs.MailTabProperties`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`mailTabs.MailTab`
      
      Details about the updated mail tab.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

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

.. _mailTabs.FolderMode:

FolderMode
----------

.. api-section-annotation-hack:: 

A supported folder mode in the folder pane.

.. api-header::
   :label: `string`

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         Supported values:
         
         .. api-member::
            :name: :value:`all`
         
         .. api-member::
            :name: :value:`unified`
         
         .. api-member::
            :name: :value:`tags`
         
         .. api-member::
            :name: :value:`unread`
         
         .. api-member::
            :name: :value:`favorite`
         
         .. api-member::
            :name: :value:`recent`
   

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
      
      The arrangement of the folder pane, message list pane, and message display pane.
      
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
      :type: (:ref:`folders.MailFolder`, optional)
      
      The folder displayed in the mail tab. The :permission:`accountsRead` permission is required for this property to be included.
   
   
   .. api-member::
      :name: [``folderMode``]
      :type: (:ref:`mailTabs.FolderMode`, optional)
      :annotation: -- [Added in TB 125]
      
      The folder mode of the currently displayed folder.
   
   
   .. api-member::
      :name: [``folderModesEnabled``]
      :type: (array of :ref:`mailTabs.FolderMode`, optional)
      :annotation: -- [Added in TB 125]
      
      The enabled folder modes in the folder pane, and their sort order.
   
   
   .. api-member::
      :name: [``folderPaneVisible``]
      :type: (boolean, optional)
      
      Whether the folder pane is visible or not.
   
   
   .. api-member::
      :name: [``messagePaneVisible``]
      :type: (boolean, optional)
      
      Whether the message pane is visible or not.
   
   
   .. api-member::
      :name: [``sortOrder``]
      :type: (`string`, optional)
      
      The sort order of the message list.
      
      Supported values:
      
      .. api-member::
         :name: :value:`none`
      
      .. api-member::
         :name: :value:`ascending`
      
      .. api-member::
         :name: :value:`descending`
   
   
   .. api-member::
      :name: [``sortType``]
      :type: (`string`, optional)
      
      The primary sort column of the message list.
      
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
      :type: (`string`, optional)
      :annotation: -- [Added in TB 91]
      
      Grouping type of the message list.
      
      Supported values:
      
      .. api-member::
         :name: :value:`ungrouped`
      
      .. api-member::
         :name: :value:`groupedByThread`
      
      .. api-member::
         :name: :value:`groupedBySortType`
   

.. _mailTabs.MailTabProperties:

MailTabProperties
-----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``displayedFolder``]
      :type: (:ref:`folders.MailFolderId` or :ref:`folders.MailFolder`, optional)
      
      Sets the folder displayed in the mail tab. Requires the :permission:`accountsRead` permission. The previous message selection in the given folder will be restored, if any.
   
   
   .. api-member::
      :name: [``folderMode``]
      :type: (:ref:`mailTabs.FolderMode`, optional)
      :annotation: -- [Added in TB 125]
      
      Sets the currently used folder mode, enabling it if required. If used without also specifying :value:`displayedFolder`, the currently selected folder is re-selected in the new folder mode, if possible.
   
   
   .. api-member::
      :name: [``folderModesEnabled``]
      :type: (array of :ref:`mailTabs.FolderMode`, optional)
      :annotation: -- [Added in TB 125]
      
      Set the enabled folder modes in the folder pane, and their sort order.
   
   
   .. api-member::
      :name: [``folderPaneVisible``]
      :type: (boolean, optional)
      
      Shows or hides the folder pane.
   
   
   .. api-member::
      :name: [``layout``]
      :type: (`string`, optional)
      
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
      :type: (boolean, optional)
      
      Shows or hides the message display pane.
   
   
   .. api-member::
      :name: [``sortOrder``]
      :type: (`string`, optional)
      
      Sorts the list of messages. :value:`sortType` must also be given.
      
      Supported values:
      
      .. api-member::
         :name: :value:`none`
      
      .. api-member::
         :name: :value:`ascending`
      
      .. api-member::
         :name: :value:`descending`
   
   
   .. api-member::
      :name: [``sortType``]
      :type: (`string`, optional)
      
      Sorts the list of messages. :value:`sortOrder` must also be given.
      
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
      :type: (`string`, optional)
      
      Sets the grouping type of displayed messages.
      
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
      
      String to match against the :value:`recipients`, :value:`author`, :value:`subject`, or :value:`body`.
   
   
   .. api-member::
      :name: [``author``]
      :type: (boolean, optional)
      
      Shows messages where :value:`text` matches the author.
   
   
   .. api-member::
      :name: [``body``]
      :type: (boolean, optional)
      
      Shows messages where :value:`text` matches the message body.
   
   
   .. api-member::
      :name: [``recipients``]
      :type: (boolean, optional)
      
      Shows messages where :value:`text` matches the recipients.
   
   
   .. api-member::
      :name: [``subject``]
      :type: (boolean, optional)
      
      Shows messages where :value:`text` matches the subject.
   
