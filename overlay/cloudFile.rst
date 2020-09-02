=========
cloudFile
=========

The cloudFile (a.k.a. fileLink) API first appeared in Thunderbird 64, and was uplifted to
Thunderbird 60.4 ESR.

From Thunderbird 68.2.1 (Thunderbird 71 beta), an extension can choose to receive data for upload
as a ``File`` object rather than as an ``ArrayBuffer``. You **should** specify which you want as
the default may change in a future version.

The `DropBox Uploader`__ sample extension uses this API.

__ https://github.com/thundernest/sample-extensions/tree/master/dropbox
