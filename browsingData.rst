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

.. hint::

   The browsingData API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/browsingData>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

Use the :code:`chrome.browsingData` API to remove browsing data from a user's local profile.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`browsingData`

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

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsing^data.^removal^options`)

   .. api-member::
      :name: ``dataToRemove``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :name: ``options``
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

   .. api-member::
      :type: object

      .. api-member::
         :name: ``dataRemovalPermitted``
         :type: (:ref:`browsing^data.^data^type^set`)

         All of the types will be present in the result, with values of :code:`true` if they are permitted to be removed (e.g., by enterprise policy) and :code:`false` if not.

      .. api-member::
         :name: ``dataToRemove``
         :type: (:ref:`browsing^data.^data^type^set`)

         All of the types will be present in the result, with values of :code:`true` if they are both selected to be removed and permitted to be removed, otherwise :code:`false`.

      .. api-member::
         :name: ``options``
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
      :type: (boolean, optional)

      The browser's cache. Note: when removing data, this clears the *entire* cache: it is not limited to the range you specify.

   .. _browsing^data.^data^type^set.cookies:

   .. api-member::
      :name: [``cookies``]
      :type: (boolean, optional)

      The browser's cookies.

   .. _browsing^data.^data^type^set.downloads:

   .. api-member::
      :name: [``downloads``]
      :type: (boolean, optional)

      The browser's download list.

   .. _browsing^data.^data^type^set.form^data:

   .. api-member::
      :name: [``formData``]
      :type: (boolean, optional)

      The browser's stored form data.

   .. _browsing^data.^data^type^set.history:

   .. api-member::
      :name: [``history``]
      :type: (boolean, optional)

      The browser's history.

   .. _browsing^data.^data^type^set.indexed^d^b:

   .. api-member::
      :name: [``indexedDB``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 57]

      Websites' IndexedDB data.

   .. _browsing^data.^data^type^set.local^storage:

   .. api-member::
      :name: [``localStorage``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 57]

      Websites' local storage data.

   .. _browsing^data.^data^type^set.passwords:

   .. api-member::
      :name: [``passwords``]
      :type: (boolean, optional)

      Stored passwords.

   .. _browsing^data.^data^type^set.plugin^data:

   .. api-member::
      :name: [``pluginData``]
      :type: (boolean, optional)

      Plugins' data.

   .. _browsing^data.^data^type^set.server^bound^certificates:

   .. api-member::
      :name: [``serverBoundCertificates``]
      :type: (boolean, optional)

      Server-bound certificates.

   .. _browsing^data.^data^type^set.service^workers:

   .. api-member::
      :name: [``serviceWorkers``]
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
      :type: (string, optional)
      :annotation: -- [Added in TB 84]

      Only remove data associated with this specific cookieStoreId.

   .. _browsing^data.^removal^options.hostnames:

   .. api-member::
      :name: [``hostnames``]
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
      :type: (object, optional)

      An object whose properties specify which origin types ought to be cleared. If this object isn't specified, it defaults to clearing only "unprotected" origins. Please ensure that you *really* want to remove application data before adding 'protectedWeb' or 'extensions'.

      .. api-member::
         :name: [``extension``]
         :type: (boolean, optional)

         Extensions and packaged applications a user has installed (be _really_ careful!).

      .. api-member::
         :name: [``protectedWeb``]
         :type: (boolean, optional)

         Websites that have been installed as hosted applications (be careful!).

      .. api-member::
         :name: [``unprotectedWeb``]
         :type: (boolean, optional)

         Normal websites.

   .. _browsing^data.^removal^options.since:

   .. api-member::
      :name: [``since``]
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)

      Remove data accumulated on or after this date, represented in milliseconds since the epoch (accessible via the :code:`getTime` method of the JavaScript :code:`Date` object). If absent, defaults to 0 (which would remove all browsing data).

      .. note::

         :code:`since` is not supported with the following data types: :code:`cache`, :code:`indexedDB`, :code:`localStorage`, and :code:`serviceWorkers`.
