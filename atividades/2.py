# 2. Faça um Programa que leia três números e mostre-os em ordem decrescente

numero1 = int(input("Informe o primeiro número :"))
numero2 = int(input("Informe o segundo número :"))
numero3 = int(input("Informe o terceiro número :"))

if numero1 >= numero2 and numero1 >= numero3 :
    print (numero1)
    if numero2 >= numero3:
        print(numero2)
        print(numero3)
    else :
      print (numero3)
      print(numero2)
elif numero2 >= numero1 and numero2 >= numero3 :
    print (numero2)
    if numero1 >= numero3 :
        print (numero1)
        print (numero3)
    else :
        print (numero3)
        print (numero1)
else :
    print (numero3)
    if numero2 >= numero1 :
        print (numero1)
        print (numero2)
    else :
        print(numero2)
        print(numero1)

