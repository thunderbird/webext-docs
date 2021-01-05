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
      
      The new description for the command.
      
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
         :type: (:ref:`manifest.KeyName`)
      
   

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

Fired when a registered command is activated using a keyboard shortcut.

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
   
