.. container:: sticky-sidebar

  ≡ mailTabs API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

============
mailTabs API
============

.. role:: permission

.. role:: value

.. role:: code

The mailTabs API allows to interact with Thunderbird's main mail tab (a.k.a 3-pane tab).

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`accountsRead`

   See your mail accounts, their identities and their folders.

.. api-member::
   :name: :permission:`messagesRead`

   Read your email messages.

.. rst-class:: api-main-section

Functions
=========

.. _mail^tabs.create:

create([createProperties])
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Creates a new mail tab. Standard tab properties can be adjusted via :ref:`tabs.update` after the mail tab has been created. A new mail window can be created via :ref:`windows.create`.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``createProperties``]
      :type: (:ref:`mail^tabs.^mail^tab^properties`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`mail^tabs.^mail^tab`

      Details about the created mail tab. Will contain the ID of the new tab.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mail^tabs.get:

get(tabId)
----------

.. api-section-annotation-hack:: -- [Added in TB 89]

Get the :ref:`mail^tabs.^mail^tab` properties of a mail tab.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``tabId``
      :type: (integer)

      ID of the requested mail tab. Throws if the requested :value:`tabId` does not belong to a mail tab.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`mail^tabs.^mail^tab`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mail^tabs.get^listed^messages:

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
      :type: :ref:`messages.^message^list`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _mail^tabs.get^selected^folders:

getSelectedFolders([tabId])
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

Lists the selected folders in the folder pane. Does not include folders which are context-clicked, but not selected. The context-clicked folders are always returned by the :ref:`menus.on^clicked` event of the menus API.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)

      Defaults to the active tab of the current window.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _mail^tabs.get^selected^messages:

getSelectedMessages([tabId])
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Lists the selected messages in the current folder. Includes messages in collapsed threads. Does not include messages which are context-clicked, but not selected. The context-clicked messages are always returned by the :ref:`menus.on^clicked` event of the menus API.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)

      Defaults to the active tab of the current window.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`messages.^message^list`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _mail^tabs.query:

query([queryInfo])
------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

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

         The ID of the parent window, or :ref:`windows.^w^i^n^d^o^w_^i^d_^c^u^r^r^e^n^t` for the current window.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`mail^tabs.^mail^tab`
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mail^tabs.set^quick^filter:

setQuickFilter([tabId], properties)
-----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

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
         :annotation: -- [Added in TB 68]

         Shows only flagged messages.

      .. api-member::
         :name: [``show``]
         :type: (boolean, optional)

         Shows or hides the Quick Filter bar.

      .. api-member::
         :name: [``tags``]
         :type: (boolean or :ref:`messages.tags.^tags^detail`, optional)

         Shows only messages with tags on them.

      .. api-member::
         :name: [``text``]
         :type: (:ref:`mail^tabs.^quick^filter^text^detail`, optional)

         Shows only messages matching the supplied text.

      .. api-member::
         :name: [``unread``]
         :type: (boolean, optional)

         Shows only unread messages.

.. _mail^tabs.set^selected^messages:

setSelectedMessages([tabId], messageIds)
----------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 106]

