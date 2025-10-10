Avoid using ``innerHTML``
=========================

A common practice is to use ``innerHTML`` to assign a complex DOM
structure to an existing element, which will generate the required DOM
nodes on-the-fly. Usually there are two use cases:

-  updating the content of a UI element (notification, status, …)
-  loading external content (an RSS feed, a message, …)

Using ``innerHTML`` directly is risky because it **injects raw HTML into
the DOM**, which can easily introduce **cross-site scripting (XSS)
vulnerabilities** if any of the content comes from user input or an
external source. It also bypasses the browser's native DOM APIs, which
can lead to **unexpected behavior, broken layouts, or loss of event
listeners**.

Even when the content originates from internal sources, using
``innerHTML`` is generally a poor practice. Replacing an element's
entire HTML structure forces the browser to destroy and rebuild the DOM
nodes, which can lead to **performance issues**, unnecessary layout
recalculations, and the loss of attached event listeners or state. For
these reasons, it is recommended to manipulate the DOM selectively using
element creation, ``textContent``, or data-driven visibility toggles.

More information on this topic is available on
`MDN <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Safely_inserting_external_content_into_a_page>`__.

Update content via span placeholders
------------------------------------

Consider the following code:

.. code:: javascript

   const message = document.getElementById('message');
   message.innerHTML = `The following <b>${counts}</b> items have been found:`;

Here, ``innerHTML`` is used just to insert a formatted value. A better
approach is to include the static part directly in the markup and only
update the dynamic part.

.. code:: html

   <div id="message">
     The following <b><span data-msg="counts"></span></b> items have been found:
   </div>

.. code:: javascript

   document.querySelector('#message span[data-msg="counts"]').textContent = counts;

This avoids HTML parsing entirely and ensures the inserted value is
treated as plain text.

Update content by hiding/showing markup via CSS
-----------------------------------------------

Consider the following markup and code:

.. code:: html

   <div id="status"></div>

.. code:: javascript

   const statusElement = document.getElementById("status");
   if (error) {
     statusElement.innerHTML = `<div class="red">Something went wrong: ${error}</div>`;
   } else {
     statusElement.innerHTML = `<div class="green">Success!</div>`;
     setTimeout(() => statusElement.innerHTML = "", 3000);
   }

A more efficient approach involves defining both states in advance and
toggling their visibility with CSS:

.. code:: html

   <div data-view="none" id="status">
     <div class="red">Something went wrong: <span data-msg="error"></span></div>
     <div class="green">Success!</div>
   </div>

.. code:: css

   #status div.green, #status div.red { display: none; }
   #status[data-view="green"] div.green { display: revert; }
   #status[data-view="red"] div.red { display: revert; }

.. code:: javascript

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

Update content using templates
------------------------------

Consider the following code:

.. code:: javascript

   if (error) {
     const message = document.createElement('p');
     message.innerHTML = `Missing configuration. <a href="#" onclick="browser.runtime.openOptionsPage(); window.close();">Open settings to update configuration</a>`;
     document.getElementById('configs').appendChild(message);
   }

Instead of dynamically generating HTML, define a ``<template>`` in the
markup and populate it programmatically:

.. code:: html

   <template id="missing-config-template">
     <p>
       Missing configuration.
       <a href="#" data-action="open-settings">Open settings to update configuration</a>
     </p>
   </template>

.. code:: javascript

     const template = document.getElementById('missing-config-template');
     const message = template.content.cloneNode(true);
     const link = message.querySelector('[data-action="open-settings"]');

     link.addEventListener('click', event => {
       event.preventDefault();
       browser.runtime.openOptionsPage();
       window.close();
     });

     document.getElementById('configs').appendChild(message);

This approach avoids both ``innerHTML`` and inline event handlers,
ensures safe text insertion, and cleanly separates structure from
behavior.

Safely inserting external markup with DOMPurify
-----------------------------------------------

In some cases, an extension may need to display **externally sourced or
user-generated HTML**, for example, when rendering message previews or
feed entries. In such situations, using ``innerHTML`` directly is
unsafe, because it allows potentially malicious HTML or script content
to be injected into the page.

To handle this scenario safely, the recommended approach is to
**sanitize the markup first using**
`DOMPurify <https://github.com/cure53/DOMPurify>`__, and then insert the
sanitized content using ``insertAdjacentHTML()``.

Including DOMPurify
~~~~~~~~~~~~~~~~~~~

Do not load DOMPurify **directly** from a remote CDN such as jsDelivr or
cdnjs. Instead, you must:

1. | **Download** the desired DOMPurify release (for example, version
     3.2.7) from a trusted source such as
   | [`https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.2.7/purify.min.js](https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.2.7/purify.min.js) <https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.2.7/purify.min.js](https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.2.7/purify.min.js)>`__

2. **Include** it in your extension package under a local folder, for
   example in ``vendors/purify.min.js``

3. **Document** this dependency in a file named ``VENDORS.md`` in the
   root of your extension. The file should specify the file name and the
   original source URL:

::

   purify.min.js: https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.2.7/purify.min.js

This allows reviewers to verify that the file is unchanged.

Insert purified markup with ``insertAdjacentHTML()``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: html

   <script src="vendors/purify.min.js"></script>
   <div id="preview"></div>

.. code:: javascript

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

This combination provides a controlled way to render external HTML
safely within Thunderbird extensions. In the future, browsers will
support built-in sanitization for ``insertAdjacentHTML()`` via the
`Sanitizer API <https://developer.mozilla.org/en-US/docs/Web/API/Sanitizer>`__,
but for now, using ``DOMPurify()`` remains necessary.
