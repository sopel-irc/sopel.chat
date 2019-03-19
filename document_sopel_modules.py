#!/usr/bin/env python2.7
"""
Sopel module documentation utility
This script creates (either Markdown or reST) files, documenting the commands
and module configuration options in a Sopel instance.

Copyright 2012 Edward Powell, embolalia.net
Copyright 2019 dgw, technobabbl.es
Licensed under the Eiffel Forum License 2.

https://sopel.chat
"""
import argparse
import inspect
import operator
import os
import imp
import sys
try:
    import sopel
except:
    print ("Sopel isn't installed globally. You may have problems.")


def main(argv=None):
    this_dir = os.path.dirname(os.path.abspath(__file__))
    config_vals_file = os.path.join(this_dir, '_usage/module-configuration.md')
    commands_file = os.path.join(this_dir, '_usage/commands.md')

    parser = argparse.ArgumentParser(
        description="Sopel module documentation utility",
        usage='%(prog)s [options]'
        )
    parser.add_argument(
        '--sopel',
        dest='sopel_root',
        nargs='?',
        help="Specify the location of Sopel's code.",
        default=os.path.join(os.path.dirname(this_dir), 'sopel')
        )
    parser.add_argument(
        '--clean',
        action='store_true',
        help="Clean up the generated page files."
        )

    if argv:
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()

    if args.clean:
        print("Cleaning up generated module documentation...")
        os.remove(config_vals_file)
        os.remove(commands_file)
        return

    print("Generating module docs using Sopel from " + args.sopel_root)
    print("...")
    os.sys.path.insert(0, args.sopel_root)

    filenames = []
    modules_dir = os.path.join(args.sopel_root, 'sopel', 'modules')

    for fn in os.listdir(modules_dir):
        if fn.endswith('.py') and not fn.startswith('_'):
            filenames.append(os.path.join(modules_dir, fn))

    filenames.sort()

    filenames.append(os.path.join(args.sopel_root, 'sopel', 'coretasks.py'))

    commands = []

    with open(config_vals_file, 'w') as f:
        f.write(inspect.cleandoc("""\
        ---
        title: Module configuration
        order: 5
        ---

        This page contains documentation for all modules within Sopel's main
        modules directory. If you have added modules without rebuilding the
        documentation, or are using a secondary modules directory, those
        modules will not be shown here.

        ## Modules
        """))
        for filename in filenames:
            c = document_module(filename, f)
            if c:
                commands.extend(c)

    with open(commands_file, 'w') as f:
        f.write(inspect.cleandoc("""\
        ---
        title: Module commands
        order: 10
        ---

        This page contains a list of all commands from modules within Sopel's
        main modules directory. If you have added modules without rebuilding
        the documentation, or are using a secondary modules directory, those
        modules will not be shown here.
        """))
        f.write("\n\n| Command(s) | Purpose | Example | Module |\n")
        f.write("| ---------- | ------- | ------- | ------ |\n")
        for c in commands:
            process_command(f, c)

    print("Done!")

def document_module(module_file, f):
    try: module = imp.load_source(os.path.basename(module_file)[:-3], module_file)
    except Exception as e:
        print ("Error loading %s: %s\nThis module will not be documented."
               % (module_file, e))
    else:
        commands = []
        if hasattr(module, 'configure'):
            f.write('\n\n### %s\n\n'%(module.__name__))
            if not module.configure.__doc__:
                module.configure.__doc__ = 'This module has configuration options that are not documented. Go bludgeon the author.'
            f.write(inspect.cleandoc(module.configure.__doc__))
        for obj in dir(module):
            func = getattr(module, obj)
            if not callable(func):
                # guard against modules that use `from sopel import module`
                continue
            if (hasattr(func, 'commands')):
                if not hasattr(func, 'name'):
                    name = func.__name__
                else:
                    name = func.name
                setattr(func, 'module_name', module.__name__)
                commands.append((name, func))

        # return the commands from each module in (roughly) alphabetical order
        commands.sort()
        return commands

def process_command(f, func):
    name = func[0]
    func = func[1]

    purpose = (func.__doc__ or '*No documentation found.*')
    purpose = inspect.cleandoc(purpose).replace('\n', '<br>').replace('|', '\\|')
    if hasattr(func, 'example'):
        example = '`%s`' % func.example[0]["example"].replace('$nickname', 'Sopel')
    else:
        example = ''

    commands = '.'+'<br>.'.join(func.commands) #TODO rules
    module = func.module_name
    line = "| %s | %s | %s | %s |\n" % (commands, purpose, example, module)
    f.write(line)

if __name__ == '__main__':
    main()
