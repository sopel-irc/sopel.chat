---
layout: default
title: Sopel - The Python IRC Bot
---

# Installation
## From Linux repositories (Fedora, Arch)
The easiest way to install Sopel is from the package repositories.

For Fedora, just run `sudo yum install willie` in a terminal.

On Arch, Sopel is available in the AUR.

## From PyPI
Installing from PyPI is the next best way to install Sopel, since it'll handle
installing all of the extra stuff you need to run all of the modules properly.

Sopel works on both Python 2 and Python 3. If you're planning on using Python
3 with CentOS, you may want to see [this guide](/python3-centos7.html) on
getting that set up easily.

You will need to have pip installed. On Debian and Ubuntu, you can do this by
running `sudo apt-get install python-pip` in a terminal. For OSX and Windows,
follow PIP's setup instructions
[here](http://pip.readthedocs.org/en/latest/installing.html).

Once you have pip set up, just do `sudo pip install willie`. If you get an
error about lxml (or, probably, any other big messy looking error), it's
beacuse `pip` is having problems installing `lxml`, which some modules depend
on. You're best off installing `python-lxml` from your package repos and trying
again. If you can't for some reason (you're using a virtualenv or alternate
python, you don't have root access, you're on Windows), follow their
instructions [here](http://lxml.de/installation.html).

## Manual installation
The latest version of Sopel is available
[here](https://github.com/embolalia/willie/releases/latest). Download it, and
run `python setup.py install`. You will need to download all of Sopel's
dependencies and install them manually as well. These can be found on the
[Python Package Index](https://pypi.python.org/pypi). The only one that's
needed for the bot itself to work is
[backports.ssl\_match\_hostname](https://pypi.python.org/pypi/backports.ssl_match_hostname/3.4.0.2)
Other things are needed for modules to work properly. If you get errors about
being unable to import modules when you start the bot, search for them on PyPI.
