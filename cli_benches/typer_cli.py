import typer
from cli_benches.model import run

def main(numbers: list[int] = typer.Option(None, "--numbers", "-n", help="put numbers"),
         strings: list[str] = typer.Option(None, "--strings", "-s", help="put strings")):
    run(numbers, strings)

def cli():
    typer.run(main)

if __name__ == "__main__":
    cli()
