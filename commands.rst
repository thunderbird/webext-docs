.. container:: sticky-sidebar

  ≡ commands API

  * `Manifest file properties`_
  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

============
commands API
============

.. role:: permission

.. role:: value

.. role:: code

Use the commands API to add keyboard shortcuts that trigger actions in your extension, for example opening one of the action popups or sending a command to the extension.

Thunderbird's commands API is largely the same as the `Firefox commands API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/commands>`__.

.. rst-class:: api-main-section

Manifest file properties
========================

.. _commands.commands:

.. api-member::
   :name: [``commands``]
   :refid: commands-commands
   :refname: commands
   :type: (object, optional)
   :annotation: -- [Added in TB 66]

   A *dictionary object* defining one or more commands as *name-value* pairs, the *name* being the name of the command and the *value* being a :ref:`commands.^commands^shortcut`.

   The *name* may also be one of the following built-in special shortcuts:

    * :value:`_execute_action`
    * :value:`_execute_compose_action`
    * :value:`_execute_message_display_action`

   Example:

   .. code-block:: JSON

      {
        "commands": {
          "toggle-feature": {
            "suggested_key": {
              "default": "Ctrl+Shift+Y",
              "linux": "Ctrl+Shift+U"
            },
            "description": "Send a 'toggle-feature' event"
          },
          "_execute_compose_action": {
            "suggested_key": {
              "default": "Alt+F5"
            },
            "description": "Open the compose action popup"
          }
        }
      }

.. rst-class:: api-main-section

Permissions
===========

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`commands` is required to use ``messenger.commands.*``.

.. rst-class:: api-main-section

Functions
=========

.. _commands.get^all:

getAll()
--------

.. api-section-annotation-hack:: -- [Added in TB 66]

Returns all the registered extension commands for this extension and their shortcut (if active).

.. api-header::
   :label: Return type (`Promise`_)

   .. _commands.get^all.returns:

   .. api-member::
      :refid: commands-get-all-returns
      :refname: _returns
      :type: array of :ref:`commands.^command`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _commands.open^shortcut^settings:

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

   .. _commands.reset.name:

   .. api-member::
      :name: ``name``
      :refid: commands-reset-name
      :refname: name
      :type: (string)

      The name of the command.

.. _commands.update:

update(detail)
--------------

.. api-section-annotation-hack:: -- [Added in TB 66]

Update the details of an already defined command.

.. api-header::
   :label: Parameters

   .. _commands.update.detail:

   .. api-member::
      :name: ``detail``
      :refid: commands-update-detail
      :refname: detail
      :type: (object)

      The new details for the command.

      .. _commands.update.detail.name:

      .. api-member::
         :name: ``name``
         :refid: commands-update-detail-name
         :refname: name
         :type: (string)

         The name of the command.

      .. _commands.update.detail.description:

      .. api-member::
         :name: [``description``]
         :refid: commands-update-detail-description
         :refname: description
         :type: (string, optional)

         The description for the command.

      .. _commands.update.detail.shortcut:

      .. api-member::
         :name: [``shortcut``]
         :refid: commands-update-detail-shortcut
         :refname: shortcut
         :type: (string, optional)

         An empty string to clear the shortcut, or a string matching the format defined by the `MDN page of the commands API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/commands#shortcut_values>`__  to set a new shortcut key. If the string does not match this format, the function throws an error.

.. rst-class:: api-main-section

Events
======

.. _commands.on^changed:

onChanged
---------

.. api-section-annotation-hack:: -- [Added in TB 115]

Fired when a registered command's shortcut is changed.

.. api-header::
   :label: Parameters for onChanged.addListener(listener)

   .. _commands.on^changed.listener(change^info):

   .. api-member::
      :name: ``listener(changeInfo)``
      :refid: commands-on-changed-listener-change-info
      :refname: listener(changeInfo)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _commands.on^changed.change^info:

   .. api-member::
      :name: ``changeInfo``
      :refid: commands-on-changed-change-info
      :refname: changeInfo
      :type: (object)

      .. _commands.on^changed.change^info.name:

      .. api-member::
         :name: ``name``
         :refid: commands-on-changed-change-info-name
         :refname: name
         :type: (string)

         The name of the shortcut.

      .. _commands.on^changed.change^info.new^shortcut:

      .. api-member::
         :name: ``newShortcut``
         :refid: commands-on-changed-change-info-new-shortcut
         :refname: newShortcut
         :type: (string)

         The new shortcut active for this command, or blank if not active.

      .. _commands.on^changed.change^info.old^shortcut:

      .. api-member::
         :name: ``oldShortcut``
         :refid: commands-on-changed-change-info-old-shortcut
         :refname: oldShortcut
         :type: (string)

         The old shortcut which is no longer active for this command, or blank if the shortcut was previously inactive.

