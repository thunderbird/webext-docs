.. container:: sticky-sidebar
  
  ≡ On this page
  
  * `Guides Overview`_
  * `Where to get help and more information`_

  .. include:: _includes/developer-resources.rst

======================================================================
WebExtension API Documentation & Guides (Thunderbird 144, Manifest V2)
======================================================================

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
Thunderbird's schema files. The `webext-schemas <https://github.com/thunderbird/webext-annotated-schemas>`__
repository can be used to obtain a copy of the relevant files.

Guides Overview
===============

:doc:`guides/eventListeners`
  Learn how to attach listeners to Thunderbird WebExtension events and respond to user actions or changes in the application. This guide covers handling event parameters, working with events that provide additional options, and offers best practices for implementing event listeners.
 
:doc:`guides/messageLists`
  Discover how to efficiently work with large mail folders in Thunderbird WebExtensions. This guide explains how message lists are paginated to handle thousands of messages, how to retrieve pages of messages using the API, and how to iterate over messages using generators. It also covers executing asynchronous queries, handling auto-pagination, and safely aborting ongoing queries to manage performance and resource usage.
 
:doc:`guides/vcard`
  Explore how to manage Thunderbird contacts using the vCard format. This section explains how to work with legacy and modern contact properties, update individual fields safely, and manipulate vCards directly using the `ical.js` library. Best practices are provided for reading, modifying, and storing contact information while avoiding common pitfalls with legacy property mappings.



:doc:`guides/experiments`
  Understand how to extend Thunderbird with custom Experiment APIs. This section covers declaring Experiments in the manifest, implementing their functions and events, and managing native tabs and native windows through the extension context. It also provides guidance on integrating these APIs safely alongside Thunderbird's built-in WebExtension features.
 
Where to get help and more information
======================================

`Introduction to add-on development`__
  Find information about creating and updating extensions for Thunderbird. Includes getting-started-tutorials and a collection of helpful articles and guides.

`Add-on developer community`__
  Learn how to get in touch with other Thunderbird add-on developers, to ask questions and to share knowledge.
  
`Example extensions`__ 
  A collection of WebExtensions, showing how to use Thunderbird WebExtension APIs.
  
`MDN sample extensions`__
  A collection of WebExtensions, showing how to use WebExtension APIs in Firefox. They probably won't work directly in Thunderbird, but they may provide hints on how to use some of the WebExtension APIs that Thunderbird inherited from Firefox.

`MDN WebExtension documentation`__
  Find general information about the WebExtensions API cross-browser technology used by Firefox and many Chromium-based browsers. Not all information listed there apply to Thunderbird.

__ https://developer.thunderbird.net/add-ons/
__ https://developer.thunderbird.net/add-ons/community
__ https://github.com/thunderbird/webext-examples
__ https://github.com/mdn/webextensions-examples
__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions
