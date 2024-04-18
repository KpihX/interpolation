import numpy as np
import matplotlib.pyplot as plt

from math import *

""" Objects """

real = int | float
Real = {int, float}

""" Functions """

def plot_f(ax, f, x_plot):
    if callable(f):
        f_str = "f"
    elif type(f) == str:
        f_exp = f
        f_str = "f(x) = " + f_exp
        f = lambda x: eval(f_exp.replace("x", str(x)))
    else:
        raise ValueError(f"!{f} must be either a function or a string!")
    
    y_f = np.array([f(x) for x in x_plot]) # ? y_f = f(x_plot)
    ax.plot(x_plot, y_f, label=f_str)
    ax.legend()

def set_fig(title = "Plotting of Interpolations of f", xlabel = "x", ylabel = "y"):         
    fig, ax = plt.subplots()
    plt.title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig, ax
