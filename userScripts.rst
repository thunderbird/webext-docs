.. container:: sticky-sidebar

  ≡ userScripts API

  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /includes/developer-resources.rst

===============
userScripts API
===============

.. role:: permission

.. role:: value

.. role:: code

.. rst-class:: api-main-section

Permissions
===========

.. api-member::
   :name: :permission:`userScripts`

   Allow unverified third-party scripts to access your data

.. rst-class:: api-permission-info

.. note::

   A manifest entry named :value:`user_scripts` is required to use ``messenger.userScripts.*``.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`userScripts` is required to use ``messenger.userScripts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _userScripts.configureWorld:

configureWorld(properties)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Configures the environment for scripts running in a USER_SCRIPT world.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``properties``
      :type: (:ref:`userScripts.WorldProperties`)

      The desired configuration for a USER_SCRIPT world.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _userScripts.getScripts:

getScripts([filter])
--------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Returns all dynamically-registered user scripts for this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`userScripts.UserScriptFilter`, optional)

      If specified, this method returns only the user scripts that match it.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`userScripts.RegisteredUserScript`

      List of registered user scripts.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _userScripts.getWorldConfigurations:

getWorldConfigurations()
------------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Returns all registered USER_SCRIPT world configurations.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`userScripts.WorldProperties`

      All configurations registered with configureWorld().

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _userScripts.register:

register(scripts)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Registers one or more user scripts for this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``scripts``
      :type: (array of :ref:`userScripts.RegisteredUserScript`)

      List of user scripts to be registered.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _userScripts.resetWorldConfiguration:

resetWorldConfiguration([worldId])
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Resets the configuration for a given world. That world will fall back to the default world's configuration.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``worldId``]
      :type: (string, optional)

      The ID of the USER_SCRIPT world to reset. If omitted or empty, resets the default world's configuration.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _userScripts.unregister:

unregister([filter])
--------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Unregisters all dynamically-registered user scripts for this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``filter``]
      :type: (:ref:`userScripts.UserScriptFilter`, optional)

      If specified, this method unregisters only the user scripts that match it.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _userScripts.update:

update(scripts)
---------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Updates one or more user scripts for this extension.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: ``scripts``
      :type: (array of object)

      List of user scripts to be updated.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. rst-class:: api-main-section

Types
=====

.. _userScripts.RunAt:

RunAt
-----

.. api-section-annotation-hack:: -- [Added in TB 45]

The soonest that the JavaScript or CSS will be injected into the tab.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`document_start`

         .. api-member::
            :name: :value:`document_end`

         .. api-member::
            :name: :value:`document_idle`

.. _userScripts.MatchPattern:

MatchPattern
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`<all_urls>`

OR

.. api-header::
   :label: :ref:`userScripts.MatchPatternRestricted`

OR

.. api-header::
   :label: :ref:`userScripts.MatchPatternUnestricted`

.. _userScripts.ExecutionWorld:

ExecutionWorld
--------------

.. api-section-annotation-hack:: -- [Added in TB 136]

The JavaScript world for a script to execute within. :code:`USER_SCRIPT` is the default execution environment of user scripts, :code:`MAIN` is the web page's execution environment.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. api-member::
            :name: :value:`MAIN`

         .. api-member::
            :name: :value:`USER_SCRIPT`

.. _userScripts.RegisteredUserScript:

RegisteredUserScript
--------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

An object that represents a user script registered programmatically

.. api-header::
   :label: object

   .. api-member::
      :name: ``id``
      :type: (string)

      The ID of the user script specified in the API call. This property must not start with a '_' as it's reserved as a prefix for generated script IDs.

   .. api-member::
      :name: ``js``
      :type: (array of :ref:`userScripts.ScriptSource`)

      The list of ScriptSource objects defining sources of scripts to be injected into matching pages.

   .. api-member::
      :name: [``allFrames``]
      :type: (boolean, optional)

      If allFrames is :code:`true`, implies that the JavaScript should be injected into all frames of current page. By default, it's :code:`false` and is only injected into the top frame.

   .. api-member::
      :name: [``excludeGlobs``]
      :type: (array of string, optional)

   .. api-member::
      :name: [``excludeMatches``]
      :type: (array of :ref:`userScripts.MatchPattern`, optional)

   .. api-member::
      :name: [``includeGlobs``]
      :type: (array of string, optional)

      At least one of matches or includeGlobs should be non-empty. The script runs in documents whose URL match either pattern.

   .. api-member::
      :name: [``matches``]
      :type: (array of :ref:`userScripts.MatchPattern`, optional)

      At least one of matches or includeGlobs should be non-empty. The script runs in documents whose URL match either pattern.

   .. api-member::
      :name: [``runAt``]
      :type: (:ref:`userScripts.RunAt`, optional)

      The soonest that the JavaScript will be injected into the tab. Defaults to "document_idle".

   .. api-member::
      :name: [``world``]
      :type: (:ref:`userScripts.ExecutionWorld`, optional)

      The JavaScript script for a script to execute within. Defaults to "USER_SCRIPT".

   .. api-member::
      :name: [``worldId``]
      :type: (string, optional)

      If specified, specifies a specific user script world ID to execute in. Only valid if :value:`world` is omitted or is :value:`USER_SCRIPT`. If :value:`worldId` is omitted, the script will execute in the default user script world (""). Values with leading underscores (:value:`_`) are reserved. The maximum length is 256.

.. _userScripts.ScriptSource:

ScriptSource
------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Object with file xor code property. Equivalent to the ExtensionFileOrCode, except the file remains a relative URL.

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. api-member::
            :name: ``file``
            :type: (string)

            The path of the JavaScript file to inject relative to the extension's root directory.

OR

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. api-member::
            :name: ``code``
            :type: (string)

.. _userScripts.UserScriptFilter:

UserScriptFilter
----------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Optional filter to use with getScripts() and unregister().

.. api-header::
   :label: object

   .. api-member::
      :name: [``ids``]
      :type: (array of string, optional)

.. _userScripts.WorldProperties:

WorldProperties
---------------

.. api-section-annotation-hack:: -- [Added in TB 136]

The configuration of a USER_SCRIPT world.

.. api-header::
   :label: object

   .. api-member::
      :name: [``csp``]
      :type: (string, optional)

      The world's Content Security Policy. Defaults to the CSP of regular content scripts, which prohibits dynamic code execution such as eval.

   .. api-member::
      :name: [``messaging``]
      :type: (boolean, optional)

      Whether the runtime.sendMessage and runtime.connect methods are exposed. Defaults to not exposing these messaging APIs.

   .. api-member::
      :name: [``worldId``]
      :type: (string, optional)

      The identifier of the world. Values with leading underscores (:value:`_`) are reserved. The maximum length is 256. Defaults to the default USER_SCRIPT world ("").
