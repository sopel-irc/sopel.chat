---
title: Formatting & color codes
migrated: true
source: wiki
---

Sopel will accept formatted IRC messages. You just need to put IRC control codes in your `bot.say`/`bot.action` strings.

## Best approach
```python
from sopel.formatting import *

color("RED STRING", colors.RED)
bold("BOLD STRING")
underline("UNDERLINED STRING")
```
See [the API docs]({{ site.docs }}api.html#module-sopel.formatting) for more information.

## colors
Sopel accepts strings with colors written like this: `\x03XX,YY` at the beginning of the text you want colored and `\x03` at the end. for example, `\x0309,01This is some text\x03` would produce ![Green text on a black background showing "This is some text"](https://puu.sh/qKBZS/46144c4c05.png).

## color numbers
This table shows the various colors that can be used:

Number | Name
------ | ----
00     | white
01     | black
02     | blue (navy)
03     | green
04     | red
05     | brown (maroon)
06     | purple
07     | orange (olive)
08     | yellow
09     | light green (lime)
10     | teal (a green/blue cyan)
11     | light cyan (cyan / aqua)
12     | light blue (royal)
13     | pink (light purple / fuchsia)
14     | grey
15     | light grey (silver)

## Other codes
This table shows other codes that can be used to format or clear IRC text:

Code   | Meaning
------ | -------
`\x02` | bold
`\x03` | colored text
`\x1D` | italic text
`\x1F` | underlined text
`\x16` | swap background and foreground colors ("reverse video")
`\x0F` | reset all formatting