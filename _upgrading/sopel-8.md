---
title: Sopel 8.0 Migration
covers_from: 7.x
covers_to: 8.0
---

# Sopel 8.0 Migration

Version 8.0 brings Sopel into the modern era of Python, finally dropping support
for [end-of-life](python-devguide-versions) Python releases as of December 2023,
including Python 2 and several older versions of Python 3. This allows us to make
significant improvements under the hood that were held back by these legacy
versions, e.g. the IRC connection backend and Sopel's event system.

  [python-devguide-versions]: https://devguide.python.org/versions/

## Owner/admin usage changes

### Updated Python requirements & support policy

Sopel 8.0 requires Python 3.8 or higher. Support for Python 2.7 and 3.3–3.7 has
been removed. In exchange, known issues sometimes preventing use of Sopel 7 with
Python 3.11+ have been fixed.

During the lifecycle of Sopel 8.x, we will do our best to test against new
Python releases as they come. We will continue to test against Python versions
that reach end-of-life unless it becomes impractical to do so—in which case the
next maintenance release of Sopel will officially drop support for the Python
version(s) that can no longer be tested.

### CLI changes

Sopel 8 continues the command-line interface overhaul we began in version 7,
mostly in the form of removing support for legacy usage from Sopel's 6.x era.

The bare `sopel` command now offers only basic control. Most of its legacy
options have been removed:

|             Legacy command            |             Modern command             |
|:-------------------------------------:|:--------------------------------------:|
| `sopel --quit` or `sopel -q`          | `sopel stop`                           |
| `sopel --kill` or `sopel -k`          | `sopel stop --kill` or `sopel stop -k` |
| `sopel --restart` or `sopel -r`       | `sopel restart`                        |
| `sopel --configure-all` or `sopel -w` | `sopel configure`                      |
| `sopel --configure-modules`           | `sopel configure --plugins`            |
| `sopel --list` or `sopel -l`          | `sopel-config list`                    |
| `sopel -v`                            | `sopel -V` / `sopel --version`         |
| `sopel --quiet`                       | n/a; this feature didn't work anyway   |

### Ignore system

In Sopel 8, "hostmask" blocks are now called "host" blocks, which reflects the
reality of how those values are used by Sopel. Bot admins' muscle memories will
have to learn to type e.g. `.blocks add host` instead of `.blocks add hostmask`.

We intend to add [actual "hostmask" blocking][better-ignore-system] in a future
Sopel release.

_Note that the **config file** option for "hostmask" blocks already was, and
still is, named `host_blocks`. This change only affects interactive blocklist
editing by bot admins via IRC commands._

  [better-ignore-system]: https://github.com/sopel-irc/sopel/issues/1355

### Configuration & plugin-handling changes

#### What's a "module", doc?

Sopel 8 no longer loads plugins from the `<homedir>/modules` directory by default.
To migrate, rename this directory to `plugins` or declare it in the `extra` field of
[the `[core]` configuration section][core-section-plugins].

This is part of our efforts to clarify the difference between a "module" (which is a
[Python concept][py-module]) and a "plugin" (which is a special kind of "module" that
can extend Sopel with new functionality).

  [core-section-plugins]: https://sopel.chat/docs/run/configuration.html#plugins
  [py-module]: https://docs.python.org/3/glossary.html#term-module

#### Encrypted IRC by default

Unless its config file specifies different values, Sopel 8 assumes that it
_should_ `use_ssl` and connect to the standard encrypted `port` 6697.

Older versions assumed they should _not_ `use_ssl` and use `port` 6667.

#### Taming logging to a channel

`DEBUG` is no longer a valid choice for the `logging_channel_level` setting, and
`logging_channel_level` is no longer inherited from the main `logging_level`
setting. The new default `logging_channel_level` is `WARNING`.

Having Sopel output its log messages to an IRC channel of your choice can be
convenient, but if `DEBUG` logs could be sent to IRC, it was possible to have
Sopel give you _too much of a good thing_ and get stuck. Every debug message
sent to IRC would itself generate multiple additional debug log entries, filling
the bot's outbound message queue—and the best solution to prevent deadlocks is
to simply prohibit `DEBUG` from being used with `logging_channel_level`.

#### Farewell, Phenny/Jenni

