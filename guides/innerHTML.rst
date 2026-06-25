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

If external or user-provided HTML must be rendered, it has to be sanitized first.
Thunderbird 148 and later provide the built-in
`Sanitizer API <https://developer.mozilla.org/en-US/docs/Web/API/Sanitizer>`__, so
``Element.setHTML()`` can sanitize and insert markup in a single step without a
third-party library.

.. note::

   Avoid ``innerHTML`` (and ``outerHTML`` / ``srcdoc`` / ``insertAdjacentHTML()``).
   Use the alternatives described in this guide instead, and ``Element.setHTML()``
   for HTML that must be inserted from external or user-provided data.

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

On Thunderbird 148 and later, the built-in
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
