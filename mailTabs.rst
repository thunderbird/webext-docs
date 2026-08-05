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

.. role:: small

The mailTabs API allows to interact with Thunderbird's main mail tab (a.k.a 3-pane tab).

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _mail^tabs.permission.accounts^read:

.. api-member::
   :name: :permission:`accountsRead`
   :refid: mail-tabs-permission-accounts-read
   :refname: accountsRead

   See your mail accounts, their identities and their folders.

.. _mail^tabs.permission.messages^read:

.. api-member::
   :name: :permission:`messagesRead`
   :refid: mail-tabs-permission-messages-read
   :refname: messagesRead

   Read your email messages.

.. rst-class:: api-main-section

Functions
=========

.. _mail^tabs.create:

create([createProperties])
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Creates a new mail tab. Standard tab properties can be adjusted via :ref:`tabs.update` after the mail tab has been created. A new mail window can be created via :ref:`windows.create`.

.. api-header::
   :label: Parameters

   .. _mail^tabs.create.create^properties:

   .. api-member::
      :name: [``createProperties``]
      :refid: mail-tabs-create-create-properties
      :refname: createProperties
      :type: (:ref:`mail^tabs.^mail^tab^properties`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _mail^tabs.create.returns:

   .. api-member::
      :refid: mail-tabs-create-returns
      :refname: _returns
      :type: :ref:`mail^tabs.^mail^tab`

      Details about the created mail tab. Will contain the ID of the new tab.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mail^tabs.get:

get(tabId)
----------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

Get the :ref:`mail^tabs.^mail^tab` properties of a mail tab.

.. api-header::
   :label: Parameters

   .. _mail^tabs.get.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: mail-tabs-get-tab-id
      :refname: tabId
      :type: (integer)

      ID of the requested mail tab. Throws if the requested :value:`tabId` does not belong to a mail tab.

.. api-header::
   :label: Return type (`Promise`_)

   .. _mail^tabs.get.returns:

   .. api-member::
      :refid: mail-tabs-get-returns
      :refname: _returns
      :type: :ref:`mail^tabs.^mail^tab`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mail^tabs.get^listed^messages:

getListedMessages([tabId], [options])
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Lists the messages in the current view, honoring sort order and filters as used in the UI. Sort order of the returned messages can be overridden via the :value:`options` parameter

.. api-header::
   :label: Parameters

   .. _mail^tabs.get^listed^messages.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: mail-tabs-get-listed-messages-tab-id
      :refname: tabId
      :type: (integer, optional)

      Defaults to the active tab of the current window.

   .. _mail^tabs.get^listed^messages.options:

   .. api-member::
      :name: [``options``]
      :refid: mail-tabs-get-listed-messages-options
      :refname: options
      :type: (object, optional)

      .. _mail^tabs.get^listed^messages.options.sort^order:

      .. api-member::
         :name: [``sortOrder``]
         :refid: mail-tabs-get-listed-messages-options-sort-order
         :refname: sortOrder
         :type: (`string`, optional)
         :annotation: -- [Added in TB 153.0]

         The sort order for the returned messages. Ignored if :value:`sortType` is not specified.

         Supported values:

         .. _mail^tabs.get^listed^messages.options.sort^order.ascending:

         .. api-member::
            :name: :value:`ascending`
            :refid: mail-tabs-get-listed-messages-options-sort-order-ascending
            :refname: ascending

         .. _mail^tabs.get^listed^messages.options.sort^order.descending:

         .. api-member::
            :name: :value:`descending`
            :refid: mail-tabs-get-listed-messages-options-sort-order-descending
            :refname: descending

      .. _mail^tabs.get^listed^messages.options.sort^type:

      .. api-member::
         :name: [``sortType``]
         :refid: mail-tabs-get-listed-messages-options-sort-type
         :refname: sortType
         :type: (`string`, optional)
         :annotation: -- [Added in TB 153.0]

         Specifies how the returned messages should be sorted. This does not change the actual sort of the displayed messages. Default sort order is :value:`descending`, if not specified otherwise. Returning sorted messages is faster than manually sorting the messages afterwards, but slower than returning the messages in their original order.

         Supported values:

         .. _mail^tabs.get^listed^messages.options.sort^type.author:

         .. api-member::
            :name: :value:`author`
            :refid: mail-tabs-get-listed-messages-options-sort-type-author
            :refname: author

         .. _mail^tabs.get^listed^messages.options.sort^type.date:

         .. api-member::
            :name: :value:`date`
            :refid: mail-tabs-get-listed-messages-options-sort-type-date
            :refname: date

         .. _mail^tabs.get^listed^messages.options.sort^type.flagged:

         .. api-member::
            :name: :value:`flagged`
            :refid: mail-tabs-get-listed-messages-options-sort-type-flagged
            :refname: flagged

         .. _mail^tabs.get^listed^messages.options.sort^type.junk:

         .. api-member::
            :name: :value:`junk`
            :refid: mail-tabs-get-listed-messages-options-sort-type-junk
            :refname: junk

         .. _mail^tabs.get^listed^messages.options.sort^type.junk^score:

         .. api-member::
            :name: :value:`junkScore`
            :refid: mail-tabs-get-listed-messages-options-sort-type-junk-score
            :refname: junkScore

         .. _mail^tabs.get^listed^messages.options.sort^type.priority:

         .. api-member::
            :name: :value:`priority`
            :refid: mail-tabs-get-listed-messages-options-sort-type-priority
            :refname: priority

         .. _mail^tabs.get^listed^messages.options.sort^type.read:

         .. api-member::
            :name: :value:`read`
            :refid: mail-tabs-get-listed-messages-options-sort-type-read
            :refname: read

         .. _mail^tabs.get^listed^messages.options.sort^type.recipients:

         .. api-member::
            :name: :value:`recipients`
            :refid: mail-tabs-get-listed-messages-options-sort-type-recipients
            :refname: recipients

         .. _mail^tabs.get^listed^messages.options.sort^type.size:

         .. api-member::
            :name: :value:`size`
            :refid: mail-tabs-get-listed-messages-options-sort-type-size
            :refname: size

         .. _mail^tabs.get^listed^messages.options.sort^type.subject:

         .. api-member::
            :name: :value:`subject`
            :refid: mail-tabs-get-listed-messages-options-sort-type-subject
            :refname: subject

         .. _mail^tabs.get^listed^messages.options.sort^type.tags:

         .. api-member::
            :name: :value:`tags`
            :refid: mail-tabs-get-listed-messages-options-sort-type-tags
            :refname: tags

.. api-header::
   :label: Return type (`Promise`_)

   .. _mail^tabs.get^listed^messages.returns:

   .. api-member::
      :refid: mail-tabs-get-listed-messages-returns
      :refname: _returns
      :type: :ref:`messages.^message^list`
      :annotation: -- [Added in TB 153.0]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _mail^tabs.get^selected^folders:

getSelectedFolders([tabId])
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

Lists the selected folders in the folder pane. Does not include folders which are context-clicked, but not selected. The context-clicked folders are always returned by the :ref:`menus.on^clicked` event of the menus API.

.. api-header::
   :label: Parameters

   .. _mail^tabs.get^selected^folders.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: mail-tabs-get-selected-folders-tab-id
      :refname: tabId
      :type: (integer, optional)

      Defaults to the active tab of the current window.

.. api-header::
   :label: Return type (`Promise`_)

   .. _mail^tabs.get^selected^folders.returns:

   .. api-member::
      :refid: mail-tabs-get-selected-folders-returns
      :refname: _returns
      :type: array of :ref:`folders.^mail^folder`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _mail^tabs.get^selected^messages:

getSelectedMessages([tabId])
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Lists the selected messages in the current folder. Includes messages in collapsed threads. Does not include messages which are context-clicked, but not selected. The context-clicked messages are always returned by the :ref:`menus.on^clicked` event of the menus API.

.. api-header::
   :label: Parameters

   .. _mail^tabs.get^selected^messages.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: mail-tabs-get-selected-messages-tab-id
      :refname: tabId
      :type: (integer, optional)

      Defaults to the active tab of the current window.

.. api-header::
   :label: Return type (`Promise`_)

   .. _mail^tabs.get^selected^messages.returns:

   .. api-member::
      :refid: mail-tabs-get-selected-messages-returns
      :refname: _returns
      :type: :ref:`messages.^message^list`
      :annotation: -- [Added in TB 91.0]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. _mail^tabs.query:

query([queryInfo])
------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Gets all mail tabs that have the specified properties, or all mail tabs if no properties are specified.

.. api-header::
   :label: Parameters

   .. _mail^tabs.query.query^info:

   .. api-member::
      :name: [``queryInfo``]
      :refid: mail-tabs-query-query-info
      :refname: queryInfo
      :type: (object, optional)

      .. _mail^tabs.query.query^info.active:

      .. api-member::
         :name: [``active``]
         :refid: mail-tabs-query-query-info-active
         :refname: active
         :type: (boolean, optional)

         Whether the tabs are active in their windows.

      .. _mail^tabs.query.query^info.current^window:

      .. api-member::
         :name: [``currentWindow``]
         :refid: mail-tabs-query-query-info-current-window
         :refname: currentWindow
         :type: (boolean, optional)

         Whether the tabs are in the current window.

      .. _mail^tabs.query.query^info.last^focused^window:

      .. api-member::
         :name: [``lastFocusedWindow``]
         :refid: mail-tabs-query-query-info-last-focused-window
         :refname: lastFocusedWindow
         :type: (boolean, optional)

         Whether the tabs are in the last focused window.

      .. _mail^tabs.query.query^info.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: mail-tabs-query-query-info-window-id
         :refname: windowId
         :type: (integer, optional)

         The ID of the parent window, or :ref:`windows.^w^i^n^d^o^w_^i^d_^c^u^r^r^e^n^t` for the current window.

.. api-header::
   :label: Return type (`Promise`_)

   .. _mail^tabs.query.returns:

   .. api-member::
      :refid: mail-tabs-query-returns
      :refname: _returns
      :type: array of :ref:`mail^tabs.^mail^tab`
      :annotation: -- [Added in TB 91.0]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _mail^tabs.set^quick^filter:

setQuickFilter([tabId], properties)
-----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Sets the Quick Filter user interface based on the options specified.

.. api-header::
   :label: Parameters

   .. _mail^tabs.set^quick^filter.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: mail-tabs-set-quick-filter-tab-id
      :refname: tabId
      :type: (integer, optional)

      Defaults to the active tab of the current window.

   .. _mail^tabs.set^quick^filter.properties:

   .. api-member::
      :name: ``properties``
      :refid: mail-tabs-set-quick-filter-properties
      :refname: properties
      :type: (object)

      .. _mail^tabs.set^quick^filter.properties.attachment:

      .. api-member::
         :name: [``attachment``]
         :refid: mail-tabs-set-quick-filter-properties-attachment
         :refname: attachment
         :type: (boolean, optional)

         Shows only messages with attachments.

      .. _mail^tabs.set^quick^filter.properties.contact:

      .. api-member::
         :name: [``contact``]
         :refid: mail-tabs-set-quick-filter-properties-contact
         :refname: contact
         :type: (boolean, optional)

         Shows only messages from people in the address book.

      .. _mail^tabs.set^quick^filter.properties.flagged:

      .. api-member::
         :name: [``flagged``]
         :refid: mail-tabs-set-quick-filter-properties-flagged
         :refname: flagged
         :type: (boolean, optional)

         Shows only flagged messages.

      .. _mail^tabs.set^quick^filter.properties.show:

      .. api-member::
         :name: [``show``]
         :refid: mail-tabs-set-quick-filter-properties-show
         :refname: show
         :type: (boolean, optional)

         Shows or hides the Quick Filter bar.

      .. _mail^tabs.set^quick^filter.properties.tags:

      .. api-member::
         :name: [``tags``]
         :refid: mail-tabs-set-quick-filter-properties-tags
         :refname: tags
         :type: (boolean or :ref:`messages.tags.^tags^detail`, optional)

         Shows only messages with tags on them.

      .. _mail^tabs.set^quick^filter.properties.text:

      .. api-member::
         :name: [``text``]
         :refid: mail-tabs-set-quick-filter-properties-text
         :refname: text
         :type: (:ref:`mail^tabs.^quick^filter^text^detail`, optional)

         Shows only messages matching the supplied text.

      .. _mail^tabs.set^quick^filter.properties.unread:

      .. api-member::
         :name: [``unread``]
         :refid: mail-tabs-set-quick-filter-properties-unread
         :refname: unread
         :type: (boolean, optional)

         Shows only unread messages.

.. _mail^tabs.set^selected^messages:

setSelectedMessages([tabId], messageIds)
----------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 102.3.3]

