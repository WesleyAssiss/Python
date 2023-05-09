"""
Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor
correspondente em dólares
"""
valor_reais = float(input("Digite o valor em reais: "))
cotacao_dolar = float(input("Digite a cotação do dólar: "))

valor_dolares = valor_reais / cotacao_dolar

print(f"O valor em dólares é: ${valor_dolares:.2f}")
