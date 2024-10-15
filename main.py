import numpy as np
from sympy import symbols, sympify, diff, lambdify

# Método de Newton
def newton(f, df, x0, tol, max_iter=100, iteration=0):
    print(f"Iteração {iteration}: x = {x0}")
    if np.abs(f(x0)) < tol:
        return x0
    elif iteration >= max_iter:
        print("Máximo de iterações atingido.")
        return x0
    elif df(x0) == 0:
        print("Derivada igual a zero. Não é possível continuar.")
        return x0
    else:
        return newton(f, df, x0 - f(x0)/df(x0), tol, max_iter, iteration + 1)

# Método da Bisseção
def bissecao(f, a, b, tol, max_iter=100):
    if f(a) * f(b) >= 0:
        print("A função deve mudar de sinal no intervalo dado.")
        return None
    
    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        print(f"Iteração {iteration}: a = {a}, b = {b}, c = {c}")
        if np.abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration += 1

    print("Máximo de iterações atingido.")
    return (a + b) / 2

# Método do Ponto Fixo
def ponto_fixo(g, x0, tol, max_iter=100):
    iteration = 0
    while iteration < max_iter:
        x1 = g(x0)
        print(f"Iteração {iteration}: x = {x1}")
        if np.abs(x1 - x0) < tol:
            return x1
        x0 = x1
        iteration += 1
    print("Máximo de iterações atingido.")
    return x0

# Método da Secante
def secante(f, x0, x1, tol, max_iter=100):
    iteration = 0
    while iteration < max_iter:
        if np.abs(f(x1)) < tol:
            return x1
        x_temp = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        print(f"Iteração {iteration}: x0 = {x0}, x1 = {x1}, novo x = {x_temp}")
        x0, x1 = x1, x_temp
        iteration += 1
    print("Máximo de iterações atingido.")
    return x1

# Método Regula Falsi (Falsa Posição)
def regula_falsi(f, a, b, tol, max_iter=100):
    if f(a) * f(b) >= 0:
        print("A função deve mudar de sinal no intervalo dado.")
        return None
    
    iteration = 0
    while iteration < max_iter:
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        print(f"Iteração {iteration}: a = {a}, b = {b}, c = {c}")
        if np.abs(f(c)) < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration += 1

    print("Máximo de iterações atingido.")
    return c

def main():
    x = symbols('x') 
    
    f_input = input("Digite a função em relação à x: ")
    f_sym = sympify(f_input)

    # Converter a função simbólica em função numérica com numpy
    f = lambdify(x, f_sym, 'numpy')

    # Exibir o menu
    print("\nEscolha o método para calcular a raiz:")
    print("1 - Método de Newton")
    print("2 - Método da Bisseção")
    print("3 - Método do Ponto Fixo")
    print("4 - Método da Secante")
    print("5 - Método Regula Falsi")

    metodo = input("Digite o número correspondente ao método: ").strip()

    try:
        precision = float(input("Precisão: "))
    except ValueError:
        print("Erro: Entrada inválida.")
        return

    if metodo == "1":
        try:
            x0 = float(input("x0: "))
        except ValueError:
            print("Erro: Entrada inválida.")
            return

        # Calcula derivada
        f_prime_sym = diff(f_sym, x)
        f_prime = lambdify(x, f_prime_sym, 'numpy')

        # Executar método de Newton
        estimate = newton(f, f_prime, x0, precision)
        print("Estimativa final pelo método de Newton =", estimate)

    elif metodo == "2":
        try:
            a = float(input("a (limite inferior do intervalo): "))
            b = float(input("b (limite superior do intervalo): "))
        except ValueError:
            print("Erro: Entrada inválida.")
            return

        # Executar método da bisseção
        estimate = bissecao(f, a, b, precision)
        if estimate is not None:
            print("Estimativa final pelo método da Bisseção =", estimate)

    elif metodo == "3":
        g_input = input("Digite a função g(x) para o método do ponto fixo: ")
        g_sym = sympify(g_input)
        g = lambdify(x, g_sym, 'numpy')

        try:
            x0 = float(input("x0: "))
        except ValueError:
            print("Erro: Entrada inválida.")
            return

        # Executar método do Ponto Fixo
        estimate = ponto_fixo(g, x0, precision)
        print("Estimativa final pelo método do Ponto Fixo =", estimate)

    elif metodo == "4":
        try:
            x0 = float(input("x0: "))
            x1 = float(input("x1: "))
        except ValueError:
            print("Erro: Entrada inválida.")
            return

        # Executar método da Secante
        estimate = secante(f, x0, x1, precision)
        print("Estimativa final pelo método da Secante =", estimate)

    elif metodo == "5":
        try:
            a = float(input("a (limite inferior do intervalo): "))
            b = float(input("b (limite superior do intervalo): "))
        except ValueError:
            print("Erro: Entrada inválida.")
            return

        # Executar método Regula Falsi
        estimate = regula_falsi(f, a, b, precision)
        if estimate is not None:
            print("Estimativa final pelo método Regula Falsi =", estimate)

    else:
        print("Método inválido. Escolha entre '1', '2', '3', '4' ou '5'.")

if __name__ == "__main__":
    main()
