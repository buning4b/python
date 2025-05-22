# Desafio Operadores Lógicos

#Os Trabalhos
trabalho_terca = False
trabalho_quinta = False
'''
- Confirmando os 2: TV 50' + Sorvete
- Confirmando apenas 1 : TV 32' + Sorvete
- Nenhum confirmado: Fica em Casa
'''
TV_50 = trabalho_quinta and trabalho_terca
TV_32 = trabalho_terca != trabalho_quinta
Sorvete = trabalho_quinta or trabalho_terca
Casa = not Sorvete

print(f"TV50={TV_50} TV32={TV_32} SORVETE={Sorvete} CASA={Casa}")
