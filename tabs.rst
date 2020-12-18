====
tabs
====

Use the ``browser.tabs`` API to interact with the browser's tab system. You can use this API to create, modify, and rearrange tabs in the browser.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: ``activeTab``
.. api-member::
   :name: ``tabs``

   Access browser tabs
.. api-member::
   :name: ``tabHide``

   Hide and show browser tabs

.. rst-class:: api-main-section

Functions
=========

.. _tabs.get:

get(tabId)
----------

.. api-section-annotation-hack:: 

Retrieves details about the specified tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      :annotation: 
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`tabs.Tab`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.getCurrent:

getCurrent()
------------

.. api-section-annotation-hack:: 

Gets the tab that this script call is being made from. May be undefined if called from a non-tab context (for example: a background page or popup view).

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`tabs.Tab`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.connect:

connect(tabId, [connectInfo])
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 82, backported to TB 78.4]

Connects to the content script(s) in the specified tab. The `runtime.onConnect <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect>`_ event is fired in each content script running in the specified tab for the current extension. For more details, see `Content Script Messaging <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`_.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      :annotation: 
   
   
   .. api-member::
      :name: [``connectInfo``]
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``frameId``]
         :type: (integer)
         :annotation: 
         
         Open a port to a specific frame identified by ``frameId`` instead of all frames in the tab.
      
      
      .. api-member::
         :name: [``name``]
         :type: (string)
         :annotation: 
         
         Will be passed into onConnect for content scripts that are listening for the connection event.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: `Port <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port>`_
      :annotation: 
      
      A port that can be used to communicate with the content scripts running in the specified tab.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.sendMessage:

sendMessage(tabId, message, [options])
--------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 82, backported to TB 78.4]

Sends a single message to the content script(s) in the specified tab, with an optional callback to run when a response is sent back.  The `runtime.onMessage <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage>`_ event is fired in each content script running in the specified tab for the current extension.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      :annotation: 
   
   
   .. api-member::
      :name: ``message``
      :type: (any)
      :annotation: 
   
   
   .. api-member::
      :name: [``options``]
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``frameId``]
         :type: (integer)
         :annotation: 
         
         Send a message to a specific frame identified by ``frameId`` instead of all frames in the tab.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: any
      :annotation: 
      
      The JSON response object sent by the handler of the message. If an error occurs while connecting to the specified tab, the callback will be called with no arguments and `runtime.lastError <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError>`_ will be set to the error message.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.create:

create(createProperties)
------------------------

.. api-section-annotation-hack:: 

Creates a new tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``createProperties``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``active``]
         :type: (boolean)
         :annotation: 
         
         Whether the tab should become the active tab in the window. Does not affect whether the window is focused (see :ref:`windows.update`). Defaults to ``true``.
      
      
      .. api-member::
         :name: [``index``]
         :type: (integer)
         :annotation: 
         
         The position the tab should take in the window. The provided value will be clamped to between zero and the number of tabs in the window.
      
      
      .. api-member::
         :name: [``selected``]
         :type: (boolean) **Unsupported.**
         :annotation: 
         
         Whether the tab should become the selected tab in the window. Defaults to ``true``
      
      
      .. api-member::
         :name: [``url``]
         :type: (string)
         :annotation: 
         
         The URL to navigate the tab to initially. Fully-qualified URLs must include a scheme (i.e. 'http://www.google.com', not 'www.google.com'). Relative URLs will be relative to the current page within the extension. Defaults to the New Tab Page.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer)
         :annotation: 
         
         The window to create the new tab in. Defaults to the current window.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`tabs.Tab`
      :annotation: 
      
      Details about the created tab. Will contain the ID of the new tab.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.duplicate:

duplicate(tabId)
----------------

.. api-section-annotation-hack:: 

Duplicates a tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      :annotation: 
      
      The ID of the tab which is to be duplicated.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`tabs.Tab`
      :annotation: 
      
      Details about the duplicated tab. The :ref:`tabs.Tab` object doesn't contain ``url``, ``title`` and ``favIconUrl`` if the ``tabs`` permission has not been requested.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.query:

query(queryInfo)
----------------

.. api-section-annotation-hack:: 

