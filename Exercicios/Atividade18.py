"""
Leia um valor de volume em metros cúbicos m^3 e apresente-o convertido em litros.
A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em
metros cúbicos
"""

metros_cubicos = float(input("Digite o valor em metros cúbicos:"))
litros = 1000 * metros_cubicos

print(f"O valor de volume em litros é: {litros:.0f} Litros")