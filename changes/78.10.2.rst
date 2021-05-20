==============================
Changes in Thunderbird 78.10.2
==============================

accounts
========

* accounts.list() has been fixed to work with folder names including `%` or `@` characters.


messages
========

* messages.getFull() now properly throws if something went wrong, instead of remaining in the pending state indefinitely.