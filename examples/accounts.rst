Extracting IMAP accounts
------------------------

The following code can be used to find all IMAP accounts

.. code-block:: javascript

  // Get all accounts.
  let accounts = await messenger.accounts.list();
  
  // Filter on accounts with type "imap".
  let imapAccounts = accounts.filter(account => account.type == "imap")