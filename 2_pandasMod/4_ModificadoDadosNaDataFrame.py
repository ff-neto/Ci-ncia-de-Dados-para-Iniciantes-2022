import pandas as pd

# -----------------------------------------------------
# Ler um arquivo texto (csv)
# df === data frame
df = pd.read_csv('pasta/data.csv')

df


# -----------------------------------------------------
# filtrar: um vendedor 
vendedor = df.loc[df['SellerG'] == 'Nelson']

vendedor


# -----------------------------------------------------
# trocar de nome do vendendor 
df.loc[df['SellerG'] == 'Nelson', 'SellerG'] = 'Ronald'

df


# -----------------------------------------------------
# filtrar: achar o vendedor Ronald e trocar o método S para pendente
df.loc[(df['SellerG'] == 'Ronald', ['Method'])] = 'Pending'

df