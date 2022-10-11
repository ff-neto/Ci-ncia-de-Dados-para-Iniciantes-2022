import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------------------------------
# Ler um arquivo texto (csv)
gas = pd.read_csv('/content/gas_prices.csv')
gas


# -----------------------------------------------------
# adicionando label e cores
plt.title('Price is US$')

plt.plot(gas['Year'], gas['Australia'], 'r.--', label = 'Australia')
plt.plot(gas['Year'], gas['Italy'], 'y.--', label = 'Italy')
plt.plot(gas['Year'], gas['USA'], 'b.--', label = 'USA')
plt.plot(gas['Year'], gas['Japan'], 'g.--', label = 'Japan')

plt.xticks(gas['Year'][::2])

plt.xlabel('Years')
plt.ylabel('US$')

plt.legend()
plt.show()