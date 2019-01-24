#!/bin/bash

echo "Starting custom build script..."

echo "Building Jekyll site"
bundler exec jekyll build

echo "Building Sphinx docs"
git clone --depth 1 https://github.com/sopel-irc/sopel.git sopel
cd sopel/docs
make html
cd ../../

echo "Moving Sphinx docs to Jekyll output folder"
mv sopel/docs/build/html _site/docs

echo "Should be all done!"
echo "Finished custom build script."
