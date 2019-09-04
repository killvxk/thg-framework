import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    add_subcommand_fizzbuzz(subparsers)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    args.func(args)


def add_subcommand_fizzbuzz(subparsers):
    parser = subparsers.add_parser('fizzbuzz', help='do the fizzbuzz!')
    parser.set_defaults(func=handle_subcommand_fizzbuzz)
    parser.add_argument('-n', '--number', type=int, default=100, help='number for fizzbuzz to count to')


def handle_subcommand_fizzbuzz(args):
    from pypkgtemp.hello import fizzbuzz
    fizzbuzz(args.number)


if __name__ == '__main__':
    main()
