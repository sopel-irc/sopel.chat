---
title: Installing and running Sopel
order: -9100
previously:
  - /tutorials/part-1-installation/
  - /download.html
---

## Installing Sopel

Sopel 7 requires Python 2.7, or Python 3.3+. Sopel 8 will require Python 3.7 or
newer.

**The recommended way to install Sopel is using `pip`.** Your distro may have a
package available, but these are not maintained by the Sopel team, and are
[often out of date](https://repology.org/project/sopel/versions).
- Alpine: [sopel](https://pkgs.alpinelinux.org/packages?name=sopel)
- Arch and derivatives:
  [community/sopel](https://archlinux.org/packages/community/any/sopel/)
  [aur/sopel-git](https://aur.archlinux.org/packages/sopel-git)
- Debian: Install with `pip`, the
  [packages](https://packages.debian.org/search?keywords=sopel) are extremely
  out of date.
- NixOS: `python3.10-sopel`
- Ubuntu: Install with `pip`, the
  [packages](https://packages.ubuntu.com/search?keywords=sopel) are extremely
  out of date.

If you want to use Python 3 on CentOS, you may want to see [this guide]({% link
_appendices/using-python-3-on-centos-7.md %}) on getting that set up easily.


### Recommended installation

#### Installing pip

Pip is often automatically installed alongside Python, but if it isn't, you'll
need to install it yourself. On most distributions you can just install the
`python-pip` package, e.g. `sudo apt install python-pip`.
For macOS and Windows, follow the `pip`
[setup instructions](https://pip.readthedocs.org/en/latest/installing/).

#### Installing Sopel

To install or update Sopel system-wide, you can usually just run
`sudo pip install --upgrade sopel` – or on windows, just
`pip install --upgrade sopel`.

If you prefer to install it in a
[virtualenv](https://docs.python.org/3/library/venv.html), first create it with
`python3 -m venv path/to/sopel/venv`. Every time you open your terminal,
before running `sopel` commands you must activate the virtualenv by running
`source path/to/sopel/venv`. You can then run `pip install --upgrade sopel`
to install or upgrade Sopel and its dependencies.

Don't forget to check the [upgrade notes](#upgrading) before upgrading!

Once the `sopel` package is installed, see below for how to
[configure](#configuring) the bot and have it start automatically as a
[service](#creating-a-service).


### Installing from source

First, follow the above instructions to [install `pip`](#installing-pip)
if necessary, and create and activate a virtualenv if you prefer.

Next, you'll need the source code. You can get this by downloading and
extracting a tarball from the [releases page]({{ site.repo }}/releases/latest)
on the Sopel GitHub, or by cloning the repository with
`git clone https://github.com/sopel-irc/sopel.git`.

You can then run `pip install --upgrade --editable path/to/sopel`.
This will install all of Sopel's dependencies and create an
["editable" installation](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs),
which allows you to make and test changes to Sopel's source code without having
to reinstall it with `pip` each time.

To update installations from source, you will need to either download a new
tarball or use git to fetch updates.


### Upgrading

If you already have an older version of Sopel (or Willie) installed, and want
to upgrade to the newest version, you should consult the migration guides.

{% assign ups = site.upgrading | sort: "covers_to"
  %}{% for up in ups %}{%
    unless up.covers_to and up.covers_from %}{%
      continue %}{% comment %} Skips guides that aren't ready {% endcomment %}{%
    endunless %}{%
    assign from_name = "Sopel" %}{%
    assign to_name = "Sopel" %}{%
    assign covers_from = up.covers_from | plus: 0 %}{%
    assign covers_to = up.covers_to | plus: 0 %}{%
    if covers_from < 6.0 %}{% assign from_name = "Willie" %}{% endif
    %}{%
    if covers_to < 6.0 %}{% assign to_name = "Willie" %}{% endif
%}  * [Upgrading from {{ from_name }} {{ up.covers_from }} to {{ to_name }} {{ up.covers_to }}]({{ up.url }})
{% endfor %}

You might need to read more than one if your existing Sopel instance is old
enough. Each guide only covers migrating from the previous major version. So
for example, if you still have Willie 4 running, and you want to get Sopel 6,
you should read the Willie 5 migration guide (covers going from 4 to 5) _and_
the Sopel 6 migration guide (covers going from 5 to 6).

Once you're aware of any changes you may need to make for major upgrades, you
can use the instructions in the
[Recommended installation](#installing-sopel) or
[Installing from source](#installing-from-source) sections to install the
updates.


## Configuring

> If you're running Sopel on Windows, replace all following occurrences of `sopel` with `python sopel.py`

To run Sopel, just type the command `sopel` in your terminal. The first time
you run Sopel, it will bring you through a quick setup wizard. Most of the
questions should be pretty straightforward. When you see something in square
brackets, that's the default setting, and you can just hit enter to keep it.
When asked for a list of items like which channels to connect to, enter one
per line, then an empty line when you're done. This wizard doesn't cover every
option, only the ones which are needed to get the bot running. The core config
settings are all [documented]({{ site.docs }}config.html#the-core-configuration-section),
if you want to make other tweaks in the config file.

Finally, it will ask you about configuration settings for plugins. This will
automatically detect what plugins you have available, and run their
configuration utility if they have one.

By default, your configuration file will be stored as `~/.sopel/default.cfg`.
You can change this with the `-c` flag, e.g. `sopel -c other/config.cfg` or
`sopel configure -c oftc.cfg`. This allows you to easily keep multiple config
files for running multiple bots, for example on different networks.
You can access the configuration wizard again by running `sopel configure`,
or configure only plugins with `sopel configure --plugins`.
You can get a list of all available options by running `sopel --help`.

Once you're done configuring Sopel, you can start it by running the command
`sopel`.


## Creating a service

Configuring a service for Sopel is optional, but makes it easy to have the bot
start automatically.

In the [`contrib` folder]({{ site.repo }}/tree/master/contrib) of Sopel's
source repository are several example files to help with this.

For distros using systemd, there are examples for both single-instance
(`sopel.service`) and multi-instance (`sopel@.service`) setups.
To use one, edit it if necessary, then copy it to `/etc/systemd/system/`,
run `sudo systemctl daemon-reload`, and enable/start the service
(`sudo systemctl enable --now sopel.service` or `sopel@myconfig.service`).

If you are using a virtualenv, the `sopel` program will be e.g.
`your/venv/bin/sopel`.

If you create a script or configuration file to run Sopel under another init
system, feel free to submit it to [the repo]({{ site.repo }}) for other users'
convenience.


## Adding plugins

The easiest place to put new plugins is in `~/.sopel/plugins`. Simply create
this directory if it does not exist, and drop `.py` plugin files into it.
Sopel will auto-load them unless [configured otherwise][config-plugins].

Plugin authors might also publish their works as packages; you can find them
[by searching PyPI](https://pypi.org/search/?q=%22sopel%22), or by using your
favorite search engine to search for e.g. "sopel weather plugin".

Of course, you can also write your own custom plugins! Check out the
[plugin development overview]({% link docs/plugin.html %}) and Sopel's
[API documentation][docs-plugin] to get started.

  [config-plugins]: /docs/configuration.html#plugins
  [docs-plugin]: /docs/plugin.html


## Authentication

Most IRC networks have a service that allows you to authenticate yourself as
the owner of a username. This is configurable in Sopel with these settings:
[`auth_method`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_method),
[`auth_password`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_password),
[`auth_target`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_target),
and [`auth_username`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_username).
