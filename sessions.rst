.. _sessions_api:

========
sessions
========

The sessions API first appeared in Thunderbird 115. It allows to add tab related session data to Thunderbird's tabs, which will be restored on app restart.

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Functions
=========

.. _sessions.setTabValue:

setTabValue(tabId, key, value)
------------------------------

.. api-section-annotation-hack:: 

Store a key/value pair associated with a given tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      
      ID of the tab with which you want to associate the data. Error is thrown if ID is invalid.
   
   
   .. api-member::
      :name: ``key``
      :type: (string)
      
      Key that you can later use to retrieve this particular data value.
   
   
   .. api-member::
      :name: ``value``
      :type: (string)
   

.. _sessions.getTabValue:

getTabValue(tabId, key)
-----------------------

.. api-section-annotation-hack:: 

Retrieve a previously stored value for a given tab, given its key.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      
      ID of the tab whose data you are trying to retrieve. Error is thrown if ID is invalid.
   
   
   .. api-member::
      :name: ``key``
      :type: (string)
      
      Key identifying the particular value to retrieve.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: string
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _sessions.removeTabValue:

removeTabValue(tabId, key)
--------------------------

.. api-section-annotation-hack:: 

Remove a key/value pair from a given tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      
      ID of the tab whose data you are trying to remove. Error is thrown if ID is invalid.
   
   
   .. api-member::
      :name: ``key``
      :type: (string)
      
      Key identifying the particular value to remove.
   
