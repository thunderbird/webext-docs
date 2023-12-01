================================
Changes up to Thunderbird 91 ESR
================================

-------------------
Thunderbird 81 Beta
-------------------

messageDisplay API
==================

* The :ref:`messageDisplay.getDisplayedMessages` function has been added to allow access to details of multiple-selection of email. Previously only a single selection function was available.

* The :ref:`messageDisplay.onMessagesDisplayed` event has been added.

See the documentation on those functions and events for more information.

.. _thunderbird_82_0b1:

-------------------
Thunderbird 82 Beta
-------------------

compose API
===========

* Attachments can now be specified in the :ref:`beginNew <compose.beginNew>`,
  :ref:`beginReply <compose.beginReply>`, and :ref:`beginForward <compose.beginForward>` functions.

tabs API
========

* The :ref:`connect <tabs.connect>` and :ref:`sendMessage <tabs.sendMessage>` functions now work as
  they do in Firefox.

messageDisplayScripts API
=========================

* Content script functions can now operate on a message display "tab" in the same way they do on a
  content tab in Thunderbird or Firefox. This requires the new :permission:`messagesModify` permission.

  Here are some basic examples. See `the MDN documentation`__ for a more in-depth explanation.

  .. code-block:: javascript

    // Where tabId is the id of a message display tab:

    browser.tabs.executeScript(tabId, {
      code: `document.body.textContent = "Hey look, the script ran!";`,
    });

    browser.tabs.executeScript(tabId, {
      file: "display.js",
    });

    browser.tabs.insertCSS(tabId, {
      code: "body { background-color: red; }",
    });

    browser.tabs.insertCSS(tabId, {
      file: "display.css",
    });

    browser.tabs.removeCSS(tabId, {
      code: "body { background-color: red; }",
    });

    browser.tabs.removeCSS(tabId, {
      file: "display.css",
    });

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts

* Scripts can also be registered to run automatically on messages being displayed, using the new
  :doc:`/messageDisplayScripts`.
  
  Again, this works just like the contentScripts API:

  .. code-block:: javascript

    let registeredScripts = await browser.messageDisplayScripts.register({
      css: [
        // Any number of code or file objects could be listed here.
        { code: "body { background-color: red; }" },
        { file: "display.css" },
      ],
      js: [
        // Any number of code or file objects could be listed here.
        { code: `document.body.textContent = "Hey look, the script ran!";` },
        { file: "display.js" },
      ],
    });

  Added code will run immediately and CSS will be immediately applied to already-open message
  display tabs or windows, and any new message display tabs or windows.

  The returned value, ``registeredScripts`` in this example, is an object with which you can
  unregister the code/CSS:

  .. code-block:: javascript

    await registeredScripts.unregister();

.. note::

  This functionality does *not* permanently alter messages, only what the user sees when they are
  displayed.

-------------------
Thunderbird 83 Beta
-------------------

compose API
===========

* :ref:`ComposeAttachment <compose.ComposeAttachment>` objects now have a ``size`` property with
  the size of the attachment in bytes.

contacts API
============

* The :ref:`onUpdated <contacts.onUpdated>` event now calls listeners with a second argument,
  containing details of the changes made. For example:

  .. code-block:: json

    {
      "FirstName": {
        "oldValue": "Daniel",
        "newValue": "Danielle"
      },
      "DisplayName": {
        "oldValue": "Daniel Smith",
        "newValue": "Danielle Smith"
      }
    }

menus API
=========

* A ``compose_attachment`` context can now be used. This context applies when the user opens a
  context menu on selected attachments in a compose window. The selected attachments can be
  accessed from the ``attachments`` property in an :ref:`onShown <menus.onShown>` or
  :ref:`onClicked <menus.onClicked>` listener.
  
* The standard properties available to :ref:`onShown <menus.onShown>` are now available for
  messages being displayed, if your extension has the :permission:`messagesRead` permission.

-------------------
Thunderbird 84 Beta
-------------------

compose API
===========

* The :ref:`beginNew <compose.beginNew>` function now has an optional ``messageId`` argument. If
  ``messageId`` is provided, the referenced message is opened to compose as a new message. This
  works for ordinary messages and templates.
  
* Using :ref:`beginForward <compose.beginForward>` function with a ``forwardInline`` type and
  ``details`` argument specified has been fixed.
    

menus API
=========

