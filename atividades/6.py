nota1 = float(input("Informe a primeira nota"))
nota2 = float(input("Informe a segunda nota"))

media = (nota1+nota2)/2
if media >= 9 :
    conceito = "A"
    situação = "aprovado"
elif media >= 7.5 :
    conceito = "B"
    situação = "aprovado"
elif media >= 6 :
    conceito = "C"
    situação = "aprovado"
elif media >= 4 :
    conceito = "D"
    situação = "reprovado"
else :
    conceito = "E"
    situação = "reprovado"
    

