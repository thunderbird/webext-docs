.. container:: sticky-sidebar

  ≡ accounts API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

============
accounts API
============

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

The accounts API provides access to the user's server accounts.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _accounts.permission.accounts^read:

.. api-member::
   :name: :permission:`accountsRead`
   :refid: accounts-permission-accounts-read
   :refname: accountsRead

   See your mail accounts, their identities and their folders.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`accountsRead` is required to use ``messenger.accounts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _accounts.get:

get(accountId, [includeSubFolders])
-----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Returns details of the requested account, or :value:`null` if it doesn't exist.

.. api-header::
   :label: Parameters

   .. _accounts.get.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: accounts-get-account-id
      :refname: accountId
      :type: (:ref:`accounts.^mail^account^id`)

   .. _accounts.get.include^sub^folders:

   .. api-member::
      :name: [``includeSubFolders``]
      :refid: accounts-get-include-sub-folders
      :refname: includeSubFolders
      :type: (boolean, optional)
      :annotation: -- [Added in TB 89]

      Specifies whether the :ref:`folders.^mail^folder` in the :value:`rootFolder` property of the returned :ref:`accounts.^mail^account` should populate its :value:`subFolders` property, and include all (nested!) subfolders. This also affects the deprecated :value:`folders` property of the returned :ref:`accounts.^mail^account`. Defaults to :value:`true`.

.. api-header::
   :label: Return type (`Promise`_)

   .. _accounts.get.returns:

   .. api-member::
      :refid: accounts-get-returns
      :refname: _returns
      :type: :ref:`accounts.^mail^account` or null
      :annotation: -- [Added in TB 91]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.get^default:

getDefault([includeSubFolders])
-------------------------------

.. api-section-annotation-hack:: -- [Added in TB 85]

Returns the default account, or :value:`null` if it is not defined.

.. api-header::
   :label: Parameters

   .. _accounts.get^default.include^sub^folders:

   .. api-member::
      :name: [``includeSubFolders``]
      :refid: accounts-get-default-include-sub-folders
      :refname: includeSubFolders
      :type: (boolean, optional)
      :annotation: -- [Added in TB 89]

      Specifies whether the :ref:`folders.^mail^folder` in the :value:`rootFolder` property of the default :ref:`accounts.^mail^account` should populate its :value:`subFolders` property, and include all (nested!) subfolders. This also affects the deprecated :value:`folders` property of the default :ref:`accounts.^mail^account`. Defaults to :value:`true`

.. api-header::
   :label: Return type (`Promise`_)

   .. _accounts.get^default.returns:

   .. api-member::
      :refid: accounts-get-default-returns
      :refname: _returns
      :type: :ref:`accounts.^mail^account` or null
      :annotation: -- [Added in TB 91]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.get^default^identity:

getDefaultIdentity(accountId)
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 85]

Returns the default identity for an account, or :value:`null` if it is not defined.

.. api-header::
   :label: Parameters

   .. _accounts.get^default^identity.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: accounts-get-default-identity-account-id
      :refname: accountId
      :type: (:ref:`accounts.^mail^account^id`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _accounts.get^default^identity.returns:

   .. api-member::
      :refid: accounts-get-default-identity-returns
      :refname: _returns
      :type: :ref:`identities.^mail^identity` or null
      :annotation: -- [Added in TB 89]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.list:

list([includeSubFolders])
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Returns all mail accounts. They will be returned in the same order as used in Thunderbird's folder pane.

.. api-header::
   :label: Parameters

   .. _accounts.list.include^sub^folders:

   .. api-member::
      :name: [``includeSubFolders``]
      :refid: accounts-list-include-sub-folders
      :refname: includeSubFolders
      :type: (boolean, optional)
      :annotation: -- [Added in TB 89]

      Specifies whether the :ref:`folders.^mail^folder` in the :value:`rootFolder` property of each found :ref:`accounts.^mail^account` should populate its :value:`subFolders` property, and include all (nested!) subfolders. This also affects the deprecated :value:`folders` property of each found :ref:`accounts.^mail^account`. Defaults to :value:`true`.

.. api-header::
   :label: Return type (`Promise`_)

   .. _accounts.list.returns:

   .. api-member::
      :refid: accounts-list-returns
      :refname: _returns
      :type: array of :ref:`accounts.^mail^account`
      :annotation: -- [Added in TB 91]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.set^default^identity:

setDefaultIdentity(accountId, identityId)
-----------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 76]

Sets the default identity for an account.

.. api-header::
   :label: Parameters

   .. _accounts.set^default^identity.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: accounts-set-default-identity-account-id
      :refname: accountId
      :type: (:ref:`accounts.^mail^account^id`)

   .. _accounts.set^default^identity.identity^id:

   .. api-member::
      :name: ``identityId``
      :refid: accounts-set-default-identity-identity-id
      :refname: identityId
      :type: (string)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Events
======

.. _accounts.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 98]

Fired when a new account has been created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _accounts.on^created.listener(account^id, account):

   .. api-member::
      :name: ``listener(accountId, account)``
      :refid: accounts-on-created-listener-account-id-account
      :refname: listener(accountId, account)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _accounts.on^created.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: accounts-on-created-account-id
      :refname: accountId
      :type: (:ref:`accounts.^mail^account^id`)

   .. _accounts.on^created.account:

   .. api-member::
      :name: ``account``
      :refid: accounts-on-created-account
      :refname: account
      :type: (:ref:`accounts.^mail^account`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 98]

