=========================
Changes in Thunderbird 97
=========================

cloudFile API
=============

* deprecated the ``manifest.service_url`` entry, it is superseded by the optional ``service_url`` property of the :ref:`cloudFile.CloudFileTemplateInfo`
* added new optional properties to :ref:`cloudFile.CloudFileTemplateInfo` : ``download_expiry_date``, ``download_limit`` and ``download_password_protected``

---

Bugzilla list of fixed WebExtension API defects in `Thunderbird 97 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=97%20Branch&o2=equals>`__.
