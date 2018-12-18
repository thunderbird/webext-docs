========
commands
========

The commands API first appeared in Thunderbird 66. It's more or less the same as the `Firefox commands API`__.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands

Use the commands API to add keyboard shortcuts that trigger actions in your extension, for example, an action to open the browser action or send a command to the xtension.

Manifest file properties
========================

- [``commands``] (object)

.. note::

  A manifest entry named ``commands`` is required to use ``commands``.

Functions
=========

.. _commands.update:

update(detail)
--------------

Update the details of an already defined command.

- ``detail`` (object) The new description for the command.

  - ``name`` (string) The name of the command.
  - [``description``] (string) The new description for the command.
  - [``shortcut``] (:ref:`manifest.KeyName`)

.. _commands.reset:

reset(name)
-----------

Reset a command's details to what is specified in the manifest.

- ``name`` (string) The name of the command.

.. _commands.getAll:

getAll()
--------

Returns all the registered extension commands for this extension and their shortcut (if active).

Returns a `Promise`_ fulfilled with:

- array of :ref:`commands.Command`

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Events
======

.. _commands.onCommand:

onCommand(command)
------------------

Fired when a registered command is activated using a keyboard shortcut.

- ``command`` (string)

Types
=====

.. _commands.Command:

Command
-------

object

- [``description``] (string) The Extension Command description
- [``name``] (string) The name of the Extension Command
- [``shortcut``] (string) The shortcut active for this command, or blank if not active.
