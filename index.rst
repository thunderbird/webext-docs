==========================================
Thunderbird WebExtension API Documentation
==========================================

These documents assume you already have some familiarity with the WebExtension technology. If not, it is
highly recommended to read our `Guide to MailExtensions`__ or some of the `MDN documentation on the subject`__.

__ https://developer.thunderbird.net/add-ons/mailextensions
__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions

.. hint::

  In Thunderbird, all WebExtension API can be accessed through the *browser.\** namespace, as with Firefox,
  but also through the  *messenger.\** namespace, which is a better fit for Thunderbird.

.. important::

  WebExtension APIs are asynchronous, that is, they return a `Promise`__ object which resolves when
  ready. See `Using Promises`__ for more information about Promises.

__ https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
__ https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises


This documentation includes the following topics:

 * `Thunderbird WebExtension APIs`_
 * `Firefox WebExtension APIs supported by Thunderbird`_
 * :ref:`HowToGuide`
 * `Where To Get Help And More Information`_

For any problems or feature requests please `file a bug`__.

__ https://bugzilla.mozilla.org/enter_bug.cgi?product=Thunderbird&component=Add-Ons%3A+Extensions+API




Thunderbird WebExtension APIs
=============================

Thunderbird provides the following messenger related WebExtension APIs, which are sometimes referred to as MailExtension APIs:

+-------------------------------+------------------------------------------------------------+
| Thunderbird API               | Description                                                |
+===============================+====================+=======================================+
| :doc:`accounts`               | |accounts-Description|                                     |
+-------------------------------+------------------------------------------------------------+
| :doc:`addressBooks`           | |addressBooks-Description|                                 |
+-------------------------------+------------------------------------------------------------+
| :doc:`addressBooks.provider`  | |addressBooksProvider-Description|                         |
+-------------------------------+------------------------------------------------------------+
| :doc:`browserAction`          | |browserAction-Description|                                |
+-------------------------------+------------------------------------------------------------+
| :doc:`cloudFile`              | |cloudFile-Description|                                    |
+-------------------------------+------------------------------------------------------------+
| :doc:`commands`               | |commands-Description|                                     |
+-------------------------------+------------------------------------------------------------+
| :doc:`compose`                | |compose-Description|                                      |
+-------------------------------+------------------------------------------------------------+
| :doc:`composeAction`          | |composeAction-Description|                                |
+-------------------------------+------------------------------------------------------------+
| :doc:`composeScripts`         | |composeScripts-Description|                               |
+-------------------------------+------------------------------------------------------------+
| :doc:`contacts`               | |contacts-Description|                                     |
+-------------------------------+------------------------------------------------------------+
| :doc:`folders`                | |folders-Description|                                      |
+-------------------------------+------------------------------------------------------------+
| :doc:`identities`             | |identities-Description|                                   |
+-------------------------------+------------------------------------------------------------+
| :doc:`mailingLists`           | |mailingLists-Description|                                 |
+-------------------------------+------------------------------------------------------------+
| :doc:`mailTabs`               | |mailTabs-Description|                                     |
+-------------------------------+------------------------------------------------------------+
| :doc:`menus`                  | |menus-Description|                                        |
+-------------------------------+------------------------------------------------------------+
| :doc:`messageDisplay`         | |messageDisplay-Description|                               |
+-------------------------------+------------------------------------------------------------+
| :doc:`messageDisplayAction`   | |messageDisplayAction-Description|                         |
+-------------------------------+------------------------------------------------------------+
| :doc:`messageDisplayScripts`  | |messageDisplayScripts-Description|                        |
+-------------------------------+------------------------------------------------------------+
| :doc:`messages`               | |messages-Description|                                     |
+-------------------------------+------------------------------------------------------------+
| :doc:`spacesToolbar`          | |spacesToolbar-Description|                                |
+-------------------------------+------------------------------------------------------------+
| :doc:`tabs`                   | |tabs-Description|                                         |
+-------------------------------+------------------------------------------------------------+
| :doc:`theme`                  | |theme-Description|                                        |
+-------------------------------+------------------------------------------------------------+
| :doc:`windows`                | |windows-Description|                                      |
+-------------------------------+------------------------------------------------------------+
  
