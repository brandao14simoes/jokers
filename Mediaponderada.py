# Media Pondera em Python

# Leia 3 Valores, no caso, Variaveis A,B e C, que são as três notas de um aluno. A seguir
# , calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem pseo 3 e anota C
# tem peso %. Considere que cada nota pode ir de a até 10.0, sempre com uma casa decial.

# Progrma dividido em Três Etapas Entrada, Processamento, Saida
# pesos = A,B,C = 2, 3, 5
# notas = [A, B, C]
# nota = int(input("Digite um numero para as notas?"))

# Entrada
A = float(input("Digite a primeira nota: "))
B = float(input("Digite a segunda nota:  "))
C = float(input("Digite a terceira nota: "))

# Processamento
Media = (A * 2 + B * 3 + C * 5) / 10
MediaFormatada = "{:.1f}".format(Media)

if Media > 7.54:
    print("Você passou, Média =", MediaFormatada)
else:
    print("Você não passou, Média =", MediaFormatada)

# Saída
print("Sua média foi {:.1f}".format(Media))  # Display Media with one decimal place
