''''Perguntar ao usuario quantos alunos tem na sala e crias um array, unidimensional (vetor) com o nome de todos os alunos da sala'''

qtd=int(input("Quantos alunos tem na sala: "))
nome = [" "]*qtd

for y in range(qtd):
    nome[y] = input("Digite o nome do aluno: ")

for x in range (qtd):
    print(nome[x], x)







'''
A = 10
B= [0] = 3
[] [] [] []
0  1  2  3 
int num = 30
float notas []
notas = [0.0]*5 => EM PYTHON
[0.0] [0.0] [0.0] [0.0] [0.0] 
So aceita o tipo de dados que vc colocou int,float 
notas = [0.0]*5
notas [0.0] [0.0] [2] [15] [0.0]
        0    1     2    3    4 
notas [3]= 15
notas [2]= 3
for x in range(5):
  print(notas[x])'''