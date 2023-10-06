#Faça um algotitmo que leia idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa
#apenas em dias. considera

anos=int(input("Informe  seu ano: "))
meses=int(input("Informe  sua meses: "))
dias=int(input("Informe  sua dia: "))

idadedias=anos*365+meses*30+dias

print(f"Voce viveu {idadedias} dias")