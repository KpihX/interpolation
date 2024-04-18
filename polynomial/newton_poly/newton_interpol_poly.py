from .newton_poly import *

class NewtonInterpolPoly(NewtonPolynomial):
    def __init__(self, x, y, name='P'):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        super().__init__(self.newton_interpol_coefs(), x[:-1], name)

    def newton_interpol_coefs(self):
        n = len(self.x)
        coefficients = self.y.copy()
        step = 1
        for j in range(1, n):
            coefficients[j:n] = (coefficients[j:n] - coefficients[j-1:n-1]) / (self.x[j:n] - self.x[j-step:n-step])
            step += 1
        return coefficients

    def plot(self, ax, x_plot, label="Lagrange Interpolation of f"):
        super().plot(ax, x_plot, label)