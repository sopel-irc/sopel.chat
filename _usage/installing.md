---
title: Installing and running Sopel
migrated: true
source: wiki
order: -9100
previously:
  - /tutorials/part-1-installation/
---

**NOTE: This guide is for Sopel 6.0+. If you are still using a version named
"Willie", we highly encourage you to upgrade, as such old versions are no
longer supported.**

## Installing Sopel

The best way to get Sopel is to just `sudo pip install sopel` (leave out the
`sudo` on Windows). If you don't have pip already installed, you should follow
the instructions [here](https://pip.readthedocs.org/en/stable/installing/)
to do so. If you get an error, our [download page]({% link download.md %})
has more instructions.

### Creating a service

Sopel's source repository has example `systemd` unit files in [the `contrib`
folder]({{ site.repo }}/tree/master/contrib). Both single- (`sopel.service`)
and multi-instance (`sopel@.service`) examples exist.

## First run

> If you're running Sopel on Windows, replace all following occurrences of `sopel` with `python sopel.py`

To run Sopel, just type the command `sopel` in your terminal. The first time
you run Sopel, it will bring you through a quick setup wizard. Most of the
questions should be pretty straightforward. When you see something in square
brackets, that's the default setting, and you can just hit enter to keep it.
When asked for the channels to connect to, enter them separated by commas
(e.g. `#spam,#eggs,#cheese`) This wizard doesn't cover every option, only the
ones which are needed to get the bot running. The core config settings are all
[documented]({{ site.docs }}config.html#the-core-configuration-section),
if you want to make other tweaks.

Finally, it will ask you about configuration settings for modules. This will
automatically detect what modules you have available, and run their
configuration utility if they have one.

Your configuration file will be stored in `~/.sopel`. The file will be called
`default.cfg` by default. You can access the configuration wizard again by
running `sopel -w`. You can also get just the module options with
`sopel --configure-modules`. You can specify another configuration file with
`sopel -c filename`. This works both for the configuration utility and for
running the bot. This way, you can keep multiple different config files for
different networks, for example. You can see a list of all these options by
running `sopel -h` or `sopel --help`.

Once you've finished the configuration tool, Sopel will automatically start,
connect to the network, and join the channels you specified.

## Authentication

Most IRC networks have a service that allows you to authenticate yourself as
the owner of a username. This is configurable in Sopel with these settings:
[`auth_method`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_method),
[`auth_password`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_password),
[`auth_target`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_target),
and [`auth_username`]({{ site.docs }}config.html#sopel.config.core_section.CoreSection.auth_username).

----

Want to learn how to write modules for Sopel? [Continue to the tutorial!]({% link _tutorials/part-1-writing-modules.md %})

Just want to play around with your new IRC bot? [Read more usage articles!]({% link _usage/index.md %})
