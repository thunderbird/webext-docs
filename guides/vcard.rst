.. container:: sticky-sidebar
  
  .. include:: ../_includes/developer-resources.rst

===========================
Working with vCard contacts
===========================

Since Thunderbird 102, contact details are stored as vCards. They are exposed via the ``vCard`` property, and updating this property will modify the contact according to the newly set vCard string.

Instead of manually parsing or manipulating the vCard string, we recommend using the same `ical.js <https://github.com/kewisch/ical.js>`__ library that Thunderbird itself uses. Bundle its ``ical.min.js`` build with the add-on from a trusted source (see :doc:`/guides/vendoring`) and import it into the background script. The background script must be declared as a module in order to import ES6 modules:

.. code-block:: json

  "background": {
    "scripts": [
      "background.js"
    ],
    "type": "module"
  },

Declare the bundled ``ical.min.js`` file, and any other third-party library you ship, so reviewers can verify it is unmodified. See :doc:`/guides/vendoring` for the trusted sources and the accepted declaration formats. The ``VENDOR.md`` entry could look like this:

.. code-block:: text
   :caption: VENDOR.md

   local/path/to/ical.min.js:
    - Version: 2.2.1
    - URL: https://cdn.jsdelivr.net/npm/ical.js@2.2.1/dist/ical.min.js

In the ``background.js`` script one can then import the library and parse vCard strings as follows:

.. code-block:: javascript

  import ICAL from "./ical.min.js";

  // Get JSON representation of the vCard data.
  let vCardObj = ICAL.parse("BEGIN:VCARD\r\nVERSION:4.0\r\nN:LastName;FirstName;;;\r\nEMAIL;PREF=1:user@inter.net\r\nEND:VCARD\r\n");
  let [ component, jCard ] = vCardObj;
  
  /* ICAL.parse() return value:
   *  
   * Array(3)
   *  0: "vcard"     // Name of the component.
   *  1: Array(3)    // Array of entries.
   *     0: Array(4) ["version", {}, "text", "4.0" ]
   *     1: Array(4) [ "n", {}, "text", [ "LastName", "FirstName", "", "", "" ] ]
   *     2: Array(4) [ "email", { pref: "1" }, "text", "user@inter.net"]
   *  2: Array []    // Array of subcomponents, should be empty for vCard, used
   *                 // by vCalendar, which has vEvent subcomponents.
   */

  // Manipulate the jCard object.
  if (component == "vcard") {
    let email = jCard.find(e => e[0] == "email");
    if (email) {
      email[3] = "other@inter.net"
    }
  }

  // Update the contact.
  messenger.contacts.update(id, {vCard: ICAL.stringify(vCardObj)});

The ical library also supports manipulating the data on a higher level, using the ``Component`` class:

.. code-block:: javascript

  // Get JSON representation of the vCard data (jCal).
  var vCard = new ICAL.Component(ICAL.parse("BEGIN:VCARD\r\nVERSION:4.0\r\nN:LastName;FirstName;;;\r\nEMAIL;PREF=1:user@inter.net\r\nEND:VCARD\r\n"));
  
  // Add an entry.
  vCard.addPropertyWithValue("email", "third@inter.net");
  
  /* Other useful methods:
   *
   *  vCard.getFirstProperty("email")
   *  vCard.getFirstPropertyValue("email")
   *
   *  vCard.getAllProperties("email")
   *  vCard.removeAllProperties("email")
   *
   *  let emailEntry = new ICAL.Property(["email", { pref: "1" }, "text", "other@inter.net"]);
   *  vCard.addProperty(emailEntry)
   *  vCard.addPropertyWithValue("email", "other2@inter.net")
   *
   *  vCard.removeProperty(emailEntry)
   */

  // Update an entry.
  let email = vCard.getAllProperties("email").find(e => e.jCal[3] == "user@inter.net");
  if (email) {
    // Option 1: Manipulate the existing jCal entry (Array(4), [name, options, type, value])
    email.jCal[3] = "other@inter.net";
    // Option 2: Remove the existing entry and add a new one (changes order of entries)
    vCard.removeProperty(email);
    vCard.addProperty(new ICAL.Property(["email", {}, "text", "other@inter.net"]));
  }

  // Update the contact.
  messenger.contacts.update(id, {vCard: vCard.toString()});

======================================
Working with legacy contact properties
======================================

Before the release of Thunderbird 102, contacts in Thunderbird's address books only supported a `fixed set of properties <https://searchfox.org/comm-central/rev/97fafb8294c5f9c9c65d33888a03f89a10b0b19e/mailnews/addrbook/modules/VCardUtils.jsm#310-349>`__. All these properties where accessible through :ref:`contacts.^contact^properties`.

.. important::

  Accessing contact details through these legacy properties is **deprecated**. Newly added fields in the address book UI (e.g. the ``Timezone`` information), are not accessible through legacy properties, but only through the vCard.
  
  When updating a contact and providing values for the ``vCard`` property as well as for legacy properties, the specified legacy properties are ignored.


Updating legacy properties
===========================

A vCard can store multiple values for each type and legacy properties point to the first entry of the associated type. Deleting the one which is currently exposed through a legacy property only deletes that single entry, not all entries. Consider a contact being updated and some of its legacy properties are cleared as follows:

.. code-block:: javascript

  await messenger.contacts.update(id, {
    "PrimaryEmail" : null,
    "HomePhone" : null
  })

If the vCard had multiple email addresses or multiple home numbers, each next entry will now be exposed through the associated legacy property. This can lead to unexpected results, when setting ``SecondEmail`` on a contact which does not yet have any email entries:

.. code-block:: javascript

  await messenger.contacts.update(id, {
    "SecondEmail" : "user@inter.net",
  })
  
  let { properties } = await messenger.contacts.get(id);
  console.log(properties);

The console output will include ``PrimaryEmail: user@inter.net``, but no value for ``SecondEmail``, simply because ``PrimaryEmail`` points to the first email address stored in the vCard.
