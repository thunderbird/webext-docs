.. container:: sticky-sidebar

  ≡ userScripts API

  * `Events`_

  .. include:: /overlay/developer-resources.rst

===============
userScripts API
===============

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`user_scripts` is required to use ``messenger.userScripts.*``.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`userScripts` is required to use ``messenger.userScripts.*``.

.. rst-class:: api-main-section

Events
======

.. _userScripts.onBeforeScript:

onBeforeScript
--------------

.. api-section-annotation-hack:: 

Event called when a new userScript global has been created

.. api-header::
   :label: Parameters for onBeforeScript.addListener(listener)

   
   .. api-member::
      :name: ``listener(userScript)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``userScript``
      :type: (object)
      
      .. api-member::
         :name: ``defineGlobals``
         :type: (function)
         
         Exports all the properties of a given plain object as userScript globals
      
      
      .. api-member::
         :name: ``export``
         :type: (function)
         
         Convert a given value to make it accessible to the userScript code
      
      
      .. api-member::
         :name: ``global``
         :type: (any)
         
         The userScript global
      
      
      .. api-member::
         :name: ``metadata``
         :type: (any)
         
         The userScript metadata (as set in userScripts.register)
      
   

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`
