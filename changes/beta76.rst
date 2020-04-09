=========================
Changes in Thunderbird 76
=========================

accounts
========

* Thunderbird 76 introduces the :ref:`accounts.MailIdentity` type for interacting with mail
  identities. Like the rest of the accounts API, it is mostly read-only as we believe that
  configuration of identities should only happen using the built-in UI.

* The :ref:`accounts.MailAccount` type now contains a list of identities associated with that
  account. The default identity is listed first and other identities are in no particular order.

* The accounts API now has a :ref:`accounts.setDefaultIdentity` function.

compose
=======

* The :ref:`compose.ComposeDetails` type now has an ``identity`` field for getting or setting the
  identity associated with a message being composed.

mailTabs/messageDisplay
=======================

* For consistency with other APIs and with browser WebExtensions (ie. those used in Firefox, etc.),
  some events that passed a numeric tab ID to listeners now pass an object representing the tab
  instead. *This change is not backwards-compatible.*

  The affected events are:

  * :ref:`mailTabs.onDisplayedFolderChanged`
  * :ref:`mailTabs.onSelectedMessagesChanged`
  * :ref:`messageDisplay.onMessageDisplayed`

messages
========

* The ``accountsRead`` permission is now required for all functions that accept a
  :ref:`folders.MailFolder` argument. The permission was already required to obtain a ``MailFolder``
  anyway, so this change should not break extensions.

experiments
===========

* For extensions with the ``addressBooks`` permission, a new ``addressBookManager`` object is
  available to WebExtensions experiment implementations. The ``addressBookManager`` provides the
  following functions to help you interact with the :doc:`/addressBooks`, :doc:`/contacts` and
  :doc:`/mailingLists` APIs:

  * ``findAddressBookById``, ``findContactById``, ``findMailingListById`` to help you find "real"
    address book objects (``nsIAbCard``, ``nsIAbDirectory``) for the IDs provided by the
    addressBooks API. Note that there is active development in the address book and these interfaces
    will be changing in the near term without public announcement.
  * ``convert`` to turn "real" objects back into API-friendly objects.

  For more information on these functions see the `source code of the addressBooks APIs`__.

__ https://hg.mozilla.org/comm-central/file/tip/mail/components/extensions/parent/ext-addressBook.js
