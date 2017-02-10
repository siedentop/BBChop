from random import seed
from BBChop.BBChop import BBChop
from BBChop import likelihoods
from BBChop import dag

import experiment


if __name__ == '__main__':
    N = 10
    L = 7
    p = 0.1

    seed(1)
    runner = experiment.Runner(L, p)

    prior = [ 1. / float(N) for i in range(N)]
    finder = BBChop(prior, 0.9, runner,
                    likelihoods.singleRateCalc,
                    dag.listDag())

    where = finder.search()
