tam = int(input("Informe o tamanho da lista"))
lista = []

for i in range(tam):
    valor = int(input("Informe um valor"))
    lista.append(valor)

for i in range(0, len(lista)-1):
    menor = lista[i]
    for j in range(i+1,len(lista)):
        if menor>lista[j]:
            menor = lista[j]
            aux = j
            print(menor)
#localizamos o menor e precisamos colocar na posição correta
lista[aux] = lista[i]
lista[i] = menor

lista[i],lista[aux] = lista[aux], lista[i]

print(lista)
