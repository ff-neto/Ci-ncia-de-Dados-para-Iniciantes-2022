import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------
# Ler um arquivo texto (csv)
# df === data frame
df = pd.read_csv('/content/icecreamsales.csv')
df

# Conversão de Fahrenheit para Celsius
celsius = (df['Temperature'] - 32) * 5 / 9
df['Temperature'] = celsius
df

# Colocar temperatura em ordem
result = df.sort_values('Temperature', ascending = False)
result


# Criar o gráfico com todos os dados e salvar em pdf. 
plt.title('Ice cream Truck')

plt.ylabel('Sales (US$')
plt.xlabel('Temperatura (Celsius)')

plt.plot(result['Temperature'], result['Sales'], 'r.--', label = 'US$')

plt.legend()
plt.savefig('icecreamSales.pdf')
plt.show()

