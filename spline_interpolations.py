# %% [markdown]
# # Spline Interpolations of a given analytic function

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
n = 40

# Defintion of Uniforms points
x_uniform = np.linspace(a, b, n)
y_uniform = [f(x) for x in x_uniform]
print("Uniforms points")
print("x_uniform =", x_uniform)
print("\ny_uniform =", y_uniform)

# %% [markdown]
# ## 3. Test of Linear Spline Interpolation

# %%
from polynomial.newton_poly import  Spline1Poly

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("x =", x)
print("y =", y)
polynomial = Spline1Poly(x, y)
print(polynomial)

x = 1.5
value = polynomial.horner_eval(x)
print(f"p({x}) = {value}")

# %% [markdown]
# ## 4. Uniform Linear Spline Interpolation of f

# %%
uni_linear_spline_poly = Spline1Poly(x_uniform, y_uniform, "Uni_linear_spline_poly")

print(uni_linear_spline_poly)

x0 = 1
print(f"\nUni_linear_spline_poly({x0}) =", uni_linear_spline_poly.horner_eval(x0))

# print("\nx_uniform =", x_uniform)
# print("\ny_uniform =", y_uniform)

fig, ax = set_fig()
plot_f(ax, f, x_plot)

uni_linear_spline_poly.plot(ax, "Uniform Linear Spline Interpolation of f")

# %% [markdown]
# ## 5. Uniform Cubic Spline Interpolation of f

# %%
from polynomial.taylor_poly import Spline3Polys
      
uni_spline3_poly = Spline3Polys(x_uniform, y_uniform, "Uni_spline3_poly")

print(uni_spline3_poly)

x0 = 1
print(f"\nUni_spline3_poly({x0}) =", uni_spline3_poly.horner_eval(x0))

fig, ax = set_fig()
plot_f(ax, f, x_plot)

# print("\nx_uniform =", x_uniform)
# print("\ny_uniform =", y_uniform)

uni_linear_spline_poly.plot(ax, "Uniform Linear Spline Interpolation of f")
uni_spline3_poly.plot(ax, n_plot, "Uniform Cubic Spline Interpolation of f")

# %% [markdown]
# ## 6. Errors of SPline Interpolations of f

# %%
from integration import gauss_integration

func_err_spline1 = lambda x: (f(x) - uni_linear_spline_poly.horner_eval(x))**2
func_err_spline3 = lambda x: (f(x) - uni_spline3_poly.horner_eval(x))**2
err_spline1 = sqrt(gauss_integration(func_err_spline1, a, b))
err_spline3 = sqrt(gauss_integration(func_err_spline3, a, b))
print("err_spline1 =", err_spline1)
print("err_spline3 =", err_spline3)

fig, ax = set_fig()

plot_f(ax, f, x_plot)
uni_linear_spline_poly.plot(ax, "Uniform Linear Spline Interpolation of f")
uni_spline3_poly.plot(ax, n_plot, "Uniform Cubic Spline Interpolation of f")

y_uni_plot = [func_err_spline1(x) for x  in x_plot]
ax.plot(x_plot, y_uni_plot, label="Error of Uniform Linear Spline Interpolation of f")

y_tche_plot = [func_err_spline3(x) for x  in x_plot]
ax.plot(x_plot, y_tche_plot, label="Error of Uniform Cubic Spline Interpolation of f")

ax.legend()



