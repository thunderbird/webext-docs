.. container:: sticky-sidebar

  ≡ permissions API

  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

===============
permissions API
===============

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The permissions API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/permissions>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

.. rst-class:: api-main-section

Functions
=========

.. _permissions.contains:

contains(permissions)
---------------------

.. api-section-annotation-hack:: -- [Added in TB 55]

Check if the extension has the given permissions.

.. api-header::
   :label: Parameters

   .. _permissions.contains.permissions:

   .. api-member::
      :name: ``permissions``
      :refid: permissions-contains-permissions
      :refname: permissions
      :type: (:ref:`permissions.^any^permissions`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _permissions.contains.returns:

   .. api-member::
      :refid: permissions-contains-returns
      :refname: _returns
      :type: boolean

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _permissions.get^all:

getAll()
--------

.. api-section-annotation-hack:: -- [Added in TB 55]

Get a list of all the extension's permissions.

.. api-header::
   :label: Return type (`Promise`_)

   .. _permissions.get^all.returns:

   .. api-member::
      :refid: permissions-get-all-returns
      :refname: _returns
      :type: :ref:`permissions.^any^permissions`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _permissions.remove:

remove(permissions)
-------------------

.. api-section-annotation-hack:: -- [Added in TB 55]

Relinquish the given permissions.

.. api-header::
   :label: Parameters

   .. _permissions.remove.permissions:

   .. api-member::
      :name: ``permissions``
      :refid: permissions-remove-permissions
      :refname: permissions
      :type: (:ref:`permissions.^permissions`)

.. _permissions.request:

request(permissions)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 55]

Request the given permissions.

.. note::

   It's not possible to request permissions from within DevTools (`bug 1796933 <https://bugzil.la/1796933>`__).

.. note::

   Before version 101, permissions cannot be requested from a sidebar document (`bug 1493396 <https://bugzil.la/1493396>`__).

.. note::

   Before version 75, permissions cannot be requested from popup panels (see `bug 1432083 <https://bugzil.la/1432083>`__).

.. note::

   Before version 61, permissions cannot be requested from options pages embedded in :code:`about:addons` (see `bug 1382953 <https://bugzil.la/1382953>`__).

