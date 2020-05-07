---
title: "Sopel tutorial, Part 5: Folders, packages, and PyPI"
previously:
  - /tutorials/part-6-packaging-and-distributing-modules/
  - /tutorials/part-5-packaging-and-distributing-modules/
---

**NOTE: This guide is for Sopel 6.0+. If you are still using a version named
"Willie", we strongly encourage you to upgrade, as such old versions are no
longer supported.**

The [Python Package Index (PyPI)](https://pypi.org/) makes it easy to share
your Sopel plugins and use plugins written by other people. Even if you aren't
sharing your plugin, you might want to break it into multiple files to keep the
code organized as the plugin's complexity increases.

Sopel supports three kinds of multi-file plugin:

* a folder (6.0+)
* a namespace package (6.0+)
* an entry point (7.0+)

Which one you choose is mostly down to preference, and whether you want to
publish your plugin on PyPI. A folder plugin can't "just work" when installed
from PyPI (Sopel won't be able to find it), but the other two types can.

The main drawback to multi-file plugins is that Sopel can't reload them
properly. However, you should know a secret: Sopel's `.reload` command is kind
of a lie, because Python's `reload()` function is kind of a lie. There's a
_ton_ of stuff that Python doesn't update when "reloading" a module. Sopel
_pretends_ to reload single-file plugins so it's easier to get started writing
them, but the charade starts to crumble if anything is renamed—and it _really_
falls apart once you have multiple files. (Sopel will _pretend_ to reload a
multi-file plugin, too—but only the main file, if even that.)

So, once you make the jump from a single file to one of these multi-file
structures, you'll probably want to move plugin development to a dedicated test
bot (and test channel/network) where quitting and restarting the bot to debug
code changes won't bother anyone.

## Folder plugins
<div class="sidebar-note">Supported in Sopel 6.0+</div>

Putting your plugin in a folder is simple, especially if you're already
familiar with how Python modules work. Let's say you've been working with
`~/.sopel/plugins/spam.py`. All you have to do is move it to
`~/.sopel/plugins/spam/__init__.py`. Of course, you probably want to split it
out from that file a bit.

The first thing you want to do is put `from __future__ import absolute_import`
at the top of your `__init__.py`, and any other Python files you have in here.
If you're only going to use this plugin with Python 3, this isn't necessary,
but it clears up some weirdness with how imports work in Python 2.

You can split anything out to anywhere you want. The only rule is that the
things that the bot is searching for (basically, just the things that you're
decorating with the decorators in `sopel.module`) need to be present in that
`__init__.py`. So if you had a callable `eggs` in there, and you move it into
`~/.sopel/plugins/spam/callables.py`, you'll want to have `from .callables
import eggs` (note the leading `.` that indicates the `callables` module is in
the same directory). It's worth noting that you won't be able to import things
from `__init__.py` in other files in the directory reliably, so it's probably
best to have `__init__.py` do nothing but import the things it needs.

## Namespace package plugins
<div class="sidebar-note">Supported in Sopel 6.0+</div>

A namespace package is very similar to a folder plugin, but it can be shared on
PyPI and "just works" when installed: Sopel looks for modules in the
`sopel_modules.*` namespace and loads them as plugins.

The easiest way to create one of these is to [use the cookiecutter
template](#using-the-cookiecutter-template).

## Entry point plugins
<div class="sidebar-note">Supported in Sopel 7.0+</div>

Inspired by other plugin-supporting projects like `flake8` and `pytest`, Sopel
7.0 added the ability to specify plugins as [`setuptools` entry
points](https://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins).
These can be shared on PyPI and will be discovered automatically when Sopel
starts. They also have the unique advantage of allowing you to distribute
multiple plugins in the same package—each entry point is a separate plugin.

Here, too, the easiest way to get started is [with the cookiecutter
template](#using-the-cookiecutter-template).

## Using the cookiecutter template

Our [cookiecutter template](https://github.com/sopel-irc/cookiecutter-sopel) is
a quick way to get the skeleton of a plugin. It's easy:

```sh
pip install cookiecutter
# for the entry point style
cookiecutter gh:sopel-irc/cookiecutter-sopel
# for the namespace plugin style
cookiecutter gh:sopel-irc/cookiecutter-sopel -c sopel_modules
```

Answer all the prompts, and you'll have a ready-made repo structure to plop
your plugin into.
