Using folder and message types
==============================

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
