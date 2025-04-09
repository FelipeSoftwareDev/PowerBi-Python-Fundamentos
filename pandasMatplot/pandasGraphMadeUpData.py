import matplotlib.pyplot as plt
import pandas as pd

# Criando um conjunto de dados fictício
dados = {'Vendas': [100, 200, 300, 400, 500],
         'Lucro': [20, 40, 70, 100, 130]}

df = pd.DataFrame(dados)

# Criando o gráfico
plt.figure(figsize=(6,4))
plt.scatter(df['Vendas'], df['Lucro'], color='blue', label='Lucro por Venda')
plt.xlabel('Vendas')
plt.ylabel('Lucro')
plt.title('Relação entre Vendas e Lucro')
plt.legend()
plt.grid(True)

# Exibir no Power BI
plt.show()
