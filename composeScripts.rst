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

.. note::

  The permission ``compose`` is required to use ``composeScripts``.

Functions
=========

.. _composeScripts.register:

register(composeScriptOptions)
------------------------------

Register a compose script programmatically

- ``composeScriptOptions`` (:ref:`composeScripts.RegisteredComposeScriptOptions`)

.. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

Types
=====

.. _composeScripts.RegisteredComposeScript:

RegisteredComposeScript
-----------------------

An object that represents a compose script registered programmatically

object:

- ``unregister()`` Unregister a compose script registered programmatically

.. _composeScripts.RegisteredComposeScriptOptions:

RegisteredComposeScriptOptions
------------------------------

Details of a compose script registered programmatically

object:

- [``css``] (array of `ExtensionFileOrCode <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/ExtensionFileOrCode>`_) The list of CSS files to inject
- [``js``] (array of `ExtensionFileOrCode <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/ExtensionFileOrCode>`_) The list of JavaScript files to inject
