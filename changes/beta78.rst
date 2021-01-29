=========================
Changes in Thunderbird 78
=========================

accounts
========

* These functions have been added:

  * :ref:`accounts.getDefault`
  * :ref:`accounts.getDefaultIdentity`
  
  *This change was made in Thunderbird 78.7.*  
  
browserAction, composeAction, messageDisplayAction
==================================================

* Labels of action buttons can now be set independently from the title/tooltip. Empty strings are
  supported as well and enforce an icon-only mode (which is the only mode supported by Firefox).
  The label can be set via the new manifest key ''default_label''. Additionally, the following
  functions have been added:
  
  * :ref:`browserAction.getLabel`, :ref:`composeAction.getLabel`, :ref:`messageDisplayAction.getLabel`,
  * :ref:`browserAction.setLabel`, :ref:`composeAction.setLabel`, :ref:`messageDisplayAction.setLabel`,
  
  *This change was made in Thunderbird 78.6.1.*

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

  *This change was made in Thunderbird 78 beta 2.*
  
* The :ref:`compose.beginNew` function accepts a messageId to use the given message as a template.

  *This change was made in Thunderbird 78.7.*

identity
========

* The `browser.identity <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/identity>`_
  namespace for OAuth handling was enabled.

  *This change was made in Thunderbird 78 beta 2.*
