nome = 'Ana Paula'
# Acessando os elementos do nome
print(nome[0])
print(nome[6])
print(nome[-3])
print(nome[4:])  # significa que eu quero do quarto elemento em diante do nome.
print(nome[-5:])  # também funcina com numero negativo
# Significa que o índice final (3 que seria o Espaço), será desconsiderado, pegando o indice 0,1,2.
print(nome[:3])
# Pegando do índice 2 - 4 (não pegará o ultimo elemento)
print(nome[2:5])

numero = '1234567890'
print(numero)
print(numero[::])
print(numero[::2]) #vai pegando o numero de 2 em 2
print(numero[::2]) # vai pegando do numero 1 e vai pulando de 2 em 2
print(numero[::-1]) # faz a str de forma contrária
print(numero[::-2]) # vai pegando o numero de forma contrária pegando 2 em 2

print(nome[::-1])
