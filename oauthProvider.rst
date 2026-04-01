.. container:: sticky-sidebar

  ≡ oauthProvider API

  * `Manifest file properties`_

  .. include:: /_includes/developer-resources.rst

=================
oauthProvider API
=================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. rst-class:: api-main-section

Manifest file properties
========================

.. _oauth^provider.oauth_provider:

.. api-member::
   :name: [``oauth_provider``]
   :refid: oauth-provider-oauth-provider
   :refname: oauth_provider
   :type: (object, optional)

   Describes an OAuth authentication provider for Thunderbird to use when connecting to mail/address book/calendar services. You will need to have a client ID registered with the provider to use this API.

   .. _oauth^provider.oauth_provider.authorization^endpoint:

   .. api-member::
      :name: ``authorizationEndpoint``
      :refid: oauth-provider-oauth-provider-authorization-endpoint
      :refname: authorizationEndpoint
      :type: (string)

      OAuth authorization endpoint address.

   .. _oauth^provider.oauth_provider.client^id:

   .. api-member::
      :name: ``clientId``
      :refid: oauth-provider-oauth-provider-client-id
      :refname: clientId
      :type: (string)

      Identifies the OAuth client to the server.

   .. _oauth^provider.oauth_provider.hostnames:

   .. api-member::
      :name: ``hostnames``
      :refid: oauth-provider-oauth-provider-hostnames
      :refname: hostnames
      :type: (array of string)

      One or more hostnames which use this OAuth provider.

   .. _oauth^provider.oauth_provider.issuer:

   .. api-member::
      :name: ``issuer``
      :refid: oauth-provider-oauth-provider-issuer
      :refname: issuer
      :type: (string)

      A string to identify this provider in the login manager. This *should* match the hostname of the authorization endpoint, although that is not required.

   .. _oauth^provider.oauth_provider.redirection^endpoint:

   .. api-member::
      :name: ``redirectionEndpoint``
      :refid: oauth-provider-oauth-provider-redirection-endpoint
      :refname: redirectionEndpoint
      :type: (string)

      OAuth redirection endpoint.

   .. _oauth^provider.oauth_provider.scopes:

   .. api-member::
      :name: ``scopes``
      :refid: oauth-provider-oauth-provider-scopes
      :refname: scopes
      :type: (string)

      The scopes to request when using this OAuth provider.

   .. _oauth^provider.oauth_provider.token^endpoint:

   .. api-member::
      :name: ``tokenEndpoint``
      :refid: oauth-provider-oauth-provider-token-endpoint
      :refname: tokenEndpoint
      :type: (string)

      OAuth token endpoint address.

   .. _oauth^provider.oauth_provider.client^secret:

   .. api-member::
      :name: [``clientSecret``]
      :refid: oauth-provider-oauth-provider-client-secret
      :refname: clientSecret
      :type: (string, optional)

      Identifies the OAuth client to the server.

   .. _oauth^provider.oauth_provider.use^p^k^c^e:

   .. api-member::
      :name: [``usePKCE``]
      :refid: oauth-provider-oauth-provider-use-p-k-c-e
      :refname: usePKCE
      :type: (boolean, optional)

      If the authorization uses PKCE.
