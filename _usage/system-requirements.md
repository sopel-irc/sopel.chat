---
title: System requirements
migrated: true
source: wiki
order: -9999
---

Sopel is designed to run with Python 2.7 or 3.3+. (**Note:** The next major version, Sopel 8, will require Python 3.6+.)

While all development and "official" tests run on Linux, Sopel should probably work in other POSIX-compliant OSes, and seems to more-or-less work on Windows.

Sopel itself has few external dependencies, besides Python. There are a couple, though:

* [dnspython](https://github.com/rthalley/dnspython) - used internally to enhance connection reliability
* [requests](https://github.com/requests/requests) - used to maintain compatibility with old plugins that use deprecated features of Sopel's `web` utility API
* [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) - used for database cross-compatibility (SQLite, MySQL, PostgreSQL, etc.)

Most of Sopel's dependencies are only needed for specific plugins. Below is a listing of some of these. If you don't want to use a specific plugin, you do not need its dependencies.

* [geoip2](https://github.com/maxmind/GeoIP2-python) - ip. You will also need the appropriate database files, which Sopel will download automatically if they are not found.
* [ipaddress](https://github.com/phihag/ipaddress) - url (only needed on Python 2)
* [praw](https://github.com/praw-dev/praw) - reddit
* [pytz](https://launchpad.net/pytz) - remind, clock, seen, tell
* [requests](https://github.com/requests/requests) - used by nearly every plugin that needs to talk to a web service. This includes both built-in and third-party plugins; you probably should just install this one.
* [xmltodict](https://github.com/martinblech/xmltodict) - bugzilla, search

Most of these packages can be installed through the `pip` command, or via your Linux distribution's software repository. If you install Sopel through `pip` or your distribution's package manager (on Fedora or Arch), all of these dependencies will be installed for you.
