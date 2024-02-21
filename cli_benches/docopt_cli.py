"""Example CLI application using docopt.

Usage:
  my_cli.py --numbers=<numbers>... --strings=<strings>...

Options:
  -n --numbers=<numbers>...  List of numbers.
  -s --strings=<strings>...  List of strings.
"""

from docopt import docopt
from cli_benches.model import run

arguments = docopt(__doc__)

def cli():
    numbers = list(map(int, arguments['--numbers']))
    strings = arguments['--strings']
    run(numbers, strings)

if __name__ == "__main__":
    cli()
