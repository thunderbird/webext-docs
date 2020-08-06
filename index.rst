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

  This documentation is for pre-release versions of Thunderbird. See the `"78" version`__ for
  Thunderbird 78, or the `"68" version`__ for Thunderbird 68.
  For any problems or feature requests please `file a bug`__.

__ https://thunderbird-webextensions.readthedocs.io/en/78/
__ https://thunderbird-webextensions.readthedocs.io/en/68/
__ https://bugzilla.mozilla.org/enter_bug.cgi?product=Thunderbird&component=Add-Ons%3A+Extensions+API

.. note::

  In Thunderbird, all WebExtension API can be accessed through the *browser.\** namespace, as with Firefox, but also through the  *messenger.\** namespace, which is a better fit for Thunderbird.

.. toctree::
  :maxdepth: 1

  accounts
  addressBooks
  browserAction
  cloudFile
  commands
  compose
  composeAction
  composeScripts
  contacts
  folders
  mailingLists
  mailTabs
  menus
  messageDisplay
  messageDisplayAction
  messages
  tabs
  windows

.. toolkit_apis:

The following APIs are also included and work as they do in Firefox:

- `contentScripts <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts>`_
- `downloads <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads>`_
- `experiments <https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/basics.html#webextensions-experiments>`_
- `extension <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension>`_
- `i18n <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n>`_
- `identity <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/identity>`_ *Added in Thunderbird 78.0b2*
- `management <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/management>`_
- `permissions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/permissions>`_
- `pkcs11 <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pkcs11>`_
- `runtime <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime>`_
- `storage <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage>`_
- `theme <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme>`_

Changes to APIs
===============

.. toctree::
  :maxdepth: 1

  changes/beta74
  changes/beta75
  changes/beta76
  changes/beta77
  changes/beta78
  changes/beta81

How To
======

.. toctree::
  :maxdepth: 1

  how-to/experiments
  how-to/messageLists

Where To Get Help
=================

- `developer.thunderbird.net`__ for information about building Thunderbird, and creating extensions.
- `Add-ons message board`__ for Thunderbird add-on developers to ask questions and share knowledge.
- `Bugzilla`__ for bug reports and feature requests.
- `developer.mozilla.org`__ for Firefox WebExtensions, on which Thunderbird's are based.

__ https://developer.thunderbird.net/
__ https://thunderbird.topicbox.com/groups/addons
__ https://bugzilla.mozilla.org/enter_bug.cgi?product=Thunderbird&component=Add-Ons%3A+Extensions+API
__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions
