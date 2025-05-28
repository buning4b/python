# Como acessar os elementos de uma lista
lista = [1, 5, 'Rebeca', 'Guilherme', 3.14]  # Lista é uma estrutura indexada.
# Vai dizer qual a posição do item dentro da lista.
print(lista.index('Guilherme'))
# print(lista.index(42)) Quando o elemento não tá na lista, gerará um erro.
print(lista[2])
print(1 in lista)
print('Rebeca' in lista)
print('Pedro' not in lista)
print(lista[0])
print(lista[4])
# print(lista[5])
print(lista[-1])
print(lista[-5])