#!/usr/bin/env python3
"""
Sopel changelog page generation utility

This script creates discrete Markdown files for each version section in Sopel's
NEWS file, in the "changelogs" collection of the Jekyll site, so the changelog
entries will always be up-to-date with the Sopel version checked out for
building the Sphinx docs.

Copyright 2019 dgw, technobabbl.es
Licensed under the Eiffel Forum License 2.

https://sopel.chat
"""
import argparse
import glob
import inspect
import os
import re


def main(argv=None):
    this_dir = os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser(
        description="Sopel changelog page generation utility",
        usage='%(prog)s [options]'
        )
    parser.add_argument(
        '--news',
        dest='news_file',
        nargs='?',
        help="Specify the location of the NEWS file to use.",
        default=os.path.join(os.path.join(this_dir, '_sopel'), 'NEWS')
        )
    parser.add_argument(
        '--clean',
        action='store_true',
        help="Clean up the generated changelog files."
        )

    if argv:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()

    if args.clean:
        print("Cleaning up changelog files...")
        for entry in glob.glob('_changelogs/*.md'):
            if not entry.endswith('index.md'):
                os.remove(entry)
        os.remove('latest.json')
        return

    news_file = os.path.abspath(os.path.expanduser(args.news_file))

    print("Generating changelog pages using NEWS file: " + news_file)

    with open(news_file, 'r') as f:
        news = f.read()

    split_news = re.split(r'Changes between \d+\.\d+(?:\.\d+)? and ', news)[1:]

    versions = {}
    for entry in split_news:
        version = re.match('^(.+?)\n', entry).group(1)
        body = re.search('(?s)\n=+\n(.*)', entry).group(1).strip()
        versions.update( {version: body} )

    for version, text in versions.items():
        with open('_changelogs/{}.md'.format(version), 'w') as f:
            f.write("---\ntitle: Version {version}\n---\n\n{log_entry}\n"
                    .format(version=version, log_entry=text))

    print("Done! {} versions documented.".format(len(versions.keys())))


if __name__ == '__main__':
    main()
