import argparse
import json
from multiprocessing import Pool, cpu_count
from datetime import datetime

from experiment import run_experiment

def run_and_save(config):
  data = run_experiment(config)
  h = hash(frozenset(config.values()))
  try:
    f = open('result_{}.json'.format(h), 'w')
    json.dump(data, f)
  finally:
    f.close()
  return data

def compute(configs):
    with Pool(cpu_count()) as p:
        data = p.map(run_and_save, configs)

    with open('result_{}.json'.format(datetime.now()), 'w') as fp:
        json.dump(data, fp)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
      description='Run experiment for given JSON input.'
      )
    parser.add_argument('jsonfile')

    args = parser.parse_args()
    with open(args.jsonfile) as f:
        configs = json.load(f)

    compute(configs)
