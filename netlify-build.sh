#!/bin/bash
set -e

echo "Starting custom build script..."

echo "Generating changelogs"
python3 document_versions.py --news=_sopel/NEWS

echo "Installing Sopel globally for plugin autodoc script"
pip3 install ./_sopel

echo "Generating latest.json file"
python3 generate_latest_json.py

echo "Generating plugin command/config pages"
python3 document_sopel_plugins.py --sopel=_sopel

echo "Installing Sopel's dev dependencies"
# Jinja2 pin for dependency hell on Sopel 7.x;
# shouldn't be necessary once we switch to docs for 8.0
pip3 install -r ./_sopel/dev-requirements.txt 'Jinja2<3.1'

echo "Building Sphinx docs"
cd _sopel/docs
make html
cd ../../

echo "Moving Sphinx docs to Jekyll site folder for output"
mv _sopel/docs/build/html/ docs/

echo "Building Jekyll site"
jekyll build

echo "Finished custom build script!"
