.. container:: sticky-sidebar

  ≡ browsingData API

  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

================
browsingData API
================

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The browsingData API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/browsingData>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`chrome.browsingData` API to remove browsing data from a user's local profile.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _browsing^data.permission.browsing^data:

.. api-member::
   :name: :permission:`browsingData`
   :refid: browsing-data-permission-browsing-data
   :refname: browsingData

   Clear recent browsing history, cookies, and related data.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`browsingData` is required to use ``messenger.browsingData.*``.

.. rst-class:: api-main-section

Functions
=========

.. _browsing^data.remove:

remove(options, dataToRemove)
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears various types of browsing data stored in a user's profile.

.. note::

   Specifying :code:`dataTypes.history` will also remove download history and service workers.

.. api-header::
   :label: Parameters

   .. _browsing^data.remove.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

   .. _browsing^data.remove.data^to^remove:

   .. api-member::
      :name: ``dataToRemove``
      :refid: browsing-data-remove-data-to-remove
      :refname: dataToRemove
      :type: (:ref:`browsing^data.^data^type^set`)

      The set of data types to remove.

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^appcache:

removeAppcache(options)
-----------------------

.. api-section-annotation-hack:: 

Clears websites' appcache data.

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^appcache.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-appcache-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^cache:

removeCache(options)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's cache.

.. note::

   :code:`removalOptions.since` is not supported.

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^cache.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-cache-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^cookies:

removeCookies(options)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's cookies and server-bound certificates modified within a particular timeframe.

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^cookies.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-cookies-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^downloads:

removeDownloads(options)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's list of downloaded files (*not* the downloaded files themselves).

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^downloads.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-downloads-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^file^systems:

removeFileSystems(options)
--------------------------

.. api-section-annotation-hack:: 

Clears websites' file system data.

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^file^systems.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-file-systems-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^form^data:

removeFormData(options)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's stored form data (autofill).

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^form^data.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-form-data-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^history:

removeHistory(options)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's history.

.. note::

   This function also removes download history and service workers.

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^history.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-history-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^indexed^d^b:

removeIndexedDB(options)
------------------------

.. api-section-annotation-hack:: 

Clears websites' IndexedDB data.

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^indexed^d^b.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-indexed-d-b-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^local^storage:

removeLocalStorage(options)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 57]

Clears websites' local storage data.

.. note::

   :code:`removalOptions.since` is not supported.

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^local^storage.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-local-storage-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^passwords:

removePasswords(options)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's stored passwords.

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^passwords.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-passwords-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^plugin^data:

removePluginData(options)
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears plugins' data.

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^plugin^data.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-plugin-data-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.remove^web^s^q^l:

removeWebSQL(options)
---------------------

.. api-section-annotation-hack:: 

Clears websites' WebSQL data.

