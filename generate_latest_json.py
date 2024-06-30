#!/usr/bin/env python3
"""
Sopel update-check JSON generation utility

This script creates a `latest.json` file representing the most recent stable and
unstable `sopel` releases published to PyPI, using PyPI's own JSON API.

Copyright 2024 dgw, technobabbl.es
Licensed under the Eiffel Forum License 2.

https://sopel.chat
"""
import json
import sys

from packaging.version import parse as parse_version
import requests


def main(argv=None):
    response = requests.get('https://pypi.org/pypi/sopel/json')
    response.raise_for_status()
    data = response.json()
    releases = sorted(parse_version(v) for v in data['releases'].keys())

    latest = releases[-1]
    stable = latest
    if latest.is_prerelease:
        stable_releases_rev = (ver for ver in reversed(releases[:-1]) if not ver.is_prerelease)
        try:
            stable = next(stable_releases_rev)
        except StopIteration:
            print("ERROR: Latest version is a prerelease, but no earlier stable version found!")
            sys.exit(1)

    with open('latest.json', 'w') as f:
        sopel_version_info = {
            "version": str(stable),
            "unstable": str(latest),
            "release_notes": f"https://sopel.chat/changelog/{stable}/",
            "unstable_notes": f"https://github.com/sopel-irc/sopel/releases/v{latest}",
        }
        json.dump(sopel_version_info, f, indent=4)

    print("Generated latest.json file pointing to {} (stable) + {} (unstable)."
          .format(stable, latest))


if __name__ == '__main__':
    main()
