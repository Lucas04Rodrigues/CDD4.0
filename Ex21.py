
qtd=int(input("Quantos alunos tem na sala: "))
nome = [" "]*qtd
achou=0
resp = "s"
for x in range(qtd):
   nome[x] = input("Digite o nome do aluno: ")
while resp == "s":
    pesquisa=input("Qual aluno deseja encontrar ?")
    for j in range (qtd):
        if pesquisa == nome[j]:
            achou=achou+1
            print(f"O aluno {nome[j]} esta na posição {j} ")
    if achou ==0:
        print(f"O nome {pesquisa} não esta na lista")
    if achou != nome:
        print("Nome invalido, digite um nome valido")

#qtd=int(input("Quantos alunos tem na sala: "))
#nome = [" "]*qtd

#for y in range(qtd):
 #   nome[y] = input("Digite o nome do aluno: ")

#or x in range (qtd):
 #   print(nome[x], x)'''