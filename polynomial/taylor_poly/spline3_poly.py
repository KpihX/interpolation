from .taylor_poly import *

class Spline3Poly(TaylorPolynomial):
    def __init__(self, a, b, y_a, y_b, d_a, d_b, name="P"):
        self.a = a
        self.b = b
        self.y_a = y_a
        self.y_b = y_b
        self.d_a = d_a
        self.d_b = d_b
        self.name = name
        super().__init__(self.coefs(), a, name)
        self.coefficients = self.coefs()
        # print(self.coefficients)

    def coefs(self):
        h = self.b - self.a
        # print(self.a, self.b, self.y_a, self.y_b, self.d_a, self.d_b, h)
        # print([self.y_a, (self.y_b - self.y_a)/h - (2*self.d_a + self.d_b)*h/6, self.d_a/2, (self.d_b - self.d_a)/(6*h)])
        return [self.y_a, (self.y_b - self.y_a)/h - (2*self.d_a + self.d_b)*h/6, self.d_a/2, (self.d_b - self.d_a)/(6*h)]
    
    def plot(self, ax, x_plot, label="Spline Cubic Interpolation"):
        super().plot(ax, x_plot, label)