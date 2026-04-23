salario = float(input("informe salário"))

if salario <= 280 :
    per_aumento = 20
elif salario <= 700 :
    per_aumento = 15
elif salario <= 1500 :
    per_aumento = 10
else :
    per_aumento = 5
if salario <= 0 :
    print("salário inválido")
else :
    aumento = salario*per_aumento/100
    
    print("sal.antes registro", salario)
    print("% de aumento", per_aumento)
    print("valor do aumento", aumento)
    print("novo salario", salario + aumento)



