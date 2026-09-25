Source code submission for ATN review
======================================

Add-ons submitted to addons.thunderbird.net (ATN) are reviewed as submitted,
so the review team has to be able to read every file inside the package. If
your build process only **copies** files,
such as the workflow described in :doc:`/guides/vendoring`, the packaged
add-on already is that readable source, and no further submission is needed.

If your build process instead **transforms** your authored code into what
actually ships, for example by minifying it, bundling it with a tool such as
webpack or browserify, compiling it from another language such as
TypeScript, the packaged files are no longer reviewable on their own. In that
case, upload an archive of the original authored source (the source code
archive, or SCA) alongside build instructions the review team can follow to
reproduce the exact files you shipped.

.. note::

   Source code submissions take considerably longer to review than a
   standard XPI submission. Prefer the approach in :doc:`/guides/vendoring`
   wherever your project allows it, and use a source code submission only if
   your build genuinely needs to transform code.

Minification is not obfuscation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Minifying code (removing whitespace and shortening identifiers while keeping its
logic intact) is allowed as long as the original source is submitted alongside
it.

Obfuscating code (deliberately transforming it so its logic cannot be
followed) is not allowed, even when the original source is submitted
alongside it. An add-on that ships obfuscated code violates the add-on policy
and will be blocked.

What the review team needs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The review team rebuilds your extension from the submitted source to confirm
it produces the exact files you shipped, so write the instructions against a
plain, freshly installed environment rather than relying on tools, caches, or
configuration already present on your own machine. A ``README`` at the root
of the archive is the usual place to document this:

.. code-block:: markdown
   :caption: README.md

   ## Build environment

   - OS: Ubuntu 24.04
   - Node.js: 20.11.0
   - npm: 10.2.4

   ## Build steps

   npm ci
   npm run build

Alongside the ``README``, include:

- **Open-source, local tooling.** Every tool referenced by the build
  instructions can be installed and run locally. A build step that depends on
  a web-based service cannot be inspected or reproduced, so it cannot be
  accepted.
- **A lockfile.** ``package-lock.json`` or ``npm-shrinkwrap.json`` for npm,
  ``pnpm-lock.yaml`` for pnpm. A version range in ``package.json``, such as
  ``^1.2.3``, can resolve to a different release by the time the review team
  rebuilds your add-on, and the lockfile is what pins it down. The review
  team reproduces the install with ``npm ci`` or
  ``pnpm install --frozen-lockfile``.
- **A build script**, if you have one, so the commands documented in the
  ``README`` do not have to be run by hand.
- **No generated files.** Leave ``node_modules`` and your build output out of
  the archive. The review team recreates them from the lockfile, and shipping
  your own copies makes every regenerated file look like a change, which
  only causes confusion.

Keep the archive minimal
~~~~~~~~~~~~~~~~~~~~~~~~~

Every file in the archive is subject to review, so include only what the
build needs to produce the shipped add-on. From previous experience, test
files often fail the automated review and cause rejections, which could be
avoided by not including them. This applies beyond the test files
themselves: leave out test fixtures and the configuration for a test runner
too, since none of it ends up in the shipped add-on either.

Do not bundle a third-party library's source into the archive. Declare it as
a dependency in ``package.json`` instead, and let npm pull it in during the
build, the same way the review team's rebuild does. Resolving dependencies
this way, rather than including their source in the SCA, is the main point
of a source code submission, but it only works for widely used libraries the
review team can install from the public registry. Anything else, such as a
library that only lives in a private repository, is not widely used, or is
not published at all, has to be included in the archive directly.

Before you submit
~~~~~~~~~~~~~~~~~~

- The build tools are open-source and run locally, with no step depending on
  a web-based service.
- The ``README`` names the operating system and the exact tool versions used,
  with links to obtain them, plus the full command sequence to reproduce the
  build.
- The lockfile is included and matches the dependency versions you actually
  built with.
- ``node_modules`` and the build output are left out of the archive.
- Only widely used, publicly published libraries are declared as
  dependencies and pulled in via npm. Anything else, such as a private or
  unpublished library, is included in the archive directly.
- Test files, test fixtures, and test-only tooling are left out of the
  archive.
- The packaged add-on and the rebuilt output match: submit the source archive
  alongside the add-on, not instead of it.
