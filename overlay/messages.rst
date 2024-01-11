  ≡ Related information
  
  * :doc:`/examples/messageLists`
  * :doc:`/examples/eventListeners`

============
messages API
============

The messages API first appeared in Thunderbird 66.

.. note::

  When the term ``messageId`` is used in these documents, it *doesn't* refer to the Message-ID
  email header. It is an internal tracking number that does not remain after a restart. Nor does
  it follow an email that has been moved to a different folder.

.. warning::

  Some functions in this API potentially return *a lot* of messages. Be careful what you wish for!
  See :doc:`examples/messageLists` for more information.