.. |accounts-Description| replace:: Enables an extension to access information of accounts and identities configured in Thunderbird's account manager.
.. |addressBooks-Description| replace:: Enables an extension to access, modify, create and delete Thunderbird address books.
.. |addressBooksProvider-Description| replace:: Allows to implement address books whose storage and entries are not handled by Thunderbird but by the extension.
.. |browserAction-Description| replace:: Enables an extension to interact with a `browser action button`_. 
.. |cloudFile-Description| replace:: Enables an extension to register a cloudFile provider, which can be used to upload large attachments to a server, instead of attaching them directly to the email.
.. |commands-Description| replace:: The commands API adds keyboard shortcuts that can trigger actions in an extension.
.. |compose-Description| replace:: Enables an extension to open a new message compose window or react to events while the message is being composed.
.. |composeAction-Description| replace:: Enables an extension to interact with a `compose action button`_.
.. |composeScripts-Description| replace:: Functionally is the same as the contentScripts API except that it works on the document of email messages during composition.
.. |contacts-Description| replace:: Enables an extension to access, modify, create and delete contacts in Thunderbird address books.
.. |folders-Description| replace:: Enables an extension to access, modify, create and delete mail account folders.
.. |identities-Description| replace:: Enables an extension to create, modify and delete mail account identities.
.. |theme-Description| replace:: The theme API can be used to create static or dynamic Thunderbird themes. Theme experiments are supported.
.. |mailingLists-Description| replace:: Enables an extension to access, modify, create and delete mailing lists in Thunderbird address books.
.. |mailTabs-Description| replace:: Enables an extension to interact with Thunderbird's main window.
.. |menus-Description| replace:: Enables an extension to add (context-) menu entries to Thunderbird menus.
.. |messageDisplay-Description| replace:: Enables an extension to react on and interact with the currently displayed messages.
.. |messageDisplayAction-Description| replace:: Enables an extension to interact with a `message display action button`_. 
.. |messageDisplayScripts-Description| replace:: Functionally is the same as the contentScripts API except that it works on the document of email messages being displayed.
.. |messages-Description| replace:: Enables an extension to list, search, read, copy, move and delete messages.
.. |spacesToolbar-Description| replace:: Enables an extension to interact with Thunderbird's spaces toolbar.
.. |tabs-Description| replace:: Enables an extension to interact with Thunderbird's tab system. It allows to create, modify, and rearrange tabs and to communicate with scripts in tabs.
.. |windows-Description| replace:: Enables an extension to interact with Thunderbird's windows which can contain webpage tabs and also with other window types like composer or address books that cannot contain webpage tabs. You can use this API to create, modify, and rearrange windows.

.. _`browser action button`: https://developer.thunderbird.net/add-ons/mailextensions/supported-ui-elements#browser-action
.. _`compose action button`: https://developer.thunderbird.net/add-ons/mailextensions/supported-ui-elements#compose-action
.. _`message display action button`: https://developer.thunderbird.net/add-ons/mailextensions/supported-ui-elements#message-display-action

The documentation for these APIs is generated automatically from the schema documents at
`mail/components/extensions/schemas`__.

__ https://hg.mozilla.org/comm-central/file/tip/mail/components/extensions/schemas/

Firefox WebExtension APIs supported by Thunderbird
==================================================

As Thunderbird is based on Firefox, many of its WebExtension APIs can be used in Thunderbird
as well. The APIs listed in the following table are known to work with Thunderbird.

.. note::

  The following APIs link to their MDN description pages. Please be aware, that MDN
  is dedicated to web browsers (not limited to Firefox). Some information listed on MDN
  may not apply to Thunderbird and some API methods may not be supported. Each API
  page should include a compatibility chart and if that includes support for Firefox,
  it should work in Thunderbird as well. 

