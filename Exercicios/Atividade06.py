"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit
A formula de conversão é F = C *(9.0/5.0)+32.0, sendo F a temperatura em
Fahrenheit e C a temperatura em Celsius
"""

# Solicita ao usuário que digite a temperatura em Celsius
temp_celsius = float(input("Digite a temperatura em graus Celsius: "))

# Converte a temperatura para Fahrenheit usando a fórmula F = C * (9/5) + 32
temp_fahrenheit = temp_celsius * (9.0/5.0) + 32.0

# Imprime o resultado da conversão
print(f"A temperatura em graus Fahrenheit é: {temp_fahrenheit:.0f}°C")
