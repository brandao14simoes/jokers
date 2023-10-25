# Deve-se ler o código de uma peça 1, o número de peças 1, p valor únitario
# de cada peça 1, o código de uma peça 2, o numero de peças 2 e o valor unitário
# de cada peça 2. Após, calcule e mostre o valor a ser pago

# Entrada
ID1, QTD1, Valor1 = map(float, input("Digite info da peça 1: id, qtd, valor\n").split())
ID2, QTD2, Valor2 = map(float, input("Digite info da peça 2: id, qtd#, valor\n").split())


# Processamento
valor_total = (QTD1 * QTD2) + (QTD1 * Valor2)



# Saida
print("Valor a pagar R$:", str("%.2f"%valor_total))
print(f"O total a pagar é R${valor_total}")