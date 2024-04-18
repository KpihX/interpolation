import numpy as np
from ..utils import number_wrapper

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

    def __str__(self, nb_dec_digits = 6):
        first_term = round(self.coefficients[0], nb_dec_digits)
        terms = [f"{first_term}"] if first_term != 0 else []
        val = round(self.a, nb_dec_digits)
        factor = f"(x - {val})" if val > 0 else f"(x + {-val})" if val < 0 else "x"
        for i in range(1, len(self.coefficients)):
            coef_str = number_wrapper(self.coefficients[i], nb_dec_digits)
            if coef_str == "":
                continue
            terms.append(f"{coef_str} * " + factor + (f"^{i}" if i >= 2 else ""))
        return self.name + "(x) = " + " + ".join(terms)