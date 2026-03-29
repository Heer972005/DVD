import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")

addiction = df["addiction_level"].value_counts().sort_values()

plt.barh(addiction.index, 
         addiction.values, 
         color="orange",
         edgecolor="black",
         height=0.6)
plt.title("Addiction Level Distribution")
plt.xlabel("Count")
plt.ylabel("Addiction Level")

plt.show()

sns.countplot(y="addiction_level", 
              data=df, 
              order=df["addiction_level"].index,
              palette="coolwarm",
              edgecolor="black"
              )


plt.title("Addiction Levels")
plt.xlabel("Count")
plt.ylabel("Addiction Level")
plt.show()