+-----------------------------+------------------------------------------------------------+
| Firefox API                 | Description                                                |
+=============================+====================+=======================================+
| `browserSettings`_          | |browserSettings-Description|                              |
+-----------------------------+------------------------------------------------------------+
| `clipboard`_                | |clipboard-Description|                                    |
+-----------------------------+------------------------------------------------------------+
| `contentScripts`_           | |contentScripts-Description|                               |
+-----------------------------+------------------------------------------------------------+
| `cookies`_                  | |cookies-Description|                                      |
+-----------------------------+------------------------------------------------------------+
| `dns`_                      | |dns-Description|                                          |
+-----------------------------+------------------------------------------------------------+
| `downloads`_                | |downloads-Description|                                    |
+-----------------------------+------------------------------------------------------------+
| `extension`_                | |extension-Description|                                    |
+-----------------------------+------------------------------------------------------------+
| `i18n`_                     | |i18n-Description|                                         |
+-----------------------------+------------------------------------------------------------+
| `identity`_                 | |identity-Description|                                     |
|                             |                                                            |
|                             | *Added in Thunderbird 78.0b2*                              |
+-----------------------------+------------------------------------------------------------+
| `idle`_                     | |idle-Description|                                         |
+-----------------------------+------------------------------------------------------------+
| `privacy`_                  | |privacy-Description|                                      |
+-----------------------------+------------------------------------------------------------+
| `management`_               | |management-Description|                                   |
+-----------------------------+------------------------------------------------------------+
| `notifications`_            | |notifications-Description|                                |
+-----------------------------+------------------------------------------------------------+
| `permissions`_              | |permissions-Description|                                  |
+-----------------------------+------------------------------------------------------------+
| `protocol_handlers`_        | |protocol_handlers-Description|                            |
+-----------------------------+------------------------------------------------------------+
| `pkcs11`_                   | |pkcs11-Description|                                       |
+-----------------------------+------------------------------------------------------------+
| `proxy`_                    | |proxy-Description|                                        |
+-----------------------------+------------------------------------------------------------+
| `runtime`_                  | |runtime-Description|                                      |
+-----------------------------+------------------------------------------------------------+
| `storage`_                  | |storage-Description|                                      |
+-----------------------------+------------------------------------------------------------+
| `userScripts`_              | |userScripts-Description|                                  |
+-----------------------------+------------------------------------------------------------+
| `webNavigation`_            | |webNavigation-Description|                                |
+-----------------------------+------------------------------------------------------------+
| `webRequest`_               | |webRequest-Description|                                   |
+-----------------------------+------------------------------------------------------------+

.. _browserSettings: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/browserSettings
.. _clipboard: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/clipboard
.. _contentScripts: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts
.. _cookies: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/cookies
.. _dns: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/dns
.. _downloads: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/downloads
.. _extension: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension
.. _i18n: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n
.. _identity: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/identity
.. _idle: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/idle
.. _privacy: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/privacy
.. _management: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/management
.. _notifications: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/notifications
.. _permissions: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/permissions
.. _pkcs11: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pkcs11
.. _protocol_handlers: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/protocol_handlers
.. _proxy: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/proxy
.. _runtime: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime
.. _storage: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/storage
.. _userScripts: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/userScripts
.. _webNavigation: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webNavigation
.. _webRequest: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/webRequest

