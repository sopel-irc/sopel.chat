---
title: Appendices
permalink: /appendix/
---

This appendix contains older technical & guide material that predates the
[developer guide to plugins]({% link docs/plugin.html %}), and hosts some
outdated [usage]({% link _usage/index.md %}) guide material that probably
isn't relevant to most users.

{% assign docs = site.appendices | where_exp: "doc", "doc.url != page.url" | sort: "order" %}
{% for doc in docs %}
  * [{{ doc.title }}]({{ doc.url }})
{% endfor %}
