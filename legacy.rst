======
legacy
======

The legacy API first appeared in Thunderbird 63.

This API enables Thunderbird "legacy" extensions to continue working in the WebExtensions world.
To this end, a new XUL overlay loader was created to replace the original one, which has been
removed.

For the most part, things works exactly as they did before. However, as overlays are now added to
a window's document *after* it has been parsed, you may experience some unusual behaviours. For
example, your code may add a listener for an event that has already happened, or the UI doesn't
return to its previous state correctly. Wibbly-wobbly, timey-wimey, … stuff.

.. warning::

  Legacy extensions will not be around forever, and possibly will not even make it to Thunderbird
  68.

Manifest file properties
========================

- [``legacy``] (boolean or object)
