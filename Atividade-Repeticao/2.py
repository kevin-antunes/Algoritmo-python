# Crie um programa no qual o usuário informe o código do cargo de um funcionário (ver
# tabela abaixo) e o seu respectivo salário. Para encerrar a leitura dos dados, defina uma
# condição de parada (por exemplo, código do cargo igual a zero). Ao fim, o programa deve
# informar a média salarial dos nutricionistas.

soma = 0
qtdNutricionistas = 0
while True :
    codigoCargo = int(input("Informe o código do cargo :"))
    if codigoCargo == 0 :
        break
    salario = float(input("Informe o salário :"))
    if codigoCargo == 2 :
        soma += salario #soma = soma + salario
        qtdNutricionistas += 1
    
if qtdNutricionistas > 0 :
    media = soma/qtdNutricionistas
    print("A média salarial dos nutricionistas é :", media)
else :
    print("Nenhum nutricionista informado")
    

