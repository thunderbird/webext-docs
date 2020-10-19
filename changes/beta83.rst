=========================
Changes in Thunderbird 83
=========================

compose
=======

* :ref:`ComposeAttachment <compose.ComposeAttachment>` objects now have a ``size`` property with
  the size of the attachment in bytes.

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
