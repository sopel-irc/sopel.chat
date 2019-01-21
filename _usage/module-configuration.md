---
title: Module configuration (outdated)
migrated: true
source: wiki
order: 9100
---

### This page is mostly outdated

Several of the modules described here have been moved out of Sopel and into standalone projects. Their configuration settings might still be useful as a reference, however.

----

This page contains documentation for all modules within Sopel's main modules directory. If you have added modules without rebuilding the documentation, or are using a secondary modules directory, those modules will not be shown here.

Modules
=======
github
------
| [github] | example | purpose |
| -------- | ------- | ------- |
| oauth_token | 5868e7af57496cc3ae255868e7af57496cc3ae25 | The OAuth token to connect to your github repo |
| repo | sopel-irc/sopel/ | The GitHub repo you're working from. |
radio
-----
| [radio] | example | purpose |
| ------- | ------- | ------- |
| URL | http://127.0.0.1:8000/ | URL to the ShoutCAST administration page |
| sID | 1 | Stream ID (only required for multi-stream servers.) |
url
---
| [url] | example | purpose |
| ---- | ------- | ------- |
| exclude | https?://git\\.io/.* | A list of regular expressions for URLs for which the title should not be shown. |
| exclusion_char | ! | A character (or string) which, when immediately preceding a URL, will stop the URL's title from being shown. |
admin
-----
| [admin] | example | purpose |
| -------- | ------- | ------- |
| hold_ground | False | Auto re-join on kick |
twit
----
These values are all found by signing up your bot at
[apps.twitter.com](https://apps.twitter.com).

| [twitter] | example | purpose |
| --------- | ------- | ------- |
| consumer_key | 09d8c7b0987cAQc7fge09 | OAuth consumer key |
| consumer_secret | LIaso6873jI8Yasdlfi76awer76yhasdfi75h6TFJgf | OAuth consumer secret |
| access_token | 564018348-Alldf7s6598d76tgsadfo9asdf56uUf65aVgdsf6 | OAuth access token |
| access_token_secret | asdfl7698596KIKJVGvJDcfcvcsfdy85hfddlku67 | OAuth access token secret |
bucket
------
It is highly recommended that you run the configuration utility on this
module, as it will handle creating an initializing your database. More
information on this module at https://github.com/sopel-irc/sopel/wiki/The-Bucket-Module:-User-and-Bot-Owner-Documentation

| [bucket] | example | purpose |
| -------- | ------- | ------- |
| db_host | example.com | The address of the MySQL server |
| db_user | bucket | The username to log into the MySQL database |
| db_pass | hunter2 | The password for the MySQL database |
| db_name | bucket | The name of the database you will use |
| literal_path | /home/sopel/www/bucket | The path in which to store output of the literal command |
| literal_baseurl | http://example.net/~sopel/bucket | The base URL for literal output |
bugzilla
--------
| [bugzilla] | example | purpose |
| ---- | ------- | ------- |
| domains | bugzilla.redhat.com,bugzilla.mozilla.org | A list of Bugzilla issue tracker domains |
meetbot
-------
| [meetbot] | example | purpose |
| --------- | ------- | ------- |
| meeting_log_path | /home/sopel/www/meetings | Path to meeting logs storage directory (should be an absolute path, accessible on a webserver) |
| meeting_log_baseurl | http://example.com/~sopel/meetings | Base URL for the meeting logs directory |