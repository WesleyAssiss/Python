"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius
A formula de conversão é C = K - 273.15, sendo C a temperatura em
em Celsius e K a tempertatura em Kelvin
"""

# Solicita ao usuário que digite a temperatura em Kelvin
temp_Kelvin = float(input("Digite a temperatura em graus Kelvin: "))

# Converte a temperatura para Celsius usando a fórmula C = 5.0 *(F - 32.0)/9.0
temp_celsius = (temp_Kelvin - 273.15)

# Imprime o resultado da conversão
print(f"A temperatura em Celsius é: {temp_celsius:.2f}°C")
