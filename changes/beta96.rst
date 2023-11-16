=========================
Changes in Thunderbird 96
=========================

cloudFile API
=============

* added ``templateInfo`` as a supported return value property of the :ref:`cloudFile.onFileUpload` event, to specify a :ref:`cloudFile.CloudFileTemplateInfo` with additional information for the cloud file entry added to the users message
* added ``error`` as a supported return value property of the :ref:`cloudFile.onFileUpload` event, to show an error message to the user, in case upload failed

* added :ref:`cloudFile.onFileRename` event to properly handle cloud file rename operations (the file on the server should be renamed as well, if the cloud file attachment in the email is renamed by the user)

messages API
============

* added ``attachment`` as a supported property of the :ref:`messages.query` function, to be able to query for messages with or without attachments

____

Bugzilla list of fixed WebExtension API defects in `Thunderbird 96 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=96%20Branch&o2=equals>`__.
