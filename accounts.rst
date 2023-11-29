.. _accounts_api:

============
accounts API
============

The accounts API first appeared in Thunderbird 66.

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`accountsRead`

   See your mail accounts, their identities and their folders

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`accountsRead` is required to use ``messenger.accounts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _accounts.get:

get(accountId, [includeFolders])
--------------------------------

.. api-section-annotation-hack:: 

Returns details of the requested account, or :value:`null` if it doesn't exist.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``accountId``
      :type: (:ref:`accounts.MailAccountId`)
   
   
   .. api-member::
      :name: [``includeFolders``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 91]
      
      Specifies whether the returned :ref:`accounts.MailAccount` object should included the account's folders. Defaults to :value:`true`.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`accounts.MailAccount`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.getDefault:

getDefault([includeFolders])
----------------------------

.. api-section-annotation-hack:: -- [Added in TB 85, backported to TB 78.7.0]

Returns the default account, or :value:`null` if it is not defined.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``includeFolders``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 91]
      
      Specifies whether the returned :ref:`accounts.MailAccount` object should included the account's folders. Defaults to :value:`true`.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`accounts.MailAccount`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.list:

list([includeFolders])
----------------------

.. api-section-annotation-hack:: 

Returns all mail accounts. They will be returned in the same order as used in Thunderbird's folder pane.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``includeFolders``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 91]
      
      Specifies whether the returned :ref:`accounts.MailAccount` objects should included their account's folders. Defaults to :value:`true`.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`accounts.MailAccount`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Events
======

.. _accounts.onCreated:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 98]

Fired when a new account has been created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   
   .. api-member::
      :name: ``listener(accountId, account)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``accountId``
      :type: (:ref:`accounts.MailAccountId`)
   
   
   .. api-member::
      :name: ``account``
      :type: (:ref:`accounts.MailAccount`)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.onDeleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 98]

Fired when an account has been removed.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   
   .. api-member::
      :name: ``listener(accountId)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``accountId``
      :type: (:ref:`accounts.MailAccountId`)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 98]

Fired when a property of an account has been modified. Folders and identities of accounts are not monitored by this event, use the dedicated folder and identity events instead. A changed ``defaultIdentity`` is reported only after a different identity has been assigned as default identity, but not after a property of the default identity has been changed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   
   .. api-member::
      :name: ``listener(accountId, changedValues)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``accountId``
      :type: (:ref:`accounts.MailAccountId`)
   
   
   .. api-member::
      :name: ``changedValues``
      :type: (object)
      
      .. api-member::
         :name: ``defaultIdentity``
         :type: (:ref:`identities.MailIdentity`)
         
         The default identity of this account.
      
      
      .. api-member::
         :name: ``name``
         :type: (string)
         
         The human-friendly name of this account.
      
   

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

An object describing a mail account, as returned for example by the :ref:`accounts.list` and :ref:`accounts.get` methods. The ``folders`` property is only included if requested.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``id``
      :type: (:ref:`accounts.MailAccountId`)
      
      A unique identifier for this account.
   
   
   .. api-member::
      :name: ``identities``
      :type: (array of :ref:`identities.MailIdentity`)
      :annotation: -- [Added in TB 76]
      
      The identities associated with this account. The default identity is listed first, others in no particular order.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      The human-friendly name of this account.
   
   
   .. api-member::
      :name: ``type``
      :type: (string)
      
      What sort of account this is, e.g. :value:`imap`, :value:`nntp`, or :value:`pop3`.
   
   
   .. api-member::
      :name: [``rootFolder``]
      :type: (:ref:`folders.MailFolder`, optional)
      
      The root folder associated with this account.
   

.. _accounts.MailAccountId:

MailAccountId
-------------

.. api-section-annotation-hack:: 

A unique id representing a :ref:`accounts.MailAccount`.

.. api-header::
   :label: string
