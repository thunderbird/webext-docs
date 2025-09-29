.. container:: sticky-sidebar

  ≡ identities API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

==============
identities API
==============

.. role:: permission

.. role:: value

.. role:: code

The identities API allows to manage the user's identities (each account can have multiple identities).

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`accountsIdentities`

   Create, modify or delete your mail account identities.

.. api-member::
   :name: :permission:`accountsRead`

   See your mail accounts, their identities and their folders.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`accountsRead` is required to use ``messenger.identities.*``.

.. rst-class:: api-main-section

Functions
=========

.. _identities.create:

create(accountId, details)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Create a new identity in the specified account.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``accountId``
      :type: (:ref:`accounts.MailAccountId`)

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

   - :permission:`accountsIdentities`
   - :permission:`accountsRead`

.. _identities.delete:

delete(identityId)
------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Attempts to delete the requested identity. Default identities cannot be deleted.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``identityId``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`accountsIdentities`
   - :permission:`accountsRead`

.. _identities.get:

get(identityId)
---------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Returns details of the requested identity, or :value:`null` if it doesn't exist.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``identityId``
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`identities.MailIdentity` or null

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.getDefault:

getDefault(accountId)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Returns the default identity for the requested account, or :value:`null` if it is not defined.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``accountId``
      :type: (:ref:`accounts.MailAccountId`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`identities.MailIdentity` or null

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.list:

list([accountId])
-----------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Returns the identities of the specified account, or all identities if no account is specified. Do not expect the returned identities to be in any specific order. Use :ref:`identities.getDefault` to get the default identity of an account.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``accountId``]
      :type: (:ref:`accounts.MailAccountId`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`identities.MailIdentity`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.setDefault:

setDefault(accountId, identityId)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Sets the default identity for the requested account.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``accountId``
      :type: (:ref:`accounts.MailAccountId`)

   .. api-member::
      :name: ``identityId``
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.update:

update(identityId, details)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

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

   - :permission:`accountsIdentities`
   - :permission:`accountsRead`

.. rst-class:: api-main-section

Events
======

.. _identities.onCreated:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

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

.. api-section-annotation-hack:: -- [Added in TB 91]

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

.. api-section-annotation-hack:: -- [Added in TB 91]

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

.. _identities.EncryptionCapabilities:

EncryptionCapabilities
----------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

.. api-header::
   :label: object

   .. _identities.EncryptionCapabilities.canEncrypt:

   .. api-member::
      :name: ``canEncrypt``
      :type: (boolean)

      Whether the encryption technology is configured to support message encryption.

   .. _identities.EncryptionCapabilities.canSign:

   .. api-member::
      :name: ``canSign``
      :type: (boolean)

      Whether the encryption technology is configured to support message signing.

.. _identities.MailIdentity:

MailIdentity
------------

.. api-section-annotation-hack:: -- [Added in TB 91]

.. api-header::
   :label: object

   .. _identities.MailIdentity.accountId:

   .. api-member::
      :name: [``accountId``]
      :type: (:ref:`accounts.MailAccountId`, optional)

      The id of the :ref:`accounts.MailAccount` this identity belongs to. The :value:`accountId` property is read-only.

   .. _identities.MailIdentity.composeHtml:

   .. api-member::
      :name: [``composeHtml``]
      :type: (boolean, optional)

      If the identity uses HTML as the default compose format.

   .. _identities.MailIdentity.email:

   .. api-member::
      :name: [``email``]
      :type: (string, optional)

      The user's email address as used when messages are sent from this identity.

   .. _identities.MailIdentity.encryptionCapabilities:

   .. api-member::
      :name: [``encryptionCapabilities``]
      :type: (object, optional)
      :annotation: -- [Added in TB 128]

      The encryption capabilities of this identity. Read only.

      .. api-member::
         :name: ``OpenPGP``
         :type: (:ref:`identities.EncryptionCapabilities`)
         :annotation: -- [Added in TB 128]

         The capabilities of this identity for the OpenPGP encryption technology.

      .. api-member::
         :name: ``S/MIME``
         :type: (:ref:`identities.EncryptionCapabilities`)
         :annotation: -- [Added in TB 128]

         The capabilities of this identity for the S/MIME encryption technology.

   .. _identities.MailIdentity.id:

   .. api-member::
      :name: [``id``]
      :type: (string, optional)

      A unique identifier for this identity. The :value:`id` property is read-only.

   .. _identities.MailIdentity.label:

   .. api-member::
      :name: [``label``]
      :type: (string, optional)

      A user-defined label for this identity.

   .. _identities.MailIdentity.name:

   .. api-member::
      :name: [``name``]
      :type: (string, optional)

      The user's name as used when messages are sent from this identity.

   .. _identities.MailIdentity.organization:

   .. api-member::
      :name: [``organization``]
      :type: (string, optional)

      The organization associated with this identity.

   .. _identities.MailIdentity.replyTo:

   .. api-member::
      :name: [``replyTo``]
      :type: (string, optional)

      The reply-to email address associated with this identity.

   .. _identities.MailIdentity.signature:

   .. api-member::
      :name: [``signature``]
      :type: (string, optional)

      The signature of the identity.

   .. _identities.MailIdentity.signatureIsPlainText:

   .. api-member::
      :name: [``signatureIsPlainText``]
      :type: (boolean, optional)

      If the signature should be interpreted as plain text or as HTML.
