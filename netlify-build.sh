#!/bin/bash

echo "Starting custom build script..."

echo "Installing Sphinx & plugins"
pip install sphinx sphinxcontrib-versioning

echo "Building Jekyll site"
bundler exec jekyll build

if [ -d "sopel/" ]; then
    cd sopel
    git checkout master
    git pull origin master
    cd docs
else
    git clone --depth 1 https://github.com/sopel-irc/sopel.git sopel
    cd sopel/docs
fi

echo "Building Sphinx docs"
sphinx-versioning build docs build/html
cd ../../

echo "Moving Sphinx docs to Jekyll output folder"
mv sopel/docs/build/html _site/docs

echo "Should be all done!"
echo "Finished custom build script."
