==============
composeScripts
==============

This compose scripts API first appeared in Thunderbird 77. Functionally it is the same as the
`content scripts`__ API except that it works on the document of email messages during composition.
See the MDN documentation for a more in-depth explanation and :doc:`/changes/beta77` for examples.

See also :ref:`executeScript <tabs.executeScript>`, :ref:`insertCSS <tabs.insertCSS>`, and
:ref:`removeCSS <tabs.removeCSS>`.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts

.. note::

  Registering a compose script through ``manifest.json`` is not possible at this point.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: ``messagesModify``

   Read and modify your email messages as they are displayed to you

.. rst-class:: api-permission-info

.. note::

  The permission ``compose`` is required to use ``composeScripts``.

.. rst-class:: api-main-section

Functions
=========

.. _composeScripts.register:

register(composeScriptOptions)
------------------------------

.. api-section-annotation-hack:: 

Register a compose script programmatically

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``composeScriptOptions``
      :type: (:ref:`composeScripts.RegisteredComposeScriptOptions`)
      :annotation: 
   

.. rst-class:: api-main-section

Types
=====

.. _composeScripts.RegisteredComposeScript:

RegisteredComposeScript
-----------------------

.. api-section-annotation-hack:: 

An object that represents a compose script registered programmatically

.. api-header::
   :label: object

   - ``unregister()`` Unregister a compose script registered programmatically

.. _composeScripts.RegisteredComposeScriptOptions:

RegisteredComposeScriptOptions
------------------------------

.. api-section-annotation-hack:: 

Details of a compose script registered programmatically

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
   
