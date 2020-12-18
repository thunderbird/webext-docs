========
mailTabs
========

The messages API first appeared in Thunderbird 66 (see `bug 1499617`__).

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1499617

The `Filter`__  and `Layout`__ sample extensions use this API.

__ https://github.com/thundernest/sample-extensions/tree/master/filter
__ https://github.com/thundernest/sample-extensions/tree/master/layout

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
      :annotation: 
      
      .. api-member::
         :name: [``active``]
         :type: (boolean)
         :annotation: 
         
         Whether the tabs are active in their windows.
      
      
      .. api-member::
         :name: [``currentWindow``]
         :type: (boolean)
         :annotation: 
         
         Whether the tabs are in the current window.
      
      
      .. api-member::
         :name: [``lastFocusedWindow``]
         :type: (boolean)
         :annotation: 
         
         Whether the tabs are in the last focused window.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer)
         :annotation: 
         
         The ID of the parent window, or :ref:`windows.WINDOW_ID_CURRENT` for the current window.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: array of :ref:`mailTabs.MailTab`
      :annotation: 
   
   
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
      :annotation: 
      
      Defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``updateProperties``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``displayedFolder``]
         :type: (:ref:`folders.MailFolder`)
         :annotation: 
         
         Sets the folder displayed in the tab. The extension must have an accounts permission to do this.
      
      
      .. api-member::
         :name: [``folderPaneVisible``]
         :type: (boolean)
         :annotation: 
         
         Shows or hides the folder pane.
      
      
      .. api-member::
         :name: [``layout``]
         :type: (`string`)
         :annotation: 
         
         Sets the arrangement of the folder pane, message list pane, and message display pane. Note that setting this applies it to all mail tabs.
         
         Supported values:
         
         .. api-member::
            :name: ``standard``
         
         .. api-member::
            :name: ``wide``
         
         .. api-member::
            :name: ``vertical``
         
      
      
      .. api-member::
         :name: [``messagePaneVisible``]
         :type: (boolean)
         :annotation: 
         
         Shows or hides the message display pane.
      
      
      .. api-member::
         :name: [``sortOrder``]
         :type: (`string`)
         :annotation: 
         
         Sorts the list of messages. ``sortType`` must also be given.
         
         Supported values:
         
         .. api-member::
            :name: ``none``
         
         .. api-member::
            :name: ``ascending``
         
         .. api-member::
            :name: ``descending``
         
      
      
      .. api-member::
         :name: [``sortType``]
         :type: (`string`)
         :annotation: 
         
         Sorts the list of messages. ``sortOrder`` must also be given.
         
         Supported values:
         
         .. api-member::
            :name: ``none``
         
         .. api-member::
            :name: ``date``
         
         .. api-member::
            :name: ``subject``
         
         .. api-member::
            :name: ``author``
         
         .. api-member::
            :name: ``id``
         
         .. api-member::
            :name: ``thread``
         
         .. api-member::
            :name: ``priority``
         
         .. api-member::
            :name: ``status``
         
         .. api-member::
            :name: ``size``
         
         .. api-member::
            :name: ``flagged``
         
         .. api-member::
            :name: ``unread``
         
         .. api-member::
            :name: ``recipient``
         
         .. api-member::
            :name: ``location``
         
         .. api-member::
            :name: ``tags``
         
         .. api-member::
            :name: ``junkStatus``
         
         .. api-member::
            :name: ``attachments``
         
         .. api-member::
            :name: ``account``
         
         .. api-member::
            :name: ``custom``
         
         .. api-member::
            :name: ``received``
         
         .. api-member::
            :name: ``correspondent``
         
      
   

.. _mailTabs.getSelectedMessages:

getSelectedMessages([tabId])
----------------------------

.. api-section-annotation-hack:: 

Lists the selected messages in the current folder. A messages permission is required to do this.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      :annotation: 
      
      Defaults to the active tab of the current window.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`messages.MessageList`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - ``messagesRead``

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
      :annotation: 
      
      Defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``properties``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``attachment``]
         :type: (boolean)
         :annotation: 
         
         Shows only messages with attachments.
      
      
      .. api-member::
         :name: [``contact``]
         :type: (boolean)
         :annotation: 
         
         Shows only messages from people in the address book.
      
      
      .. api-member::
         :name: [``flagged``]
         :type: (boolean)
         :annotation: 
         
         Shows only flagged messages.
      
      
      .. api-member::
         :name: [``show``]
         :type: (boolean)
         :annotation: 
         
         Shows or hides the Quick Filter bar.
      
      
      .. api-member::
         :name: [``tags``]
         :type: (boolean or :ref:`messages.TagsDetail`)
         :annotation: 
         
         Shows only messages with tags on them.
      
      
      .. api-member::
         :name: [``text``]
         :type: (:ref:`mailTabs.QuickFilterTextDetail`)
         :annotation: 
         
         Shows only messages matching the supplied text.
      
      
      .. api-member::
         :name: [``unread``]
         :type: (boolean)
         :annotation: 
         
         Shows only unread messages.
      
   

