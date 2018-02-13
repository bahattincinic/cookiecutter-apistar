import sys
import argparse
import subprocess
import pytest


def run_tests():
    exitcode = pytest.main(['tests.py'])
    if exitcode:
        sys.exit(exitcode)


def get_parser():
    parser = argparse.ArgumentParser(
        prog="{{ cookiecutter.app_name }}",
        description='{{ cookiecutter.app_name }} Test Runner'
    )
    parser.add_argument('--nolint', dest='nolint', action='store_true')
    parser.add_argument('--lintonly', dest='lintonly', action='store_true')

    return parser


def run_flake8():
    ret = subprocess.call(
        ['flake8', '.', '--max-line-length=80']
    )

    if ret > 0:
        sys.exit(-1)


if __name__ == "__main__":
    parser = get_parser()
    args, ukargs = parser.parse_known_args()

    if args.nolint:
        run_tests()
    elif args.lintonly:
        run_flake8()
    else:
        run_flake8()
        run_tests()
