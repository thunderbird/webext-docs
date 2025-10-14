Strategies to avoid using ``innerHTML``
=======================================

The use of ``innerHTML`` is a fast and convenient way to create DOM nodes. The
problem is that it encourages a pattern where entire DOM trees are replaced instead
of being updated selectively. Even if it is only used for initial rendering, it
can easily lead to adopting the same pattern for updates later, which may cause
layout flicker, loss of state, and unnecessary re-rendering. Replacing an existing
DOM tree is highly inefficient; it is better to use explicit DOM manipulation
methods or data-driven rendering approaches instead. When possible, the approaches
described below that avoid using ``innerHTML`` entirely are preferred, as they
promote more stable and maintainable DOM updates. For example:

- ``textContent`` to safely replace text
- ``createElement()``, ``append()``, or templating functions to build new structures
- CSS or visibility toggles instead of rebuilding markup
- libraries such as `lighterhtml <https://github.com/WebReflection/lighterhtml>`__,
  which create DOM trees efficiently and update them via diffing instead of replacement

If external or user-provided HTML must be rendered, it has to be sanitized first
(for example, with `DOMPurify <https://github.com/cure53/DOMPurify>`__).
``insertAdjacentHTML()`` works well with sanitized markup and will also benefit
from the upcoming built-in `Sanitizer API <https://developer.mozilla.org/en-US/docs/Web/API/Sanitizer>`__,
allowing code to drop the extra sanitization step later without further restructuring.

.. note::

   Using ``innerHTML`` for one-time rendering is accepted for add-ons hosted on
   ATN when no updates are performed. However, the alternatives described in this
   guide are generally suggested.

More information on this topic is available on
`MDN <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Safely_inserting_external_content_into_a_page>`__.

Update content via ``span`` placeholders
----------------------------------------

Consider the following code:

.. code-block:: javascript
   :caption: popup.js

   const message = document.getElementById('message');
   message.innerHTML = `The following <b>${counts}</b> items have been found:`;

Here, ``innerHTML`` is used just to insert a formatted value. A better
approach is to include the static part directly in the markup and only
update the dynamic part.

.. code-block:: html
   :caption: popup.html

   <div id="message">
     The following <b><span data-msg="counts"></span></b> items have been found:
   </div>

.. code-block:: javascript
   :caption: popup.js

   document.querySelector('#message span[data-msg="counts"]').textContent = counts;

This avoids HTML parsing entirely and ensures the inserted value is
treated as plain text.

Update content by hiding/showing markup via CSS
-----------------------------------------------

Consider the following markup and code:

.. code-block:: html
   :caption: popup.html

   <div id="status"></div>

.. code-block:: javascript
   :caption: popup.js

   const statusElement = document.getElementById("status");
   if (error) {
     statusElement.innerHTML = `<div class="red">Something went wrong: ${error}</div>`;
   } else {
     statusElement.innerHTML = `<div class="green">Success!</div>`;
     setTimeout(() => statusElement.innerHTML = "", 3000);
   }

A more efficient approach involves defining both states in advance and
toggling their visibility with CSS:

.. code-block:: html
   :caption: popup.html

   <div data-view="none" id="status">
     <div class="red">Something went wrong: <span data-msg="error"></span></div>
     <div class="green">Success!</div>
   </div>

.. code-block:: css
   :caption: popup.css

   #status div.green, #status div.red { display: none; }
   #status[data-view="green"] div.green { display: revert; }
   #status[data-view="red"] div.red { display: revert; }

.. code-block:: javascript
   :caption: popup.js

   const statusElement = document.getElementById("status");
   if (error) {
     statusElement.querySelector('span[data-msg="error"]').textContent = error;
     statusElement.dataset.view = "red";
   } else {
     statusElement.dataset.view = "green";
     setTimeout(() => statusElement.dataset.view = "none", 3000);
   }

This method keeps the DOM stable, avoids expensive reflows, and
separates logic from presentation.

Insert dynamic content using templates
--------------------------------------

Consider the following code:

.. code-block:: javascript
   :caption: popup.js

   if (error) {
     const message = document.createElement('p');
     message.innerHTML = `Missing configuration. <a href="#" onclick="browser.runtime.openOptionsPage(); window.close();">Open settings to update configuration</a>`;
     document.getElementById('configs').appendChild(message);
   }

Instead of dynamically generating HTML, define a ``<template>`` in the
markup and populate it programmatically:

.. code-block:: html
   :caption: popup.html

   <template id="missing-config-template">
     <p>
       Missing configuration.
       <a href="#" data-action="open-settings">Open settings to update configuration</a>
     </p>
   </template>

.. code-block:: javascript
   :caption: popup.js

     const template = document.getElementById('missing-config-template');
     const message = template.content.cloneNode(true);
     const link = message.querySelector('[data-action="open-settings"]');

     link.addEventListener('click', event => {
       event.preventDefault();
       browser.runtime.openOptionsPage();
       window.close();
     });

     document.getElementById('configs').appendChild(message);

This approach avoids both uses of ``innerHTML`` and inline event handlers,
ensures safe text insertion, and cleanly separates structure from behavior.

