# Aula 20250902
# Tema: loop, if

# Declarações
alunos = []
notas = []
MEDIA = 6.0
MINIMO = 3.0

for i in range(5):
    # Entradas
    aluno = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))

    alunos.append(aluno)
    notas.append(nota)

    if(float(nota) >= MEDIA ):
        print(f'O aluno está aprovado com nota: {nota}')
    elif(float(nota) >= MINIMO ):
        print(f'O aluno está de recuperação, pois sua nota é {nota}')
    else:
        print(f'O aluno está reprovado, pois sua nota é {nota}')

print(alunos)
print(notas)