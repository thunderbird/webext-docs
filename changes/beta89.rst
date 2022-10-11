=========================
Changes in Thunderbird 89
=========================

mailTabs
========

* added :ref:`mailTabs.getCurrent` and :ref:`mailTabs.get` functions


menus
=====

* fixed ``browser_action`` :ref:`menus.ContextType`
* added ``message_display_action`` and ``compose_action`` :ref:`menus.ContextType`
* introducing a ``fieldId`` property to :ref:`menus.onClickData` and :ref:`menus.onShowData` to to support fields part of the Thunderbird UI (currently supported values are ``composeSubject``, ``composeTo``, ``composeCc``, ``composeBcc``, ``composeReplyTo`` and ``composeNewsgroupTo``)

---

Bugzilla list of fixed WebExtension API defects in `Thunderbird 89 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=89%20Branch&o2=equals>`__.
