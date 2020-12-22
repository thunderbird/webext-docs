================================
Working with WebExtension Events
================================

WebExtensions can react on events by attaching a listener. Consider the :ref:`menus.onClicked` event of the menus API:

.. code-block:: javascript

  async function menuListener(info, tab) {
    ...
    // do something with the info and tab parameters received from the event
  }
  
  messenger.menus.onClicked.addListener(menuListener);
  
Using a more modern syntax:

.. code-block:: javascript
 
  messenger.menus.onClicked.addListener(async (info, tab) => {
    // do something with the info and tab parameters received from the event
	...
  });
