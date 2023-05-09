"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin
A formula de conversão é K = C + 273.15, sendo C a temperatura em
em Celsius e K a tempertatura em Kelvin
"""


# Solicita ao usuário que digite a temperatura em Kelvin
temp_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte a temperatura para Celsius usando a fórmula C = 5.0 *(F - 32.0)/9.0
temp_Kelvin = (temp_celsius - 273.15)

# Imprime o resultado da conversão
print(f"A temperatura em Kelvin é: {temp_Kelvin:.2f}°C")
