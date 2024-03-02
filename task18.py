import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings
from scipy.optimize import minimize

def mixed(z, *args):
    return np.sum(neg_gauss(z, *params) for params in args)
Z = mixed((X, Y), (10, -5, -12), (7, 5, 5), (9, -5, 10))
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
contours = ax.contour(X, Y, Z, 16, colors="black", linewidths=2,
linestyles='-.')
ax.clabel(contours, inline=True, fontsize=16)
contours = ax.contourf(X, Y, Z, 200, cmap=plt.cm.jet)
plt.show()

# Gradient method
x0 = (-10, -2)
path = [x0]
result = minimize(mixed, x0,
 args=((10, -5, -12), (7, 5, 5), (9, -5, 10)),
 callback=get_path,
 )
Z = mixed((X, Y), (10, -5, -12), (7, 5, 5), (9, -5, 10))
path = np.array(path)
fig, ax = plt.subplots(1, 2, figsize=(20, 10))
contours = ax[0].contour(X, Y, Z, 16, colors="black", linewidths=2,
linestyles='-.')
ax[0].clabel(contours, inline=True, fontsize=16)
contours = ax[0].contourf(X, Y, Z, 200, cmap=plt.cm.jet)
ax[0].scatter(path[:, 0], path[:, 1], s=1600, c='yellow',
 marker='*',
 alpha=1,
 edgecolor='black',
 linewidth=2,
 zorder=1
