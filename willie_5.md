---
layout: default
title: Willie 5.0 Migration
---

# Willie 5.0 Migration

In an attempt to clean up the API and make Willie more stable, easier to use,
and easier to maintain, many things will be changing in an upcoming release of
Willie. You may be seeing a number of deprecation warnings from Willie, to let
you know if you'll run into a problem when the changes happen.

## Database rewrite

This is likely the only thing that will affect people who haven't written their
own modules for Willie. Willie's entire database system is being rewritten from
scratch, as the old system had proven unreliable and insecure. A number of
things will be changed because of this.

### Table migrations

Data will have to be migrated to the new schema. More information on this will
be provided as the release of 5.0 approaches.

### Database system support

Only sqlite will be supported. If you are currently using MySQL or Postgres,
you may want to migrate your database to sqlite prior to the release of 5.0, as
any migration path we release will only cover sqlite-to-sqlite. There are a
number of guides that can be found to show how to do this migration - the basic
idea is to dump your existing database to a file and load it back into sqlite.

### Database access functions

If you are a module writer, any access to the database will need to be changed
to the new standards. To ease this process, the 5.0 API will be backported, to
the extent possible, into new releases of the 4.x series. Basic tasks, like
getting a setting for a user or channel, will simply require changing some
calls.

However, the pseudo-ORM Willie was using, which enabled you to add your own
tables to the database, will be dropped. If you were using that API, you will
need to write the SQL for it yourself or use another ORM or query writing
system. SQLAlchemy is highly recommended for this. While we don't currently
provide SQLAlchemy ORM definitions, if you make some for your own use and they
prove helpful, we would consider merging them and would greatly appreciate the
contribution.
