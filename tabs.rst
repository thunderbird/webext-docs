.. _tabs_api:

====
tabs
====

.. role:: permission

.. role:: value

The tabs API supports creating, modifying and interacting with tabs in Thunderbird windows.

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`activeTab`

.. api-member::
   :name: :permission:`tabs`

   Access browser tabs

.. api-member::
   :name: :permission:`tabHide`

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
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`tabs.Tab`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.getCurrent:

getCurrent()
------------

.. api-section-annotation-hack:: 

Gets the tab that this script call is being made from. May be undefined if called from a non-tab context (for example: a background page or popup view).

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`tabs.Tab`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.connect:

connect(tabId, [connectInfo])
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 82, backported to TB 78.4.0]

Connects to the content script(s) in the specified tab. The `runtime.onConnect <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onConnect>`_ event is fired in each content script running in the specified tab for the current extension. For more details, see `Content Script Messaging <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`_.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: [``connectInfo``]
      :type: (object)
      
      .. api-member::
         :name: [``frameId``]
         :type: (integer)
         
         Open a port to a specific frame identified by ``frameId`` instead of all frames in the tab.
      
      
      .. api-member::
         :name: [``name``]
         :type: (string)
         
         Will be passed into onConnect for content scripts that are listening for the connection event.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: `Port <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/Port>`_
      
      A port that can be used to communicate with the content scripts running in the specified tab.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.sendMessage:

sendMessage(tabId, message, [options])
--------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 82, backported to TB 78.4.0]

Sends a single message to the content script(s) in the specified tab, with an optional callback to run when a response is sent back. The `runtime.onMessage <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/onMessage>`_ event is fired in each content script running in the specified tab for the current extension.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``message``
      :type: (any)
   
   
   .. api-member::
      :name: [``options``]
      :type: (object)
      
      .. api-member::
         :name: [``frameId``]
         :type: (integer)
         
         Send a message to a specific frame identified by ``frameId`` instead of all frames in the tab.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: any
      
      The JSON response object sent by the handler of the message. If an error occurs while connecting to the specified tab, the callback will be called with no arguments and `runtime.lastError <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/runtime/lastError>`_ will be set to the error message.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.create:

create(createProperties)
------------------------

.. api-section-annotation-hack:: 

