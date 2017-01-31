from multiprocessing import Pool, cpu_count
from itertools import product

from experiment import run_experiment


def dict_product(**kwargs):
    ''' A generator that procudes the cartesian product over the
    inputs as a dictionary each.
    '''
    keys = kwargs.keys()
    values = kwargs.values()
    for elem in product(*values):
        yield dict( zip(keys, elem) )

def generate_plot(n):
    ''' Generate plot '''

    data = []
    configs = dict_product(N=[10, 100, 1000],
                           fail_prob=[1., .9, .5, .25, .1, 0.01, 0.005],
                           certainty=[0.9, 0.7],
                           fail_loc_func = [lambda N : int(N * 0.7), lambda N : int(N * 0.5)],
                           seed=[1, 2, 3])

    def apply_fail_loc_fun(gen):
        for d in gen:
            try:
                d['fail_loc'] = d['fail_loc_func'](d['N'])
                del d['fail_loc_func']
            except KeyError:
                pass
            yield d
    configs = apply_fail_loc_fun(configs)
    
    c = next(configs)
    data = run_experiment(**c)

    with Pool(cpu_count()) as p:
        data = p.map(run_experiment, configs)

    try:
        import numpy as np
        import matplotlib.pyplot as plt
        import pandas as pd

        data_frame = pd.DataFrame(data)  # Try pd.DataFrame.from_records(d) with >0.16.2
        print(data_frame)

        probs =  data_frame['fail_prob']
        trials = data_frame['trials']
        plt.loglog(probs, trials)
        plt.title('semilogx')
        plt.grid(True)
        plt.show()
    except ImportError:
        import json
        with open('analysis.json', 'w') as fp:
            json.dump(data, fp)

if __name__ == '__main__':
    generate_plot(1)
