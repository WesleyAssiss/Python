"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula
da conversão é: R = G * Pi / 180, sendo G o ângulo em graus e R em radianos
e Pi = 3.14
"""
import math

graus = float(input("Digite o ângulo em graus: "))
radianos = graus * math.pi / 180

print(f"O ângulo em radianos é: {radianos:.2f} rad")