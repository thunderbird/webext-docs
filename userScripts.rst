.. container:: sticky-sidebar

  ≡ userScripts API

  * `Permissions`_
  * `Functions`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

===============
userScripts API
===============

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The userScripts API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/userScripts>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

.. note::

   Available for use with Manifest V3 only.

.. note::

   An incompatible version of this API is available for Manifest V2. See `userScripts (Legacy) <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/userScripts_legacy>`__.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. _user^scripts.permission.user^scripts:

.. api-member::
   :name: :permission:`userScripts`
   :refid: user-scripts-permission-user-scripts
   :refname: userScripts

   Allow unverified third-party scripts to access your data.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`userScripts` is required to use ``messenger.userScripts.*``.

.. rst-class:: api-main-section

Functions
=========

.. _user^scripts.configure^world:

configureWorld(properties)
--------------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Configures the environment for scripts running in a USER_SCRIPT world.

.. api-header::
   :label: Parameters

   .. _user^scripts.configure^world.properties:

   .. api-member::
      :name: ``properties``
      :refid: user-scripts-configure-world-properties
      :refname: properties
      :type: (:ref:`user^scripts.^world^properties`)

      The desired configuration for a USER_SCRIPT world.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _user^scripts.get^scripts:

getScripts([filter])
--------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Returns all dynamically-registered user scripts for this extension.

.. api-header::
   :label: Parameters

   .. _user^scripts.get^scripts.filter:

   .. api-member::
      :name: [``filter``]
      :refid: user-scripts-get-scripts-filter
      :refname: filter
      :type: (:ref:`user^scripts.^user^script^filter`, optional)

      If specified, this method returns only the user scripts that match it.

.. api-header::
   :label: Return type (`Promise`_)

   .. _user^scripts.get^scripts.returns:

   .. api-member::
      :refid: user-scripts-get-scripts-returns
      :refname: _returns
      :type: array of :ref:`user^scripts.^registered^user^script`

      List of registered user scripts.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _user^scripts.get^world^configurations:

getWorldConfigurations()
------------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Returns all registered USER_SCRIPT world configurations.

.. api-header::
   :label: Return type (`Promise`_)

   .. _user^scripts.get^world^configurations.returns:

   .. api-member::
      :refid: user-scripts-get-world-configurations-returns
      :refname: _returns
      :type: array of :ref:`user^scripts.^world^properties`

      All configurations registered with configureWorld().

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _user^scripts.register:

register(scripts)
-----------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Registers one or more user scripts for this extension.

.. note::

   An incompatible version of this function is available for Manifest V2. See `userScripts (Legacy) <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/userScripts_legacy/register>`__.

.. api-header::
   :label: Parameters

   .. _user^scripts.register.scripts:

   .. api-member::
      :name: ``scripts``
      :refid: user-scripts-register-scripts
      :refname: scripts
      :type: (array of :ref:`user^scripts.^registered^user^script`)

      List of user scripts to be registered.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _user^scripts.reset^world^configuration:

resetWorldConfiguration([worldId])
----------------------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Resets the configuration for a given world. That world will fall back to the default world's configuration.

.. api-header::
   :label: Parameters

   .. _user^scripts.reset^world^configuration.world^id:

   .. api-member::
      :name: [``worldId``]
      :refid: user-scripts-reset-world-configuration-world-id
      :refname: worldId
      :type: (string, optional)

      The ID of the USER_SCRIPT world to reset. If omitted or empty, resets the default world's configuration.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _user^scripts.unregister:

unregister([filter])
--------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Unregisters all dynamically-registered user scripts for this extension.

.. api-header::
   :label: Parameters

   .. _user^scripts.unregister.filter:

   .. api-member::
      :name: [``filter``]
      :refid: user-scripts-unregister-filter
      :refname: filter
      :type: (:ref:`user^scripts.^user^script^filter`, optional)

      If specified, this method unregisters only the user scripts that match it.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. _user^scripts.update:

update(scripts)
---------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Updates one or more user scripts for this extension.

.. api-header::
   :label: Parameters

   .. _user^scripts.update.scripts:

   .. api-member::
      :name: ``scripts``
      :refid: user-scripts-update-scripts
      :refname: scripts
      :type: (array of object)

      List of user scripts to be updated.

.. api-header::
   :label: Required permissions

   - :permission:`userScripts`

