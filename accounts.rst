.. _accounts_api:

========
accounts
========

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

.. _accounts.list:

list([includeFolders])
----------------------

.. api-section-annotation-hack:: 

Returns all mail accounts.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``includeFolders``]
      :type: (boolean)
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

.. _accounts.get:

get(accountId, [includeFolders])
--------------------------------

.. api-section-annotation-hack:: 

Returns details of the requested account, or :value:`null` if it doesn't exist.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
   
   
   .. api-member::
      :name: [``includeFolders``]
      :type: (boolean)
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
      :type: (boolean)
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

.. _accounts.setDefaultIdentity:

setDefaultIdentity(accountId, identityId)
-----------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 76]

Sets the default identity for an account.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
   
   
   .. api-member::
      :name: ``identityId``
      :type: (string)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.getDefaultIdentity:

getDefaultIdentity(accountId)
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 85, backported to TB 78.7.0]

Returns the default identity for an account, or :value:`null` if it is not defined.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`identities.MailIdentity`
   
   
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

An object describing a mail account, as returned for example by the :ref:`accounts.list` and :ref:`accounts.get` methods. The ``folders`` property is only included if requested.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``id``
      :type: (string)
      
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
      :name: [``folders``]
      :type: (array of :ref:`folders.MailFolder`)
      
      The folders for this account are only included if requested.
   
