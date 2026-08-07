def maior_de_dois(a,b):
    if a>=b :
        return a
    else:
        return b
a = float(input("Informe um valor "))
b = float(input("Informe um valor "))

maior = maior_de_dois(a,b)

print("O maior número é ", maior)