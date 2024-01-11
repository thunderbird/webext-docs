Using tabs and windows
======================

To access tabs or windows using the ID values from the built-in APIs, use the ``tabManager`` or
``windowManager`` objects. These are have functions similar to, but not the same as, the APIs:

.. code-block:: javascript

  // Get a real tab from a tab ID:
  let tabObject = context.extension.tabManager.get(tabId);
  let realTab = tabObject.nativeTab;
  let realTabWindow = tabObject.window;

  // Get a tab ID from a real tab:
  context.extension.tabManager.getWrapper(realTab).id;

  // Query tabs: (note this returns a Generator, not an array like the API)
  context.extension.tabManager.query(queryInfo);

"Tabs" are a bit weird. For a tab on the main Thunderbird window, the ``nativeTab`` property is
the ``tabInfo`` object you'd get from that window's ``<tabmail>``. For a tab *not* on the main
window, e.g. a "tab" representing the message composition window, both ``nativeTab`` and ``window``
properties refer to the window itself.

.. code-block:: javascript

  // Get a real window from a window ID:
  let windowObject = context.extension.windowManager.get(windowId);
  let realWindow = windowObject.window;

  // Get a window ID from a real window:
  context.extension.windowManager.getWrapper(realWindow).id;

  // Get all windows: (note this returns a Generator, not an array like the API)
  context.extension.windowManager.getAll();

For more things you could use on ``tabObject`` or ``windowObject`` in the examples above, see
`the Tab, TabMailTab, and Window classes in the source code`__.

__ https://hg.mozilla.org/releases/comm-esr78/file/tip/mail/components/extensions/parent/ext-mail.js#l763
