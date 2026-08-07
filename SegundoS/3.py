def classifica_idade(idade):
    if idade>=60:
        return 'idoso'
    elif  idade>=18:
        return 'adulto'
    elif idade>=12:
        return 'adolescente'
    else :  
        return 'criança'
idade = int(input("Informe a idade"))
print(classifica_idade(idade))









#def classifica_idade(idade):
    #if idade>12:
        #return 'criança'
    #elif  idade>=12 and idade<=17:
        #return 'adolecente'
    #elif idade>=18 and idade<=59:
        #return 'adulto'
    #else :  
        #return 'idoso'
#idade = int(input("Informe a idade"))
#print(classifica_idade(idade))