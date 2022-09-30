import pandas as pd

# -----------------------------------------------------
# Ler um arquivo texto (csv)
dados_csv = pd.read_csv('fifa/data.csv')

# -----------------------------------------------------
# Salvar os dados em csv e retirando o index
dados_csv.to_csv('dados1.csv', index = False)

# Salvar os dados em excel e retirando o index
dados_csv.to_excel('dados2.xlsx', index = False)

# Salvar os dados em txt. Retirando o index e colocando um delimitador(separador) para tab
dados_csv.to_csv('dados3.txt', index = False, sep='\t')
