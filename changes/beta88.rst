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

