"""
Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula da conversão é: M = H * 10000, sendo M a área em metros quadrados e
H a área em hectares
"""
H = float(input("Digite o valor da área em hectares: "))
M = H * 10000

print(f"O valor da área em metros quadrados é: {M:.2f}m²")