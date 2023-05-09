"""
Leia um número real e imprima a quinta parte deste número
"""
# Solicita ao usuário para digitar um número real
num_real = float(input("Digite um número real: "))

# Calcula a quinta parte deste número
quinta_parte = num_real / 5

# Imprime a quinta parte deste número
print("A quinta parte do número digitado é:", quinta_parte)

print(f'A posição do quinto número é: {str(num_real)[5]}')
