.. container:: sticky-sidebar

  ≡ windows API

  * `Functions`_
  * `Events`_
  * `Types`_
  * `Properties`_

  .. include:: /overlay/developer-resources.rst

  ≡ Related information
  
  * :doc:`/examples/eventListeners`

  ≡ Related examples on Github

  * `"Await Popup" example <https://github.com/thunderbird/sample-extensions/tree/master/manifest_v3/awaitPopup>`__

===========
windows API
===========

.. note::

  These APIs are for the main Thunderbird windows which can contain webpage tabs and also other
  window types like composer that cannot contain webpage tabs. Make sure your
  code interacts with windows appropriately, depending on their type.

.. role:: permission

.. role:: value

.. role:: code

The windows API supports creating, modifying and interacting with Thunderbird windows.

.. rst-class:: api-main-section

Functions
=========

.. _windows.create:

create([createData])
--------------------

.. api-section-annotation-hack:: 

Creates (opens) a new window with any optional sizing, position or default URL provided. When loading a page into a popup window, same-site links are opened within the same window, all other links are opened in the user's default browser. To override this behavior, add-ons have to register a `content script <https://bugzilla.mozilla.org/show_bug.cgi?id=1618828#c3>`__ , capture click events and handle them manually. Same-site links with targets other than :value:`_self` are opened in a new tab in the most recent ``normal`` Thunderbird window.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``createData``]
      :type: (object, optional)
      
      .. api-member::
         :name: [``allowScriptsToClose``]
         :type: (boolean, optional)
         
         Allow scripts running inside the window to close the window by calling :code:`window.close()`.
      
      
      .. api-member::
         :name: [``cookieStoreId``]
         :type: (string, optional)
         
         The CookieStoreId to use for all tabs that were created when the window is opened.
      
      
      .. api-member::
         :name: [``focused``]
         :type: (boolean, optional) **Unsupported.**
         
         If true, opens an active window. If false, opens an inactive window.
      
      
      .. api-member::
         :name: [``height``]
         :type: (integer, optional)
         
         The height in pixels of the new window, including the frame. If not specified defaults to a natural height.
      
      
      .. api-member::
         :name: [``incognito``]
         :type: (boolean, optional) **Unsupported.**
      
      
      .. api-member::
         :name: [``left``]
         :type: (integer, optional)
         
         The number of pixels to position the new window from the left edge of the screen. If not specified, the new window is offset naturally from the last focused window.
      
      
      .. api-member::
         :name: [``state``]
         :type: (:ref:`windows.WindowState`, optional)
         
         The initial state of the window. The ``minimized``, ``maximized`` and ``fullscreen`` states cannot be combined with ``left``, ``top``, ``width`` or ``height``.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer, optional)
         
         The id of the tab for which you want to adopt to the new window.
      
      
      .. api-member::
         :name: [``titlePreface``]
         :type: (string, optional)
         
         A string to add to the beginning of the window title.
      
      
      .. api-member::
         :name: [``top``]
         :type: (integer, optional)
         
         The number of pixels to position the new window from the top edge of the screen. If not specified, the new window is offset naturally from the last focused window.
      
      
      .. api-member::
         :name: [``type``]
         :type: (:ref:`windows.CreateType`, optional)
         
         Specifies what type of window to create. Thunderbird does not support :value:`panel` and :value:`detached_panel`, they are interpreted as :value:`popup`.
      
      
      .. api-member::
         :name: [``url``]
         :type: (string or array of string, optional)
         
         A URL to be opened in a popup window, ignored in all other window types. This may also be an array, but only the first element is used (popup windows may not have multiple tabs). If the URL points to a content page (a web page, an extension page or a registered WebExtension protocol handler page), the popup window will navigate to the requested page. All other URLs will be opened externally after creating an empty popup window. Fully-qualified URLs must include a scheme (i.e. :value:`http://www.google.com`, not :value:`www.google.com`). Relative URLs will be relative to the root of the extension. Defaults to the New Tab Page.
      
      
      .. api-member::
         :name: [``width``]
         :type: (integer, optional)
         
         The width in pixels of the new window, including the frame. If not specified defaults to a natural width.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`windows.Window`
      
      Contains details about the created window.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.get:

get(windowId, [getInfo])
------------------------

.. api-section-annotation-hack:: 

Gets details about a window.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``windowId``
      :type: (integer)
   
   
   .. api-member::
      :name: [``getInfo``]
      :type: (:ref:`windows.GetInfo`, optional)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`windows.Window`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.getAll:

getAll([getInfo])
-----------------

.. api-section-annotation-hack:: 

Gets all windows.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``getInfo``]
      :type: (:ref:`windows.GetInfo`, optional)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`windows.Window`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.getCurrent:

