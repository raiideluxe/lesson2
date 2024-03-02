import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10 ,10, 1000)
y = np.linspace(-10 ,10, 1000)
plt.figure(figsize=(10,5))
plt.grid(lw=0.5, ls='--')
plt.plot(x, ((np.sin(x**2+y**2))/(x**2+y**2)),lw = 4, color = 'red',zorder = 0)
plt.show()







