---
title: Command-line arguments
migrated: true
source: wiki
order: -9001
---

Sopel's command-line arguments are as follows:

<dl>
  <dt><tt>-h</tt>, <tt>--help</tt></dt>
  <dd>Show the help message and exit</dd>
  <dt><tt>-l</tt>, <tt>--list</tt></dt>
  <dd>List all available config files</dd>
  <dt><tt>-c filename</tt>, <tt>--config filename</tt></dt>
  <dd>Use the given config file. Path is relative to <tt>~/.sopel</tt>. If not given, <tt>default.cfg</tt> is assumed.</dd>
  <dt><tt>-m</tt>, <tt>--migrate</tt></dt>
  <dd>Migrate the current Sopel configuration file from the old <tt>.py</tt> format to the new <code>ConfigParser</code>-based <tt>.cfg</tt> format</dd>
  <dt><tt>-d</tt>, <tt>--fork</tt></dt>
  <dd>Run Sopel in the background. Output will still be shown unless <tt>--quiet</tt> is used.</dd>
  <dt><tt>-q</tt>, <tt>--quit</tt></dt>
  <dd>Tell a running Sopel to quit gracefully. (That is, send a QUIT message to the server before exiting.) This only affects the Sopel instance with the same config file — i.e. the same <tt>--config</tt> will need to be specified here if it was specified when you started Sopel.</dd>
  <dt><tt>--quiet</tt></dt>
  <dd>Suppress all terminal output</dd>
  <dt><tt>-k</tt>, <tt>--kill</tt></dt>
  <dd>Kill a running Sopel in an un-clean fashion (i.e. send SIGKILL to the process; no quit message will be sent to the server). Like <tt>--quit</tt>, the same <tt>--config</tt> must be specified here as when it was started, if any. Should only be used if Sopel does not respond to <tt>--quit</tt>.</dd>
</dl>