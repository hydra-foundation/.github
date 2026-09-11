#!/usr/bin/env python3
"""Regenerate the package table in profile/README.md.

The package list comes from the monorepo's `replace` block and the prose from
each package's composer.json `description`, which is also what Packagist shows.
Editing a description in the monorepo is therefore the way to change this page.

`app` is fetched separately: it is the skeleton, and lives in its own
repository rather than in the monorepo.

    render_packages.py                      # read the published monorepo
    render_packages.py --source ../hydra    # preview a local checkout first
"""

import argparse
import json
import pathlib
import re
import sys
import urllib.request

ORG = "hydra-foundation"
MONOREPO = f"https://raw.githubusercontent.com/{ORG}/hydra/main"
SKELETON = f"https://raw.githubusercontent.com/{ORG}/app/main/composer.json"

START = "<!-- packages:start -->"
END = "<!-- packages:end -->"

# Dependency order, roughly: the foundation first, then what builds on it.
# A package missing from this list still appears, alphabetically at the end,
# so adding one to the monorepo needs no edit here to show up on the page.
ORDER = (
    "core", "http", "nyholm", "php-di", "kernel", "session", "database", "cache",
    "validation", "view", "log", "event", "auth", "authorization", "csrf",
    "console", "admin",
)


def read(location):
    if "://" in location:
        with urllib.request.urlopen(location, timeout=30) as response:
            return json.load(response)
    return json.loads(pathlib.Path(location).read_text())


def packages(source, skeleton):
    replace = read(f"{source}/composer.json")["replace"]
    names = sorted(name.split("/", 1)[1] for name in replace)
    ranked = sorted(names, key=lambda n: (ORDER.index(n) if n in ORDER else len(ORDER), n))

    for name in ranked:
        description = read(f"{source}/packages/{name}/composer.json")["description"]
        yield name, description, f"https://github.com/{ORG}/hydra/tree/main/packages/{name}"

    yield "app", read(skeleton)["description"], f"https://github.com/{ORG}/app"


def table(source, skeleton):
    rows = ["| Package | Role |", "| --- | --- |"]
    for name, description, url in packages(source, skeleton):
        rows.append(f"| [**`{name}`**]({url}) | {description} |")
    return "\n".join(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=MONOREPO,
                        help="monorepo checkout or raw URL (default: published main)")
    parser.add_argument("--skeleton", default=SKELETON,
                        help="app composer.json path or raw URL")
    args = parser.parse_args()

    readme = pathlib.Path(__file__).resolve().parent.parent / "profile" / "README.md"
    current = readme.read_text()

    if START not in current or END not in current:
        sys.exit(f"{readme}: missing the {START} / {END} markers")

    rendered = f"{START}\n{table(args.source, args.skeleton)}\n{END}"
    updated, count = re.subn(
        rf"{re.escape(START)}.*?{re.escape(END)}",
        lambda _: rendered,
        current,
        flags=re.DOTALL,
    )

    if count != 1:
        sys.exit(f"{readme}: expected one marker pair, matched {count}")

    if updated == current:
        print("package table is up to date")
        return

    readme.write_text(updated)
    print("package table regenerated")


if __name__ == "__main__":
    main()
