"""
Leia quatro notas, calcule a média aritmética e imprima o resultado
"""
nota1,nota2,nota3,nota4 = map(float, input("Digite as quatros notas: ").split())

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média aritmética das quatro notas é: {media}")

"""
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A média aritmética das quatro notas é: ", media)

"""