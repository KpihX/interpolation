import numpy as np

from math import *

def tchebychev_points(a, b, n):
    return (a + b)/2 - (b - a)/2 * np.array([cos(pi*(2*i+1)/(2*n)) for i in range(n)])

def number_wrapper(x, nb_dec_digits=3):
    x = round(x, nb_dec_digits)
    if x == 0:
        return ""
    if x > 0:
        return str(x)
    return f"({x})"