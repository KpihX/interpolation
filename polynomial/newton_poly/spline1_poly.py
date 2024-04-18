from .newton_interpol_poly import *

class Spline1Poly:
    def __init__(self, x, y, name="P"):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.name = name
        self.polynomials = [NewtonInterpolPoly(self.x[i:i+2], self.y[i:i+2], "") for i in range(len(self.x)-1)]

    def horner_eval(self, x0):
        before_x0 = 0
        for i in range(1, len(self.polynomials)):
            if self.x[i] > self.x[before_x0] and x0 >= self.x[i]:
                before_x0 = i
        if before_x0 == 0 and self.x[0] > x0:
            raise ValueError(f"!{x0} est avant la plage des abscisses!")
        return self.polynomials[before_x0].horner_eval(x0)
    
    def plot(self, ax, label="Spline linear Interpolation of f"):
        ax.plot(self.x, self.y, label=label)
        ax.legend()
        
    def __str__(self) -> str:
        string = (self.name + "(x) =")
        for i, poly in enumerate(self.polynomials):
            string += "\t" + str(poly)[5:] + f"   if x in [{self.x[i]}, {self.x[i+1]}]\n"
            
        return string

