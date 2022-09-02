nome = "Vitor"
idade = 24


# print("Olá, meu nome é", nome, "e tenho", idade, "anos.")
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")


def saudacao():
    nome_input = input("Qual é o seu nome? ")
    print(f"Olá, {nome_input}!")


saudacao()


def nome_completo():
    primeiro_nome = input("Qual é o seu primeiro nome? ")
    sobrenome = input("Qual é o seu sobrenome? ")
    nome_inteiro = primeiro_nome + " " + sobrenome
    print(f"Olá, {nome_inteiro}!")


nome_completo()


def saudacao_parametro(nome):
    print(f"Olá, {nome}!")


saudacao_parametro("Vitor")
