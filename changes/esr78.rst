================================
Changes up to Thunderbird 78 ESR
================================

-------------------
Thunderbird 74 Beta
-------------------

legacy API
==========

* The legacy API has been removed.

accounts API & folders API
==========================

* The :ref:`MailFolder <folders.MailFolder>` object gained a subFolders property. From now on the
  :doc:`accounts API functions </accounts>` will return a hierarchy of folders instead of a flat
  list. If you still need a flat list you should traverse the folder hierarchy:

  .. code-block:: javascript

    browser.accounts.list().then(accounts => {
      let arrayOfFolders = [];

      function traverse(folders) {
        if (!folders) {
          return;
        }
        for (let f of folders) {
          arrayOfFolders.push(f);
          traverse(f.subFolders);
        }
      }

      for (let account of accounts) {
        traverse(account.folders);
      }
      return arrayOfFolders;
    });

  This example code works with both the current API in 68 and the new version in 74 (which will be
  backported to 68 after some time in beta).

compose API
===========

* The compose API gained two new functions and an event. The
  :ref:`getComposeDetails <compose.getComposeDetails>` and
  :ref:`setComposeDetails <compose.setComposeDetails>` functions let you retrieve or change the
  recipients and subject of a message being composed. More details will be added later. The
  :ref:`onBeforeSend <compose.onBeforeSend>` event is fired when a message is about to be sent. At
  this point your extension can prevent sending or change the same details as in the new functions.

messages API
============

* The :ref:`query <messages.query>` function can now query by tags.

* The :ref:`MessageHeader <messages.MessageHeader>` object now has junk properties:
  ``junkScore`` is an integer score from 0 (not spam) to 100 (spam).
  ``junk`` shows whether or not that score is greater than the junk threshold.

-------------------
Thunderbird 75 Beta
-------------------

action APIs
===========

* The onClick event of the action APIs now has information about the active tab and the click event.

  This brings the events into line with browser WebExtensions. For messageDisplayAction, this is a
  change of behavior – previously the ID of the active tab was passed as the first argument.

  *This change was uplifted to 74 beta 2.*

compose API
===========

* The :ref:`onBeforeSend <compose.onBeforeSend>` event now has information about the active tab.

  *This change was uplifted to 74 beta 2.*

* The compose API functions can now handle the message body.

  All responses from :ref:`getComposeDetails <compose.getComposeDetails>` calls and
  :ref:`onBeforeSend <compose.onBeforeSend>` events now return the message body. How you handle this
  depends on the composition mode (plain text or HTML). For plain text composition mode, the
  ``isPlainText`` field is set to ``true`` and ``plainTextBody`` should be used. For HTML
  composition, ``isPlainText`` is set to ``false`` and ``body`` should be used.

  The ``body`` field is a string. You should parse this to an HTML document before modifying it, and
  serialise the document back to a string before calling setComposeDetails. `Here's a sample
  extension.`__

  __ https://github.com/thunderbird/sample-extensions/tree/master/composeBody

messages API
============

* A new event was added: :ref:`onNewMailReceived <messages.onNewMailReceived>`.

  Your extension can now be notified of incoming mail. This is based on the
  ``MailServices.mfn.msgsClassified`` notification.

-------------------
Thunderbird 76 Beta
-------------------

accounts API
============

* Thunderbird 76 introduces the :ref:`identities.MailIdentity` type for interacting with mail
  identities. Like the rest of the accounts API, it is mostly read-only as we believe that
  configuration of identities should only happen using the built-in UI.

* The :ref:`accounts.MailAccount` type now contains a list of identities associated with that
  account. The default identity is listed first and other identities are in no particular order.

compose API
===========

* The :ref:`compose.ComposeDetails` type now has an ``identityId`` field for getting or setting the
  identity associated with a message being composed.

mailTabs/messageDisplay
=======================

* For consistency with other APIs and with browser WebExtensions (ie. those used in Firefox, etc.),
  some events that passed a numeric tab ID to listeners now pass an object representing the tab
  instead. *This change is not backwards-compatible.*

  The affected events are:

  * :ref:`mailTabs.onDisplayedFolderChanged`
  * :ref:`mailTabs.onSelectedMessagesChanged`
  * :ref:`messageDisplay.onMessageDisplayed`

messages API
============

* The :permission:`accountsRead` permission is now required for all functions that accept a
  :ref:`folders.MailFolder` argument. The permission was already required to obtain a ``MailFolder``
  anyway, so this change should not break extensions.

