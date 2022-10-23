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

* The `browser.identity <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/identity>`__
  namespace for OAuth handling was enabled.

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 78 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=Thunderbird%2078.0&o2=equals>`__.
