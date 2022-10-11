=========================
Changes in Thunderbird 77
=========================

compose
=======

* The :doc:`/compose` API functions :ref:`beginNew <compose.beginNew>`,
  :ref:`beginReply <compose.beginReply>`, and :ref:`beginForward <compose.beginForward>` now return
  a :ref:`tabs.Tab` object for use with other API functions.

* Listeners to the :ref:`compose.onBeforeSend <compose.onBeforeSend>` event are now called
  sequentially in the order they were added. Be aware that other extensions may see this event
  before or after yours does.

tabs
====

* Events in the :doc:`/tabs` and :doc:`/windows` APIs now fire in many more situations:

  * Calendar tabs now fire :ref:`tabs.onCreated <tabs.onCreated>`,
    :ref:`tabs.onActivated <tabs.onActivated>`, and :ref:`tabs.onRemoved <tabs.onRemoved>` just
    like other tabs do.

  * The first 3-pane tab in a main window now fires :ref:`tabs.onCreated <tabs.onCreated>` when the
    window opens.

  * Address book, composition, and message display windows now fire
    :ref:`tabs.onCreated <tabs.onCreated>` and :ref:`tabs.onRemoved <tabs.onRemoved>` events as
    well as :ref:`windows.onCreated <windows.onCreated>` and
    :ref:`windows.onRemoved <windows.onRemoved>` events. Each of these windows has exactly one tab
    in the :doc:`/tabs` API and the added events reflect that.

    Whether the ``tabs`` event happens before or after the corresponding ``windows`` event is
    non-deterministic.

composeScripts/tabs
===================

* Content script functions can now operate on a compose window "tab" in the same way they do on a
  content tab in Thunderbird or Firefox. (Despite the fact they don't have tabs, compose windows
  have one tab object under the :doc:`/tabs` API.) This requires the "compose" permission.

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
  :doc:`/composeScripts` API. Again, this works just like the contentScripts API:

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

---

Bugzilla list of fixed WebExtension API defects in `Thunderbird 77 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=77%20Branch&o2=equals>`__.
