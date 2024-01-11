Introduction to Experiment APIs
===============================

A WebExtension Experiment API is an additional API that is shipped with your WebExtension. It allows
your extension to interact with Thunderbird, much like earlier types of extension did. If you find
the built-in Thunderbird APIs can do 80% of what you want to achieve, then WebExtension Experiment
APIs are for you.

.. note::

  Firefox does not allow WebExtension Experiment APIs on release or beta versions. Thunderbird does.

The full code of this example is `on GitHub`__.

__ https://github.com/thunderbird/sample-extensions/tree/master/manifest_v2/experiment

.. note::

  This is a very cut-down example. You may find the `Firefox documentation`__ helpful, particularly
  the pages on `API schemas`__, `implementing a function`__, and `implementing an event`__.

  There is also a detailed introduction at `developer.thunderbird.net`__.

__ https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/index.html
__ https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/schema.html
__ https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/functions.html
__ https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/events.html
__ https://developer.thunderbird.net/add-ons/mailextensions/experiments

Extension manifest
------------------

Experiment APIs are declared in the experiment_apis property in a WebExtension’s manifest.json
file. For example:

.. code-block:: json

  {
    "manifest_version": 2,
    "name": "Extension containing an Experiment API",
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