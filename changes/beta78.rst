=========================
Changes in Thunderbird 78
=========================

compose
=======

* Attachments in the compose window can now be accessed with the compose API. These functions have
  been added:

  * :ref:`compose.listAttachments`
  * :ref:`compose.addAttachment`
  * :ref:`compose.updateAttachment`
  * :ref:`compose.removeAttachment`

  These events have been added:

  * :ref:`compose.onAttachmentAdded`
  * :ref:`compose.onAttachmentRemoved`

  See the documentation on those functions and events for more information.

* A new event, :ref:`compose.onIdentityChanged` was added.


identity
========

* The `browser.identity <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/identity>`_
  namespace for OAuth handling was enabled.
