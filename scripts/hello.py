#!/usr/bin/env python3
"""
Author:     Todd Demone
Purpose:    say hello
"""

import argparse


def get_args():
    """Get the command line arguments"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name', default='World',
                        type=str, help='Name to greet')
    return parser.parse_args()


def say_hello(name='World'):
    """Create a greeting that may include a person's name"""

    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    return f'Hello, {name}!'


def main():
    """Entry point of the script"""

    args = get_args()
    print(say_hello(args.name))


if __name__ == '__main__':
    main()
