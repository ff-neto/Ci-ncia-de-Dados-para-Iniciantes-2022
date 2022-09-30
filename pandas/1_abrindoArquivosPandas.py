import pandas as pd

# -----------------------------------------------------
# Ler um arquivo texto (csv)
dados_csv = pd.read_csv('pasta/data.csv')

dados_csv

# -----------------------------------------------------
# Ler um arquivo execel
dados_xlsx = pd.read_excel('pasta/data.xlsx')

dados_xlsx


# -----------------------------------------------------
# Ler uma página Web
dados_html = pd.read_html('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')

dados_html


# -----------------------------------------------------
# Ler um arquivo txt
dados_txt = pd.read_csv('pasta/data.txt', delimiter = '\t')

dados_txt
