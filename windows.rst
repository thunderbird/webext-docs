=======
windows
=======

.. note::

  These APIs are for the main Thunderbird windows which can contain webpage tabs and also other
  window types like composer or address books that cannot contain webpage tabs.  Make sure your
  code interacts with windows appropriately, depending on their type.

Use the ``browser.windows`` API to interact with Thunderbird. You can use this API to create, modify, and rearrange windows.

.. rst-class:: api-main-section

Functions
=========

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
      :annotation: 
   
   
   .. api-member::
      :name: [``getInfo``]
      :type: (:ref:`windows.GetInfo`)
      :annotation: 
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`windows.Window`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.getCurrent:

getCurrent([getInfo])
---------------------

.. api-section-annotation-hack:: 

Gets the current window.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``getInfo``]
      :type: (:ref:`windows.GetInfo`)
      :annotation: 
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`windows.Window`
      :annotation: 
   
   
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
      :type: (:ref:`windows.GetInfo`)
      :annotation: 
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`windows.Window`
      :annotation: 
   
   
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
      :type: (:ref:`windows.GetInfo`)
      :annotation: 
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: array of :ref:`windows.Window`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _windows.create:

create([createData])
--------------------

.. api-section-annotation-hack:: 

Creates (opens) a new browser with any optional sizing, position or default URL provided.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``createData``]
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``allowScriptsToClose``]
         :type: (boolean)
         :annotation: 
         
         Allow scripts to close the window.
      
      
      .. api-member::
         :name: [``focused``]
         :type: (boolean) **Unsupported.**
         :annotation: 
         
         If true, opens an active window. If false, opens an inactive window.
      
      
      .. api-member::
         :name: [``height``]
         :type: (integer)
         :annotation: 
         
         The height in pixels of the new window, including the frame. If not specified defaults to a natural height.
      
      
      .. api-member::
         :name: [``incognito``]
         :type: (boolean)
         :annotation: 
         
         Whether the new window should be an incognito window.
      
      
      .. api-member::
         :name: [``left``]
         :type: (integer)
         :annotation: 
         
         The number of pixels to position the new window from the left edge of the screen. If not specified, the new window is offset naturally from the last focused window. This value is ignored for panels.
      
      
      .. api-member::
         :name: [``state``]
         :type: (:ref:`windows.WindowState`)
         :annotation: 
         
         The initial state of the window. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined with 'left', 'top', 'width' or 'height'.
      
      
      .. api-member::
         :name: [``tabId``]
         :type: (integer)
         :annotation: 
         
         The id of the tab for which you want to adopt to the new window.
      
      
      .. api-member::
         :name: [``titlePreface``]
         :type: (string)
         :annotation: 
         
         A string to add to the beginning of the window title.
      
      
      .. api-member::
         :name: [``top``]
         :type: (integer)
         :annotation: 
         
         The number of pixels to position the new window from the top edge of the screen. If not specified, the new window is offset naturally from the last focused window. This value is ignored for panels.
      
      
      .. api-member::
         :name: [``type``]
         :type: (:ref:`windows.CreateType`)
         :annotation: 
         
         Specifies what type of browser window to create. The 'panel' and 'detached_panel' types create a popup unless the '--enable-panels' flag is set.
      
      
      .. api-member::
         :name: [``url``]
         :type: (string or array of string)
         :annotation: 
         
         A URL or array of URLs to open as tabs in the window. Fully-qualified URLs must include a scheme (i.e. 'http://www.google.com', not 'www.google.com'). Relative URLs will be relative to the current page within the extension. Defaults to the New Tab Page.
      
      
      .. api-member::
         :name: [``width``]
         :type: (integer)
         :annotation: 
         
         The width in pixels of the new window, including the frame. If not specified defaults to a natural width.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`windows.Window`
      :annotation: 
      
      Contains details about the created window.
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

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
      :annotation: 
   
   
   .. api-member::
      :name: ``updateInfo``
      :type: (object)
      :annotation: 
      
      .. api-member::
         :name: [``drawAttention``]
         :type: (boolean)
         :annotation: 
         
         If true, causes the window to be displayed in a manner that draws the user's attention to the window, without changing the focused window. The effect lasts until the user changes focus to the window. This option has no effect if the window already has focus. Set to false to cancel a previous draw attention request.
      
      
      .. api-member::
         :name: [``focused``]
         :type: (boolean)
         :annotation: 
         
         If true, brings the window to the front. If false, brings the next window in the z-order to the front.
      
      
      .. api-member::
         :name: [``height``]
         :type: (integer)
         :annotation: 
         
         The height to resize the window to in pixels. This value is ignored for panels.
      
      
      .. api-member::
         :name: [``left``]
         :type: (integer)
         :annotation: 
         
         The offset from the left edge of the screen to move the window to in pixels. This value is ignored for panels.
      
      
      .. api-member::
         :name: [``state``]
         :type: (:ref:`windows.WindowState`)
         :annotation: 
         
         The new state of the window. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined with 'left', 'top', 'width' or 'height'.
      
      
      .. api-member::
         :name: [``titlePreface``]
         :type: (string)
         :annotation: 
         
         A string to add to the beginning of the window title.
      
      
      .. api-member::
         :name: [``top``]
         :type: (integer)
         :annotation: 
         
         The offset from the top edge of the screen to move the window to in pixels. This value is ignored for panels.
      
      
      .. api-member::
         :name: [``width``]
         :type: (integer)
         :annotation: 
         
         The width to resize the window to in pixels. This value is ignored for panels.
      
   

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :name: 
      :type: :ref:`windows.Window`
      :annotation: 
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

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
      :annotation: 
   

