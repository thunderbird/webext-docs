.. container:: sticky-sidebar

  ≡ downloads API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

=============
downloads API
=============

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The downloads API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/downloads>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`downloads`

   Download files and read and modify the browser’s download history

.. api-member::
   :name: :permission:`downloads.open`

   Open files downloaded to your computer

Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`downloads` is required to use ``messenger.downloads.*``.

.. rst-class:: api-main-section

Functions
=========

.. _downloads.cancel:

cancel(downloadId)
------------------

.. api-section-annotation-hack:: -- [Added in TB 48]

Cancel a download. When :code:`callback` is run, the download is cancelled, completed, interrupted or doesn't exist anymore.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``downloadId``
      :type: (integer)

      The id of the download to cancel.

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.download:

download(options)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 47]

Download a URL. If the URL uses the HTTP[S] protocol, then the request will include all cookies currently set for its hostname. If both :code:`filename` and :code:`saveAs` are specified, then the Save As dialog will be displayed, pre-populated with the specified :code:`filename`. If the download started successfully, :code:`callback` will be called with the new `DownloadItem <#type-DownloadItem>`__'s :code:`downloadId`. If there was an error starting the download, then :code:`callback` will be called with :code:`downloadId=undefined` and `chrome.extension.lastError <extension.html#property-lastError>`__ will contain a descriptive string. The error strings are not guaranteed to remain backwards compatible between releases. You must not parse it.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``options``
      :type: (object)

      What to download and how.

      .. api-member::
         :name: ``url``
         :type: (string)

         The URL to download.

      .. api-member::
         :name: [``allowHttpErrors``]
         :type: (boolean, optional)

         When this flag is set to :code:`true`, then the browser will allow downloads to proceed after encountering HTTP errors such as :code:`404 Not Found`.

      .. api-member::
         :name: [``body``]
         :type: (string, optional)

         Post body.

      .. api-member::
         :name: [``conflictAction``]
         :type: (:ref:`downloads.FilenameConflictAction`, optional)

      .. api-member::
         :name: [``cookieStoreId``]
         :type: (string, optional)

         The cookie store ID of the contextual identity; requires "cookies" permission.

      .. api-member::
         :name: [``filename``]
         :type: (string, optional)

         A file path relative to the Downloads directory to contain the downloaded file.

      .. api-member::
         :name: [``headers``]
         :type: (array of object, optional)

         Extra HTTP headers to send with the request if the URL uses the HTTP[s] protocol. Each header is represented as a dictionary containing the keys :code:`name` and either :code:`value` or :code:`binaryValue`, restricted to those allowed by XMLHttpRequest.

      .. api-member::
         :name: [``incognito``]
         :type: (boolean, optional)

         Whether to associate the download with a private browsing session.

      .. api-member::
         :name: [``method``]
         :type: (`string`, optional)

         The HTTP method to use if the URL uses the HTTP[S] protocol.

         Supported values:

         .. api-member::
            :name: :value:`GET`

         .. api-member::
            :name: :value:`POST`

      .. api-member::
         :name: [``saveAs``]
         :type: (boolean, optional)

         Use a file-chooser to allow the user to select a filename. If the option is not specified, the file chooser will be shown only if the Thunderbird "Always ask you where to save files" option is enabled (i.e. the pref :code:`browser.download.useDownloadDir` is set to :code:`false`).

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: integer

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.drag:

drag(downloadId)
----------------

.. api-section-annotation-hack:: 

Initiate dragging the file to another application.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``downloadId``
      :type: (integer)

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.erase:

erase(query)
------------

.. api-section-annotation-hack:: -- [Added in TB 48]

Erase matching `DownloadItems <#type-DownloadItem>`__ from history

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``query``
      :type: (:ref:`downloads.DownloadQuery`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of integer

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.getFileIcon:

getFileIcon(downloadId, [options])
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 48]

