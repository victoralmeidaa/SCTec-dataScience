from pymongo import MongoClient
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
# Link de conecção localhost/porta 27027
uri = 'mongodb://localhost:27017/'

client = MongoClient(uri)

# Escolha o banco de dados para ser usado
db = client['mundotech']

# Coletar dados
collection = db['colecao_teste']

data = list(collection.find())

print(data)

df = pd.DataFrame(data)

print(f'Colunas disponeiveis no DataFrame: {df.columns.tolist()}')

sns.countplot(x='occupation',data=df)
plt.show()

client.close()