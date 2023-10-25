# Programa que ler o nome do Vendedor, o seu salario e o total de vendas
# efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15%
# de comissão sobre suas vendas efetuadas, informar o total a receber no final do
# mês cmom duas casas decimais

# Entrada
Vendedor = str(input("Digite nome do Funcionario: "))
Salario = float(input("Digite Salario do Vendedor: "))
Total_de_vendas = float(input(f"Digite Total de vendas realizadas pelo {Vendedor}: "))

# Processamento
salario_final = Salario  + Total_de_vendas*0.15
salario_final = str("%.2f"%salario_final)

# Saida
print(f"{Vendedor} Tem o salario de", salario_final)