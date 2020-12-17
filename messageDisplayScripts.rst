=====================
messageDisplayScripts
=====================

This message display scripts API first appeared in Thunderbird 82 and was backported to Thunderbird
78.4. Functionally it is the same as the `content scripts`__ API except that it works on the
document of email messages being displayed. See the MDN documentation for a more in-depth
explanation and :doc:`/changes/beta82` for examples.

See also :ref:`executeScript <tabs.executeScript>`, :ref:`insertCSS <tabs.insertCSS>`,
:ref:`removeCSS <tabs.removeCSS>`, and :doc:`composeScripts`.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts

.. note::

  Registering a message display script through ``manifest.json`` is not possible at this point.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: ``messagesModify``

   Read and modify your email messages as they are displayed to you

.. rst-class:: api-permission-info

.. note::

  The permission ``messagesModify`` is required to use ``messageDisplayScripts``.

.. rst-class:: api-main-section

Functions
=========

.. _messageDisplayScripts.register:

register(messageDisplayScriptOptions)
-------------------------------------

.. api-section-annotation-hack:: 

Register a message display script programmatically

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageDisplayScriptOptions``
      :type: (:ref:`messageDisplayScripts.RegisteredMessageDisplayScriptOptions`)
      :annotation: 
   

.. rst-class:: api-main-section

Types
=====

.. _messageDisplayScripts.RegisteredMessageDisplayScript:

RegisteredMessageDisplayScript
------------------------------

.. api-section-annotation-hack:: 

An object that represents a message display script registered programmatically

.. api-header::
   :label: object

   - ``unregister()`` Unregister a message display script registered programmatically

.. _messageDisplayScripts.RegisteredMessageDisplayScriptOptions:

RegisteredMessageDisplayScriptOptions
-------------------------------------

.. api-section-annotation-hack:: 

Details of a message display script registered programmatically

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``css``]
      :type: (array of `ExtensionFileOrCode <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/ExtensionFileOrCode>`_)
      :annotation: 
   
      The list of CSS files to inject
   
   
   .. api-member::
      :name: [``js``]
      :type: (array of `ExtensionFileOrCode <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/ExtensionFileOrCode>`_)
      :annotation: 
   
      The list of JavaScript files to inject
   
