a = {1, 2, 3}
print(type(a))
# a[0], conjunto não aceita índice
a = set('coddd3r')
print(a)
print('3' in a, 4 not in a)
print({ 1, 2, 3} == {3, 2, 1, 3})

# operações

c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2)) # Não muda nenhum conjunto
print(c1.update(c2))
print(c1)

c2 <= c1 # Subconjunto
c1 >= c2 # Superconjunto

print({1, 2, 3} - {2})
print(c1 - c2)
c1 -= {2}
print(c1)