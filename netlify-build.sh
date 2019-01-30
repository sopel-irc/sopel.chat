#!/bin/bash

echo "Starting custom build script..."

echo "Installing Sphinx"
pip install sphinx

echo "Generating changelogs"
python generate_changelogs.py --news=_sopel/NEWS

echo "Building Jekyll site"
bundler exec jekyll build

echo "Building Sphinx docs"
cd _sopel/docs
make html
cd ../../

echo "Moving Sphinx docs to Jekyll output folder"
mv _sopel/docs/build/html _site/docs

echo "Should be all done!"
echo "Finished custom build script."