experiment APIs
===============

* For extensions with the :permission:`addressBooks` permission, a new ``addressBookManager`` object is
  available to WebExtensions experiment implementations. The ``addressBookManager`` provides the
  following functions to help you interact with the :doc:`/addressBooks`, :doc:`/contacts` and
  :doc:`/mailingLists`:

  * ``findAddressBookById``, ``findContactById``, ``findMailingListById`` to help you find "real"
    address book objects (``nsIAbCard``, ``nsIAbDirectory``) for the IDs provided by the
    addressBooks API. Note that there is active development in the address book and these interfaces
    will be changing in the near term without public announcement.
  * ``convert`` to turn "real" objects back into API-friendly objects.

  For more information on these functions see the `source code of the addressBooks APIs`__.

__ https://hg.mozilla.org/comm-central/file/tip/mail/components/extensions/parent/ext-addressBook.js


.. _thunderbird_77_0b1:

-------------------
Thunderbird 77 Beta
-------------------

compose API
===========

* The :doc:`/compose` functions :ref:`beginNew <compose.beginNew>`,
  :ref:`beginReply <compose.beginReply>`, and :ref:`beginForward <compose.beginForward>` now return
  a :ref:`tabs.Tab` object for use with other API functions.

* Listeners to the :ref:`compose.onBeforeSend <compose.onBeforeSend>` event are now called
  sequentially in the order they were added. Be aware that other extensions may see this event
  before or after yours does.

tabs API
========

* Events in the :doc:`/tabs` and :doc:`/windows` now fire in many more situations:

  * Calendar tabs now fire :ref:`tabs.onCreated <tabs.onCreated>`,
    :ref:`tabs.onActivated <tabs.onActivated>`, and :ref:`tabs.onRemoved <tabs.onRemoved>` just
    like other tabs do.

  * The first 3-pane tab in a main window now fires :ref:`tabs.onCreated <tabs.onCreated>` when the
    window opens.

  * Address book, composition, and message display windows now fire
    :ref:`tabs.onCreated <tabs.onCreated>` and :ref:`tabs.onRemoved <tabs.onRemoved>` events as
    well as :ref:`windows.onCreated <windows.onCreated>` and
    :ref:`windows.onRemoved <windows.onRemoved>` events. Each of these windows has exactly one tab
    in the :doc:`/tabs` and the added events reflect that.

    Whether the ``tabs`` event happens before or after the corresponding ``windows`` event is
    non-deterministic.

composeScripts API
==================

* Content script functions can now operate on a compose window "tab" in the same way they do on a
  content tab in Thunderbird or Firefox. (Despite the fact they don't have tabs, compose windows
  have one tab object under the :doc:`/tabs`.) This requires the :permission:`compose` permission.

  Here are some basic examples. See `the MDN documentation`__ for a more in-depth explanation.

  .. code-block:: javascript

    // Where tabId is the id of a compose window tab:

    browser.tabs.executeScript(tabId, {
      code: `document.body.textContent = "Hey look, the script ran!";`,
    });

    browser.tabs.executeScript(tabId, {
      file: "compose.js",
    });

    browser.tabs.insertCSS(tabId, {
      code: "body { background-color: red; }",
    });

    browser.tabs.insertCSS(tabId, {
      file: "compose.css",
    });

    browser.tabs.removeCSS(tabId, {
      code: "body { background-color: red; }",
    });

    browser.tabs.removeCSS(tabId, {
      file: "compose.css",
    });

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts

* Scripts can also be registered to run automatically on composition window "tabs", using the new
  :doc:`/composeScripts`. Again, this works just like the contentScripts API:

  .. code-block:: javascript

    let registeredScripts = await browser.composeScripts.register({
      css: [
        // Any number of code or file objects could be listed here.
        { code: "body { background-color: red; }" },
        { file: "compose.css" },
      ],
      js: [
        // Any number of code or file objects could be listed here.
        { code: `document.body.textContent = "Hey look, the script ran!";` },
        { file: "compose.js" },
      ],
    });

  Added code will run immediately and CSS will be immediately applied to already-open composition
  windows, and any new composition windows.

  The returned value, ``registeredScripts`` in this example, is an object with which you can
  unregister the code/CSS:

  .. code-block:: javascript

    await registeredScripts.unregister();

.. warning::

  This functionality has the ability to completely destroy every message being composed, with no
  way to undo it. Be careful!