The project that eventually became Sopel diverged from Jenni in 2012. After more
than a decade of maintaining backward compatibility (in a theoretical sense, at
least) with plugins originally written for Jenni and its predecessor Phenny,
Sopel 8.0 bids a fond farewell to plugin code from that era.

Beyond the maintenance burden of making sure Sopel could still _technically_
load such old plugins, we felt it was disingenuous to continue "supporting" them
when the rest of Sopel's API has changed and evolved so much that the chance of
such old plugins _actually still working_ is now very low indeed. Thus, we're
not _dropping_ support for those decade-old plugins as much as _admitting that
things have changed a lot_ and users would be better off seeking (or if
necessary, writing) newer plugins with similar functionality.


## Sopel 8 plugin changes

### Removed built-in plugins

Sopel's built-in plugins are slowly being migrated out to their own standalone
packages. In 8.0, we say farewell to:

* `help`: now published as [`sopel-help`][sopel-help]
  * Note: Sopel still requires the `sopel-help` package, so it will be installed
    and available automatically.
* `ip`: now published as [`sopel-iplookup`][sopel-iplookup]
* `meetbot`: now published as [`sopel-meetbot`][sopel-meetbot]
* `py`: now published as [`sopel-py`][sopel-py]
* `reddit`: now published as [`sopel-reddit`][sopel-reddit]
* `remind`: now published as [`sopel-remind`][sopel-remind]

Over the longer term, this will help the Sopel project manage plugin maintenance
and updates more quickly.

  [sopel-help]: https://pypi.org/project/sopel-help/
  [sopel-iplookup]: https://pypi.org/project/sopel-iplookup/
  [sopel-meetbot]: https://pypi.org/project/sopel-meetbot/
  [sopel-py]: https://pypi.org/project/sopel-py/
  [sopel-reddit]: https://pypi.org/project/sopel-reddit/
  [sopel-remind]: https://pypi.org/project/sopel-remind/

### Notable changes to built-in plugins

#### `currency` plugin

The `fiat_provider` setting now takes precedence over the `fixer_io_key`.
Previously, setting a `fixer_io_key` would use the `fixer.io` fiat exchange rate
provider regardless of the `fiat_provider` setting.

`exchangerate.host` is no longer a valid `fiat_provider` choice; it has been
replaced by the new default, `open.er-api.com`.

#### `reload` plugin

The `.update` command has been removed from the `reload` plugin. It relied on
running Sopel in a way that we don't officially support, so we chose to remove
the command.

To replace `.update`, if you were using it, we recommend writing an external
script that [stops Sopel][cli-stop], updates the components you want, and then
[starts Sopel][cli-start] again.

  [cli-stop]: https://sopel.chat/docs/run/cli.html#sopel-stop
  [cli-start]: https://sopel.chat/docs/run/cli.html#sopel-start

#### `wikipedia` plugin

The old command names (`.w`, `.wik`, and `.wiki`) are no longer used; they were
freed up for use by bespoke plugins. `wikipedia` functionality is now invoked by
the `.wikipedia` command, or `.wp` for short.

The deprecated `lang_per_channel` config-file setting has been removed. Chanops
and Sopel admins can set the preferred wiki language for a channel using the
`.wpclang` command instead.


## Sopel 8 API changes

Changes that could be particularly surprising are marked with a ⚠️ emoji.

### ⚠️ Command names are now literal

Sopel 8 no longer supports regular expressions in command names, which are now
[escaped][re.escape] during plugin loading. This change helps plugin developers
avoid unintentional interference with the default capture groups for commands,
and also clears the way for enhancements to plugin/command management.

Notes in the [documentation for `@sopel.plugin.command()`][command-decorator]
list possible Sopel 8-compatible adaptations for a few common use cases.

  [command-decorator]: https://sopel.chat/docs/plugin/decorators.html#sopel.plugin.command
  [re.escape]: https://docs.python.org/3.11/library/re.html#re.escape

### ⚠️ Time-handling changes

`trigger.time` is now an ["aware" `datetime` object][py-aware], meaning it has a
UTC offset associated with it. Comparison or arithmetic operations between
"aware" and "naïve" `datetime` objects are not allowed; code that manipulates
`trigger.time` values will need to make sure "naïve" `datetime` objects created,
or retrieved from sources, outside the bot are converted to "aware" values.

  [py-aware]: https://docs.python.org/3.11/library/datetime.html#aware-and-naive-objects

