# Updating automatically generated pages

Some of the website pages are automatically generated using the
[document_sopel_modules.py](document_sopel_modules.py) script in the root of
this repository. These pages are the [command list](_usage/commands.md) and the
[module configuration](_usage/module-configuration.md) list.

Generally, these pages should be updated after a new version of Sopel releases.
This is how to do it. You will need local clones of sopel-irc/sopel-website
(this repo) & sopel-irc/sopel (Sopel itself), and a reasonably current version
of `sopel` installed globally on your system.

The script is very old. It has been updated to mostly-working condition, but it
cannot document module configuration options any more due to changes in how the
standard `configure()` method works. This function would be nice to have back,
of course, so any help fixing it for current module code is much appreciated!

## Quick guide

Preferably, this script should be run under a version of Python 3 that
Sopel supports. If your `python` points to an old version, substitute `python3`
or whatever name is appropriate for your system.

The script expects that `sopel` is at least installed globally, even if the
installed version is not the latest release, so that it can open module files.

From the root of `sopel-website`, run the following command:

    python document_sopel_modules.py

If Sopel's code is not stored in (from this repo's perspective) `../sopel`, use
the `--sopel` argument like so:

    python document_sopel_modules.py --sopel=/path/to/sopel/repo