.. rst-class:: api-main-section

Types
=====

.. _user^scripts.^execution^world:

ExecutionWorld
--------------

.. api-section-annotation-hack:: -- [Added in TB 136]

The JavaScript world for a script to execute within. :code:`USER_SCRIPT` is the default execution environment of user scripts, :code:`MAIN` is the web page's execution environment.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _user^scripts.^execution^world.^m^a^i^n:

         .. api-member::
            :name: :value:`MAIN`
            :refid: user-scripts-execution-world-m-a-i-n
            :refname: MAIN

         .. _user^scripts.^execution^world.^u^s^e^r_^s^c^r^i^p^t:

         .. api-member::
            :name: :value:`USER_SCRIPT`
            :refid: user-scripts-execution-world-u-s-e-r-s-c-r-i-p-t
            :refname: USER_SCRIPT

.. _user^scripts.^match^pattern:

MatchPattern
------------

.. api-section-annotation-hack:: 

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _user^scripts.^match^pattern.<all_urls>:

         .. api-member::
            :name: :value:`<all_urls>`
            :refid: user-scripts-match-pattern-all-urls
            :refname: <all_urls>

*or*

.. api-header::
   :label: :ref:`user^scripts.^match^pattern^restricted`

*or*

.. api-header::
   :label: :ref:`user^scripts.^match^pattern^unestricted`

.. _user^scripts.^match^pattern^restricted:

MatchPatternRestricted
----------------------

.. api-section-annotation-hack:: 

Same as MatchPattern above, but excludes <all_urls>

.. api-header::
   :label: string

*or*

.. api-header::
   :label: string

.. _user^scripts.^match^pattern^unestricted:

MatchPatternUnestricted
-----------------------

.. api-section-annotation-hack:: 

Mostly unrestricted match patterns for privileged add-ons. This should technically be rejected for unprivileged add-ons, but, reasons. The MatchPattern class will still refuse privileged schemes for those extensions.

.. api-header::
   :label: string

.. _user^scripts.^registered^user^script:

RegisteredUserScript
--------------------

.. api-section-annotation-hack:: -- [Added in TB 136]

An object that represents a user script registered programmatically

.. api-header::
   :label: object

   .. _user^scripts.^registered^user^script.id:

   .. api-member::
      :name: ``id``
      :refid: user-scripts-registered-user-script-id
      :refname: id
      :type: (string)

      The ID of the user script specified in the API call. This property must not start with a '_' as it's reserved as a prefix for generated script IDs.

   .. _user^scripts.^registered^user^script.js:

   .. api-member::
      :name: ``js``
      :refid: user-scripts-registered-user-script-js
      :refname: js
      :type: (array of :ref:`user^scripts.^script^source`)

      The list of ScriptSource objects defining sources of scripts to be injected into matching pages.

   .. _user^scripts.^registered^user^script.all^frames:

   .. api-member::
      :name: [``allFrames``]
      :refid: user-scripts-registered-user-script-all-frames
      :refname: allFrames
      :type: (boolean, optional)

      If allFrames is :code:`true`, implies that the JavaScript should be injected into all frames of current page. By default, it's :code:`false` and is only injected into the top frame.

   .. _user^scripts.^registered^user^script.exclude^globs:

   .. api-member::
      :name: [``excludeGlobs``]
      :refid: user-scripts-registered-user-script-exclude-globs
      :refname: excludeGlobs
      :type: (array of string, optional)

   .. _user^scripts.^registered^user^script.exclude^matches:

   .. api-member::
      :name: [``excludeMatches``]
      :refid: user-scripts-registered-user-script-exclude-matches
      :refname: excludeMatches
      :type: (array of :ref:`user^scripts.^match^pattern`, optional)

   .. _user^scripts.^registered^user^script.include^globs:

   .. api-member::
      :name: [``includeGlobs``]
      :refid: user-scripts-registered-user-script-include-globs
      :refname: includeGlobs
      :type: (array of string, optional)

      At least one of matches or includeGlobs should be non-empty. The script runs in documents whose URL match either pattern.

   .. _user^scripts.^registered^user^script.matches:

   .. api-member::
      :name: [``matches``]
      :refid: user-scripts-registered-user-script-matches
      :refname: matches
      :type: (array of :ref:`user^scripts.^match^pattern`, optional)

      At least one of matches or includeGlobs should be non-empty. The script runs in documents whose URL match either pattern.

   .. _user^scripts.^registered^user^script.run^at:

   .. api-member::
      :name: [``runAt``]
      :refid: user-scripts-registered-user-script-run-at
      :refname: runAt
      :type: (:ref:`user^scripts.^run^at`, optional)

      The soonest that the JavaScript will be injected into the tab. Defaults to "document_idle".

   .. _user^scripts.^registered^user^script.world:

   .. api-member::
      :name: [``world``]
      :refid: user-scripts-registered-user-script-world
      :refname: world
      :type: (:ref:`user^scripts.^execution^world`, optional)

      The JavaScript script for a script to execute within. Defaults to "USER_SCRIPT".

   .. _user^scripts.^registered^user^script.world^id:

   .. api-member::
      :name: [``worldId``]
      :refid: user-scripts-registered-user-script-world-id
      :refname: worldId
      :type: (string, optional)

      If specified, specifies a specific user script world ID to execute in. Only valid if :value:`world` is omitted or is :value:`USER_SCRIPT`. If :value:`worldId` is omitted, the script will execute in the default user script world (""). Values with leading underscores (:value:`_`) are reserved. The maximum length is 256.