getCurrent([getInfo])
---------------------

.. api-section-annotation-hack:: 

Gets the active or topmost window.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``getInfo``]
      :type: (:ref:`windows.GetInfo`, optional)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`windows.Window`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.getLastFocused:

getLastFocused([getInfo])
-------------------------

.. api-section-annotation-hack:: 

Gets the window that was most recently focused — typically the window 'on top'.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``getInfo``]
      :type: (:ref:`windows.GetInfo`, optional)
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`windows.Window`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.openDefaultBrowser:

openDefaultBrowser(url)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 84, backported to TB 78.6.0]

Opens the provided URL in the default system browser.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``url``
      :type: (string)
   

.. _windows.remove:

remove(windowId)
----------------

.. api-section-annotation-hack:: 

Removes (closes) a window, and all the tabs inside it.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``windowId``
      :type: (integer)
   

.. _windows.update:

update(windowId, updateInfo)
----------------------------

.. api-section-annotation-hack:: 

Updates the properties of a window. Specify only the properties that you want to change; unspecified properties will be left unchanged.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``windowId``
      :type: (integer)
   
   
   .. api-member::
      :name: ``updateInfo``
      :type: (object)
      
      .. api-member::
         :name: [``drawAttention``]
         :type: (boolean, optional)
         
         Setting this to :value:`true` will cause the window to be displayed in a manner that draws the user's attention to the window, without changing the focused window. The effect lasts until the user changes focus to the window. This option has no effect if the window already has focus.
      
      
      .. api-member::
         :name: [``focused``]
         :type: (boolean, optional)
         
         If true, brings the window to the front. If false, brings the next window in the z-order to the front.
      
      
      .. api-member::
         :name: [``height``]
         :type: (integer, optional)
         
         The height to resize the window to in pixels.
      
      
      .. api-member::
         :name: [``left``]
         :type: (integer, optional)
         
         The offset from the left edge of the screen to move the window to in pixels. This value is ignored for panels.
      
      
      .. api-member::
         :name: [``state``]
         :type: (:ref:`windows.WindowState`, optional)
         
         The new state of the window. The ``minimized``, ``maximized`` and ``fullscreen`` states cannot be combined with ``left``, ``top``, ``width`` or ``height``.
      
      
      .. api-member::
         :name: [``titlePreface``]
         :type: (string, optional)
         
         A string to add to the beginning of the window title.
      
      
      .. api-member::
         :name: [``top``]
         :type: (integer, optional)
         
         The offset from the top edge of the screen to move the window to in pixels. This value is ignored for panels.
      
      
      .. api-member::
         :name: [``width``]
         :type: (integer, optional)
         
         The width to resize the window to in pixels.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: :ref:`windows.Window`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Events
======

.. _windows.onCreated:

onCreated
---------

.. api-section-annotation-hack:: 

Fired when a window is created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   
   .. api-member::
      :name: ``listener(window)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``window``
      :type: (:ref:`windows.Window`)
      
      Details of the window that was created.
   

.. _windows.onFocusChanged:

onFocusChanged
--------------

.. api-section-annotation-hack:: 

Fired when the currently focused window changes. Will be :ref:`windows.WINDOW_ID_NONE`, if all windows have lost focus. **Note:** On some Linux window managers, WINDOW_ID_NONE will always be sent immediately preceding a switch from one window to another.

.. api-header::
   :label: Parameters for onFocusChanged.addListener(listener)

   
   .. api-member::
      :name: ``listener(windowId)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``windowId``
      :type: (integer)
      
      ID of the newly focused window.
   

.. _windows.onRemoved:

onRemoved
---------

.. api-section-annotation-hack:: 

Fired when a window is removed (closed).

.. api-header::
   :label: Parameters for onRemoved.addListener(listener)

   
   .. api-member::
      :name: ``listener(windowId)``
      
      A function that will be called when this event occurs.
   

.. api-header::
   :label: Parameters passed to the listener function

   
   .. api-member::
      :name: ``windowId``
      :type: (integer)
      
      ID of the removed window.
   

.. rst-class:: api-main-section

Types
=====

.. _windows.CreateType:

CreateType
----------

.. api-section-annotation-hack:: 

Specifies what type of window to create. Thunderbird does not support :value:`panel` and :value:`detached_panel`, they are interpreted as :value:`popup`.

.. api-header::
   :label: `string`

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         Supported values:
         
         .. api-member::
            :name: :value:`normal`
         
            A normal Thunderbird window, a.k.a. 3-pane-window (folder pane, message pane and preview pane).
         
         .. api-member::
            :name: :value:`popup`
         
            A non-modal stand-alone popup window.
         
         .. api-member::
            :name: :value:`panel`
         
            Not supported, same as :value:`popup`
         
         .. api-member::
            :name: :value:`detached_panel`
         
            Not supported, same as :value:`popup`
   

