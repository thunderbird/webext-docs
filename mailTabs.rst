========
mailTabs
========

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
  - [``layout``] (string)
  - [``messagePaneVisible``] (boolean)

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

