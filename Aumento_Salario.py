# Aumento de Salario percentual apartir do Salario


salario = float(input("Digite seu salario:"))

if salario <= 400:
    percentual = "15%"
    reajuste = salario * 0.15
elif salario <= 400 and salario <=800:
        percentual = "12%"
        reajuste = salario * 0.12
elif 800.01 <= salario < 1200.00:
    percentual = "7,5%"
    reajuste = salario * 0.075
elif 1200.01 <= salario 2000.00:
    percentual = "6%"
    reajuste = salario * 0.06
else: 
    percentual = "3%"
    reajuste = salario * 0.03


    