# 20250909 - Aula 5
#Funções

# imports

import numpy as np

# Definições
X = np.random.rand(5)
W = np.random.rand(5)
b = 1
v = 0
u = 0

#Funções
def juncaoAditiva():
    u = 0
    print(X)
    print(W)
    for i in range(len(X)):
        v = X[i]*W[i]
        print(v)
        u = u + v
        print(v)
        print(u)# 20250909 - Aula 5
#Funções

# imports

import numpy as np

# Definições
X = np.random.rand(5)
W = np.random.rand(5)
b = 1
v = 0

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
    if (z >= 0):
        y = 1
        print(f"A rede neural foi ativsada com valor igual a {y} ")
    elif (z < 0):
        y = 0
        print(f"A rede neural foi desativsada")

# Executando
if __name__ == "__main__":
    main()