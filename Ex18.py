

numero=int(input("Digite um numero"))
opcao=input("Digite 1 para antecessor \n"
                 "2 para sucessor\n"
                 "3 para finalizar: ")
while True:
    if opcao == "1" :
        print(f" O antecessor de {numero} é {numero -1}")
    elif opcao == "2" :
        print(f" O sucessor de {numero} é {numero +1}")
    elif opcao == "3" :
        break
    else:
        print("Opçao invalida")