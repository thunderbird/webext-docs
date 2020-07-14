========================
WebExtension Experiments
========================

A WebExtension experiment is an additional API that is shipped with your WebExtension. It allows
your extension to interact with Thunderbird, much like earlier types of extension did. If you find
the built-in Thunderbird APIs can do 80% of what you want to achieve, then WebExtension experiments
are for you.

.. note::

  Firefox does not allow WebExtension experiments on release or beta versions. Thunderbird does.

Adding an experiment to your extension
======================================

The full code of this example is `on GitHub`__.

__ https://github.com/thundernest/sample-extensions/tree/master/experiment

.. note::

  This is a very cut-down example. You may find the `Firefox documentation`__ helpful, particularly
  the pages on `API schemas`__, `implementing a function`__, and `implementing an event`__.

__ https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/index.html
__ https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/schema.html
__ https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/functions.html
__ https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/events.html

Extension manifest
------------------

Experimental APIs are declared in the experiment_apis property in a WebExtension’s manifest.json
file. For example:

.. code-block:: json

  {
    "manifest_version": 2,
    "name": "Extension containing an experimental API",
    "experiment_apis": {
      "myapi": {
        "schema": "schema.json",
        "parent": {
          "scopes": ["addon_parent"],
          "paths": [["myapi"]],
          "script": "implementation.js"
        }
      }
    }
  }

Schema
------

The schema defines the interface between your experiment API and the rest of your extension, which
would use ``browser.myapi`` in this example. In it you describe the functions, events, and types
you'll be implementing:

.. code-block:: json

  [
    {
      "namespace": "myapi",
      "functions": [
        {
          "name": "sayHello",
          "type": "function",
          "description": "Says hello to the user.",
          "async": true,
          "parameters": [
            {
              "name": "name",
              "type": "string",
              "description": "Who to say hello to."
            }
          ]
        }
      ]
    }
  ]

You can see some more-complicated schemas `in the Thunderbird source code`__. 

__ https://hg.mozilla.org/comm-central/file/tip/mail/components/extensions/schemas

Implementing functions
----------------------

And finally, the implementation. In this file, you'll put all the code that directly interacts with
Thunderbird UI or components. Start by creating an object with the same name as your api at the top
level. (Remember to use ``var myapi`` or ``this.myapi``, not ``let myapi`` or ``const myapi``.)

The object has a function ``getAPI`` which returns another object containing your API. Your
functions and events are members of this returned object:

.. code-block:: javascript

  var myapi = class extends ExtensionCommon.ExtensionAPI {
    getAPI(context) {
      return {
        myapi: {
          async sayHello(name) {
            Services.wm.getMostRecentWindow("mail:3pane").alert("Hello " + name + "!");
          },
        }
      }
    }
  };

(Note that the sayHello function is an async function, and ``alert`` blocks until the prompt is
closed. If you call ``browser.myapi.sayHello()``, it would return a Promise that doesn't resolve
until the user closes the alert.)

Implementing events
-------------------

The code for events is more complicated, but the pattern is the same every time. The interesting
bit is the ``register`` function, with the argument named ``fire`` in this example. Any call to
``fire.async`` will notify listeners that the event fired with the arguments you used.

In ``register``, add event listeners, notification observers, or whatever else is needed.
``register`` runs when the extension calls ``browser.myapi.onToolbarClick.addListener``, and
returns a function that removes the listeners and observers. This returned function runs when the
extension calls ``browser.myapi.onToolbarClick.removeListener``, or shuts down.

.. code-block:: javascript

  var myapi = class extends ExtensionCommon.ExtensionAPI {
    getAPI(context) {
      return {
        myapi: {
          onToolbarClick: new ExtensionCommon.EventManager({
            context,
            name: "myapi.onToolbarClick",
            register(fire) {
              function callback(event, id, x, y) {
                return fire.async(id, x, y);
              }

              windowListener.add(callback);
              return function() {
                windowListener.remove(callback);
              };
            },
          }).api(),
        }
      }
    }
  };

Using folder and message types
------------------------------

The built-in schema define some common objects that you may wish to return, namely
:ref:`MailFolder <folders.MailFolder>`, :ref:`MessageHeader <messages.MessageHeader>`,
and :ref:`MessageList <messages.MessageList>`.

To use these types, interact with the ``folderManager`` or ``messageManager`` objects which are
members of the ``context.extension`` object passed to ``getAPI``:

.. code-block:: javascript

  // Get an nsIMsgFolder from a MailFolder:
  let realFolder = context.extension.folderManager.get(accountId, path);

  // Get a MailFolder from an nsIMsgFolder:
  context.extension.folderManager.convert(realFolder);

  // Get an nsIMsgDBHdr from a MessageHeader:
  let realMessage = context.extension.messageManager.get(messageId);

  // Get a MessageHeader from an nsIMsgDBHdr:
  context.extension.messageManager.convert(realMessage);

  // Start a MessageList from an array or enumerator of nsIMsgDBHdr:
  context.extension.messageManager.startMessageList(realFolder.messages);

Using tabs and windows
----------------------

To access tabs or windows using the ID values from the built-in APIs, use the ``tabManager`` or
``windowManager`` objects. These are have functions similar to, but not the same as, the APIs:

.. code-block:: javascript

  // Get a real tab from a tab ID:
  let tabObject = context.extension.tabManager.get(tabId);
  let realTab = tabObject.nativeTab;
  let realTabWindow = tabObject.window;

  // Get a tab ID from a real tab:
  context.extension.tabManager.getWrapper(realTab).id;

  // Query tabs: (note this returns a Generator, not an array like the API)
  context.extension.tabManager.query(queryInfo);

"Tabs" are a bit weird. For a tab on the main Thunderbird window, the ``nativeTab`` property is
the ``tabInfo`` object you'd get from that window's ``<tabmail>``. For a tab *not* on the main
window, e.g. a "tab" representing the message composition window, both ``nativeTab`` and ``window``
properties refer to the window itself.

.. code-block:: javascript

  // Get a real window from a window ID:
  let windowObject = context.extension.windowManager.get(windowId);
  let realWindow = windowObject.window;

  // Get a window ID from a real window:
  context.extension.windowManager.getWrapper(realWindow).id;

  // Get all windows: (note this returns a Generator, not an array like the API)
  context.extension.windowManager.getAll();

For more things you could use on ``tabObject`` or ``windowObject`` in the examples above, see
`the Tab, TabMailTab, and Window classes in the source code`__.

__ https://hg.mozilla.org/releases/comm-esr78/file/tip/mail/components/extensions/parent/ext-mail.js#l763

Experiment API Generator
========================

Try the `Experiment Generator`__ to quickly get started making a WebExtension experiment. It
doesn't cover all the possibilities, but should be useful for most use-cases or learning how
things work.

__ https://darktrojan.github.io/generator/generator.html

Getting your API added to Thunderbird
=====================================

If you think your API would be useful to other extensions, consider having it added to Thunderbird.
`File a bug in the Extensions API component`__ and add your schema and implementation files as
attachments.

__ https://bugzilla.mozilla.org/enter_bug.cgi?product=Thunderbird&component=Add-Ons%3A%20Extensions%20API
