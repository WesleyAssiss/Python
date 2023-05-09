"""
Faça um programa que leia um número real e o imprima
"""
import re

numero = input("Digite um número real: ")
numero = re.sub(r",", ".", numero)  # substitui ',' ou '.' por '.'
num = float(numero)
print("O número digitado foi:", num)
