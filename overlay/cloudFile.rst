=============
cloudFile API
=============

The cloudFile (a.k.a. fileLink) API first appeared in Thunderbird 60. It allows to create a provider to store large attachments in the cloud instead of attaching them directly to the message.

From Thunderbird 68.2.1 (Thunderbird 71 beta), an extension can choose to receive data for upload
as a `File <https://developer.mozilla.org/en-US/docs/Web/API/File>`__ object rather than as an `ArrayBuffer <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer>`__. You **should** specify which you want as
the default may change in a future version.

The `DropBox Uploader`__ sample extension uses this API.

__ https://github.com/thunderbird/sample-extensions/tree/master/dropbox
