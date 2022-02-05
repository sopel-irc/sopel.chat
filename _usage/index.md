---
title: Using Sopel
permalink: /usage/
---

Some of Sopel's features warrant additional documentation, beyond what can be
(readily) included in Sopel's `.help` output.

While the [plugin documentation]({% link docs/plugin.html %}) is intended for
developers, these usage documents are targeted squarely at users—those running
or using the bot. The goal is to explain how to do useful things with Sopel,
without writing any code.

{% assign docs = site.usage | where_exp: "doc", "doc.url != page.url" | sort: "order" %}
{% for doc in docs %}
  * [{{ doc.title }}]({{ doc.url }})
{% endfor %}