Selects none, one or multiple messages. Opens collapsed threads to show the selection, if required.

.. api-header::
   :label: Parameters

   .. _mail^tabs.set^selected^messages.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: mail-tabs-set-selected-messages-tab-id
      :refname: tabId
      :type: (integer, optional)

      Defaults to the active tab of the current window.

   .. _mail^tabs.set^selected^messages.message^ids:

   .. api-member::
      :name: ``messageIds``
      :refid: mail-tabs-set-selected-messages-message-ids
      :refname: messageIds
      :type: (array of :ref:`messages.^message^id`)

      The IDs of the messages, which should be selected. The mail tab will switch to the folder of the selected messages. Throws if they belong to different folders. Array can be empty to deselect any currently selected message.

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`messagesRead`

.. _mail^tabs.update:

update([tabId], updateProperties)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Modifies the properties of a mail tab. Properties that are not specified in :value:`updateProperties` are not modified.

.. api-header::
   :label: Parameters

   .. _mail^tabs.update.tab^id:

   .. api-member::
      :name: [``tabId``]
      :refid: mail-tabs-update-tab-id
      :refname: tabId
      :type: (integer, optional)

      Defaults to the active tab of the current window.

   .. _mail^tabs.update.update^properties:

   .. api-member::
      :name: ``updateProperties``
      :refid: mail-tabs-update-update-properties
      :refname: updateProperties
      :type: (:ref:`mail^tabs.^mail^tab^properties`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _mail^tabs.update.returns:

   .. api-member::
      :refid: mail-tabs-update-returns
      :refname: _returns
      :type: :ref:`mail^tabs.^mail^tab`
      :annotation: -- [Added in TB 128.0]

      Details about the updated mail tab.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _mail^tabs.on^displayed^folder^changed:

onDisplayedFolderChanged
------------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Fired when the displayed folder changes in any mail tab.

.. api-header::
   :label: Parameters for onDisplayedFolderChanged.addListener(listener)

   .. _mail^tabs.on^displayed^folder^changed.listener(tab, displayed^folder):

   .. api-member::
      :name: ``listener(tab, displayedFolder)``
      :refid: mail-tabs-on-displayed-folder-changed-listener-tab-displayed-folder
      :refname: listener(tab, displayedFolder)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _mail^tabs.on^displayed^folder^changed.tab:

   .. api-member::
      :name: ``tab``
      :refid: mail-tabs-on-displayed-folder-changed-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)
      :annotation: -- [Added in TB 78.0]

   .. _mail^tabs.on^displayed^folder^changed.displayed^folder:

   .. api-member::
      :name: ``displayedFolder``
      :refid: mail-tabs-on-displayed-folder-changed-displayed-folder
      :refname: displayedFolder
      :type: (:ref:`folders.^mail^folder`)
      :annotation: -- [Added in TB 78.0]

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _mail^tabs.on^selected^messages^changed:

