# 1) Crie um programa no qual o usuário informe a idade de um número indeterminado de
# alunos. Para encerrar a leitura dos dados, o usuário deve informar uma idade negativa.
# No final, o programa deve mostrar a média aritmética entre a maior e a menor idade


maior = 0
menor = 0
idade = 0

while idade >= 0 :
    idade = int(input("Informe uma idade: "))
    if idade > maior :
        maior = idade
    if idade > 0 and menor == 0:
        menor = idade
    if idade > 0 and idade < menor :
        menor = idade
        
media = (menor + maior)/2 
print("Maior :", maior)
print("menor :", menor)
print("A média é :", media)
