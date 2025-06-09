from string import Template
nome, idade = 'Ana', 30

print('Nome: %s Idade: %d' % (nome, idade)) # mais antiga
print('Nome: {0} Idade: {1}'.format(nome, idade)) # python < 3.6
print(f'Nome: {nome} Idade: {idade} {2 ** 8 + 1}') # python >= 3.6

s = Template('Nome: $n Idade: $i')
print(s.substitute(n=nome, i=idade))