Retrieve an icon for the specified download. For new downloads, file icons are available after the `onCreated <#event-onCreated>`__ event has been received. The image returned by this function while a download is in progress may be different from the image returned after the download is complete. Icon retrieval is done by querying the underlying operating system or toolkit depending on the platform. The icon that is returned will therefore depend on a number of factors including state of the download, platform, registered file types and visual theme. If a file icon cannot be determined, `chrome.extension.lastError <extension.html#property-lastError>`__ will contain an error message.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``downloadId``
      :type: (integer)

      The identifier for the download.

   .. api-member::
      :name: [``options``]
      :type: (object, optional)

      .. api-member::
         :name: [``size``]
         :type: (integer, optional)

         The size of the icon.  The returned icon will be square with dimensions size * size pixels.  The default size for the icon is 32x32 pixels.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: string

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.open:

open(downloadId)
----------------

.. api-section-annotation-hack:: -- [Added in TB 48]

Open the downloaded file.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``downloadId``
      :type: (integer)

.. api-header::
   :label: Required permissions

   - :permission:`downloads`
   - :permission:`downloads.open`

.. _downloads.pause:

pause(downloadId)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 48]

Pause the download. If the request was successful the download is in a paused state. Otherwise `chrome.extension.lastError <extension.html#property-lastError>`__ contains an error message. The request will fail if the download is not active.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``downloadId``
      :type: (integer)

      The id of the download to pause.

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.removeFile:

removeFile(downloadId)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 48]

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``downloadId``
      :type: (integer)

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.resume:

resume(downloadId)
------------------

.. api-section-annotation-hack:: -- [Added in TB 48]

Resume a paused download. If the request was successful the download is in progress and unpaused. Otherwise `chrome.extension.lastError <extension.html#property-lastError>`__ contains an error message. The request will fail if the download is not active.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``downloadId``
      :type: (integer)

      The id of the download to resume.

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.search:

search(query)
-------------

.. api-section-annotation-hack:: -- [Added in TB 47]

Find `DownloadItems <#type-DownloadItem>`__. Set :code:`query` to the empty object to get all `DownloadItems <#type-DownloadItem>`__. To get a specific `DownloadItem <#type-DownloadItem>`__, set only the :code:`id` field.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``query``
      :type: (:ref:`downloads.DownloadQuery`)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`downloads.DownloadItem`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.show:

show(downloadId)
----------------

.. api-section-annotation-hack:: -- [Added in TB 48]

Show the downloaded file in its folder in a file manager.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``downloadId``
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: boolean

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.showDefaultFolder:

showDefaultFolder()
-------------------

.. api-section-annotation-hack:: -- [Added in TB 48]

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. rst-class:: api-main-section

Events
======

.. _downloads.onChanged:

onChanged
---------

.. api-section-annotation-hack:: -- [Added in TB 47]

When any of a `DownloadItem <#type-DownloadItem>`__'s properties except :code:`bytesReceived` changes, this event fires with the :code:`downloadId` and an object containing the properties that changed.