Gets all tabs that have the specified properties, or all tabs if no properties are specified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``queryInfo``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``active``]
         :type: (boolean)
         :annotation: 
         
         Whether the tabs are active in their windows.
      
      
      .. api-member::
         :name: [``currentWindow``]
         :type: (boolean)
         :annotation: 
         
         Whether the tabs are in the current window.
      
      
      .. api-member::
         :name: [``highlighted``]
         :type: (boolean)
         :annotation: 
         
         Whether the tabs are highlighted.  Works as an alias of active.
      
      
      .. api-member::
         :name: [``index``]
         :type: (integer)
         :annotation: 
         
         The position of the tabs within their windows.
      
      
      .. api-member::
         :name: [``lastFocusedWindow``]
         :type: (boolean)
         :annotation: 
         
         Whether the tabs are in the last focused window.
      
      
      .. api-member::
         :name: [``mailTab``]
         :type: (boolean)
         :annotation: 
         
         Whether the tab is a Thunderbird 3-pane tab.
      
      
      .. api-member::
         :name: [``status``]
         :type: (:ref:`tabs.TabStatus`)
         :annotation: 
         
         Whether the tabs have completed loading.
      
      
      .. api-member::
         :name: [``title``]
         :type: (string)
         :annotation: 
         
         Match page titles against a pattern.
      
      
      .. api-member::
         :name: [``url``]
         :type: (string or array of string)
         :annotation: 
         
         Match tabs against one or more `URL Patterns <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns>`_. Note that fragment identifiers are not matched.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer)
         :annotation: 
         
         The ID of the parent window, or :ref:`windows.WINDOW_ID_CURRENT` for the current window.
      
      
      .. api-member::
         :name: [``windowType``]
         :type: (:ref:`tabs.WindowType`)
         :annotation: 
         
         The type of window the tabs are in.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: array of :ref:`tabs.Tab`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.update:

update([tabId], updateProperties)
---------------------------------

.. api-section-annotation-hack:: 

Modifies the properties of a tab. Properties that are not specified in ``updateProperties`` are not modified.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      :annotation: 
      
      Defaults to the selected tab of the current window.
   
   
   .. api-member::
      :name: ``updateProperties``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``active``]
         :type: (boolean)
         :annotation: 
         
         Whether the tab should be active. Does not affect whether the window is focused (see :ref:`windows.update`).
      
      
      .. api-member::
         :name: [``url``]
         :type: (string)
         :annotation: 
         
         A URL to navigate the tab to.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`tabs.Tab`
      :annotation: 
      
      Details about the updated tab. The :ref:`tabs.Tab` object doesn't contain ``url``, ``title`` and ``favIconUrl`` if the ``tabs`` permission has not been requested.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.move:

move(tabIds, moveProperties)
----------------------------

.. api-section-annotation-hack:: 

Moves one or more tabs to a new position within its window, or to a new window. Note that tabs can only be moved to and from normal windows (``window.type === "normal"``).

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabIds``
      :type: (integer or array of integer)
      :annotation: 
      
      The tab or list of tabs to move.
   
   
   .. api-member::
      :name: ``moveProperties``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: ``index``
         :type: (integer)
         :annotation: 
         
         The position to move the window to. -1 will place the tab at the end of the window.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer)
         :annotation: 
         
         Defaults to the window the tab is currently in.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`tabs.Tab` or array of :ref:`tabs.Tab`
      :annotation: 
      
      Details about the moved tabs.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.reload:

reload([tabId], [reloadProperties])
-----------------------------------

.. api-section-annotation-hack:: 

Reload a tab.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      :annotation: 
      
      The ID of the tab to reload; defaults to the selected tab of the current window.
   
   
   .. api-member::
      :name: [``reloadProperties``]
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``bypassCache``]
         :type: (boolean)
         :annotation: 
         
         Whether using any local cache. Default is false.
      
   

.. _tabs.remove:

remove(tabIds)
--------------

.. api-section-annotation-hack:: 

Closes one or more tabs.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabIds``
      :type: (integer or array of integer)
      :annotation: 
      
      The tab or list of tabs to close.
   

.. _tabs.executeScript:

executeScript([tabId], details)
-------------------------------

.. api-section-annotation-hack:: 

Injects JavaScript code into a page. For details, see the `programmatic injection <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`_ section of the content scripts doc.

.. api-header::
   :label: API changes

   
   .. api-member::
      :name: Thunderbird 77
   
      With the "compose" permission, this now works in the document of email messages during composition.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      :annotation: 
      
      The ID of the tab in which to run the script; defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``details``
      :type: (`InjectDetails <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/InjectDetails>`_)
      :annotation: 
      
      Details of the script to run.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: array of any
      :annotation: 
      
      The result of the script in every injected frame.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.insertCSS:

insertCSS([tabId], details)
---------------------------

.. api-section-annotation-hack:: 

Injects CSS into a page. For details, see the `programmatic injection <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`_ section of the content scripts doc.

