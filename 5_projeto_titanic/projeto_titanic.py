import pandas as pd

# -----------------------------------------------------
# Ler um arquivo texto (csv)
# df === data frame
titanic = pd.read_csv('/content/titanic.csv')

# definir a coluna: nome, idade, sexo, classe e sobreviveu
df = titanic[['Name', 'Age', 'Sex', 'Pclass', 'Survived']]

# filtrar  nome por ordem alfabética
df = df.sort_values(['Name'], ascending = True)

# filtrar: somente sexo feminino, classe somente 1º classe e se sobreviveu 
df = df.loc[(df['Sex'] == 'female') & (df['Pclass'] == 1) & (df['Survived'] == 1)]
df

# salvar o arquivo em csv
df.to_csv('titanic_result.csv', index = False)
