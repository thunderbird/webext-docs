.. container:: sticky-sidebar

  ≡ messages.tags API

  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /overlay/developer-resources.rst

=================
messages.tags API
=================

The messages.tags API first appeared in Thunderbird 121.

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Permissions
===========

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

create(key, tag, color)
-----------------------

.. api-section-annotation-hack:: 

Creates a new message tag. Tagging a message will store the tag's key in the user's message. Throws if the specified tag key is used already.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``key``
      :type: (string)
      
      Unique tag identifier (will be converted to lower case). Must not include :value:`()<>{/%*"` or spaces.
   
   
   .. api-member::
      :name: ``tag``
      :type: (string)
      
      Human-readable tag name.
   
   
   .. api-member::
      :name: ``color``
      :type: (string)
      
      Tag color in hex format (i.e.: #000080 for navy blue). Value will be stored as upper case.
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesTags`

.. _messages.tags.delete:

delete(key)
-----------

.. api-section-annotation-hack:: 

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

.. api-section-annotation-hack:: 

Returns a list of tags that can be set on messages, and their human-friendly name, colour, and sort order.

.. api-header::
   :label: Return type (`Promise`_)

   
   .. api-member::
      :type: array of :ref:`messages.tags.MessageTag`
   
   
   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`messagesTagsList`

.. _messages.tags.update:

update(key, updateProperties)
-----------------------------

.. api-section-annotation-hack:: 

Updates a message tag. Throws if the specified tag key does not exist.

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``key``
      :type: (string)
      
      Unique tag identifier (will be converted to lower case). Must not include :value:`()<>{/%*"` or spaces.
   
   
   .. api-member::
      :name: ``updateProperties``
      :type: (object)
      
      .. api-member::
         :name: [``color``]
         :type: (string, optional)
         
         Tag color in hex format (i.e.: #000080 for navy blue). Value will be stored as upper case.
      
      
      .. api-member::
         :name: [``tag``]
         :type: (string, optional)
         
         Human-readable tag name.
      
   

.. api-header::
   :label: Required permissions

   - :permission:`messagesTags`

.. rst-class:: api-main-section

Types
=====

.. _messages.tags.MessageTag:

MessageTag
----------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``color``
      :type: (string)
      
      Tag color.
   
   
   .. api-member::
      :name: ``key``
      :type: (string)
      
      Unique tag identifier.
   
   
   .. api-member::
      :name: ``ordinal``
      :type: (string)
      
      Custom sort string (usually empty).
   
   
   .. api-member::
      :name: ``tag``
      :type: (string)
      
      Human-readable tag name.
   

.. _messages.tags.TagsDetail:

TagsDetail
----------

.. api-section-annotation-hack:: 

Used for filtering messages by tag in various methods. Note that functions using this type may have a partial implementation.

.. api-header::
   :label: object

   
   .. api-member::
      :name: ``mode``
      :type: (`string`)
      
      Whether all of the tag filters must apply, or any of them.
      
      Supported values:
      
      .. api-member::
         :name: :value:`all`
      
      .. api-member::
         :name: :value:`any`
   
   
   .. api-member::
      :name: ``tags``
      :type: (object)
      
      A *dictionary object* with one or more filter condition as *key-value* pairs, the *key* being the tag to filter on, and the *value* being a boolean expression, requesting whether a message must include (:value:`true`) or exclude (:value:`false`) the tag. For a list of available tags, call the :ref:`messages.tags.list` method.
   
