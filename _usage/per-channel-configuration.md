---
title: Per-channel configuration
order: 50
---

**Note: This feature is available only in Sopel 7.0 and later.**

If your Sopel bot is in many channels, you've probably run into at least one
case where a plugin that one channel loves is hated by the users and/or
operators in another. This is pretty common—after all, every IRC channel is a
fiefdom with its own dictator, who may or may not be benevolent.

Fortunately, configuring Sopel to work around such situations is easy.

## Channel config sections

In Sopel's config file, you can add sections for channels you want to treat
specially. For example:

```cfg
[#FunHaters]
disable_plugins = emoticons,instagram,reddit,xkcd
disable_commands = {"dice": ["roll", "choose"], "url": ["title_auto"]}
```

The channel name is taken literally; no pattern-matching is supported, for now.

In channels named `#FunHaters`, this would disable the `emoticons`, `instagram`,
`reddit`, and `xkcd` plugins entirely; it would also prevent the automatic
title-fetcher from `url` from running (but still allow the manual `.title`
command), and block use of the `.roll` and `.ch` commands from the `dice`
plugin. Details for each option below.

### `disable_plugins`

The `disable_plugins` option is a simple comma-separated list of plugin names,
just like [`core.enable`]({{ site.docs
}}config.html#sopel.config.core_section.CoreSection.enable) or
[`core.exclude`]({{ site.docs
}}config.html#sopel.config.core_section.CoreSection.exclude).

### `disable_commands`

The `disable_commands` option is written as a Python dict, where each key is a
plugin name and each value is a list of method names within that plugin.

Be sure to use the _method_ name, not the _command_ name. Matching on method
names makes it possible to disable things like URL handlers, too.

*Note: A future version of Sopel might move to a YAML config file format instead
of the INI format it uses now, to simplify the inclusion of more complex,
structured options like this. Let us know [on
IRC](irc://irc.libera.chat/#sopel) if you think this is a good idea.*
