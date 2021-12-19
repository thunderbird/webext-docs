=============================
Changes in Thunderbird 91.4.1
=============================

cloudFile API
=============

* added ``templateInfo`` as a supported return value property of the :ref:`cloudFile.onFileUpload` event, to specify a :ref:`cloudFile.CloudFileTemplateInfo` with additional information for the cloud file entry added to the users message

messages API
============

* added ``attachment`` as a supported property of the :ref:`messages.query` function, to be able to query for messages with or without attachments
