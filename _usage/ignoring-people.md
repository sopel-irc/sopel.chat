---
title: Making Sopel ignore people
migrated: true
source: wiki
order: 100
---

Sopel has a built-in ability to ignore specified people. This is managed through the `.blocks` command. Sopel can block by either nickname or hostmask.

Both the nicks and the hostmasks you give to Sopel use regular expressions. If you're just looking to block a specific name (like you might if you want to block another bot), you don't need to worry about this. Otherwise, refer to [this page](https://docs.python.org/2/library/re.html) for details about the syntax.

The `.blocks` command is used by giving it one of three different commands: `list`, `add`, and `del`. These list all blocks, add a block, or delete a block respectively. After that, it takes an argument of either `nick` or `hostmask`, indicating whether you want to list/add/delete nick or hostmask blocks. `add` and `del` both take a final argument, the nick or hostmask block that you want to add/delete.

```
.blocks add nick somenickhere
.blocks del nick somenickhere
.blocks add hostmask .*@.*\.bad\.actor\.net
.blocks list nick
.blocks list hostmask
```
