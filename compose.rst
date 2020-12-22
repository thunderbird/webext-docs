.. _compose_api:

=======
compose
=======

This message composition window API first appeared in Thunderbird 67 (see `bug 1503423`__).

__ https://bugzilla.mozilla.org/show_bug.cgi?id=1503423

.. role:: permission

.. rst-class:: api-main-section

Functions
=========

.. _compose.beginNew:

beginNew([details])
-------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: [``details``]
      :type: (:ref:`compose.ComposeParams`)
   

.. _compose.beginReply:

beginReply(messageId, [replyType])
----------------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
      
      The message to reply to, as retrieved using other APIs.
   
   
   .. api-member::
      :name: [``replyType``]
      :type: (`string`)
      
      Supported values:
      
      .. api-member::
         :name: ``replyToSender``
      
      .. api-member::
         :name: ``replyToList``
      
      .. api-member::
         :name: ``replyToAll``
   

.. _compose.beginForward:

beginForward(messageId, [forwardType], [details])
-------------------------------------------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: Parameters

   
   .. api-member::
      :name: ``messageId``
      :type: (integer)
      
      The message to forward, as retrieved using other APIs.
   
   
   .. api-member::
      :name: [``forwardType``]
      :type: (`string`)
      
      Supported values:
      
      .. api-member::
         :name: ``forwardInline``
      
      .. api-member::
         :name: ``forwardAsAttachment``
   
   
   .. api-member::
      :name: [``details``]
      :type: (:ref:`compose.ComposeParams`)
   

.. rst-class:: api-main-section

Types
=====

.. _compose.ComposeParams:

ComposeParams
-------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: object

   
   .. api-member::
      :name: [``bcc``]
      :type: (array of :ref:`compose.ComposeRecipient`)
   
   
   .. api-member::
      :name: [``body``]
      :type: (string)
   
   
   .. api-member::
      :name: [``cc``]
      :type: (array of :ref:`compose.ComposeRecipient`)
   
   
   .. api-member::
      :name: [``replyTo``]
      :type: (string)
   
   
   .. api-member::
      :name: [``subject``]
      :type: (string)
   
   
   .. api-member::
      :name: [``to``]
      :type: (array of :ref:`compose.ComposeRecipient`)
   

.. _compose.ComposeRecipient:

ComposeRecipient
----------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         A name and email address in the format "Name <email@example.com>", or just an email address.
   

OR

.. api-header::
   :label: object

   
   .. container:: api-member-node
   
      .. container:: api-member-description-only
         
         .. api-member::
            :name: ``id``
            :type: (string)
            
            The ID of a contact or mailing list from the :doc:`contacts` and :doc:`mailingLists` APIs.
         
         
         .. api-member::
            :name: ``type``
            :type: (`string`)
            
            Which sort of object this ID is for.
            
            Supported values:
            
            .. api-member::
               :name: ``contact``
            
            .. api-member::
               :name: ``mailingList``
         
   
