=========================
Changes in Thunderbird 97
=========================

cloudFile API
=============

* deprecated the ``manifest.service_url`` entry, it is superseded by the optional ``service_url`` property of the :ref:`cloudFile.CloudFileTemplateInfo`
* added new optional properties to :ref:`cloudFile.CloudFileTemplateInfo` : ``download_expiry_date``, ``download_limit`` and ``download_password_protected``
