import pandas as pd

x = pd.read_excel(r"C:\Users\Rafael.Almeida\Desktop\Aula\Alura\Python\Pandas\lendo_planilhas\teste.xlsx")

# print(x)
print(x["Nome"][7])
