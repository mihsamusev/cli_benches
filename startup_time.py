import argparse
import subprocess
from collections import defaultdict
import time
import json
import statistics


STATS = "stats"
COUNT = "count"
MEAN = "mean"
MEDIAN = "median"
STD = "std"


def command(s: str):
    return [s, "--help"]

def aggregate(times: dict) -> list[dict]:
    out = []
    for key, data in times.items():
        aggregated = {
            "name": key,
            STATS: {
                COUNT: len(data),
                MEAN: statistics.mean(data),
                MEDIAN: statistics.median(data),
                STD: statistics.stdev(data)
            }
        }
        out.append(aggregated)
    return out

def bench(tools: list[str], n_rounds: int):
    times = defaultdict(list)
    for tool in tools:
        for _ in range(n_rounds):
            start_time = time.time()
            subprocess.run(command(tool), shell=True, text=True, capture_output=True)
            elapsed = time.time() - start_time
            times[tool].append(elapsed)

    return times

def main(n_samples: int):
    tools = [
        "argparse-cli",
        "typer-cli",
        "click-cli",
        "docopt-cli",
        ]
    times = bench(tools, n_samples)
    result = aggregate(times)
    result = sorted(result, key= lambda x: x["stats"][MEAN])
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser() 
    parser.add_argument("-s", "--samples", type=int, default=10, help="number of samples")
    args = parser.parse_args()
    main(args.samples)
