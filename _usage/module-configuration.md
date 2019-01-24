---
title: Module configuration
order: 5
---

This page contains documentation for all modules within Sopel's main
modules directory. If you have added modules without rebuilding the
documentation, or are using a secondary modules directory, those
modules will not be shown here.

## Modules

### admin

| name | example | purpose |
| ---- | ------- | ------- |
| hold\_ground | False | Auto-rejoin the channel after being kicked. |
| auto\_accept\_invite | True | Auto-join channels when invited. |

### bugzilla

| name | example | purpose |
| ---- | ------- | ------- |
| domains | bugzilla.redhat.com,bugzilla.mozilla.org | A list of Bugzilla issue tracker domains |

### clock

| name | example | purpose |
| ---- | ------- | ------- |
| tz | America/Chicago | Preferred time zone (see <https://sopel.chat/tz>); defaults to UTC |
| time\_format | %Y-%m-%d - %T%Z | Preferred time format (see <http://strftime.net>) |

### ip

| name | example | purpose |
| ---- | ------- | ------- |
| GeoIP\_db\_path | /home/sopel/GeoIP/ | Path to the GeoIP database files |

### meetbot

| name | example | purpose |
| ---- | ------- | ------- |
| meeting\_log\_path | /home/sopel/www/meetings | Path to meeting logs storage directory (should be an absolute path, accessible on a webserver) |
| meeting\_log\_baseurl | http://example.com/~sopel/meetings | Base URL for the meeting logs directory |

### safety

| name | example | purpose |
| ---- | ------- | ------- |
| enabled\_by\_default | True | Enable URL safety in all channels where it isn't explicitly disabled. |
| known\_good | sopel.chat,dftba.net | List of "known good" domains to ignore. |
| vt\_api\_key | 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef | Optional VirusTotal API key to improve malicious URL detection |

### url

| name | example | purpose |
| ---- | ------- | ------- |
| exclude | https?://git\\.io/.* | A list of regular expressions for URLs for which the title should not be shown. |
| exclusion\_char | ! | A character (or string) which, when immediately preceding a URL, will stop the URL's title from being shown. |
| shorten\_url\_length | 72 | If greater than 0, the title fetcher will include a TinyURL version of links longer than this many characters. |

### wikipedia

| name | example | purpose |
| ---- | ------- | ------- |
| default\_lang | en | The default language to find articles from (same as Wikipedia language subdomain) |
| lang\_per\_channel | #YourPants:en,#TusPantalones:es | List of #channel:langcode pairs to define Wikipedia language per channel |