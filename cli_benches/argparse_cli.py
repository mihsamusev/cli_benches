import argparse
from cli_benches.model import run

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numbers", type=int, nargs="+", help="put numbers")
    parser.add_argument("-s", "--strings", type=str, nargs="+", help="put strings")
    args = parser.parse_args()
    
    run(args.numbers, args.strings)
    

if __name__ == "__main__":
    cli()
