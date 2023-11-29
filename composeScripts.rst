.. _composeScripts_api:

==============
composeScripts
==============

This compose scripts API first appeared in Thunderbird 77. Functionally it is the same as the
`content scripts`__ API except that it works on the document of email messages during composition.
See the MDN documentation for a more in-depth explanation and :ref:`thunderbird_77_0b1` for examples.

See also :ref:`executeScript <tabs.executeScript>`, :ref:`insertCSS <tabs.insertCSS>`,
:ref:`removeCSS <tabs.removeCSS>`, and :doc:`messageDisplayScripts`.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts

.. note::

  Registering a compose script in the *manifest.json* file is not possible at this point.

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`sensitiveDataUpload`

   Transfer sensitive user data (if access has been granted) to a remote server for further processing

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`compose` is required to use ``messenger.composeScripts.*``.

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
   

.. api-header::
   :label: Required permissions

   - :permission:`compose`

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
      :type: (array of :ref:`composeScripts.extensionTypes.ExtensionFileOrCode`, optional)
      
      The list of CSS files to inject
   
   
   .. api-member::
      :name: [``js``]
      :type: (array of :ref:`composeScripts.extensionTypes.ExtensionFileOrCode`, optional)
      
      The list of JavaScript files to inject
   

.. rst-class:: api-main-section

External Types
==============

The following types are not defined by this API, but by the underlying Mozilla WebExtension code base. They are included here, because there is no other public documentation available.

.. _composeScripts.extensionTypes.ExtensionFileOrCode:

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
   
