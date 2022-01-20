=========================
Changes in Thunderbird 98
=========================

compose API
===========

* deprecated the ``getFile()`` function of the :ref:`compose.ComposeAttachment` (example of a backward-compatible drop-in `wrapper function <https://thunderbird.topicbox.com/groups/addons/T290381ad849307a1-Mda1465bd6388138d5a893ff8/request-to-deprecate-composeattachment-getfile>`__)
* added :ref:`compose.getAttachmentFile` function to get the content of a :ref:`compose.ComposeAttachment` as a DOM ``File`` object
* added support to use a :ref:`compose.ComposeAttachment` as the attachment in :ref:`compose.addAttachment` and in :ref:`compose.ComposeDetails`
* modified the rules for ``body``, ``plainTextBody`` and ``isPlainText`` properties of :ref:`compose.ComposeDetails` in a backward compatible way - specifying both body types no longer causes an exception and it is now even suggested to always specify both and either let the API pick the users default compose mode, or use the ``isPlainText`` property as selector 
