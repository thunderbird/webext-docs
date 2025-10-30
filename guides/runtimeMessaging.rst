.. container:: sticky-sidebar
  
  .. include:: ../_includes/developer-resources.rst

======================
Using runtime messages
======================

Different parts of a WebExtension can communicate using runtime messages. The receiving end must register a listener function:

.. code-block:: javascript

  function listener(data, sender, sendResponse) {
    // Do something with the received data and sender parameters.
    switch (data.msg) {
      case "greet":
        console.log(`Hello from tab ${sender.tab.id}`);
        sendResponse("Hi there!");
        break;
      case "farewell":
        console.log(`Goodbye from tab ${sender.tab.id}`);
        sendResponse("Goodbye!");
        break;
    } 
  }
  messenger.runtime.onMessage.addListener(listener);


Any other part of the extension can now send messages to this listener:

.. code-block:: javascript

  await messenger.runtime.sendMessage({ msg: "greet" });

There are a few quirks that developers should be aware of:

* A script cannot send a message to itself. A message sent from the background will not be received by listeners in the background script.
* The listener function should not be asynchronous. If multiple `runtime.onMessage` listeners are registered, asynchronous listeners can trigger unexpected behavior. Even with only one listener, it is best practice to keep them synchronous to avoid future debugging issues.
* When multiple listeners are registered for the `runtime.onMessage` event, each receives the message. How they respond determines which result is returned to the sender.

Using multiple onMessage listeners with synchronous responses
=============================================================

If a WebExtension registers multiple `runtime.onMessage` listeners (in the same file or in different files), all listeners will be called when a message is sent. The simplest way to define which listener should respond is by using the `sendResponse()` function selectively. For example:

.. code-block:: javascript
   :caption: popup1.js

   function listener(data, sender, sendResponse) {
     switch (data.msg) {
       case "greet":
         console.log(`Hello from tab ${sender.tab.id}`);
         sendResponse("Hi there!");
         break;
     } 
   }
   messenger.runtime.onMessage.addListener(listener);

.. code-block:: javascript
   :caption: popup2.js

   function listener(data, sender, sendResponse) {
     switch (data.msg) {
       case "farewell":
         console.log(`Goodbye from tab ${sender.tab.id}`);
         sendResponse("Goodbye!");
         break;
     } 
   }
   messenger.runtime.onMessage.addListener(listener);

.. code-block:: javascript
   :caption: background.js

   // Send a "greet" message
   let response = await messenger.runtime.sendMessage({ msg: "greet" });
   console.log(response); // "Hi there!"

If both popup files are loaded, both listeners will be invoked, but only the listener in `popup1.js` sends a response.

Using multiple onMessage listeners with asynchronous responses
==============================================================

If a WebExtension registers multiple `runtime.onMessage` listeners, and at least one needs to perform asynchronous operations before responding, the situation becomes more complex. The following two approaches for handling asynchronous responses are supported:

* The listener returns `true` to indicate that it will respond asynchronously. The `sendResponse()` channel will be kept open until the listener uses it to send its response.

  .. code-block:: javascript
    :caption: popup1.js

    async function performAsyncOperation(data, sender) {
      // Simulate async work.
      await new Promise(resolve => setTimeout(resolve, 1000)); 
      return "Hi there!";
    }

    function listener(data, sender, sendResponse) {
      switch (data.msg) {
        case "greet":
          console.log(`Hello from tab ${sender.tab.id}`);
          performAsyncOperation(data, sender).then(
            // Send the response when the async operation is complete.
            response => sendResponse(response) 
          );   
          break;
      }
      // Indicate that we will respond asynchronously, keeping the sendResponse channel open.
      return true; 
    }
    messenger.runtime.onMessage.addListener(listener);

  .. code-block:: javascript
    :caption: popup2.js

    function listener(data, sender, sendResponse) {
      switch (data.msg) {
        case "farewell":
          console.log(`Goodbye from tab ${sender.tab.id}`);
          sendResponse("Goodbye!");
          break;
      } 
    }
    messenger.runtime.onMessage.addListener(listener);   

  Both listeners will be called whenever a message is sent. If the message is "greet", the listener in `popup1.js` performs its asynchronous operation and responds after a delay. If the message is "farewell", the listener in `popup2.js` responds immediately.

  .. note::

    The return value of `messenger.runtime.sendMessage()` received by the sending party is always a `Promise`, regardless of whether the message is handled synchronously or asynchronously.

* The listener returns a `Promise` for the response. This approach is more straightforward and easier to read. For example:

  .. code-block:: javascript
    :caption: popup1.js

    async function performAsyncOperation(data, sender) {
       // Simulate async work.
      await new Promise(resolve => setTimeout(resolve, 1000));
      return "Hi there!";
    }

    function listener(data, sender, sendResponse) {
      switch (data.msg) {
        case "greet":
          console.log(`Hello from tab ${sender.tab.id}`);
          // Return a Promise that resolves to the response.
          return performAsyncOperation(data, sender); 
      }
    }
    messenger.runtime.onMessage.addListener(listener);

  .. code-block:: javascript
    :caption: popup2.js

    function listener(data, sender, sendResponse) {
      switch (data.msg) {
        case "farewell":
          console.log(`Goodbye from tab ${sender.tab.id}`);
          // Return a resolved Promise for the response.
          return Promise.resolve("Goodbye!");
      } 
    }
    messenger.runtime.onMessage.addListener(listener);   

  Both listeners will be called whenever a message is sent. If the message is "greet", the listener in `popup1.js` performs its asynchronous operation and returns a Promise for its response. If the message is "farewell", the listener in `popup2.js` responds with an already resolved Promise.

  .. note::

    The implementation in `popup2.js` could also simply use `sendResponse("Goodbye!")` instead of returning a resolved Promise. Both approaches are valid and will work correctly.

  The important point to remember is that listeners should return a `Promise` only when they actually handle the message. Consider the following alternative implementation using an asynchronous listener function for `popup1.js`:
  
  .. code-block:: javascript
    :caption: popup1.js

    async function listener(data, sender, sendResponse) {
      switch (data.msg) {
        case "greet":
          console.log(`Hello from tab ${sender.tab.id}`);
          await new Promise(resolve => setTimeout(resolve, 1000)); // Simulate async work
          return { response: "Hi there!" };
      }
    }
    messenger.runtime.onMessage.addListener(listener);  

  This may cause the sender to receive an `undefined` response when sending a "farewell" message, since the listener in `popup1.js` always returns a `Promise`, even when it doesn't handle the message. Depending on the registration order and other timing effects, the response from `popup2.js` may be ignored.