onSelectedMessagesChanged
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

Fired when the selected messages change in any mail tab.

.. api-header::
   :label: Parameters for onSelectedMessagesChanged.addListener(listener)

   .. _mail^tabs.on^selected^messages^changed.listener(tab, selected^messages):

   .. api-member::
      :name: ``listener(tab, selectedMessages)``
      :refid: mail-tabs-on-selected-messages-changed-listener-tab-selected-messages
      :refname: listener(tab, selectedMessages)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _mail^tabs.on^selected^messages^changed.tab:

   .. api-member::
      :name: ``tab``
      :refid: mail-tabs-on-selected-messages-changed-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)
      :annotation: -- [Added in TB 78.0]

   .. _mail^tabs.on^selected^messages^changed.selected^messages:

   .. api-member::
      :name: ``selectedMessages``
      :refid: mail-tabs-on-selected-messages-changed-selected-messages
      :refname: selectedMessages
      :type: (:ref:`messages.^message^list`)
      :annotation: -- [Added in TB 78.0]

.. api-header::
   :label: Required permissions

   - :permission:`messagesRead`

.. rst-class:: api-main-section

Types
=====

.. _mail^tabs.^folder^mode:

FolderMode
----------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

A supported folder mode in the folder pane.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _mail^tabs.^folder^mode.all:

         .. api-member::
            :name: :value:`all`
            :refid: mail-tabs-folder-mode-all
            :refname: all

            Show all folders.

         .. _mail^tabs.^folder^mode.favorite:

         .. api-member::
            :name: :value:`favorite`
            :refid: mail-tabs-folder-mode-favorite
            :refname: favorite

            Show only favorite folders.

         .. _mail^tabs.^folder^mode.recent:

         .. api-member::
            :name: :value:`recent`
            :refid: mail-tabs-folder-mode-recent
            :refname: recent

            Show recently used folders.

         .. _mail^tabs.^folder^mode.tags:

         .. api-member::
            :name: :value:`tags`
            :refid: mail-tabs-folder-mode-tags
            :refname: tags

            Show virtual tag folders.

         .. _mail^tabs.^folder^mode.unified:

         .. api-member::
            :name: :value:`unified`
            :refid: mail-tabs-folder-mode-unified
            :refname: unified

            Show the unified folder view.

         .. _mail^tabs.^folder^mode.unread:

         .. api-member::
            :name: :value:`unread`
            :refid: mail-tabs-folder-mode-unread
            :refname: unread

            Show only folders with unread messages.

