=====================
addressBooks.provider
=====================

The :ref:`addressBooks.provider_api` API first appeared in Thunderbird 90. It allows to add address books, which are not stored or cached by Thunderbird itself, but are handled completely by the extension. Address books created by the :ref:`addressBooks.provider_api` API will forward all access requests to the WebExtension. Possible use cases:

* implement a custom storage
* implement search-only address books querying a remote server

So far, only the API for search-only address books is implemented. 

.. warning::

  This API will change in future releases of Thunderbird.
