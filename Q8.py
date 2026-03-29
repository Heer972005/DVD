import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")
bins=[15, 25, 35, 50, 100]
labels = ["Youth", "Young Adults", "Adults", "Senior Citizens"]
df["Age Group"]=pd.cut(df["age"],bins=bins,labels=labels)
group = df.groupby("Age Group")["daily_screen_time_hours"].sum()

plt.stackplot(group.index, group.values)

plt.title("Contribution by Age Group")
plt.show()