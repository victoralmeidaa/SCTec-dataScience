from pymongo import MongoClient
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

uri = 'mongodb://localhost:27017/'

client = MongoClient(uri)

db = client['db_car']
collection = db['Carros']
data = list(collection.find())
print(data)

df = pd.DataFrame(data)
print(f'Colunas disponiveis no DF: {df.columns.tolist()}')

sns.countplot(x='Marca',data=df)
plt.show()

client.close()
