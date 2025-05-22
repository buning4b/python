True or False
a = 7 != 3 and 2 > 3 # False, já que uma dos dois é falso.
print(a)

# Tabela verdade do AND
True and True # True
True and False # False
False and True # False
False and False # False
True and True and False and True # False

# Tabela verdade do OR 'or'
True or True # True
True or False # True
False or True # True
False or False # False
False or False or True or False # True

# Tabela do XOR !=
True != True # False
True != False # True
False != True # True
False != False # False 

# Operação de Negação (unário)
not True # False
not False # True
not 0 # True, já que 0 é false
not 1 # False, já que qualquer número != 0 é True

# Cuidado!
True & True
False | True
True ^ False

# AND Bit-a-Bit
# 3 = 11 
# 2 = 10
# _ = 10
print (3 & 2)

# OR Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 11
print(3 | 2)

# XOR Bit-a-Bit
# 3 = 11
# 2 = 10
# _ = 01
print(3 ^ 2)

# Um pouco de realidade. Operadores Bit-a-Bit NÃO pode ser usado quando está usando operadores lógicos
saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario

meta = saldo_positivo and despesas_controladas
print(meta)