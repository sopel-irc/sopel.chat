---
title: "Sopel tutorial, Part 3: Memory and URL info functions"
migrated: true
source: wiki
previously:
  - /tutorials/part-4-memory-and-url-info-functions/
---

**NOTE: This guide is for Sopel 6.0+. If you are still using a version named
"Willie", we strongly encourage you to upgrade, as such old versions are no
longer supported.**

Communicating safely between modules can be very useful. Sopel provides for
this with the Memory system. The intended use is for when you have volatile
information which needs to be quickly and safely accessed and updated while the
bot is running. In this part of the guide, we're going to cover how to use it.

## Memory basics

The bot object that gets passed to callables has the attribute `memory`. This
is basically a Python dict with some added thread safety. True to form, though,
you don't need to worry about how that works. The only difference is that, if
you want to be thread safe (and you do), you should use the `contains` function
rather than the `in` keyword when checking if memory contains a given key. So
very simply, to see if a key is in memory you can just do 
`bot.memory.contains(key)`. If you want to access that key, you just do
`bot.memory[key]`. Keys can be any of the same things they can be in regular
Python dicts - numbers, strings, tuples, etc. - but they're usually strings.

### Sample use: Keeping track of the last URL

One frequent use of memory is to keep track of the last URL that was seen in a
channel. The bot currently ships with a `.title` command , found in `url.py`,
which will give the title or other URL information on the last URL posted in
the channel. The `url.py` module knows how to keep track of urls that other
people say, but what about when Sopel itself says a URL, like as the result of
the `.duck` command in `search.py`, which gives the first link from a
DuckDuckGo search of a given query? The answer is to put that link into memory.

What different memory keys exist and are used for is entirely by convention;
the API spells out no special rules here. However, one of the ones used by the
modules the bot ships with is `last_seen_url` which, as you'd expect, contains
the last seen URL. The key itself is a Python dict of channel names to the
last URL seen in that channel. So when the `.duck` command wants to update it,
it uses code like this:

```py
    if 'last_seen_url' not in bot.memory:
        bot.memory['last_seen_url'] = SopelMemory()
    bot.memory['last_seen_url'][trigger.sender] = url
```

Where `trigger.sender`, as you'll recall, is the channel (or nick, if a PM)
the message came from, and `url` is the result from the search. To make the bot
memory thread-safe, we use `SopelMemory` objects instead of normal dicts.

## URL info functions

One of the things Sopel supports is advanced URL information. For example,
Sopel can respond to a link to a YouTube video with not just the title, but
the uploader, the time it was uploaded, the duration, and more. Here's how
it works. We only need to see four lines of it to get the gist; the rest is
just retrieving the information from YouTube.

```py
@url(r"https?://(?:www\.)?(youtube\.com/watch\S*v=|youtu\.be/)([\w-]+)")
def ytinfo(bot, trigger, match):
    vid_id = match.group(2)
    #stuff
```
The first line gives Sopel a regex for URLs this function will handle - here
we match both youtube.com and youtu.be links. The second line will seem a
bit unusual compared to `@rule` and `@command` callables because of its third
argument. When Sopel is calling this function, it will provide the regular
expression match object in this third argument.

Want to learn about how to document (and test!) your module's commands?
[Continue to part 4!]({% link _tutorials/part-4-the-help-command.md %})
