=============================
Changes in Thunderbird 96
=============================

cloudFile API
=============

* added ``templateInfo`` as a supported return value property of the :ref:`cloudFile.onFileUpload` event, to specify a :ref:`cloudFile.CloudFileTemplateInfo` with additional information for the cloud file entry added to the users message
* added ``error`` as a supported return value property of the :ref:`cloudFile.onFileUpload` event, to show an error message to the user, in case upload failed

* added :ref:`cloudFile.onFileRename` event to properly handle cloud file rename operations (the file on the server should be renamed as well, if the cloud file attachment in the email is renamed by the user)

messages API
============

* added ``attachment`` as a supported property of the :ref:`messages.query` function, to be able to query for messages with or without attachments
