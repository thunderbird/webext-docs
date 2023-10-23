==========================
Changes in Thunderbird 115
==========================

WebExtensions usually are not reviewed when submitted but instead are made available instantly. The WebExtension permission system should guard against malicious actors. However, the data available to extensions is very sensitive and if a user granted access to messages and contacts he mostly assumes the data is only used locally. Extensions however, can unknowingly send this data to remote servers. We therefore started to enforce review of all extensions, which request sensitive permissions like ``messagesRead`` or ``addressBooks``. We also introduce an additional ``sensitiveDataUpload`` permission, which allows to by-pass this human review, but prompts the user for the following permission: *Transfer sensitive user data (if access has been granted) to a remote server for further processing.*

If an add-on is not requesting that permission, but a reviewer concludes that it is indeed sending data to a remote server not under the control of the user, the reviewer may request the permission to be added.

browserAction API
=================
* Deprecate the ``default_area`` manifest entry in favour of the recently added ``allowed_spaces`` manifest entry.
* Add support for the ``type`` manifest entry to define a ``menu`` button, whose menu entries can be controlled through the :ref:`menus_api` API and a new ``browser_action_menu`` context.

addressBooks API
================
* The function :ref:`addressBooks.openUI` now returns a Promise for the :ref:`tabs.Tab` of the opened tab.

commands API
============
* Add the :ref:`commands.onChanged` event to be notified when a command shortcut has been changed.

compose API
===========
* Add support for the ``type`` manifest entry to define a ``menu`` button, whose menu entries can be controlled through the :ref:`menus_api` API and a new ``compose_action_menu`` context.

messages API
============
* The ``queryInfo`` parameter for :ref:`messages.query` is now optional.
* Added :ref:`messages.openAttachment` to open message attachments with the registered application. A big thank you to Mark Banner.
* Add support for the ``type`` manifest entry to define a ``menu`` button, whose menu entries can be controlled through the :ref:`menus_api` API and a new ``message_display_action_menu`` context.

messageDisplay API
==================
* Added support for :ref:`messageDisplay.open` to open messages from a DOM File object.

sessions API
============
* Add a first simple version of the :ref:`sessions_api` API to allow extensions to store tab related session data, which is restored on app restart.

spaces API
==========
* Add :ref:`spaces_api` API which supersedes the spacesToolbar API and allows to manage built-in and custom spaces.

spacesToolbar API
=================
* Add :ref:`spacesToolbar.clickButton` to trigger a click on the button of a space in the spaces toolbar. In Manifest v3 the button-centric ``spacesToolbar API`` was removed and replaced by the space-centric ``spaces API``, where the corresponding method is named `spaces.open() <https://webextension-api.thunderbird.net/en/latest-mv3/spaces.html#open-spaceid-windowid>`__.

tabs API
========
* The ``queryInfo`` parameter for :ref:`tabs.query` is now optional.
* Add a ``spaceId`` member to the :ref:`tabs.Tab` type.
* Add a ``cookieStoreId`` member to the :ref:`tabs.Tab` type. A big thank you to Neil Rashbrook.
* Add support for the ``previousTabId`` parameter to the :ref:`tabs.onActivated` event.
* Changed handling of URLs in :ref:`tabs.update`: If the URL points to a content page (a web page, an extension page or a registered WebExtension protocol handler page), the tab will navigate to the requested page. All other URLs will be opened externally without changing the tab. Note: The function will throw an error, if a content page is loaded into a non-content tab (its type must be either :value:`content` or :value:`mail`).


____

Bugzilla list of all fixed WebExtension API bugs in `Thunderbird 114 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=114%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__ and `Thunderbird 115 <https://bugzilla.mozilla.org/buglist.cgi?target_milestone=115%20Branch&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API>`__.
