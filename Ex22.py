'''Exercício 04
Escreva um código que permita a leitura das notas de uma turma de 5 alunos e
guarde num vetor, Calcular a média da turma e contar quantos alunos obtiveram
média desta media calculada Escrever a média da turma e o resultado
da contagem
'''
contAluno=0
notas= [0]*5
soma=0
for x in range (5):
    notas[x]=float(input("informe a nota: "))

for y in range(5):
    soma+=notas[y]
media=soma/5
for z in range(5):
    if notas[z]>=media:
        contAluno+=1
print(f"A media da sala é {media} e {contAluno} obtiveram notas acima da media. ")