Creates a new content tab. Use the :ref:`messageDisplay_api` to open messages. Only supported in :value:`normal` windows.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``createProperties``
      :type: (object)
      
      Properties for the new tab. Defaults to an empty tab, if no ``url`` is provided.
      
      .. api-member::
         :name: [``active``]
         :type: (boolean)
         
         Whether the tab should become the active tab in the window. Does not affect whether the window is focused (see :ref:`windows.update`). Defaults to :value:`true`.
      
      
      .. api-member::
         :name: [``index``]
         :type: (integer)
         
         The position the tab should take in the window. The provided value will be clamped to between zero and the number of tabs in the window.
      
      
      .. api-member::
         :name: [``selected``]
         :type: (boolean) **Unsupported.**
         
         Whether the tab should become the selected tab in the window. Defaults to :value:`true`
      
      
      .. api-member::
         :name: [``url``]
         :type: (string)
         
         The URL to navigate the tab to initially. Fully-qualified URLs must include a scheme (i.e. :value:`http://www.google.com`, not :value:`www.google.com`). Relative URLs will be relative to the current page within the extension.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer)
         
         The window to create the new tab in. Defaults to the current window.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`tabs.Tab`
      
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
      
      The ID of the tab which is to be duplicated.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`tabs.Tab`
      
      Details about the duplicated tab. The :ref:`tabs.Tab` object doesn't contain ``url``, ``title`` and ``favIconUrl`` if the :permission:`tabs` permission has not been requested.
   
   
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
      
      .. api-member::
         :name: [``active``]
         :type: (boolean)
         
         Whether the tabs are active in their windows.
      
      
      .. api-member::
         :name: [``currentWindow``]
         :type: (boolean)
         
         Whether the tabs are in the current window.
      
      
      .. api-member::
         :name: [``highlighted``]
         :type: (boolean)
         
         Whether the tabs are highlighted. Works as an alias of active.
      
      
      .. api-member::
         :name: [``index``]
         :type: (integer)
         
         The position of the tabs within their windows.
      
      
      .. api-member::
         :name: [``lastFocusedWindow``]
         :type: (boolean)
         
         Whether the tabs are in the last focused window.
      
      
      .. api-member::
         :name: [``mailTab``]
         :type: (boolean)
         
         Whether the tab is a Thunderbird 3-pane tab.
      
      
      .. api-member::
         :name: [``status``]
         :type: (:ref:`tabs.TabStatus`)
         
         Whether the tabs have completed loading.
      
      
      .. api-member::
         :name: [``title``]
         :type: (string)
         
         Match page titles against a pattern.
      
      
      .. api-member::
         :name: [``type``]
         :type: (string)
         :annotation: -- [Added in TB 91]
         
         Match tabs against the given Tab.type (see :ref:`tabs.Tab`). Ignored if ``queryInfo.mailTab`` is specified.
      
      
      .. api-member::
         :name: [``url``]
         :type: (string or array of string)
         
         Match tabs against one or more `URL Patterns <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Match_patterns>`_. Note that fragment identifiers are not matched.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer)
         
         The ID of the parent window, or :ref:`windows.WINDOW_ID_CURRENT` for the current window.
      
      
      .. api-member::
         :name: [``windowType``]
         :type: (:ref:`tabs.WindowType`)
         
         The type of window the tabs are in.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`tabs.Tab`
   
   
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
      
      Defaults to the selected tab of the current window.
   
   
   .. api-member::
      :name: ``updateProperties``
      :type: (object)
      
      Properties which should to be updated.
      
      .. api-member::
         :name: [``active``]
         :type: (boolean)
         
         Set this to :value:`true`, if the tab should be active. Does not affect whether the window is focused (see :ref:`windows.update`). Setting this to false has no effect.
      
      
      .. api-member::
         :name: [``url``]
         :type: (string)
         
         A URL to navigate the tab to. Only applicable for :value:`content` tabs and active :value:`mail` tabs.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`tabs.Tab`
      
      Details about the updated tab. The :ref:`tabs.Tab` object doesn't contain ``url``, ``title`` and ``favIconUrl`` if the :permission:`tabs` permission has not been requested.
   
   
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
      
      The tab or list of tabs to move.
   
   
   .. api-member::
      :name: ``moveProperties``
      :type: (object)
      
      .. api-member::
         :name: ``index``
         :type: (integer)
         
         The position to move the window to. :value:`-1` will place the tab at the end of the window.
      
      
      .. api-member::
         :name: [``windowId``]
         :type: (integer)
         
         Defaults to the window the tab is currently in.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`tabs.Tab` or array of :ref:`tabs.Tab`
      
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
      
      The ID of the tab to reload; defaults to the selected tab of the current window.
   
   
   .. api-member::
      :name: [``reloadProperties``]
      :type: (object)
      
      .. api-member::
         :name: [``bypassCache``]
         :type: (boolean)
         
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
      
      The tab or list of tabs to close.
   

.. _tabs.executeScript:

executeScript([tabId], details)
-------------------------------

.. api-section-annotation-hack:: 

Injects JavaScript code into a page. For details, see the `programmatic injection <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`_ section of the content scripts doc.

.. api-header::
   :label: Changes in Thunderbird 77

   
   .. api-member::
      :name: With the :permission:`compose` permission, this now works in the document of email messages during composition.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      The ID of the tab in which to run the script; defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``details``
      :type: (`InjectDetails <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/InjectDetails>`_)
      
      Details of the script to run.
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of any
      
      The result of the script in every injected frame.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _tabs.insertCSS:

insertCSS([tabId], details)
---------------------------

.. api-section-annotation-hack:: 

Injects CSS into a page. For details, see the `programmatic injection <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`_ section of the content scripts doc.

.. api-header::
   :label: Changes in Thunderbird 77

   
   .. api-member::
      :name: With the :permission:`compose` permission, this now works in the document of email messages during composition.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      The ID of the tab in which to insert the CSS; defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``details``
      :type: (`InjectDetails <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/InjectDetails>`_)
      
      Details of the CSS text to insert.
   

.. _tabs.removeCSS:

removeCSS([tabId], details)
---------------------------

.. api-section-annotation-hack:: 

Removes injected CSS from a page. For details, see the `programmatic injection <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts>`_ section of the content scripts doc.

