import pandas as pd

# Dicionario
d = {'Nome': ['Ana', 'Grazy', "Maria"], 'Idade': [20, 22, 38], "Altura": [1.56, 1.72, 1.78]}

dados = pd.DataFrame(data=d)

# print(dados)

# Convertendo para excel
dados.to_excel('dados.xls', index=False)
dados.to_excel('dados.xlsx', index=False)
