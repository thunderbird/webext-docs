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