.. api-header::
   :label: Changes in Thunderbird 77

   
   .. api-member::
      :name: With the :permission:`compose` permission, this now works in the document of email messages during composition.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
      
      The ID of the tab from which to remove the injected CSS; defaults to the active tab of the current window.
   
   
   .. api-member::
      :name: ``details``
      :type: (`InjectDetails <https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/extensionTypes/InjectDetails>`_)
      
      Details of the CSS text to remove.
   

.. rst-class:: api-main-section

Events
======

.. _tabs.onCreated:

onCreated
---------

.. api-section-annotation-hack:: 

Fired when a tab is created. Note that the tab's URL may not be set at the time this event fired, but you can listen to onUpdated events to be notified when a URL is set.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   
   .. api-member::
      :name: ``listener(tab)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      
      Details of the tab that was created.
   

.. _tabs.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: 

Fired when a tab is updated.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener, filter)

   
   .. api-member::
      :name: ``listener(tabId, changeInfo, tab)``
      
      A function that will be called when this event occurs.
   
   
   .. api-member::
      :name: [``filter``]
      :type: (:ref:`tabs.UpdateFilter`)
      
      A set of filters that restricts the events that will be sent to this listener.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``changeInfo``
      :type: (object)
      
      Lists the changes to the state of the tab that was updated.
      
      .. api-member::
         :name: [``favIconUrl``]
         :type: (string)
         
         The tab's new favicon URL.
      
      
      .. api-member::
         :name: [``status``]
         :type: (string)
         
         The status of the tab. Can be either :value:`loading` or :value:`complete`.
      
      
      .. api-member::
         :name: [``url``]
         :type: (string)
         
         The tab's URL if it has changed.
      
   
   
   .. api-member::
      :name: ``tab``
      :type: (:ref:`tabs.Tab`)
      
      Gives the state of the tab that was updated.
   

.. _tabs.onMoved:

onMoved
-------

.. api-section-annotation-hack:: 

Fired when a tab is moved within a window. Only one move event is fired, representing the tab the user directly moved. Move events are not fired for the other tabs that must move in response. This event is not fired when a tab is moved between windows. For that, see :ref:`tabs.onDetached`.

.. api-header::
   :label: Parameters for onMoved.addListener(listener)

   
   .. api-member::
      :name: ``listener(tabId, moveInfo)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``moveInfo``
      :type: (object)
      
      .. api-member::
         :name: ``fromIndex``
         :type: (integer)
      
      
      .. api-member::
         :name: ``toIndex``
         :type: (integer)
      
      
      .. api-member::
         :name: ``windowId``
         :type: (integer)
      
   

.. _tabs.onActivated:

onActivated
-----------

.. api-section-annotation-hack:: 

Fires when the active tab in a window changes. Note that the tab's URL may not be set at the time this event fired, but you can listen to onUpdated events to be notified when a URL is set.

.. api-header::
   :label: Parameters for onActivated.addListener(listener)

   
   .. api-member::
      :name: ``listener(activeInfo)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``activeInfo``
      :type: (object)
      
      .. api-member::
         :name: ``tabId``
         :type: (integer)
         
         The ID of the tab that has become active.
      
      
      .. api-member::
         :name: ``windowId``
         :type: (integer)
         
         The ID of the window the active tab changed inside of.
      
   

.. _tabs.onDetached:

onDetached
----------

.. api-section-annotation-hack:: 

Fired when a tab is detached from a window, for example because it is being moved between windows.

.. api-header::
   :label: Parameters for onDetached.addListener(listener)

   
   .. api-member::
      :name: ``listener(tabId, detachInfo)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``detachInfo``
      :type: (object)
      
      .. api-member::
         :name: ``oldPosition``
         :type: (integer)
      
      
      .. api-member::
         :name: ``oldWindowId``
         :type: (integer)
      
   

.. _tabs.onAttached:

onAttached
----------

.. api-section-annotation-hack:: 

Fired when a tab is attached to a window, for example because it was moved between windows.

.. api-header::
   :label: Parameters for onAttached.addListener(listener)

   
   .. api-member::
      :name: ``listener(tabId, attachInfo)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``attachInfo``
      :type: (object)
      
      .. api-member::
         :name: ``newPosition``
         :type: (integer)
      
      
      .. api-member::
         :name: ``newWindowId``
         :type: (integer)
      
   

