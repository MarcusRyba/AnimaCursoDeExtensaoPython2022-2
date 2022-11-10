# Meu Primeiro Projeto Python
print("Alo mundo!")



'''
comentario em bloco 
'''

nome = "Marcus ryba"
idade = 19 

print(nome)

print("Alo mundo!")


print("Minha idade é "+str(idade)+" anos")
print(f"Minha idade é {idade} anos")
print("Minha idade é {} anos".format(idade))

print("Meu nome é {} e tenho {} anos".format(nome, idade))
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Você é xóven ainda, xóven ainda...")

genero = input("Informe o gênero M=Masculino, F=Feminino, O=Outros: ")
if idade >= 18 and genero == "M":
  print("... e você também precisa/precisou prestar o serviço militar obrigatório")



print("vai ser executada de qualquer jeito")