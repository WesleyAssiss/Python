# lê os dados da peça 1
codigo_peca1, qtde_peca1, valor_unitario1 = input().split()
codigo_peca1 = int(codigo_peca1)
qtde_peca1 = int(qtde_peca1)
valor_unitario1 = float(valor_unitario1)

# lê os dados da peça 2
codigo_peca2, qtde_peca2, valor_unitario2 = input().split()
codigo_peca2 = int(codigo_peca2)
qtde_peca2 = int(qtde_peca2)
valor_unitario2 = float(valor_unitario2)

# calcula o valor total a pagar
valor_total = qtde_peca1 * valor_unitario1 + qtde_peca2 * valor_unitario2

# exibe o resultado com duas casas decimais
print(f"VALOR A PAGAR: R$ {valor_total:.2f}")