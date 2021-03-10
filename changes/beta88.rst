=========================
Changes in Thunderbird 88
=========================

compose
=======

* :ref:`compose.ComposeDetails` of the :ref:`compose_api` API now supports a ``type`` property, to distinguish between ``new``, ``reply``, ``forward`` and ``draft``.


menus
=====

* The :ref:`menus_api` API now supports the ``tools_menu`` :ref:`menus.ContextType`.
* The :ref:`menus.onShowData` and :ref:`menus.onClickData` now include a ``selectedAccount`` property, if the menu was opened on a root folder in the folder pane, representing an account.


messages
========

* The :ref:`messages_api` API now supports :ref:`messages.listAttachments` and :ref:`messages.getAttachmentFile` methods to work with message attachments.

