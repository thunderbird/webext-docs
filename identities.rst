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

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _identities.permission.accounts^identities:

.. api-member::
   :name: :permission:`accountsIdentities`
   :refid: identities-permission-accounts-identities

   Create, modify or delete your mail account identities.

.. _identities.permission.accounts^read:

.. api-member::
   :name: :permission:`accountsRead`
   :refid: identities-permission-accounts-read

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

   .. _identities.create.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: identities-create-account-id
      :type: (:ref:`accounts.^mail^account^id`)

   .. _identities.create.details:

   .. api-member::
      :name: ``details``
      :refid: identities-create-details
      :type: (:ref:`identities.^mail^identity`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _identities.create.returns:

   .. api-member::
      :refid: identities-create-returns
      :type: :ref:`identities.^mail^identity`

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

   .. _identities.delete.identity^id:

   .. api-member::
      :name: ``identityId``
      :refid: identities-delete-identity-id
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

   .. _identities.get.identity^id:

   .. api-member::
      :name: ``identityId``
      :refid: identities-get-identity-id
      :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _identities.get.returns:

   .. api-member::
      :refid: identities-get-returns
      :type: :ref:`identities.^mail^identity` or null

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.get^default:

getDefault(accountId)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Returns the default identity for the requested account, or :value:`null` if it is not defined.

.. api-header::
   :label: Parameters

   .. _identities.get^default.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: identities-get-default-account-id
      :type: (:ref:`accounts.^mail^account^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _identities.get^default.returns:

   .. api-member::
      :refid: identities-get-default-returns
      :type: :ref:`identities.^mail^identity` or null

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.list:

list([accountId])
-----------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Returns the identities of the specified account, or all identities if no account is specified. Do not expect the returned identities to be in any specific order. Use :ref:`identities.get^default` to get the default identity of an account.

.. api-header::
   :label: Parameters

   .. _identities.list.account^id:

   .. api-member::
      :name: [``accountId``]
      :refid: identities-list-account-id
      :type: (:ref:`accounts.^mail^account^id`, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _identities.list.returns:

   .. api-member::
      :refid: identities-list-returns
      :type: array of :ref:`identities.^mail^identity`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.set^default:

setDefault(accountId, identityId)
---------------------------------

.. api-section-annotation-hack:: -- [Added in TB 91]

Sets the default identity for the requested account.

.. api-header::
   :label: Parameters

   .. _identities.set^default.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: identities-set-default-account-id
      :type: (:ref:`accounts.^mail^account^id`)

   .. _identities.set^default.identity^id:

   .. api-member::
      :name: ``identityId``
      :refid: identities-set-default-identity-id
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

   .. _identities.update.identity^id:

   .. api-member::
      :name: ``identityId``
      :refid: identities-update-identity-id
      :type: (string)

   .. _identities.update.details:

   .. api-member::
      :name: ``details``
      :refid: identities-update-details
      :type: (:ref:`identities.^mail^identity`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _identities.update.returns:

   .. api-member::
      :refid: identities-update-returns
      :type: :ref:`identities.^mail^identity`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsIdentities`
   - :permission:`accountsRead`

.. rst-class:: api-main-section

Events
======

.. _identities.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when a new identity has been created and added to an account. The event also fires for default identities that are created when a new account is added.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _identities.on^created.listener(identity^id, identity):

   .. api-member::
      :name: ``listener(identityId, identity)``
      :refid: identities-on-created-listener-identity-id-identity

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _identities.on^created.identity^id:

   .. api-member::
      :name: ``identityId``
      :refid: identities-on-created-identity-id
      :type: (string)

   .. _identities.on^created.identity:

   .. api-member::
      :name: ``identity``
      :refid: identities-on-created-identity
      :type: (:ref:`identities.^mail^identity`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when an identity has been removed from an account.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. _identities.on^deleted.listener(identity^id):

   .. api-member::
      :name: ``listener(identityId)``
      :refid: identities-on-deleted-listener-identity-id

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _identities.on^deleted.identity^id:

   .. api-member::
      :name: ``identityId``
      :refid: identities-on-deleted-identity-id
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _identities.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 91]

Fired when one or more properties of an identity have been modified. The returned :ref:`identities.^mail^identity` includes only the changed values.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. _identities.on^updated.listener(identity^id, changed^values):

   .. api-member::
      :name: ``listener(identityId, changedValues)``
      :refid: identities-on-updated-listener-identity-id-changed-values

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _identities.on^updated.identity^id:

   .. api-member::
      :name: ``identityId``
      :refid: identities-on-updated-identity-id
      :type: (string)

   .. _identities.on^updated.changed^values:

   .. api-member::
      :name: ``changedValues``
      :refid: identities-on-updated-changed-values
      :type: (:ref:`identities.^mail^identity`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Types
=====

.. _identities.^encryption^capabilities:

EncryptionCapabilities
----------------------

.. api-section-annotation-hack:: -- [Added in TB 128]

.. api-header::
   :label: object

   .. _identities.^encryption^capabilities.can^encrypt:

   .. api-member::
      :name: ``canEncrypt``
      :refid: identities-encryption-capabilities-can-encrypt
      :type: (boolean)

      Whether the encryption technology is configured to support message encryption.

   .. _identities.^encryption^capabilities.can^sign:

   .. api-member::
      :name: ``canSign``
      :refid: identities-encryption-capabilities-can-sign
      :type: (boolean)

      Whether the encryption technology is configured to support message signing.

.. _identities.^mail^identity:

MailIdentity
------------

.. api-section-annotation-hack:: -- [Added in TB 91]

.. api-header::
   :label: object

   .. _identities.^mail^identity.account^id:

   .. api-member::
      :name: [``accountId``]
      :refid: identities-mail-identity-account-id
      :type: (:ref:`accounts.^mail^account^id`, optional)

      The id of the :ref:`accounts.^mail^account` this identity belongs to. The :value:`accountId` property is read-only.

   .. _identities.^mail^identity.compose^html:

   .. api-member::
      :name: [``composeHtml``]
      :refid: identities-mail-identity-compose-html
      :type: (boolean, optional)

      If the identity uses HTML as the default compose format.

   .. _identities.^mail^identity.email:

   .. api-member::
      :name: [``email``]
      :refid: identities-mail-identity-email
      :type: (string, optional)

      The user's email address as used when messages are sent from this identity.

   .. _identities.^mail^identity.encryption^capabilities:

   .. api-member::
      :name: [``encryptionCapabilities``]
      :refid: identities-mail-identity-encryption-capabilities
      :type: (object, optional)
      :annotation: -- [Added in TB 128]

      The encryption capabilities of this identity. Read only.

      .. _identities.^mail^identity.encryption^capabilities.^open^p^g^p:

      .. api-member::
         :name: ``OpenPGP``
         :refid: identities-mail-identity-encryption-capabilities-open-p-g-p
         :type: (:ref:`identities.^encryption^capabilities`)
         :annotation: -- [Added in TB 128]

         The capabilities of this identity for the OpenPGP encryption technology.

      .. _identities.^mail^identity.encryption^capabilities.^s/^m^i^m^e:

      .. api-member::
         :name: ``S/MIME``
         :refid: identities-mail-identity-encryption-capabilities-s-m-i-m-e
         :type: (:ref:`identities.^encryption^capabilities`)
         :annotation: -- [Added in TB 128]

         The capabilities of this identity for the S/MIME encryption technology.

   .. _identities.^mail^identity.id:

   .. api-member::
      :name: [``id``]
      :refid: identities-mail-identity-id
      :type: (string, optional)

      A unique identifier for this identity. The :value:`id` property is read-only.

   .. _identities.^mail^identity.label:

   .. api-member::
      :name: [``label``]
      :refid: identities-mail-identity-label
      :type: (string, optional)

      A user-defined label for this identity.

   .. _identities.^mail^identity.name:

   .. api-member::
      :name: [``name``]
      :refid: identities-mail-identity-name
      :type: (string, optional)

      The user's name as used when messages are sent from this identity.

   .. _identities.^mail^identity.organization:

   .. api-member::
      :name: [``organization``]
      :refid: identities-mail-identity-organization
      :type: (string, optional)

      The organization associated with this identity.

   .. _identities.^mail^identity.reply^to:

   .. api-member::
      :name: [``replyTo``]
      :refid: identities-mail-identity-reply-to
      :type: (string, optional)

      The reply-to email address associated with this identity.

   .. _identities.^mail^identity.signature:

   .. api-member::
      :name: [``signature``]
      :refid: identities-mail-identity-signature
      :type: (string, optional)

      The signature of the identity.

   .. _identities.^mail^identity.signature^is^plain^text:

   .. api-member::
      :name: [``signatureIsPlainText``]
      :refid: identities-mail-identity-signature-is-plain-text
      :type: (boolean, optional)

      If the signature should be interpreted as plain text or as HTML.
