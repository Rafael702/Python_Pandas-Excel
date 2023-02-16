import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_excel(r"C:\Users\Rafael.Almeida\Desktop\Aula\Alura\Python\Pandas\lendo_planilhas\teste.xlsx")

# Grafico em Linha
# plt.plot(x["Nome"])

# Grafico em Histograma
# plt.hist("ID", bins= 20)

# Grafico em formato de pizza
plt.pie(x["ID"], labels=x["Nome"], autopct="%1.0f%%")

plt.show()

# print(x)
# print(x["Nome"][7])
