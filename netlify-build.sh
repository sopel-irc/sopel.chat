#!/bin/bash

echo "Starting custom build script..."

echo "Cleaning up leftover Sopel clone"
rm -rf sopel/

echo "Installing Sphinx"
pip install sphinx

echo "Building Jekyll site"
bundler exec jekyll build

echo "Getting latest Sopel source (for documentation)"
git clone --depth 1 https://github.com/sopel-irc/sopel.git sopel

echo "Building Sphinx docs"
cd sopel/docs
make html
cd ../../

echo "Moving Sphinx docs to Jekyll output folder"
mv sopel/docs/build/html _site/docs

echo "Cleaning up Sopel repo"
rm -rf sopel/

echo "Should be all done!"
echo "Finished custom build script."
