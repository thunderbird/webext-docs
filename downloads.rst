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

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _downloads.permission.downloads:

.. api-member::
   :name: :permission:`downloads`
   :refid: downloads-permission-downloads
   :refname: downloads

   Download files and read and modify the browser’s download history.

.. _downloads.permission.downloads.open:

.. api-member::
   :name: :permission:`downloads.open`
   :refid: downloads-permission-downloads-open
   :refname: downloads.open

   Open files downloaded to your computer.

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

   .. _downloads.cancel.download^id:

   .. api-member::
      :name: ``downloadId``
      :refid: downloads-cancel-download-id
      :refname: downloadId
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

   .. _downloads.download.options:

   .. api-member::
      :name: ``options``
      :refid: downloads-download-options
      :refname: options
      :type: (object)

      What to download and how.

      .. _downloads.download.options.url:

      .. api-member::
         :name: ``url``
         :refid: downloads-download-options-url
         :refname: url
         :type: (string)

         The URL to download.

      .. _downloads.download.options.allow^http^errors:

      .. api-member::
         :name: [``allowHttpErrors``]
         :refid: downloads-download-options-allow-http-errors
         :refname: allowHttpErrors
         :type: (boolean, optional)

         When this flag is set to :code:`true`, then the browser will allow downloads to proceed after encountering HTTP errors such as :code:`404 Not Found`.

      .. _downloads.download.options.body:

      .. api-member::
         :name: [``body``]
         :refid: downloads-download-options-body
         :refname: body
         :type: (string, optional)

         Post body.

      .. _downloads.download.options.conflict^action:

      .. api-member::
         :name: [``conflictAction``]
         :refid: downloads-download-options-conflict-action
         :refname: conflictAction
         :type: (:ref:`downloads.^filename^conflict^action`, optional)

      .. _downloads.download.options.cookie^store^id:

      .. api-member::
         :name: [``cookieStoreId``]
         :refid: downloads-download-options-cookie-store-id
         :refname: cookieStoreId
         :type: (string, optional)

         The cookie store ID of the contextual identity; requires "cookies" permission.

      .. _downloads.download.options.filename:

      .. api-member::
         :name: [``filename``]
         :refid: downloads-download-options-filename
         :refname: filename
         :type: (string, optional)

         A file path relative to the Downloads directory to contain the downloaded file.

      .. _downloads.download.options.headers:

      .. api-member::
         :name: [``headers``]
         :refid: downloads-download-options-headers
         :refname: headers
         :type: (array of object, optional)

         Extra HTTP headers to send with the request if the URL uses the HTTP[s] protocol. Each header is represented as a dictionary containing the keys :code:`name` and either :code:`value` or :code:`binaryValue`, restricted to those allowed by XMLHttpRequest.

      .. _downloads.download.options.incognito:

      .. api-member::
         :name: [``incognito``]
         :refid: downloads-download-options-incognito
         :refname: incognito
         :type: (boolean, optional)

         Whether to associate the download with a private browsing session.

      .. _downloads.download.options.method:

      .. api-member::
         :name: [``method``]
         :refid: downloads-download-options-method
         :refname: method
         :type: (`string`, optional)

         The HTTP method to use if the URL uses the HTTP[S] protocol.

         Supported values:

         .. _downloads.download.options.method.^g^e^t:

         .. api-member::
            :name: :value:`GET`
            :refid: downloads-download-options-method-g-e-t
            :refname: GET

         .. _downloads.download.options.method.^p^o^s^t:

         .. api-member::
            :name: :value:`POST`
            :refid: downloads-download-options-method-p-o-s-t
            :refname: POST

      .. _downloads.download.options.save^as:

      .. api-member::
         :name: [``saveAs``]
         :refid: downloads-download-options-save-as
         :refname: saveAs
         :type: (boolean, optional)

         Use a file-chooser to allow the user to select a filename. If the option is not specified, the file chooser will be shown only if the Thunderbird "Always ask you where to save files" option is enabled (i.e. the pref :code:`browser.download.useDownloadDir` is set to :code:`false`).

.. api-header::
   :label: Return type (`Promise`_)

   .. _downloads.download.returns:

   .. api-member::
      :refid: downloads-download-returns
      :refname: _returns
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

   .. _downloads.drag.download^id:

   .. api-member::
      :name: ``downloadId``
      :refid: downloads-drag-download-id
      :refname: downloadId
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

   .. _downloads.erase.query:

   .. api-member::
      :name: ``query``
      :refid: downloads-erase-query
      :refname: query
      :type: (:ref:`downloads.^download^query`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _downloads.erase.returns:

   .. api-member::
      :refid: downloads-erase-returns
      :refname: _returns
      :type: array of integer

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.get^file^icon:

getFileIcon(downloadId, [options])
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 48]

