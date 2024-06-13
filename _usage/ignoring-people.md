---
title: Making Sopel ignore people
source: wiki
order: 100
---

Sopel has a built-in ability to ignore specified users by either nickname or
hostname. Bot admins can manage Sopel's ignores using the `.blocks` command.

Both the nicknames and the hostnames you give to Sopel use regular expressions.
If you're just looking to block a specific name (like you might if you want to
block another bot), you don't need to worry about this. Otherwise, refer to
[this page](https://docs.python.org/3/library/re.html) for the syntax.

The `.blocks` command is used by giving it one of the three main
subcommands—`list`, `add`, and `del`—followed by `nick` or `host` to indicate
whether you want to list/add/delete nickname or hostname blocks. `add` and `del`
both require a final argument: the nick or host pattern that you want to
add/delete.

```
.blocks add nick somenickhere
.blocks del nick somenickhere
.blocks add host .*\.bad\.actor\.net
.blocks list nick
.blocks list host
```
