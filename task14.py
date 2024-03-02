import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def dfdt(f,t):
    return f + t

def dfdt_vector(f,t):
    return np.array([dfdt(f[0],t)])

f0=float(input())
t_values = np.linspace(0,1,100)
f_values = odeint(dfdt_vector, f0, t_values)

print(f"{f_values[-1][0]:.2f}")
