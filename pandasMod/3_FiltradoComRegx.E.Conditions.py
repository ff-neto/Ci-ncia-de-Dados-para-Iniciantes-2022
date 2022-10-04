import pandas as pd
import re

# -----------------------------------------------------
# Ler um arquivo texto (csv)
# df === data frame
df = pd.read_csv('pasta/data.csv')


# -----------------------------------------------------
# filtrar: a rua que começa em 59 e abaixo de 500.000 dolars australiano ('^59' ^: iniciar em...)
filter3 = df.loc[(df['Address'].str.contains('^59', flags=re.I)) & (df['Price'] <= 500000)]

filter3