.. note::

  Javascript or CSS applied by these methods is *not* sent with the message. This is not a way to
  decorate messages or make them interactive.

--------------------
Thunderbird 78.0 ESR
--------------------

compose API
===========

* Attachments in the compose window can now be accessed with the compose API. These functions have
  been added:

  * :ref:`compose.listAttachments`
  * :ref:`compose.addAttachment`
  * :ref:`compose.updateAttachment`
  * :ref:`compose.removeAttachment`

  These events have been added:

  * :ref:`compose.onAttachmentAdded`
  * :ref:`compose.onAttachmentRemoved`

  See the documentation on those functions and events for more information.

* A new event, :ref:`compose.onIdentityChanged` was added.


identity API
============

* The `browser.identity <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/identity>`__
  namespace for OAuth handling was enabled.

----------------------
Thunderbird 78.4.0 ESR
----------------------

compose API
===========

* Backported support for attachments being specified in the :ref:`beginNew <compose.beginNew>`,
  :ref:`beginReply <compose.beginReply>`, and :ref:`beginForward <compose.beginForward>` functions.

messageDisplay API
==================

* The :ref:`messageDisplay.getDisplayedMessages` function has been backported to allow access to details of multiple-selection of email. Previously only a single selection function was available.

* The :ref:`messageDisplay.onMessagesDisplayed` event has been backported.

messageDisplayScripts API
=========================

* Backported support for content script functions to operate on a message display tab in the same way they do on a
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


tabs API
========

* The :ref:`connect <tabs.connect>` and :ref:`sendMessage <tabs.sendMessage>` functions now work as
  they do in Firefox.

----------------------
Thunderbird 78.5.0 ESR
----------------------

compose API
===========

* :ref:`ComposeAttachment <compose.ComposeAttachment>` objects now have a ``size`` property with
  the size of the attachment in bytes.

* Backported support for the ``compose_attachment`` context. This context applies when the user opens a
  context menu on selected attachments in a compose window. The selected attachments can be
  accessed from the ``attachments`` property in an :ref:`onShown <menus.onShown>` or
  :ref:`onClicked <menus.onClicked>` listener.

tabs API
========

* At start-up, :ref:`tabs.create <tabs.create>` will now wait for a window to open before
  attempting to open a tab.

----------------------
Thunderbird 78.6.0 ESR
----------------------

menus API
=========

* The standard properties available to :ref:`onShown <menus.onShown>` are now available for
  messages being composed, if your extension has the :permission:`compose` permission.

windows API
===========

* Backported the :ref:`windows.openDefaultBrowser` function. 

----------------------
Thunderbird 78.6.1 ESR
----------------------

action API
==========

* The :ref:`action.setLabel` and :ref:`action.getLabel` functions have been backported. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

composeAction API
=================

* The :ref:`composeAction.setLabel` and :ref:`composeAction.getLabel` functions have been backported. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

messageDisplayAction API
========================

* The :ref:`messageDisplayAction.setLabel` and :ref:`messageDisplayAction.getLabel` functions have been backported. It is now possible to set a label value different from the title (which is used as tooltip text). The label can be set to an empty string to make the action button not have a label at all. If the toolbar is set to text-mode only (no icons), the action button label uses the title as fallback, in case an empty label has been set.

----------------------
Thunderbird 78.7.0 ESR
----------------------

accounts API
============

* The ``composeHtml`` property has been backported to the :ref:`identities.MailIdentity` type, to indicate, if the identity uses HTML as the default compose format.

compose API
===========

* The begin* functions now honor ``body``, ``plainTextBody`` and ``isPlaintext`` as compose format selectors, overriding the default compose format of the used/default identity. The :ref:`accounts_api` can be used to get the used/default identity and its default compose format.

* The :ref:`beginNew <compose.beginNew>` function now has an optional ``messageId`` argument. If
  ``messageId`` is provided, the referenced message is opened to compose as a new message. This
  works for ordinary messages and templates.
  
* Using :ref:`beginForward <compose.beginForward>` function with a ``forwardInline`` type and
  ``details`` argument specified has been fixed.

----------------------
Thunderbird 78.7.1 ESR
----------------------

theme API
=========

* The :ref:`theme_api` was backported (see `bug 1684666 <https://bugzilla.mozilla.org/show_bug.cgi?id=1684666>`__). It’s more or less the same as the `Firefox theme API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/theme>`__, but has been extended to better fit the needs of Thunderbird.

  The color key ``sidebar_highlight_border`` has been added.
