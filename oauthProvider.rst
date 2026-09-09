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

The oauthProvider API allows to manage OAuth authentication providers for Thunderbird to use when connecting to mail/address book/calendar services.

.. rst-class:: api-main-section

Manifest file properties
========================

.. _oauth^provider.oauth_provider:

.. api-member::
   :name: [``oauth_provider``]
   :refid: oauth-provider-oauth-provider
   :refname: oauth_provider
   :type: (object, optional)
   :annotation: -- [Added in TB 140]

   Describes an OAuth authentication provider for Thunderbird. You will need to have a client ID registered with the provider to use this API.

   .. _oauth^provider.oauth_provider.authorization^endpoint:

   .. api-member::
      :name: ``authorizationEndpoint``
      :refid: oauth-provider-oauth-provider-authorization-endpoint
      :refname: authorizationEndpoint
      :type: (string)
      :annotation: -- [Added in TB 140]

      OAuth authorization endpoint address.

   .. _oauth^provider.oauth_provider.client^id:

   .. api-member::
      :name: ``clientId``
      :refid: oauth-provider-oauth-provider-client-id
      :refname: clientId
      :type: (string)
      :annotation: -- [Added in TB 140]

      Identifies the OAuth client to the server.

   .. _oauth^provider.oauth_provider.hostnames:

   .. api-member::
      :name: ``hostnames``
      :refid: oauth-provider-oauth-provider-hostnames
      :refname: hostnames
      :type: (array of string)
      :annotation: -- [Added in TB 140]

      One or more server hostnames that use this OAuth provider. Include any service or autodiscovery hostnames that may initiate OAuth authentication. For example, to override many Microsoft configurations, both of these would be needed - ["office365.com", "outlook.com"]

   .. _oauth^provider.oauth_provider.issuer:

   .. api-member::
      :name: ``issuer``
      :refid: oauth-provider-oauth-provider-issuer
      :refname: issuer
      :type: (string)
      :annotation: -- [Added in TB 140]

      A string to identify this provider in the login manager. This *should* match the hostname of the authorization endpoint, although that is not required.

   .. _oauth^provider.oauth_provider.redirection^endpoint:

   .. api-member::
      :name: ``redirectionEndpoint``
      :refid: oauth-provider-oauth-provider-redirection-endpoint
      :refname: redirectionEndpoint
      :type: (string)
      :annotation: -- [Added in TB 140]

      OAuth redirection endpoint.

   .. _oauth^provider.oauth_provider.scopes:

   .. api-member::
      :name: ``scopes``
      :refid: oauth-provider-oauth-provider-scopes
      :refname: scopes
      :type: (string)
      :annotation: -- [Added in TB 140]

      The scopes to request when using this OAuth provider.

   .. _oauth^provider.oauth_provider.token^endpoint:

   .. api-member::
      :name: ``tokenEndpoint``
      :refid: oauth-provider-oauth-provider-token-endpoint
      :refname: tokenEndpoint
      :type: (string)
      :annotation: -- [Added in TB 140]

      OAuth token endpoint address.

   .. _oauth^provider.oauth_provider.client^secret:

   .. api-member::
      :name: [``clientSecret``]
      :refid: oauth-provider-oauth-provider-client-secret
      :refname: clientSecret
      :type: (string, optional)
      :annotation: -- [Added in TB 140]

      Identifies the OAuth client to the server.

   .. _oauth^provider.oauth_provider.email^domains:

   .. api-member::
      :name: [``emailDomains``]
      :refid: oauth-provider-oauth-provider-email-domains
      :refname: emailDomains
      :type: (array of string, optional)
      :annotation: -- [Added in TB 155]

      Email domains for which this OAuth provider should be used. If omitted, the provider applies to all domains in use with a given hostname

   .. _oauth^provider.oauth_provider.issuer^identifier:

   .. api-member::
      :name: [``issuerIdentifier``]
      :refid: oauth-provider-oauth-provider-issuer-identifier
      :refname: issuerIdentifier
      :type: (string, optional)
      :annotation: -- [Added in TB 153]

      The OAuth authorization server issuer identifier, as defined by RFC 9207. If provided, it *must* be an exact string match to what the provider gives in the iss field.

   .. _oauth^provider.oauth_provider.use^external^browser:

   .. api-member::
      :name: [``useExternalBrowser``]
      :refid: oauth-provider-oauth-provider-use-external-browser
      :refname: useExternalBrowser
      :type: (boolean, optional)
      :annotation: -- [Added in TB 153]

      If the login flow should use the system web browser. If true, the redirectionEndpoint *must* be a loopback address, so an origin of http://127.0.0.1 or http://localhost.

   .. _oauth^provider.oauth_provider.use^p^k^c^e:

   .. api-member::
      :name: [``usePKCE``]
      :refid: oauth-provider-oauth-provider-use-p-k-c-e
      :refname: usePKCE
      :type: (boolean, optional)
      :annotation: -- [Added in TB 140]

      If the authorization uses PKCE.
