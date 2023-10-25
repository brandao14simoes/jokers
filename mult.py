# Leia 2 valores inteiros (A e B). Ápos, o programa deve mostrar uma mensagem
# são multiplos ou não multiplos, indicando se os valores lidos são multiplos entre si

# Entrada
A, B = map(int, input("Digite os dois numeros:\n").split())

if A % B  == 0 or B % A == 0:
    print("Multiplos")
else:
    print("Não são Multiplos")
