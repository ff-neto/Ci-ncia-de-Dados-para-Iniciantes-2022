import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------------------------------
# Ler um arquivo texto (csv)
gas = pd.read_csv('/content/gas_prices.csv')
gas


# -----------------------------------------------------
# plot -> criar gráfico de linhas e comparar com três países
plt.plot(gas['Year'], gas['Australia'])
plt.plot(gas['Year'], gas['Italy'])
plt.plot(gas['Year'], gas['USA'])

plt.show()