from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def func(y,t):
 u, f = y
 dydt = [2 * u - f, u]
 return dydt

t = np.arange(0,1,10)
res = odeint(func, y0 = [1,1], t = t)
plt.figure(figsize=(5,4))
plt.plot(t, res[:, 1])
plt.plot(t[::50], np.exp(t[::50]), 'o')
plt.show()

