print("=== Hipermercado Tabajara ===")


#Tabela de opções
print("--Tipos de carne--")
print("--1 - Filé Duplo--")
print("--2 - Alcatra--")
print("--3 - Picanha--")


tipo = int(input("Escolha o tipo de carne (1/2/3): "))
quantidade = float(input("Digite a quantidade (kg): "))
pagamento = input("O pagamento será no cartão Tabajara ? (S/N) :").upper()


if tipo == 1:
    nome_carne = "Filé Duplo"
    if quantidade <= 5:
        preço_kg = 24.90
    else:
        preço_kg = 25.80

elif tipo == 2:
    nome_carne = "Alcatra"
    if quantidade <= 5:
        preço_kg = 25.90
    else:
        preço_kg = 26.80

elif tipo == 3:
    nome_carne = "Picanha"
    if quantidade <= 5:
        preço_kg = 46.90
    else: 
        preço_kg = 37.80
else:
    print("Tipo inválido!")
    exit()

# Cálculo total
total = quantidade * preço_kg

# Desconto
if pagamento == "S":
    desconto = total * 0.05
    tipo_pagamento = "Cartão Tabajara"
else:
    desconto = 0
    tipo_pagamento = "Dinheiro/Outro"


valor_final = total - desconto


# Cupom fiscal
print("\n=== CUPOM FISCAL ===")
print(f"Tipo de carne: {nome_carne}")
print(f"Quantidade: {quantidade:.2f} Kg")
print(f"Preço total: R$ {total:.2f}")
print(f"Tipo de pagamento: {tipo_pagamento}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")
print("========================")

