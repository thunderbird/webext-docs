=========================
Changes in Thunderbird 74
=========================

legacy
======

* The legacy API has been removed. This has been covered elsewhere.

accounts/folders
================

* The :ref:`MailFolder <folders.MailFolder>` object gained a subFolders property. From now on the
  :doc:`accounts API functions </accounts>` will return a hierarchy of folders instead of a flat
  list. If you still need a flat list you should traverse the folder hierarchy:

  .. code-block:: javascript

    browser.accounts.list().then(accounts => {
      let arrayOfFolders = [];

      function traverse(folders) {
        if (!folders) {
          return;
        }
        for (let f of folders) {
          arrayOfFolders.push(f);
          traverse(f.subFolders);
        }
      }

      for (let account of accounts) {
        traverse(account.folders);
      }
      return arrayOfFolders;
    });

  This example code works with both the current API in 68 and the new version in 74 (which will be
  backported to 68 after some time in beta).

compose
=======

* The compose API gained two new functions and an event. The
  :ref:`getComposeDetails <compose.getComposeDetails>` and
  :ref:`setComposeDetails <compose.setComposeDetails>` functions let you retrieve or change the
  recipients and subject of a message being composed. More details will be added later. The
  :ref:`onBeforeSend <compose.onBeforeSend>` event is fired when a message is about to be sent. At
  this point your extension can prevent sending or change the same details as in the new functions.

messages
========

* The :ref:`query <messages.query>` function can now query by tags.

* The :ref:`MessageHeader <messages.MessageHeader>` object now has junk properties:
  ``junkScore`` is an integer score from 0 (not spam) to 100 (spam).
  ``junk`` shows whether or not that score is greater than the junk threshold.

---

Bugzilla list of fixed WebExtension API defects in `Thunderbird 74 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=74%20Branch&o2=equals>`__.