.. _commands.on^command:

onCommand
---------

.. api-section-annotation-hack:: -- [Added in TB 66]

Fired when a registered command is activated using a keyboard shortcut. This is a user input event handler. For asynchronous listeners some `restrictions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/User_actions>`__ apply.

.. api-header::
   :label: Parameters for onCommand.addListener(listener)

   .. _commands.on^command.listener(command, tab):

   .. api-member::
      :name: ``listener(command, tab)``
      :refid: commands-on-command-listener-command-tab
      :refname: listener(command, tab)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _commands.on^command.command:

   .. api-member::
      :name: ``command``
      :refid: commands-on-command-command
      :refname: command
      :type: (string)

   .. _commands.on^command.tab:

   .. api-member::
      :name: ``tab``
      :refid: commands-on-command-tab
      :refname: tab
      :type: (:ref:`tabs.^tab`)
      :annotation: -- [Added in TB 106]

      The details of the active tab while the command occurred.

.. rst-class:: api-main-section

Types
=====

.. _commands.^command:

Command
-------

.. api-section-annotation-hack:: -- [Added in TB 66]

.. api-header::
   :label: object

   .. _commands.^command.description:

   .. api-member::
      :name: [``description``]
      :refid: commands-command-description
      :refname: description
      :type: (string, optional)

      The description of the Extension Command

   .. _commands.^command.name:

   .. api-member::
      :name: [``name``]
      :refid: commands-command-name
      :refname: name
      :type: (string, optional)

      The name of the Extension Command

   .. _commands.^command.shortcut:

   .. api-member::
      :name: [``shortcut``]
      :refid: commands-command-shortcut
      :refname: shortcut
      :type: (string, optional)

      The shortcut active for this command, or blank if not active.

.. _commands.^commands^shortcut:

CommandsShortcut
----------------

.. api-section-annotation-hack:: -- [Added in TB 140]

.. api-header::
   :label: object

   .. _commands.^commands^shortcut.description:

   .. api-member::
      :name: [``description``]
      :refid: commands-commands-shortcut-description
      :refname: description
      :type: (string, optional)

   .. _commands.^commands^shortcut.suggested_key:

   .. api-member::
      :name: [``suggested_key``]
      :refid: commands-commands-shortcut-suggested-key
      :refname: suggested_key
      :type: (object, optional)

      .. _commands.^commands^shortcut.suggested_key.default:

      .. api-member::
         :name: [``default``]
         :refid: commands-commands-shortcut-suggested-key-default
         :refname: default
         :type: (:ref:`commands.^key^name`, optional)

         Default key combination.

      .. _commands.^commands^shortcut.suggested_key.linux:

      .. api-member::
         :name: [``linux``]
         :refid: commands-commands-shortcut-suggested-key-linux
         :refname: linux
         :type: (:ref:`commands.^key^name`, optional)

         Key combination on Linux.

      .. _commands.^commands^shortcut.suggested_key.mac:

      .. api-member::
         :name: [``mac``]
         :refid: commands-commands-shortcut-suggested-key-mac
         :refname: mac
         :type: (:ref:`commands.^key^name`, optional)

         Key combination on Mac.

      .. _commands.^commands^shortcut.suggested_key.windows:

      .. api-member::
         :name: [``windows``]
         :refid: commands-commands-shortcut-suggested-key-windows
         :refname: windows
         :type: (:ref:`commands.^key^name`, optional)

         Key combination on Windows.

.. _commands.^key^name:

KeyName
-------

.. api-section-annotation-hack:: -- [Added in TB 66]

Definition of a shortcut, for example :value:`Alt+F5`. The string must match the shortcut format as defined by the `MDN page of the commands API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/commands#shortcut_values>`__.

.. api-header::
   :label: string
