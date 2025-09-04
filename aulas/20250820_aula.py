# Aula
# Variáveis e constantes

# import


# Declarações
firstName = "joão"
lastName = "Silva"
name = firstName + ' ' + lastName
valorHora = 45.36
valorHoraAprox = int(valorHora)
diasTrabalhados = 30
HORASTRABALHADAS = 8.5
HORASTRABALHADASAJUST = float(HORASTRABALHADAS)
vencimento = (HORASTRABALHADASAJUST * valorHora) * diasTrabalhados

dadosFuncionario = [firstName,lastName,vencimento]
dadosFuncionario.append(diasTrabalhados)

#valores = array(valorHora,HORASTRABALHADASAJUST)


# Saídas
print(dadosFuncionario)

print(dadosFuncionario[0] + ' ' + dadosFuncionario[1])
print('R$  ', dadosFuncionario[2])
#print(dadosFuncionario)
#print(f'Funcionário: '{name})
#print(f'Salário Mensal :'{vencimento})