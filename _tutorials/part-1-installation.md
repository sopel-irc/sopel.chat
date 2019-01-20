---
title: "Sopel tutorial, Part 1: Installation and first run"
migrated: true
source: wiki
---

**NOTE: This tutorial is being updated for 6.0. Most of it will work with 5.4.1
or above, but below 6.0 you may need to replace "sopel" with "willie" in some
places.**

This tutorial is intended to give you an overview of all the features Sopel
has to offer. In this part, we'll start by getting Sopel running, and then
make a simple Hello, world! complete with proper documentation. This guide
assumes you are running version 6.0 or higher of Sopel. (You can find this by
giving Sopel the `.version` command.)

This guide assumes you have at least some familiarity with programming. You
should know the basics of what functions are and stuff like that. Since Sopel
is written in Python, knowing Python will help, but if you've worked with
most other languages you should be able to infer enough from the examples to
get things done.

While this guide does cover a lot of what is available, there is much more than
can be described here. The API documentation is available [online]({{ site.docs }}),
and serves as a useful reference.

## Installing

The best way to get Sopel is to just `sudo pip install sopel` (leave out the
`sudo` on Windows). If you don't have pip already installed, you should follow
the instructions [here](https://pip.readthedocs.org/en/stable/installing/)
to do so. If you get an error, our [download page]({% link download.md %})
has more instructions.

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

Want to learn how to write modules for Sopel? [Continue to part 2!]({% link _tutorials/part-2-writing-modules.md %})