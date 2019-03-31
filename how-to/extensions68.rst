======================================
Updating Extensions for Thunderbird 68
======================================

Since Thunderbird 60 was released, there have been many major changes to Thunderbird's core.
Almost every extension will require modifications for compatibility with the next Thunderbird, 68.
Some changes are trivial, others not.

This is an overview of some of the major changes we know about. It would be impossible to list all
of the changes. Since the release of Thunderbird 60, Bugzilla has another 50,000 bugs on file.
(Fortunately most of them are not bugs, it's just a term we use.) If just 1% of them affected
Thunderbird extensions, this would be a very long document.

Terminology
===========

Before going any further, here's some of the terminology I'll use in this document:

Overlay extension
  The original type of extension for Thunderbird and Firefox. This type uses documents that overlay
  Thunderbird UI, adding and modifying it. Uses an RDF manifest (``install.rdf``) and requires a
  restart of Thunderbird for installation/uninstallation, upgrading/downgrading and
  enabling/disabling.

Overlay loader
  This is a Thunderbird component that takes the code as written in an overlay extension and
  applies it to the UI. In Thunderbird 60, this was a part of the core Thunderbird UI libary, but
  it was removed. We built a new overlay loader to replace as much of the removed code as possible,
  but there are differences. More on this later.

Bootstrapped extension
  Uses a bootstrap file (``bootstrap.js``) as an entry point to the extension. The file defines
  four methods (``install``, ``uninstall``, ``startup``, and ``shutdown``) from which all extension
  behaviour is controlled. This type of extension can be installed or shut down without restarting
  Thunderbird, so it's sometimes called a "restartless" extension. Also uses an RDF manifest
  (``install.rdf``).

Legacy extension
  Refers to either an overlay extension or a bootstrapped extension.

WebExtension
  This is the current type of extension used by Firefox and Chrome. We have adapted the technology
  for use on Thunderbird and added some features specific to Thunderbird. Unlike legacy extensions,
  a WebExtension does *not* have complete access to Thunderbird's internal components and UI, but
  accesses functionality through APIs. Uses a JSON manifest (``manifest.json``).

  There is some talk of calling WebExtensions on Thunderbird "MailExtensions". You may see that
  term in various places, but it means the same thing.

The Future
==========

It's difficult to say for sure what the future will hold for Thunderbird extensions. A *lot* of
work has been done to ensure all three types of extension will work in Thunderbird 68. Beyond that,
we just don't know.

Overlay extensions are problematic because so much of what they depended on no longer exists.
Bootstrapped extensions are less of a problem but are still considered at-risk.

Changes Required
================

At this point I'll attempt to list the changes many extensions will need for compatibility with
Thunderbird 68. I'll probably miss something you need, because it is simply impossible to stay on
top of everything. (Remember Thunderbird is based on the Firefox code, and they have been changing
things all over the place.)

Switch to JSON Manifest
-----------------------

.. note::

  This should *not* be done to bootstrapped extensions.

To use the new overlay loader, overlay extensions *must* switch from an RDF manifest to a `JSON
manifest`__. As far as the software is concerned, this effectively makes the overlay extension into
a WebExtension.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json

Here's a basic example. This install manifest:

.. code-block:: xml

  <?xml version="1.0" encoding="utf-8"?>
  <RDF xmlns="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
       xmlns:em="http://www.mozilla.org/2004/em-rdf#">
    <Description about="urn:mozilla:install-manifest">
      <em:id>myextension@sample.extensions.thunderbird.net</em:id>
      <em:type>2</em:type>
      <em:name>Extension</em:name>
      <em:description>Does a thing!</em:description>
      <em:version>1.0</em:version>
      <em:optionsURL>chrome://myextension/content/options.html</em:optionsURL>
      <em:optionsType>3</em:optionsType><!-- Options in a tab -->
      <em:targetApplication>
        <Description>
          <em:id>{3550f703-e582-4d05-9a08-453d09bdfdc6}</em:id>
          <em:minVersion>60.0</em:minVersion>
          <em:maxVersion>60.*</em:maxVersion>
        </Description>
      </em:targetApplication>
    </Description>
  </RDF>

becomes:

.. code-block:: json

  {
    "manifest_version": 2,
    "applications": {
      "gecko": {
        "id": "myextension@sample.extensions.thunderbird.net",
        "strict_min_version": "67.0a1"
      }
    },
    "name": "Extension",
    "description": "Does a thing",
    "version": "2.0",

    "legacy": {
      "options": {
        "page": "chrome://myextension/content/options.html",
        "open_in_tab": true
      }
    }
  }

Note the ``legacy`` key. It's a special key to engage Thunderbird's new overlay loader. The value
here could just be ``true``, but in this example there is an options page, so I put that
information in. This is similar to the standard WebExtension ``options_ui`` key, but you can
specify a chrome URL. The key ``open_in_tab`` is optional and defaults to value ``false``.
``true`` corresponds to optionsType 3 in install.rdf.

This example is only in English. You probably want to use translated strings in your manifest.
Read `this MDN article about it`__. Unfortunately that means you now need two sets of translated
strings, one (that you already have) for your extension and another for the manifest.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Internationalization#Internationalizing_manifest.json

Examples of overlay extension converted like this are:
 - `Open With <https://github.com/darktrojan/openwith/blob/VERSION_6.9/manifest.json>`_
 - `Shrunked Image Resizer <https://github.com/darktrojan/shrunked/blob/VERSION_4.5/manifest.json>`_

.. note::

  It *is* possible to have both ``install.rdf`` and ``manifest.json`` files in your extension, so
  you *could* release a version compatible with Thunderbird 60 and 68. I **do not** recommend it.

Chrome Manifest
---------------

If you have a ``chrome.manifest``, some things have changed. Notably, ``overlay`` and ``style``
lines are now handled by the new overlay loader. You'll see this line in the Error Console:

.. code-block:: text

  Ignoring unrecognized chrome manifest directive 'overlay'.

It comes from the old system, which no longer deals with such things.

You might see the same line, but regarding ``interfaces``. Registering your own interfaces using
``.xpt`` files is no longer possible.

Overlays
--------

We switched to a completely new overlay loader in Thunderbird 63. While we tried to retain parity
with the old overlay loader, some things no longer work the way they used to, or at all.

Overlays in Thunderbird itself (except the calendar extensions) have been removed, so extensions
can not overlay the removed Thunderbird overlays any more. For example, if your add-on overlaid
``mailWindowOverlay.xul``, that needs to be changed; in this example you most likely need to
overlay ``messenger.xul`` now.

``<script>`` Tags
"""""""""""""""""

``<script>`` tags are no longer inserted into the overlaid document. Scripts in an overlay are run
*after* the application of the overlay, regardless of their position in the overlay.

You may be used to putting the contents of a script directly in a document. This currently still
works but it may break in the future. **Inline scripts are strongly discouraged.** Use a file
instead.

Removed XUL Elements
--------------------

Some XUL elements no longer exist. Here are some I'm aware of:

- ``<colorpicker>`` - use ``<html:input type="color">``
- ``<listbox>`` and friends - use ``<richlistbox>``

  - ``.insertItemAt(index)`` no longer exists - use ``.insertBefore()``
  - ``.removeItemAt(index)`` no longer exists - use ``.getItemAtIndex(index).remove()``

- ``<prefwindow>``, ``<prefpane>``, ``<preferences>``, and ``<preference>``
- ``<progressmeter>`` - use ``<html:progress max="100">``
- ``<textbox type="number">`` - use ``<html:input type="number">``
- ``<textbox multiline="true">`` - use ``<html:textarea>``

In order to use HTML elements in your XUL, you must load the HTML namespace into your overlay
or dialog:

.. code-block:: xml

  <dialog
      xmlns:html="http://www.w3.org/1999/xhtml"
      xmlns="http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul"/>

Some widgets are now implemented as `custom elements`__ and may need some extra work.

For the most common example, the editable menulist is now a custom element, and it needs some
extra files to be linked from your document:

.. code-block:: xml

  <?xml version="1.0"?>
  <?xml-stylesheet type="text/css" href="chrome://global/skin/global.css"?>
  <!-- New stylesheet needed: -->
  <?xml-stylesheet type="text/css" href="chrome://messenger/skin/menulist.css"?>
  <!-- Annoyingly, in Thunderbird 66, you want chrome://messenger/content/menulist.css. -->

  <page xmlns="http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul">
    <!-- New script needed: -->
    <script type="application/javascript" src="chrome://messenger/content/customElements.js"/>

    <!-- Note the additional "is" attribute: -->
    <menulist is="menulist-editable" editable="true">
      <menupopup>
        <menuitem value="foo" label="foo"/>
        <menuitem value="bar" label="bar"/>
      </menupopup>
    </menulist>
  </page>

An editable menulist can also be created via JavaScript:

.. code-block:: javascript

  let menulist = document.createElement("menulist", { is : "menulist-editable" });
  menulist.setAttribute("is", "menulist-editable");
  menulist.setAttribute("editable", "true");

__ https://developer.mozilla.org/en-US/docs/Web/Web_Components/Custom_Elements

.. note::

  The replacements listed here might work in subtly different ways. Check your functionality!

XBL
---

XBL is on Death Row. Many XBL bindings have been replaced or simply no longer exist. The remainder
are being removed. This may result in slight behaviour changes for some UI components.

If you have your own XBL bindings, you should get rid of them. Mostly the Firefox and Thunderbird
teams are using `custom elements`__ instead.

__ https://developer.mozilla.org/en-US/docs/Web/Web_Components/Custom_Elements

Renamed Files
-------------

A number of Javascript modules have been renamed with the ``.jsm`` extension. Most notably:

- ``mailServices.js`` has been renamed to ``MailServices.jsm``. This change was originally
  backwards-compatible with a deprecation warning, but the changes to module importing (see below)
  made that pointless and the old file has now been removed completely.
- ``MailUtils.js`` is now ``MailUtils.jsm``.

Javascript Module Imports
-------------------------

In Thunderbird 67, a major backwards-incompatible change was made to importing javascript modules.
Where once you used any of these:

.. code-block:: javascript

  Components.utils.import("resource://foo/modules/Foo.jsm");
  // or…
  Cu.import("resource://foo/modules/Foo.jsm");
  // or…
  ChromeUtils.defineModuleGetter(this, "Foo", "resource://foo/modules/Foo.jsm");

Or the two-argument variation:

.. code-block:: javascript

  var { Foo } = Cu.import("resource://foo/modules/Foo.jsm", null);
  // or…
  var scope = {}; Cu.import("resource://foo/modules/Foo.jsm", scope); // scope.Foo…

You should now do this:

.. code-block:: javascript

  var { Foo } = ChromeUtils.import("resource://foo/modules/Foo.jsm");
  // or…
  var scope = ChromeUtils.import("resource://foo/modules/Foo.jsm"); // scope.Foo…

``ChromeUtils.import`` is a replacement for ``Components.utils.import`` (which was also changed
in this way). Note that no second argument is supplied. The returned object is a dictionary of
only the objects listed in ``EXPORTED_SYMBOLS``.

Network API Changes
-------------------

Thunderbird 67 made some incompatible changes to the network interface.

nsIStreamListener
"""""""""""""""""

The ``onDataAvailable`` method lost its ``context`` argument. This was removed in `bug 1525319`__
which breaks the API.

To be backward compatible you need to probe the parameters. In case the third parameter is an
nsIInputStream it is the old API. If the second one is an input stream it is the new API.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1525319

.. code-block:: javascript

  onDataAvailable(...args) {
    // The old API passes the stream as third parameter
    if (args[2] instanceof Ci.nsIInputStream)
      return this.onOldDataAvailableCalled(args[2], args[3], args[4]);

    // The new API uses the second parameter
    if (args[1] instanceof Ci.nsIInputStream)
      return this.onNewDataAvailableCalled(args[1], args[2], args[3]);

    throw new Error("Unknown signature for nsIStreamListener.onDataAvailable()");
  }

nsIRequestObserver
""""""""""""""""""

The ``onStartRequest`` and ``onStopRequest`` methods also no longer have a ``context`` argument,
which could be detected in a similar way.

nsIProtocolHandler
""""""""""""""""""

The obsolete method ``newChannel`` was removed and ``newChannel2`` was renamed to ``newChannel``.
(`Bug 1528971`__.)

As ``newChannel`` has been unused for a long time it should be safe to just replace the old
``newChannel`` implementation with the ``newChannel2`` and forward calls from ``newChannel2``.

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1528971

.. code-block:: javascript

  // Change the signature to the new one...
  // ... you'll need to add the loadInfo parameter
  //
  // Note loadInfo may be null in Thunderbird 60.
  newChannel(URI, loadInfo) {
    // Do your logic here
  }

  // Keep the old method as it will be needed for backward compatibility...
  // ... and forward the request to the new method.
  newChannel2(URI, loadInfo) {
    return this.newChannel(URI, loadInfo);
  }

.. note::

  Again, even though these examples show you *can* write code compatible with both Thunderbird 60
  and Thunderbird 68, that *doesn't mean you should*.

See Also
========

Some additional low-level details about things you may run into that have changed since Thunderbird 60 can be found `on the Thunderbird wiki <https://wiki.mozilla.org/Thunderbird/Add-ons_Guide_63#Removed_in_Thunderbird_60>`_.
