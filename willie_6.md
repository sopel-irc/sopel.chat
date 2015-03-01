---
layout: default
title: Willie 6.0 Migration
---

# Willie 6.0 Migration

Writing Willie modules is cool. But what's cooler is *sharing* them. We want to
make that easier. With that in mind, we're preparing for Willie 6 to focus on
enabling that. Shortly after Willie 6 is released, we plan on introducing a
PyPI-like repository to give you a central place to share and enjoy Willie
modules.

However, in order to facilitate these changes, we do have to make some breaking
changes. This page tells you what you need to do to account for them. It will
be updated with more information as development toward Willie 6 continues.
Don't worry; this will likely be the last release with breaking changes for a
while.

## Login configurations

This is the only user-facing breaking change we're planning. There will be new
`auth_password`, `auth_user`, and `auth_method` settings in the config, which
will apply to all the different ways of authenticating that Willie supports.
If you configure with the wizard, you won't notice this change; it only really
concerns you if you're manually editing the config file.

## Reorganization of `willie.tools`

This is yet to be done, but some of the things you're importing from
`willie.tools` will now be elsewhere.

## Static configuration sections

The documentation for the core configuration settings has always been lacking,
so we've come up with a way to make it document itself the same way we document
the API. However, to force ourselves to document it, we'll be disabling the
magic that lets you grab arbitrary keys from the core config. You'll only be
able to use the pre-defined ones. Other sections will stay as they are; this
will only affect `config.core`.

## Refactoring of module loading

A bunch of stuff is getting moved around and refactored so that we can load
modules from folders. Unless you're messing with the loading internals in your
modules, this won't break anything for you.
