==========================
Changes in Thunderbird 113
==========================

action APIs
===========
* Removed the user input requirement from :ref:`action.openPopup`, :ref:`composeAction.openPopup` and :ref:`messageDisplayAction.openPopup`. Also added support for the ``windowId`` property, to open the popup of a specific window. Furthermore, ``openPopup()`` now returns a boolean value, indicating whether opening of the popup has failed, because the action button or the entire toolbar has been removed by the user.
* Fixed the annoying issue on MacOS, where the popup was opened empty after the second time it was opened. A big shout out to Arnd Issler for helping to track this down.

compose API
===========
* Fix compose API to no longer clear all (!) headers, if :ref:`compose.setComposeDetails` is used to update the non-standard ``X-`` headers.

protocol_handler API
====================
* Add support for WebExtension defined protocols to be accepted as command line arguments. More details can be found in the `bug <https://bugzilla.mozilla.org/show_bug.cgi?id=1824976#c0>`__.

____

Bugzilla list of all fixed WebExtension API bugs in `Thunderbird 112 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=112%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__ and `Thunderbird 113 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=113%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__.
