import numpy as np

class TaylorPolynomial:
    def __init__(self, coefficients, a, name="P"):
        self.coefficients = np.array(coefficients, dtype=float)
        self.a = a
        self.name = name
        
    def horner_eval(self, x0):
        n = len(self.coefficients)
        result = self.coefficients[-1]
        for i in range(n - 2, -1, -1):
            result = result * (x0 - self.a) + self.coefficients[i]
        return result
    
    def plot(self, ax, x_plot, label="P"):
        y_plot = [self.horner_eval(x) for x in x_plot]
        ax.plot(x_plot, y_plot, label=label)
        ax.legend()
    
    def __str__(self):
        nb_dec_digits = 3
        terms = [f"{self.coefficients[0]}"] if self.coefficients[0] != 0 else []
        factor = f"(x - {round(self.a, nb_dec_digits)})" if self.a != 0 else "x"
        for i in range(1, len(self.coefficients)):
            if self.coefficients[i] == 0:
                continue
            terms.append(f"{round(self.coefficients[i], nb_dec_digits)} * " + factor + f"^{i}")
        return self.name + "(x) = " + " + ".join(terms)
