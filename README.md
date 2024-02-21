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

Alternativey, pipe through `csvkit` utils for pretty printing:
```bash
python startup_time.py -s 100 | in2csv -f json | csvlook
```

## Results
### WSL2
```bash
| name         | stats/count | stats/mean | stats/median | stats/std |
| ------------ | ----------- | ---------- | ------------ | --------- |
| argparse-cli |         100 |     0.023… |       0.022… |    0.002… |
| docopt-cli   |         100 |     0.024… |       0.021… |    0.010… |
| click-cli    |         100 |     0.040… |       0.038… |    0.006… |
| typer-cli    |         100 |     0.050… |       0.048… |    0.003… |
```

### Windows
```bash
| name         | stats/count | stats/mean | stats/median | stats/std |
| ------------ | ----------- | ---------- | ------------ | --------- |
| docopt-cli   |         100 |     0.105… |       0.103… |    0.010… |
| argparse-cli |         100 |     0.122… |       0.120… |    0.010… |
| click-cli    |         100 |     0.176… |       0.169… |    0.040… |
| typer-cli    |         100 |     0.440… |       0.414… |    0.077… |
```
