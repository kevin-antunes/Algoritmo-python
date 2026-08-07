def Calculadora_Simples(a,b,operador):
    if operador =="+":
        return a+b
    elif operador =="-":
        return a-b
    elif operador =="*":
        return a*b
    elif operador =="/" and b!=0:
        return a/b
    elif operador =="/" and b==0:
        return "não é divisível por zero"
    else:
        return "operação inválida"

x = float(input("Informe um número"))
y = float(input("informe um numero"))