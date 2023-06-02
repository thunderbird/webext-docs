==========================
Changes in Thunderbird 115
==========================

Introduce an additional ``sensitiveDataUpload``permission, which allows to by-pass human review, but prompts the user for the following permission: Transfer sensitive user data (if access has been granted) to a remote server for further processing.
If an add-on is not requesting that permission, but a reviewer concludes that it is indeed sending data to a remote server not under the control of the user, the reviewer may request the permission to be added.

addressBooks API
================
* The function :ref:`addressBooks.openUI` now returns a Promise for the :ref:`tabs.Tab` of the opened tab.

commands API
============
* Add the :ref:`commands.onChanged` event to be notified when a command shortcut has been changed.

messages API
============
* The ``queryInfo`` parameter for :ref:`messages.query` is now optional.
* Added :ref:``messages.openAttachment`` to open message attachments with the registered application. A big thank you to Mark Banner.

messageDisplay API
==================
* Added support for :ref:`messageDisplay.open` to open messages from DOM File object.

spaces API & spacesToolbar API
==============================
* The button-centric spacesToolbar API was removed for Manifest v3 and has been replaced by the spaces-centric spaces API.

tabs API
========
* The ``queryInfo`` parameter for :ref:`tabs.query` is now optional.
* Add a ``spaceId`` member to the :ref:`tabs.Tab` type.
* Add a ``cookieStoreId`` member to the :ref:`tabs.Tab` type. A big thank you to Neil Rashbrook.
* Add support for the ``previousTabId`` parameter to the :ref:`tabs.onActivated` event.
* Changed handling of URLs in :ref:`tabs.update`: If the URL points to a content page (a web page, an extension page or a registered WebExtension protocol handler page), the tab will navigate to the requested page. All other URLs will be opened externally without changing the tab. Note: The function will throw an error, if a content page is loaded into a non-content tab (its type must be either :value:`content` or :value:`mail`).


____

Bugzilla list of all fixed WebExtension API bugs in `Thunderbird 114 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=114%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__ and `Thunderbird 115 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=115%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__.
