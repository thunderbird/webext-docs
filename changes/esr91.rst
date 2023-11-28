============================
Changes up to Thunderbird 91
============================

------------------
Thunderbird 81.0b1
------------------

messageDisplay
==============

* The :ref:`messageDisplay.getDisplayedMessages` function has been added to allow access to details of multiple-selection of email. Previously only a single selection function was available.

  *This change has been backported to Thunderbird 78.4.0.*

* The :ref:`messageDisplay.onMessagesDisplayed` event has been added.

  *This change has been backported to Thunderbird 78.4.0.*

See the documentation on those functions and events for more information.

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 79 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=Thunderbird%2079&o2=equals>`__, `Thunderbird 80 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=Thunderbird%2080&o2=equals>`__ and `Thunderbird 81 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=81%20Branch&o2=equals>`__.

.. _thunderbird_82_0b1:

------------------
Thunderbird 82.0b1
------------------

compose
=======

* Attachments can now be specified in the :ref:`beginNew <compose.beginNew>`,
  :ref:`beginReply <compose.beginReply>`, and :ref:`beginForward <compose.beginForward>` functions.

  *This change has been backported to Thunderbird 78.4.0.*

tabs
====

* The :ref:`connect <tabs.connect>` and :ref:`sendMessage <tabs.sendMessage>` functions now work as
  they do in Firefox.

  *This change has been backported to Thunderbird 78.4.0.*

messageDisplayScripts/tabs
==========================

* Content script functions can now operate on a message display "tab" in the same way they do on a
  content tab in Thunderbird or Firefox. This requires the new "messagesModify" permission.

  *This change has been backported to Thunderbird 78.4.0.*

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
  :doc:`/messageDisplayScripts` API. 
  
  *This change has been backported to Thunderbird 78.4.0.*
  
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

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 82 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=82%20Branch&o2=equals>`__.

------------------
Thunderbird 83.0b1
------------------

compose
=======

* :ref:`ComposeAttachment <compose.ComposeAttachment>` objects now have a ``size`` property with
  the size of the attachment in bytes.
  
  *This change has been backported to Thunderbird 78.5.0.*

contacts
========

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

menus
=====

* A ``compose_attachment`` context can now be used. This context applies when the user opens a
  context menu on selected attachments in a compose window. The selected attachments can be
  accessed from the ``attachments`` property in an :ref:`onShown <menus.onShown>` or
  :ref:`onClicked <menus.onClicked>` listener.
  
  *This change has been backported to Thunderbird 78.5.0.*
  
* The standard properties available to :ref:`onShown <menus.onShown>` are now available for
  messages being displayed, if your extension has the ``messagesRead`` permission.

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 83 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=83%20Branch&o2=equals>`__.

------------------
Thunderbird 84.0b1
------------------

compose
=======

* The :ref:`beginNew <compose.beginNew>` function now has an optional ``messageId`` argument. If
  ``messageId`` is provided, the referenced message is opened to compose as a new message. This
  works for ordinary messages and templates.

  *This change has been backported to Thunderbird 78.7.0.*
  
* Using :ref:`beginForward <compose.beginForward>` function with a ``forwardInline`` type and
  ``details`` argument specified has been fixed.
  
  *This change has been backported to Thunderbird 78.7.0.*
  

menus
=====

* The standard properties available to :ref:`onShown <menus.onShown>` are now available for
  messages being composed, if your extension has the ``compose`` permission.

  *This change has been backported to Thunderbird 78.6.0.*

tabs
====

* At start-up, :ref:`tabs.create <tabs.create>` will now wait for a window to open before
  attempting to open a tab.

  *This change has been backported to Thunderbird 78.5.0.*
 
windows
=======

* The :ref:`windows.openDefaultBrowser` function has been added. 

  *This change has been backported to Thunderbird 78.6.0.*

browserAction
==================================================

* The :ref:`browserAction.setLabel` and :ref:`browserAction.getLabel` functions have been added. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

  *This change has been backported to Thunderbird 78.6.0.*

composeAction
==================================================

* The :ref:`composeAction.setLabel` and :ref:`composeAction.getLabel` functions have been added. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

  *This change has been backported to Thunderbird 78.6.0.*

messageDisplayAction
==================================================

* The :ref:`messageDisplayAction.setLabel` and :ref:`messageDisplayAction.getLabel` functions have been added. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

  *This change has been backported to Thunderbird 78.6.0.*

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 84 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=84%20Branch&o2=equals>`__.

------------------
Thunderbird 85.0b1
------------------

addressBooks & contacts
=======================

The :ref:`addressBooks_api` and :ref:`contacts_api` APIs will now return read-only address books. Add-ons that may update contacts and address books should check the ``readOnly`` flag of :ref:`addressBooks.AddressBookNode`.

accounts
========

* The ``composeHtml`` property has been added to the :ref:`identities.MailIdentity` type, to indicate, if the identity uses HTML as the default compose format.

  *This change has been backported to Thunderbird 78.7.0.*

