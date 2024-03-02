from scipy.optimize import minimize
import numpy as np
import math
#a=float(input())
#b=float(input())
x0y0 = [0,0]
def myfunc(vars,a,b):
    x,y = vars
    return (x+y)**2-2*x*(y+a)-2*y*b+a+b
a=8
b=6
result = minimize(myfunc, x0y0, args=(a,b))
print(result)
