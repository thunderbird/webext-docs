.. container:: sticky-sidebar

  ≡ identity API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

============
identity API
============

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The identity API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/identity>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the chrome.identity API to get OAuth2 access tokens.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _identity.permission.identity:

.. api-member::
   :name: :permission:`identity`
   :refid: identity-permission-identity
   :refname: identity

   Grant access to some or all methods of the identity API.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`identity` is required to use ``messenger.identity.*``.

.. rst-class:: api-main-section

Functions
=========

.. _identity.get^accounts:

getAccounts()
-------------

.. api-section-annotation-hack:: 

Retrieves a list of AccountInfo objects describing the accounts present on the profile.

.. api-header::
   :label: Return type (`Promise`_)

   .. _identity.get^accounts.returns:

   .. api-member::
      :refid: identity-get-accounts-returns
      :refname: _returns
      :type: array of :ref:`identity.^account^info`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. _identity.get^auth^token:

getAuthToken([details])
-----------------------

.. api-section-annotation-hack:: 

Gets an OAuth2 access token using the client ID and scopes specified in the oauth2 section of manifest.json.

.. api-header::
   :label: Parameters

   .. _identity.get^auth^token.details:

   .. api-member::
      :name: [``details``]
      :refid: identity-get-auth-token-details
      :refname: details
      :type: (object, optional)

      .. _identity.get^auth^token.details.account:

      .. api-member::
         :name: [``account``]
         :refid: identity-get-auth-token-details-account
         :refname: account
         :type: (:ref:`identity.^account^info`, optional)

      .. _identity.get^auth^token.details.interactive:

      .. api-member::
         :name: [``interactive``]
         :refid: identity-get-auth-token-details-interactive
         :refname: interactive
         :type: (boolean, optional)

      .. _identity.get^auth^token.details.scopes:

      .. api-member::
         :name: [``scopes``]
         :refid: identity-get-auth-token-details-scopes
         :refname: scopes
         :type: (array of string, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _identity.get^auth^token.returns:

   .. api-member::
      :refid: identity-get-auth-token-returns
      :refname: _returns
      :type: array of :ref:`identity.^account^info`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. _identity.get^profile^user^info:

getProfileUserInfo()
--------------------

.. api-section-annotation-hack:: 

Retrieves email address and obfuscated gaia id of the user signed into a profile.

.. api-header::
   :label: Return type (`Promise`_)

   .. _identity.get^profile^user^info.returns:

   .. api-member::
      :refid: identity-get-profile-user-info-returns
      :refname: _returns
      :type: object

      .. _identity.get^profile^user^info.returns.email:

      .. api-member::
         :name: ``email``
         :refid: identity-get-profile-user-info-returns-email
         :refname: email
         :type: (string)

      .. _identity.get^profile^user^info.returns.id:

      .. api-member::
         :name: ``id``
         :refid: identity-get-profile-user-info-returns-id
         :refname: id
         :type: (string)

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. _identity.get^redirect^u^r^l:

getRedirectURL([path])
----------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Generates a redirect URL to be used in :ref:`identity.launch^web^auth^flow`.

.. api-header::
   :label: Parameters

   .. _identity.get^redirect^u^r^l.path:

   .. api-member::
      :name: [``path``]
      :refid: identity-get-redirect-u-r-l-path
      :refname: path
      :type: (string, optional)

      The path appended to the end of the generated URL.

.. api-header::
   :label: Return type (`Promise`_)

   .. _identity.get^redirect^u^r^l.returns:

   .. api-member::
      :refid: identity-get-redirect-u-r-l-returns
      :refname: _returns
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. _identity.launch^web^auth^flow:

launchWebAuthFlow(details)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Starts an auth flow at the specified URL.

.. api-header::
   :label: Parameters

   .. _identity.launch^web^auth^flow.details:

   .. api-member::
      :name: ``details``
      :refid: identity-launch-web-auth-flow-details
      :refname: details
      :type: (object)

      .. _identity.launch^web^auth^flow.details.url:

      .. api-member::
         :name: ``url``
         :refid: identity-launch-web-auth-flow-details-url
         :refname: url
         :type: (:ref:`identity.^http^u^r^l`)

      .. _identity.launch^web^auth^flow.details.interactive:

      .. api-member::
         :name: [``interactive``]
         :refid: identity-launch-web-auth-flow-details-interactive
         :refname: interactive
         :type: (boolean, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. _identity.launch^web^auth^flow.returns:

   .. api-member::
      :refid: identity-launch-web-auth-flow-returns
      :refname: _returns
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. _identity.remove^cached^auth^token:

removeCachedAuthToken(details)
------------------------------

.. api-section-annotation-hack:: 

Removes an OAuth2 access token from the Identity API's token cache.

.. api-header::
   :label: Parameters

   .. _identity.remove^cached^auth^token.details:

   .. api-member::
      :name: ``details``
      :refid: identity-remove-cached-auth-token-details
      :refname: details
      :type: (object)

      .. _identity.remove^cached^auth^token.details.token:

      .. api-member::
         :name: ``token``
         :refid: identity-remove-cached-auth-token-details-token
         :refname: token
         :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. _identity.remove^cached^auth^token.returns:

   .. api-member::
      :refid: identity-remove-cached-auth-token-returns
      :refname: _returns
      :type: object

      .. _identity.remove^cached^auth^token.returns.email:

      .. api-member::
         :name: ``email``
         :refid: identity-remove-cached-auth-token-returns-email
         :refname: email
         :type: (string)

      .. _identity.remove^cached^auth^token.returns.id:

      .. api-member::
         :name: ``id``
         :refid: identity-remove-cached-auth-token-returns-id
         :refname: id
         :type: (string)

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. rst-class:: api-main-section

Events
======

.. _identity.on^sign^in^changed:

onSignInChanged
---------------

.. api-section-annotation-hack:: 

Fired when signin state changes for an account on the user's profile.

.. api-header::
   :label: Parameters for onSignInChanged.addListener(listener)

   .. _identity.on^sign^in^changed.listener(account, signed^in):

   .. api-member::
      :name: ``listener(account, signedIn)``
      :refid: identity-on-sign-in-changed-listener-account-signed-in
      :refname: listener(account, signedIn)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _identity.on^sign^in^changed.account:

   .. api-member::
      :name: ``account``
      :refid: identity-on-sign-in-changed-account
      :refname: account
      :type: (:ref:`identity.^account^info`)

   .. _identity.on^sign^in^changed.signed^in:

   .. api-member::
      :name: ``signedIn``
      :refid: identity-on-sign-in-changed-signed-in
      :refname: signedIn
      :type: (boolean)

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. rst-class:: api-main-section

Types
=====

.. _identity.^account^info:

AccountInfo
-----------

.. api-section-annotation-hack:: 

An object encapsulating an OAuth account id.

.. api-header::
   :label: object

   .. _identity.^account^info.id:

   .. api-member::
      :name: ``id``
      :refid: identity-account-info-id
      :refname: id
      :type: (string)

      A unique identifier for the account. This ID will not change for the lifetime of the account.

.. _identity.^http^u^r^l:

HttpURL
-------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string
