import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_3D_color_space():
    """ Plots a 3D scatter plot of the color space RGB """
    # 10x10x10 = 1000, works good on my machine, can even increase 20x20x20 = 8000
    r = np.arange(0, 1, 0.1)
    g = np.arange(0, 1, 0.1)
    b = np.arange(0, 1, 0.1)
    R, G, B = np.meshgrid(r, b, g)
    R = R.flatten()
    G = G.flatten()
    B = B.flatten()
    colors = np.c_[R, G, B]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(R, B, G, marker='o', c=colors)
    plt.title('3D color space')
    plt.show()


plot_3D_color_space()
