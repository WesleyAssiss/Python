"""
Leia um valor de comprimento em jardas e apresente-o convertido em metros.
A fórmula de conversão é: M = 0.91 * J, sendo J o comprimento em jardas
e M o comprimento em metros.
"""

jardas = float(input("Digite o valor do comprimento em jardas: "))
metros = 0.91 * jardas

print(f"O valor do comprimento em metros é: {metros:.2f}m")