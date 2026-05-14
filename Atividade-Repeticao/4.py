
total_aluno = 0
aprovado = 0
reprovado = 0 
matricula = 0
matricula = int(input("Informe sua matricula :"))
while matricula != 9999 :
    nota1 = int(input("Informe a primeira nota :"))
    nota2 = int(input("Informe a segunda nota :"))
    nota3 = int(input("Informe a terceira nota :"))
    media_final = ((2 *nota1)+(3* nota2)+(4* nota3))/9
    if media_final >= 5 :
        print("Matricula :", matricula)
        print("Aprovado com média :",media_final)
        aprovado = aprovado+1#Aprovado +=1
    else :
        print("Matricula : ",matricula)
        print("Reprovado com média :", media_final)
        reprovado = reprovado+1#Reprovado +=1
    matricula = int(input("Informe sua matricula :"))
total_alunos = aprovado=reprovado
print("Total de Aprovados",aprovado)
print("Total de Reprovados",reprovado)  
print("Total de alunos", total_alunos)
