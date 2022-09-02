idade = 20


def verifica_idade(idade):
    if idade >= 18:
        print("Você é maior de idade!")
    else:
        print("Você é menor de idade!")


verifica_idade(idade)


def verifica_idade_sem_parametro():
    idade = input("Digite sua idade: ")
    idade = int(idade)
    if idade >= 18:
        print("Você é maior de idade!")
    else:
        print("Você é menor de idade!")


verifica_idade_sem_parametro()