.. _user^scripts.^run^at:

RunAt
-----

.. api-section-annotation-hack:: -- [Added in TB 45]

The soonest that the JavaScript or CSS will be injected into the tab.

.. api-header::
   :label: `string`

   .. container:: api-member-node

      .. container:: api-member-description-only

         Supported values:

         .. _user^scripts.^run^at.document_end:

         .. api-member::
            :name: :value:`document_end`
            :refid: user-scripts-run-at-document-end
            :refname: document_end

         .. _user^scripts.^run^at.document_idle:

         .. api-member::
            :name: :value:`document_idle`
            :refid: user-scripts-run-at-document-idle
            :refname: document_idle

         .. _user^scripts.^run^at.document_start:

         .. api-member::
            :name: :value:`document_start`
            :refid: user-scripts-run-at-document-start
            :refname: document_start

.. _user^scripts.^script^source:

ScriptSource
------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Object with file xor code property. Equivalent to the ExtensionFileOrCode, except the file remains a relative URL.

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _user^scripts.^script^source.file:

         .. api-member::
            :name: ``file``
            :refid: user-scripts-script-source-file
            :refname: file
            :type: (string)

            The path of the JavaScript file to inject relative to the extension's root directory.

*or*

.. api-header::
   :label: object

   .. container:: api-member-node

      .. container:: api-member-description-only

         .. _user^scripts.^script^source.code:

         .. api-member::
            :name: ``code``
            :refid: user-scripts-script-source-code
            :refname: code
            :type: (string)

.. _user^scripts.^user^script^filter:

UserScriptFilter
----------------

.. api-section-annotation-hack:: -- [Added in TB 136]

Optional filter to use with getScripts() and unregister().

.. api-header::
   :label: object

   .. _user^scripts.^user^script^filter.ids:

   .. api-member::
      :name: [``ids``]
      :refid: user-scripts-user-script-filter-ids
      :refname: ids
      :type: (array of string, optional)

.. _user^scripts.^world^properties:

WorldProperties
---------------

.. api-section-annotation-hack:: -- [Added in TB 136]

The configuration of a USER_SCRIPT world.

.. api-header::
   :label: object

   .. _user^scripts.^world^properties.csp:

   .. api-member::
      :name: [``csp``]
      :refid: user-scripts-world-properties-csp
      :refname: csp
      :type: (string, optional)

      The world's Content Security Policy. Defaults to the CSP of regular content scripts, which prohibits dynamic code execution such as eval.

   .. _user^scripts.^world^properties.messaging:

   .. api-member::
      :name: [``messaging``]
      :refid: user-scripts-world-properties-messaging
      :refname: messaging
      :type: (boolean, optional)

      Whether the runtime.sendMessage and runtime.connect methods are exposed. Defaults to not exposing these messaging APIs.

   .. _user^scripts.^world^properties.world^id:

   .. api-member::
      :name: [``worldId``]
      :refid: user-scripts-world-properties-world-id
      :refname: worldId
      :type: (string, optional)

      The identifier of the world. Values with leading underscores (:value:`_`) are reserved. The maximum length is 256. Defaults to the default USER_SCRIPT world ("").
