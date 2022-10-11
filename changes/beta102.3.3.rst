==============================
Changes in Thunderbird 102.3.3
==============================

browserAction API
=================
* Added ``default_windows`` manifest key to :ref:`browserAction_api`, allowing to show the action button also in stand-alone message windows.

commands API
============
* Added ``tab`` parameter to the :ref:`commands.onCommand` event, returning the currently active tab. Since the event is a user input event handler, it was not possible to query the active tab (via `browser.tabs.query()`), without loosing this elevated status due to calling an asynchronous function. Solved by returning the tab as a parameter (similar to :ref:`menus.onClicked` and other user input event handlers).

mailTabs API
============
* Added :ref:`mailTabs.setSelectedMessages`.

____

Bugzilla list of fixed WebExtension API defects uplifted from `Thunderbird 106 <https://bugzilla.mozilla.org/buglist.cgi?v3=defect&f2=target_milestone&resolution=FIXED&component=Add-Ons%3A%20Extensions%20API&o3=equals&f1=flagtypes.name&product=Thunderbird&o1=equals&f3=bug_type&query_format=advanced&v2=106%20Branch&o2=equals&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=approval-comm-esr102%2B>`__.
