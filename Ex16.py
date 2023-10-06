#Faça um codigo que receba o valor da base e da aultura de um tiangulo e calcule sua area. usando a formula
 #A= (base * altura)/2
resposta= "s"
while resposta == "s" or resposta =="S":
    base= float(input("Digite um base"))
    while base == 0:
        base("numero invalido tente novamente:  ")
    altura= float(input("Digite outro altura"))
    while altura == 0:
        altura("numero invalido tente novamente:  ")

    A = (base * altura) /2
    print(f"Os valores da soma é ", A, "cm²" )
    resposta = input("Deseja continuar (s/n)? ")



