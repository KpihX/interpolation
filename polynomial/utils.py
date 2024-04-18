import numpy as np

from math import *

def tchebychev_points(a, b, n):
    return (a + b)/2 - (b - a)/2 * np.array([cos(pi*(2*i+1)/(2*n)) for i in range(n)])