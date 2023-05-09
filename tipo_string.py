"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True','42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True","42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''','''42.3'''
"""

# - Estiver entre aspas simples triplas -> """uma string""", """234""", """a""", """True""","""42.3"""
nome = 'Geek University'
print(nome)
print(type(nome))

"""
[::-1] -> Comce do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1])# Inversão da String Pythônico
print(nome.replace('e','i'))
print(type(nome))

texto = 'socorram me subino onibus em marrocos' # Palíndromo
print(texto)
print(texto[::-1])

nome = 'ana' # Palíndromo
print(nome)
print(nome[::-1])