Retrieve an icon for the specified download. For new downloads, file icons are available after the `onCreated <#event-onCreated>`__ event has been received. The image returned by this function while a download is in progress may be different from the image returned after the download is complete. Icon retrieval is done by querying the underlying operating system or toolkit depending on the platform. The icon that is returned will therefore depend on a number of factors including state of the download, platform, registered file types and visual theme. If a file icon cannot be determined, `chrome.extension.lastError <extension.html#property-lastError>`__ will contain an error message.

.. api-header::
   :label: Parameters

   .. _downloads.get^file^icon.download^id:

   .. api-member::
      :name: ``downloadId``
      :refid: downloads-get-file-icon-download-id
      :refname: downloadId
      :type: (integer)

      The identifier for the download.

   .. _downloads.get^file^icon.options:

   .. api-member::
      :name: [``options``]
      :refid: downloads-get-file-icon-options
      :refname: options
      :type: (object, optional)

      .. _downloads.get^file^icon.options.size:

      .. api-member::
         :name: [``size``]
         :refid: downloads-get-file-icon-options-size
         :refname: size
         :type: (integer, optional)

         The size of the icon.  The returned icon will be square with dimensions size * size pixels.  The default size for the icon is 32x32 pixels.

.. api-header::
   :label: Return type (`Promise`_)

   .. _downloads.get^file^icon.returns:

   .. api-member::
      :refid: downloads-get-file-icon-returns
      :refname: _returns
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

   .. _downloads.open.download^id:

   .. api-member::
      :name: ``downloadId``
      :refid: downloads-open-download-id
      :refname: downloadId
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

   .. _downloads.pause.download^id:

   .. api-member::
      :name: ``downloadId``
      :refid: downloads-pause-download-id
      :refname: downloadId
      :type: (integer)

      The id of the download to pause.

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.remove^file:

removeFile(downloadId)
----------------------

.. api-section-annotation-hack:: -- [Added in TB 48]

.. api-header::
   :label: Parameters

   .. _downloads.remove^file.download^id:

   .. api-member::
      :name: ``downloadId``
      :refid: downloads-remove-file-download-id
      :refname: downloadId
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

   .. _downloads.resume.download^id:

   .. api-member::
      :name: ``downloadId``
      :refid: downloads-resume-download-id
      :refname: downloadId
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

   .. _downloads.search.query:

   .. api-member::
      :name: ``query``
      :refid: downloads-search-query
      :refname: query
      :type: (:ref:`downloads.^download^query`)

.. api-header::
   :label: Return type (`Promise`_)

   .. _downloads.search.returns:

   .. api-member::
      :refid: downloads-search-returns
      :refname: _returns
      :type: array of :ref:`downloads.^download^item`

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

   .. _downloads.show.download^id:

   .. api-member::
      :name: ``downloadId``
      :refid: downloads-show-download-id
      :refname: downloadId
      :type: (integer)

.. api-header::
   :label: Return type (`Promise`_)

   .. _downloads.show.returns:

   .. api-member::
      :refid: downloads-show-returns
      :refname: _returns
      :type: boolean

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.show^default^folder:

showDefaultFolder()
-------------------

.. api-section-annotation-hack:: -- [Added in TB 48]

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. rst-class:: api-main-section

Events
======

.. _downloads.on^changed:

onChanged
---------

.. api-section-annotation-hack:: -- [Added in TB 47]

When any of a `DownloadItem <#type-DownloadItem>`__'s properties except :code:`bytesReceived` changes, this event fires with the :code:`downloadId` and an object containing the properties that changed.

