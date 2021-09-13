import matplotlib.pyplot as plt
import seaborn as sns

def matrix_plot(matrix):
    f, ax = plt.subplots(figsize=(15, 15)) 
    heatmap = sns.heatmap(matrix,
                      square=True,
                      linewidths = .5,
                      cmap ='Blues',
                      cbar_kws={"shrink": .4, 'ticks' : [-0.5, -0.625, -0.25, -0.125, 0.0]},
                      vmin = -0.5, 
                      vmax = 0.0,
                      )
    ax.set_yticklabels(matrix[i], rotation = 0)
    ax.set_xticklabels(matrix[i])
    sns.set_style({'xtick.bottom': True}, {'ytick.left': True})
    return heatmap

