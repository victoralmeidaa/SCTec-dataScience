import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

sns.boxplot(x=df['age'])
plt.show()