"""
Tipo Numérico

2**63 (2^63)-> 9223372036854775808 o maior número que posso armazenar em inteiro no Java
Ctrl + L -> Limpa o terminal
"""
num = 1_000_000

print(num)

print(float(num))

"""
Tipo float
Tipo real, decimal
Casas decimais
Obs: O separador de casas decimais na programação é o ponto e não a virgula.
"""
# Errado do ponto de vista Float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

# É possivel fazer dupla atribuição
valor1, valor2 = 3, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: AO converter valores float para inteiros, nós perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
res = variavel ** 2
print(res)

"""
Tipo Booleano
Álgebra Booleana, criada por George Boole
2 constantes, verdadeiro ou falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial minuscula

Errado:
true,false
Certo:
True,False
"""
ativo = False
print(ativo)

"""
Operações básicas:
"""
# Negação (not):
"""
Fazendo a negação se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
print(not ativo)
logado = True
# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro
deve ser verdadeiro.
"""
print(True or True)# Verdadeiro
print(True or False)# Verdadeiro
print(False or True)# Verdadeiro
print(False or False)# Falso

print(ativo or logado)

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os
valores devem ser verdadeiros.

print(True or True)# Verdadeiro
print(True or False)# Falso
print(False or True)# Falso
print(False or False)# Verdadeiro
"""

