cont= 0
while cont == "S" or cont == "s":
    n1 = float(input("Digite uma nota! "))
    n2 = float(input("Digite outra nota! "))
    total = (n1 + n2)/2

    if total >= 7:
        print("Aluno Aprovado")
    elif total <=4:
        print("Aluno de Recuperação")
    else:
            print("Reprovado")




input("Deseja continuar? ")