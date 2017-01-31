from random import random, seed

from BBChop.BBChop import BBChop
from BBChop import likelihoods, dag

from klepto.archives import file_archive
from klepto.keymaps import keymap
from klepto.safe import lru_cache

class Runner:
    def __init__(self, first_failure_location, failure_rate):
        self.fail_loc = first_failure_location
        self.trials = 0
        self.p = failure_rate
        
        
    def test(self, where):
        ''' Test at given location. '''
        self.trials += 1
        if where >= self.fail_loc:
            return self.p > random()
        else:
            return False
      

    def switch(self, where):
        ''' Switch test location '''
        pass
    def statusCallback(self, ended, mostLikely, mostLikelyProbs, probs, counts):
        '''
        ended: True if testing is done.
        mostLikely: most likely location
        mostLikelyProbs: probability at most likely location
        '''
        #print("Status [{}, {}, {}]".format(ended, mostLikely, mostLikelyProbs))
        pass

class Annotator:
    def __init__(self, f):
        self.f = f
        self.__name__ = f.__name__
    
    def __call__(self, *args, **kwargs):
        print('Starting: {}, {}'.format(args, kwargs))
        self.f(*args, **kwargs)
        print('Done with: {}, {}'.format(args, kwargs))



archiver = file_archive('cache_analysis.pkl', cached=False)
km = keymap()

@lru_cache(maxsize=1024, cache=archiver, keymap=km)
def run_experiment(*args, **kwargs):
    ''' Runs experiment and returns tuples of facts.
    Those are (loc_found, loc_correct, num_trials)
    '''
    print('Starting: {}, {}'.format(args, kwargs))

    # If we got dictionary as args, unpack
    if args and not kwargs:
        kwargs = args[0]

    N = kwargs['N']
    certainty = kwargs['certainty']
    fail_loc = kwargs['fail_loc']
    fail_prob = kwargs['fail_prob']
    _seed = kwargs['seed']

    seed(_seed)
    prior = [ 1. / float(N) for i in range(N)]
    runner = Runner(fail_loc, fail_prob)

    finder = BBChop(prior, certainty, runner,
                    likelihoods.singleRateCalc,
                    dag.listDag())

    where = finder.search()

    kwargs['where'] = where
    kwargs['success'] = fail_loc == where
    kwargs['trials'] = runner.trials

    print('Done with: {}, {}'.format(args, kwargs))

    return kwargs
