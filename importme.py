import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('baseball_stats.csv')


def plot_team_ratio(team_name):
    df['team_ratio'] = df['wins']/df['runs_scored']
    team_ratio = df[df.name == team_name][['year', 'team_ratio']]
    plt.bar(team_ratio['year'], team_ratio['team_ratio'])
    plt.show()
    