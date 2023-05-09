"""
Leia um valor de comprimento em centímetros e apresente-o convertido em
polegadas. A fórmula de conversão é P = C/2.54, sendo C o comprimento em
centímetros e P o comprimento em polegadas
"""
centimetros = float(input("Digite o valor em centímetros: "))
polegadas = centimetros / 2.54

print(f"O valor em polegadas é: {polegadas:.0f} pol")