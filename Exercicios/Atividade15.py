"""
Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula
da conversão é: G = R * 180 / Pi, sendo G o ângulo em graus e R em radianos
e Pi = 3.14
"""

import math

radianos = float(input("Digite o ângulo em radianos: "))
graus = radianos * 180 / math.pi

print(f"O ângulo em graus é: {graus:.0f}°C")