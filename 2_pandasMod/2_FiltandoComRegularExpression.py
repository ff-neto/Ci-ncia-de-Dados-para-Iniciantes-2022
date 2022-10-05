import pandas as pd
import re

# -----------------------------------------------------
# Ler um arquivo texto (csv)
# df === data frame
df = pd.read_csv('pasta/data.csv')


# -----------------------------------------------------
# filtrar: 3 quartos e casa e abaixo de 500.000 dolars australiano
filter1 = df.loc[( df['Rooms'] == 3) & (df['Type'] == 'h') & (df['Price'] <= 500000) ]

filter1


# -----------------------------------------------------
# filtrar: a rua Turner st ou Turner rd (flags=re.I : filtrado em letras maiúsculas e minúsculas)
filter2 = df.loc[df['Address'].str.contains('Turner St| Turner Rd', flags=re.I)]

filter2