Selects none, one or multiple messages. Opens collapsed threads to show the selection, if required.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)

      Defaults to the active tab of the current window.

   .. api-member::
      :name: ``messageIds``
      :type: (array of :ref:`messages.^message^id`)

      The IDs of the messages, which should be selected. The mail tab will switch to the folder of the selected messages. Throws if they belong to different folders. Array can be empty to deselect any currently selected message.

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesRead`

.. _mail^tabs.update:

update([tabId], updateProperties)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Modifies the properties of a mail tab. Properties that are not specified in :value:`updateProperties` are not modified.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``tabId``]
      :type: (integer, optional)

      Defaults to the active tab of the current window.

   .. api-member::
      :name: ``updateProperties``
      :type: (:ref:`mail^tabs.^mail^tab^properties`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`mail^tabs.^mail^tab`
      :annotation: -- [Added in TB 121]

      Details about the updated mail tab.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _mail^tabs.on^displayed^folder^changed:

onDisplayedFolderChanged
------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

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
      :type: (:ref:`tabs.^tab`)
      :annotation: -- [Added in TB 76]

   .. api-member::
      :name: ``displayedFolder``
      :type: (:ref:`folders.^mail^folder`)
      :annotation: -- [Added in TB 76]

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _mail^tabs.on^selected^messages^changed:

onSelectedMessagesChanged
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

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
      :type: (:ref:`tabs.^tab`)
      :annotation: -- [Added in TB 76]

   .. api-member::
      :name: ``selectedMessages``
      :type: (:ref:`messages.^message^list`)
      :annotation: -- [Added in TB 76]

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. rst-class:: api-main-section

Types
=====

.. _mail^tabs.^folder^mode:

FolderMode
----------

.. api-section-annotation-hack:: -- [Added in TB 127]

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

.. _mail^tabs.^mail^tab:

MailTab
-------

.. api-section-annotation-hack:: -- [Added in TB 89]

.. api-header::
   :label: object

   .. _mail^tabs.^mail^tab.active:

   .. api-member::
      :name: ``active``
      :type: (boolean)

   .. _mail^tabs.^mail^tab.layout:

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

   .. _mail^tabs.^mail^tab.tab^id:

   .. api-member::
      :name: ``tabId``
      :type: (integer)
      :annotation: -- [Added in TB 128]

   .. _mail^tabs.^mail^tab.window^id:

   .. api-member::
      :name: ``windowId``
      :type: (integer)

   .. _mail^tabs.^mail^tab.displayed^folder:

   .. api-member::
      :name: [``displayedFolder``]
      :type: (:ref:`folders.^mail^folder`, optional)

      The folder displayed in the mail tab. The :permission:`accountsRead` permission is required for this property to be included.

   .. _mail^tabs.^mail^tab.folder^mode:

   .. api-member::
      :name: [``folderMode``]
      :type: (:ref:`mail^tabs.^folder^mode`, optional)
      :annotation: -- [Added in TB 127]

      The folder mode of the currently displayed folder.

   .. _mail^tabs.^mail^tab.folder^modes^enabled:

   .. api-member::
      :name: [``folderModesEnabled``]
      :type: (array of :ref:`mail^tabs.^folder^mode`, optional)
      :annotation: -- [Added in TB 127]

      The enabled folder modes in the folder pane, and their sort order.

   .. _mail^tabs.^mail^tab.folder^pane^visible:

   .. api-member::
      :name: [``folderPaneVisible``]
      :type: (boolean, optional)

      Whether the folder pane is visible or not.

   .. _mail^tabs.^mail^tab.group^type:

   .. api-member::
      :name: [``groupType``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 128]

      Grouping type of the message list.

      Supported values:

      .. api-member::
         :name: :value:`ungrouped`

      .. api-member::
         :name: :value:`groupedByThread`

      .. api-member::
         :name: :value:`groupedBySortType`

   .. _mail^tabs.^mail^tab.message^pane^visible:

   .. api-member::
      :name: [``messagePaneVisible``]
      :type: (boolean, optional)

      Whether the message pane is visible or not.

   .. _mail^tabs.^mail^tab.sort^order:

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

   .. _mail^tabs.^mail^tab.sort^type:

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

.. _mail^tabs.^mail^tab^properties:

MailTabProperties
-----------------

.. api-section-annotation-hack:: -- [Added in TB 121]

.. api-header::
   :label: object

   .. _mail^tabs.^mail^tab^properties.displayed^folder^id:

   .. api-member::
      :name: [``displayedFolderId``]
      :type: (:ref:`folders.^mail^folder^id`, optional)
      :annotation: -- [Added in TB 127]

      Sets the folder displayed in the mail tab. Requires the :permission:`accountsRead` permission. The previous message selection in the given folder will be restored, if any.

   .. _mail^tabs.^mail^tab^properties.folder^mode:

   .. api-member::
      :name: [``folderMode``]
      :type: (:ref:`mail^tabs.^folder^mode`, optional)
      :annotation: -- [Added in TB 127]

      Sets the currently used folder mode, enabling it if required. If used without also specifying :value:`displayedFolder`, the currently selected folder is re-selected in the new folder mode, if possible.

   .. _mail^tabs.^mail^tab^properties.folder^modes^enabled:

   .. api-member::
      :name: [``folderModesEnabled``]
      :type: (array of :ref:`mail^tabs.^folder^mode`, optional)
      :annotation: -- [Added in TB 127]

      Set the enabled folder modes in the folder pane, and their sort order.

   .. _mail^tabs.^mail^tab^properties.folder^pane^visible:

   .. api-member::
      :name: [``folderPaneVisible``]
      :type: (boolean, optional)

      Shows or hides the folder pane.

   .. _mail^tabs.^mail^tab^properties.group^type:

   .. api-member::
      :name: [``groupType``]
      :type: (`string`, optional)
      :annotation: -- [Added in TB 128]

      Grouping type of the message list.

      Supported values:

      .. api-member::
         :name: :value:`ungrouped`

      .. api-member::
         :name: :value:`groupedByThread`

      .. api-member::
         :name: :value:`groupedBySortType`

   .. _mail^tabs.^mail^tab^properties.layout:

   .. api-member::
      :name: [``layout``]
      :type: (`string`, optional)

      Sets the arrangement of the folder pane, message list pane, and message display pane. Setting a layout will be applied to all mail tabs.

      Supported values:

      .. api-member::
         :name: :value:`standard`

      .. api-member::
         :name: :value:`wide`

      .. api-member::
         :name: :value:`vertical`

   .. _mail^tabs.^mail^tab^properties.message^pane^visible:

   .. api-member::
      :name: [``messagePaneVisible``]
      :type: (boolean, optional)

      Shows or hides the message display pane.

   .. _mail^tabs.^mail^tab^properties.sort^order:

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

   .. _mail^tabs.^mail^tab^properties.sort^type:

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

.. _mail^tabs.^quick^filter^text^detail:

QuickFilterTextDetail
---------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

.. api-header::
   :label: object

   .. _mail^tabs.^quick^filter^text^detail.text:

   .. api-member::
      :name: ``text``
      :type: (string)

      String to match against the :value:`recipients`, :value:`author`, :value:`subject`, or :value:`body`.

   .. _mail^tabs.^quick^filter^text^detail.author:

   .. api-member::
      :name: [``author``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 68]

      Shows messages where :value:`text` matches the author.

   .. _mail^tabs.^quick^filter^text^detail.body:

   .. api-member::
      :name: [``body``]
      :type: (boolean, optional)

      Shows messages where :value:`text` matches the message body.

   .. _mail^tabs.^quick^filter^text^detail.recipients:

   .. api-member::
      :name: [``recipients``]
      :type: (boolean, optional)

      Shows messages where :value:`text` matches the recipients.

   .. _mail^tabs.^quick^filter^text^detail.subject:

   .. api-member::
      :name: [``subject``]
      :type: (boolean, optional)

      Shows messages where :value:`text` matches the subject.
