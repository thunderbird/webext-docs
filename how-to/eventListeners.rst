================================
Working with WebExtension events
================================

WebExtensions can react on events by attaching a listener. Consider the :ref:`menus.onClicked` event of the menus API:

.. code-block:: javascript

  async function menuListener(info, tab) {
    // Do something with the info and tab parameters
    // received from the event.
  }
  
  messenger.menus.onClicked.addListener(menuListener);
  
Alternative implementation using an anonymous arrow function:

.. code-block:: javascript
 
  messenger.menus.onClicked.addListener(async (info, tab) => {
    // Do something with the info and tab parameters
    // received from the event.
  });

Events with additional parameters
=================================

Some events support additional parameters, for example the :ref:`tabs.onUpdated` event.

The additional parameter ``filter`` is the second parameter of the ``addListener``
function, specifying what type of update events should be reported.

.. code-block:: javascript

  async function listener(tabId, changeInfo) {
    // Do something with the tabId and changeInfo parameters
    // received from the event.
  }
  
  messenger.tabs.onUpdated.addListener(listener, {tabId: 5});
