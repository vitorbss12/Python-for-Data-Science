from typing import List


idade = [10, 20, 15, 30]


def verifica_idade(idade):
    if idade >= 18:
        print(f"{idade} - Você é maior de idade!")
    else:
        print(f"{idade} - Você é menor de idade!")


for i in idade:
    verifica_idade(i)


def verifica_idade_com_for(idade):
    for i in idade:
        if i >= 18:
            print(f"{i} - Você é maior de idade!")
        else:
            print(f"{i} - Você é menor de idade!")


verifica_idade_com_for(idade)

# Booleano

permissoes: List = []
idades = [20, 14, 40]


def verifica_idade_boleano(permissoes, idades):
    for i in idades:
        if i >= 18:
            permissoes.append(True)
        else:
            permissoes.append(False)
    for j in permissoes:
        if j:
            print("Você é maior de idade!")
        else:
            print("Você é menor de idade!")


verifica_idade_boleano(permissoes, idades)
