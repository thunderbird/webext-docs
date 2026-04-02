.. container:: sticky-sidebar

  ≡ extension API

  * `Functions`_
  * `Types`_
  * `Properties`_

  .. include:: /_includes/developer-resources.rst

=============
extension API
=============

.. role:: permission

.. role:: value

.. role:: code

.. role:: small

.. hint::

   The extension API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/extension>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

The :code:`browser.extension` API has utilities that can be used by any extension page. It includes support for exchanging messages between an extension and its content scripts or between extensions, as described in detail in Message Passing.

.. rst-class:: api-main-section

Functions
=========

.. _extension.get^background^page:

getBackgroundPage()
-------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Returns the JavaScript 'window' object for the background page running inside the current extension. Returns null if the extension has no background page.

.. api-header::
   :label: Return type (`Promise`_)

   .. _extension.get^background^page.returns:

   .. api-member::
      :refid: extension-get-background-page-returns
      :refname: _returns
      :type: `Window <https://developer.mozilla.org/en-US/docs/Web/API/Window>`__

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _extension.get^u^r^l:

getURL(path)
------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Converts a relative path within an extension install directory to a fully-qualified URL.

.. api-header::
   :label: Parameters

   .. _extension.get^u^r^l.path:

   .. api-member::
      :name: ``path``
      :refid: extension-get-u-r-l-path
      :refname: path
      :type: (string)

      A path to a resource within an extension expressed relative to its install directory.

.. api-header::
   :label: Return type (`Promise`_)

   .. _extension.get^u^r^l.returns:

   .. api-member::
      :refid: extension-get-u-r-l-returns
      :refname: _returns
      :type: string

      The fully-qualified URL to the resource.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _extension.get^views:

getViews([fetchProperties])
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Returns an array of the JavaScript 'window' objects for each of the pages running inside the current extension.

.. note::

   If this is called from a page that is part of a private browsing window, such as a sidebar in a private window or a popup opened from a private window, then its return value will not include the extension's background page.

.. api-header::
   :label: Parameters

   .. _extension.get^views.fetch^properties:

   .. api-member::
      :name: [``fetchProperties``]
      :refid: extension-get-views-fetch-properties
      :refname: fetchProperties
      :type: (object, optional)

      .. _extension.get^views.fetch^properties.tab^id:

      .. api-member::
         :name: [``tabId``]
         :refid: extension-get-views-fetch-properties-tab-id
         :refname: tabId
         :type: (integer, optional)

         Find a view according to a tab id. If this field is omitted, returns all views.

      .. _extension.get^views.fetch^properties.type:

      .. api-member::
         :name: [``type``]
         :refid: extension-get-views-fetch-properties-type
         :refname: type
         :type: (:ref:`extension.^view^type`, optional)

         The type of view to get. If omitted, returns all views (including background pages and tabs). Valid values: 'tab', 'popup', 'sidebar'.

      .. _extension.get^views.fetch^properties.window^id:

      .. api-member::
         :name: [``windowId``]
         :refid: extension-get-views-fetch-properties-window-id
         :refname: windowId
         :type: (integer, optional)

         The window to restrict the search to. If omitted, returns all views.

.. api-header::
   :label: Return type (`Promise`_)

   .. _extension.get^views.returns:

   .. api-member::
      :refid: extension-get-views-returns
      :refname: _returns
      :type: array of `Window <https://developer.mozilla.org/en-US/docs/Web/API/Window>`__

      Array of global objects

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _extension.is^allowed^file^scheme^access:

isAllowedFileSchemeAccess()
---------------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Retrieves the state of the extension's access to the 'file://' scheme (as determined by the user-controlled 'Allow access to File URLs' checkbox.

.. api-header::
   :label: Return type (`Promise`_)

   .. _extension.is^allowed^file^scheme^access.returns:

   .. api-member::
      :refid: extension-is-allowed-file-scheme-access-returns
      :refname: _returns
      :type: boolean

      True if the extension can access the 'file://' scheme, false otherwise.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. _extension.is^allowed^incognito^access:

isAllowedIncognitoAccess()
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Retrieves the state of the extension's access to Incognito-mode (as determined by the user-controlled 'Allowed in Incognito' checkbox.

.. api-header::
   :label: Return type (`Promise`_)

   .. _extension.is^allowed^incognito^access.returns:

   .. api-member::
      :refid: extension-is-allowed-incognito-access-returns
      :refname: _returns
      :type: boolean

      True if the extension has access to Incognito mode, false otherwise.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. rst-class:: api-main-section

Types
=====

.. _extension.^view^type:

ViewType
--------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

The type of extension view.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _extension.^view^type.popup:

         .. api-member::
            :name: :value:`popup`
            :refid: extension-view-type-popup
            :refname: popup

         .. _extension.^view^type.sidebar:

         .. api-member::
            :name: :value:`sidebar`
            :refid: extension-view-type-sidebar
            :refname: sidebar

         .. _extension.^view^type.tab:

         .. api-member::
            :name: :value:`tab`
            :refid: extension-view-type-tab
            :refname: tab

.. rst-class:: api-main-section

Properties
==========

.. _extension.in^incognito^context:

inIncognitoContext
------------------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

True for content scripts running inside incognito tabs, and for extension pages running inside an incognito process. The latter only applies to extensions with 'split' incognito_behavior.

.. _extension.last^error:

lastError
---------

.. api-section-annotation-hack:: -- [Added in TB 60.0]

Set for the lifetime of a callback if an ansychronous extension api has resulted in an error. If no error has occured lastError will be :value:`undefined`.
