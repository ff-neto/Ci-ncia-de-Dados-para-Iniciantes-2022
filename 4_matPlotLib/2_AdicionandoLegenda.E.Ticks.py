import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------------------------------
# Ler um arquivo texto (csv)
gas = pd.read_csv('/content/gas_prices.csv')
gas


# -----------------------------------------------------
# plot -> criar gráfico de linhas e comparar com três países
plt.title('Valor em combustivel em US$')

plt.plot(gas['Year'], gas['Australia'], label = 'Australia')
plt.plot(gas['Year'], gas['Italy'], label = 'Italy')
plt.plot(gas['Year'], gas['USA'], label = 'USA')

plt.xticks(gas['Year'][::2])

plt.legend()
plt.show()
