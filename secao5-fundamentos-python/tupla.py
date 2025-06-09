tupla = tuple()
tupla = ()
type(tupla)
print(dir(tuple))
tupla = ('um')
print(type(tupla))
tupla = ('um',)
print(type(tupla))
# Estrutura indexada.
print(tupla[0])
# Não dá pra alterar objetos em uma tupla
# tupla[0] = 'novo'
cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.count('azul'))
print(len(cores))