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

Permissions
===========

- messagesModify "Read and modify your email messages as they are displayed to you"

.. note::

  The permission ``messagesModify`` is required to use ``messageDisplayScripts``.

Functions
=========

.. _messageDisplayScripts.register:

register(messageDisplayScriptOptions)
-------------------------------------

Register a message display script programmatically

- ``messageDisplayScriptOptions`` (:ref:`messageDisplayScripts.RegisteredMessageDisplayScriptOptions`)

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Types
=====

.. _messageDisplayScripts.RegisteredMessageDisplayScript:

RegisteredMessageDisplayScript
------------------------------

An object that represents a message display script registered programmatically

object:

- ``unregister()`` Unregister a message display script registered programmatically

.. _messageDisplayScripts.RegisteredMessageDisplayScriptOptions:

RegisteredMessageDisplayScriptOptions
-------------------------------------

Details of a message display script registered programmatically

object:

- [``css``] (array of `ExtensionFileOrCode <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/ExtensionFileOrCode>`_) The list of CSS files to inject
- [``js``] (array of `ExtensionFileOrCode <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/ExtensionFileOrCode>`_) The list of JavaScript files to inject
