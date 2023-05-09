"""
Leia uma velocidade em KM/H(quilômetros por hora) e apresente-a convertida em
m/s(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
KM/h e M em m/s
"""

KM_H = float(input("Digite a valocidade em quilômetros por hora (KM/H): "))

ms = KM_H / 3.6

print(f"A velocidade em metros por segundo é: {ms:.2f}m/s")