.. _windows.GetInfo:

GetInfo
-------

.. api-section-annotation-hack:: 

Specifies additional requirements for the returned windows.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``populate``]
      :type: (boolean, optional)
      
      If true, the :ref:`windows.Window` returned will have a ``tabs`` property that contains an array of :ref:`tabs.Tab` objects representing the tabs inside the window. The :ref:`tabs.Tab` objects only contain the ``url``, ``title`` and ``favIconUrl`` properties if the extension's manifest file includes the :permission:`tabs` permission.
   
   
   .. api-member::
      :name: [``windowTypes``]
      :type: (array of :ref:`windows.WindowType`, optional)
      
      If set, the :ref:`windows.Window` returned will be filtered based on its type. Supported by :ref:`windows.getAll` only, ignored in all other functions.
   

.. _windows.Window:

Window
------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``alwaysOnTop``
      :type: (boolean)
      
      Whether the window is set to be always on top.
   
   
   .. api-member::
      :name: ``focused``
      :type: (boolean)
      
      Whether the window is currently the focused window.
   
   
   .. api-member::
      :name: ``incognito``
      :type: (boolean)
      
      Whether the window is incognito. Since Thunderbird does not support the incognito mode, this is always :value:`false`.
   
   
   .. api-member::
      :name: [``height``]
      :type: (integer, optional)
      
      The height of the window, including the frame, in pixels.
   
   
   .. api-member::
      :name: [``id``]
      :type: (integer, optional)
      
      The ID of the window. Window IDs are unique within a session.
   
   
   .. api-member::
      :name: [``left``]
      :type: (integer, optional)
      
      The offset of the window from the left edge of the screen in pixels.
   
   
   .. api-member::
      :name: [``state``]
      :type: (:ref:`windows.WindowState`, optional)
      
      The state of this window.
   
   
   .. api-member::
      :name: [``tabs``]
      :type: (array of :ref:`tabs.Tab`, optional)
      
      Array of :ref:`tabs.Tab` objects representing the current tabs in the window. Only included if requested by :ref:`windows.get`, :ref:`windows.getCurrent`, :ref:`windows.getAll` or :ref:`windows.getLastFocused`, and the optional :ref:`windows.GetInfo` parameter has its ``populate`` member set to :value:`true`.
   
   
   .. api-member::
      :name: [``title``]
      :type: (string, optional)
      
      The title of the window. Read-only.
   
   
   .. api-member::
      :name: [``top``]
      :type: (integer, optional)
      
      The offset of the window from the top edge of the screen in pixels.
   
   
   .. api-member::
      :name: [``type``]
      :type: (:ref:`windows.WindowType`, optional)
      
      The type of window this is.
   
   
   .. api-member::
      :name: [``width``]
      :type: (integer, optional)
      
      The width of the window, including the frame, in pixels.
   

.. _windows.WindowState:

WindowState
-----------

.. api-section-annotation-hack:: 

The state of this window.

.. api-header::
   :label: `string`

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         Supported values:
         
         .. api-member::
            :name: :value:`normal`
         
         .. api-member::
            :name: :value:`minimized`
         
         .. api-member::
            :name: :value:`maximized`
         
         .. api-member::
            :name: :value:`fullscreen`
         
         .. api-member::
            :name: :value:`docked`
   

.. _windows.WindowType:

WindowType
----------

.. api-section-annotation-hack:: 

The type of a window. Under some circumstances a window may not be assigned a type property.

.. api-header::
   :label: `string`

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         Supported values:
         
         .. api-member::
            :name: :value:`normal`
         
            A normal Thunderbird window, a.k.a. 3-pane-window (folder pane, message pane and preview pane).
         
         .. api-member::
            :name: :value:`popup`
         
            A non-modal stand-alone popup window.
         
         .. api-member::
            :name: :value:`messageCompose`
            :annotation: -- [Added in TB 70, backported to TB 68.1.1]
         
            A non-modal stand-alone message compose window.
         
         .. api-member::
            :name: :value:`messageDisplay`
            :annotation: -- [Added in TB 70, backported to TB 68.1.1]
         
            A non-modal stand-alone message display window, viewing a single message.
   

.. rst-class:: api-main-section

Properties
==========

.. _windows.WINDOW_ID_CURRENT:

WINDOW_ID_CURRENT
-----------------

.. api-section-annotation-hack:: 

The windowId value that represents the current window.

.. _windows.WINDOW_ID_NONE:

WINDOW_ID_NONE
--------------

.. api-section-annotation-hack:: 

The windowId value that represents the absence of a window.