Inserting and updating content dynamically with ``lighterhtml``
---------------------------------------------------------------

The `lighterhtml <https://github.com/WebReflection/lighterhtml>`__ library (based
on `hyperHTML <https://github.com/WebReflection/hyperHTML>`__) uses ``template literals``
and allows creating DOM trees from strings just like ``innerHTML``, but later
updates to already rendered nodes are done incrementally instead of being fully
torn down and rebuilt from scratch.

Bundle ``lighterhtml`` with the add-on
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Download** the desired ``lighterhtml`` release from a CDN such as jsDelivr or
   cdnjs (for example, version 4.2.0) from a trusted source such as
   https://cdn.jsdelivr.net/npm/lighterhtml@4.2.0/min.min.js

2. **Include** it in the extension under a local folder, for example in
   ``vendor/lighterhtml.min.js``

3. **Document** this dependency in a file named ``VENDOR.md`` in the
   root of the extension. The file should specify the file name and the
   original source URL:

   .. code-block:: markdown
      :caption: VENDOR.md

      lighterhtml.js: https://cdn.jsdelivr.net/npm/lighterhtml@4.2.0/min.min.js

   This allows reviewers to verify that the file is unchanged.

Create DOM nodes from strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load the ``lighterhtml`` library:

.. code-block:: html
   :caption: popup.html

   <html>
      <head>
         <script src="/vendor/lighterhtml.min.js"></script>
         <script defer src="popup.js"></script>
      </head>
      <body>
         ...
      </body>
   </html>

Use ``lighterhtml.html.node`` to create DOM nodes via ``template literals``:

.. code-block:: javascript
   :caption: popup.js

   // Shortcut.
   const lhNode = lighterhtml.html.node;

   const list = ['some', '<b>nasty</b>', 'list'];
   const node = lhNode`
      <p>This is a simple <i>test</i></p>
      <ul>${list.map(text => lhNode`
         <li>${text}</li>
      `)}
      </ul>
   `
   document.body.appendChild(node);


Render and update DOM nodes from strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``lighterhtml.html`` and ``lighterhtml.render`` to create wired content,
which can be updated later:

.. code-block:: javascript
   :caption: popup.js
   
   const names = [
      'Arianna',
      'Luca',
      'Isa'
   ]

   setInterval(greetings, 2000);

   function greetings() {
      names.unshift(names.pop());
      lighterhtml.render(
         document.body, lighterhtml.html`${names.map(
            name => lighterhtml.html`<p>Hello ${name}!</p>`
         )}`
      );
   }

The library supports many more interesting, as automatically converting ``onclick``
attributes into real event listeners.

Safely sanitizing external markup with ``DOMPurify``
----------------------------------------------------

In some cases, an extension may need to display **externally sourced or user-generated
HTML**, for example, when rendering message previews or feed entries. In such
situations, using ``innerHTML`` or any other method to directly insert the raw
HTML is unsafe, because it allows potentially malicious HTML or script content
to be injected into the page.

To handle this scenario safely, the recommended approach is to **sanitize the
markup first using** `DOMPurify <https://github.com/cure53/DOMPurify>`__, and then
insert the sanitized content using ``insertAdjacentHTML()``.

Bundle ``DOMPurify`` with the add-on
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Download** the desired ``DOMPurify`` release from a CDN such as jsDelivr or
   cdnjs (for example, version 3.2.7) from a trusted source such as
   https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.2.7/purify.min.js

2. **Include** it in the extension under a local folder, for example in
   ``vendor/purify.min.js``

3. **Document** this dependency in a file named ``VENDOR.md`` in the
   root of the extension. The file should specify the file name and the
   original source URL:

   .. code-block:: markdown
      :caption: VENDOR.md

      purify.min.js: https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.2.7/purify.min.js

   This allows reviewers to verify that the file is unchanged.

Insert purified markup with ``insertAdjacentHTML()``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load the ``DOMPurify`` library:

.. code-block:: html
   :caption: popup.html

   <html>
      <head>
         <script src="/vendor/purify.min.js"></script>
         <script defer src="popup.js"></script>
      </head>
      <body>
         <div id="preview"></div>
      </body>
   </html>


Sanitize external HTML and add it to the DOM via ``insertAdjacentHTML()``:

.. code-block:: javascript
   :caption: popup.js

   async function renderExternalMarkup(url) {
       const response = await fetch(url);
       const rawHtml = await response.text();

       // Sanitize the received HTML.
       const safeHtml = DOMPurify.sanitize(rawHtml);

       // Insert the sanitized markup.
       const preview = document.getElementById('preview');
       preview.insertAdjacentHTML('beforeend', safeHtml);
   }

   renderExternalMarkup('https://example.com/feed-entry.html');

This combination provides a controlled way to render external HTML safely within
Thunderbird extensions. In the future, ``insertAdjacentHTML()`` will support
built-in sanitization with the
`Sanitizer API <https://developer.mozilla.org/en-US/docs/Web/API/Sanitizer>`__,
but for now, ``DOMPurify`` remains necessary.
