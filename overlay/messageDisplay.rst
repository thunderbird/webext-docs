  ≡ Related examples on Github

  * `"Message Display" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v2/messageDisplay>`__
  
.. _messageDisplay_api:

==================
messageDisplay API
==================

A message can be displayed in either a 3-pane tab, a tab of its own, or in a window of its own.
All are referenced by ``tabId`` in this API. Display windows are considered to have exactly one
tab, which has limited functionality compared to tabs from the main window.
