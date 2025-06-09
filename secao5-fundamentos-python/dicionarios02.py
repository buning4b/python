# Alterações de dados
pessoa = {'nome': 'Prof.Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44 # Atualiza o valor do dicionario
pessoa['cursos'].append('Angular') #Adiciona um valor a chave de um dicionario
print(pessoa)
pessoa.pop('idade') # Remove uma chave e valor do dicionario
print(pessoa)
pessoa.update({'idade': 40, 'sexo': 'M'}) # Adiciona uma chave - valor ao dicionário
print(pessoa)
del pessoa['cursos'] # Idem pop
print(pessoa)
pessoa.clear() # Remove tudo da lista
print(pessoa)