The fallback format string used by `sopel.tools.time.format_time()` changed from
outputting the timezone name (`UTC`) to the UTC offset (`+0000`). This format
string is used only if there is no preferred format set for the nick, channel,
_and/or_ config passed to the function.

`format_time()`'s handling of "aware" and "naïve" `datetime`s was also improved,
but those changes should be transparent to both users and plugin developers. Let
us know if you encounter situations where `format_time()` behaves surprisingly.

`sopel.tools.time.validate_timezone()` now also raises a `ValueError` even if
the timezone to be validated is `None`. This was previously a special case that
_returned_ `None`.

### Enums everywhere

_(Insert the classic Buzz Lightyear meme here, if you want.)_

The following parts of Sopel's API each became an enumeration of some kind:

* `sopel.formatting.colors`
  * Class members' names and values remain unchanged
* `sopel.tools.events`
  * Class members' names and values remain unchanged
* `sopel.plugin.OP`, `sopel.plugin.VOICE`, etc.
  * These constants became shortcuts to equivalent members of a new
    `sopel.privileges.AccessLevel` enumeration
  * The old constants are **not** deprecated until we are closer to releasing
    improved API features around channel access

Now that Sopel is squarely in the Python 3 world, using `Enum`s where they make
sense will let us gradually improve how some parts of its API fit together in
the long run.

None of these changes are expected to require any immediate code updates for
correct _function_. However, code updates _might_ be required in projects that
make use of type-checking.

### Identifier casemapping

Any reasonably modern IRC server advertises its method for normalizing nicknames
to every client that connects. Sopel 8 builds on the `bot.isupport` mechanism
added in Sopel 7 and makes use of the advertised `CASEMAPPING` value when
comparing and normalizing nicknames itself.

To support handling this under the hood, the bot's `config.core.nick` setting is
now stored and returned as a normal `str`. It and any other strings that you'd
like to treat as nicknames should be passed through the `bot.make_identifier()`
method to get the same `Identifier` type you're used to from Sopel 7, configured
to use the IRC server's advertised casemapping method.

### Database changes

`bot.db.get_nick_id()` no longer creates a new ID by default if its `create`
parameter is unspecified.

Plugin code doesn't usually need to use this method. But if you do use it,
you'll possibly need to handle a new `ValueError` exception when calling this
method on a nick that hasn't yet been assigned an ID.

### IRC event changes

The event names `RPL_INVITELIST` and `RPL_ENDOFINVITELIST` have been updated per
[clarifications][invitelist-madness] from the "Modern IRC" living-specification project.
`RPL_INVEXLIST` and `RPL_ENDOFINVEXLIST` were added to the list of named events
that Sopel knows about.

Plugin code might need to be updated as a result of these changes, but keep in
mind that [different IRC servers mean different things][invitelist-warning] when
they send these events. If in doubt, specify a raw numeric value (e.g. `'346'`).
Writing truly cross-network plugins that react to these events should be
undertaken _very_ carefully.

  [invitelist-madness]: https://github.com/ircdocs/modern-irc/issues/42
  [invitelist-warning]: https://modern.ircdocs.horse/#invite-list

### IRC connection status monitoring

`bot.connection_registered` now indicates that a _connection_ is open, the 
IRC server has _accepted_ the bot as a client, and the bot can _send commands_.
Previously, this boolean value indicated only that a connection was open.

This is useful to plugins with code that runs without a triggering IRC event but
still outputs to IRC, such as a `@sopel.plugin.interval()` job or acting on data
received [via a socket][sopel-sockmsg]. `if not bot.connection_registered`, the
output can be skipped, retried after a delay, etc.

  [sopel-sockmsg]: https://github.com/dgw/sopel-sockmsg

### More consistent `trigger` objects

#### ⚠️ `STATUSMSG` handling

Events sent to a channel can be scoped to users with a particular privilege
level, or _status_, in that channel. IRC servers advertise the availability of
this feature using the `STATUSMSG` token in `RPL_ISUPPORT`.

In Sopel 7, `trigger.sender` included the status prefix, and it was difficult
for plugins to detect and remove it themselves if so desired. Sopel 8.0 removes
the status prefix from `trigger.sender` and leaves only the channel name, while
the status prefix (if any) is exposed as `trigger.status_prefix`. This change is
useful, for example, to plugins that use `trigger.sender` to store or retrieve
_channel values_ in `bot.db`.

