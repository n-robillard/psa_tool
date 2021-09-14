"""
Program for help the graphic vizualisation in psa_tool

=====================================================================

Produce an heatmap for the vizualisation of the normalized mutual information
"""

import matplotlib.pyplot as plt
import seaborn as sns

def matrix_plot(matrix):
    f, ax = plt.subplots(figsize=(15, 15)) 
    heatmap = sns.heatmap(matrix,
                      square=True,
                      linewidths = .5,
                      cmap ='Blues',
                      cbar_kws={"shrink": .4, 'ticks' : [-0.2, -0.1, 0.0, 0.1, 0.2]},
                      vmin = -0.2, 
                      vmax = 0.2,
                      )
    sns.set_style({'xtick.bottom': True}, {'ytick.left': True})
    plt.title("Normalized Mutual Information")
    plt.xlabel("Fragment number")
    plt.ylabel("Fragment number")
    return heatmap

#TODO: other vizualisation of different criteria (entropy, frames, etc.)