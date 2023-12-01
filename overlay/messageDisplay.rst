  ≡ Other relevant information

  * `"Message Display" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v3/messageDisplay>`__
  
==================
messageDisplay API
==================

The message display API first appeared in Thunderbird 68.

A message can be displayed in either a 3-pane tab, a tab of its own, or in a window of its own.
All are referenced by ``tabId`` in this API. Display windows are considered to have exactly one
tab, which has limited functionality compared to tabs from the main window.
