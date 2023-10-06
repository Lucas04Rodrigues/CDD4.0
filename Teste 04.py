x = 0
soma = 0
alunos= int(input("Digite a quantidade de alunos"))
while x < alunos :
    valores = float(input("Digite uma nota"))
    x=x+1
    soma=soma+valores
media=soma/alunos
print(media)