.. _mail^tabs.^mail^tab:

MailTab
-------

.. api-section-annotation-hack:: -- [Added in TB 91.0]

.. api-header::
   :label: object

   .. _mail^tabs.^mail^tab.active:

   .. api-member::
      :name: ``active``
      :refid: mail-tabs-mail-tab-active
      :refname: active
      :type: (boolean)

   .. _mail^tabs.^mail^tab.layout:

   .. api-member::
      :name: ``layout``
      :refid: mail-tabs-mail-tab-layout
      :refname: layout
      :type: (`string`)

      The arrangement of the folder pane, message list pane, and message display pane.

      Supported values:

      .. _mail^tabs.^mail^tab.layout.standard:

      .. api-member::
         :name: :value:`standard`
         :refid: mail-tabs-mail-tab-layout-standard
         :refname: standard

         The standard layout with the folder pane on the left, and the message list and message display stacked on the right.

      .. _mail^tabs.^mail^tab.layout.vertical:

      .. api-member::
         :name: :value:`vertical`
         :refid: mail-tabs-mail-tab-layout-vertical
         :refname: vertical

         The vertical layout with the folder pane, message list, and message display side by side in three columns.

      .. _mail^tabs.^mail^tab.layout.wide:

      .. api-member::
         :name: :value:`wide`
         :refid: mail-tabs-mail-tab-layout-wide
         :refname: wide

         The wide layout with the folder pane and message list side by side on top, and the message display on the bottom.

   .. _mail^tabs.^mail^tab.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: mail-tabs-mail-tab-tab-id
      :refname: tabId
      :type: (integer)
      :annotation: -- [Added in TB 128.0]

   .. _mail^tabs.^mail^tab.window^id:

   .. api-member::
      :name: ``windowId``
      :refid: mail-tabs-mail-tab-window-id
      :refname: windowId
      :type: (integer)

   .. _mail^tabs.^mail^tab.displayed^folder:

   .. api-member::
      :name: [``displayedFolder``]
      :refid: mail-tabs-mail-tab-displayed-folder
      :refname: displayedFolder
      :type: (:ref:`folders.^mail^folder`, optional)

      The folder displayed in the mail tab. The :permission:`accountsRead` permission is required for this property to be included.

   .. _mail^tabs.^mail^tab.folder^mode:

   .. api-member::
      :name: [``folderMode``]
      :refid: mail-tabs-mail-tab-folder-mode
      :refname: folderMode
      :type: (:ref:`mail^tabs.^folder^mode`, optional)
      :annotation: -- [Added in TB 128.0]

      The folder mode of the currently displayed folder.

   .. _mail^tabs.^mail^tab.folder^modes^enabled:

   .. api-member::
      :name: [``folderModesEnabled``]
      :refid: mail-tabs-mail-tab-folder-modes-enabled
      :refname: folderModesEnabled
      :type: (array of :ref:`mail^tabs.^folder^mode`, optional)
      :annotation: -- [Added in TB 128.0]

      The enabled folder modes in the folder pane, and their sort order.

   .. _mail^tabs.^mail^tab.folder^pane^visible:

   .. api-member::
      :name: [``folderPaneVisible``]
      :refid: mail-tabs-mail-tab-folder-pane-visible
      :refname: folderPaneVisible
      :type: (boolean, optional)

      Whether the folder pane is visible or not.

   .. _mail^tabs.^mail^tab.group^type:

   .. api-member::
      :name: [``groupType``]
      :refid: mail-tabs-mail-tab-group-type
      :refname: groupType
      :type: (`string`, optional)
      :annotation: -- [Added in TB 128.0]

      Grouping type of the message list.

      Supported values:

      .. _mail^tabs.^mail^tab.group^type.grouped^by^sort^type:

      .. api-member::
         :name: :value:`groupedBySortType`
         :refid: mail-tabs-mail-tab-group-type-grouped-by-sort-type
         :refname: groupedBySortType

         Messages are grouped by the current sort type.

      .. _mail^tabs.^mail^tab.group^type.grouped^by^thread:

      .. api-member::
         :name: :value:`groupedByThread`
         :refid: mail-tabs-mail-tab-group-type-grouped-by-thread
         :refname: groupedByThread

         Messages are grouped by threads.

      .. _mail^tabs.^mail^tab.group^type.ungrouped:

      .. api-member::
         :name: :value:`ungrouped`
         :refid: mail-tabs-mail-tab-group-type-ungrouped
         :refname: ungrouped

         Messages are not grouped.

   .. _mail^tabs.^mail^tab.message^pane^visible:

   .. api-member::
      :name: [``messagePaneVisible``]
      :refid: mail-tabs-mail-tab-message-pane-visible
      :refname: messagePaneVisible
      :type: (boolean, optional)

      Whether the message pane is visible or not.

   .. _mail^tabs.^mail^tab.sort^order:

   .. api-member::
      :name: [``sortOrder``]
      :refid: mail-tabs-mail-tab-sort-order
      :refname: sortOrder
      :type: (`string`, optional)

      The sort order of the message list.

      Supported values:

      .. _mail^tabs.^mail^tab.sort^order.ascending:

      .. api-member::
         :name: :value:`ascending`
         :refid: mail-tabs-mail-tab-sort-order-ascending
         :refname: ascending

         Ascending sort order.

      .. _mail^tabs.^mail^tab.sort^order.descending:

      .. api-member::
         :name: :value:`descending`
         :refid: mail-tabs-mail-tab-sort-order-descending
         :refname: descending

         Descending sort order.

      .. _mail^tabs.^mail^tab.sort^order.none:

      .. api-member::
         :name: :value:`none`
         :refid: mail-tabs-mail-tab-sort-order-none
         :refname: none

         No sort order.

   .. _mail^tabs.^mail^tab.sort^type:

   .. api-member::
      :name: [``sortType``]
      :refid: mail-tabs-mail-tab-sort-type
      :refname: sortType
      :type: (`string`, optional)

      The primary sort column of the message list.

      Supported values:

      .. _mail^tabs.^mail^tab.sort^type.account:

      .. api-member::
         :name: :value:`account`
         :refid: mail-tabs-mail-tab-sort-type-account
         :refname: account

         Sort by account, grouping messages belonging to the same account.

      .. _mail^tabs.^mail^tab.sort^type.attachments:

      .. api-member::
         :name: :value:`attachments`
         :refid: mail-tabs-mail-tab-sort-type-attachments
         :refname: attachments

         Sort by attachment status.

      .. _mail^tabs.^mail^tab.sort^type.author:

      .. api-member::
         :name: :value:`author`
         :refid: mail-tabs-mail-tab-sort-type-author
         :refname: author

         Sort by author.

      .. _mail^tabs.^mail^tab.sort^type.correspondent:

      .. api-member::
         :name: :value:`correspondent`
         :refid: mail-tabs-mail-tab-sort-type-correspondent
         :refname: correspondent

         Sort by correspondents.

      .. _mail^tabs.^mail^tab.sort^type.custom:

      .. api-member::
         :name: :value:`custom`
         :refid: mail-tabs-mail-tab-sort-type-custom
         :refname: custom

         Sort by a custom column.

      .. _mail^tabs.^mail^tab.sort^type.date:

      .. api-member::
         :name: :value:`date`
         :refid: mail-tabs-mail-tab-sort-type-date
         :refname: date

         Sort by date.

      .. _mail^tabs.^mail^tab.sort^type.flagged:

      .. api-member::
         :name: :value:`flagged`
         :refid: mail-tabs-mail-tab-sort-type-flagged
         :refname: flagged

         Sort by starred status.

      .. _mail^tabs.^mail^tab.sort^type.id:

      .. api-member::
         :name: :value:`id`
         :refid: mail-tabs-mail-tab-sort-type-id
         :refname: id

         Sort by the Message-ID header, a unique identifier assigned by the sending server.

      .. _mail^tabs.^mail^tab.sort^type.junk^status:

      .. api-member::
         :name: :value:`junkStatus`
         :refid: mail-tabs-mail-tab-sort-type-junk-status
         :refname: junkStatus

         Sort by spam status.

      .. _mail^tabs.^mail^tab.sort^type.location:

      .. api-member::
         :name: :value:`location`
         :refid: mail-tabs-mail-tab-sort-type-location
         :refname: location

         Sort by folder location.

      .. _mail^tabs.^mail^tab.sort^type.none:

      .. api-member::
         :name: :value:`none`
         :refid: mail-tabs-mail-tab-sort-type-none
         :refname: none

         Not sorted.

      .. _mail^tabs.^mail^tab.sort^type.priority:

      .. api-member::
         :name: :value:`priority`
         :refid: mail-tabs-mail-tab-sort-type-priority
         :refname: priority

         Sort by priority.

      .. _mail^tabs.^mail^tab.sort^type.received:

      .. api-member::
         :name: :value:`received`
         :refid: mail-tabs-mail-tab-sort-type-received
         :refname: received

         Sort by received date.

      .. _mail^tabs.^mail^tab.sort^type.recipient:

      .. api-member::
         :name: :value:`recipient`
         :refid: mail-tabs-mail-tab-sort-type-recipient
         :refname: recipient

         Sort by recipient.

      .. _mail^tabs.^mail^tab.sort^type.size:

      .. api-member::
         :name: :value:`size`
         :refid: mail-tabs-mail-tab-sort-type-size
         :refname: size

         Sort by message size.

      .. _mail^tabs.^mail^tab.sort^type.status:

      .. api-member::
         :name: :value:`status`
         :refid: mail-tabs-mail-tab-sort-type-status
         :refname: status

         Sort by message status.

      .. _mail^tabs.^mail^tab.sort^type.subject:

      .. api-member::
         :name: :value:`subject`
         :refid: mail-tabs-mail-tab-sort-type-subject
         :refname: subject

         Sort by subject.

      .. _mail^tabs.^mail^tab.sort^type.tags:

      .. api-member::
         :name: :value:`tags`
         :refid: mail-tabs-mail-tab-sort-type-tags
         :refname: tags

         Sort by tags.

      .. _mail^tabs.^mail^tab.sort^type.thread:

      .. api-member::
         :name: :value:`thread`
         :refid: mail-tabs-mail-tab-sort-type-thread
         :refname: thread

         Sort by thread, grouping messages that belong to the same conversation.

      .. _mail^tabs.^mail^tab.sort^type.unread:

      .. api-member::
         :name: :value:`unread`
         :refid: mail-tabs-mail-tab-sort-type-unread
         :refname: unread

         Sort by unread status.

