=====================
messageDisplayScripts
=====================

This message display scripts API first appeared in Thunderbird 78. Functionally it is the same as
the `content scripts`__ API except that it works on the document of email messages being displayed.
See the MDN documentation for a more in-depth explanation and :doc:`/changes/beta82` for examples.

See also :ref:`executeScript <tabs.executeScript>`, :ref:`insertCSS <tabs.insertCSS>`,
:ref:`removeCSS <tabs.removeCSS>`, and :doc:`composeScripts`.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts

.. note::

  Registering a message display script in the *manifest.json* file is not possible at this point.
