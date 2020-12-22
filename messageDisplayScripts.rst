.. _messageDisplayScripts_api:

=====================
messageDisplayScripts
=====================

This message display scripts API first appeared in Thunderbird 82. Functionally it is the same as
the `content scripts`__ API except that it works on the document of email messages being displayed.
See the MDN documentation for a more in-depth explanation and :doc:`/changes/beta82` for examples.

See also :ref:`executeScript <tabs.executeScript>`, :ref:`insertCSS <tabs.insertCSS>`,
:ref:`removeCSS <tabs.removeCSS>`, and :doc:`composeScripts`.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts

.. note::

  Registering a message display script through ``manifest.json`` is not possible at this point.

.. role:: permission

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`messagesModify`

   Read and modify your email messages as they are displayed to you

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`messagesModify` is required to use ``messageDisplayScripts``.

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
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesModify`

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
      :type: (array of :ref:`messageDisplayScripts.extensionTypes.ExtensionFileOrCode`)
      
      The list of CSS files to inject
   
   
   .. api-member::
      :name: [``js``]
      :type: (array of :ref:`messageDisplayScripts.extensionTypes.ExtensionFileOrCode`)
      
      The list of JavaScript files to inject
   

.. rst-class:: api-main-section

External Types
==============

The following types are not defined by this API, but by the underlying Mozilla WebExtension code base. They are included here, because there is no other public documentation available.

.. _messageDisplayScripts.extensionTypes.ExtensionFileOrCode:

ExtensionFileOrCode
-------------------

.. api-section-annotation-hack:: 

Specify code, either by pointing to a file or by providing the code directly. Only one of the two is allowed.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``code``
      :type: (string)
      
      Some JavaScript code to register.
   
   
   .. api-member::
      :name: ``file``
      :type: (string)
      
      A URL starting at the extension's manifest.json and pointing to a JavaScript file to register.
   
