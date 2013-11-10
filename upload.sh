#!/bin/sh
# Build the site, and upload it to the server. Takes one argument, the user to
# log in as on the server

USER=$1

jekyll build
scp -r _site/* $USER@willie.dftba.net:/var/www/willie/
