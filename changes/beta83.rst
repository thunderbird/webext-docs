=========================
Changes in Thunderbird 83
=========================

compose
=======

* :ref:`ComposeAttachment <compose.ComposeAttachment>` objects now have a ``size`` property with
  the size of the attachment in bytes.
  
  *This change has been backported to Thunderbird 78.5.0.*

contacts
========

* The :ref:`onUpdated <contacts.onUpdated>` event now calls listeners with a second argument,
  containing details of the changes made. For example:

  .. code-block:: json

    {
      "FirstName": {
        "oldValue": "Daniel",
        "newValue": "Danielle"
      },
      "DisplayName": {
        "oldValue": "Daniel Smith",
        "newValue": "Danielle Smith"
      }
    }

menus
=====

* A ``compose_attachment`` context can now be used. This context applies when the user opens a
  context menu on selected attachments in a compose window. The selected attachments can be
  accessed from the ``attachments`` property in an :ref:`onShown <menus.onShown>` or
  :ref:`onClicked <menus.onClicked>` listener.
  
  *This change has been backported to Thunderbird 78.5.0.*
  
* The standard properties available to :ref:`onShown <menus.onShown>` are now available for
  messages being displayed, if your extension has the ``messagesRead`` permission.

---

Bugzilla list of fixed WebExtension API defects in `Thunderbird 83 <https://bugzilla.mozilla.org/buglist.cgi?query_format=advanced&f2=target_milestone&component=Add-Ons%3A%20Extensions%20API&resolution=FIXED&o1=equals&product=Thunderbird&columnlist=bug_type%2Cshort_desc%2Cproduct%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cchangeddate%2Ctarget_milestone&v1=defect&f1=bug_type&v2=83%20Branch&o2=equals>`__.
