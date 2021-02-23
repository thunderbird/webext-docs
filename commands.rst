.. _commands_api:

========
commands
========

The commands API first appeared in Thunderbird 66. It's more or less the same as the `Firefox commands API`__.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands

.. role:: permission

Use the commands API to add keyboard shortcuts that trigger actions in your extension, for example, an action to open the browser action or send a command to the xtension.

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``commands``]
   :type: (object)
   
   Object defining one or more commands as key-value pairs, the key being the name of the command and the value being a :ref:`commands.CommandsShortcut`. The key may also be one of the following built-in special shortcuts: 
   
    * ``_execute_browser_action`` 
   
    *  ``_execute_compose_action`` 
   
    * ``_execute_message_display_action``
   
   Example: 
   
   .. literalinclude:: includes/commands/manifest.json
     :language: JSON
   
   

.. rst-class:: api-permission-info

.. note::

   A manifest entry named ``commands`` is required to use ``commands``.

.. rst-class:: api-main-section

Functions
=========

.. _commands.update:

update(detail)
--------------

.. api-section-annotation-hack:: 

Update the details of an already defined command.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``detail``
      :type: (object)
      
      
      
      .. api-member::
         :name: ``name``
         :type: (string)
         
         The name of the command.
      
      
      .. api-member::
         :name: [``description``]
         :type: (string)
         
         The new description for the command.
      
      
      .. api-member::
         :name: [``shortcut``]
         :type: (string)
         
         An empty string to clear the shortcut, or a string matching the format defined by the `MDN page of the commands API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/commands#shortcut_values>`_  to set a new shortcut key. If the string does not match this format, the function throws an error.
      
   

.. _commands.reset:

reset(name)
-----------

.. api-section-annotation-hack:: 

Reset a command's details to what is specified in the manifest.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``name``
      :type: (string)
      
      The name of the command.
   

.. _commands.getAll:

getAll()
--------

.. api-section-annotation-hack:: 

Returns all the registered extension commands for this extension and their shortcut (if active).

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`commands.Command`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _commands.onCommand:

onCommand(command)
------------------

.. api-section-annotation-hack:: 

Fired when a registered command is activated using a keyboard shortcut. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``command``
      :type: (string)
   

.. rst-class:: api-main-section

Types
=====

.. _commands.Command:

Command
-------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``description``]
      :type: (string)
      
      The Extension Command description
   
   
   .. api-member::
      :name: [``name``]
      :type: (string)
      
      The name of the Extension Command
   
   
   .. api-member::
      :name: [``shortcut``]
      :type: (string)
      
      The shortcut active for this command, or blank if not active.
   

.. _commands.CommandsShortcut:

CommandsShortcut
----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``description``]
      :type: (string)
   
   
   .. api-member::
      :name: [``suggested_key``]
      :type: (object)
      
      .. api-member::
         :name: [``default``]
         :type: (:ref:`commands.KeyName`)
         
         Default key combination.
      
      
      .. api-member::
         :name: [``linux``]
         :type: (:ref:`commands.KeyName`)
         
         Key combination on Linux.
      
      
      .. api-member::
         :name: [``mac``]
         :type: (:ref:`commands.KeyName`)
         
         Key combination on Mac.
      
      
      .. api-member::
         :name: [``windows``]
         :type: (:ref:`commands.KeyName`)
         
         Key combination on Windows.
      
   

.. _commands.KeyName:

KeyName
-------

.. api-section-annotation-hack:: 

Definition of the shortcut, for example ``Alt+F5``. The string must match the shortcut format as defined by the `MDN page of the commands API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/commands#shortcut_values>`_.

.. api-header::
   :label: string
