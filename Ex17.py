#Receba numeros que o usuario digitar e some com o limite de até 1000
soma=0
quantidade =int(input("Quantos numeros são"))
for i in range(quantidade):
    numero=int(input("Digite um numero"))
    soma= soma + numero
    if soma > 1000:
        break
media = soma / quantidade
print(soma)