.. |browserSettings-Description| replace:: Enables an extension to modify certain global browser settings. Because these are global settings, it's possible for extensions to conflict. See the documentation for *BrowserSetting.set()* for details of how conflicts are handled.
.. |clipboard-Description| replace:: Enables an extension to copy items to the system clipboard. Currently the API only supports copying images, but it's intended to support copying text and HTML in the future. 
.. |contentScripts-Description| replace:: Use this API to register content scripts to instruct the browser to insert the given content scripts into pages that match the URL patterns specified during registration. In Thunderbird, content scripts can only be used in web pages loaded into tabs. 
.. |cookies-Description| replace:: Enables an extension to get and set cookies, and be notified when they change.
.. |dns-Description| replace:: Enables an extension to resolve domain names.
.. |downloads-Description| replace:: Enables extensions to save files to disk.
.. |extension-Description| replace:: Utilities related to an extension. Gets URLs to resources packages with an extension. Gets the Window object for some of the extension's pages. Get the values for various settings.
.. |i18n-Description| replace:: Functions to internationalize an extension. It can be used to get localized strings from locale files packaged with an extension and to find out Thunderbird's current language.
.. |identity-Description| replace:: Use the identity API to get an OAuth2 authorization code or access token, which an extension can then use to access user data from a service that supports OAuth2 access (such as Google or Facebook).
.. |idle-Description| replace:: Find out when the user's system is idle, locked, or active.
.. |privacy-Description| replace:: Access and modify various privacy-related settings.
.. |management-Description| replace:: Gets information about installed add-ons.
.. |notifications-Description| replace:: Display notifications to the user, using the underlying operating system's notification mechanism.
.. |permissions-Description| replace:: Enables extensions to request extra permissions at runtime, after they have been installed.
.. |pkcs11-Description| replace:: Enables an extension to enumerate PKCS #11 security modules and to make them accessible as sources of keys and certificates.
.. |protocol_handlers-Description| replace:: Using this manifest key will register one or more web-based protocol handlers. It allows to register a website or an extension page as a handler for a particular protocol.
.. |proxy-Description| replace:: Enables an extension to proxy web requests. Use the *proxy.onRequest* event listener to intercept web requests, and return an object that describes whether and how to proxy them.
.. |runtime-Description| replace:: This module provides information about the extension and the environment it's running in. It also provides messaging APIs to communicate between different parts of the extension, communicate with other extensions and communicate with native applications.
.. |storage-Description| replace:: Enables extensions to store and retrieve data, and listen for changes to stored items.
.. |userScripts-Description| replace:: Use this API to register user scripts, third-party scripts designed to manipulate webpages or provide new features. Registering a user script instructs the browser to attach the script to pages that match the URL patterns specified during registration. In Thunderbird, user scripts can only be used in web pages loaded into tabs. This API offers similar capabilities to contentScripts but with features suited to handling third-party scripts.
.. |webNavigation-Description| replace:: Add event listeners for the various stages of a navigation. A navigation consists of a frame in the browser transitioning from one URL to another, usually (but not always) in response to a user action like clicking a link.
.. |webRequest-Description| replace:: Add event listeners for the various stages of making an HTTP request, which includes websocket requests on ws:// and wss://. The event listener receives detailed information about the request and can modify or cancel the request.

.. toctree::
  :hidden:
  :caption: API Documentation
  
  accounts
  addressBooks
  addressBooks.provider
  browserAction
  cloudFile
  commands
  compose
  composeAction
  composeScripts
  contacts
  folders
  identities
  mailingLists
  mailTabs
  menus
  messageDisplay
  messageDisplayAction
  messageDisplayScripts
  messages
  spacesToolbar
  theme
  tabs
  windows

.. _HowToGuide:

.. toctree::
  :maxdepth: 1
  :caption: How To Guides

  how-to/contacts
  how-to/eventListeners
  how-to/messageLists
  how-to/experiments

.. toctree::
  :glob:
  :hidden:
  :caption: Changes to APIs

  changes/*

Where To Get Help And More Information
======================================

`Thunderbird add-on developer documentation`__
  Find information about creating and updating extensions for Thunderbird. Includes getting-started-tutorials and a collection of helpful articles and guides.

`Thunderbird add-on developer community`__
  Learn how to get in touch with other add-on developers, to ask questions and to share knowledge.
  
`Thunderbird sample extensions`__ 
  A collection of MailExtensions, showing how to use Thunderbird WebExtension APIs.
  
`MDN sample extensions`__
  A collection of WebExtensions, showing how to use WebExtension APIs. They probably won't work directly in Thunderbird, but they may provide hints on how to use some of the WebExtension APIs that Thunderbird inherited from Firefox.

`MDN WebExtension documentation`__
  Find general information about the WebExtensions API cross-browser technology used by Firefox and many Chromium-based browsers. Not all information listed there apply to Thunderbird.

__ https://developer.thunderbird.net/add-ons/
__ https://developer.thunderbird.net/add-ons/community
__ https://github.com/thundernest/sample-extensions
__ https://github.com/mdn/webextensions-examples
__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions
