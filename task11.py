import numpy as np
import matplotlib.pyplot as plt

R = 3
r = 1

theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

x = (R + r * np.cos(phi)) * np.cos(theta)
y = (R + r * np.sin(phi)) * np.sin(theta)
z = r * np.sin(phi)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, cmap=plt.cm.ocean_r)

plt.show()