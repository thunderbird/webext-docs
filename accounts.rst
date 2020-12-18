========
accounts
========

The accounts API first appeared in Thunderbird 66 (see `bug 1488176`__).

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1488176

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: ``accountsRead``

   See your mail accounts and their folders

.. rst-class:: api-permission-info

.. note::

  The permission ``accountsRead`` is required to use ``accounts``.

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
      :name: 
      :type: array of :ref:`accounts.MailAccount`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

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
      :annotation: 
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`accounts.MailAccount`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

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
      :annotation: 
   
   
   .. api-member::
      :name: ``identityId``
      :type: (string)
      :annotation: 
   

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
      :annotation: 
      
      The folders for this account.
   
   
   .. api-member::
      :name: ``id``
      :type: (string)
      :annotation: 
      
      A unique identifier for this account.
   
   
   .. api-member::
      :name: ``identities``
      :type: (array of :ref:`accounts.MailIdentity`)
      :annotation: -- [Added in TB 76]
      
      The identities associated with this account. The default identity is listed first, others in no particular order.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      :annotation: 
      
      The human-friendly name of this account.
   
   
   .. api-member::
      :name: ``type``
      :type: (string)
      :annotation: 
      
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
      :annotation: 
      
      The id of the :ref:`accounts.MailAccount` this identity belongs to.
   
   
   .. api-member::
      :name: ``email``
      :type: (string)
      :annotation: 
      
      The user's email address as used when messages are sent from this identity.
   
   
   .. api-member::
      :name: ``id``
      :type: (string)
      :annotation: 
      
      A unique identifier for this identity.
   
   
   .. api-member::
      :name: ``label``
      :type: (string)
      :annotation: 
      
      A user-defined label for this identity.
   
   
   .. api-member::
      :name: ``name``
      :type: (string)
      :annotation: 
      
      The user's name as used when messages are sent from this identity.
   
   
   .. api-member::
      :name: ``organization``
      :type: (string)
      :annotation: 
      
      The organization associated with this identity.
   
   
   .. api-member::
      :name: ``replyTo``
      :type: (string)
      :annotation: 
      
      The reply-to email address associated with this identity.
   
