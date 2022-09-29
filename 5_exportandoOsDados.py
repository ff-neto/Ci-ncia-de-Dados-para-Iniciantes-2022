import pandas as pd

# -----------------------------------------------------
# Ler um arquivo texto (csv)
dados_csv = pd.read_csv('fifa/data.csv')

# -----------------------------------------------------
# Localizar dentro de dado: nacionalidade Brasileira
dados_csv.loc[dados_csv['Nationality'] == 'Bazil']

# Localizar dentro de dado: quantos jogadores com idade igual a 21
dados_csv.loc[dados_csv['Age'] == 21]


# -----------------------------------------------------
# Ordena em ordem cresente
dados_csv.sort_values('Name')

dados_csv.sort_values(['Name', 'Age'])

# Ordena em ordem decresente