---
title: Changelog
permalink: /changelog/
---

The contents of Sopel's [NEWS]({{ site.repo }}/blob/master/NEWS) file, until
now only accessible via browsing the [GitHub repository]({{ site.repo }}), now
automatically parsed and broken into pages for your reading pleasure.

{% assign docs = site.changelogs | where_exp: "doc", "doc.url != page.url" | sort: "title" | reverse %}
<ul>
{% for doc in docs %}
  <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
{% endfor %}