.. api-header::
   :label: Parameters

   .. _permissions.request.permissions:

   .. api-member::
      :name: ``permissions``
      :refid: permissions-request-permissions
      :refname: permissions
      :type: (:ref:`permissions.^permissions`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _permissions.request.returns:

   .. api-member::
      :refid: permissions-request-returns
      :refname: _returns
      :type: boolean

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _permissions.on^added:

onAdded
-------

.. api-section-annotation-hack:: -- [Added in TB 77]

Fired when the extension acquires new permissions.

.. api-header::
   :label: Parameters for onAdded.addListener(listener)

   .. _permissions.on^added.listener(permissions):

   .. api-member::
      :name: ``listener(permissions)``
      :refid: permissions-on-added-listener-permissions
      :refname: listener(permissions)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _permissions.on^added.permissions:

   .. api-member::
      :name: ``permissions``
      :refid: permissions-on-added-permissions
      :refname: permissions
      :type: (:ref:`permissions.^permissions`)

.. _permissions.on^removed:

onRemoved
---------

.. api-section-annotation-hack:: -- [Added in TB 77]

Fired when permissions are removed from the extension.

.. api-header::
   :label: Parameters for onRemoved.addListener(listener)

   .. _permissions.on^removed.listener(permissions):

   .. api-member::
      :name: ``listener(permissions)``
      :refid: permissions-on-removed-listener-permissions
      :refname: listener(permissions)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _permissions.on^removed.permissions:

   .. api-member::
      :name: ``permissions``
      :refid: permissions-on-removed-permissions
      :refname: permissions
      :type: (:ref:`permissions.^permissions`)

.. rst-class:: api-main-section

Types
=====

.. _permissions.^any^permissions:

AnyPermissions
--------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _permissions.^any^permissions.data_collection:

   .. api-member::
      :name: [``data_collection``]
      :refid: permissions-any-permissions-data-collection
      :refname: data_collection
      :type: (array of :ref:`permissions.^optional^data^collection^permission`, optional)

   .. _permissions.^any^permissions.origins:

   .. api-member::
      :name: [``origins``]
      :refid: permissions-any-permissions-origins
      :refname: origins
      :type: (array of :ref:`permissions.^match^pattern`, optional)

   .. _permissions.^any^permissions.permissions:

   .. api-member::
      :name: [``permissions``]
      :refid: permissions-any-permissions-permissions
      :refname: permissions
      :type: (array of :ref:`permissions.^permission` or :ref:`permissions.^optional^only^permission`, optional)

.. _permissions.^common^data^collection^permission:

CommonDataCollectionPermission
------------------------------

.. api-section-annotation-hack:: 

.. warning::

   Unlike Firefox, Thunderbird does not use the built-in onboarding flow that prompts users to opt into data collection. In Thunderbird, add-ons must request consent explicitly, for example by adding a checkbox on the options page or by showing a popup. The application does not provide an automatic prompt.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _permissions.^common^data^collection^permission.authentication^info:

         .. api-member::
            :name: :value:`authenticationInfo`
            :refid: permissions-common-data-collection-permission-authentication-info
            :refname: authenticationInfo

         .. _permissions.^common^data^collection^permission.bookmarks^info:

         .. api-member::
            :name: :value:`bookmarksInfo`
            :refid: permissions-common-data-collection-permission-bookmarks-info
            :refname: bookmarksInfo

         .. _permissions.^common^data^collection^permission.browsing^activity:

         .. api-member::
            :name: :value:`browsingActivity`
            :refid: permissions-common-data-collection-permission-browsing-activity
            :refname: browsingActivity

         .. _permissions.^common^data^collection^permission.financial^and^payment^info:

         .. api-member::
            :name: :value:`financialAndPaymentInfo`
            :refid: permissions-common-data-collection-permission-financial-and-payment-info
            :refname: financialAndPaymentInfo

         .. _permissions.^common^data^collection^permission.health^info:

         .. api-member::
            :name: :value:`healthInfo`
            :refid: permissions-common-data-collection-permission-health-info
            :refname: healthInfo

         .. _permissions.^common^data^collection^permission.location^info:

         .. api-member::
            :name: :value:`locationInfo`
            :refid: permissions-common-data-collection-permission-location-info
            :refname: locationInfo

         .. _permissions.^common^data^collection^permission.personal^communications:

         .. api-member::
            :name: :value:`personalCommunications`
            :refid: permissions-common-data-collection-permission-personal-communications
            :refname: personalCommunications

         .. _permissions.^common^data^collection^permission.personally^identifying^info:

         .. api-member::
            :name: :value:`personallyIdentifyingInfo`
            :refid: permissions-common-data-collection-permission-personally-identifying-info
            :refname: personallyIdentifyingInfo

         .. _permissions.^common^data^collection^permission.search^terms:

         .. api-member::
            :name: :value:`searchTerms`
            :refid: permissions-common-data-collection-permission-search-terms
            :refname: searchTerms

         .. _permissions.^common^data^collection^permission.website^activity:

         .. api-member::
            :name: :value:`websiteActivity`
            :refid: permissions-common-data-collection-permission-website-activity
            :refname: websiteActivity

         .. _permissions.^common^data^collection^permission.website^content:

         .. api-member::
            :name: :value:`websiteContent`
            :refid: permissions-common-data-collection-permission-website-content
            :refname: websiteContent

.. _permissions.^match^pattern:

MatchPattern
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _permissions.^match^pattern.<all_urls>:

         .. api-member::
            :name: :value:`<all_urls>`
            :refid: permissions-match-pattern-all-urls
            :refname: <all_urls>

*or*

.. api-header::
   :label: :ref:`permissions.^match^pattern^restricted`

*or*

.. api-header::
   :label: :ref:`permissions.^match^pattern^unestricted`

.. _permissions.^match^pattern^restricted:

MatchPatternRestricted
----------------------

.. api-section-annotation-hack:: 

Same as MatchPattern above, but excludes <all_urls>

.. api-header::
   :label: string

*or*

.. api-header::
   :label: string

.. _permissions.^match^pattern^unestricted:

MatchPatternUnestricted
-----------------------

.. api-section-annotation-hack:: 

Mostly unrestricted match patterns for privileged add-ons. This should technically be rejected for unprivileged add-ons, but, reasons. The MatchPattern class will still refuse privileged schemes for those extensions.

.. api-header::
   :label: string

.. _permissions.^optional^data^collection^permission:

OptionalDataCollectionPermission
--------------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: :ref:`permissions.^common^data^collection^permission`

*or*

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _permissions.^optional^data^collection^permission.technical^and^interaction:

         .. api-member::
            :name: :value:`technicalAndInteraction`
            :refid: permissions-optional-data-collection-permission-technical-and-interaction
            :refname: technicalAndInteraction

.. _permissions.^optional^only^permission:

OptionalOnlyPermission
----------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         No supported values.

.. _permissions.^optional^permission:

OptionalPermission
------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: :ref:`permissions.^optional^permission^no^prompt`

*or*

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _permissions.^optional^permission.accounts^folders:

         .. api-member::
            :name: :value:`accountsFolders`
            :refid: permissions-optional-permission-accounts-folders
            :refname: accountsFolders
            :annotation: -- [Added in TB 68]

         .. _permissions.^optional^permission.accounts^identities:

         .. api-member::
            :name: :value:`accountsIdentities`
            :refid: permissions-optional-permission-accounts-identities
            :refname: accountsIdentities
            :annotation: -- [Added in TB 91]

         .. _permissions.^optional^permission.accounts^read:

         .. api-member::
            :name: :value:`accountsRead`
            :refid: permissions-optional-permission-accounts-read
            :refname: accountsRead
            :annotation: -- [Added in TB 66]

         .. _permissions.^optional^permission.address^books:

         .. api-member::
            :name: :value:`addressBooks`
            :refid: permissions-optional-permission-address-books
            :refname: addressBooks
            :annotation: -- [Added in TB 64]

         .. _permissions.^optional^permission.browser^settings:

         .. api-member::
            :name: :value:`browserSettings`
            :refid: permissions-optional-permission-browser-settings
            :refname: browserSettings

         .. _permissions.^optional^permission.browsing^data:

         .. api-member::
            :name: :value:`browsingData`
            :refid: permissions-optional-permission-browsing-data
            :refname: browsingData

         .. _permissions.^optional^permission.clipboard^read:

         .. api-member::
            :name: :value:`clipboardRead`
            :refid: permissions-optional-permission-clipboard-read
            :refname: clipboardRead

         .. _permissions.^optional^permission.clipboard^write:

         .. api-member::
            :name: :value:`clipboardWrite`
            :refid: permissions-optional-permission-clipboard-write
            :refname: clipboardWrite

         .. _permissions.^optional^permission.compose:

         .. api-member::
            :name: :value:`compose`
            :refid: permissions-optional-permission-compose
            :refname: compose
            :annotation: -- [Added in TB 74]

         .. _permissions.^optional^permission.compose.save:

         .. api-member::
            :name: :value:`compose.save`
            :refid: permissions-optional-permission-compose-save
            :refname: compose.save
            :annotation: -- [Added in TB 102]

         .. _permissions.^optional^permission.compose.send:

         .. api-member::
            :name: :value:`compose.send`
            :refid: permissions-optional-permission-compose-send
            :refname: compose.send
            :annotation: -- [Added in TB 90]

         .. _permissions.^optional^permission.declarative^net^request^feedback:

         .. api-member::
            :name: :value:`declarativeNetRequestFeedback`
            :refid: permissions-optional-permission-declarative-net-request-feedback
            :refname: declarativeNetRequestFeedback

         .. _permissions.^optional^permission.downloads:

         .. api-member::
            :name: :value:`downloads`
            :refid: permissions-optional-permission-downloads
            :refname: downloads

         .. _permissions.^optional^permission.downloads.open:

         .. api-member::
            :name: :value:`downloads.open`
            :refid: permissions-optional-permission-downloads-open
            :refname: downloads.open

         .. _permissions.^optional^permission.geolocation:

         .. api-member::
            :name: :value:`geolocation`
            :refid: permissions-optional-permission-geolocation
            :refname: geolocation

         .. _permissions.^optional^permission.management:

         .. api-member::
            :name: :value:`management`
            :refid: permissions-optional-permission-management
            :refname: management

         .. _permissions.^optional^permission.messages^delete:

         .. api-member::
            :name: :value:`messagesDelete`
            :refid: permissions-optional-permission-messages-delete
            :refname: messagesDelete
            :annotation: -- [Added in TB 91]

         .. _permissions.^optional^permission.messages^import:

         .. api-member::
            :name: :value:`messagesImport`
            :refid: permissions-optional-permission-messages-import
            :refname: messagesImport
            :annotation: -- [Added in TB 106]

         .. _permissions.^optional^permission.messages^modify^permanent:

         .. api-member::
            :name: :value:`messagesModifyPermanent`
            :refid: permissions-optional-permission-messages-modify-permanent
            :refname: messagesModifyPermanent
            :annotation: -- [Added in TB 123]

         .. _permissions.^optional^permission.messages^move:

         .. api-member::
            :name: :value:`messagesMove`
            :refid: permissions-optional-permission-messages-move
            :refname: messagesMove
            :annotation: -- [Added in TB 66]

         .. _permissions.^optional^permission.messages^read:

         .. api-member::
            :name: :value:`messagesRead`
            :refid: permissions-optional-permission-messages-read
            :refname: messagesRead
            :annotation: -- [Added in TB 66]

         .. _permissions.^optional^permission.messages^tags:

         .. api-member::
            :name: :value:`messagesTags`
            :refid: permissions-optional-permission-messages-tags
            :refname: messagesTags
            :annotation: -- [Added in TB 102]

         .. _permissions.^optional^permission.messages^tags^list:

         .. api-member::
            :name: :value:`messagesTagsList`
            :refid: permissions-optional-permission-messages-tags-list
            :refname: messagesTagsList
            :annotation: -- [Added in TB 122]

         .. _permissions.^optional^permission.messages^update:

         .. api-member::
            :name: :value:`messagesUpdate`
            :refid: permissions-optional-permission-messages-update
            :refname: messagesUpdate
            :annotation: -- [Added in TB 122]

         .. _permissions.^optional^permission.messenger^settings:

         .. api-member::
            :name: :value:`messengerSettings`
            :refid: permissions-optional-permission-messenger-settings
            :refname: messengerSettings
            :annotation: -- [Added in TB 137]

         .. _permissions.^optional^permission.native^messaging:

         .. api-member::
            :name: :value:`nativeMessaging`
            :refid: permissions-optional-permission-native-messaging
            :refname: nativeMessaging

         .. _permissions.^optional^permission.notifications:

         .. api-member::
            :name: :value:`notifications`
            :refid: permissions-optional-permission-notifications
            :refname: notifications

         .. _permissions.^optional^permission.pkcs11:

         .. api-member::
            :name: :value:`pkcs11`
            :refid: permissions-optional-permission-pkcs11
            :refname: pkcs11

         .. _permissions.^optional^permission.privacy:

         .. api-member::
            :name: :value:`privacy`
            :refid: permissions-optional-permission-privacy
            :refname: privacy

         .. _permissions.^optional^permission.sensitive^data^upload:

         .. api-member::
            :name: :value:`sensitiveDataUpload`
            :refid: permissions-optional-permission-sensitive-data-upload
            :refname: sensitiveDataUpload
            :annotation: -- [Added in TB 115]

         .. _permissions.^optional^permission.sessions:

         .. api-member::
            :name: :value:`sessions`
            :refid: permissions-optional-permission-sessions
            :refname: sessions
            :annotation: -- [Added in TB 140]

         .. _permissions.^optional^permission.tabs:

         .. api-member::
            :name: :value:`tabs`
            :refid: permissions-optional-permission-tabs
            :refname: tabs
            :annotation: -- [Added in TB 62]

         .. _permissions.^optional^permission.web^navigation:

         .. api-member::
            :name: :value:`webNavigation`
            :refid: permissions-optional-permission-web-navigation
            :refname: webNavigation

.. _permissions.^optional^permission^no^prompt:

OptionalPermissionNoPrompt
--------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _permissions.^optional^permission^no^prompt.idle:

         .. api-member::
            :name: :value:`idle`
            :refid: permissions-optional-permission-no-prompt-idle
            :refname: idle

.. _permissions.^permission:

Permission
----------

.. api-section-annotation-hack:: 

.. api-header::
   :label: :ref:`permissions.^permission^no^prompt`

*or*

.. api-header::
   :label: :ref:`permissions.^optional^permission`

*or*

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _permissions.^permission.declarative^net^request:

         .. api-member::
            :name: :value:`declarativeNetRequest`
            :refid: permissions-permission-declarative-net-request
            :refname: declarativeNetRequest

.. _permissions.^permission^no^prompt:

PermissionNoPrompt
------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: :ref:`permissions.^optional^permission^no^prompt`

*or*

.. api-header::
   :label: :ref:`permissions.^permission^privileged`

*or*

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _permissions.^permission^no^prompt.alarms:

         .. api-member::
            :name: :value:`alarms`
            :refid: permissions-permission-no-prompt-alarms
            :refname: alarms

         .. _permissions.^permission^no^prompt.contextual^identities:

         .. api-member::
            :name: :value:`contextualIdentities`
            :refid: permissions-permission-no-prompt-contextual-identities
            :refname: contextualIdentities

         .. _permissions.^permission^no^prompt.declarative^net^request^with^host^access:

         .. api-member::
            :name: :value:`declarativeNetRequestWithHostAccess`
            :refid: permissions-permission-no-prompt-declarative-net-request-with-host-access
            :refname: declarativeNetRequestWithHostAccess

         .. _permissions.^permission^no^prompt.dns:

         .. api-member::
            :name: :value:`dns`
            :refid: permissions-permission-no-prompt-dns
            :refname: dns

         .. _permissions.^permission^no^prompt.identity:

         .. api-member::
            :name: :value:`identity`
            :refid: permissions-permission-no-prompt-identity
            :refname: identity

         .. _permissions.^permission^no^prompt.menus:

         .. api-member::
            :name: :value:`menus`
            :refid: permissions-permission-no-prompt-menus
            :refname: menus
            :annotation: -- [Added in TB 77]

         .. _permissions.^permission^no^prompt.storage:

         .. api-member::
            :name: :value:`storage`
            :refid: permissions-permission-no-prompt-storage
            :refname: storage

         .. _permissions.^permission^no^prompt.theme:

         .. api-member::
            :name: :value:`theme`
            :refid: permissions-permission-no-prompt-theme
            :refname: theme
            :annotation: -- [Added in TB 86]

         .. _permissions.^permission^no^prompt.unlimited^storage:

         .. api-member::
            :name: :value:`unlimitedStorage`
            :refid: permissions-permission-no-prompt-unlimited-storage
            :refname: unlimitedStorage

.. _permissions.^permission^privileged:

PermissionPrivileged
--------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _permissions.^permission^privileged.mozilla^addons:

         .. api-member::
            :name: :value:`mozillaAddons`
            :refid: permissions-permission-privileged-mozilla-addons
            :refname: mozillaAddons

.. _permissions.^permissions:

Permissions
-----------

.. api-section-annotation-hack:: -- [Added in TB 55]

.. api-header::
   :label: object

   .. _permissions.^permissions.data_collection:

   .. api-member::
      :name: [``data_collection``]
      :refid: permissions-permissions-data-collection
      :refname: data_collection
      :type: (array of :ref:`permissions.^optional^data^collection^permission`, optional)

   .. _permissions.^permissions.origins:

   .. api-member::
      :name: [``origins``]
      :refid: permissions-permissions-origins
      :refname: origins
      :type: (array of :ref:`permissions.^match^pattern`, optional)

   .. _permissions.^permissions.permissions:

   .. api-member::
      :name: [``permissions``]
      :refid: permissions-permissions-permissions
      :refname: permissions
      :type: (array of :ref:`permissions.^optional^permission` or :ref:`permissions.^optional^only^permission`, optional)
