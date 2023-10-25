# Calculo de area

# Entrada 
A, B, C = map(float, input("Digite A, B, C: \n").split())


# Processamento
triangulo = (A * C)/2.0
circulo = 3.14159 * C ** 2
trapezio = ((A + B )* C)/2.0
quadrado = B ** 2
retangulo = A * B

# Saida

print("Triangulo",str("%.3f"%triangulo))
print("Circulo", str("%.3f"%circulo))
print("Trapezoido", str("%.3f"%trapezio))
print("Quadrado", str("%.3f"%quadrado))
print("Retangulo",str("%.3f"% retangulo))
