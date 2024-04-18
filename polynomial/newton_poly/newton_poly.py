import numpy as np

from ..utils import number_wrapper

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
    
    def __str__(self, nb_dec_digits = 6):
        first_term = round(self.coefficients[0], nb_dec_digits)
        terms = [f"{first_term}"] if first_term != 0 else []
        term = ""
        for i in range(0, len(self.coefficients)-1):
            coef_str = number_wrapper(self.coefficients[i+1], nb_dec_digits)
            if coef_str == "":
                continue
            val = round(self.x[i], nb_dec_digits)
            term += f"(x - {val})" if val > 0 else f"(x + {-val})" if val < 0 else "x"
            terms.append(f"{coef_str} * " + term)
        return self.name + "(x) = " + " + ".join(terms)
