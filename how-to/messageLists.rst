==========================
Working with message lists
==========================

Mail folders could contain a *lot* of messages: thousands, tens of thousands, or even hundreds of thousands.

It would be a very bad idea to deal with that many messages at once, so the WebExtensions APIs split any response that could contain many messages into pages (or chunks). The default size of each page is 100 messages, although this could change and you **must not** rely on that number.

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

  async function* getMessages(list) {
    let page = await list;
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

  let messages = getMessages(messenger.messages.list(folder));
  for await (let message of messages) {
    // Do something with the message.
    let full = await messenger.messages.getFull(message.id);    
  }

Working with queries
====================

A :ref:`messages.query` will be executed asynchronously and could need a long time
to complete, if the user has a lot of messages.

Additionally, Thunderbird may have already found the relevant messages, but is not
yet returning them. This is due to the pagination mechanism which typically only
returns a page after 100 messages have been added (or until the end of the list is reached).

There are some measures to deal with these restrictions:

* The auto pagination mechanism introduced in Thunderbird 121 will return pages
  after the defined ``autoPaginationTimeout`` (default is :value:1000 ms) even if
  the page has not yet reached its nominal page size. The auto pagination mechanism
  can be disabled by setting the ``autoPaginationTimeout`` property of the
  ``queryInfo`` object to :value:0.

* An still ongoing query can be terminated by aborting its associated list, using
  :ref:`messages.abortList`. Thunderbird will then also stop searching for the
  requested messages.

* In order to abort a query even before any page has been returned (which includes
  the list id), the ``returnMessageListId`` property of the ``queryInfo`` object
  can be set. This changes the return value of :ref:`messages.query` and immediately
  returns the id of the associated message list.

