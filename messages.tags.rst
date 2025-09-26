.. container:: sticky-sidebar

  ≡ messages.tags API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

=================
messages.tags API
=================

.. role:: permission

.. role:: value

.. role:: code

The messages.tags API allows to manage the user's message tags.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API: depending on which permissions are requested, certain functions may be unavailable or some data may be omitted from responses.

.. api-member::
   :name: :permission:`accountsRead`

   See your mail accounts, their identities and their folders

.. api-member::
   :name: :permission:`messagesTags`

   Create, modify and delete message tags

.. api-member::
   :name: :permission:`messagesTagsList`

   List message tags

.. rst-class:: api-main-section

Functions
=========

.. _messages.tags.create:

create([key], tag, color, [callback])
-------------------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Creates a new message tag and returns the associated key. Tagging a message will store the tag's key in the user's message. Throws if the specified tag key is used already.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``key``]
      :type: (string, optional)

      Unique tag identifier (will be converted to lower case). Must not include :value:`()<>{/%*"` or spaces. Will be auto-generated if not provided.

   .. api-member::
      :name: ``tag``
      :type: (string)

      Human-readable tag name.

   .. api-member::
      :name: ``color``
      :type: (string)

      Tag color in hex format (i.e.: :value:`#000080` for navy blue).

   .. api-member::
      :name: [``callback``]
      :type: (function, optional)
      :annotation: -- [Added in TB 136]

.. api-header::
   :label: Required permissions

   - :permission:`messagesTags`

.. _messages.tags.delete:

delete(key)
-----------

.. api-section-annotation-hack:: -- [Added in TB 121]

Deletes a message tag, removing it from the list of known tags. Its key will not be removed from tagged messages, but they will appear untagged. Recreating a deleted tag, will make all former tagged messages appear tagged again.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``key``
      :type: (string)

      Unique tag identifier (will be converted to lower case). Must not include :value:`()<>{/%*"` or spaces.

.. api-header::
   :label: Required permissions

   - :permission:`messagesTags`

.. _messages.tags.list:

list()
------

.. api-section-annotation-hack:: -- [Added in TB 121]

Returns a list of tags that can be set on messages, and their human-friendly name, colour, and sort order.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`MessageTag`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesTagsList`

.. _messages.tags.update:

update(key, updateProperties)
-----------------------------

.. api-section-annotation-hack:: -- [Added in TB 121]

Updates a message tag. Throws if the specified tag key does not exist.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``key``
      :type: (string)

      Unique tag identifier (will be converted to lower case). Must not include :value:`()<>{/%*"` or spaces.

   .. api-member::
      :name: ``updateProperties``
      :type: (:ref:`MessageTagProperties`)

.. api-header::
   :label: Required permissions

   - :permission:`messagesTags`

.. rst-class:: api-main-section

Events
======

.. _messages.tags.onCreated:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 136]

Fired when a new message tag has been created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. api-member::
      :name: ``listener(tag)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``tag``
      :type: (:ref:`MessageTag`)

.. api-header::
   :label: Required permissions

   - :permission:`messagesTagsList`

.. _messages.tags.onDeleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 136]

Fired when a message tag has been deleted.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. api-member::
      :name: ``listener(key)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``key``
      :type: (string)

      Unique tag identifier of the deleted message tag.

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _messages.tags.onUpdated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 136]

Fired when one or more properties of a message tag have been updated.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. api-member::
      :name: ``listener(key, changedProperties, oldProperties)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``key``
      :type: (string)

      Unique tag identifier of the updated message tag.

   .. api-member::
      :name: ``changedProperties``
      :type: (:ref:`MessageTagProperties`)

      The changed message tag properties.

   .. api-member::
      :name: ``oldProperties``
      :type: (:ref:`MessageTagProperties`)

      The old values of the changed message tag properties.

.. api-header::
   :label: Required permissions

   - :permission:`messagesTagsList`

.. rst-class:: api-main-section

Types
=====

.. _messages.tags.MessageTag:

MessageTag
----------

.. api-section-annotation-hack:: -- [Added in TB 121]

.. api-header::
   :label: object

   .. _messages.tags.MessageTag.color:

   .. api-member::
      :name: ``color``
      :type: (string)

      Tag color in upper case hex format (i.e.: :value:`#000080` for navy blue).

   .. _messages.tags.MessageTag.key:

   .. api-member::
      :name: ``key``
      :type: (string)

      Unique tag identifier.

   .. _messages.tags.MessageTag.ordinal:

   .. api-member::
      :name: ``ordinal``
      :type: (string)

      A custom sort string.

   .. _messages.tags.MessageTag.tag:

   .. api-member::
      :name: ``tag``
      :type: (string)

      Human-readable tag name.

.. _messages.tags.MessageTagProperties:

MessageTagProperties
--------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

.. api-header::
   :label: object

   .. _messages.tags.MessageTagProperties.color:

   .. api-member::
      :name: [``color``]
      :type: (string, optional)

      Tag color in upper case hex format (i.e.: :value:`#000080` for navy blue).

   .. _messages.tags.MessageTagProperties.ordinal:

   .. api-member::
      :name: [``ordinal``]
      :type: (string, optional)

      A custom sort string.

   .. _messages.tags.MessageTagProperties.tag:

   .. api-member::
      :name: [``tag``]
      :type: (string, optional)

      Human-readable tag name.
