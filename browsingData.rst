.. container:: sticky-sidebar

  ≡ browsingData API

  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

================
browsingData API
================

.. role:: permission

.. role:: value

.. role:: code

Use the <code>chrome.browsingData</code> API to remove browsing data from a user's local profile.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`browsingData`

   Clear recent browsing history, cookies, and related data

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`browsingData` is required to use ``messenger.browsingData.*``.

.. rst-class:: api-main-section

Functions
=========

.. _browsingData.remove:

remove(options, dataToRemove)
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears various types of browsing data stored in a user's profile.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

   .. api-member::
      :name: ``dataToRemove``
      :type: (:ref:`browsingData.DataTypeSet`)

      The set of data types to remove.

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removeAppcache:

removeAppcache(options)
-----------------------

.. api-section-annotation-hack:: 

Clears websites' appcache data.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removeCache:

removeCache(options)
--------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's cache.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removeCookies:

removeCookies(options)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's cookies and server-bound certificates modified within a particular timeframe.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removeDownloads:

removeDownloads(options)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's list of downloaded files (*not* the downloaded files themselves).

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removeFileSystems:

removeFileSystems(options)
--------------------------

.. api-section-annotation-hack:: 

Clears websites' file system data.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removeFormData:

removeFormData(options)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's stored form data (autofill).

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removeHistory:

removeHistory(options)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's history.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removeIndexedDB:

removeIndexedDB(options)
------------------------

.. api-section-annotation-hack:: 

Clears websites' IndexedDB data.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removeLocalStorage:

removeLocalStorage(options)
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 57]

Clears websites' local storage data.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removePasswords:

removePasswords(options)
------------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears the browser's stored passwords.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removePluginData:

removePluginData(options)
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 53]

Clears plugins' data.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.removeWebSQL:

removeWebSQL(options)
---------------------

.. api-section-annotation-hack:: 

Clears websites' WebSQL data.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (:ref:`browsingData.RemovalOptions`)

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. _browsingData.settings:

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
         :type: (:ref:`browsingData.DataTypeSet`)

         All of the types will be present in the result, with values of :code:`true` if they are permitted to be removed (e.g., by enterprise policy) and :code:`false` if not.

      .. api-member::
         :name: ``dataToRemove``
         :type: (:ref:`browsingData.DataTypeSet`)

         All of the types will be present in the result, with values of :code:`true` if they are both selected to be removed and permitted to be removed, otherwise :code:`false`.

      .. api-member::
         :name: ``options``
         :type: (:ref:`browsingData.RemovalOptions`)

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`browsingData`

.. rst-class:: api-main-section

Types
=====

.. _browsingData.DataTypeSet:

DataTypeSet
-----------

.. api-section-annotation-hack:: 

A set of data types. Missing data types are interpreted as :code:`false`.

.. api-header::
   :label: object

   .. api-member::
      :name: [``cache``]
      :type: (boolean, optional)

      The browser's cache. Note: when removing data, this clears the *entire* cache: it is not limited to the range you specify.

   .. api-member::
      :name: [``cookies``]
      :type: (boolean, optional)

      The browser's cookies.

   .. api-member::
      :name: [``downloads``]
      :type: (boolean, optional)

      The browser's download list.

   .. api-member::
      :name: [``formData``]
      :type: (boolean, optional)

      The browser's stored form data.

   .. api-member::
      :name: [``history``]
      :type: (boolean, optional)

      The browser's history.

   .. api-member::
      :name: [``indexedDB``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 57]

      Websites' IndexedDB data.

   .. api-member::
      :name: [``localStorage``]
      :type: (boolean, optional)
      :annotation: -- [Added in TB 57]

      Websites' local storage data.

   .. api-member::
      :name: [``passwords``]
      :type: (boolean, optional)

      Stored passwords.

   .. api-member::
      :name: [``pluginData``]
      :type: (boolean, optional)

      Plugins' data.

   .. api-member::
      :name: [``serverBoundCertificates``]
      :type: (boolean, optional)

      Server-bound certificates.

   .. api-member::
      :name: [``serviceWorkers``]
      :type: (boolean, optional)

      Service Workers.

.. _browsingData.RemovalOptions:

RemovalOptions
--------------

.. api-section-annotation-hack:: 

Options that determine exactly what data will be removed.

.. api-header::
   :label: object

   .. api-member::
      :name: [``cookieStoreId``]
      :type: (string, optional)
      :annotation: -- [Added in TB 84]

      Only remove data associated with this specific cookieStoreId.

   .. api-member::
      :name: [``hostnames``]
      :type: (array of string, optional)
      :annotation: -- [Added in TB 56]

      Only remove data associated with these hostnames (only applies to cookies and localStorage).

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

   .. api-member::
      :name: [``since``]
      :type: (`Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__, optional)

      Remove data accumulated on or after this date, represented in milliseconds since the epoch (accessible via the :code:`getTime` method of the JavaScript :code:`Date` object). If absent, defaults to 0 (which would remove all browsing data).
