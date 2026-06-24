Vendoring 3rd party libraries
=============================

Add-ons are not allowed to load and execute remote code at runtime, so every
third-party library an add-on relies on must be **bundled** (*vendored*) into
the package. To keep these bundled copies trustworthy, each one has to be
declared and traceable back to an exact upstream release.

If your extension uses minified, obfuscated or otherwise machine-generated
first-party code, please see `our requirements`__ for that.

__ https://extensionworkshop.com/documentation/publish/source-code-submission/

Declaring your vendored libraries unlocks two things:

- **Automated security auditing.** Declared, version-pinned libraries are matched
  against known-vulnerability databases, so an add-on shipping a vulnerable
  release is flagged automatically, and outdated dependencies with newer releases
  available can be surfaced.
- **Source integrity.** The review team verifies that each bundled file is
  byte-for-byte identical to the official release by comparing checksums (hashes).
  This only works if the bundled copy is **unmodified** and if the declaration
  points at the exact file it was copied from.

For a declaration to be verifiable, every source URL must:

- point to the **exact file** of a **specific release** (not a branch, a
  ``latest`` tag, or a bare repository link), and
- be hosted on a **trusted source**: ``unpkg.com``, ``cdn.jsdelivr.net``, or
  ``registry.npmjs.org`` (all backed by the npm registry), or
  ``raw.githubusercontent.com``.

The three npm-backed sources resolve to a package name and version, which lets them
be audited against the `OSV <https://osv.dev/>`__ (Open Source Vulnerabilities)
database automatically, so prefer them. ``raw.githubusercontent.com`` is supported
as a less-preferred alternative. A file served straight from GitHub cannot be
mapped to an npm release, so its known-vulnerability status cannot be determined
automatically, even though it can still be integrity-checked.

There are two accepted ways to declare vendored libraries. One is a free-form
``VENDOR.md`` file. The other is a ``package.json``, a structured format in which
you name each package and the exact version you bundle. Both are first-class
options, so use whichever fits your workflow.

Declare libraries in a ``VENDOR.md`` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Place a file named ``VENDOR.md`` in the root of the add-on. List every bundled
library in its own block, pairing the **packaged file path** with the **source
URL** it was downloaded from:

.. code-block:: markdown
   :caption: VENDOR.md

   vendor/purify.min.js:
    - Version: 3.4.11
    - URL: https://cdn.jsdelivr.net/npm/dompurify@3.4.11/dist/purify.min.js

   vendor/lighterhtml.min.js:
    - Version: 4.2.0
    - URL: https://cdn.jsdelivr.net/npm/lighterhtml@4.2.0/min.js

The format is intentionally lenient. What matters is that each bundled file is
paired with a source URL that points to the exact released file on a trusted host.
To vendor a library that ships as several files, declare the **folder** it lives
in instead of listing every file individually.

Declare libraries in ``package.json``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ``package.json`` lets you declare each bundled library as a structured
dependency, listing the package name and the version you ship. You do not need an
existing npm setup to use it. You can write the file purely to document your
vendored libraries, and when you do, no separate ``VENDOR.md`` is needed for those
libraries. Each dependency must resolve to an **exact** version so the bundled copy
can be checked against a known release:

.. code-block:: json
   :caption: package.json

   {
     "name": "my-addon",
     "version": "1.0.0",
     "dependencies": {
       "dompurify": "3.4.11"
     }
   }

A version **range** (for example ``^3.4.11`` or ``~3.4``) is not pinned, because
it can resolve to different releases over time:

.. code-block:: json
   :caption: package.json

   {
     "name": "my-addon",
     "version": "1.0.0",
     "dependencies": {
       "dompurify": "^3.4.11"
     }
   }

If you want to keep using ranges in ``package.json``, commit the lock file
alongside it. The lock file records the exact resolved version that was bundled,
which is what gets verified. Any of ``package-lock.json``, ``npm-shrinkwrap.json``,
``yarn.lock``, or ``pnpm-lock.yaml`` is accepted:

.. code-block:: json
   :caption: package-lock.json

   {
     "name": "my-addon",
     "version": "1.0.0",
     "lockfileVersion": 3,
     "packages": {
       "node_modules/dompurify": {
         "version": "3.4.11",
         "resolved": "https://registry.npmjs.org/dompurify/-/dompurify-3.4.11.tgz",
         "integrity": "sha512-..."
       }
     }
   }

Because these declarations name an npm package and an exact version, they are
audited against the OSV database automatically.

Pull in libraries and generate these files with npm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`npm <https://www.npmjs.com/>`__ creates and maintains both files for you. In the
add-on project folder:

1. Create a ``package.json`` if you do not already have one:

   .. code-block:: shell

      npm init -y

2. Install each library. This adds it to the ``dependencies`` section of the
   ``package.json`` file and writes the exact version you received into the
   ``package-lock.json`` file, which is what documents the bundled version:

   .. code-block:: shell

      npm install dompurify

3. Copy the file you actually load from the ``node_modules`` folder into the
   add-on, then reference that local copy from your code:

   .. code-block:: shell

      cp node_modules/dompurify/dist/purify.min.js vendor/purify.min.js

The ``node_modules`` folder is only used to obtain the files and does not need to
ship with the add-on. The ``package.json`` and the lock file are what document the
bundled versions for review.

Update a vendored library
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a review reports a known vulnerability, or a newer release is simply
available, bump the bundled copy to a fixed version. A vulnerability advisory
names the release that resolves the issue, so pick a version at or above it.

If you manage the library with ``package.json``, install the newer version. This
rewrites both the ``package.json`` and the lock file:

.. code-block:: shell

   npm install dompurify@latest

You can also request a specific version instead of ``latest``, for example
``npm install dompurify@3.4.12``. Then re-copy the updated file into the add-on,
overwriting the old copy:

.. code-block:: shell

   cp node_modules/dompurify/dist/purify.min.js vendor/purify.min.js

If you declared the library in a ``VENDOR.md`` file, do the same by hand:

1. Download the newer release from a trusted source.
2. Replace the bundled file in the add-on with the new copy.
3. Update the ``Version`` and ``URL`` entries in ``VENDOR.md`` to match the
   release you just bundled.

In both cases, make sure the bundled file is the unmodified release so its
checksum still matches the upstream version, then resubmit the add-on.
