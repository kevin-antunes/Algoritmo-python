#1) Escreva um programa que peça dois números inteiros e imprima todos os
#números inteiros entre eles.





inicio = int(input("Informe um número inicial :"))
fim = int(input("informe um final :"))

# Se o for for maior  que o y, o que acontece?
if inicio < fim:
    for i in range(inicio+1,fim):
        print(i)
else:
    for i in range(inicio+1,fim,-1):
        print(i)