The `bot` passed to a plugin callable triggered by an IRC event automatically
includes the status prefix, if present, in the default `destination` parameter
to methods that send a _message_ to IRC. Plugin callables that simply invoke
`bot.say()`, `bot.reply()`, etc. in direct response to a `trigger` and without
overriding the default `destination` will most likely get the expected behavior.

[`sopel-remind`][sopel-remind] is an example of one kind of plugin that this
change [might surprise][remind-statusmg]. Naïve implementation of such a feature
might simply store `(trigger.nick, trigger.sender, parsed_message)` and send
`bot.reply(parsed_message, trigger.sender, trigger.nick)` after the specified
amount of time has passed. The `trigger.status_prefix` is lost, and the reminder
will be sent to the entire channel instead of only the status-limited subset of
users who could have seen the original command.

  [remind-statusmsg]: https://github.com/sopel-irc/sopel-remind/issues/10

#### Only set the `sender` when it makes sense

Sopel 8.0 now _only_ sets `trigger.sender` for the following events:

  * `INVITE`
  * `JOIN`
  * `KICK`
  * `MODE`
  * `NOTICE`
  * `PART`
  * `PRIVMSG`
  * `TOPIC`

In all other cases, the `sender` will be `None` and plugin code should use the
`trigger.args` list to retrieve all information about the event.

For general IRC events like `QUIT`, `RPL_NAMREPLY`, etc. that don't happen "in"
a channel or other specific _context_, the `trigger.sender` value that plugin
callables saw in Sopel 7 was unpredictable at best. Writing correct behavior
should be more intuitive with this change.

#### To have `text`, you must first have `args`

`trigger.text` will now be _empty_ (`''`) if the event carries no `args`.
In Sopel 7, `trigger.text` contained the command name (e.g. `'QUIT'`) in these
cases, but that was a bug.

### IRC privilege requirement changes

In Sopel 8.0, the `@sopel.plugin.require_privilege()` decorator now implies
`@sopel.plugin.require_chanmsg()`, and the decorated callable will not run if
triggered outside of a channel. Previously, `require_privilege` restrictions
were simply ignored, and the callable would run anyway.

The `@sopel.plugin.require_bot_privilege()` decorator also now implies
`@sopel.plugin.require_chanmsg()`, with the same associated behavior change.

### Capability negotiation rework

The old `CapReq` method of asking Sopel to negotiate additional capabilities on
behalf of your plugin has been replaced with a much more robust system based on
the new `sopel.plugin.capability` class/decorator.

Plugins can now request capabilities in one of two ways:

```python
"""Sample plugin file"""

from sopel import plugin

# this will register a capability request
CAP_ACCOUNT_TAG = plugin.capability('account-tag')

# this will work as well
@plugin.capability('message-prefix')
def cap_message_prefix(cap_req, bot, acknowledged):
    # do something if message-prefix is ACK or NAK
    ...
```

The first method is easier if you just want to require a capability. The second
is easier if your plugin needs to _do something in response to_ the IRC server's
response to the capability request. See the documentation for more details about
[plugins and managing capabilities][capability-section].

  [capability-section]: https://sopel.chat/docs/plugin/advanced.html#managing-capability-negotiation

### The bot's hostmask

In Sopel 8, accessing `bot.hostmask` when the bot lacks sufficient data to
determine its own hostmask will return `None`. The behavior in Sopel 7 was to
raise a `KeyError`.

### Testing tool changes

The `MockIRCServer` mock object from Sopel's `pytest` plugin implements
`blocking` as a keyword-only argument in Sopel 8. This applies to:

* `MockIRCServer.channel_joined()`
* `MockIRCServer.join()`
* `MockIRCServer.mode_set()`
* `MockIRCServer.pm()`
* `MockIRCServer.say()`

To upgrade test cases using this mock, simply add `blocking=` to this parameter
of the method call if it's missing.

### Moved API features

We wanted to organize things better in Sopel 8.0, so some of the API features
have moved. The old locations will still work until Sopel 9.0, but you'll be way
ahead of the game if you update your plugins now!

* `Identifier` type moved from `sopel.tools` to `sopel.tools.identifiers`
* `SopelMemory` and `SopelMemoryWithDefault` types moved from `sopel.tools` to
  `sopel.tools.memories`
* `sopel.tools.check_pid()` moved to `sopel.cli.utils`