.. rst-class:: api-main-section

Events
======

.. _mailTabs.onDisplayedFolderChanged:

onDisplayedFolderChanged(tab, displayedFolder)
----------------------------------------------

.. api-section-annotation-hack:: 

Fired when the displayed folder changes in any mail tab.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Changed in TB 76, previously just the tab's ID]
   
   
   .. api-member::
      :name: ``displayedFolder``
      :type: (:ref:`folders.MailFolder`)
      :annotation: 
   

.. api-header::
   :label: Required permissions

   - ``accountsRead``

.. _mailTabs.onSelectedMessagesChanged:

onSelectedMessagesChanged(tab, selectedMessages)
------------------------------------------------

.. api-section-annotation-hack:: 

Fired when the selected messages change in any mail tab.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Changed in TB 76, previously just the tab's ID]
   
   
   .. api-member::
      :name: ``selectedMessages``
      :type: (:ref:`messages.MessageList`)
      :annotation: 
   

.. api-header::
   :label: Required permissions

   - ``messagesRead``

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
      :annotation: 
   
   
   .. api-member::
      :name: ``displayedFolder``
      :type: (:ref:`folders.MailFolder`)
      :annotation: 
      
      The ``accountsRead`` permission is required.
   
   
   .. api-member::
      :name: ``folderPaneVisible``
      :type: (boolean)
      :annotation: 
   
   
   .. api-member::
      :name: ``id``
      :type: (integer)
      :annotation: 
   
   
   .. api-member::
      :name: ``layout``
      :type: (`string`)
      :annotation: 
      
      Supported values:
      
      .. api-member::
         :name: ``standard``
      
      .. api-member::
         :name: ``wide``
      
      .. api-member::
         :name: ``vertical``
      
   
   
   .. api-member::
      :name: ``messagePaneVisible``
      :type: (boolean)
      :annotation: 
   
   
   .. api-member::
      :name: ``sortOrder``
      :type: (`string`)
      :annotation: 
      
      Supported values:
      
      .. api-member::
         :name: ``none``
      
      .. api-member::
         :name: ``ascending``
      
      .. api-member::
         :name: ``descending``
      
   
   
   .. api-member::
      :name: ``sortType``
      :type: (`string`)
      :annotation: 
      
      Supported values:
      
      .. api-member::
         :name: ``none``
      
      .. api-member::
         :name: ``date``
      
      .. api-member::
         :name: ``subject``
      
      .. api-member::
         :name: ``author``
      
      .. api-member::
         :name: ``id``
      
      .. api-member::
         :name: ``thread``
      
      .. api-member::
         :name: ``priority``
      
      .. api-member::
         :name: ``status``
      
      .. api-member::
         :name: ``size``
      
      .. api-member::
         :name: ``flagged``
      
      .. api-member::
         :name: ``unread``
      
      .. api-member::
         :name: ``recipient``
      
      .. api-member::
         :name: ``location``
      
      .. api-member::
         :name: ``tags``
      
      .. api-member::
         :name: ``junkStatus``
      
      .. api-member::
         :name: ``attachments``
      
      .. api-member::
         :name: ``account``
      
      .. api-member::
         :name: ``custom``
      
      .. api-member::
         :name: ``received``
      
      .. api-member::
         :name: ``correspondent``
      
   
   
   .. api-member::
      :name: ``windowId``
      :type: (integer)
      :annotation: 
   

.. _mailTabs.QuickFilterTextDetail:

QuickFilterTextDetail
---------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``text``
      :type: (string)
      :annotation: 
      
      String to match against the ``recipients``, ``author``, ``subject``, or ``body``.
   
   
   .. api-member::
      :name: [``author``]
      :type: (boolean)
      :annotation: 
      
      Shows messages where ``text`` matches the author.
   
   
   .. api-member::
      :name: [``body``]
      :type: (boolean)
      :annotation: 
      
      Shows messages where ``text`` matches the message body.
   
   
   .. api-member::
      :name: [``recipients``]
      :type: (boolean)
      :annotation: 
      
      Shows messages where ``text`` matches the recipients.
   
   
   .. api-member::
      :name: [``subject``]
      :type: (boolean)
      :annotation: 
      
      Shows messages where ``text`` matches the subject.
   
