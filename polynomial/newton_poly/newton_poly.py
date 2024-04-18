import numpy as np

class NewtonPolynomial:
    def __init__(self, coefficients, x, name="P"):
        assert len(coefficients) == len(x) + 1
        self.coefficients = np.array(coefficients, dtype=float)
        self.x = np.array(x, dtype=float)
        self.name = name
        
    def horner_eval(self, x0):
        n = len(self.coefficients)
        result = self.coefficients[-1]
        for i in range(n - 2, -1, -1):
            result = result * (x0 - self.x[i]) + self.coefficients[i]
        return result
    
    def plot(self, ax, x_plot, label="P"):
        y_plot = self.horner_eval(x_plot)
        ax.plot(x_plot, y_plot, label=label)
        ax.legend()
    
    def __str__(self):
        nb_dec_digits = 3
        terms = [f"{self.coefficients[0]}"] if self.coefficients[0] != 0 else []
        term = ""
        for i in range(0, len(self.coefficients)-1):
            if self.coefficients[i+1] == 0:
                continue
            term += f"(x - {round(self.x[i], nb_dec_digits)})" if self.x[i] != 0 else "x"
            terms.append(f"{round(self.coefficients[i+1], nb_dec_digits)} * " + term)
        return self.name + "(x) = " + " + ".join(terms)