.. _mail^tabs.^mail^tab^properties:

MailTabProperties
-----------------

.. api-section-annotation-hack:: -- [Added in TB 128.0]

.. api-header::
   :label: object

   .. _mail^tabs.^mail^tab^properties.displayed^folder^id:

   .. api-member::
      :name: [``displayedFolderId``]
      :refid: mail-tabs-mail-tab-properties-displayed-folder-id
      :refname: displayedFolderId
      :type: (:ref:`folders.^mail^folder^id`, optional)

      Sets the folder displayed in the mail tab. Requires the :permission:`accountsRead` permission. The previous message selection in the given folder will be restored, if any.

   .. _mail^tabs.^mail^tab^properties.folder^mode:

   .. api-member::
      :name: [``folderMode``]
      :refid: mail-tabs-mail-tab-properties-folder-mode
      :refname: folderMode
      :type: (:ref:`mail^tabs.^folder^mode`, optional)

      Sets the currently used folder mode, enabling it if required. If used without also specifying :value:`displayedFolder`, the currently selected folder is re-selected in the new folder mode, if possible.

   .. _mail^tabs.^mail^tab^properties.folder^modes^enabled:

   .. api-member::
      :name: [``folderModesEnabled``]
      :refid: mail-tabs-mail-tab-properties-folder-modes-enabled
      :refname: folderModesEnabled
      :type: (array of :ref:`mail^tabs.^folder^mode`, optional)

      Set the enabled folder modes in the folder pane, and their sort order.

   .. _mail^tabs.^mail^tab^properties.folder^pane^visible:

   .. api-member::
      :name: [``folderPaneVisible``]
      :refid: mail-tabs-mail-tab-properties-folder-pane-visible
      :refname: folderPaneVisible
      :type: (boolean, optional)

      Shows or hides the folder pane.

   .. _mail^tabs.^mail^tab^properties.group^type:

   .. api-member::
      :name: [``groupType``]
      :refid: mail-tabs-mail-tab-properties-group-type
      :refname: groupType
      :type: (`string`, optional)

      Grouping type of the message list.

      Supported values:

      .. _mail^tabs.^mail^tab^properties.group^type.grouped^by^sort^type:

      .. api-member::
         :name: :value:`groupedBySortType`
         :refid: mail-tabs-mail-tab-properties-group-type-grouped-by-sort-type
         :refname: groupedBySortType

         Messages are grouped by the current sort type.

      .. _mail^tabs.^mail^tab^properties.group^type.grouped^by^thread:

      .. api-member::
         :name: :value:`groupedByThread`
         :refid: mail-tabs-mail-tab-properties-group-type-grouped-by-thread
         :refname: groupedByThread

         Messages are grouped by threads.

      .. _mail^tabs.^mail^tab^properties.group^type.ungrouped:

      .. api-member::
         :name: :value:`ungrouped`
         :refid: mail-tabs-mail-tab-properties-group-type-ungrouped
         :refname: ungrouped

         Messages are not grouped.

   .. _mail^tabs.^mail^tab^properties.layout:

   .. api-member::
      :name: [``layout``]
      :refid: mail-tabs-mail-tab-properties-layout
      :refname: layout
      :type: (`string`, optional)

      Sets the arrangement of the folder pane, message list pane, and message display pane. Setting a layout will be applied to all mail tabs.

      Supported values:

      .. _mail^tabs.^mail^tab^properties.layout.standard:

      .. api-member::
         :name: :value:`standard`
         :refid: mail-tabs-mail-tab-properties-layout-standard
         :refname: standard

         The standard layout with the folder pane on the left, and the message list and message display stacked on the right.

      .. _mail^tabs.^mail^tab^properties.layout.vertical:

      .. api-member::
         :name: :value:`vertical`
         :refid: mail-tabs-mail-tab-properties-layout-vertical
         :refname: vertical

         The vertical layout with the folder pane, message list, and message display side by side in three columns.

      .. _mail^tabs.^mail^tab^properties.layout.wide:

      .. api-member::
         :name: :value:`wide`
         :refid: mail-tabs-mail-tab-properties-layout-wide
         :refname: wide

         The wide layout with the folder pane and message list side by side on top, and the message display on the bottom.

   .. _mail^tabs.^mail^tab^properties.message^pane^visible:

   .. api-member::
      :name: [``messagePaneVisible``]
      :refid: mail-tabs-mail-tab-properties-message-pane-visible
      :refname: messagePaneVisible
      :type: (boolean, optional)

      Shows or hides the message display pane.

   .. _mail^tabs.^mail^tab^properties.sort^order:

   .. api-member::
      :name: [``sortOrder``]
      :refid: mail-tabs-mail-tab-properties-sort-order
      :refname: sortOrder
      :type: (`string`, optional)

      Sorts the list of messages. :value:`sortType` must also be given.

      Supported values:

      .. _mail^tabs.^mail^tab^properties.sort^order.ascending:

      .. api-member::
         :name: :value:`ascending`
         :refid: mail-tabs-mail-tab-properties-sort-order-ascending
         :refname: ascending

         Ascending sort order.

      .. _mail^tabs.^mail^tab^properties.sort^order.descending:

      .. api-member::
         :name: :value:`descending`
         :refid: mail-tabs-mail-tab-properties-sort-order-descending
         :refname: descending

         Descending sort order.

      .. _mail^tabs.^mail^tab^properties.sort^order.none:

      .. api-member::
         :name: :value:`none`
         :refid: mail-tabs-mail-tab-properties-sort-order-none
         :refname: none

         No sort order.

   .. _mail^tabs.^mail^tab^properties.sort^type:

   .. api-member::
      :name: [``sortType``]
      :refid: mail-tabs-mail-tab-properties-sort-type
      :refname: sortType
      :type: (`string`, optional)

      Sorts the list of messages. :value:`sortOrder` must also be given.

      Supported values:

      .. _mail^tabs.^mail^tab^properties.sort^type.account:

      .. api-member::
         :name: :value:`account`
         :refid: mail-tabs-mail-tab-properties-sort-type-account
         :refname: account

         Sort by account, grouping messages belonging to the same account.

      .. _mail^tabs.^mail^tab^properties.sort^type.attachments:

      .. api-member::
         :name: :value:`attachments`
         :refid: mail-tabs-mail-tab-properties-sort-type-attachments
         :refname: attachments

         Sort by attachment status.

      .. _mail^tabs.^mail^tab^properties.sort^type.author:

      .. api-member::
         :name: :value:`author`
         :refid: mail-tabs-mail-tab-properties-sort-type-author
         :refname: author

         Sort by author.

      .. _mail^tabs.^mail^tab^properties.sort^type.correspondent:

      .. api-member::
         :name: :value:`correspondent`
         :refid: mail-tabs-mail-tab-properties-sort-type-correspondent
         :refname: correspondent

         Sort by correspondents.

      .. _mail^tabs.^mail^tab^properties.sort^type.custom:

      .. api-member::
         :name: :value:`custom`
         :refid: mail-tabs-mail-tab-properties-sort-type-custom
         :refname: custom

         Sort by a custom column.

      .. _mail^tabs.^mail^tab^properties.sort^type.date:

      .. api-member::
         :name: :value:`date`
         :refid: mail-tabs-mail-tab-properties-sort-type-date
         :refname: date

         Sort by date.

      .. _mail^tabs.^mail^tab^properties.sort^type.flagged:

      .. api-member::
         :name: :value:`flagged`
         :refid: mail-tabs-mail-tab-properties-sort-type-flagged
         :refname: flagged

         Sort by starred status.

      .. _mail^tabs.^mail^tab^properties.sort^type.id:

      .. api-member::
         :name: :value:`id`
         :refid: mail-tabs-mail-tab-properties-sort-type-id
         :refname: id

         Sort by the Message-ID header, a unique identifier assigned by the sending server.

      .. _mail^tabs.^mail^tab^properties.sort^type.junk^status:

      .. api-member::
         :name: :value:`junkStatus`
         :refid: mail-tabs-mail-tab-properties-sort-type-junk-status
         :refname: junkStatus

         Sort by spam status.

      .. _mail^tabs.^mail^tab^properties.sort^type.location:

      .. api-member::
         :name: :value:`location`
         :refid: mail-tabs-mail-tab-properties-sort-type-location
         :refname: location

         Sort by folder location.

      .. _mail^tabs.^mail^tab^properties.sort^type.none:

      .. api-member::
         :name: :value:`none`
         :refid: mail-tabs-mail-tab-properties-sort-type-none
         :refname: none

         Not sorted.

      .. _mail^tabs.^mail^tab^properties.sort^type.priority:

      .. api-member::
         :name: :value:`priority`
         :refid: mail-tabs-mail-tab-properties-sort-type-priority
         :refname: priority

         Sort by priority.

      .. _mail^tabs.^mail^tab^properties.sort^type.received:

      .. api-member::
         :name: :value:`received`
         :refid: mail-tabs-mail-tab-properties-sort-type-received
         :refname: received

         Sort by received date.

      .. _mail^tabs.^mail^tab^properties.sort^type.recipient:

      .. api-member::
         :name: :value:`recipient`
         :refid: mail-tabs-mail-tab-properties-sort-type-recipient
         :refname: recipient

         Sort by recipient.

      .. _mail^tabs.^mail^tab^properties.sort^type.size:

      .. api-member::
         :name: :value:`size`
         :refid: mail-tabs-mail-tab-properties-sort-type-size
         :refname: size

         Sort by message size.

      .. _mail^tabs.^mail^tab^properties.sort^type.status:

      .. api-member::
         :name: :value:`status`
         :refid: mail-tabs-mail-tab-properties-sort-type-status
         :refname: status

         Sort by message status.

      .. _mail^tabs.^mail^tab^properties.sort^type.subject:

      .. api-member::
         :name: :value:`subject`
         :refid: mail-tabs-mail-tab-properties-sort-type-subject
         :refname: subject

         Sort by subject.

      .. _mail^tabs.^mail^tab^properties.sort^type.tags:

      .. api-member::
         :name: :value:`tags`
         :refid: mail-tabs-mail-tab-properties-sort-type-tags
         :refname: tags

         Sort by tags.

      .. _mail^tabs.^mail^tab^properties.sort^type.thread:

      .. api-member::
         :name: :value:`thread`
         :refid: mail-tabs-mail-tab-properties-sort-type-thread
         :refname: thread

         Sort by thread, grouping messages that belong to the same conversation.

      .. _mail^tabs.^mail^tab^properties.sort^type.unread:

      .. api-member::
         :name: :value:`unread`
         :refid: mail-tabs-mail-tab-properties-sort-type-unread
         :refname: unread

         Sort by unread status.

