
import fire
from cli_benches.model import run

def main(numbers=None, strings=None):
    """
    Wraps the run function for use with Fire.
    :param numbers: A list of integers.
    :param strings: A list of strings.
    """
    if numbers is None:
        numbers = []
    if strings is None:
        strings = []

    # Assuming numbers and strings are passed as lists of strings from the CLI
    # Convert strings to their appropriate types
    numbers = [int(num) for num in numbers]
    strings = [str(s) for s in strings]
    
    run(numbers, strings)

def cli():
    fire.Fire(main)

if __name__ == '__main__':
    cli()
