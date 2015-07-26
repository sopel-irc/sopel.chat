---
layout: default
title: Sopel - The Python IRC Bot
---

# Introduction

<span class="Sopel">Sopel</span> is a simple, easy-to-use, open-source IRC
utility bot, written in [Python](http://python.org). It's designed to be easy
to use, easy to run, and easy to make new features for.

<span class="Sopel">Sopel</span> comes with a ton of ready-made features for
you to use. It can leave notes for people, give you reminders, and
[much more](https://github.com/sopel-irc/sopel/wiki/Commands).

<span class="Sopel">Sopel</span> also comes with a
[fully-documented](/docs) and
easy-to-use API, so you can write your own features. There's also an
[easy tutorial](https://github.com/sopel-irc/sopel/wiki/Sopel-tutorial,-Part-1)
you can follow along with, to help you learn.

Developing for <span class="Sopel">Sopel</span> is a great way to familiarize
yourself with Python. It's easy to start, but there's no limit to the cool
things you can do with it.

<span class="Sopel">Sopel</span> is available on the
[Python Package Index](http://pypi.python.org/pypi/willie/)
([6.0 alpha](http://pypi.python.org/pypi/sopel)), and in a
[tarball](https://github.com/sopel-irc/sopel/releases/latest).

# Features

* Fully documented API for writing new modules
* SSL Support
* [IRCv3](http://ircv3.org) support, with SASL authentication
* Easy quickstart wizard
* Dynamic topic support using topic masks
* Numerous modules: Wikipedia, Reddit, Bugzilla, unit conversion, and more
* Support for remembering timezone, weather location, and other information for
users
* Persistent user and channel settings database using SQLite
* Ability to easily run as a daemon
* Safe asynchronous inter-module communication
* And much, much more

# Project History

[Sean Palmer](http://inamidst.com/) was the original creator of the bot, which
he called phenny.

[Michael Yanovich](https://yanovich.net) improved it, and changed the name to
[jenni](https://github.com/myano/jenni/).

[Embolalia](https://embolalia.com) improved it even more, with a lot of
help from [Dimitri Molenaars](http://tyrope.nl/index.php?lang=EN) and
[Elad Alfassa](http://eladalfassa.com), and renamed it to Willie, and later
Sopel. This is the current and most advanced version of the bot.

A number of other people have helped out along the way, and they can be seen in
the [CREDITS](https://github.com/sopel-irc/sopel/blob/master/CREDITS) file in
Sopel's source code.

# Frequently Asked Questions

<ul class="faq">
<li class="q">Where can I report a problem with Sopel?</li>

<li class="a">You can file a ticket in our <a
href="https://github.com/sopel-irc/sopel/issues">GitHub issue tracker</a>, or
join the developers Embolalia, Tyrope, and elad in 
<a href="irc://irc.freenode.net/#sopel">#sopel</a> on Freenode.</li>

<li class="q">Is there somewhere I can go to find modules other people have
written for Sopel?</li>

<li class="a">Starting in <a href="/willie_6.html">Sopel 6</a>, you'll be able
to just search PyPI for "sopel_modules". In the mean time, the closest we have is
<a href="https://github.com/sopel-irc/sopel-extras">sopel-extras</a>.</li>

<li class="q">Will Phenny/jenni modules work with Sopel?</li>

<li class="a">Probably. There are a small number of features in the older
versions which are implemented differently in Sopel. The vast majority of
modules should work without problems, though.</li>

<li class="q">Can I use Sopel with Docker?</li>

<li class="a">Probably, but there's not much reason to. We only provide support
for one version of Sopel at a time, and it already supports running multiple
instances side-by-side. If you really need to containerize dependencies,
virtualenv is a lot easier.</li>

<li class="q">Does Sopel work on Google App Engine?</li>

<li class="a">Probably not. App Engine doesn't currently do sqlite, which
Sopel requires for its database.</li>

<li class="q">Does Sopel run on OSX? Windows? PyPy? Jython?</li>

<li class="a">Probably, probably, probably, probably. Sopel itself is pure
Python (though some included modules have dependencies that aren't, like lxml),
and an effort is made to be as platform-independant as possible. That said,
most of the development is done on Linux, so some platform-specific bugs may be
missed. If you do run into a bug, be sure to report it, because otherwise we
won't know about it.</li>

<li class="q">How do I make Sopel give me ops when I enter a channel?</li>

<li class="a">You should use your network's services to do this. If you're on a
network like EFnet which doesn't have services, you can write a module to make
Sopel do it. Sopel will never be as good at it as network services, though,
so we don't include that functionality in our default set of modules.</li>

<li class="q">Why is Sopel saying <code>...</code>?</li>

<li class="a">Sopel is built to avoid being spammy as much as possible, so it
keeps track of the last few things its said. If too many of those last few
things are the same, it says <code>...</code> a few times instead of repeating
itself (and then stops trying to say that thing entirely, until its said some
other things). Usually, this happens because someone is spamming the same
command over and over, or something is just broken. It doesn't keep the bot
from saying anything else, and it can say the same thing as often as you want,
as long as it says some other stuff, too.</li>
</ul>
