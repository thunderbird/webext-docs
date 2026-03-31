.. container:: sticky-sidebar

  ≡ chromeSettingsOverrides API

  * `Manifest file properties`_

  .. include:: /_includes/developer-resources.rst

===========================
chromeSettingsOverrides API
===========================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. rst-class:: api-main-section

Manifest file properties
========================

.. _chrome^settings^overrides.chrome_settings_overrides:

.. api-member::
   :name: [``chrome_settings_overrides``]
   :refid: chrome-settings-overrides-chrome-settings-overrides
   :refname: chrome_settings_overrides
   :type: (object, optional)
   :annotation: -- [Added in TB 68.0a1]

   .. _chrome^settings^overrides.chrome_settings_overrides.search_provider:

   .. api-member::
      :name: [``search_provider``]
      :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider
      :refname: search_provider
      :type: (object, optional)
      :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.name:

      .. api-member::
         :name: ``name``
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-name
         :refname: name
         :type: (string)
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.search_url:

      .. api-member::
         :name: ``search_url``
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-search-url
         :refname: search_url
         :type: (string)
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.alternate_urls:

      .. api-member::
         :name: [``alternate_urls``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-alternate-urls
         :refname: alternate_urls
         :type: (array of string, optional) **Deprecated.**
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.encoding:

      .. api-member::
         :name: [``encoding``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-encoding
         :refname: encoding
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0a1]

         Encoding of the search term.

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.favicon_url:

      .. api-member::
         :name: [``favicon_url``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-favicon-url
         :refname: favicon_url
         :type: (string or string, optional)
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.image_url:

      .. api-member::
         :name: [``image_url``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-image-url
         :refname: image_url
         :type: (string, optional) **Deprecated.**
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.image_url_post_params:

      .. api-member::
         :name: [``image_url_post_params``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-image-url-post-params
         :refname: image_url_post_params
         :type: (string, optional) **Deprecated.**
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.instant_url:

      .. api-member::
         :name: [``instant_url``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-instant-url
         :refname: instant_url
         :type: (string, optional) **Deprecated.**
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.instant_url_post_params:

      .. api-member::
         :name: [``instant_url_post_params``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-instant-url-post-params
         :refname: instant_url_post_params
         :type: (string, optional) **Deprecated.**
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.is_default:

      .. api-member::
         :name: [``is_default``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-is-default
         :refname: is_default
         :type: (boolean, optional)
         :annotation: -- [Added in TB 68.0a1]

         Sets the default engine to a built-in engine only.

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.keyword:

      .. api-member::
         :name: [``keyword``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-keyword
         :refname: keyword
         :type: (string or array of string, optional)
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.params:

      .. api-member::
         :name: [``params``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-params
         :refname: params
         :type: (array of object, optional)
         :annotation: -- [Added in TB 68.0a1]

         A list of optional search url parameters. This allows the addition of search url parameters based on how the search is performed in Thunderbird.

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.prepopulated_id:

      .. api-member::
         :name: [``prepopulated_id``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-prepopulated-id
         :refname: prepopulated_id
         :type: (integer, optional) **Deprecated.**
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.search_form:

      .. api-member::
         :name: [``search_form``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-search-form
         :refname: search_form
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.search_url_get_params:

      .. api-member::
         :name: [``search_url_get_params``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-search-url-get-params
         :refname: search_url_get_params
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0a1]

         GET parameters to the search_url as a query string.

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.search_url_post_params:

      .. api-member::
         :name: [``search_url_post_params``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-search-url-post-params
         :refname: search_url_post_params
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0a1]

         POST parameters to the search_url as a query string.

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.suggest_url:

      .. api-member::
         :name: [``suggest_url``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-suggest-url
         :refname: suggest_url
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0a1]

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.suggest_url_get_params:

      .. api-member::
         :name: [``suggest_url_get_params``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-suggest-url-get-params
         :refname: suggest_url_get_params
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0a1]

         GET parameters to the suggest_url as a query string.

      .. _chrome^settings^overrides.chrome_settings_overrides.search_provider.suggest_url_post_params:

      .. api-member::
         :name: [``suggest_url_post_params``]
         :refid: chrome-settings-overrides-chrome-settings-overrides-search-provider-suggest-url-post-params
         :refname: suggest_url_post_params
         :type: (string, optional)
         :annotation: -- [Added in TB 68.0a1]

         POST parameters to the suggest_url as a query string.
