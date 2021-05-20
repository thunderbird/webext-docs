=============================
Changes in Thunderbird 78.4.0
=============================

compose
=======

* Attachments can now be specified in the :ref:`beginNew <compose.beginNew>`,
  :ref:`beginReply <compose.beginReply>`, and :ref:`beginForward <compose.beginForward>` functions.

tabs
====

* The :ref:`connect <tabs.connect>` and :ref:`sendMessage <tabs.sendMessage>` functions now work as
  they do in Firefox.

messageDisplay
==============

* The :ref:`messageDisplay.getDisplayedMessages` function has been added to allow access to details of multiple-selection of email. Previously only a single selection function was available.

* The :ref:`messageDisplay.onMessagesDisplayed` event has been added.

See the documentation on those functions and events for more information.

messageDisplayScripts/tabs
==========================

* Content script functions can now operate on a message display "tab" in the same way they do on a
  content tab in Thunderbird or Firefox. This requires the new "messagesModify" permission.

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
