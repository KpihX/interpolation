from .spline3_poly import *

class Spline3Polys:
    def __init__(self, x, y, name="P"):
        n = len(x)
        assert n == len(y)
            
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        # print(np.concatenate([[0], self.y2_values(), [0]]))
        self.y2 = np.concatenate([[0], self.y2_values(), [0]])
        self.name = name
        # print(self.x, self.y, self.y2, sep="\n")
        self.polynomials = [Spline3Poly(self.x[i], self.x[i+1], self.y[i], self.y[i+1], self.y2[i], self.y2[i+1]) for i in range(n-1)]
        # print(x_uniform, y_uniform)
        # for poly in self.polynomials:
        #     print(poly.a, poly.b, poly.y_a, poly.y_b, poly.horner_eval(poly.a), poly.horner_eval(poly.b))
        #     poly.plot(ax, np.linspace(poly.a, poly.b, n_plot), "Uniform Cubic Spline Interpolation of f")

        
        
    def y2_values(self):
        n = len(self.x)-1
        h = [self.x[i+1] - self.x[i] for i in range(n)]
        lamda = [self.x[i+2] - self.x[i] for i in range(n-1)]
        beta = [(self.y[i+1]-self.y[i])/h[i] for i in range(n)]
        # print([[2*lamda[0], h[1]] + [0] * (n-3)])
        # print("**", [[0] * (i-1) + [h[i], 2*lamda[i], h[i+1]] + [0] * (n-i-3) for i in range(1, n-2)])
        A = np.array([[2*lamda[0], h[1]] + [0] * (n-3)] + [[0] * (i-1) + [h[i], 2*lamda[i], h[i+1]] + [0] * (n-i-3) for i in range(1, n-2)] + ([[0] * (n-3) + [h[n-2], 2*lamda[n-2]]] if n >= 3 else []))
        B = 6 * np.array([beta[i+1]-beta[i] for i in range(n-1)])
        return np.linalg.solve(A, B)
        
    def horner_eval(self, x0):
        before_x0 = 0
        for i in range(1, len(self.x)):
            if self.x[i] > self.x[before_x0] and x0 >= self.x[i]:
                before_x0 = i
                
        if before_x0 == len(self.x)-1:
            return self.y[-1]
            
        if before_x0 == 0 and self.x[0] > x0:
            raise ValueError(f"!{x0} est avant la plage des abscisses!")
        # print("***", self.x[before_x0], self.x[before_x0+1], x0)
        
        return self.polynomials[before_x0].horner_eval(x0)
    
    def plot(self, ax, n_plot = 100, label="P"):
        x_plot = np.linspace(min(self.x), max(self.x), n_plot)
        y_plot = [self.horner_eval(x) for x in x_plot]
        ax.plot(x_plot, y_plot, label=label)
        ax.legend()