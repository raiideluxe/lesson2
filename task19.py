from scipy.optimize import minimize
import numpy as np
import math

x0=float(input())
def myfunc(x):
    return x**2*(x-4)**2*math.exp(-x**2)

result = minimize(lambda x: -myfunc(x), x0, method='Nelder-Mead')

xmax = round(result.x[0],2)
print({xmax})

