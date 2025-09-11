# 20250909 - Aula 5
#Funções

# Definições
a=int(input("Digite valor de a: "))
b=int(input("Digite valor de b: "))
c=0

#Funções
def soma():
    c = a + b
    print(c)
    return c

def main():
    c = soma()
    d = int(c) + 1
    print(d)

# Executando
if __name__ == "__main__":
    main()