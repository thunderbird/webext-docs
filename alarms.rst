.. container:: sticky-sidebar

  ≡ alarms API

  * `Permissions`_
  * `Functions`_
  * `Events`_
  * `Types`_

  .. include:: /_includes/developer-resources.rst

==========
alarms API
==========

.. role:: permission

.. role:: value

.. role:: code

.. hint::

   The alarms API is inherited from Firefox, and its primary documentation is maintained by Mozilla at `MDN <https://developer.mozilla.org/docs/Mozilla/Add-ons/WebExtensions/API/alarms>`__. Thunderbird implements only the subset of functions, events, and types listed here. The MDN pages may provide further details and examples, but they may also reference features that are not supported in Thunderbird.

.. rst-class:: api-main-section

Permissions
===========

The following permissions influence the behavior of the API. Depending on which permissions are requested, additional methods might be available, or certain data may be included in responses.

.. hint::

   Request permissions only when needed. Unnecessary requests may result in rejection during ATN review.

.. api-member::
   :name: :permission:`alarms`

   Grant access to some or all methods of the alarms API.

.. rst-class:: api-permission-info

.. note::

   The permission :permission:`alarms` is required to use ``messenger.alarms.*``.

.. rst-class:: api-main-section

Functions
=========

.. _alarms.clear:

clear([name])
-------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Clears the alarm with the given name.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``name``]
      :type: (string, optional)

      The name of the alarm to clear. Defaults to the empty string.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: boolean

      Whether an alarm of the given name was found to clear.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`alarms`

.. _alarms.clear^all:

clearAll()
----------

.. api-section-annotation-hack:: -- [Added in TB 45]

Clears all alarms.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: boolean

      Whether any alarm was found to clear.

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`alarms`

.. _alarms.create:

create([name], alarmInfo)
-------------------------

.. api-section-annotation-hack:: -- [Added in TB 45]

Creates an alarm. After the delay is expired, the onAlarm event is fired. If there is another alarm with the same name (or no name if none is specified), it will be cancelled and replaced by this alarm.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``name``]
      :type: (string, optional)

      Optional name to identify this alarm. Defaults to the empty string.

   .. api-member::
      :name: ``alarmInfo``
      :type: (object)

      Details about the alarm. The alarm first fires either at 'when' milliseconds past the epoch (if 'when' is provided), after 'delayInMinutes' minutes from the current time (if 'delayInMinutes' is provided instead), or after 'periodInMinutes' minutes from the current time (if only 'periodInMinutes' is provided). Users should never provide both 'when' and 'delayInMinutes'. If 'periodInMinutes' is provided, then the alarm recurs repeatedly after that many minutes.

      .. api-member::
         :name: [``delayInMinutes``]
         :type: (number, optional)

         Number of minutes from the current time after which the alarm should first fire.

      .. api-member::
         :name: [``periodInMinutes``]
         :type: (number, optional)

         Number of minutes after which the alarm should recur repeatedly.

      .. api-member::
         :name: [``when``]
         :type: (number, optional)

         Time when the alarm is scheduled to first fire, in milliseconds past the epoch.

.. api-header::
   :label: Required permissions

   - :permission:`alarms`

.. _alarms.get:

get([name])
-----------

.. api-section-annotation-hack:: -- [Added in TB 45]

Retrieves details about the specified alarm.

.. api-header::
   :label: Parameters

   .. api-member::
      :name: [``name``]
      :type: (string, optional)

      The name of the alarm to get. Defaults to the empty string.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: :ref:`alarms.^alarm`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`alarms`

.. _alarms.get^all:

getAll()
--------

.. api-section-annotation-hack:: -- [Added in TB 45]

Gets an array of all the alarms.

.. api-header::
   :label: Return type (`Promise`_)

   .. api-member::
      :type: array of :ref:`alarms.^alarm`

   .. _Promise: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

.. api-header::
   :label: Required permissions

   - :permission:`alarms`

.. rst-class:: api-main-section

Events
======

.. _alarms.on^alarm:

onAlarm
-------

.. api-section-annotation-hack:: -- [Added in TB 45]

Fired when an alarm has expired. Useful for transient background pages.

.. api-header::
   :label: Parameters for onAlarm.addListener(listener)

   .. api-member::
      :name: ``listener(name)``

      A function that will be called when this event occurs.

.. api-header::
   :label: Parameters passed to the listener function

   .. api-member::
      :name: ``name``
      :type: (:ref:`alarms.^alarm`)

      The alarm that has expired.

.. api-header::
   :label: Required permissions

   - :permission:`alarms`

.. rst-class:: api-main-section

Types
=====

.. _alarms.^alarm:

Alarm
-----

.. api-section-annotation-hack:: -- [Added in TB 45]

.. api-header::
   :label: object

   .. _alarms.^alarm.name:

   .. api-member::
      :name: ``name``
      :type: (string)

      Name of this alarm.

   .. _alarms.^alarm.scheduled^time:

   .. api-member::
      :name: ``scheduledTime``
      :type: (number)

      Time when the alarm is scheduled to fire, in milliseconds past the epoch.

   .. _alarms.^alarm.period^in^minutes:

   .. api-member::
      :name: [``periodInMinutes``]
      :type: (number, optional)

      When present, signals that the alarm triggers periodically after so many minutes.
