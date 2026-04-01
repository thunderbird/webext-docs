.. container:: sticky-sidebar

  ≡ sessions API

  * `Functions`_

  .. include:: /_includes/developer-resources.rst

============
sessions API
============

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

The sessions API allows to add tab related session data to Thunderbird's tabs, which will be restored on app restart.

Thunderbird's sessions API is similar to the `Firefox sessions API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/sessions>`__, but it doesn't support accessing or restoring closed tabs.

.. note::

   The Sessions API currently does not require the :permission:`sessions` permission, but it will soon. It's recommended to request this permission before it becomes mandatory, to ensure your add-on continues to function properly.

.. rst-class:: api-main-section

Functions
=========

.. _sessions.get^tab^value:

getTabValue(tabId, key)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 115.0]

Retrieve a previously stored value for a given tab, given its key. Returns :value:`undefined` if the requested :value:`key` does not exist for the given :value:`tabId`.

.. api-header::
   :label: Parameters

   .. _sessions.get^tab^value.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: sessions-get-tab-value-tab-id
      :refname: tabId
      :type: (integer)

      ID of the tab whose data you are trying to retrieve. Error is thrown if ID is invalid.

   .. _sessions.get^tab^value.key:

   .. api-member::
      :name: ``key``
      :refid: sessions-get-tab-value-key
      :refname: key
      :type: (string)

      Key identifying the particular value to retrieve.

.. api-header::
   :label: Return type (`Promise`_)

   .. _sessions.get^tab^value.returns:

   .. api-member::
      :refid: sessions-get-tab-value-returns
      :refname: _returns
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _sessions.remove^tab^value:

removeTabValue(tabId, key)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 115.0]

Remove a key/value pair from a given tab.

.. api-header::
   :label: Parameters

   .. _sessions.remove^tab^value.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: sessions-remove-tab-value-tab-id
      :refname: tabId
      :type: (integer)

      ID of the tab whose data you are trying to remove. Error is thrown if ID is invalid.

   .. _sessions.remove^tab^value.key:

   .. api-member::
      :name: ``key``
      :refid: sessions-remove-tab-value-key
      :refname: key
      :type: (string)

      Key identifying the particular value to remove.

.. _sessions.set^tab^value:

setTabValue(tabId, key, value)
------------------------------

.. api-section-annotation-hack:: -- [Added in TB 115.0]

Store a key/value pair associated with a given tab.

.. api-header::
   :label: Parameters

   .. _sessions.set^tab^value.tab^id:

   .. api-member::
      :name: ``tabId``
      :refid: sessions-set-tab-value-tab-id
      :refname: tabId
      :type: (integer)

      ID of the tab with which you want to associate the data. Error is thrown if ID is invalid.

   .. _sessions.set^tab^value.key:

   .. api-member::
      :name: ``key``
      :refid: sessions-set-tab-value-key
      :refname: key
      :type: (string)

      Key that you can later use to retrieve this particular data value.

   .. _sessions.set^tab^value.value:

   .. api-member::
      :name: ``value``
      :refid: sessions-set-tab-value-value
      :refname: value
      :type: (string)
