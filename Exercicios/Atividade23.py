"""
Leia um valor de comprimento em metros e apresente-o convertido em jardas.
A fórmula de conversão é: J = M / 0.91, sendo J o comprimento em jardas
e M o comprimento em metros
"""
M = float(input("Digite um valor em metros: "))
J = M / 0.91

print(f"O valor em jardas é: {J:.2f}jardas")