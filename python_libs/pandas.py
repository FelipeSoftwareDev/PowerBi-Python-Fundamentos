import pandas as pd

# 1. Carregar o dataset do Titanic a partir de um repositório público
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 2. Explorar os dados
print("Primeiras linhas do dataset:")
print(df.head())

print("\nInformações do dataset:")
print(df.info())

print("\nQuantidade de valores nulos por coluna:")
print(df.isnull().sum())

# 3. Tratamento dos dados incompletos

# a) Substituir valores ausentes na coluna 'Age' pela mediana
age_median = df['Age'].median()
df['Age'].fillna(age_median, inplace=True)
print("\nValores ausentes em 'Age' substituídos pela mediana:", age_median)

# b) Substituir valores ausentes na coluna 'Cabin' por 'Desconhecido'
df['Cabin'].fillna('Desconhecido', inplace=True)

# c) Substituir valores ausentes na coluna 'Embarked' pelo valor mais frequente (moda)
embarked_mode = df['Embarked'].mode()[0]
df['Embarked'].fillna(embarked_mode, inplace=True)
print("Valores ausentes em 'Embarked' substituídos pela moda:", embarked_mode)

# 4. Verificar novamente a quantidade de valores nulos
print("\nQuantidade de valores nulos após o tratamento:")
print(df.isnull().sum())

# Exibir as primeiras linhas do dataset após a limpeza
print("\nDataset após tratamento dos dados:")
print(df.head())
