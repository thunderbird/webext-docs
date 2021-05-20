=============================
Changes in Thunderbird 78.7.0
=============================

accounts
========

* The ``composeHtml`` property has been added to the :ref:`accounts.MailIdentity` type, to indicate, if the identity uses HTML as the default compose format.

* The :ref:`accounts.getDefaultIdentity` function has been added, to get the default identity of a given account. Use :ref:`accounts.getDefault` to get the default account.

compose
=======

* The begin* functions now honor ``body``, ``plainTextBody`` and ``isPlaintext`` as compose format selectors, overriding the default compose format of the used/default identity. The :ref:`accounts_api` API can be used to get the used/default identity and its default compose format.
  
* The :ref:`beginNew <compose.beginNew>` function now has an optional ``messageId`` argument. If
  ``messageId`` is provided, the referenced message is opened to compose as a new message. This
  works for ordinary messages and templates.
  
* Using :ref:`beginForward <compose.beginForward>` function with a ``forwardInline`` type and
  ``details`` argument specified has been fixed.
