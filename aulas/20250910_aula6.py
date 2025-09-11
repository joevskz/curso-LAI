# 20250910 - Aula 6

#Funções: degrau e sigmoide para perceptron

# imports

import numpy as np

# Definições
X = np.random.rand(5)
W = np.random.rand(5)
b = 1
v = 0
beta = 0.25
a = 0

#Funções
def juncaoAditiva():
    u = 0
    print(X)
    print(W)
    for i in range(len(X)):
        v = X[i]*W[i]
        u = u + v
        print(v)
        print(u)
    u = u - b
    print(u)
    return u

def main():
    z = juncaoAditiva()
    print(z)
    a = -1 * beta * z
    y = 1/(1+(np.exp(a)))
    print(f'a saída do neurônio é {y}')

# Executando
if __name__ == "__main__":
    main()


# próxima função: tangente hiperbólica; resolução de sistemas lineares (operações com matrizes)