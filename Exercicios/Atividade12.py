"""
Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula
de conversão é: K = 1,61 * M, sendo K a distância em quilômetros e M em milhas.
"""

dist_milhas = float(input("Digite a distância em milhas: "))

dist_quilometros = 1.61 * dist_milhas

print(f"A distância em quilômetros é: {dist_quilometros:.0f}Km")