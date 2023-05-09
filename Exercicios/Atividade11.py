"""
Leia uma velocidade em m/s(metros por segundo) e apresente-a convertida em
KM/H(quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade em
KM/h e M em m/s
"""


ms = float(input("Digite a valocidade em metros por segundos (m/s): "))

KM_H = ms * 3.6

print(f"A velocidade em quilômetros por hora é: {KM_H:.0f}Km/h")