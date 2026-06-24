Strategies to avoid using ``innerHTML``
=======================================

The use of ``innerHTML`` is a fast and convenient way to create DOM nodes. The
issue is that it encourages a pattern where entire DOM trees are replaced instead
of being updated selectively. Even if it is only used for initial rendering, it
can easily lead to adopting the same pattern for updates later, which may cause
layout flicker, loss of state, and unnecessary re-rendering. Replacing an existing
DOM tree is highly inefficient, it is better to use explicit DOM manipulation
methods or data-driven rendering approaches instead. Some common alternatives to
``innerHTML`` include:

- ``textContent`` to safely replace text
- ``createElement()``, ``append()``, or templating functions to build new structures
- CSS or visibility toggles instead of rebuilding markup
- libraries such as `lighterhtml <https://github.com/WebReflection/lighterhtml>`__,
  which create DOM trees efficiently and update them via diffing instead of replacement

If external or user-provided HTML must be rendered, it has to be sanitized first.
Thunderbird 153 and later provide the built-in
`Sanitizer API <https://developer.mozilla.org/en-US/docs/Web/API/Sanitizer>`__, so
``Element.setHTML()`` can sanitize and insert markup in a single step without a
third-party library. To support older Thunderbird versions, sanitize the markup
with a library such as `DOMPurify <https://github.com/cure53/DOMPurify>`__ and
insert it with ``insertAdjacentHTML()``.

.. note::
 
   Using ``innerHTML`` is accepted for add-ons hosted on ATN when it is not used
   to update existing DOM nodes. However, the alternatives described in this guide
   are generally suggested.

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

Download a ``lighterhtml`` release from a trusted source and place it in a local
folder of the add-on, for example ``vendor/lighterhtml.min.js``, then declare it so
reviewers can verify the bundled file is unchanged. See :doc:`/guides/vendoring` for
the trusted sources and the accepted declaration formats.

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

The library supports many additional features, such as automatically converting
``onclick`` attributes into real event listeners.

Safely sanitizing external markup
----------------------------------------------------

In some cases, an extension may need to display **externally sourced or user-generated
HTML**, for example, when rendering message previews or feed entries. In such
situations, using ``innerHTML`` or any other method to directly insert the raw
HTML is unsafe, because it allows potentially malicious HTML or script content
to be injected into the page.

The markup has to be sanitized before it reaches the DOM.

Sanitize with ``Element.setHTML()``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Thunderbird 153 and later, the built-in
`Sanitizer API <https://developer.mozilla.org/en-US/docs/Web/API/Sanitizer>`__
parses and sanitizes the markup in a single step, with no third-party library to
bundle. Given a ``<div id="preview">`` element in the page, the sanitized content
can be rendered with ``Element.setHTML()``:

.. code-block:: javascript
   :caption: popup.js

   async function renderExternalMarkup(url) {
       const response = await fetch(url);
       const rawHtml = await response.text();

       // Parse and sanitize the received HTML, then render it.
       const preview = document.getElementById('preview');
       preview.setHTML(rawHtml);
   }

   renderExternalMarkup('https://example.com/feed-entry.html');

Sanitize with ``DOMPurify`` on older versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run on Thunderbird versions before 153, sanitize the markup with ``DOMPurify``
and insert the result with ``insertAdjacentHTML()``. First bundle it with the
add-on.

Download a ``DOMPurify`` release from a trusted source and place it in a local
folder of the add-on, for example ``vendor/purify.min.js``, then declare it so
reviewers can verify the bundled file is unchanged. See :doc:`/guides/vendoring` for
the trusted sources and the accepted declaration formats.

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
