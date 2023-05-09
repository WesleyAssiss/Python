"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados
dos três valores lidos
"""
#Exemplo de entrada: 10 20 30
x, y, z= map(float, input("Digite os três valores: ").split())

soma = (x ** 2) + (y ** 2) + (z ** 2)

print(f"O valor da soma dos três valores é: {soma:.2f}m²")


"""
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

soma_quadrados = valor1 ** 2 + valor2 ** 2 + valor3 ** 2

print("A soma dos quadrados dos três valores é: ", soma_quadrados)

"""