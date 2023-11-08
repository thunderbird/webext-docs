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
 * `Firefox WebExtension APIs`_
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
| :doc:`contacts`               | |contacts-Description|                                     |
+-------------------------------+------------------------------------------------------------+
| :doc:`folders`                | |folders-Description|                                      |
+-------------------------------+------------------------------------------------------------+
| :doc:`legacy`                 | |legacy-Description|                                       |
+-------------------------------+------------------------------------------------------------+
| :doc:`mailingLists`           | |mailingLists-Description|                                 |
+-------------------------------+------------------------------------------------------------+
| :doc:`mailTabs`               | |mailTabs-Description|                                     |
+-------------------------------+------------------------------------------------------------+
| :doc:`menus`                  | |menus-Description|                                        |
+-------------------------------+------------------------------------------------------------+
| :doc:`messageDisplay`         | |messageDisplay-Description|                               |
+-------------------------------+------------------------------------------------------------+
| :doc:`messages`               | |messages-Description|                                     |
+-------------------------------+------------------------------------------------------------+
| :doc:`tabs`                   | |tabs-Description|                                         |
+-------------------------------+------------------------------------------------------------+
| :doc:`windows`                | |windows-Description|                                      |
+-------------------------------+------------------------------------------------------------+
  
.. |accounts-Description| replace:: Enables an extension to access information of accounts and identities configured in Thunderbird's account manager.
.. |addressBooks-Description| replace:: Enables an extension to access, modify, create and delete Thunderbird address books.
.. |browserAction-Description| replace:: Enables an extension to interact with a `browser action button`_. 
.. |cloudFile-Description| replace:: Enables an extension to register a cloudFile provider, which can be used to upload large attachments to a server, instead of attaching them directly to the email.
.. |commands-Description| replace:: The commands API adds keyboard shortcuts that can trigger actions in an extension.
.. |compose-Description| replace:: Enables an extension to open a new message compose window or react to events while the message is being composed.
.. |composeAction-Description| replace:: Enables an extension to interact with a `compose action button`_.
.. |contacts-Description| replace:: Enables an extension to access, modify, create and delete contacts in Thunderbird address books.
.. |folders-Description| replace:: Enables an extension to access, modify, create and delete mail account folders.
.. |legacy-Description| replace:: This API enables Thunderbird “legacy” extensions to continue working in the WebExtensions world. 
.. |mailingLists-Description| replace:: Enables an extension to access, modify, create and delete mailing lists in Thunderbird address books.
.. |mailTabs-Description| replace:: Enables an extension to interact with Thunderbird's main window.
.. |menus-Description| replace:: Enables an extension to add (context-) menu entries to Thunderbird menus.
.. |messageDisplay-Description| replace:: Enables an extension to react on and interact with the currently displayed messages.
.. |messages-Description| replace:: Enables an extension to list, search, read, copy, move and delete messages.
.. |tabs-Description| replace:: Enables an extension to interact with Thunderbird's tab system. It allows to create, modify, and rearrange tabs and to communicate with scripts in tabs.
.. |windows-Description| replace:: Enables an extension to interact with Thunderbird's windows which can contain webpage tabs and also with other window types like composer or address books that cannot contain webpage tabs. You can use this API to create, modify, and rearrange windows.

.. _`browser action button`: https://developer.thunderbird.net/add-ons/mailextensions/supported-ui-elements#browser-action
.. _`compose action button`: https://developer.thunderbird.net/add-ons/mailextensions/supported-ui-elements#compose-action
.. _`message display action button`: https://developer.thunderbird.net/add-ons/mailextensions/supported-ui-elements#message-display-action

The documentation for these APIs is generated automatically from the schema documents at
`mail/components/extensions/schemas`__.

__ https://hg.mozilla.org/comm-central/file/tip/mail/components/extensions/schemas/

Firefox WebExtension APIs
=========================

As Thunderbird is based on Firefox, many of its WebExtension APIs can be used in Thunderbird
as well. The APIs listed in the following table are known to work with Thunderbird.

.. note::

  The following APIs link to their MDN description pages. Please be aware, that MDN
  is dedicated to web browsers (not limited to Firefox). Some information listed on MDN
  may not apply to Thunderbird and some API methods may not be supported. Each API
  page should include a compatibility chart and if that includes support for Firefox,
  it should work in Thunderbird as well. 

- `contentScripts <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts>`_
- `experiments <https://firefox-source-docs.mozilla.org/toolkit/components/extensions/webextensions/basics.html#webextensions-experiments>`_
- `extension <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extension>`_
- `i18n <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/i18n>`_
- `management <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/management>`_
- `permissions <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/permissions>`_
- `pkcs11 <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/pkcs11>`_
- `runtime <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime>`_
- `theme <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/theme>`_

.. toctree::
  :hidden:
  :caption: API Documentation
  
  accounts
  addressBooks
  browserAction
  cloudFile
  commands
  compose
  composeAction
  contacts
  folders
  legacy
  mailingLists
  mailTabs
  menus
  messageDisplay
  messageDisplayAction
  messages
  tabs
  windows
  
.. _HowToGuide:

.. toctree::
  :maxdepth: 1
  :caption: How To Guides

  how-to/eventListeners
  how-to/messageLists
  how-to/experiments

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
__ https://github.com/thunderbird/sample-extensions
__ https://github.com/mdn/webextensions-examples
__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions
