import click
from cli_benches.model import run


@click.command()
@click.option('-n', '--numbers', multiple=True, type=int, help="put numbers")
@click.option('-s', '--strings', multiple=True, type=str, help="put strings")
def cli(numbers, strings):
    """
    Simple CLI that accepts a list of numbers and a list of strings.
    """
    run(numbers, strings)

if __name__ == '__main__':
    cli()
