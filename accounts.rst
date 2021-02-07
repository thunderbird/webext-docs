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

.. _accounts.getDefault:

getDefault()
------------

.. api-section-annotation-hack:: -- [Added in TB 85, backported to TB 78.7.0]

Returns the default account, or null if it is not defined.

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

Returns the default identity for an account, or null if it is not defined.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
   

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
      :name: ``identities``
      :type: (array of :ref:`accounts.MailIdentity`)
      :annotation: -- [Added in TB 76]
      
      The identities associated with this account. The default identity is listed first, others in no particular order.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      The human-friendly name of this account.
   
   
   .. api-member::
      :name: ``type``
      :type: (string)
      
      What sort of account this is, e.g. ``imap``, ``nntp``, or ``pop3``.
   

.. _accounts.MailIdentity:

MailIdentity
------------

.. api-section-annotation-hack:: -- [Added in TB 76]

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
      
      The id of the :ref:`accounts.MailAccount` this identity belongs to.
   
   
   .. api-member::
      :name: ``composeHtml``
      :type: (boolean)
      :annotation: -- [Added in TB 85, backported to TB 78.7.0]
      
      Wether the identity uses HTML as the default compose format.
   
   
   .. api-member::
      :name: ``email``
      :type: (string)
      
      The user's email address as used when messages are sent from this identity.
   
   
   .. api-member::
      :name: ``id``
      :type: (string)
      
      A unique identifier for this identity.
   
   
   .. api-member::
      :name: ``label``
      :type: (string)
      
      A user-defined label for this identity.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      The user's name as used when messages are sent from this identity.
   
   
   .. api-member::
      :name: ``organization``
      :type: (string)
      
      The organization associated with this identity.
   
   
   .. api-member::
      :name: ``replyTo``
      :type: (string)
      
      The reply-to email address associated with this identity.
   
