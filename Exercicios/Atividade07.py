"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius
A formula de conversão é C = 5.0 *(F - 32.0)/9.0, sendo F a temperatura em
Fahrenheit e C a temperatura em Celsius
"""

# Solicita ao usuário que digite a temperatura em Fahrenheit
temp_fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura para Celsius usando a fórmula C = 5.0 *(F - 32.0)/9.0
temp_celsius = 5.0 * (temp_fahrenheit - 32.0)/9.0

# Imprime o resultado da conversão
print(f"A temperatura em graus Celsius é: {temp_celsius:.0f}°C")
