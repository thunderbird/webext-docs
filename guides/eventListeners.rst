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

Some events support additional parameters, for example the :ref:`messages.onNewMailReceived` event.

The additional parameter ``monitorAllFolders`` is the second parameter of the ``addListener``
function, specifying whether to monitor just the standard inbox folders, or all folders.

.. code-block:: javascript

  async function listener(folder, messages) {
    // Do something with the folder and messages parameters
    // received from the event.
  }
  
  messenger.messages.onNewMailReceived.addListener(listener, true);
