  ≡ Related examples on Github

  * `"Inline Attachment Preview" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v2/messageDisplayScript.pdfPreview>`__
  * `"Notification Banner" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v2/messageDisplayScript.pdfPreview>`__
  
=========================
messageDisplayScripts API
=========================

This message display scripts API is the same as
the `content scripts`__ API except that it works on the document of email messages being displayed.

See also :ref:`executeScript <tabs.executeScript>`, :ref:`insertCSS <tabs.insertCSS>`,
:ref:`removeCSS <tabs.removeCSS>`, and :doc:`composeScripts`.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts

.. note::

  Registering a message display script in the *manifest.json* file is not possible at this point.
