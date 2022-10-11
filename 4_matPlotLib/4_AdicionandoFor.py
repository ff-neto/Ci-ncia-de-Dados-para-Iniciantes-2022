import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------------------------------
# Ler um arquivo texto (csv)
gas = pd.read_csv('/content/gas_prices.csv')
gas


# -----------------------------------------------------
plt.title('Price is US$')

listCountry = ['Australia', 'USA', 'Italy', 'Mexico', 'France', 'Germany']

for country in gas:
  if country in listCountry:
    plt.plot(gas['Year'], gas[country], label=[country], marker='.')

plt.xticks(gas['Year'][::2])

plt.xlabel('Years')
plt.ylabel('US$')

plt.legend()
plt.show()