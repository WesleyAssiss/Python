"""
Leia uma distância em quilôemtros e apresente-a convertida em milhas. A fórmula
de conversão é: M = K / 1.61, sendo K a distância em quilômetros e M em milhas.
"""
dist_quilometros = float(input("Digite a distância em quilômetros: "))

dist_milhas = dist_quilometros / 1.61

print(f"A distância em milhas é: {dist_milhas:.0f}milhas")
