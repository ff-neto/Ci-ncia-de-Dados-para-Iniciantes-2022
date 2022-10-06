import pandas as pd

# -----------------------------------------------------
# Ler um arquivo texto (csv)
# df === data frame
df = pd.read_csv('pasta/data.csv')

df


# -----------------------------------------------------
# filtrar: por vendedor e tirar a média
df.groupby(['SellerG']).sum()


# -----------------------------------------------------
# filtrar: por vendedor e soma os valores baseado na coluna de preço e filtar do maior para o menor e selecionar os 10 melhores vendedores
df.groupby(['SellerG']).sum('Price').sort_values('Price', ascending = False).head(10)


# -----------------------------------------------------
# filtrar: por vendedor e soma os valores baseado na coluna de quartos e filtar do maior para o menor e selecionar os 10 melhores vendedores
df.groupby(['SellerG']).sum('Rooms').sort_values('Rooms', ascending = False).head(10)
