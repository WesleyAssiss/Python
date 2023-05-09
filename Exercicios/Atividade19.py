"""
Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m^3 .
A fórmula de conversão é: M = L / 1000, sendo L o volume em litros e M o volume em
metros cúbicos
"""
litros = float(input("Digite o valor em metros cúbicos:"))
metros_cubicos = litros / 1000

print(f"O valor de volume em metros cúbicos é: {metros_cubicos:.2f}m³")