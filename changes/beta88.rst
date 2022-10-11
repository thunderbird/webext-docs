=========================
Changes in Thunderbird 88
=========================

compose
=======

* added a ``type`` property to :ref:`compose.ComposeDetails`, to distinguish between ``new``, ``reply``, ``forward`` and ``draft``
* added a ``from`` property to :ref:`compose.ComposeDetails`, to get/set the actual from address (independent of the used identity)

contacts
========

* fixed :ref:`contacts.quickSearch` to not fail on mailing lists

menus
=====

* added a ``tools_menu`` context to :ref:`menus.ContextType`
* added a ``selectedAccount`` property to :ref:`menus.onShowData` and :ref:`menus.onClickData`, if the menu was opened on a root folder in the folder pane
* fixed :ref:`menus.onClicked` to keep the user input status so :ref:`browserAction.openPopup` can be used


messages
========

* added :ref:`messages.listAttachments` and :ref:`messages.getAttachmentFile` methods to work with message attachments
* fixed :ref:`messages.getRaw` to work for nntp/news messages

=======================
Fixes in Thunderbird 88
=======================

* `Bugzilla list of all fixed defects <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&list_id=16239985&component=Add-Ons%3A%20Extensions%20API&component=Add-Ons%3A%20General&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=88%20Branch&o2=equals>`__.
