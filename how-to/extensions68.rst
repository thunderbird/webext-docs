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

Required Changes for Thunderbird 68
===================================

At this point I'll attempt to list the changes many extensions will need for compatibility with
Thunderbird 68. I'll probably miss something you need, because it is simply impossible to stay on
top of everything. (Remember Thunderbird is based on the Firefox code, and they have been changing
things all over the place.)

Required Changes for Overlay Extensions
---------------------------------------

Switch to JSON Manifest
```````````````````````

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
specify a chrome URL.

The key ``open_in_tab`` is optional and defaults to value ``false``. Value ``true`` corresponds to 
optionsType 3 in install.rdf. 

Examples of overlay extension converted like this are:
 - `Mail Redirect <https://addons.thunderbird.net/de/thunderbird/addon/mailredirect/>`_ 

The above example JSON manifest is only in English. You probably want to use translated strings
in your manifest. Read `this MDN article about it`__. Unfortunately that means you now need two
sets of translated strings, one (that you already have) for your extension and another for the manifest.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Internationalization#Internationalizing_manifest.json

.. note::

  It *is* possible to have both ``install.rdf`` and ``manifest.json`` files in your extension, so
  you *could* release a version compatible with Thunderbird 60 and 68. I **do not** recommend it.


Chrome Manifest
```````````````

If you have a ``chrome.manifest``, some things have changed. Notably, ``overlay`` and ``style``
lines are now handled by the new overlay loader. You'll see this line in the Error Console:

.. code-block:: text

  Ignoring unrecognized chrome manifest directive 'overlay'.

It comes from the old system, which no longer deals with such things.

You might see the same line, but regarding ``interfaces``. Registering your own interfaces using
``.xpt`` files is no longer possible.

Overlays
````````

We switched to a completely new overlay loader in Thunderbird 63. While we tried to retain parity
with the old overlay loader, some things no longer work the way they used to, or at all.

For Thunderbird itself overlays have been progressively removed. By version 63, there are no overlays
left, so extensions can of course not overlay the removed Thunderbird overlays any more. 
For example, if your add-on overlaid ``mailWindowOverlay.xul``, that needs to be changed; in this 
example you most likely need to overlay ``messenger.xul`` now. 


``<script>`` Tags
"""""""""""""""""

``<script>`` tags are no longer inserted into the overlaid document. Scripts in an overlay are run
*after* the application of the overlay, regardless of their position in the overlay.

You may be used to putting the contents of a script directly in a document. This currently still
works but it may break in the future. **Inline scripts are strongly discouraged.** Use a file
instead.


Required Changes for all Extension Types
----------------------------------------

Removed XUL Elements
````````````````````
Some XUL elements no longer exist. Here are some I'm aware of:

- ``<listbox>`` and friends - use ``<richlistbox>`` (`migration example <https://github.com/jobisoft/CategoryManager/commit/2267888be7de0d7ebe4f5b4626c48210c071b16f/>`_)
- ``<colorpicker>`` - use HTML ``<input type="color">``
- ``<progressmeter>`` - use HTML ``<progress>`` (`migration example <https://github.com/jobisoft/CategoryManager/commit/be23d9abfba29e5585d485348d84bd36c3c6bcaf/>`_)
- ``<textbox type="number">`` - use HTML ``<input type="number">``
- ``<menulist editable="true">`` - use the new custom element ``<menulist is="menulist-editable" editable="true">``

.. note::

  In order to use custom elements, you need load customElements.js in your XUL: 
  ``<script type="application/javascript" src="chrome://messenger/content/customElements.js"/>``
  
  For the editable menulist you also need to load menulist.css in your XUL:
  ``<?xml-stylesheet href="chrome://messenger/content/menulist.css" type="text/css"?>``
  
  An editable menulist can also be created via JavaScript:
  .. code-block:: javascript
    let menulist = document.createElement("menulist", { is : "menulist-editable"});
    menulist.setAttribute("is", "menulist-editable");
    menulist.setAttribute("editable", "true");
  

Note that the replacements listed here might work in subtly different ways. Check your
functionality!

Removed XUL Element methods
```````````````````````````
These removals are related to the removal of the listbox element:

- ``.insertItemAt(index)` - use ``.insertBefore()``
- ``.removeItemAt(index)` - use ``.getItemAtIndex(index).remove()``

Renamed Files
`````````````
- ``mailServices.js`` has been renamed to ``MailServices.jsm``. The old name keeps working for now, 
  but you get a deprecation warning in the error console if you use the old name.

Removed Interfaces
``````````````````
- ``nsIStringBundleService``(XUL stringbundleset / stringbundle) - use ``Services.strings.createBundle(...)``

.. note::

  In order to use stringbundles, you need to load stringbundle.js in your XUL: 
  <script type="application/x-javascript" src="chrome://global/content/elements/stringbundle.js"/>,
  For overlay extensions the XUL Overlay loader takes care of this. See also bug 1459743

 

XBL
```

XBL is on Death Row. Many XBL bindings have been replaced or simply no longer exist. The remainder
are being removed. This may result in slight behaviour changes for some UI components.

If you have your own XBL bindings, you should get rid of them. Mostly the Firefox and Thunderbird
teams are using `custom elements`__ instead.

__ https://developer.mozilla.org/en-US/docs/Web/Web_Components/Custom_Elements


Javascript Module Imports
`````````````````````````

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

``ChromeUtils.import`` is a replacement for ``Components.utils.import`` (which was also changed)
in this way. Note that no second argument is supplied. The returned object is a dictionary of only
the objects listed in ``EXPORTED_SYMBOLS``.
