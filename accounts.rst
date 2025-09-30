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

The accounts API provides access to the user's server accounts.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`accountsRead`

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

   .. api-member::
      :name: ``accountId``
      :type: (:ref:`accounts.^mail^account^id`)

   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 89]

      Specifies whether the :ref:`folders.^mail^folder` in the :value:`rootFolder` property of the returned :ref:`accounts.^mail^account` should populate its :value:`subFolders` property, and include all (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
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

   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 89]

      Specifies whether the :ref:`folders.^mail^folder` in the :value:`rootFolder` property of the default :ref:`accounts.^mail^account` should populate its :value:`subFolders` property, and include all (nested!) subfolders. Defaults to :value:`false`

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`accounts.^mail^account` or null
      :annotation: -- [Added in TB 91]

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

   .. api-member::
      :name: [``includeSubFolders``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 89]

      Specifies whether the :ref:`folders.^mail^folder` in the :value:`rootFolder` property of each found :ref:`accounts.^mail^account` should populate its :value:`subFolders` property, and include all (nested!) subfolders. Defaults to :value:`false`.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`accounts.^mail^account`
      :annotation: -- [Added in TB 91]

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

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

   .. api-member::
      :name: ``listener(accountId, account)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``accountId``
      :type: (:ref:`accounts.^mail^account^id`)

   .. api-member::
      :name: ``account``
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

   .. api-member::
      :name: ``listener(accountId)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``accountId``
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

   .. api-member::
      :name: ``listener(accountId, changedValues)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``accountId``
      :type: (:ref:`accounts.^mail^account^id`)

   .. api-member::
      :name: ``changedValues``
      :type: (object)

      .. api-member::
         :name: ``defaultIdentity``
         :type: (:ref:`identities.^mail^identity`)

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

   .. _accounts.^mail^account.id:

   .. api-member::
      :name: ``id``
      :type: (:ref:`accounts.^mail^account^id`)

      A unique identifier for this account.

   .. _accounts.^mail^account.identities:

   .. api-member::
      :name: ``identities``
      :type: (array of :ref:`identities.^mail^identity`)

      The identities associated with this account. The default identity is listed first, others in no particular order.

   .. _accounts.^mail^account.name:

   .. api-member::
      :name: ``name``
      :type: (string)

      The human-friendly name of this account.

   .. _accounts.^mail^account.root^folder:

   .. api-member::
      :name: ``rootFolder``
      :type: (:ref:`folders.^mail^folder`)
      :annotation: -- [Added in TB 121]

      The root folder associated with this account.

   .. _accounts.^mail^account.type:

   .. api-member::
      :name: ``type``
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

         .. api-member::
            :name: :value:`imap`

         .. api-member::
            :name: :value:`local`

         .. api-member::
            :name: :value:`nntp`

         .. api-member::
            :name: :value:`pop3`

         .. api-member::
            :name: :value:`rss`
