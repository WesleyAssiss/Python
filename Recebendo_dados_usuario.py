"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

exemplos:
- Aspas simples -> 'Angelina Jolie'
- Aspas duplas -> "Angelina Jolie"
- Aspas simples triplas -> '''Angelina Jolie'''
"""
# Aspas duplas triplas -> """Angelina Jolie"""


# Entrada de dados
# print("Qual seu nome? ")
# nome = input()  # Input -> Entrada

nome = input("Qual o seu nome? ")

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a): %s' % nome) # Não é muito utilizado
# print('Seja bem-vindo(a) {0}'.format(nome))  # Bastante utilizado
print(f'Seja bem-vindo(a) {nome}')  # Bastante utilizado
# print("Qual a sua idade? ")
# idade = input()

# idade = input("Qual a sua idade? ")
idade = int(input("Qual a sua idade? "))
# Processamento


# Saída de dados
# Exemplo de print 'antigo' 2.x
# print('%s tem %s anos' % (nome, idade)) # Não é muito utilizado
# print('{0} tem {1} anos'.format(nome, idade))  # Bastante utilizado
print(f'{nome} tem {idade} anos')  # Bastante utilizado

# int(idade) -> cast
# Cast é a 'conversão' de um tipo de dado para outro

# print(f'{nome} nasceu em {2023 - int(idade)}')
print(f'{nome} nasceu em {2023 - idade}')