.. api-header::
   :label: Parameters for onChanged.addListener(listener)

   .. api-member::
      :name: ``listener(downloadDelta)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``downloadDelta``
      :type: (object)

      .. api-member::
         :name: ``id``
         :type: (integer)

         The :code:`id` of the `DownloadItem <#type-DownloadItem>`__ that changed.

      .. api-member::
         :name: [``canResume``]
         :type: (:ref:`downloads.BooleanDelta`, optional)

      .. api-member::
         :name: [``danger``]
         :type: (:ref:`downloads.StringDelta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`danger`.

      .. api-member::
         :name: [``endTime``]
         :type: (:ref:`downloads.StringDelta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`endTime`.

      .. api-member::
         :name: [``error``]
         :type: (:ref:`downloads.StringDelta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`error`.

      .. api-member::
         :name: [``exists``]
         :type: (:ref:`downloads.BooleanDelta`, optional)

      .. api-member::
         :name: [``filename``]
         :type: (:ref:`downloads.StringDelta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`filename`.

      .. api-member::
         :name: [``fileSize``]
         :type: (:ref:`downloads.DoubleDelta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`fileSize`.

      .. api-member::
         :name: [``mime``]
         :type: (:ref:`downloads.StringDelta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`mime`.

      .. api-member::
         :name: [``paused``]
         :type: (:ref:`downloads.BooleanDelta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`paused`.

      .. api-member::
         :name: [``startTime``]
         :type: (:ref:`downloads.StringDelta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`startTime`.

      .. api-member::
         :name: [``state``]
         :type: (:ref:`downloads.StringDelta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`state`.

      .. api-member::
         :name: [``totalBytes``]
         :type: (:ref:`downloads.DoubleDelta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`totalBytes`.

      .. api-member::
         :name: [``url``]
         :type: (:ref:`downloads.StringDelta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`url`.

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.onCreated:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 48]

This event fires with the `DownloadItem <#type-DownloadItem>`__ object when a download begins.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. api-member::
      :name: ``listener(downloadItem)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``downloadItem``
      :type: (:ref:`downloads.DownloadItem`)

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.onErased:

onErased
--------

.. api-section-annotation-hack:: -- [Added in TB 48]

Fires with the :code:`downloadId` when a download is erased from history.

.. api-header::
   :label: Parameters for onErased.addListener(listener)

   .. api-member::
      :name: ``listener(downloadId)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``downloadId``
      :type: (integer)

      The :code:`id` of the `DownloadItem <#type-DownloadItem>`__ that was erased.

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. rst-class:: api-main-section

Types
=====

.. _downloads.BooleanDelta:

BooleanDelta
------------

.. api-section-annotation-hack:: -- [Added in TB 47]

.. api-header::
   :label: object

   .. _downloads.BooleanDelta.current:

   .. api-member::
      :name: [``current``]
      :type: (boolean, optional)

   .. _downloads.BooleanDelta.previous:

   .. api-member::
      :name: [``previous``]
      :type: (boolean, optional)

.. _downloads.DangerType:

DangerType
----------

.. api-section-annotation-hack:: -- [Added in TB 47]

<dl><dt>file</dt><dd>The download's filename is suspicious.</dd><dt>url</dt><dd>The download's URL is known to be malicious.</dd><dt>content</dt><dd>The downloaded file is known to be malicious.</dd><dt>uncommon</dt><dd>The download's URL is not commonly downloaded and could be dangerous.</dd><dt>safe</dt><dd>The download presents no known danger to the user's computer.</dd></dl>These string constants will never change, however the set of DangerTypes may change.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`file`

         .. api-member::
            :name: :value:`url`

         .. api-member::
            :name: :value:`content`

         .. api-member::
            :name: :value:`uncommon`

         .. api-member::
            :name: :value:`host`

         .. api-member::
            :name: :value:`unwanted`

         .. api-member::
            :name: :value:`safe`

         .. api-member::
            :name: :value:`accepted`

.. _downloads.DoubleDelta:

DoubleDelta
-----------

.. api-section-annotation-hack:: -- [Added in TB 47]

.. api-header::
   :label: object

   .. _downloads.DoubleDelta.current:

   .. api-member::
      :name: [``current``]
      :type: (number, optional)

   .. _downloads.DoubleDelta.previous:

   .. api-member::
      :name: [``previous``]
      :type: (number, optional)

.. _downloads.DownloadItem:

DownloadItem
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _downloads.DownloadItem.bytesReceived:

   .. api-member::
      :name: ``bytesReceived``
      :type: (number)

      Number of bytes received so far from the host, without considering file compression.

   .. _downloads.DownloadItem.canResume:

   .. api-member::
      :name: ``canResume``
      :type: (boolean)

   .. _downloads.DownloadItem.danger:

   .. api-member::
      :name: ``danger``
      :type: (:ref:`downloads.DangerType`)

      Indication of whether this download is thought to be safe or known to be suspicious.

      .. note::

         Always given as 'safe'.

   .. _downloads.DownloadItem.exists:

   .. api-member::
      :name: ``exists``
      :type: (boolean)

   .. _downloads.DownloadItem.filename:

   .. api-member::
      :name: ``filename``
      :type: (string)

      Absolute local path.

   .. _downloads.DownloadItem.fileSize:

   .. api-member::
      :name: ``fileSize``
      :type: (number)

      Number of bytes in the whole file post-decompression, or -1 if unknown.

   .. _downloads.DownloadItem.id:

   .. api-member::
      :name: ``id``
      :type: (integer)

      An identifier that is persistent across browser sessions.

   .. _downloads.DownloadItem.incognito:

   .. api-member::
      :name: ``incognito``
      :type: (boolean)

      False if this download is recorded in the history, true if it is not recorded.

   .. _downloads.DownloadItem.paused:

   .. api-member::
      :name: ``paused``
      :type: (boolean)

      True if the download has stopped reading data from the host, but kept the connection open.

   .. _downloads.DownloadItem.startTime:

   .. api-member::
      :name: ``startTime``
      :type: (string)

      Number of milliseconds between the unix epoch and when this download began.

   .. _downloads.DownloadItem.state:

   .. api-member::
      :name: ``state``
      :type: (:ref:`downloads.State`)

      Indicates whether the download is progressing, interrupted, or complete.

   .. _downloads.DownloadItem.totalBytes:

   .. api-member::
      :name: ``totalBytes``
      :type: (number)

      Number of bytes in the whole file, without considering file compression, or -1 if unknown.

   .. _downloads.DownloadItem.url:

   .. api-member::
      :name: ``url``
      :type: (string)

      Absolute URL.

   .. _downloads.DownloadItem.byExtensionId:

   .. api-member::
      :name: [``byExtensionId``]
      :type: (string, optional)

   .. _downloads.DownloadItem.byExtensionName:

   .. api-member::
      :name: [``byExtensionName``]
      :type: (string, optional)

   .. _downloads.DownloadItem.cookieStoreId:

   .. api-member::
      :name: [``cookieStoreId``]
      :type: (string, optional)
      :annotation: -- [Added in TB 92]

      The cookie store ID of the contextual identity.

   .. _downloads.DownloadItem.endTime:

   .. api-member::
      :name: [``endTime``]
      :type: (string, optional)

      Number of milliseconds between the unix epoch and when this download ended.

   .. _downloads.DownloadItem.error:

   .. api-member::
      :name: [``error``]
      :type: (:ref:`downloads.InterruptReason`, optional)

      Number indicating why a download was interrupted.

   .. _downloads.DownloadItem.estimatedEndTime:

   .. api-member::
      :name: [``estimatedEndTime``]
      :type: (string, optional)
      :annotation: -- [Added in TB 57]

   .. _downloads.DownloadItem.mime:

   .. api-member::
      :name: [``mime``]
      :type: (string, optional)

      The file's MIME type.

   .. _downloads.DownloadItem.referrer:

   .. api-member::
      :name: [``referrer``]
      :type: (string, optional)

.. _downloads.DownloadQuery:

DownloadQuery
-------------

.. api-section-annotation-hack:: -- [Added in TB 47]

Parameters that combine to specify a predicate that can be used to select a set of downloads.  Used for example in search() and erase()

.. api-header::
   :label: object

   .. _downloads.DownloadQuery.bytesReceived:

   .. api-member::
      :name: [``bytesReceived``]
      :type: (number, optional)

      Number of bytes received so far from the host, without considering file compression.

   .. _downloads.DownloadQuery.cookieStoreId:

   .. api-member::
      :name: [``cookieStoreId``]
      :type: (string, optional)
      :annotation: -- [Added in TB 92]

      The cookie store ID of the contextual identity.

   .. _downloads.DownloadQuery.danger:

   .. api-member::
      :name: [``danger``]
      :type: (:ref:`downloads.DangerType`, optional)

      Indication of whether this download is thought to be safe or known to be suspicious.

   .. _downloads.DownloadQuery.endedAfter:

   .. api-member::
      :name: [``endedAfter``]
      :type: (:ref:`downloads.DownloadTime`, optional)

      Limits results to downloads that ended after the given ms since the epoch.

      .. note::

         The parameter is ignored.

   .. _downloads.DownloadQuery.endedBefore:

   .. api-member::
      :name: [``endedBefore``]
      :type: (:ref:`downloads.DownloadTime`, optional)

      Limits results to downloads that ended before the given ms since the epoch.

      .. note::

         The parameter is ignored.

   .. _downloads.DownloadQuery.endTime:

   .. api-member::
      :name: [``endTime``]
      :type: (string, optional)

   .. _downloads.DownloadQuery.error:

   .. api-member::
      :name: [``error``]
      :type: (:ref:`downloads.InterruptReason`, optional)

      Why a download was interrupted.

   .. _downloads.DownloadQuery.exists:

   .. api-member::
      :name: [``exists``]
      :type: (boolean, optional)

   .. _downloads.DownloadQuery.filename:

   .. api-member::
      :name: [``filename``]
      :type: (string, optional)

      Absolute local path.

   .. _downloads.DownloadQuery.filenameRegex:

   .. api-member::
      :name: [``filenameRegex``]
      :type: (string, optional)

      Limits results to `DownloadItems <#type-DownloadItem>`__ whose :code:`filename` matches the given regular expression.

   .. _downloads.DownloadQuery.fileSize:

   .. api-member::
      :name: [``fileSize``]
      :type: (number, optional)

      Number of bytes in the whole file post-decompression, or -1 if unknown.

   .. _downloads.DownloadQuery.id:

   .. api-member::
      :name: [``id``]
      :type: (integer, optional)

   .. _downloads.DownloadQuery.limit:

   .. api-member::
      :name: [``limit``]
      :type: (integer, optional)

      Setting this integer limits the number of results. Otherwise, all matching `DownloadItems <#type-DownloadItem>`__ will be returned.

   .. _downloads.DownloadQuery.mime:

   .. api-member::
      :name: [``mime``]
      :type: (string, optional)

      The file's MIME type.

   .. _downloads.DownloadQuery.orderBy:

   .. api-member::
      :name: [``orderBy``]
      :type: (array of string, optional)

      Setting elements of this array to `DownloadItem <#type-DownloadItem>`__ properties in order to sort the search results. For example, setting :code:`orderBy='startTime'` sorts the `DownloadItems <#type-DownloadItem>`__ by their start time in ascending order. To specify descending order, prefix :code:`orderBy` with a hyphen: '-startTime'.

   .. _downloads.DownloadQuery.paused:

   .. api-member::
      :name: [``paused``]
      :type: (boolean, optional)

      True if the download has stopped reading data from the host, but kept the connection open.

   .. _downloads.DownloadQuery.query:

   .. api-member::
      :name: [``query``]
      :type: (array of string, optional)

      This array of search terms limits results to `DownloadItems <#type-DownloadItem>`__ whose :code:`filename` or :code:`url` contain all of the search terms that do not begin with a dash '-' and none of the search terms that do begin with a dash.

   .. _downloads.DownloadQuery.startedAfter:

   .. api-member::
      :name: [``startedAfter``]
      :type: (:ref:`downloads.DownloadTime`, optional)

      Limits results to downloads that started after the given ms since the epoch.

   .. _downloads.DownloadQuery.startedBefore:

   .. api-member::
      :name: [``startedBefore``]
      :type: (:ref:`downloads.DownloadTime`, optional)

      Limits results to downloads that started before the given ms since the epoch.

   .. _downloads.DownloadQuery.startTime:

   .. api-member::
      :name: [``startTime``]
      :type: (string, optional)

   .. _downloads.DownloadQuery.state:

   .. api-member::
      :name: [``state``]
      :type: (:ref:`downloads.State`, optional)

      Indicates whether the download is progressing, interrupted, or complete.

   .. _downloads.DownloadQuery.totalBytes:

   .. api-member::
      :name: [``totalBytes``]
      :type: (number, optional)

      Number of bytes in the whole file, without considering file compression, or -1 if unknown.

   .. _downloads.DownloadQuery.totalBytesGreater:

   .. api-member::
      :name: [``totalBytesGreater``]
      :type: (number, optional)

      Limits results to downloads whose totalBytes is greater than the given integer.

   .. _downloads.DownloadQuery.totalBytesLess:

   .. api-member::
      :name: [``totalBytesLess``]
      :type: (number, optional)

      Limits results to downloads whose totalBytes is less than the given integer.

   .. _downloads.DownloadQuery.url:

   .. api-member::
      :name: [``url``]
      :type: (string, optional)

      Absolute URL.

   .. _downloads.DownloadQuery.urlRegex:

   .. api-member::
      :name: [``urlRegex``]
      :type: (string, optional)

      Limits results to `DownloadItems <#type-DownloadItem>`__ whose :code:`url` matches the given regular expression.

.. _downloads.DownloadTime:

DownloadTime
------------

.. api-section-annotation-hack:: -- [Added in TB 47]

A time specified as a Date object, a number or string representing milliseconds since the epoch, or an ISO 8601 string

.. api-header::
   :label: string

OR

.. api-header::
   :label: `Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__

.. _downloads.FilenameConflictAction:

FilenameConflictAction
----------------------

.. api-section-annotation-hack:: -- [Added in TB 47]

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`uniquify`

         .. api-member::
            :name: :value:`overwrite`

         .. api-member::
            :name: :value:`prompt`

.. _downloads.InterruptReason:

InterruptReason
---------------

.. api-section-annotation-hack:: -- [Added in TB 47]

.. note::

   Only returns these errors: :code:`NETWORK_FAILED`, :code:`FILE_FAILED`, :code:`CRASH`, :code:`USER_CANCELED`, :code:`SERVER_BAD_CONTENT`, :code:`SERVER_FORBIDDEN`, :code:`SERVER_UNAUTHORIZED`, and :code:`SERVER_FAILED`.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`FILE_FAILED`

         .. api-member::
            :name: :value:`FILE_ACCESS_DENIED`

         .. api-member::
            :name: :value:`FILE_NO_SPACE`

         .. api-member::
            :name: :value:`FILE_NAME_TOO_LONG`

         .. api-member::
            :name: :value:`FILE_TOO_LARGE`

         .. api-member::
            :name: :value:`FILE_VIRUS_INFECTED`

         .. api-member::
            :name: :value:`FILE_TRANSIENT_ERROR`

         .. api-member::
            :name: :value:`FILE_BLOCKED`

         .. api-member::
            :name: :value:`FILE_SECURITY_CHECK_FAILED`

         .. api-member::
            :name: :value:`FILE_TOO_SHORT`

         .. api-member::
            :name: :value:`NETWORK_FAILED`

         .. api-member::
            :name: :value:`NETWORK_TIMEOUT`

         .. api-member::
            :name: :value:`NETWORK_DISCONNECTED`

         .. api-member::
            :name: :value:`NETWORK_SERVER_DOWN`

         .. api-member::
            :name: :value:`NETWORK_INVALID_REQUEST`

         .. api-member::
            :name: :value:`SERVER_FAILED`

         .. api-member::
            :name: :value:`SERVER_NO_RANGE`

         .. api-member::
            :name: :value:`SERVER_BAD_CONTENT`

         .. api-member::
            :name: :value:`SERVER_UNAUTHORIZED`

         .. api-member::
            :name: :value:`SERVER_CERT_PROBLEM`

         .. api-member::
            :name: :value:`SERVER_FORBIDDEN`

         .. api-member::
            :name: :value:`USER_CANCELED`

         .. api-member::
            :name: :value:`USER_SHUTDOWN`

         .. api-member::
            :name: :value:`CRASH`

.. _downloads.State:

State
-----

.. api-section-annotation-hack:: -- [Added in TB 47]

<dl><dt>in_progress</dt><dd>The download is currently receiving data from the server.</dd><dt>interrupted</dt><dd>An error broke the connection with the file host.</dd><dt>complete</dt><dd>The download completed successfully.</dd></dl>These string constants will never change, however the set of States may change.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`in_progress`

         .. api-member::
            :name: :value:`interrupted`

         .. api-member::
            :name: :value:`complete`

.. _downloads.StringDelta:

StringDelta
-----------

.. api-section-annotation-hack:: -- [Added in TB 47]

.. api-header::
   :label: object

   .. _downloads.StringDelta.current:

   .. api-member::
      :name: [``current``]
      :type: (string, optional)

   .. _downloads.StringDelta.previous:

   .. api-member::
      :name: [``previous``]
      :type: (string, optional)