.. api-header::
   :label: Parameters for onChanged.addListener(listener)

   .. _downloads.on^changed.listener(download^delta):

   .. api-member::
      :name: ``listener(downloadDelta)``
      :refid: downloads-on-changed-listener-download-delta
      :refname: listener(downloadDelta)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _downloads.on^changed.download^delta:

   .. api-member::
      :name: ``downloadDelta``
      :refid: downloads-on-changed-download-delta
      :refname: downloadDelta
      :type: (object)

      .. _downloads.on^changed.download^delta.id:

      .. api-member::
         :name: ``id``
         :refid: downloads-on-changed-download-delta-id
         :refname: id
         :type: (integer)

         The :code:`id` of the `DownloadItem <#type-DownloadItem>`__ that changed.

      .. _downloads.on^changed.download^delta.can^resume:

      .. api-member::
         :name: [``canResume``]
         :refid: downloads-on-changed-download-delta-can-resume
         :refname: canResume
         :type: (:ref:`downloads.^boolean^delta`, optional)

      .. _downloads.on^changed.download^delta.danger:

      .. api-member::
         :name: [``danger``]
         :refid: downloads-on-changed-download-delta-danger
         :refname: danger
         :type: (:ref:`downloads.^string^delta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`danger`.

      .. _downloads.on^changed.download^delta.end^time:

      .. api-member::
         :name: [``endTime``]
         :refid: downloads-on-changed-download-delta-end-time
         :refname: endTime
         :type: (:ref:`downloads.^string^delta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`endTime`.

      .. _downloads.on^changed.download^delta.error:

      .. api-member::
         :name: [``error``]
         :refid: downloads-on-changed-download-delta-error
         :refname: error
         :type: (:ref:`downloads.^string^delta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`error`.

      .. _downloads.on^changed.download^delta.exists:

      .. api-member::
         :name: [``exists``]
         :refid: downloads-on-changed-download-delta-exists
         :refname: exists
         :type: (:ref:`downloads.^boolean^delta`, optional)

      .. _downloads.on^changed.download^delta.filename:

      .. api-member::
         :name: [``filename``]
         :refid: downloads-on-changed-download-delta-filename
         :refname: filename
         :type: (:ref:`downloads.^string^delta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`filename`.

      .. _downloads.on^changed.download^delta.file^size:

      .. api-member::
         :name: [``fileSize``]
         :refid: downloads-on-changed-download-delta-file-size
         :refname: fileSize
         :type: (:ref:`downloads.^double^delta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`fileSize`.

      .. _downloads.on^changed.download^delta.mime:

      .. api-member::
         :name: [``mime``]
         :refid: downloads-on-changed-download-delta-mime
         :refname: mime
         :type: (:ref:`downloads.^string^delta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`mime`.

      .. _downloads.on^changed.download^delta.paused:

      .. api-member::
         :name: [``paused``]
         :refid: downloads-on-changed-download-delta-paused
         :refname: paused
         :type: (:ref:`downloads.^boolean^delta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`paused`.

      .. _downloads.on^changed.download^delta.start^time:

      .. api-member::
         :name: [``startTime``]
         :refid: downloads-on-changed-download-delta-start-time
         :refname: startTime
         :type: (:ref:`downloads.^string^delta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`startTime`.

      .. _downloads.on^changed.download^delta.state:

      .. api-member::
         :name: [``state``]
         :refid: downloads-on-changed-download-delta-state
         :refname: state
         :type: (:ref:`downloads.^string^delta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`state`.

      .. _downloads.on^changed.download^delta.total^bytes:

      .. api-member::
         :name: [``totalBytes``]
         :refid: downloads-on-changed-download-delta-total-bytes
         :refname: totalBytes
         :type: (:ref:`downloads.^double^delta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`totalBytes`.

      .. _downloads.on^changed.download^delta.url:

      .. api-member::
         :name: [``url``]
         :refid: downloads-on-changed-download-delta-url
         :refname: url
         :type: (:ref:`downloads.^string^delta`, optional)

         Describes a change in a `DownloadItem <#type-DownloadItem>`__'s :code:`url`.

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 48]

This event fires with the `DownloadItem <#type-DownloadItem>`__ object when a download begins.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _downloads.on^created.listener(download^item):

   .. api-member::
      :name: ``listener(downloadItem)``
      :refid: downloads-on-created-listener-download-item
      :refname: listener(downloadItem)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _downloads.on^created.download^item:

   .. api-member::
      :name: ``downloadItem``
      :refid: downloads-on-created-download-item
      :refname: downloadItem
      :type: (:ref:`downloads.^download^item`)

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. _downloads.on^erased:

onErased
--------

.. api-section-annotation-hack:: -- [Added in TB 48]

Fires with the :code:`downloadId` when a download is erased from history.

.. api-header::
   :label: Parameters for onErased.addListener(listener)

   .. _downloads.on^erased.listener(download^id):

   .. api-member::
      :name: ``listener(downloadId)``
      :refid: downloads-on-erased-listener-download-id
      :refname: listener(downloadId)

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _downloads.on^erased.download^id:

   .. api-member::
      :name: ``downloadId``
      :refid: downloads-on-erased-download-id
      :refname: downloadId
      :type: (integer)

      The :code:`id` of the `DownloadItem <#type-DownloadItem>`__ that was erased.

.. api-header::
   :label: Required permissions

   - :permission:`downloads`

.. rst-class:: api-main-section

Types
=====

.. _downloads.^boolean^delta:

BooleanDelta
------------

.. api-section-annotation-hack:: -- [Added in TB 47]

.. api-header::
   :label: object

   .. _downloads.^boolean^delta.current:

   .. api-member::
      :name: [``current``]
      :refid: downloads-boolean-delta-current
      :refname: current
      :type: (boolean, optional)

   .. _downloads.^boolean^delta.previous:

   .. api-member::
      :name: [``previous``]
      :refid: downloads-boolean-delta-previous
      :refname: previous
      :type: (boolean, optional)

.. _downloads.^danger^type:

DangerType
----------

.. api-section-annotation-hack:: -- [Added in TB 47]

These string constants will never change, however the set of DangerTypes may change.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _downloads.^danger^type.accepted:

         .. api-member::
            :name: :value:`accepted`
            :refid: downloads-danger-type-accepted
            :refname: accepted

         .. _downloads.^danger^type.content:

         .. api-member::
            :name: :value:`content`
            :refid: downloads-danger-type-content
            :refname: content

            The downloaded file is known to be malicious.

         .. _downloads.^danger^type.file:

         .. api-member::
            :name: :value:`file`
            :refid: downloads-danger-type-file
            :refname: file

            The download's filename is suspicious.

         .. _downloads.^danger^type.host:

         .. api-member::
            :name: :value:`host`
            :refid: downloads-danger-type-host
            :refname: host

         .. _downloads.^danger^type.safe:

         .. api-member::
            :name: :value:`safe`
            :refid: downloads-danger-type-safe
            :refname: safe

            The download presents no known danger to the user's computer.

         .. _downloads.^danger^type.uncommon:

         .. api-member::
            :name: :value:`uncommon`
            :refid: downloads-danger-type-uncommon
            :refname: uncommon

            The download's URL is not commonly downloaded and could be dangerous.

         .. _downloads.^danger^type.unwanted:

         .. api-member::
            :name: :value:`unwanted`
            :refid: downloads-danger-type-unwanted
            :refname: unwanted

         .. _downloads.^danger^type.url:

         .. api-member::
            :name: :value:`url`
            :refid: downloads-danger-type-url
            :refname: url

            The download's URL is known to be malicious.

.. _downloads.^double^delta:

DoubleDelta
-----------

.. api-section-annotation-hack:: -- [Added in TB 47]

.. api-header::
   :label: object

   .. _downloads.^double^delta.current:

   .. api-member::
      :name: [``current``]
      :refid: downloads-double-delta-current
      :refname: current
      :type: (number, optional)

   .. _downloads.^double^delta.previous:

   .. api-member::
      :name: [``previous``]
      :refid: downloads-double-delta-previous
      :refname: previous
      :type: (number, optional)

.. _downloads.^download^item:

DownloadItem
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   .. _downloads.^download^item.bytes^received:

   .. api-member::
      :name: ``bytesReceived``
      :refid: downloads-download-item-bytes-received
      :refname: bytesReceived
      :type: (number)

      Number of bytes received so far from the host, without considering file compression.

   .. _downloads.^download^item.can^resume:

   .. api-member::
      :name: ``canResume``
      :refid: downloads-download-item-can-resume
      :refname: canResume
      :type: (boolean)

   .. _downloads.^download^item.danger:

   .. api-member::
      :name: ``danger``
      :refid: downloads-download-item-danger
      :refname: danger
      :type: (:ref:`downloads.^danger^type`)

      Indication of whether this download is thought to be safe or known to be suspicious.

      .. note::

         Always given as 'safe'.

   .. _downloads.^download^item.exists:

   .. api-member::
      :name: ``exists``
      :refid: downloads-download-item-exists
      :refname: exists
      :type: (boolean)

   .. _downloads.^download^item.filename:

   .. api-member::
      :name: ``filename``
      :refid: downloads-download-item-filename
      :refname: filename
      :type: (string)

      Absolute local path.

   .. _downloads.^download^item.file^size:

   .. api-member::
      :name: ``fileSize``
      :refid: downloads-download-item-file-size
      :refname: fileSize
      :type: (number)

      Number of bytes in the whole file post-decompression, or -1 if unknown.

   .. _downloads.^download^item.id:

   .. api-member::
      :name: ``id``
      :refid: downloads-download-item-id
      :refname: id
      :type: (integer)

      An identifier that is persistent across browser sessions.

   .. _downloads.^download^item.incognito:

   .. api-member::
      :name: ``incognito``
      :refid: downloads-download-item-incognito
      :refname: incognito
      :type: (boolean)

      False if this download is recorded in the history, true if it is not recorded.

   .. _downloads.^download^item.paused:

   .. api-member::
      :name: ``paused``
      :refid: downloads-download-item-paused
      :refname: paused
      :type: (boolean)

      True if the download has stopped reading data from the host, but kept the connection open.

   .. _downloads.^download^item.start^time:

   .. api-member::
      :name: ``startTime``
      :refid: downloads-download-item-start-time
      :refname: startTime
      :type: (string)

      Number of milliseconds between the unix epoch and when this download began.

   .. _downloads.^download^item.state:

   .. api-member::
      :name: ``state``
      :refid: downloads-download-item-state
      :refname: state
      :type: (:ref:`downloads.^state`)

      Indicates whether the download is progressing, interrupted, or complete.

   .. _downloads.^download^item.total^bytes:

   .. api-member::
      :name: ``totalBytes``
      :refid: downloads-download-item-total-bytes
      :refname: totalBytes
      :type: (number)

      Number of bytes in the whole file, without considering file compression, or -1 if unknown.

   .. _downloads.^download^item.url:

   .. api-member::
      :name: ``url``
      :refid: downloads-download-item-url
      :refname: url
      :type: (string)

      Absolute URL.

   .. _downloads.^download^item.by^extension^id:

   .. api-member::
      :name: [``byExtensionId``]
      :refid: downloads-download-item-by-extension-id
      :refname: byExtensionId
      :type: (string, optional)

   .. _downloads.^download^item.by^extension^name:

   .. api-member::
      :name: [``byExtensionName``]
      :refid: downloads-download-item-by-extension-name
      :refname: byExtensionName
      :type: (string, optional)

   .. _downloads.^download^item.cookie^store^id:

   .. api-member::
      :name: [``cookieStoreId``]
      :refid: downloads-download-item-cookie-store-id
      :refname: cookieStoreId
      :type: (string, optional)
      :annotation: -- [Added in TB 92]

      The cookie store ID of the contextual identity.

   .. _downloads.^download^item.end^time:

   .. api-member::
      :name: [``endTime``]
      :refid: downloads-download-item-end-time
      :refname: endTime
      :type: (string, optional)

      Number of milliseconds between the unix epoch and when this download ended.

   .. _downloads.^download^item.error:

   .. api-member::
      :name: [``error``]
      :refid: downloads-download-item-error
      :refname: error
      :type: (:ref:`downloads.^interrupt^reason`, optional)

      Number indicating why a download was interrupted.

   .. _downloads.^download^item.estimated^end^time:

   .. api-member::
      :name: [``estimatedEndTime``]
      :refid: downloads-download-item-estimated-end-time
      :refname: estimatedEndTime
      :type: (string, optional)
      :annotation: -- [Added in TB 57]

   .. _downloads.^download^item.mime:

   .. api-member::
      :name: [``mime``]
      :refid: downloads-download-item-mime
      :refname: mime
      :type: (string, optional)

      The file's MIME type.

   .. _downloads.^download^item.referrer:

   .. api-member::
      :name: [``referrer``]
      :refid: downloads-download-item-referrer
      :refname: referrer
      :type: (string, optional)

.. _downloads.^download^query:

DownloadQuery
-------------

.. api-section-annotation-hack:: -- [Added in TB 47]

Parameters that combine to specify a predicate that can be used to select a set of downloads.  Used for example in search() and erase()

.. api-header::
   :label: object

   .. _downloads.^download^query.bytes^received:

   .. api-member::
      :name: [``bytesReceived``]
      :refid: downloads-download-query-bytes-received
      :refname: bytesReceived
      :type: (number, optional)

      Number of bytes received so far from the host, without considering file compression.

   .. _downloads.^download^query.cookie^store^id:

   .. api-member::
      :name: [``cookieStoreId``]
      :refid: downloads-download-query-cookie-store-id
      :refname: cookieStoreId
      :type: (string, optional)
      :annotation: -- [Added in TB 92]

      The cookie store ID of the contextual identity.

   .. _downloads.^download^query.danger:

   .. api-member::
      :name: [``danger``]
      :refid: downloads-download-query-danger
      :refname: danger
      :type: (:ref:`downloads.^danger^type`, optional)

      Indication of whether this download is thought to be safe or known to be suspicious.

   .. _downloads.^download^query.ended^after:

   .. api-member::
      :name: [``endedAfter``]
      :refid: downloads-download-query-ended-after
      :refname: endedAfter
      :type: (:ref:`downloads.^download^time`, optional)

      Limits results to downloads that ended after the given ms since the epoch.

      .. note::

         The parameter is ignored.

   .. _downloads.^download^query.ended^before:

   .. api-member::
      :name: [``endedBefore``]
      :refid: downloads-download-query-ended-before
      :refname: endedBefore
      :type: (:ref:`downloads.^download^time`, optional)

      Limits results to downloads that ended before the given ms since the epoch.

      .. note::

         The parameter is ignored.

   .. _downloads.^download^query.end^time:

   .. api-member::
      :name: [``endTime``]
      :refid: downloads-download-query-end-time
      :refname: endTime
      :type: (string, optional)

   .. _downloads.^download^query.error:

   .. api-member::
      :name: [``error``]
      :refid: downloads-download-query-error
      :refname: error
      :type: (:ref:`downloads.^interrupt^reason`, optional)

      Why a download was interrupted.

   .. _downloads.^download^query.exists:

   .. api-member::
      :name: [``exists``]
      :refid: downloads-download-query-exists
      :refname: exists
      :type: (boolean, optional)

   .. _downloads.^download^query.filename:

   .. api-member::
      :name: [``filename``]
      :refid: downloads-download-query-filename
      :refname: filename
      :type: (string, optional)

      Absolute local path.

   .. _downloads.^download^query.filename^regex:

   .. api-member::
      :name: [``filenameRegex``]
      :refid: downloads-download-query-filename-regex
      :refname: filenameRegex
      :type: (string, optional)

      Limits results to `DownloadItems <#type-DownloadItem>`__ whose :code:`filename` matches the given regular expression.

   .. _downloads.^download^query.file^size:

   .. api-member::
      :name: [``fileSize``]
      :refid: downloads-download-query-file-size
      :refname: fileSize
      :type: (number, optional)

      Number of bytes in the whole file post-decompression, or -1 if unknown.

   .. _downloads.^download^query.id:

   .. api-member::
      :name: [``id``]
      :refid: downloads-download-query-id
      :refname: id
      :type: (integer, optional)

   .. _downloads.^download^query.limit:

   .. api-member::
      :name: [``limit``]
      :refid: downloads-download-query-limit
      :refname: limit
      :type: (integer, optional)

      Setting this integer limits the number of results. Otherwise, all matching `DownloadItems <#type-DownloadItem>`__ will be returned.

   .. _downloads.^download^query.mime:

   .. api-member::
      :name: [``mime``]
      :refid: downloads-download-query-mime
      :refname: mime
      :type: (string, optional)

      The file's MIME type.

   .. _downloads.^download^query.order^by:

   .. api-member::
      :name: [``orderBy``]
      :refid: downloads-download-query-order-by
      :refname: orderBy
      :type: (array of string, optional)

      Setting elements of this array to `DownloadItem <#type-DownloadItem>`__ properties in order to sort the search results. For example, setting :code:`orderBy='startTime'` sorts the `DownloadItems <#type-DownloadItem>`__ by their start time in ascending order. To specify descending order, prefix :code:`orderBy` with a hyphen: '-startTime'.

   .. _downloads.^download^query.paused:

   .. api-member::
      :name: [``paused``]
      :refid: downloads-download-query-paused
      :refname: paused
      :type: (boolean, optional)

      True if the download has stopped reading data from the host, but kept the connection open.

   .. _downloads.^download^query.query:

   .. api-member::
      :name: [``query``]
      :refid: downloads-download-query-query
      :refname: query
      :type: (array of string, optional)

      This array of search terms limits results to `DownloadItems <#type-DownloadItem>`__ whose :code:`filename` or :code:`url` contain all of the search terms that do not begin with a dash '-' and none of the search terms that do begin with a dash.

   .. _downloads.^download^query.started^after:

   .. api-member::
      :name: [``startedAfter``]
      :refid: downloads-download-query-started-after
      :refname: startedAfter
      :type: (:ref:`downloads.^download^time`, optional)

      Limits results to downloads that started after the given ms since the epoch.

   .. _downloads.^download^query.started^before:

   .. api-member::
      :name: [``startedBefore``]
      :refid: downloads-download-query-started-before
      :refname: startedBefore
      :type: (:ref:`downloads.^download^time`, optional)

      Limits results to downloads that started before the given ms since the epoch.

   .. _downloads.^download^query.start^time:

   .. api-member::
      :name: [``startTime``]
      :refid: downloads-download-query-start-time
      :refname: startTime
      :type: (string, optional)

   .. _downloads.^download^query.state:

   .. api-member::
      :name: [``state``]
      :refid: downloads-download-query-state
      :refname: state
      :type: (:ref:`downloads.^state`, optional)

      Indicates whether the download is progressing, interrupted, or complete.

   .. _downloads.^download^query.total^bytes:

   .. api-member::
      :name: [``totalBytes``]
      :refid: downloads-download-query-total-bytes
      :refname: totalBytes
      :type: (number, optional)

      Number of bytes in the whole file, without considering file compression, or -1 if unknown.

   .. _downloads.^download^query.total^bytes^greater:

   .. api-member::
      :name: [``totalBytesGreater``]
      :refid: downloads-download-query-total-bytes-greater
      :refname: totalBytesGreater
      :type: (number, optional)

      Limits results to downloads whose totalBytes is greater than the given integer.

   .. _downloads.^download^query.total^bytes^less:

   .. api-member::
      :name: [``totalBytesLess``]
      :refid: downloads-download-query-total-bytes-less
      :refname: totalBytesLess
      :type: (number, optional)

      Limits results to downloads whose totalBytes is less than the given integer.

   .. _downloads.^download^query.url:

   .. api-member::
      :name: [``url``]
      :refid: downloads-download-query-url
      :refname: url
      :type: (string, optional)

      Absolute URL.

   .. _downloads.^download^query.url^regex:

   .. api-member::
      :name: [``urlRegex``]
      :refid: downloads-download-query-url-regex
      :refname: urlRegex
      :type: (string, optional)

      Limits results to `DownloadItems <#type-DownloadItem>`__ whose :code:`url` matches the given regular expression.

.. _downloads.^download^time:

DownloadTime
------------

.. api-section-annotation-hack:: -- [Added in TB 47]

A time specified as a Date object, a number or string representing milliseconds since the epoch, or an ISO 8601 string

.. api-header::
   :label: string

*or*

.. api-header::
   :label: `Date <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date>`__

.. _downloads.^filename^conflict^action:

FilenameConflictAction
----------------------

.. api-section-annotation-hack:: -- [Added in TB 47]

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _downloads.^filename^conflict^action.overwrite:

         .. api-member::
            :name: :value:`overwrite`
            :refid: downloads-filename-conflict-action-overwrite
            :refname: overwrite

         .. _downloads.^filename^conflict^action.prompt:

         .. api-member::
            :name: :value:`prompt`
            :refid: downloads-filename-conflict-action-prompt
            :refname: prompt

         .. _downloads.^filename^conflict^action.uniquify:

         .. api-member::
            :name: :value:`uniquify`
            :refid: downloads-filename-conflict-action-uniquify
            :refname: uniquify

.. _downloads.^interrupt^reason:

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

         .. _downloads.^interrupt^reason.^c^r^a^s^h:

         .. api-member::
            :name: :value:`CRASH`
            :refid: downloads-interrupt-reason-c-r-a-s-h
            :refname: CRASH

         .. _downloads.^interrupt^reason.^f^i^l^e_^a^c^c^e^s^s_^d^e^n^i^e^d:

         .. api-member::
            :name: :value:`FILE_ACCESS_DENIED`
            :refid: downloads-interrupt-reason-f-i-l-e-a-c-c-e-s-s-d-e-n-i-e-d
            :refname: FILE_ACCESS_DENIED

         .. _downloads.^interrupt^reason.^f^i^l^e_^b^l^o^c^k^e^d:

         .. api-member::
            :name: :value:`FILE_BLOCKED`
            :refid: downloads-interrupt-reason-f-i-l-e-b-l-o-c-k-e-d
            :refname: FILE_BLOCKED

         .. _downloads.^interrupt^reason.^f^i^l^e_^f^a^i^l^e^d:

         .. api-member::
            :name: :value:`FILE_FAILED`
            :refid: downloads-interrupt-reason-f-i-l-e-f-a-i-l-e-d
            :refname: FILE_FAILED

         .. _downloads.^interrupt^reason.^f^i^l^e_^n^a^m^e_^t^o^o_^l^o^n^g:

         .. api-member::
            :name: :value:`FILE_NAME_TOO_LONG`
            :refid: downloads-interrupt-reason-f-i-l-e-n-a-m-e-t-o-o-l-o-n-g
            :refname: FILE_NAME_TOO_LONG

         .. _downloads.^interrupt^reason.^f^i^l^e_^n^o_^s^p^a^c^e:

         .. api-member::
            :name: :value:`FILE_NO_SPACE`
            :refid: downloads-interrupt-reason-f-i-l-e-n-o-s-p-a-c-e
            :refname: FILE_NO_SPACE

         .. _downloads.^interrupt^reason.^f^i^l^e_^s^e^c^u^r^i^t^y_^c^h^e^c^k_^f^a^i^l^e^d:

         .. api-member::
            :name: :value:`FILE_SECURITY_CHECK_FAILED`
            :refid: downloads-interrupt-reason-f-i-l-e-s-e-c-u-r-i-t-y-c-h-e-c-k-f-a-i-l-e-d
            :refname: FILE_SECURITY_CHECK_FAILED

         .. _downloads.^interrupt^reason.^f^i^l^e_^t^o^o_^l^a^r^g^e:

         .. api-member::
            :name: :value:`FILE_TOO_LARGE`
            :refid: downloads-interrupt-reason-f-i-l-e-t-o-o-l-a-r-g-e
            :refname: FILE_TOO_LARGE

         .. _downloads.^interrupt^reason.^f^i^l^e_^t^o^o_^s^h^o^r^t:

         .. api-member::
            :name: :value:`FILE_TOO_SHORT`
            :refid: downloads-interrupt-reason-f-i-l-e-t-o-o-s-h-o-r-t
            :refname: FILE_TOO_SHORT

         .. _downloads.^interrupt^reason.^f^i^l^e_^t^r^a^n^s^i^e^n^t_^e^r^r^o^r:

         .. api-member::
            :name: :value:`FILE_TRANSIENT_ERROR`
            :refid: downloads-interrupt-reason-f-i-l-e-t-r-a-n-s-i-e-n-t-e-r-r-o-r
            :refname: FILE_TRANSIENT_ERROR

         .. _downloads.^interrupt^reason.^f^i^l^e_^v^i^r^u^s_^i^n^f^e^c^t^e^d:

         .. api-member::
            :name: :value:`FILE_VIRUS_INFECTED`
            :refid: downloads-interrupt-reason-f-i-l-e-v-i-r-u-s-i-n-f-e-c-t-e-d
            :refname: FILE_VIRUS_INFECTED

         .. _downloads.^interrupt^reason.^n^e^t^w^o^r^k_^d^i^s^c^o^n^n^e^c^t^e^d:

         .. api-member::
            :name: :value:`NETWORK_DISCONNECTED`
            :refid: downloads-interrupt-reason-n-e-t-w-o-r-k-d-i-s-c-o-n-n-e-c-t-e-d
            :refname: NETWORK_DISCONNECTED

         .. _downloads.^interrupt^reason.^n^e^t^w^o^r^k_^f^a^i^l^e^d:

         .. api-member::
            :name: :value:`NETWORK_FAILED`
            :refid: downloads-interrupt-reason-n-e-t-w-o-r-k-f-a-i-l-e-d
            :refname: NETWORK_FAILED

         .. _downloads.^interrupt^reason.^n^e^t^w^o^r^k_^i^n^v^a^l^i^d_^r^e^q^u^e^s^t:

         .. api-member::
            :name: :value:`NETWORK_INVALID_REQUEST`
            :refid: downloads-interrupt-reason-n-e-t-w-o-r-k-i-n-v-a-l-i-d-r-e-q-u-e-s-t
            :refname: NETWORK_INVALID_REQUEST

         .. _downloads.^interrupt^reason.^n^e^t^w^o^r^k_^s^e^r^v^e^r_^d^o^w^n:

         .. api-member::
            :name: :value:`NETWORK_SERVER_DOWN`
            :refid: downloads-interrupt-reason-n-e-t-w-o-r-k-s-e-r-v-e-r-d-o-w-n
            :refname: NETWORK_SERVER_DOWN

         .. _downloads.^interrupt^reason.^n^e^t^w^o^r^k_^t^i^m^e^o^u^t:

         .. api-member::
            :name: :value:`NETWORK_TIMEOUT`
            :refid: downloads-interrupt-reason-n-e-t-w-o-r-k-t-i-m-e-o-u-t
            :refname: NETWORK_TIMEOUT

         .. _downloads.^interrupt^reason.^s^e^r^v^e^r_^b^a^d_^c^o^n^t^e^n^t:

         .. api-member::
            :name: :value:`SERVER_BAD_CONTENT`
            :refid: downloads-interrupt-reason-s-e-r-v-e-r-b-a-d-c-o-n-t-e-n-t
            :refname: SERVER_BAD_CONTENT

         .. _downloads.^interrupt^reason.^s^e^r^v^e^r_^c^e^r^t_^p^r^o^b^l^e^m:

         .. api-member::
            :name: :value:`SERVER_CERT_PROBLEM`
            :refid: downloads-interrupt-reason-s-e-r-v-e-r-c-e-r-t-p-r-o-b-l-e-m
            :refname: SERVER_CERT_PROBLEM

         .. _downloads.^interrupt^reason.^s^e^r^v^e^r_^f^a^i^l^e^d:

         .. api-member::
            :name: :value:`SERVER_FAILED`
            :refid: downloads-interrupt-reason-s-e-r-v-e-r-f-a-i-l-e-d
            :refname: SERVER_FAILED

         .. _downloads.^interrupt^reason.^s^e^r^v^e^r_^f^o^r^b^i^d^d^e^n:

         .. api-member::
            :name: :value:`SERVER_FORBIDDEN`
            :refid: downloads-interrupt-reason-s-e-r-v-e-r-f-o-r-b-i-d-d-e-n
            :refname: SERVER_FORBIDDEN

         .. _downloads.^interrupt^reason.^s^e^r^v^e^r_^n^o_^r^a^n^g^e:

         .. api-member::
            :name: :value:`SERVER_NO_RANGE`
            :refid: downloads-interrupt-reason-s-e-r-v-e-r-n-o-r-a-n-g-e
            :refname: SERVER_NO_RANGE

         .. _downloads.^interrupt^reason.^s^e^r^v^e^r_^u^n^a^u^t^h^o^r^i^z^e^d:

         .. api-member::
            :name: :value:`SERVER_UNAUTHORIZED`
            :refid: downloads-interrupt-reason-s-e-r-v-e-r-u-n-a-u-t-h-o-r-i-z-e-d
            :refname: SERVER_UNAUTHORIZED

         .. _downloads.^interrupt^reason.^u^s^e^r_^c^a^n^c^e^l^e^d:

         .. api-member::
            :name: :value:`USER_CANCELED`
            :refid: downloads-interrupt-reason-u-s-e-r-c-a-n-c-e-l-e-d
            :refname: USER_CANCELED

         .. _downloads.^interrupt^reason.^u^s^e^r_^s^h^u^t^d^o^w^n:

         .. api-member::
            :name: :value:`USER_SHUTDOWN`
            :refid: downloads-interrupt-reason-u-s-e-r-s-h-u-t-d-o-w-n
            :refname: USER_SHUTDOWN

.. _downloads.^state:

State
-----

.. api-section-annotation-hack:: -- [Added in TB 47]

These string constants will never change, however the set of States may change.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _downloads.^state.complete:

         .. api-member::
            :name: :value:`complete`
            :refid: downloads-state-complete
            :refname: complete

            The download completed successfully.

         .. _downloads.^state.in_progress:

         .. api-member::
            :name: :value:`in_progress`
            :refid: downloads-state-in-progress
            :refname: in_progress

            The download is currently receiving data from the server.

         .. _downloads.^state.interrupted:

         .. api-member::
            :name: :value:`interrupted`
            :refid: downloads-state-interrupted
            :refname: interrupted

            An error broke the connection with the file host.

.. _downloads.^string^delta:

StringDelta
-----------

.. api-section-annotation-hack:: -- [Added in TB 47]

.. api-header::
   :label: object

   .. _downloads.^string^delta.current:

   .. api-member::
      :name: [``current``]
      :refid: downloads-string-delta-current
      :refname: current
      :type: (string, optional)

   .. _downloads.^string^delta.previous:

   .. api-member::
      :name: [``previous``]
      :refid: downloads-string-delta-previous
      :refname: previous
      :type: (string, optional)
