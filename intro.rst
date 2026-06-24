.. container:: sticky-sidebar
  
  ≡ On this page
  
  * `Guides Overview`_
  * `Where to get help and more information`_

  .. include:: _includes/developer-resources.rst

===========================================================================
WebExtension API Documentation & Guides (Thunderbird Beta 152, Manifest V2)
===========================================================================

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

:doc:`guides/vendoring`
  Learn how to bundle third-party libraries into your add-on and declare them so
  reviewers can verify the sources are unmodified and automated tooling can audit
  them for known vulnerabilities. This guide covers the trusted source
  requirements and both accepted declaration formats: a ``VENDOR.md`` file and a
  version-pinned ``package.json``.

:doc:`guides/innerHTML`
  Understand why ``innerHTML`` is discouraged in Thunderbird WebExtensions and which
  safer patterns to use instead. This guide covers alternatives such as
  ``textContent``, ``createElement()``, templates, and diffing libraries, replacing
  inline event handlers with real listeners, and safely rendering external or
  user-provided markup. On Thunderbird 153 and later this uses the built-in
  ``Sanitizer API`` through ``Element.setHTML()``, with ``DOMPurify`` and
  ``insertAdjacentHTML()`` as the fallback for older versions.
  
:doc:`guides/eventListeners`
  Attach listeners to Thunderbird WebExtension events with
  ``addListener()``. This guide shows how to register both named and anonymous
  listener functions, how to read the parameters an event passes to its listener,
  and how to use the extra ``addListener()`` arguments that some events accept, such
  as ``monitorAllFolders`` on ``messages.onNewMailReceived``.
 
:doc:`guides/runtimeMessaging`
  See how different parts of a Thunderbird WebExtension communicate using runtime
  messages. This guide explains how to register ``runtime.onMessage`` listeners and
  send messages between scripts, common quirks to be aware of, and how multiple
  listeners coordinate their responses.
  
:doc:`guides/messageLists`
  Discover how to efficiently work with large mail folders in Thunderbird
  WebExtensions. This guide explains how message lists are paginated so a single
  query does not load thousands of messages at once, how to walk through the pages
  returned by the API, and how to iterate over messages with generators. It also
  covers running asynchronous queries, handling auto-pagination, and safely aborting
  an ongoing query to keep performance and memory use under control.

:doc:`guides/vcard`
  Explore how to manage Thunderbird contacts, which are stored as vCards and exposed
  through the ``vCard`` property. This guide recommends parsing and editing them with
  the same ``ical.js`` library Thunderbird itself uses, shows how to bundle it and
  import it from a module background script, and how to read and update individual
  vCard fields safely. It also points to :doc:`guides/vendoring` for declaring the
  bundled library.



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