.. api-header::
   :label: API changes

   
   .. api-member::
      :name: Thunderbird 77
   
      With the "compose" permission, this now works in the document of email messages during composition.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      :annotation: 
      
      The ID of the tab in which to insert the CSS; defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``details``
      :type: (`InjectDetails <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/InjectDetails>`_)
      :annotation: 
      
      Details of the CSS text to insert.
   

.. _tabs.removeCSS:

removeCSS([tabId], details)
---------------------------

.. api-section-annotation-hack:: 

Removes injected CSS from a page. For details, see the `programmatic injection <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`_ section of the content scripts doc.

.. api-header::
   :label: API changes

   
   .. api-member::
      :name: Thunderbird 77
   
      With the "compose" permission, this now works in the document of email messages during composition.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      :annotation: 
      
      The ID of the tab from which to remove the injected CSS; defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``details``
      :type: (`InjectDetails <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/InjectDetails>`_)
      :annotation: 
      
      Details of the CSS text to remove.
   

.. rst-class:: api-main-section

Events
======

.. _tabs.onCreated:

onCreated(tab)
--------------

.. api-section-annotation-hack:: 

Fired when a tab is created. Note that the tab's URL may not be set at the time this event fired, but you can listen to onUpdated events to be notified when a URL is set.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: 
      
      Details of the tab that was created.
   

.. _tabs.onUpdated:

onUpdated(tabId, changeInfo, tab)
---------------------------------

.. api-section-annotation-hack:: 

Fired when a tab is updated.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      :annotation: 
   
   
   .. api-member::
      :name: ``changeInfo``
      :type: (object)
      :annotation: 
      
      Lists the changes to the state of the tab that was updated.
      
      .. api-member::
         :name: [``favIconUrl``]
         :type: (string)
         :annotation: 
         
         The tab's new favicon URL.
      
      
      .. api-member::
         :name: [``status``]
         :type: (string)
         :annotation: 
         
         The status of the tab. Can be either *loading* or *complete*.
      
      
      .. api-member::
         :name: [``url``]
         :type: (string)
         :annotation: 
         
         The tab's URL if it has changed.
      
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      :annotation: 
      
      Gives the state of the tab that was updated.
   

.. _tabs.onMoved:

onMoved(tabId, moveInfo)
------------------------

.. api-section-annotation-hack:: 

Fired when a tab is moved within a window. Only one move event is fired, representing the tab the user directly moved. Move events are not fired for the other tabs that must move in response. This event is not fired when a tab is moved between windows. For that, see :ref:`tabs.onDetached`.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      :annotation: 
   
   
   .. api-member::
      :name: ``moveInfo``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: ``fromIndex``
         :type: (integer)
         :annotation: 
      
      
      .. api-member::
         :name: ``toIndex``
         :type: (integer)
         :annotation: 
      
      
      .. api-member::
         :name: ``windowId``
         :type: (integer)
         :annotation: 
      
   

.. _tabs.onActivated:

onActivated(activeInfo)
-----------------------

.. api-section-annotation-hack:: 

Fires when the active tab in a window changes. Note that the tab's URL may not be set at the time this event fired, but you can listen to onUpdated events to be notified when a URL is set.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``activeInfo``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: ``tabId``
         :type: (integer)
         :annotation: 
         
         The ID of the tab that has become active.
      
      
      .. api-member::
         :name: ``windowId``
         :type: (integer)
         :annotation: 
         
         The ID of the window the active tab changed inside of.
      
   

.. _tabs.onDetached:

onDetached(tabId, detachInfo)
-----------------------------

.. api-section-annotation-hack:: 

Fired when a tab is detached from a window, for example because it is being moved between windows.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      :annotation: 
   
   
   .. api-member::
      :name: ``detachInfo``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: ``oldPosition``
         :type: (integer)
         :annotation: 
      
      
      .. api-member::
         :name: ``oldWindowId``
         :type: (integer)
         :annotation: 
      
   

.. _tabs.onAttached:

onAttached(tabId, attachInfo)
-----------------------------

.. api-section-annotation-hack:: 

Fired when a tab is attached to a window, for example because it was moved between windows.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      :annotation: 
   
   
   .. api-member::
      :name: ``attachInfo``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: ``newPosition``
         :type: (integer)
         :annotation: 
      
      
      .. api-member::
         :name: ``newWindowId``
         :type: (integer)
         :annotation: 
      
   

.. _tabs.onRemoved:

onRemoved(tabId, removeInfo)
----------------------------

.. api-section-annotation-hack:: 

Fired when a tab is closed.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
      :annotation: 
   
   
   .. api-member::
      :name: ``removeInfo``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: ``isWindowClosing``
         :type: (boolean)
         :annotation: 
         
         True when the tab is being closed because its window is being closed.
      
      
      .. api-member::
         :name: ``windowId``
         :type: (integer)
         :annotation: 
         
         The window whose tab is closed.
      
   

