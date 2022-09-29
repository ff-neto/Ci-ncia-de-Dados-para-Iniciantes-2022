import pandas as pd

# -----------------------------------------------------
# Ler um arquivo texto (csv)
dados_csv = pd.read_csv('fifa/data.csv')


# -----------------------------------------------------
"""
   Definir se o jogador é bom ou não:
   Aceleração somar com agilidade e somar com o tempo de reação
   O valor total vai definir se o jogador é bom ou não.
   Os maior valores o jogador é bom
   E o menores valores o jogador é ruim.
"""
# adiciona uma coluna no final e mostra a somatoria dos jogadores
dados_csv['total'] = dados_csv['Acceleration'] + dados_csv['Agility'] + dados_csv['Reactions']

# filtar o nome e o total
dados_csv = dados_csv[['Name', 'Total']]
dados_csv.sort_values('Total', ascending = False)
