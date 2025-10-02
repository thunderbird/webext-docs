.. container:: sticky-sidebar

  ≡ messages.tags API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

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

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _messages.tags.permission.accounts^read:

.. api-member::
   :name: :permission:`accountsRead`
   :refid: messages-tags-permission-accounts-read

   See your mail accounts, their identities and their folders.

.. _messages.tags.permission.messages^tags:

.. api-member::
   :name: :permission:`messagesTags`
   :refid: messages-tags-permission-messages-tags

   Create, modify and delete message tags.

.. _messages.tags.permission.messages^tags^list:

.. api-member::
   :name: :permission:`messagesTagsList`
   :refid: messages-tags-permission-messages-tags-list

   List message tags.

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

   .. _messages.tags.create.key:

   .. api-member::
      :name: [``key``]
      :refid: messages-tags-create-key
      :type: (string, optional)

      Unique tag identifier (will be converted to lower case). Must not include :value:`()<>{/%*"` or spaces. Will be auto-generated if not provided.

   .. _messages.tags.create.tag:

   .. api-member::
      :name: ``tag``
      :refid: messages-tags-create-tag
      :type: (string)

      Human-readable tag name.

   .. _messages.tags.create.color:

   .. api-member::
      :name: ``color``
      :refid: messages-tags-create-color
      :type: (string)

      Tag color in hex format (i.e.: :value:`#000080` for navy blue).

   .. _messages.tags.create.callback:

   .. api-member::
      :name: [``callback``]
      :refid: messages-tags-create-callback
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

   .. _messages.tags.delete.key:

   .. api-member::
      :name: ``key``
      :refid: messages-tags-delete-key
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

   .. _messages.tags.list.returns:

   .. api-member::
      :refid: messages-tags-list-returns
      :type: array of :ref:`messages.tags.^message^tag`

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

   .. _messages.tags.update.key:

   .. api-member::
      :name: ``key``
      :refid: messages-tags-update-key
      :type: (string)

      Unique tag identifier (will be converted to lower case). Must not include :value:`()<>{/%*"` or spaces.

   .. _messages.tags.update.update^properties:

   .. api-member::
      :name: ``updateProperties``
      :refid: messages-tags-update-update-properties
      :type: (:ref:`messages.tags.^message^tag^properties`)

.. api-header::
   :label: Required permissions

   - :permission:`messagesTags`

.. rst-class:: api-main-section

Events
======

.. _messages.tags.on^created:

onCreated
---------

.. api-section-annotation-hack:: -- [Added in TB 136]

Fired when a new message tag has been created.

.. api-header::
   :label: Parameters for onCreated.addListener(listener)

   .. _messages.tags.on^created.listener(tag):

   .. api-member::
      :name: ``listener(tag)``
      :refid: messages-tags-on-created-listener-tag

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _messages.tags.on^created.tag:

   .. api-member::
      :name: ``tag``
      :refid: messages-tags-on-created-tag
      :type: (:ref:`messages.tags.^message^tag`)

.. api-header::
   :label: Required permissions

   - :permission:`messagesTagsList`

.. _messages.tags.on^deleted:

onDeleted
---------

.. api-section-annotation-hack:: -- [Added in TB 136]

Fired when a message tag has been deleted.

.. api-header::
   :label: Parameters for onDeleted.addListener(listener)

   .. _messages.tags.on^deleted.listener(key):

   .. api-member::
      :name: ``listener(key)``
      :refid: messages-tags-on-deleted-listener-key

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _messages.tags.on^deleted.key:

   .. api-member::
      :name: ``key``
      :refid: messages-tags-on-deleted-key
      :type: (string)

      Unique tag identifier of the deleted message tag.

.. api-header::
   :label: Required permissions

   - :permission:`accountsRead`

.. _messages.tags.on^updated:

onUpdated
---------

.. api-section-annotation-hack:: -- [Added in TB 136]

Fired when one or more properties of a message tag have been updated.

