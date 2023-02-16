import pandas as pd

x = pd.read_excel(r"C:\Users\Rafael.Almeida\Desktop\Aula\Alura\Python\Pandas\lendo_planilhas\teste.xlsx",
                  engine='openpyxl')

dados_filtrados = x['ID'] == 9  # >, =, < e etc..

print("tabela inteira:\n")
print(x)
print("\ntabela filtrada:\n")
print(dados_filtrados)
print("\ntabela filtrada apresentando os dados:\n")
print(x[dados_filtrados])
