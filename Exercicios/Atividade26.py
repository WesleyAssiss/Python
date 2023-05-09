"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em
hectares. A fórmula da conversão é: H = M * 0.0001, sendo M a área em
metros quadrados e H a área em hectares.
"""

M = float(input("Digite o valor da área em metros quadrados: "))
H = M * 0.0001

print(f"O valor da área em hectares é: {H:.2f}ha")