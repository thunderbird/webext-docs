==========================
Changes in Thunderbird 111
==========================

messageDisplay API
==================
* Improved :ref:`messageDisplay.open` to honour the ``location`` property also for external messages. They can now also be opened in tabs.

protocol_handler API
====================
* Fix Thunderbird to properly support the `protocol_handlers API <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/protocol_handlers>`__.

windows API
===========
* Fix :ref:`windows.create` to properly support ``top`` and ``left`` properties.
* Fix ``beforeunload`` event not fired in popup windows. Note: There must have been some sort of interaction with the window (for example a mouse click into the window), for this event to be fired when the window is closed.

____

Bugzilla list of all fixed WebExtension API bugs in `Thunderbird 108 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=108%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__, `Thunderbird 109 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=109%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__, `Thunderbird 110 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=110%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__ and `Thunderbird 111 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=111%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__.
