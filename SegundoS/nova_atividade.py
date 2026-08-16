# Base de dados (Escopo global do script)
def get_estoque():
  estoque = [
    {"id": 1, "nome": "Notebook", "preco": 3500.0, "qtd": 5},
    {"id": 2, "nome": "Mouse", "preco": 80.0, "qtd": 15},
    {"id": 3, "nome": "Teclado", "preco": 150.0, "qtd": 10}
  ]
  return estoque

print(get_estoque())