Fired when an account has been removed.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. _accounts.on^deleted.listener(account^id):

   .. api-member::
      :name: ``listener(accountId)``
      :refid: accounts-on-deleted-listener-account-id
      :refname: listener(accountId)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _accounts.on^deleted.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: accounts-on-deleted-account-id
      :refname: accountId
      :type: (:ref:`accounts.^mail^account^id`)

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _accounts.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 98]

Fired when a property of an account has been modified. Folders and identities of accounts are not monitored by this event, use the dedicated folder and identity events instead. A changed :value:`defaultIdentity` is reported only after a different identity has been assigned as default identity, but not after a property of the default identity has been changed.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. _accounts.on^updated.listener(account^id, changed^values):

   .. api-member::
      :name: ``listener(accountId, changedValues)``
      :refid: accounts-on-updated-listener-account-id-changed-values
      :refname: listener(accountId, changedValues)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _accounts.on^updated.account^id:

   .. api-member::
      :name: ``accountId``
      :refid: accounts-on-updated-account-id
      :refname: accountId
      :type: (:ref:`accounts.^mail^account^id`)

   .. _accounts.on^updated.changed^values:

   .. api-member::
      :name: ``changedValues``
      :refid: accounts-on-updated-changed-values
      :refname: changedValues
      :type: (object)

      .. _accounts.on^updated.changed^values.default^identity:

      .. api-member::
         :name: ``defaultIdentity``
         :refid: accounts-on-updated-changed-values-default-identity
         :refname: defaultIdentity
         :type: (:ref:`identities.^mail^identity`)

         The default identity of this account.

      .. _accounts.on^updated.changed^values.name:

      .. api-member::
         :name: ``name``
         :refid: accounts-on-updated-changed-values-name
         :refname: name
         :type: (string)

         The human-friendly name of this account.

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. rst-class:: api-main-section

Types
=====

.. _accounts.^extension^mail^account^type:

ExtensionMailAccountType
------------------------

.. api-section-annotation-hack:: -- [Added in TB 130]

The type of an account which was added by an extension. For the time being there is no guarantee for account types added by extensions to always work as expected.

.. api-header::
   :label: string

.. _accounts.^mail^account:

MailAccount
-----------

.. api-section-annotation-hack:: -- [Added in TB 88]

An object describing a mail account, as returned for example by the :ref:`accounts.list` and :ref:`accounts.get` methods.

.. api-header::
   :label: object

   .. _accounts.^mail^account.folders:

   .. api-member::
      :name: ``folders``
      :refid: accounts-mail-account-folders
      :refname: folders
      :type: (array of :ref:`folders.^mail^folder` or null)

      The folders for this account. The property may be :value:`null`, if inclusion of folders had not been requested.

   .. _accounts.^mail^account.id:

   .. api-member::
      :name: ``id``
      :refid: accounts-mail-account-id
      :refname: id
      :type: (:ref:`accounts.^mail^account^id`)

      A unique identifier for this account.

   .. _accounts.^mail^account.identities:

   .. api-member::
      :name: ``identities``
      :refid: accounts-mail-account-identities
      :refname: identities
      :type: (array of :ref:`identities.^mail^identity`)

      The identities associated with this account. The default identity is listed first, others in no particular order.

   .. _accounts.^mail^account.name:

   .. api-member::
      :name: ``name``
      :refid: accounts-mail-account-name
      :refname: name
      :type: (string)

      The human-friendly name of this account.

   .. _accounts.^mail^account.root^folder:

   .. api-member::
      :name: ``rootFolder``
      :refid: accounts-mail-account-root-folder
      :refname: rootFolder
      :type: (:ref:`folders.^mail^folder`)
      :annotation: -- [Added in TB 121]

      The root folder associated with this account.

   .. _accounts.^mail^account.type:

   .. api-member::
      :name: ``type``
      :refid: accounts-mail-account-type
      :refname: type
      :type: (:ref:`accounts.^native^mail^account^type` or :ref:`accounts.^extension^mail^account^type`)

      What sort of account this is. Either one of the natively supported account types, or an account type added by an extension.

.. _accounts.^mail^account^id:

MailAccountId
-------------

.. api-section-annotation-hack:: -- [Added in TB 121]

A unique id representing a :ref:`accounts.^mail^account`.

.. api-header::
   :label: string

.. _accounts.^native^mail^account^type:

NativeMailAccountType
---------------------

.. api-section-annotation-hack:: -- [Added in TB 130]

The type of an account natively supported by Thunderbird.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _accounts.^native^mail^account^type.ews:

         .. api-member::
            :name: :value:`ews`
            :refid: accounts-native-mail-account-type-ews
            :refname: ews
            :annotation: -- [Added in TB 142]

            An Exchange Web Services (EWS) account.

         .. _accounts.^native^mail^account^type.imap:

         .. api-member::
            :name: :value:`imap`
            :refid: accounts-native-mail-account-type-imap
            :refname: imap

            An IMAP account.

         .. _accounts.^native^mail^account^type.nntp:

         .. api-member::
            :name: :value:`nntp`
            :refid: accounts-native-mail-account-type-nntp
            :refname: nntp

            An NNTP account.

         .. _accounts.^native^mail^account^type.none:

         .. api-member::
            :name: :value:`none`
            :refid: accounts-native-mail-account-type-none
            :refname: none

            A local account for managing local folders.

         .. _accounts.^native^mail^account^type.pop3:

         .. api-member::
            :name: :value:`pop3`
            :refid: accounts-native-mail-account-type-pop3
            :refname: pop3

            A POP3 account.

         .. _accounts.^native^mail^account^type.rss:

         .. api-member::
            :name: :value:`rss`
            :refid: accounts-native-mail-account-type-rss
            :refname: rss

            A Feed account.
