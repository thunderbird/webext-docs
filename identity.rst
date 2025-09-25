.. container:: sticky-sidebar

  ≡ identity API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

============
identity API
============

.. role:: permission

.. role:: value

.. role:: code

Use the chrome.identity API to get OAuth2 access tokens.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`identity`

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`identity` is required to use ``messenger.identity.*``.

.. rst-class:: api-main-section

Functions
=========

.. _identity.getAccounts:

getAccounts()
-------------

.. api-section-annotation-hack:: 

Retrieves a list of AccountInfo objects describing the accounts present on the profile.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`identity.AccountInfo`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. _identity.getAuthToken:

getAuthToken([details])
-----------------------

.. api-section-annotation-hack:: 

Gets an OAuth2 access token using the client ID and scopes specified in the oauth2 section of manifest.json.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``details``]
      :type: (object, optional)

      .. api-member::
         :name: [``account``]
         :type: (:ref:`identity.AccountInfo`, optional)

      .. api-member::
         :name: [``interactive``]
         :type: (boolean, optional)

      .. api-member::
         :name: [``scopes``]
         :type: (array of string, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`identity.AccountInfo`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. _identity.getProfileUserInfo:

getProfileUserInfo()
--------------------

.. api-section-annotation-hack:: 

Retrieves email address and obfuscated gaia id of the user signed into a profile.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: object

      .. api-member::
         :name: ``email``
         :type: (string)

      .. api-member::
         :name: ``id``
         :type: (string)

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. _identity.getRedirectURL:

getRedirectURL([path])
----------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Generates a redirect URL to be used in |launchWebAuthFlow|.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``path``]
      :type: (string, optional)

      The path appended to the end of the generated URL.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. _identity.launchWebAuthFlow:

launchWebAuthFlow(details)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Starts an auth flow at the specified URL.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``url``
         :type: (:ref:`identity.HttpURL`)

      .. api-member::
         :name: [``interactive``]
         :type: (boolean, optional)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. _identity.removeCachedAuthToken:

removeCachedAuthToken(details)
------------------------------

.. api-section-annotation-hack:: 

Removes an OAuth2 access token from the Identity API's token cache.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``details``
      :type: (object)

      .. api-member::
         :name: ``token``
         :type: (string)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: object

      .. api-member::
         :name: ``email``
         :type: (string)

      .. api-member::
         :name: ``id``
         :type: (string)

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. rst-class:: api-main-section

Events
======

.. _identity.onSignInChanged:

onSignInChanged
---------------

.. api-section-annotation-hack:: 

Fired when signin state changes for an account on the user's profile.

.. api-header::
   :label: Parameters for onSignInChanged.addListener(listener)

   .. api-member::
      :name: ``listener(account, signedIn)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``account``
      :type: (:ref:`identity.AccountInfo`)

   .. api-member::
      :name: ``signedIn``
      :type: (boolean)

.. api-header::
   :label: Required permissions

   - :permission:`identity`

.. rst-class:: api-main-section

Types
=====

.. _identity.AccountInfo:

AccountInfo
-----------

.. api-section-annotation-hack:: 

An object encapsulating an OAuth account id.

.. api-header::
   :label: object

   .. api-member::
      :name: ``id``
      :type: (string)

      A unique identifier for the account. This ID will not change for the lifetime of the account.

.. _identity.HttpURL:

HttpURL
-------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string
