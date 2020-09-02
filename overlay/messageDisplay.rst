==============
messageDisplay
==============

The message display API first appeared in Thunderbird 70 and was backported to Thunderbird 68.2.

A message can be displayed in either a 3-pane tab, a tab of its own, or in a window of its own.
All are referenced by ``tabId`` in this API. Display windows are considered to have exactly one
tab, which has limited functionality compared to tabs from the main window.

More functions are planned for this API for adding to the user interface, as well as a message
display action (similar to :doc:`browserAction` and :doc:`composeAction`).
