=============================
Thunderbird WebExtension APIs
=============================

Thunderbird WebExtensions are very similar to those of Firefox. These documents assume you have
some familiarity with building a WebExtension for Firefox. If not, it is highly recommended to
begin by reading some of the `MDN documentation on the subject`__.

WebExtension APIs are asynchronous, that is, they return a `Promise`__ object which resolves when
ready. See `Using Promises`__ for more information about Promises.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions
__ https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
__ https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises

The documents were generated automatically from the schema documents at
`mail/components/extensions/schemas`__.

__ https://hg.mozilla.org/comm-central/file/tip/mail/components/extensions/schemas/

.. note::

  These APIs should be considered experimental and may change in the future.
  For any problems or feature requests please `file a bug`__.

__ https://bugzilla.mozilla.org/enter_bug.cgi?product=Thunderbird&component=Add-Ons%3A+Extensions+API

.. toctree::
  :maxdepth: 1

  accounts
  addressBooks
  browserAction
  cloudFile
  commands
  compose
  composeAction
  contacts
  legacy
  mailingLists
  mailTabs
  menus
  messages
  tabs
  windows

The following APIs are also included and work as they do in Firefox:

- `contentScripts <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts>`_
- `experiments <https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/basics.html#webextensions-experiments>`_
- `extension <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension>`_
- `i18n <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n>`_
- `management <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/management>`_
- `permissions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/permissions>`_
- `pkcs11 <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pkcs11>`_ (to be added in Thunderbird 66, see `bug 1510997 <https://bugzilla.mozilla.org/show_bug.cgi?id=1510997>`_)
- `runtime <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime>`_
- `theme <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme>`_

How To
======

.. toctree::
  :maxdepth: 1

  how-to/experiments
  how-to/extensions68
  how-to/messageLists
