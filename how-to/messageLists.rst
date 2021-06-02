==========================
Working with Message Lists
==========================

Mail folders could contain a *lot* of messages: thousands, tens of thousands, or even hundreds of thousands.

It would be a very bad idea to deal with that many messages at once, so the WebExtensions APIs split any response that could contain many messages into pages (or chunks, or groups, or whatever…). The default size of each page is 100 messages, although this could change and you **must not** rely on that number.

Each page is an object with two properties: ``id``, and ``messages``. To get the next page, call :ref:`messages.continueList` with the ``id`` property as an argument:

.. code-block:: javascript

  let page = await messenger.messages.list(folder);
  // Do something with page.messages.

  while (page.id) {
    page = await messenger.messages.continueList(page.id);
    // Do something with page.messages.
  }

You could also wrap this code in a generator for ease-of-use:

.. code-block:: javascript

  async function* listMessages(folder) {
    let page = await messenger.messages.list(folder);
    for (let message of page.messages) {
      yield message;
    }

    while (page.id) {
      page = await messenger.messages.continueList(page.id);
      for (let message of page.messages) {
        yield message;
      }
    }
  }

  let messages = listMessages(folder);
  for await (let message of messages) {
    // Do something with the message.
    let full = await messenger.messages.getFull(message.id);    
  }
