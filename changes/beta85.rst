=========================
Changes in Thunderbird 85
=========================

addressBooks & contacts
=======================

The :ref:`addressBooks_api` and :ref:`contacts_api` APIs will now return read-only address books. Add-ons that may update contacts and address books should check the ``readOnly`` flag of :ref:`addressBooks.AddressBookNode`.

accounts
========

* The ``composeHtml`` property has been added to the :ref:`identities.MailIdentity` type, to indicate, if the identity uses HTML as the default compose format.

  *This change has been backported to Thunderbird 78.7.0.*

* The :ref:`accounts.getDefaultIdentity` function has been added, to get the default identity of a given account. Use :ref:`accounts.getDefault` to get the default account.

  *This change has been backported to Thunderbird 78.7.0.*

compose
=======

* The begin* functions now honor ``body``, ``plainTextBody`` and ``isPlaintext`` as compose format selectors, overriding the default compose format of the used/default identity. The :ref:`accounts_api` API can be used to get the used/default identity and its default compose format.

  *This change has been backported to Thunderbird 78.7.0.*

messages
========

* :ref:`messages.query` supports queries for messages with a given ``headerMessageId``
