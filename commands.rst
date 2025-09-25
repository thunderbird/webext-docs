.. container:: sticky-sidebar

  ≡ commands API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

============
commands API
============

.. role:: permission

.. role:: value

.. role:: code

Use the commands API to add keyboard shortcuts that trigger actions in your extension, for example opening one of the action popups or sending a command to the extension.

Thunderbird's commands API is largely the same as the <a href='https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands'>Firefox commands API</a>.

.. rst-class:: api-main-section

Manifest file properties
========================

.. api-member::
   :name: [``commands``]
   :type: (object, optional)

   A *dictionary object* defining one or more commands as *name-value* pairs, the *name* being the name of the command and the *value* being a :ref:`CommandsShortcut`.

.. rst-class:: api-main-section

Permissions
===========

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`commands` is required to use ``messenger.commands.*``.

.. rst-class:: api-main-section

Functions
=========

.. _commands.getAll:

getAll()
--------

.. api-section-annotation-hack:: -- [Added in TB 66]

Returns all the registered extension commands for this extension and their shortcut (if active).

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`commands.Command`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _commands.openShortcutSettings:

openShortcutSettings()
----------------------

.. api-section-annotation-hack:: -- [Added in TB 137]

Open extension shortcuts configuration page.

.. _commands.reset:

reset(name)
-----------

.. api-section-annotation-hack:: -- [Added in TB 66]

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

.. api-section-annotation-hack:: -- [Added in TB 66]

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

.. api-section-annotation-hack:: -- [Added in TB 115]

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

.. api-section-annotation-hack:: -- [Added in TB 66]

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

.. api-section-annotation-hack:: -- [Added in TB 66]

.. api-header::
   :label: object

   .. api-member::
      :name: [``description``]
      :type: (string, optional)

      The description of the Extension Command

   .. api-member::
      :name: [``name``]
      :type: (string, optional)

      The name of the Extension Command

   .. api-member::
      :name: [``shortcut``]
      :type: (string, optional)

      The shortcut active for this command, or blank if not active.
