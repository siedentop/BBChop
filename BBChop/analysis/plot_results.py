try:
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd

    def plot_analysis(data_frame):
        ''' Plot panda-data_frame'''
        probs =  data_frame['fail_prob']
        trials = data_frame['trials']
        plt.loglog(probs, trials)
        plt.title('semilogx')
        plt.grid(True)
        plt.show()

except ImportError:
    def plot_analysis(data_frame):
        pass





if __name__ == '__main__':
    #try:
    data_frame = pd.read_json('analysis.json')
    sns.lmplot('fail_prob', 'trials', data=data_frame)
    x = sns.violinplot(x='fail_loc', y='trials', hue='certainty', data=df2, split=True)