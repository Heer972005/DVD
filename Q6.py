import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Smartphone_Usage_And_Addiction_Analysis_7500_Rows-2.csv")
bins = [15, 26, 36, 51, 100]
labels = ["Youth", "Young Adults", "Adults", "Senior Citizens"]

df["Age Group"] = pd.cut(df["age"], bins=bins, labels=labels)

sns.violinplot(x="Age Group",
               y="daily_screen_time_hours",
               data=df,
               palette="Pastel1",
               inner="quartile" )
plt.title("Density Distribution of Smartphone Usage by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Screen Time (hours)")

plt.xticks(rotation=20)
plt.show()