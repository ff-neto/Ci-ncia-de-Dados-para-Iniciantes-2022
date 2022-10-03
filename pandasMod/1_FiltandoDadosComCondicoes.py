import pandas as pd

# -----------------------------------------------------
# Ler um arquivo texto (csv)
# df === data frame
df = pd.read_csv('pasta/data.csv')

df


# -----------------------------------------------------
# filtar: 3 quartos 
filter1 = df.loc[df['Rooms'] == 3]

filter1


# -----------------------------------------------------
# filtar: 3 quartos e casa
filter2 = df.loc[(df['Rooms'] == 3) & (df['Type'] == 'h')]

filter2