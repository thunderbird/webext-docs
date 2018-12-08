=============================
Thunderbird WebExtension APIs
=============================

The documents were generated automatically from the schema documents at `mail/components/extensions/schemas <https://hg.mozilla.org/comm-central/file/tip/mail/components/extensions/schemas/>`_.

.. note::

  These APIs should be considered experimental and could change at any time. For any problems or feature requests please `file a bug <https://bugzilla.mozilla.org/enter_bug.cgi?product=Thunderbird&component=Add-Ons%3A+Extensions+API>`_.

.. note::

  WebExtension APIs are asynchronous, that is, they return a `Promise <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise>`_ object which resolves when ready. See `Using Promises <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises>`_ for more information about Promises.

.. toctree::
  :maxdepth: 1

  accounts
  addressBooks
  browserAction
  cloudFile
  composeAction
  contacts
  legacy
  mailingLists
  mailTabs
  messages
  tabs
  windows

The following APIs are also included and work as they do in Firfox:

- `contentScripts <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts>`_
- `experiments <https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/basics.html#webextensions-experiments>`_
- `extension <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension>`_
- `i18n <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n>`_
- `management <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/management>`_
- `permissions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/permissions>`_
- `runtime <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime>`_
- `theme <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme>`_

How To
======

- `Using Promises <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises>`_
- :doc:`how-to/messageLists`