* The :ref:`accounts.getDefaultIdentity` function has been added, to get the default identity of a given account. Use :ref:`accounts.getDefault` to get the default account.

  *This change has been backported to Thunderbird 78.7.0.*

compose
=======

* The begin* functions now honor ``body``, ``plainTextBody`` and ``isPlaintext`` as compose format selectors, overriding the default compose format of the used/default identity. The :ref:`accounts_api` API can be used to get the used/default identity and its default compose format.

  *This change has been backported to Thunderbird 78.7.0.*

messages
========

* :ref:`messages.query` supports queries for messages with a given ``headerMessageId``

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 85 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=85%20Branch&o2=equals>`__.

------------------
Thunderbird 86.0b1
------------------

theme
=====

* The :ref:`theme_api` API was added to Thunderbird (see `bug 1684666 <https://bugzilla.mozilla.org/show_bug.cgi?id=1684666>`__). It’s more or less the same as the `Firefox theme API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/theme>`__, but has been extended to better fit the needs of Thunderbird.

  The color key ``sidebar_highlight_border`` has been added.

  *This change has been backported to Thunderbird 78.7.1.*

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 86 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=86%20Branch&o2=equals>`__.

------------------
Thunderbird 87.0b1
------------------

commands
========

* The :ref:`commands_api` API now supports the internal shortcuts ``_execute_compose_action`` and ``_execute_message_display_action``.

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 87 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=87%20Branch&o2=equals>`__.

------------------
Thunderbird 88.0b1
------------------

compose
=======

* added a ``type`` property to :ref:`compose.ComposeDetails`, to distinguish between ``new``, ``reply``, ``forward`` and ``draft``
* added a ``from`` property to :ref:`compose.ComposeDetails`, to get/set the actual from address (independent of the used identity)

contacts
========

* fixed :ref:`contacts.quickSearch` to not fail on mailing lists

menus
=====

* added a ``tools_menu`` context to :ref:`menus.ContextType`
* added a ``selectedAccount`` property to :ref:`menus.onShowData` and :ref:`menus.onClickData`, if the menu was opened on a root folder in the folder pane
* fixed :ref:`menus.onClicked` to keep the user input status so :ref:`browserAction.openPopup` can be used


messages
========

* added :ref:`messages.listAttachments` and :ref:`messages.getAttachmentFile` methods to work with message attachments
* fixed :ref:`messages.getRaw` to work for nntp/news messages

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 88 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=88%20Branch&o2=equals>`__.

------------------
Thunderbird 89.0b1
------------------

mailTabs
========

* added :ref:`mailTabs.getCurrent` and :ref:`mailTabs.get` functions


menus
=====

* fixed ``browser_action`` :ref:`menus.ContextType`
* added ``message_display_action`` and ``compose_action`` :ref:`menus.ContextType`
* introducing a ``fieldId`` property to :ref:`menus.onClickData` and :ref:`menus.onShowData` to to support fields part of the Thunderbird UI (currently supported values are ``composeSubject``, ``composeTo``, ``composeCc``, ``composeBcc``, ``composeReplyTo`` and ``composeNewsgroupTo``)

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 89 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=89%20Branch&o2=equals>`__.

------------------
Thunderbird 90.0b1
------------------

cloudFile
=========

* added support for the ``browser_style`` manifest property to the :ref:`cloudFile_api` API


compose
=========

* added :ref:`compose.sendMessage` function
* added :ref:`compose.getComposeState` function
* added :ref:`compose.onComposeStateChanged` event
* added :ref:`compose.ComposeState` type
* added ``redirect`` enum to type property of :ref:`compose.ComposeDetails`

messages
========

* added ``size`` property to the :ref:`messages.MessageHeader`

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 90 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=90%20Branch&o2=equals>`__.

----------------
Thunderbird 91.0
----------------

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

* added :ref:`identities_api` API (including create/delete/update functions and onCreated/onDeleted/onUpdated events)
* added ``signature`` and ``signatureIsPlainText`` to :ref:`identities.MailIdentity`


mailingLists API
================

* added ``remote`` property to :ref:`mailingLists.MailingListNode`


mailTabs
========

* the :ref:`mailTabs.MailTab` object now includes a ``viewType`` property, supporting the values ``ungrouped``, ``groupedByThread`` and ``groupedBySortType``
* the :ref:`mailTabs.update` function allows to set the new ``viewType`` property


messages
========

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

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 91 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=91%20Branch&o2=equals>`__.

------------------
Thunderbird 91.0.2
------------------

browserAction API
=================

* added support for the ``tabstoolbar`` location, usable in the ``default_area`` manifest key

------------------
Thunderbird 91.4.1
------------------

cloudFile API
=============

* added the ``templateInfo`` member to the returned properties of the :ref:`cloudFile.onFileUpload` event
* added the :ref:`cloudFile.onFileRename` event

messages
========

* :ref:`messages.query` supports queries for messages with a given ``headerMessageId``
