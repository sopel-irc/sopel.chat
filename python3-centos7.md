---
layout: default
title: Using Python 3 on CentOS 7 (the easy way)
---

# Using Python 3 on CentOS 7 (the easy way)

Whether you're running Sopel, or any other Python application, the best way to
install Python 3 on CentOS 7 is with [Software Collection Libraries][scl]. Many
guides will tell you to compile it, but that's much more time consuming, makes
you mess with your path, and can't be kept up to date with `yum`. SCL is a
much more elegant solution, and all you need to do is this<sup>[1](#fnote-1)</sup>:

    yum install scl-utils
    wget https://www.softwarecollections.org/en/scls/rhscl/python33/epel-7-x86_64/download/rhscl-python33-epel-7-x86_64.noarch.rpm
    yum install rhscl-python33-*.noarch.rpm
    yum install python33
    easy_install pip

You can then enable it for a command by putting `scl enable python33` before
it. If you want to run your shell, do `scl enable python33 -- $SHELL`.
<sup>[2](#fnote-2)</sup> If you want the Python REPL,
`scl enable python33 -- python`.

`pip` is not included (outside of `virtualenv`, which *is* included). To
install it, do `easy_install pip` with the SCL active. Then, with it still
active, you can `pip install sopel` (or whatever other package you want).

## Using SCL in `systemd` services

If you're already familiar with `systemd`, it should be clear what to do.
Prepend all the commands in your unit file with
`/usr/bin/scl enable python33 --`. The `ExecStart` in
[Sopel's service file][service-example], when modified to use SCL, becomes
this:

    ExecStart=/usr/bin/scl enable python33 -- sopel -c /etc/sopel.cfg --quiet

---

<a id="fnote-1" />**1**: If you're looking to set this up on CentOS 6 or
Fedora, the URL for `wget` will be different. See [this page][python33-scl] for
the URL for your system.

<a id="fnote-2" />**2**: The `--` separates the arguments to SCL from your
command. If you aren't passing any arguments to your command, you can leave it
out. But the error message when you forget it isn't always straightforward, so
it's a good habit.

[scl]: https://www.softwarecollections.org/en/
[python33-scl]: https://www.softwarecollections.org/en/scls/rhscl/python33/
[service-example]: https://github.com/sople-irc/sopel/blob/master/contrib/sopel.service#L10
