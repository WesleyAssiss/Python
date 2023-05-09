"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
A fórmula de conversão é C = P * 2.54, sendo C o comprimento em centimetros
e P o comprimento em polegadas.
"""

polegadas = float(input("Digite o valor em polegadas: "))
centimetros = polegadas * 2.54

print(f"O valor em centímetros é: {centimetros:.2f}cm")