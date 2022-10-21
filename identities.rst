.. _identities_api:

==========
identities
==========

The identities API first appeared in Thunderbird 91.


.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`accountsIdentities`

   Create, modify or delete your mail account identities

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`accountsRead` is required to use ``identities``.

.. rst-class:: api-main-section

Functions
=========

.. _identities.list:

list([accountId])
-----------------

.. api-section-annotation-hack:: 

Returns the identities of the specified account, or all identities if no account is specified. Do not expect the returned identities to be in any specific order. Use :ref:`identities.getDefault` to get the default identity of an account.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``accountId``]
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`identities.MailIdentity`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.get:

get(identityId)
---------------

.. api-section-annotation-hack:: 

Returns details of the requested identity, or :value:`null` if it doesn't exist.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``identityId``
      :type: (string)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`identities.MailIdentity`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.create:

create(accountId, details)
--------------------------

.. api-section-annotation-hack:: 

Create a new identity in the specified account.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``accountId``
      :type: (string)
   
   
   .. api-member::
      :name: ``details``
      :type: (:ref:`identities.MailIdentity`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`identities.MailIdentity`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`accountsIdentities`

.. _identities.delete:

delete(identityId)
------------------

.. api-section-annotation-hack:: 

Attempts to delete the requested identity. Default identities cannot be deleted.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``identityId``
      :type: (string)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`accountsIdentities`

.. _identities.update:

update(identityId, details)
---------------------------

.. api-section-annotation-hack:: 

Updates the details of an identity.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``identityId``
      :type: (string)
   
   
   .. api-member::
      :name: ``details``
      :type: (:ref:`identities.MailIdentity`)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`identities.MailIdentity`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`
   - :permission:`accountsIdentities`

.. _identities.getDefault:

getDefault(accountId)
---------------------

.. api-section-annotation-hack:: 

Returns the default identity for the requested account, or :value:`null` if it is not defined.

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

.. _identities.setDefault:

setDefault(accountId, identityId)
---------------------------------

.. api-section-annotation-hack:: 

Sets the default identity for the requested account.

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

.. rst-class:: api-main-section

Events
======

.. _identities.onCreated:

onCreated
---------

.. api-section-annotation-hack:: 

Fired when a new identity has been created and added to an account. The event also fires for default identities that are created when a new account is added.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   
   .. api-member::
      :name: ``listener(identityId, identity)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``identityId``
      :type: (string)
   
   
   .. api-member::
      :name: ``identity``
      :type: (:ref:`identities.MailIdentity`)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.onDeleted:

onDeleted
---------

.. api-section-annotation-hack:: 

Fired when an identity has been removed from an account.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   
   .. api-member::
      :name: ``listener(identityId)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``identityId``
      :type: (string)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: 

Fired when one or more properties of an identity have been modified. The returned :ref:`identities.MailIdentity` includes only the changed values.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   
   .. api-member::
      :name: ``listener(identityId, changedValues)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``identityId``
      :type: (string)
   
   
   .. api-member::
      :name: ``changedValues``
      :type: (:ref:`identities.MailIdentity`)
   

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Types
=====

.. _identities.MailIdentity:

MailIdentity
------------

.. api-section-annotation-hack:: -- [Added in TB 76]

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``accountId``]
      :type: (string)
      
      The id of the :ref:`accounts.MailAccount` this identity belongs to. The ``accountId`` property is read-only.
   
   
   .. api-member::
      :name: [``composeHtml``]
      :type: (boolean)
      :annotation: -- [Added in TB 85, backported to TB 78.7.0]
      
      If the identity uses HTML as the default compose format.
   
   
   .. api-member::
      :name: [``email``]
      :type: (string)
      
      The user's email address as used when messages are sent from this identity.
   
   
   .. api-member::
      :name: [``id``]
      :type: (string)
      
      A unique identifier for this identity. The ``id`` property is read-only.
   
   
   .. api-member::
      :name: [``label``]
      :type: (string)
      
      A user-defined label for this identity.
   
   
   .. api-member::
      :name: [``name``]
      :type: (string)
      
      The user's name as used when messages are sent from this identity.
   
   
   .. api-member::
      :name: [``organization``]
      :type: (string)
      
      The organization associated with this identity.
   
   
   .. api-member::
      :name: [``replyTo``]
      :type: (string)
      
      The reply-to email address associated with this identity.
   
   
   .. api-member::
      :name: [``signature``]
      :type: (string)
      :annotation: -- [Added in TB 91]
      
      The signature of the identity.
   
   
   .. api-member::
      :name: [``signatureIsPlainText``]
      :type: (boolean)
      :annotation: -- [Added in TB 91]
      
      If the signature should be interpreted as plain text or as HTML.
   