.. _tabs.onRemoved:

onRemoved
---------

.. api-section-annotation-hack:: 

Fired when a tab is closed.

.. api-header::
   :label: Parameters for onRemoved.addListener(listener)

   
   .. api-member::
      :name: ``listener(tabId, removeInfo)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``tabId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``removeInfo``
      :type: (object)
      
      .. api-member::
         :name: ``isWindowClosing``
         :type: (boolean)
         
         Is :value:`true` when the tab is being closed because its window is being closed.
      
      
      .. api-member::
         :name: ``windowId``
         :type: (integer)
         
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
      
      Whether the tab is active in its window. (Does not necessarily mean the window is focused.)
   
   
   .. api-member::
      :name: ``highlighted``
      :type: (boolean)
      
      Whether the tab is highlighted. Works as an alias of active
   
   
   .. api-member::
      :name: ``index``
      :type: (integer)
      
      The zero-based index of the tab within its window.
   
   
   .. api-member::
      :name: ``selected``
      :type: (boolean) **Unsupported.**
      
      Whether the tab is selected.
   
   
   .. api-member::
      :name: [``favIconUrl``]
      :type: (string)
      
      The URL of the tab's favicon. This property is only present if the extension's manifest includes the :permission:`tabs` permission. It may also be an empty string if the tab is loading.
   
   
   .. api-member::
      :name: [``height``]
      :type: (integer)
      
      The height of the tab in pixels.
   
   
   .. api-member::
      :name: [``id``]
      :type: (integer)
      
      The ID of the tab. Tab IDs are unique within a session. Under some circumstances a Tab may not be assigned an ID. Tab ID can also be set to :ref:`tabs.TAB_ID_NONE` for apps and devtools windows.
   
   
   .. api-member::
      :name: [``mailTab``]
      :type: (boolean)
      
      Whether the tab is a 3-pane tab.
   
   
   .. api-member::
      :name: [``status``]
      :type: (string)
      
      Either :value:`loading` or :value:`complete`.
   
   
   .. api-member::
      :name: [``title``]
      :type: (string)
      
      The title of the tab. This property is only present if the extension's manifest includes the :permission:`tabs` permission.
   
   
   .. api-member::
      :name: [``type``]
      :type: (`string`)
      :annotation: -- [Added in TB 91]
      
      Supported values:
      
      .. api-member::
         :name: ``addressBook``
      
      .. api-member::
         :name: ``calendar``
      
      .. api-member::
         :name: ``calendarEvent``
      
      .. api-member::
         :name: ``calendarTask``
      
      .. api-member::
         :name: ``chat``
      
      .. api-member::
         :name: ``content``
      
      .. api-member::
         :name: ``mail``
      
      .. api-member::
         :name: ``messageCompose``
      
      .. api-member::
         :name: ``messageDisplay``
      
      .. api-member::
         :name: ``special``
      
      .. api-member::
         :name: ``tasks``
   
   
   .. api-member::
      :name: [``url``]
      :type: (string)
      
      The URL the tab is displaying. This property is only present if the extension's manifest includes the :permission:`tabs` permission.
   
   
   .. api-member::
      :name: [``width``]
      :type: (integer)
      
      The width of the tab in pixels.
   
   
   .. api-member::
      :name: [``windowId``]
      :type: (integer)
      
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
      
      A list of property names. Events that do not match any of the names will be filtered out.
   
   
   .. api-member::
      :name: [``tabId``]
      :type: (integer)
   
   
   .. api-member::
      :name: [``urls``]
      :type: (array of string)
      
      A list of URLs or URL patterns. Events that cannot match any of the URLs will be filtered out. Filtering with urls requires the :permission:`tabs` or  :permission:`activeTab` permission.
   
   
   .. api-member::
      :name: [``windowId``]
      :type: (integer)
   

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

The type of a window. Under some circumstances a Window may not be assigned a type property.

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
         
         .. api-member::
            :name: ``messageCompose``
         
         .. api-member::
            :name: ``messageDisplay``
   

.. rst-class:: api-main-section

Properties
==========

.. _tabs.TAB_ID_NONE:

TAB_ID_NONE
-----------

.. api-section-annotation-hack:: 

An ID which represents the absence of a tab.
