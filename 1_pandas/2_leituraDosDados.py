import pandas as pd

# -----------------------------------------------------
# Ler um arquivo texto (csv)
dados_csv = pd.read_csv('fifa/data.csv')

dados_csv


# -----------------------------------------------------
# Mostrar as primeiras seção dos dados. Mostra os 5 primeiros dados
dados_csv.head()

# Mostra os 2 primeiros dados
dados_csv.head(2)


# -----------------------------------------------------
# Mostrar os últimos seção dos dados. Mostra os 5 últimos dados
dados_csv.tail()

# Mostra os 8 últimos dados
dados_csv.tail(8)


# -----------------------------------------------------
# Mostrar todas as colunas da tabela
dados_csv.columns


# -----------------------------------------------------
# Mostrar todas as linhas da tabela
dados_csv.index


# -----------------------------------------------------
# filtar uma coluna 
dados_csv['Name']

# filtar várias coluna
dados_csv[['Name', 'Wage','Nationality']]
