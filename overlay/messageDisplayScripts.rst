=====================
messageDisplayScripts
=====================

This message display scripts API first appeared in Thunderbird 82 and was backported to Thunderbird
78.4. Functionally it is the same as the `content scripts`__ API except that it works on the
document of email messages being displayed. See the MDN documentation for a more in-depth
explanation and :doc:`/changes/78.04.0` for examples.

See also :ref:`executeScript <tabs.executeScript>`, :ref:`insertCSS <tabs.insertCSS>`,
:ref:`removeCSS <tabs.removeCSS>`, and :doc:`composeScripts`.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/contentScripts

.. note::

  Registering a message display script through ``manifest.json`` is not possible at this point.
