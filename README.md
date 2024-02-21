## Python CLI benches
Testing startup times of popular python CLI libraries for that smooth coconut cream user experience (yes looking at you Windows)


## Installation
Clone the folder, `cd` in, then:
```bash
pip install .
```

## Bench
Currently benchmarking startup times to `--help` command output for:
- `argparse`
- `click`
- `typer`
- `docopt`

```bash
python startup_time.py -s 100
```

```json
[
    {
        "name": "docopt-cli",
        "stats": {
            "count": 100,
            "mean": 0.020550777912139894,
            "median": 0.019954800605773926,
            "std": 0.0015330532016668696
        }
    },
    {
        "name": "argparse-cli",
        "stats": {
            "count": 100,
            "mean": 0.024127743244171142,
            "median": 0.023677945137023926,
            "std": 0.0014341973597934352
        }
    },
    {
        "name": "click-cli",
        "stats": {
            "count": 100,
            "mean": 0.04092825412750244,
            "median": 0.0405193567276001,
            "std": 0.0028114824239288943
        }
    },
    {
        "name": "typer-cli",
        "stats": {
            "count": 100,
            "mean": 0.053807063102722166,
            "median": 0.05288064479827881,
            "std": 0.003146052977225996
        }
    }
]
```