.. api-header::
   :label: Parameters for onUpdated.addListener(listener)

   .. _messages.tags.on^updated.listener(key, changed^properties, old^properties):

   .. api-member::
      :name: ``listener(key, changedProperties, oldProperties)``
      :refid: messages-tags-on-updated-listener-key-changed-properties-old-properties

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. _messages.tags.on^updated.key:

   .. api-member::
      :name: ``key``
      :refid: messages-tags-on-updated-key
      :type: (string)

      Unique tag identifier of the updated message tag.

   .. _messages.tags.on^updated.changed^properties:

   .. api-member::
      :name: ``changedProperties``
      :refid: messages-tags-on-updated-changed-properties
      :type: (:ref:`messages.tags.^message^tag^properties`)

      The changed message tag properties.

   .. _messages.tags.on^updated.old^properties:

   .. api-member::
      :name: ``oldProperties``
      :refid: messages-tags-on-updated-old-properties
      :type: (:ref:`messages.tags.^message^tag^properties`)

      The old values of the changed message tag properties.

.. api-header::
   :label: Required permissions

   - :permission:`messagesTagsList`

.. rst-class:: api-main-section

Types
=====

.. _messages.tags.^message^tag:

MessageTag
----------

.. api-section-annotation-hack:: -- [Added in TB 121]

.. api-header::
   :label: object

   .. _messages.tags.^message^tag.color:

   .. api-member::
      :name: ``color``
      :refid: messages-tags-message-tag-color
      :type: (string)

      Tag color in upper case hex format (i.e.: :value:`#000080` for navy blue).

   .. _messages.tags.^message^tag.key:

   .. api-member::
      :name: ``key``
      :refid: messages-tags-message-tag-key
      :type: (string)

      Unique tag identifier.

   .. _messages.tags.^message^tag.ordinal:

   .. api-member::
      :name: ``ordinal``
      :refid: messages-tags-message-tag-ordinal
      :type: (string)

      A custom sort string.

   .. _messages.tags.^message^tag.tag:

   .. api-member::
      :name: ``tag``
      :refid: messages-tags-message-tag-tag
      :type: (string)

      Human-readable tag name.

.. _messages.tags.^message^tag^properties:

MessageTagProperties
--------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

.. api-header::
   :label: object

   .. _messages.tags.^message^tag^properties.color:

   .. api-member::
      :name: [``color``]
      :refid: messages-tags-message-tag-properties-color
      :type: (string, optional)

      Tag color in upper case hex format (i.e.: :value:`#000080` for navy blue).

   .. _messages.tags.^message^tag^properties.ordinal:

   .. api-member::
      :name: [``ordinal``]
      :refid: messages-tags-message-tag-properties-ordinal
      :type: (string, optional)

      A custom sort string.

   .. _messages.tags.^message^tag^properties.tag:

   .. api-member::
      :name: [``tag``]
      :refid: messages-tags-message-tag-properties-tag
      :type: (string, optional)

      Human-readable tag name.

.. _messages.tags.^tags^detail:

TagsDetail
----------

.. api-section-annotation-hack:: -- [Added in TB 121]

Used for filtering messages by tag in various methods. Note that functions using this type may have a partial implementation.

.. api-header::
   :label: object

   .. _messages.tags.^tags^detail.mode:

   .. api-member::
      :name: ``mode``
      :refid: messages-tags-tags-detail-mode
      :type: (`string`)

      Whether all of the tag filters must apply, or any of them.

      Supported values:

      .. _messages.tags.^tags^detail.mode.all:

      .. api-member::
         :name: :value:`all`
         :refid: messages-tags-tags-detail-mode-all

      .. _messages.tags.^tags^detail.mode.any:

      .. api-member::
         :name: :value:`any`
         :refid: messages-tags-tags-detail-mode-any

   .. _messages.tags.^tags^detail.tags:

   .. api-member::
      :name: ``tags``
      :refid: messages-tags-tags-detail-tags
      :type: (object)

      A *dictionary object* with one or more filter condition as *key-value* pairs, the *key* being the tag to filter on, and the *value* being a boolean expression, requesting whether a message must include (:value:`true`) or exclude (:value:`false`) the tag. For a list of available tags, call the :ref:`messages.tags.list` method.
