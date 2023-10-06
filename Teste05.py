val1 = float(input("Digite um numero"))
val2 = float(input("Digite outro numero"))
cont= 1
while val2 == 0:
    val2 = float(input("Numero invalido,Digite outro numero"))
    cont+=1
    if cont>4:
        break
else:
    resultado = val1/val2
    print(resultado)
print("Programa finalizado")