.. rst-class:: api-main-section

Types
=====

.. _tabs.Tab:

Tab
---

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``active``
      :type: (boolean)
      :annotation: 
      
      Whether the tab is active in its window. (Does not necessarily mean the window is focused.)
   
   
   .. api-member::
      :name: ``highlighted``
      :type: (boolean)
      :annotation: 
      
      Whether the tab is highlighted. Works as an alias of active
   
   
   .. api-member::
      :name: ``index``
      :type: (integer)
      :annotation: 
      
      The zero-based index of the tab within its window.
   
   
   .. api-member::
      :name: ``selected``
      :type: (boolean) **Unsupported.**
      :annotation: 
      
      Whether the tab is selected.
   
   
   .. api-member::
      :name: [``favIconUrl``]
      :type: (string)
      :annotation: 
      
      The URL of the tab's favicon. This property is only present if the extension's manifest includes the ``tabs`` permission. It may also be an empty string if the tab is loading.
   
   
   .. api-member::
      :name: [``height``]
      :type: (integer)
      :annotation: 
      
      The height of the tab in pixels.
   
   
   .. api-member::
      :name: [``id``]
      :type: (integer)
      :annotation: 
      
      The ID of the tab. Tab IDs are unique within a browser session. Under some circumstances a Tab may not be assigned an ID. Tab ID can also be set to :ref:`tabs.TAB_ID_NONE` for apps and devtools windows.
   
   
   .. api-member::
      :name: [``mailTab``]
      :type: (boolean)
      :annotation: 
      
      Whether the tab is a 3-pane tab.
   
   
   .. api-member::
      :name: [``status``]
      :type: (string)
      :annotation: 
      
      Either *loading* or *complete*.
   
   
   .. api-member::
      :name: [``title``]
      :type: (string)
      :annotation: 
      
      The title of the tab. This property is only present if the extension's manifest includes the ``tabs`` permission.
   
   
   .. api-member::
      :name: [``url``]
      :type: (string)
      :annotation: 
      
      The URL the tab is displaying. This property is only present if the extension's manifest includes the ``tabs`` permission.
   
   
   .. api-member::
      :name: [``width``]
      :type: (integer)
      :annotation: 
      
      The width of the tab in pixels.
   
   
   .. api-member::
      :name: [``windowId``]
      :type: (integer)
      :annotation: 
      
      The ID of the window the tab is contained within.
   

.. _tabs.TabStatus:

TabStatus
---------

.. api-section-annotation-hack:: 

Whether the tabs have completed loading.

.. api-header::
   :label: `string`

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         Supported values:
         
         .. api-member::
            :name: ``loading``
         
         .. api-member::
            :name: ``complete``
         
   

.. _tabs.UpdateFilter:

UpdateFilter
------------

.. api-section-annotation-hack:: 

An object describing filters to apply to tabs.onUpdated events.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``properties``]
      :type: (array of :ref:`tabs.UpdatePropertyName`)
      :annotation: 
      
      A list of property names. Events that do not match any of the names will be filtered out.
   
   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      :annotation: 
   
   
   .. api-member::
      :name: [``urls``]
      :type: (array of string)
      :annotation: 
      
      A list of URLs or URL patterns. Events that cannot match any of the URLs will be filtered out.  Filtering with urls requires the ``tabs`` or  ``"activeTab"`` permission.
   
   
   .. api-member::
      :name: [``windowId``]
      :type: (integer)
      :annotation: 
   

.. _tabs.UpdatePropertyName:

UpdatePropertyName
------------------

.. api-section-annotation-hack:: 

Event names supported in onUpdated.

.. api-header::
   :label: `string`

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         Supported values:
         
         .. api-member::
            :name: ``favIconUrl``
         
         .. api-member::
            :name: ``status``
         
         .. api-member::
            :name: ``title``
         
   

.. _tabs.WindowType:

WindowType
----------

.. api-section-annotation-hack:: 

The type of window.

.. api-header::
   :label: `string`

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         Supported values:
         
         .. api-member::
            :name: ``normal``
         
         .. api-member::
            :name: ``popup``
         
         .. api-member::
            :name: ``panel``
         
         .. api-member::
            :name: ``app``
         
         .. api-member::
            :name: ``devtools``
         
   

.. rst-class:: api-main-section

Properties
==========

.. _tabs.TAB_ID_NONE:

TAB_ID_NONE
-----------

.. api-section-annotation-hack:: 

An ID which represents the absence of a browser tab.
