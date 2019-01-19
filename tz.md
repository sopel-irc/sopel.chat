---
layout: default
title: Sopel Timezone Settings
---

<h1 id="yourTimezone">Your timezone couldn't be detected. Enable JavaScript, or see instructions below.</h1>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jstimezonedetect/1.0.4/jstz.min.js"></script>
<script>
var timezone = jstz.determine();
var header = document.getElementById("yourTimezone");
header.innerHTML = "Your timezone is probably: " + timezone.name();
</script>

If this isn't your timezone, you can look it up
[here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List).

Timezones like "EST" are ambiguous. EST could mean US eastern time, Australia
eastern time, or Egypt time; many other abbreviations are ambiguous, too. Then
there are daylight saving rules and other smaller differences. And then they
change… Timezones just, generally,
[suck](https://www.youtube.com/watch?v=-5wpm-gesOY). So Sopel makes use of much
more specific names, which refer to a database that has all these complicated
rules taken care of.
