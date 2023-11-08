=========================
Changes in Thunderbird 75
=========================

browserAction/composeAction/messageDisplayAction
================================================

* The onClick event of the action APIs now has information about the active tab and the click event.

  This brings the events into line with browser WebExtensions. For messageDisplayAction, this is a
  change of behaviour – previously the ID of the active tab was passed as the first argument.

  *This change was uplifted to 74 beta 2.*

compose
=======

* The :ref:`onBeforeSend <compose.onBeforeSend>` event now has information about the active tab.

  *This change was uplifted to 74 beta 2.*

* The compose API functions can now handle the message body.

  All responses from :ref:`getComposeDetails <compose.getComposeDetails>` calls and
  :ref:`onBeforeSend <compose.onBeforeSend>` events now return the message body. How you handle this
  depends on the composition mode (plain text or HTML). For plain text composition mode, the
  ``isPlainText`` field is set to ``true`` and ``plainTextBody`` should be used. For HTML
  composition, ``isPlainText`` is set to ``false`` and ``body`` should be used.

  The ``body`` field is a string. You should parse this to an HTML document before modifying it, and
  serialise the document back to a string before calling setComposeDetails. `Here's a sample
  extension.`__

  __ https://github.com/thunderbird/sample-extensions/tree/master/composeBody

messages
========

* A new event was added: :ref:`onNewMailReceived <messages.onNewMailReceived>`.

  Your extension can now be notified of incoming mail. This is based on the
  ``MailServices.mfn.msgsClassified`` notification.
