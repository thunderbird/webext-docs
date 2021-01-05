.. _accounts_api:

========
accounts
========

The accounts API first appeared in Thunderbird 66 (see `bug 1488176`__).

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1488176

.. role:: permission

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`accountsRead`

   See your mail accounts and their folders

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`accountsRead` is required to use ``accounts``.

.. rst-class:: api-main-section

Functions
=========

.. _accounts.list:

list()
------

.. api-section-annotation-hack:: 

Returns all mail accounts.

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`accounts.MailAccount`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.get:

get(accountId)
--------------

.. api-section-annotation-hack:: 

Returns details of the requested account, or null if it doesn't exist.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`accounts.MailAccount`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Types
=====

.. _accounts.MailAccount:

MailAccount
-----------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``folders``
      :type: (array of :ref:`folders.MailFolder`)
      
      The folders for this account.
   
   
   .. api-member::
      :name: ``id``
      :type: (string)
      
      A unique identifier for this account.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      The human-friendly name of this account.
   
   
   .. api-member::
      :name: ``type``
      :type: (string)
      
      What sort of account this is, e.g. ``imap``, ``nntp``, or ``pop3``.
   
