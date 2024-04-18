import numpy as np

from math import sqrt

def gauss_integration(f, a=-1, b=1):
    if (a == -1 and b == 1):
        x = sqrt(3/5)
        return (5*f(-x) + 8*f(0) + 5*f(x)) / 9
    n = int((b-a)/2)+1
    intervals = np.linspace(a, b, n)
    d = (intervals[1] - intervals[0])/2
    return sum([gauss_integration(lambda t: f((1+t)*d+intervals[k]), -1, 1) for k in range(n-1)]) * d