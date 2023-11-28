==============
composeScripts
==============

This compose scripts API first appeared in Thunderbird 77. Functionally it is the same as the
`content scripts`__ API except that it works on the document of email messages during composition.
See the MDN documentation for a more in-depth explanation and :ref:`thunderbird_77_0b1` for examples.

See also :ref:`executeScript <tabs.executeScript>`, :ref:`insertCSS <tabs.insertCSS>`,
:ref:`removeCSS <tabs.removeCSS>`, and :doc:`messageDisplayScripts`.

__ https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts

.. note::

  Registering a compose script in the *manifest.json* file is not possible at this point.
