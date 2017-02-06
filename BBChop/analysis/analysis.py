import json
from multiprocessing import Pool, cpu_count
from itertools import product

from experiment import run_experiment
from plot_results import plot_analysis


def dict_product(**kwargs):
    ''' A generator that procudes the cartesian product over the
    inputs as a dictionary each.
    '''
    keys = kwargs.keys()
    values = kwargs.values()
    for elem in product(*values):
        yield dict( zip(keys, elem) )

def get_configs():
    configs = dict_product(N=[10, 100, 1000],
                           fail_prob=[1., .9, .5, .25, .1, 0.01, 0.005],
                           certainty=[0.9, 0.7],
                           fail_loc_func = [lambda N : int(N * 0.7), lambda N : int(N * 0.5)],
                           #fail_loc = [3, 5  ],
                           seed=range(1, 10))

    def apply_fail_loc_fun(gen):
        for d in gen:
            try:
                d['fail_loc'] = d['fail_loc_func'](d['N'])
                del d['fail_loc_func']
            except KeyError:
                pass
            yield d
    configs = apply_fail_loc_fun(configs)
    return configs

def save_configs(hostnames, configs):

    n = len(hostnames)
    configs_splitted = n*[[]]

    # Map each config to the same position
    for c in configs:
        h = hash(frozenset(c.values()))
        i = h % n
        configs_splitted[i].append(c)

    for i, h in enumerate(hostnames):
        with open('{}.json'.format(h), 'w') as f:
            json.dump(configs_splitted[i], f)

def generate_plot(n):
    ''' Generate plot '''

    configs = get_configs()
    with Pool(cpu_count()) as p:
        data = p.map(run_experiment, configs)

    try:
        import pandas as pd

        data_frame = pd.DataFrame(data)  # Try pd.DataFrame.from_records(d) with >0.16.2
        print(data_frame)

        plot_analysis(data_frame)
    except ImportError:
        pass

    with open('analysis2.json', 'w') as fp:
        json.dump(data, fp)

if __name__ == '__main__':
    #generate_plot(1)
    hosts = [
    ]
    save_configs(hosts, get_configs())
