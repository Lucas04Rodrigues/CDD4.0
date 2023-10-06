senha = 12345
codigo1= int(input("Digite a senha"))
con= 0
while codigo1 != senha:
    codigo1 = int(input("Senha invalida,Digite novamente:"))
    con+= 1
    if con>=3:
        print("Senha bloqueado")
        break
else:
    print("Login efetuado com sucesso")
print("programa finalizado!!")
