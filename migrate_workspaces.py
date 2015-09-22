#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Move i3 workspaces from one output to another.

Usage:
  migrate_workspaces.py (left|right) <exclude>...

Options:
  -h, --help        Show this.

"""


from docopt import docopt
import i3


def migrate(src, dst, exclude=[]):
    workspaces = i3.get_workspaces()
    for w in workspaces:
        if w['name'] in exclude:
            continue
        if w['output'] != dst['name']:
            i3.workspace(w['name'])
            i3.command('move', 'workspace to output right')


def main(args):
    outputs = filter(lambda x: x['active'], i3.get_outputs())

    if len(outputs) < 2:
        raise ValueError("The second monitor hasn't been detected. Is it on?")
    #laptop_out, ext_out = outputs if outputs[0]['primary'] else reversed(outputs)
    excludes = args['<exclude>']
    if args['left']:
        migrate(*outputs, exclude=excludes)
    else:
        migrate(*reversed(outputs), exclude=excludes)


if __name__ == '__main__':
    args = docopt(__doc__, version="migrate workspaces")
    main(args)
