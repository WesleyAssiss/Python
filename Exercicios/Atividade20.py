"""
Leia um valor de massa em quilogramas(Kg) e apresente-o convertido em libras.
A fórmula da conversão é: L = K / 0.45, sendo K a massa em quilogramas e L a massa
em libras.
"""
Kg = float(input("Digite o valor da massa em quilogramas: "))
libras = Kg / 0.45

print(f"O valor da massa em libras é: {libras:.2f} lb")