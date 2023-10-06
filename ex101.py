def estoque (produto,quantidade,valor):
   vTotal=quantidade*valor
   print(f"O valor total é {vTotal}")
def vogais(texto):
   cont=0
   for x in texto:
      if x in "aeiouAEIOU":
         cont+=1
   print(f"Quantidade de vogais {cont}")