* The standard properties available to :ref:`onShown <menus.onShown>` are now available for
  messages being composed, if your extension has the :permission:`compose` permission.

tabs API
========

* At start-up, :ref:`tabs.create <tabs.create>` will now wait for a window to open before
  attempting to open a tab.
 
windows API
===========

* The :ref:`windows.openDefaultBrowser` function has been added. 

browserAction API
=================

* The :ref:`browserAction.setLabel` and :ref:`browserAction.getLabel` functions have been added. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

composeAction API
=================

* The :ref:`composeAction.setLabel` and :ref:`composeAction.getLabel` functions have been added. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

messageDisplayAction API
========================

* The :ref:`messageDisplayAction.setLabel` and :ref:`messageDisplayAction.getLabel` functions have been added. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

-------------------
Thunderbird 85 Beta
-------------------

addressBooks API & contacts API
===============================

The :doc:`/addressBooks` and :doc:`/contacts` will now return read-only address books. Add-ons that may update contacts and address books should check the ``readOnly`` flag of :ref:`addressBooks.AddressBookNode`.

accounts API
============

* The ``composeHtml`` property has been added to the :ref:`identities.MailIdentity` type, to indicate, if the identity uses HTML as the default compose format.

* The :ref:`accounts.getDefaultIdentity` function has been added, to get the default identity of a given account. Use :ref:`accounts.getDefault` to get the default account.

compose API
===========

* The begin* functions now honor ``body``, ``plainTextBody`` and ``isPlaintext`` as compose format selectors, overriding the default compose format of the used/default identity. The :doc:`/accounts` can be used to get the used/default identity and its default compose format.

messages API
============

* :ref:`messages.query` supports queries for messages with a given ``headerMessageId``

-------------------
Thunderbird 86 Beta
-------------------

theme API
=========

* The :ref:`theme_api` was added to Thunderbird (see `bug 1684666 <https://bugzilla.mozilla.org/show_bug.cgi?id=1684666>`__). It’s more or less the same as the `Firefox theme API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/theme>`__, but has been extended to better fit the needs of Thunderbird.
* The :doc:`/theme` was added to Thunderbird (see `bug 1684666 <https://bugzilla.mozilla.org/show_bug.cgi?id=1684666>`__). It’s more or less the same as the `Firefox theme API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/theme>`__, but has been extended to better fit the needs of Thunderbird.

  The color key ``sidebar_highlight_border`` has been added.

-------------------
Thunderbird 87 Beta
-------------------

commands API
============

* The :ref:`commands_api` now supports the internal shortcuts ``_execute_compose_action`` and ``_execute_message_display_action``.
* The :doc:`/commands` now supports the internal shortcuts ``_execute_compose_action`` and ``_execute_message_display_action``.

-------------------
Thunderbird 88 Beta
-------------------

compose API
===========

* added a ``type`` property to :ref:`compose.ComposeDetails`, to distinguish between ``new``, ``reply``, ``forward`` and ``draft``
* added a ``from`` property to :ref:`compose.ComposeDetails`, to get/set the actual from address (independent of the used identity)

contacts API
============

* fixed :ref:`contacts.quickSearch` to not fail on mailing lists

menus API
=========

* added a ``tools_menu`` context to :ref:`menus.ContextType`
* added a ``selectedAccount`` property to :ref:`menus.onShowData` and :ref:`menus.onClickData`, if the menu was opened on a root folder in the folder pane
* fixed :ref:`menus.onClicked` to keep the user input status so :ref:`browserAction.openPopup` can be used


messages API
============

* added :ref:`messages.listAttachments` and :ref:`messages.getAttachmentFile` methods to work with message attachments
* fixed :ref:`messages.getRaw` to work for nntp/news messages

-------------------
Thunderbird 89 Beta
-------------------

mailTabs API
============

* added :ref:`mailTabs.getCurrent` and :ref:`mailTabs.get` functions


menus API
=========

* fixed ``browser_action`` :ref:`menus.ContextType`
* added ``message_display_action`` and ``compose_action`` :ref:`menus.ContextType`
* introducing a ``fieldId`` property to :ref:`menus.onClickData` and :ref:`menus.onShowData` to to support fields part of the Thunderbird UI (currently supported values are ``composeSubject``, ``composeTo``, ``composeCc``, ``composeBcc``, ``composeReplyTo`` and ``composeNewsgroupTo``)

