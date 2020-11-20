=========================
Changes in Thunderbird 84
=========================

compose
=======

* The :ref:`beginNew <compose.beginNew>` function now has an optional ``messageId`` argument. If
  ``messageId`` is provided, the referenced message is opened to compose as a new message. This
  works for ordinary messages and templates.
* Using :ref:`beginForward <compose.beginForward>` function with a ``forwardInline`` type and
  ``details`` argument specified has been fixed.

menus
=====

* The standard properties available to :ref:`onShown <menus.onShown>` are now available for
  messages being composed, if your extension has the ``compose`` permission.

tabs
====

* At start-up, :ref:`tabs.create <tabs.create>` will now wait for a window to open before
  attempting to open a tab.
