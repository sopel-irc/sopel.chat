---
title: Sopel tutorials
permalink: /tutorials/
---

{% assign tuts = site.tutorials | where_exp: "tut", "tut.url != page.url" %}
{% for tut in tuts %}
  * [{{ tut.title | replace: "Sopel tutorial, ", "" }}]({{ tut.url }})
{% endfor %}
