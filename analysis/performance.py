from experiment import run_experiment

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        run_experiment(N=1000, fail_prob=0.7, certainty=0.9, fail_loc=650, seed=2)  