### Removed API features

Previously deprecated parts of Sopel's API have been removed, including:

* `bot.memory['url_callbacks']` is no longer created or populated by the bot
  * Plugins wanting to add URL handlers should use the
    [`@sopel.plugin.url()`][url-decorator] or
    [`@sopel.plugin.url_lazy()`][url-lazy-decorator] decorators instead
* `bot.privileges` channel information (deprecated since Sopel 6.2; replaced by
  [`bot.channels`][prop-bot.channels])
* `bot.msg()` method (use [`bot.say()`][meth-bot.say])
* `bot.register()` & `bot.unregister()` methods (no public-API replacement)
  * Plugins typically don't need to do this manually; if your code did, we
    advise refactoring it to work within Sopel's public APIs
* `sopel.cli.utils.redirect_outputs()` function (replaced by standard logging)
* `sopel.config.types.ConfigSection.get_list()` method (use a
  [`ListAttribute`][type-ListAttribute])
* `sopel.irc.utils.CapReq.module` attribute
  * Stopgap migration: switch to the `CapReq` type's `plugin` attribute
  * True migration: use the [`sopel.plugin.capability`][class-plugin.capability]
    class; `CapReq` will be removed in Sopel 9.0
* `sopel.loader.trim_docstring()` (use
  [`inspect.getdoc()`][func-inspect.getdoc])
* `sopel.test_tools` (use [the `pytest` plugin +
  mocks/factories][plugin-testing])
* `sopel.tools` members of the internal-use kind, deprecated since Sopel 7.1:
  * `compile_rule()`, `get_action_command_pattern()`,
    `get_action_command_regexp()`, `get_command_pattern()`,
    `get_command_regexp()`, `get_nickname_command_pattern()`, &
    `get_nickname_command_regexp()`
* `sopel.tools` members of the useless-in-modern-Python kind:
  * `Ddict` class (use
    [`collections.defaultdict`][type-collections.defaultdict])
  * `contains()` methods of `SopelMemory` and `SopelMemoryWithDefault` (use [the
    `in` operator][membership-test])
  * `get_raising_file_and_line()` (use [Sopel's logging facility][plugin-logger]
    for exceptions)
  * `stdout()` (use [Sopel's logging facility][plugin-logger], or `print()` if
    you must)
* `sopel.web` (moved to [`sopel.tools.web`][module-tools.web] in Sopel 7.0)

  [class-plugin.capability]: https://sopel.chat/docs/plugin/advanced.html#sopel.plugin.capability
  [func-inspect.getdoc]: https://docs.python.org/3.11/library/inspect.html#inspect.getdoc
  [membership-test]: https://docs.python.org/3.11/reference/expressions.html#membership-test-operations
  [meth-bot.say]: https://sopel.chat/docs/package/bot.html#sopel.bot.Sopel.say
  [module-tools.web]: https://sopel.chat/docs/package/tools/web.html
  [plugin-logger]: https://sopel.chat/docs/package/tools.html#sopel.tools.get_logger
  [plugin-testing]: https://sopel.chat/docs/plugin/test.html
  [prop-bot.channels]: https://sopel.chat/docs/package/bot.html#sopel.bot.Sopel.channels
  [type-ListAttribute]: https://sopel.chat/docs/package/config/types.html#sopel.config.types.ListAttribute
  [type-collections.defaultdict]: https://docs.python.org/3.11/library/collections.html#defaultdict-objects
  [url-decorator]: https://sopel.chat/docs/plugin/decorators.html#sopel.plugin.url
  [url-lazy-decorator]: https://sopel.chat/docs/plugin/decorators.html#sopel.plugin.url_lazy

### Deprecated API features

More small legacy API features have been deprecated in version 8.0:

* `bot.search_url_callbacks()` (use [`bot.rules.check_url_callbacks(bot,
  url)`][check-url-callbacks]; will be removed in 9.0)
* `sopel.tools.OutputRedirect` (will be removed in 8.1)
* `sopel.tools.stderr()` (we can't stress enough: plugins should use a logger,
  not stdout/stderr output; will be removed in 8.1)

We continue to reorganize, modernize, and improve various parts of Sopel's API
whenever possible. Thank you for your patience!

  [check-url-callbacks]: https://sopel.chat/docs/package/plugins/rules.html#sopel.plugins.rules.Manager.check_url_callback
