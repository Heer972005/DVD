import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")
sns.pairplot(df, hue="addiction_level")
plt.show()