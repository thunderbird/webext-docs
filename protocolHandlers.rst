.. container:: sticky-sidebar

  ≡ protocolHandlers API

  * `Manifest file properties`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

====================
protocolHandlers API
====================

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Manifest file properties
========================

.. _protocol^handlers.protocol_handlers:

.. api-member::
   :name: [``protocol_handlers``]
   :refid: protocol-handlers-protocol-handlers
   :refname: protocol_handlers
   :type: (array of :ref:`protocol^handlers.^protocol^handler`, optional)

   A list of protocol handler definitions.

.. rst-class:: api-main-section

Types
=====

.. _protocol^handlers.^extension^u^r^l:

ExtensionURL
------------

.. api-section-annotation-hack:: 

A path relative to the root of the extension.

.. api-header::
   :label: string

.. _protocol^handlers.^http^u^r^l:

HttpURL
-------

.. api-section-annotation-hack:: 

.. api-header::
   :label: string

.. _protocol^handlers.^protocol^handler:

ProtocolHandler
---------------

.. api-section-annotation-hack:: 

Represents a protocol handler definition.

.. api-header::
   :label: object

   .. _protocol^handlers.^protocol^handler.name:

   .. api-member::
      :name: ``name``
      :refid: protocol-handlers-protocol-handler-name
      :refname: name
      :type: (string)

      A user-readable title string for the protocol handler. This will be displayed to the user in interface objects as needed.

   .. _protocol^handlers.^protocol^handler.protocol:

   .. api-member::
      :name: ``protocol``
      :refid: protocol-handlers-protocol-handler-protocol
      :refname: protocol
      :type: (`string` or string)

      The protocol the site wishes to handle, specified as a string. For example, you can register to handle SMS text message links by registering to handle the "sms" scheme.

   .. _protocol^handlers.^protocol^handler.uri^template:

   .. api-member::
      :name: ``uriTemplate``
      :refid: protocol-handlers-protocol-handler-uri-template
      :refname: uriTemplate
      :type: (:ref:`protocol^handlers.^extension^u^r^l` or :ref:`protocol^handlers.^http^u^r^l`)

      The URL of the handler, as a string. This string should include "%s" as a placeholder which will be replaced with the escaped URL of the document to be handled. This URL might be a true URL, or it could be a phone number, email address, or so forth.
