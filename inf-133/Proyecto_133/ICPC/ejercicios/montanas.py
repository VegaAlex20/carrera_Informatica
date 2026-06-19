a = list(input())
lista = []
cont = 1
for i in a:
    if i == "+":
        cont += 1
    else:
        cont-= 1
    lista.append(cont)
print(lista.index(max(lista))+1)