#!/bin/bash
set -e

echo "Starting custom build script..."

echo "Generating changelogs & latest.json file"
python3 document_versions.py --news=_sopel/NEWS

echo "Installing Sopel globally for plugin autodoc script"
pip3 install ./_sopel

echo "Generating plugin command/config pages"
python3 document_sopel_plugins.py --sopel=_sopel

echo "Installing Sopel's dev dependencies"
pip3 install -r ./_sopel/dev-requirements.txt

echo "Building Sphinx docs"
cd _sopel/docs
make html
cd ../../

echo "Moving Sphinx docs to Jekyll site folder for output"
mv _sopel/docs/build/html/ docs/

echo "Building Jekyll site"
jekyll build

echo "Finished custom build script!"
