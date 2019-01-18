#!/bin/sh
# Build the site, and upload it to the server. Takes one argument, the user to
# log in as on the server

USER=${1:-$USER}

bundler exec jekyll build
scp -r _site/* $USER@sopel.chat:/var/www/sopel/