-------------------
Thunderbird 90 Beta
-------------------

cloudFile API
=============

* added support for the ``browser_style`` manifest property to the :doc:`/cloudFile`


compose API
===========

* added :ref:`compose.sendMessage` function
* added :ref:`compose.getComposeState` function
* added :ref:`compose.onComposeStateChanged` event
* added :ref:`compose.ComposeState` type
* added ``redirect`` enum to type property of :ref:`compose.ComposeDetails`

messages API
============

* added ``size`` property to the :ref:`messages.MessageHeader`

---------------------
Thunderbird 91.0 ESR
---------------------

accounts API
============

* :ref:`accounts.list`, :ref:`accounts.get` and :ref:`accounts.getDefault` now have an optional parameter ``includeFolders`` to specify if the returned :ref:`accounts.MailAccount` objects should populate the ``folders`` property. Defaults to ``true``


addressbooks API
================

* added ``remote`` property to :ref:`addressbooks.AddressBookNode`


cloudFile API
=============

* added the ``tab`` parameter to :ref:`cloudFile.onFileDeleted`
* added the ``tab`` parameter to :ref:`cloudFile.onFileUpload`
* added the ``tab`` parameter to :ref:`cloudFile.onFileUploadAbort`


compose API
===========

* all attachment related functions and events now also require the :permission:`compose` permission


contacts API
============

* added ``remote`` property to :ref:`contacts.ContactNode`
* second parameter to :ref:`contacts.quickSearch` can now be a qeuryInfo object instead of just a string, to define mored detailes query parameters


folders API
===========

* :ref:`folders.delete` now requires the :permission:`messagesDelete` permission
* added new function :ref:`folders.getParentFolders` to get information about the current hierarchy level and parent folders
* added new function :ref:`folders.getSubFolders` to get information about subfolders
* the :ref:`folders.create` function can now create folders in the root of an account, by specifying an account instead of a folder as first parameter
* added :ref:`folders.move` function
* added :ref:`folders.copy` function
* added :ref:`folders.getFolderInfo` function and :ref:`folders.MailFolderInfo` type to obtain additional folder information like ``totalMessageCounts`` or ``unreadMessageCounts``
* added :ref:`folders.onCreated` event
* added :ref:`folders.onRenamed` event
* added :ref:`folders.onMoved` event
* added :ref:`folders.onCopied` event
* added :ref:`folders.onDeleted` event
* added :ref:`folders.onFolderInfoChanged` event

identities API
==============

* added :doc:`/identities` (including create/delete/update functions and onCreated/onDeleted/onUpdated events)
* added ``signature`` and ``signatureIsPlainText`` to :ref:`identities.MailIdentity`


mailingLists API
================

* added ``remote`` property to :ref:`mailingLists.MailingListNode`


mailTabs API
============

* the :ref:`mailTabs.MailTab` object now includes a ``viewType`` property, supporting the values ``ungrouped``, ``groupedByThread`` and ``groupedBySortType``
* the :ref:`mailTabs.update` function allows to set the new ``viewType`` property


messages API
============

* :ref:`messages.query` now searches all messages and not only the indexed ones 
* added support for negative tag search to :ref:`messages.query`
* added ``includeSubFolders`` to search folders recursivly with :ref:`messages.query`
* added :ref:`messages.onUpdated`
* added :ref:`messages.onMoved`
* added :ref:`messages.onCopied`
* added :ref:`messages.onDeleted`
* added the :permission:`messagesDelete` permission to guard :ref:`messages.delete`

tabs API
========

* added ``type`` property to :ref:`tabs.Tab`, supporting ``addressBook``, ``calendar``, ``calendarEvent``, ``calendarTask``, ``chat``, ``content``, ``mail``, ``messageCompose``, ``messageDisplay``, ``special`` and ``tasks``
* added ``type`` as supported property of the ``queryInfo`` parameter of :ref:`tabs.query`

-----------------------
Thunderbird 91.0.2 ESR
-----------------------

browserAction API
=================

* backported support for the ``tabstoolbar`` location, usable in the ``default_area`` manifest key

-----------------------
Thunderbird 91.4.1 ESR
-----------------------

cloudFile API
=============

* backported support for the ``templateInfo`` property, which is now returned by the :ref:`cloudFile.onFileUpload` event

messages API
============

* backported support to query for a given ``headerMessageId`` in :ref:`messages.query`
