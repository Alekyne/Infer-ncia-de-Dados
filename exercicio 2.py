'''import math

def f(x):
    return 6 * x - 4 * math.log1p(x - 2) - 3 * math.log1p(25 - x)


def df(x):
    return 6 - 4 / (x - 2) + 3 / (25 - x)

def newton_method(x0, iterations):
    x = x0
    results = []

    for i in range(iterations):
        fx = f(x)
        dfx = df(x)
        x = x - fx / dfx
        results.append((i + 1, x))

    return results

# Definindo os dados iniciais
x0 = 3.5
num_iterations = 5

# Executando o método de Newton
results = newton_method(x0, num_iterations)

# Imprimindo a tabela de resultados
print("Iteração\tValor de x")
for iteration, x in results:
    print(f"{iteration}\t\t{x}")
'''



import math

def f(x):
    return 6 * x - 4 * math.log1p(x - 2) - 3 * math.log1p(25 - x)


def df(x):
    return 6 - 4 / (x - 2) + 3 / (25 - x)

def newton_method(x0, iterations):
    x = x0
    results = []

    for i in range(iterations):
        fx = f(x)
        dfx = df(x)
        x = x - fx / dfx
        results.append((i + 1, x))

    return results

# Definindo os dados iniciais
x0_values = [2.6, 3.5, 4.2, 5.0, 6.1]
num_iterations = 5

# Executando o método de Newton para cada valor inicial
for x0 in x0_values:
    results = newton_method(x0, num_iterations)

    # Imprimindo a tabela de resultados para cada valor inicial
    print(f"Resultados para x0 = {x0}")
    print("Iteração\tValor de x")
    for iteration, x in results:
        print(f"{iteration}\t\t{x}")
    print()


'''
import math

def f(x):
    return 6 * x - 4 * math.log(x - 2) - 3 * math.log(25 - x)

def df(x):
    return 6 - 4 / (x - 2) + 3 / (25 - x)

def newton_method(x0, iterations):
    x = x0
    results = []

    for i in range(iterations):
        try:
            fx = f(x)
            dfx = df(x)
            x = x - fx / dfx
            results.append((i + 1, x))
        except ValueError:
            results.append((i + 1, None))
            break

    return results

# Definindo os dados iniciais
x0_values = [2.6, 3.5, 4.2, 5.0, 6.1]
num_iterations = 5

# Executando o método de Newton para cada valor inicial
for x0 in x0_values:
    results = newton_method(x0, num_iterations)

    # Imprimindo a tabela de resultados para cada valor inicial
    print(f"Resultados para x0 = {x0}")
    print("Iteração\tValor de x")
    for iteration, x in results:
        if x is None:
            print(f"{iteration}\t\tNão convergiu")
        else:
            print(f"{iteration}\t\t{x}")
    print()'''


