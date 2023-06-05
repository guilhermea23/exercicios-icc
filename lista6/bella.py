qtd_convidados = int(input())
lista_festa = []
andre_vai = False

for i in range(qtd_convidados):
    nome = input()
    lista_festa.append(nome)

if "André" in lista_festa:
    andre_vai = True
    
if andre_vai:
    print("Cuidado!")
else:
    print("Seguro!")
