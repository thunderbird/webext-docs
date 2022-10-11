=========================
Changes in Thunderbird 98
=========================

accounts API
============

* added :ref:`accounts.onCreated`, :ref:`accounts.onDeleted` and :ref:`accounts.onUpdated` events

cloudFile API
=============

* added manifest property ``reuse_uploads``, to allow providers to disable automatic link reuse of already known cloud files: If a previously uploaded cloud file attachment is reused at a later time in a different message, Thunderbird may use the already known ``url`` and ``templateInfo`` values without triggering the registered :ref:`cloudFile.onFileUpload` listener again. Setting this option to false will always trigger the registered listener, providing the already known values through the ``relatedFileInfo`` parameter of the :ref:`cloudFile.onFileUpload` event, to let the provider decide how to handle these cases.
* added the ``relatedFileInfo`` parameter of the :ref:`cloudFile.onFileUpload` event: Information about an already uploaded cloud file, which is related to a new upload. For example if the content of a cloud attachment is updated, if a repeatedly used cloud attachment is renamed (and therefore should be re-uploaded to not invalidate existing links) or if the provider has its manifest property ``reuse_uploads`` set to ``false``.

compose API
===========

* deprecated the ``getFile()`` function of the :ref:`compose.ComposeAttachment` (example of a backward-compatible drop-in `wrapper function <https://thunderbird.topicbox.com/groups/addons/T290381ad849307a1-Mda1465bd6388138d5a893ff8/request-to-deprecate-composeattachment-getfile>`__)
* added :ref:`compose.getAttachmentFile` function to get the content of a :ref:`compose.ComposeAttachment` as a DOM ``File`` object
* added support to use a :ref:`compose.ComposeAttachment` as the attachment in :ref:`compose.addAttachment` and in :ref:`compose.ComposeDetails`
* modified the rules for ``body``, ``plainTextBody`` and ``isPlainText`` properties of :ref:`compose.ComposeDetails` in a backward compatible way - specifying both body types no longer causes an exception and it is now even suggested to always specify both and either let the API pick the users default compose mode, or use the ``isPlainText`` property as selector 

---

Bugzilla list of fixed WebExtension API defects in `Thunderbird 98 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=98%20Branch&o2=equals>`__.
