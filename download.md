---
layout: default
title: Download / Install
---

# Installation
## From PyPI
Installing from PyPI is the best way to install Sopel, since it'll handle
installing all of the extra stuff you need to run all of the modules properly.

Sopel works on both Python 2 and Python 3. If you're planning on using Python
3 with CentOS, you may want to see [this guide](/python3-centos7.html) on
getting that set up easily.

You will need to have `pip` installed. On Debian and Ubuntu, you can do this by
running `sudo apt-get install python-pip` in a terminal. For macOS and Windows,
follow the `pip` setup instructions
[here](https://pip.readthedocs.org/en/latest/installing/).

Once you have `pip` set up, just do `sudo pip install sopel`.

## Manual installation
The latest version of Sopel is available
[here](https://github.com/sopel-irc/sopel/releases/latest). Download it, and
run `python setup.py install`. You will need to download all of Sopel's
dependencies and install them manually as well. These can be found on the
[Python Package Index](https://pypi.org/). The only one that's
needed for the bot itself to work is
[backports.ssl\_match\_hostname](https://pypi.python.org/pypi/backports.ssl_match_hostname/3.4.0.2).
Other things are needed for modules to work properly. If you get errors about
being unable to import modules when you start the bot, search for them on PyPI.