.. _mail^tabs.^quick^filter^text^detail:

QuickFilterTextDetail
---------------------

.. api-section-annotation-hack:: -- [Added in TB 68.0]

.. api-header::
   :label: object

   .. _mail^tabs.^quick^filter^text^detail.text:

   .. api-member::
      :name: ``text``
      :refid: mail-tabs-quick-filter-text-detail-text
      :refname: text
      :type: (string)

      String to match against the :value:`recipients`, :value:`author`, :value:`subject`, or :value:`body`.

   .. _mail^tabs.^quick^filter^text^detail.author:

   .. api-member::
      :name: [``author``]
      :refid: mail-tabs-quick-filter-text-detail-author
      :refname: author
      :type: (boolean, optional)

      Shows messages where :value:`text` matches the author.

   .. _mail^tabs.^quick^filter^text^detail.body:

   .. api-member::
      :name: [``body``]
      :refid: mail-tabs-quick-filter-text-detail-body
      :refname: body
      :type: (boolean, optional)

      Shows messages where :value:`text` matches the message body.

   .. _mail^tabs.^quick^filter^text^detail.recipients:

   .. api-member::
      :name: [``recipients``]
      :refid: mail-tabs-quick-filter-text-detail-recipients
      :refname: recipients
      :type: (boolean, optional)

      Shows messages where :value:`text` matches the recipients.

   .. _mail^tabs.^quick^filter^text^detail.subject:

   .. api-member::
      :name: [``subject``]
      :refid: mail-tabs-quick-filter-text-detail-subject
      :refname: subject
      :type: (boolean, optional)

      Shows messages where :value:`text` matches the subject.
