import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

addiction = df["addiction_level"].value_counts().sort_values()

plt.barh(addiction.index, addiction.values, color="orange")
plt.title("Addiction Level Distribution")
plt.show()

sns.countplot(y="addiction_level", data=df, order=df["addiction_level"].value_counts().index)

plt.title("Addiction Levels")
plt.show()