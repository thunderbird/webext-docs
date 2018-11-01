========
mailTabs
========
The permission ``mailTabs`` is required to use ``mailTabs``.

Functions
=========

getAll()
--------

getCurrent()
------------

update([tabId], properties)
---------------------------

- [``tabId``] (integer)
- ``properties`` (object)

  - [``displayedFolder``] (object)
  - [``folderPaneVisible``] (boolean)
  - [``layout``] (string [enum_layout]_)
  - [``messagePaneVisible``] (boolean)
  - [``sortOrder``] (string [enum_sortOrder]_)
  - [``sortType``] (string [enum_sortType]_)

.. [enum_layout]:
Values for layout:

- ``standard``
- ``wide``
- ``vertical``

.. [enum_sortOrder]:
Values for sortOrder:

- ``none``
- ``ascending``
- ``descending``

.. [enum_sortType]:
Values for sortType:

- ``byNone``
- ``byDate``
- ``bySubject``
- ``byAuthor``
- ``byId``
- ``byThread``
- ``byPriority``
- ``byStatus``
- ``bySize``
- ``byFlagged``
- ``byUnread``
- ``byRecipient``
- ``byLocation``
- ``byTags``
- ``byJunkStatus``
- ``byAttachments``
- ``byAccount``
- ``byCustom``
- ``byReceived``
- ``byCorrespondent``

getSelectedMessages([tabId])
----------------------------

- [``tabId``] (integer)

setQuickFilter(properties)
--------------------------

- ``properties`` (object)

  - [``addrBook``] (boolean)
  - [``attachment``] (boolean)
  - [``recipients``] (boolean)
  - [``sender``] (boolean)
  - [``show``] (boolean)
  - [``starred``] (boolean)
  - [``subject``] (boolean)
  - [``tags``] (boolean)
  - [``text``] (string)
  - [``unread``] (boolean)

