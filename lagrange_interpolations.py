# %% [markdown]
# # Lagrange Interpolations of a given analytic function

# %% [markdown]
# ## 0. Definitions of Plotting parameters

# %%
import numpy as np

a, b, n_plot = -10, 20, 1000
x_plot = np.linspace(a, b, n_plot)
print("x_plot =", x_plot)

# %% [markdown]
# ## 1. Definition of f

# %%
from utils import *

# f_exp = "cos(x)" # "1/(1+x**2)"
# def f(x):
    # return eval(f_exp, {"x": x})

f = lambda x: 1/(1+x**2)

fig, ax = set_fig()
plot_f(ax, f, x_plot)

# %% [markdown]
# ## 2. Definition of Interpolation parameters

# %%
from polynomial.utils import *

n = 20

# Defintion of Uniforms points
x_uniform = np.linspace(a, b, n)
y_uniform = [f(x) for x in x_uniform]
print("Uniforms points")
print("x_uniform =", x_uniform)
print("\ny_uniform =", y_uniform)

#Definition of Tchebychev points
x_tchebychev = tchebychev_points(a, b, n)
y_tchebychev = [f(x) for x in x_tchebychev]
print("\nTchebychev points")
print("x_tchebychev =", x_tchebychev)
print("\ny_tchebychev =", y_tchebychev)

# %% [markdown]
# ## 3. Test of Newton Lagrange Polynomial Representation

# %%
from polynomial.newton_poly import *

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("x =", x)
print("y =", y)
polynomial = NewtonInterpolPoly(x, y)
print(polynomial)

x = 6
value = polynomial.horner_eval(x)
print(f"p({x}) = {value}")

# %% [markdown]
# ## 4. Uniform Lagrange Interpolation of f

# %%
uni_lagrange_poly = NewtonInterpolPoly(x_uniform, y_uniform)

x0 = 1
print(f"uni_lagrange_poly({x0}) =", uni_lagrange_poly.horner_eval(x0))

# print("\nx_uniform =", x_uniform)
# print("\ny_uniform =", y_uniform)

fig, ax = set_fig()
plot_f(ax, f, x_plot)
uni_lagrange_poly.plot(ax, x_plot, "Uniform Lagrange Interpolation of f")

# %% [markdown]
# ## 5. Tchebychev Lagrange Interpolation of f

# %%
tchebychev_lagrange_poly = NewtonInterpolPoly(x_tchebychev, y_tchebychev)

x0 = 1
print(f"tchebychev_lagrange_poly({x0}) =", tchebychev_lagrange_poly.horner_eval(x0))

# print("\nx_tchebychev =", x_tchebychev)
# print("\ny_tchebychev =", y_tchebychev)
print(tchebychev_lagrange_poly.horner_eval(x0))

fig, ax = set_fig()
plot_f(ax, f, x_plot)

# uni_lagrange_poly.plot(ax, x_plot, "Uniform Lagrange Interpolation of f")
tchebychev_lagrange_poly.plot(ax, x_plot, "Tchebychev Lagrange Interpolation of f")

# %% [markdown]
# ## 6. Test of Gauss Integration

# %%
from integration import *

f_ = lambda x: x**2
gaus_int_f_ = gauss_integration(f_, -2, 5)
print("Gauss Integration of f_ =", gaus_int_f_)

# %% [markdown]
# ## 7. Errors of Lagrange Interpolations of f

# %%
func_err_uniform = lambda x: (f(x) - uni_lagrange_poly.horner_eval(x))**2
func_err_tchebychev = lambda x: (f(x) - tchebychev_lagrange_poly.horner_eval(x))**2
err_uniform = sqrt(gauss_integration(func_err_uniform, a, b))
err_tchebychev = sqrt(gauss_integration(func_err_tchebychev, a, b))
print("err_uniform =", err_uniform)
print("err_tchebychev =", err_tchebychev)

fig, ax = set_fig()

# plot_f(ax, f, x_plot)
# uni_lagrange_poly.plot(ax, x_plot, "Uniform Lagrange Interpolation of f")
# tchebychev_lagrange_poly.plot(ax, x_plot, "Tchebychev Lagrange Interpolation of f")

y_uni_plot = [func_err_uniform(x) for x  in x_plot]
ax.plot(x_plot, y_uni_plot, label="Error of Uniform Lagrange Interpolation of f")

y_tche_plot = [func_err_tchebychev(x) for x  in x_plot]
ax.plot(x_plot, y_tche_plot, label="Error of Tchebychev Lagrange Interpolation of f")

ax.legend()



