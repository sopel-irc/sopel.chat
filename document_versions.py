#!/usr/bin/env python3
"""
Sopel changelog page generation utility

This script creates discrete Markdown files for each version section in Sopel's
NEWS file, in the "changelogs" collection of the Jekyll site, so the changelog
entries will always be up-to-date with the Sopel version checked out for
building the Sphinx docs.

Copyright 2020 dgw, technobabbl.es
Licensed under the Eiffel Forum License 2.

https://sopel.chat
"""
import argparse
import glob
import inspect
import json
import os
import re


def main(argv=None):
    this_dir = os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser(
        description="Sopel version documentation utility",
        usage='%(prog)s [options]'
        )
    parser.add_argument(
        '--sopel',
        dest='sopel_root',
        nargs='?',
        help="Specify the location of Sopel's code.",
        default=os.path.join(this_dir, '_sopel')
        )
    parser.add_argument(
        '--news',
        dest='news_file',
        nargs='?',
        help="Specify the location of the NEWS file to use.",
        default=None
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

    sopel_root = os.path.abspath(os.path.expanduser(args.sopel_root))
    os.sys.path.insert(0, args.sopel_root)

    try:
        from sopel import (
            __version__ as current_version,
            version_info,
            _version_info,
        )
    except ImportError:
        print("Sopel isn't importable. Cannot continue.")
        raise

    if args.news_file:
        news_file = os.path.abspath(os.path.expanduser(args.news_file))
    else:
        news_file = os.path.join(sopel_root, 'NEWS')

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

    info_dict = {}
    stable = list(versions.keys())[0]
    info_dict['version'] = stable
    info_dict['release_notes'] = 'https://sopel.chat/changelog/{}/'.format(stable)

    if version_info.releaselevel == 'final':
        info_dict['unstable'] = stable
    else:
        info_dict['unstable'] = current_version
        tag_name = 'v' + re.sub(r'\.(a|b|rc)', r'-\1', current_version)
        info_dict['unstable_notes'] = (
            'https://github.com/sopel-irc/sopel/releases/tag/{}'.format(tag_name))

    with open('latest.json', 'w') as f:
        f.write(json.dumps(info_dict, indent=4))

    if stable != info_dict['unstable']:
        unstable = ', {} (unstable)'.format(info_dict['unstable'])
    else:
        unstable = ''
    print("Generated latest.json file pointing to {} (stable){}."
          .format(stable, unstable))

if __name__ == '__main__':
    main()
