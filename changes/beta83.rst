=========================
Changes in Thunderbird 83
=========================

compose
=======

* :ref:`ComposeAttachment <compose.ComposeAttachment>` objects now have a ``size`` property with
  the size of the attachment in bytes.
  
  *This change has been backported to Thunderbird 78.5.0.*

menus
=====

* A ``compose_attachment`` context can now be used. This context applies when the user opens a
  context menu on selected attachments in a compose window. The selected attachments can be
  accessed from the ``attachments`` property in the :ref:`onClicked <menus.onClicked>` listener.
  
  *This change has been backported to Thunderbird 78.5.0.*
