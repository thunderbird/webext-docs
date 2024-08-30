.. container:: sticky-sidebar

  ≡ On this page
  
  * `Getting started`_
  * :ref:`Examples`
  * :ref:`Experiments`
  * :ref:`ChangeLog`
  * `Where to get help and more information`_

  .. include:: /overlay/developer-resources.rst 


===============================================
WebExtension Documentation for Thunderbird Beta
===============================================

Getting started
===============

These documents assume you already have some familiarity with the WebExtension technology. If not, it is
highly recommended to start with the following pages:

* `Introduction to add-on development`__
* `Hello world Add-on tutorial`__

__ https://developer.thunderbird.net/add-ons/about-add-ons
__ https://developer.thunderbird.net/add-ons/hello-world-add-on

For any problems or feature requests please `file a bug`__.

__ https://bugzilla.mozilla.org/enter_bug.cgi?product=Thunderbird&component=Add-Ons%3A+Extensions+API

.. hint::

  In Thunderbird, all WebExtension API can be accessed through the *browser.\** namespace, as with Firefox,
  but also through the  *messenger.\** namespace, which is a better fit for Thunderbird.

.. important::

  WebExtension APIs are asynchronous, that is, they return a `Promise`__ object which resolves when
  ready. See `Using Promises`__ for more information about Promises.

__ https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
__ https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises

The documentation for the APIs listed in the left side panel is generated automatically from
Thunderbird's schema files. The `webext-schemas <https://github.com/thunderbird/webext-schemas>`__
repository can be used to obtain a copy of the relevant files.

.. toctree::
  :hidden:
  :caption: API reference
  
  accounts
  addressBooks
  addressBooks.provider
  addressBooks.contacts
  addressBooks.mailingLists
  alarms
  action
  browserSettings
  browserSettings.colorManagement
  browsingData
  clipboard
  cloudFile
  commands
  compose
  composeAction
  contentScripts
  contextualIdentities
  cookies
  declarativeNetRequest
  dns
  downloads
  extension
  composeScripts
  messageDisplayScripts
  folders
  i18n
  identities
  identity
  idle
  mailTabs
  management
  menus
  messageDisplay
  messageDisplayAction
  messages
  messages.tags
  notifications
  permissions
  pkcs11
  privacy
  privacy.network
  privacy.services
  privacy.websites
  runtime
  scripting
  scripting.compose
  scripting.messageDisplay
  sessions
  spaces
  storage
  tabs
  theme
  userScripts
  messengerUtilities
  webNavigation
  webRequest
  windows

.. _Examples:

.. toctree::
  :glob:
  :maxdepth: 1
  :caption: Examples

  examples/*

.. _Experiments:

.. toctree::
  :maxdepth: 1
  :caption: Experiment APIs

  experiments/introduction
  experiments/generator
  experiments/folders_and_messages
  experiments/tabs_and_windows
  experiments/contribute

.. _ChangeLog:

.. toctree::
  :maxdepth: 1
  :caption: Changelog

  changes/140
  changes/128


Where to get help and more information
======================================

`Introduction to add-on development`__
  Find information about creating and updating extensions for Thunderbird. Includes getting-started-tutorials and a collection of helpful articles and guides.

`Add-on developer community`__
  Learn how to get in touch with other Thunderbird add-on developers, to ask questions and to share knowledge.
  
`Sample extensions`__ 
  A collection of MailExtensions, showing how to use Thunderbird WebExtension APIs.
  
`MDN sample extensions`__
  A collection of WebExtensions, showing how to use WebExtension APIs in Firefox. They probably won't work directly in Thunderbird, but they may provide hints on how to use some of the WebExtension APIs that Thunderbird inherited from Firefox.

`MDN WebExtension documentation`__
  Find general information about the WebExtensions API cross-browser technology used by Firefox and many Chromium-based browsers. Not all information listed there apply to Thunderbird.

__ https://developer.thunderbird.net/add-ons/
__ https://developer.thunderbird.net/add-ons/community
__ https://github.com/thunderbird/sample-extensions
__ https://github.com/mdn/webextensions-examples
__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions
