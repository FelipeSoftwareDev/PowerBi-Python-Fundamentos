import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

df['Age'].fillna(df['Age'].median(), inplace=True)

survival_counts = df.groupby(['Sex', 'Survived']).size().unstack()

survival_counts.columns = ['Não Sobreviveu', 'Sobreviveu']

plt.figure(figsize=(8,6))
survival_counts.plot(kind='bar', color=['salmon', 'skyblue'])
plt.title("Taxa de Sobrevivência no Titanic por Sexo")
plt.xlabel("Sexo")
plt.ylabel("Contagem")
plt.legend(title="Status de Sobrevivência")
plt.tight_layout()
plt.show()