.. api-header::
   :label: Parameters

   .. _browsing^data.remove^web^s^q^l.options:

   .. api-member::
      :name: ``options``
      :refid: browsing-data-remove-web-s-q-l-options
      :refname: options
      :type: (:ref:`browsing^data.^removal^options`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsing^data.settings:

settings()
----------

.. api-section-annotation-hack:: -- [Added in TB 53]

Reports which types of data are currently selected in the 'Clear browsing data' settings UI.  Note: some of the data types included in this API are not available in the settings UI, and some UI settings control more than one data type listed here.

.. api-header::
   :label: Return type (`Promise`_)

   .. _browsing^data.settings.returns:

   .. api-member::
      :refid: browsing-data-settings-returns
      :refname: _returns
      :type: object

      .. _browsing^data.settings.returns.data^removal^permitted:

      .. api-member::
         :name: ``dataRemovalPermitted``
         :refid: browsing-data-settings-returns-data-removal-permitted
         :refname: dataRemovalPermitted
         :type: (:ref:`browsing^data.^data^type^set`)

         All of the types will be present in the result, with values of :code:`true` if they are permitted to be removed (e.g., by enterprise policy) and :code:`false` if not.

      .. _browsing^data.settings.returns.data^to^remove:

      .. api-member::
         :name: ``dataToRemove``
         :refid: browsing-data-settings-returns-data-to-remove
         :refname: dataToRemove
         :type: (:ref:`browsing^data.^data^type^set`)

         All of the types will be present in the result, with values of :code:`true` if they are both selected to be removed and permitted to be removed, otherwise :code:`false`.

      .. _browsing^data.settings.returns.options:

      .. api-member::
         :name: ``options``
         :refid: browsing-data-settings-returns-options
         :refname: options
         :type: (:ref:`browsing^data.^removal^options`)

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. rst-class:: api-main-section

Types
=====

.. _browsing^data.^data^type^set:

DataTypeSet
-----------

.. api-section-annotation-hack:: 

A set of data types. Missing data types are interpreted as :code:`false`.

.. api-header::
   :label: object

   .. _browsing^data.^data^type^set.cache:

   .. api-member::
      :name: [``cache``]
      :refid: browsing-data-data-type-set-cache
      :refname: cache
      :type: (boolean, optional)

      The browser's cache. Note: when removing data, this clears the *entire* cache: it is not limited to the range you specify.

   .. _browsing^data.^data^type^set.cookies:

   .. api-member::
      :name: [``cookies``]
      :refid: browsing-data-data-type-set-cookies
      :refname: cookies
      :type: (boolean, optional)

      The browser's cookies.

   .. _browsing^data.^data^type^set.downloads:

   .. api-member::
      :name: [``downloads``]
      :refid: browsing-data-data-type-set-downloads
      :refname: downloads
      :type: (boolean, optional)

      The browser's download list.

   .. _browsing^data.^data^type^set.form^data:

   .. api-member::
      :name: [``formData``]
      :refid: browsing-data-data-type-set-form-data
      :refname: formData
      :type: (boolean, optional)

      The browser's stored form data.

   .. _browsing^data.^data^type^set.history:

   .. api-member::
      :name: [``history``]
      :refid: browsing-data-data-type-set-history
      :refname: history
      :type: (boolean, optional)

      The browser's history.

   .. _browsing^data.^data^type^set.indexed^d^b:

   .. api-member::
      :name: [``indexedDB``]
      :refid: browsing-data-data-type-set-indexed-d-b
      :refname: indexedDB
      :type: (boolean, optional)
      :annotation: -- [Added in TB 57]

      Websites' IndexedDB data.

   .. _browsing^data.^data^type^set.local^storage:

   .. api-member::
      :name: [``localStorage``]
      :refid: browsing-data-data-type-set-local-storage
      :refname: localStorage
      :type: (boolean, optional)
      :annotation: -- [Added in TB 57]

      Websites' local storage data.

   .. _browsing^data.^data^type^set.passwords:

   .. api-member::
      :name: [``passwords``]
      :refid: browsing-data-data-type-set-passwords
      :refname: passwords
      :type: (boolean, optional)

      Stored passwords.

   .. _browsing^data.^data^type^set.plugin^data:

   .. api-member::
      :name: [``pluginData``]
      :refid: browsing-data-data-type-set-plugin-data
      :refname: pluginData
      :type: (boolean, optional)

      Plugins' data.

   .. _browsing^data.^data^type^set.server^bound^certificates:

   .. api-member::
      :name: [``serverBoundCertificates``]
      :refid: browsing-data-data-type-set-server-bound-certificates
      :refname: serverBoundCertificates
      :type: (boolean, optional)

      Server-bound certificates.

   .. _browsing^data.^data^type^set.service^workers:

   .. api-member::
      :name: [``serviceWorkers``]
      :refid: browsing-data-data-type-set-service-workers
      :refname: serviceWorkers
      :type: (boolean, optional)

      Service Workers.

.. _browsing^data.^removal^options:

RemovalOptions
--------------

.. api-section-annotation-hack:: 

Options that determine exactly what data will be removed.

.. api-header::
   :label: object

   .. _browsing^data.^removal^options.cookie^store^id:

   .. api-member::
      :name: [``cookieStoreId``]
      :refid: browsing-data-removal-options-cookie-store-id
      :refname: cookieStoreId
      :type: (string, optional)
      :annotation: -- [Added in TB 84]

      Only remove data associated with this specific cookieStoreId.

   .. _browsing^data.^removal^options.hostnames:

   .. api-member::
      :name: [``hostnames``]
      :refid: browsing-data-removal-options-hostnames
      :refname: hostnames
      :type: (array of string, optional)
      :annotation: -- [Added in TB 56]

      Only remove data associated with these hostnames (only applies to cookies and localStorage).

      .. note::

         From Thunderbird 56 supports the specification of hostnames for the deletion of cookies and local storage items.

      .. note::

         From Thunderbird 77 also supports the specification of hostnames for the deletion of service worker and indexedDB items.

   .. _browsing^data.^removal^options.origin^types:

   .. api-member::
      :name: [``originTypes``]
      :refid: browsing-data-removal-options-origin-types
      :refname: originTypes
      :type: (object, optional)

      An object whose properties specify which origin types ought to be cleared. If this object isn't specified, it defaults to clearing only "unprotected" origins. Please ensure that you *really* want to remove application data before adding 'protectedWeb' or 'extensions'.

      .. _browsing^data.^removal^options.origin^types.extension:

      .. api-member::
         :name: [``extension``]
         :refid: browsing-data-removal-options-origin-types-extension
         :refname: extension
         :type: (boolean, optional)

         Extensions and packaged applications a user has installed (be _really_ careful!).

      .. _browsing^data.^removal^options.origin^types.protected^web:

      .. api-member::
         :name: [``protectedWeb``]
         :refid: browsing-data-removal-options-origin-types-protected-web
         :refname: protectedWeb
         :type: (boolean, optional)

         Websites that have been installed as hosted applications (be careful!).

      .. _browsing^data.^removal^options.origin^types.unprotected^web:

      .. api-member::
         :name: [``unprotectedWeb``]
         :refid: browsing-data-removal-options-origin-types-unprotected-web
         :refname: unprotectedWeb
         :type: (boolean, optional)

         Normal websites.

   .. _browsing^data.^removal^options.since:

   .. api-member::
      :name: [``since``]
      :refid: browsing-data-removal-options-since
      :refname: since
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)

      Remove data accumulated on or after this date, represented in milliseconds since the epoch (accessible via the :code:`getTime` method of the JavaScript :code:`Date` object). If absent, defaults to 0 (which would remove all browsing data).

      .. note::

         :code:`since` is not supported with the following data types: :code:`cache`, :code:`indexedDB`, :code:`localStorage`, and :code:`serviceWorkers`.
