import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

pivot_table = titanic_df.pivot_table(index='Pclass',columns='Survived',values='Fare',aggfunc=np.mean)
sns.heatmap(pivot_table,fmt='.2f',cmap='viridis',annot=True)
plt.title("Heatmap")
plt.show()