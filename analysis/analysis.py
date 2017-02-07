import json
from itertools import product

def dict_product(**kwargs):
    ''' A generator that procudes the cartesian product over the
    inputs as a dictionary each.
    '''
    keys = kwargs.keys()
    values = kwargs.values()
    for elem in product(*values):
        yield dict( zip(keys, elem) )

def get_configs():
    configs = dict_product(N=range(100, 1000, 100),
                           fail_prob=[1., 0.5, 0.1],
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
    ''' Assign each config in configs to a hostname from hostnames
    and save result as 'hostname.json'.

    Implemented so result is stable.
    '''
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

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Save configurations to different hosts.')
    parser.add_argument('hosts', metavar='host', type=str, nargs='+',
                        help='A list of hosts')
    args = parser.parse_args()
    save_configs(args.hosts, get_configs())