.. _windows.openDefaultBrowser:

openDefaultBrowser(url)
-----------------------

.. api-section-annotation-hack:: -- [Added in TB 84, backported to TB 78.6]

Opens the provided URL in the default system browser.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``url``
      :type: (string)
      :annotation: 
   

.. rst-class:: api-main-section

Events
======

.. _windows.onCreated:

onCreated(window)
-----------------

.. api-section-annotation-hack:: 

Fired when a window is created.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``window``
      :type: (:ref:`windows.Window`)
      :annotation: 
      
      Details of the window that was created.
   

.. _windows.onRemoved:

onRemoved(windowId)
-------------------

.. api-section-annotation-hack:: 

Fired when a window is removed (closed).

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``windowId``
      :type: (integer)
      :annotation: 
      
      ID of the removed window.
   

.. _windows.onFocusChanged:

onFocusChanged(windowId)
------------------------

.. api-section-annotation-hack:: 

Fired when the currently focused window changes. Will be :ref:`windows.WINDOW_ID_NONE`) if all browser windows have lost focus. Note: On some Linux window managers, WINDOW_ID_NONE will always be sent immediately preceding a switch from one browser window to another.

.. api-header::
   :label: Parameters for event listeners

   
   .. api-member::
      :name: ``windowId``
      :type: (integer)
      :annotation: 
      
      ID of the newly focused window.
   

.. rst-class:: api-main-section

Types
=====

.. _windows.CreateType:

CreateType
----------

.. api-section-annotation-hack:: 

Specifies what type of browser window to create. The 'panel' and 'detached_panel' types create a popup unless the '--enable-panels' flag is set.

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
            :name: ``detached_panel``
         
   

.. _windows.GetInfo:

GetInfo
-------

.. api-section-annotation-hack:: 

Specifies properties used to filter the :ref:`windows.Window` returned and to determine whether they should contain a list of the :ref:`tabs.Tab` objects.

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``populate``]
      :type: (boolean)
      :annotation: 
      
      If true, the :ref:`windows.Window` returned will have a ``tabs`` property that contains a list of the :ref:`tabs.Tab` objects. The ``Tab`` objects only contain the ``url``, ``title`` and ``favIconUrl`` properties if the extension's manifest file includes the ``tabs`` permission.
   
   
   .. api-member::
      :name: [``windowTypes``]
      :type: (array of :ref:`windows.WindowType`)
      :annotation: 
      
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
      :annotation: 
      
      Whether the window is set to be always on top.
   
   
   .. api-member::
      :name: ``focused``
      :type: (boolean)
      :annotation: 
      
      Whether the window is currently the focused window.
   
   
   .. api-member::
      :name: ``incognito``
      :type: (boolean)
      :annotation: 
      
      Whether the window is incognito.
   
   
   .. api-member::
      :name: [``height``]
      :type: (integer)
      :annotation: 
      
      The height of the window, including the frame, in pixels.
   
   
   .. api-member::
      :name: [``id``]
      :type: (integer)
      :annotation: 
      
      The ID of the window. Window IDs are unique within a session.
   
   
   .. api-member::
      :name: [``left``]
      :type: (integer)
      :annotation: 
      
      The offset of the window from the left edge of the screen in pixels.
   
   
   .. api-member::
      :name: [``state``]
      :type: (:ref:`windows.WindowState`)
      :annotation: 
      
      The state of this browser window.
   
   
   .. api-member::
      :name: [``tabs``]
      :type: (array of :ref:`tabs.Tab`)
      :annotation: 
      
      Array of :ref:`tabs.Tab` objects representing the current tabs in the window.
   
   
   .. api-member::
      :name: [``title``]
      :type: (string)
      :annotation: 
      
      The title of the window. Read-only.
   
   
   .. api-member::
      :name: [``top``]
      :type: (integer)
      :annotation: 
      
      The offset of the window from the top edge of the screen in pixels.
   
   
   .. api-member::
      :name: [``type``]
      :type: (:ref:`windows.WindowType`)
      :annotation: 
      
      The type of browser window this is.
   
   
   .. api-member::
      :name: [``width``]
      :type: (integer)
      :annotation: 
      
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
            :name: ``normal``
         
         .. api-member::
            :name: ``minimized``
         
         .. api-member::
            :name: ``maximized``
         
         .. api-member::
            :name: ``fullscreen``
         
         .. api-member::
            :name: ``docked``
         
   

.. _windows.WindowType:

WindowType
----------

.. api-section-annotation-hack:: 

The type of window this is. Under some circumstances a Window may not be assigned a type property.

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
            :name: ``addressBook``
            :annotation: -- [Added in TB 70, backported to TB 68.1.1]
         
         .. api-member::
            :name: ``messageCompose``
            :annotation: -- [Added in TB 70, backported to TB 68.1.1]
         
         .. api-member::
            :name: ``messageDisplay``
            :annotation: -- [Added in TB 70, backported to TB 68.1.1]
         
   

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
