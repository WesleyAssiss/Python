"""
Leia um valor de massa em libras e apresente-o convertido em quilogramas.
A fórmula de conversão é: K = L * 0.45, sendo K a massa em quilogramas e
L a massa em libras
"""

L = float(input("Digite o valor de massa em libras: "))
M = L * 0.45

print(f"O valor da massa em quilogramas é: {M:.2f}Kg")
