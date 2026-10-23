def nested_sum(t):
    soma = 0

    for lista in t:
       soma+= sum (lista)

    return soma
t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
