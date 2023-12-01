  ≡ Related information

  * `"Inline Attachment Preview" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v3/messageDisplayScript.pdfPreview>`__
  * `"Notification Banner" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v3/messageDisplayScript.pdfPreview>`__
  
=========================
messageDisplayScripts API
=========================

This message display scripts API first appeared in Thunderbird 78. Functionally it is the same as
the `content scripts`__ API except that it works on the document of email messages being displayed.
See the MDN documentation for a more in-depth explanation and :ref:`thunderbird_82_0b1` for examples.

See also :ref:`executeScript <tabs.executeScript>`, :ref:`insertCSS <tabs.insertCSS>`,
:ref:`removeCSS <tabs.removeCSS>`, and :doc:`composeScripts`.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts

.. note::

  Registering a message display script in the *manifest.json* file is not possible at this point.
