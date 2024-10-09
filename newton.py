import numpy as np  
from sympy import *

def newton(f, df, x0, tol, iteration=0):
    print(f"Iteração {iteration}: x = {x0}")

    if abs(f(x0)) < tol:
        return x0
    else:
        return newton(f, df, x0 - f(x0)/df(x0), tol, iteration + 1)


def main():

    x = symbols('x') 
    
    f_input = input("Digite a função em relação à x: ")
    f_sym = sympify(f_input)

    x0 = float(input("x0: "))
    precision = float(input("Precisao: "))

    # Calcula derivada
    f_prime_sym  = diff(f_sym, x)

    # Converter funções simbólicas para funções numéricas
    f = lambdify(x, f_sym)
    f_prime = lambdify(x, f_prime_sym)

    estimate = newton(f, f_prime, x0, precision)
    print("Estimativa final =", estimate)

if __name__ == "__main__":
    main()
