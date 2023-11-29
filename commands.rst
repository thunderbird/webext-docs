.. _commands_api:

============
commands API
============

The commands API first appeared in Thunderbird 66. It's more or less the same as the `Firefox commands API`__.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands

.. role:: permission

.. role:: value

.. role:: code

Use the commands API to add keyboard shortcuts that trigger actions in your extension, for example opening one of the action popups or sending a command to the extension.

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``commands``]
   :type: (object, optional)
   
   A *dictionary object* defining one or more commands as *name-value* pairs, the *name* being the name of the command and the *value* being a :ref:`commands.CommandsShortcut`. The *name* may also be one of the following built-in special shortcuts: 
   
    * :value:`_execute_browser_action` 
   
    * :value:`_execute_compose_action` 
   
    * :value:`_execute_message_display_action`
   
   Example: 
   
   .. literalinclude:: includes/commands/manifest.json
     :language: JSON
   
   

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`commands` is required to use ``messenger.commands.*``.

.. rst-class:: api-main-section

Functions
=========

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
      
      The new details for the command.
      
      .. api-member::
         :name: ``name``
         :type: (string)
         
         The name of the command.
      
      
      .. api-member::
         :name: [``description``]
         :type: (string, optional)
         
         The description for the command.
      
      
      .. api-member::
         :name: [``shortcut``]
         :type: (string, optional)
         
         An empty string to clear the shortcut, or a string matching the format defined by the `MDN page of the commands API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/commands#shortcut_values>`__  to set a new shortcut key. If the string does not match this format, the function throws an error.
      
   

.. rst-class:: api-main-section

Events
======

.. _commands.onChanged:

onChanged
---------

.. api-section-annotation-hack:: 

Fired when a registered command's shortcut is changed.

.. api-header::
   :label: Parameters for onChanged.addListener(listener)

   
   .. api-member::
      :name: ``listener(changeInfo)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``changeInfo``
      :type: (object)
      
      .. api-member::
         :name: ``name``
         :type: (string)
         
         The name of the shortcut.
      
      
      .. api-member::
         :name: ``newShortcut``
         :type: (string)
         
         The new shortcut active for this command, or blank if not active.
      
      
      .. api-member::
         :name: ``oldShortcut``
         :type: (string)
         
         The old shortcut which is no longer active for this command, or blank if the shortcut was previously inactive.
      
   

.. _commands.onCommand:

onCommand
---------

.. api-section-annotation-hack:: 

Fired when a registered command is activated using a keyboard shortcut. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for onCommand.addListener(listener)

   
   .. api-member::
      :name: ``listener(command, tab)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``command``
      :type: (string)
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: -- [Added in TB 106]
      
      The details of the active tab while the command occurred.
   

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
      :type: (string, optional)
      
      The Extension Command description
   
   
   .. api-member::
      :name: [``name``]
      :type: (string, optional)
      
      The name of the Extension Command
   
   
   .. api-member::
      :name: [``shortcut``]
      :type: (string, optional)
      
      The shortcut active for this command, or blank if not active.
   

.. _commands.CommandsShortcut:

CommandsShortcut
----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``description``]
      :type: (string, optional)
   
   
   .. api-member::
      :name: [``suggested_key``]
      :type: (object, optional)
      
      .. api-member::
         :name: [``default``]
         :type: (:ref:`commands.KeyName`, optional)
         
         Default key combination.
      
      
      .. api-member::
         :name: [``linux``]
         :type: (:ref:`commands.KeyName`, optional)
         
         Key combination on Linux.
      
      
      .. api-member::
         :name: [``mac``]
         :type: (:ref:`commands.KeyName`, optional)
         
         Key combination on Mac.
      
      
      .. api-member::
         :name: [``windows``]
         :type: (:ref:`commands.KeyName`, optional)
         
         Key combination on Windows.
      
   

.. _commands.KeyName:

KeyName
-------

.. api-section-annotation-hack:: 

Definition of a shortcut, for example :value:`Alt+F5`. The string must match the shortcut format as defined by the `MDN page of the commands API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/commands#shortcut_values>`__.

.. api-header::
   :label: string
